import subprocess

def run_nmap(ip_file_path, output_file_path):
    with open(ip_file_path, 'r') as ip_file:
        ip_list = ip_file.read().splitlines()

    for ip in ip_list:
        cmd = f'nmap -sV -A -p- {ip}'
        try:
            # Run Nmap and capture the output done hear
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            output = result.stdout

            # Save the output to the specified file
            with open(output_file_path, 'a') as output_file:
                output_file.write(f"Scanning IP: {ip}\n")
                output_file.write(output)
                output_file.write("\n\n")
#hova
            print(f"Scan completed for IP: {ip}")
        except Exception as e:
            print(f"Error while scanning IP: {ip}")
            print(e)

if __name__ == "__main__":
    # Replace 'input_ips.txt' with the path to your input file containing the IP addresses
    # Replace 'output.txt' with the path where you want to save the output
    run_nmap('input_ips.txt', 'output.txt')
