import subprocess
import os
import threading

def find_executable(exec_name):
    """Search for the executable in the current directory."""
    for root, dirs, files in os.walk(os.getcwd()):
        if exec_name in files:
            return os.path.join(root, exec_name)
    return None

def monitor_output(process, counter):
    """Monitor the output of the scraper and update the counter for each business."""
    while True:
        line = process.stdout.readline()
        if not line:  # If no more output, break the loop
            break
        print(line.strip())  # Print the scraper's output to console
        counter['count'] += 1
        print(f"Businesses scraped: {counter['count']}")  # Print the updated count

def start_google_maps_scraper(input_file, results_file, email=True):
    exec_path = find_executable('google-maps-scraper')
    if exec_path is None:
        print("The google-maps-scraper executable was not found in the current directory.")
        return
    
    command = [exec_path, '-input', input_file, '-results', results_file]
    
    if email:
        command.append('-email')
    
    try:
        # Start the scraper process and capture its standard output
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Create a shared counter
        counter = {'count': 0}
        
        # Start a thread to monitor the scraper's output
        output_thread = threading.Thread(target=monitor_output, args=(process, counter))
        output_thread.start()
        
        # Wait for the process to complete
        process.wait()
        
        # Wait for the output monitoring thread to finish
        output_thread.join()
        
        print(f"Google Maps Scraper completed. Total businesses scraped: {counter['count']}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while starting the Google Maps Scraper: {e}")

if __name__ == "__main__":
    input_file_name = 'example-queries.txt'
    input_file_path = os.path.join(os.getcwd(), input_file_name)
    
    if not os.path.exists(input_file_path):
        print(f"The input file '{input_file_name}' does not exist in the current directory.")
    else:
        results_file_path = os.path.join(os.getcwd(), 'results.csv')
        start_google_maps_scraper(input_file_path, results_file_path)
