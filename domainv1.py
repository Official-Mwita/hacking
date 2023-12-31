import subprocess

def run_dig(domain):
    try:
        command = f"dig @1.1.1.1 {domain} CNAME"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error while running dig for {domain}: {e}")
        return None

def check_cname_output(output):
    return "ns-422.awsdns-52.com. awsdns-hostmaster.amazon.com" in output

def main():
    filename = "dm.txt"  # Replace with the path to your file containing the list of domains
    domains_without_cname = []

    try:
        with open(filename, "r") as file:
            domains = file.read().splitlines()

        for domain in domains:
            output = run_dig(domain)
            if output and not check_cname_output(output):
                domains_without_cname.append(domain)

        print("Domains without the specified CNAME:")
        for domain in domains_without_cname:
            print(domain)

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
