import socket

def is_domain_not_found(domain):
    try:
        socket.gethostbyname(domain)
        return False
    except socket.gaierror:
        return True

def check_domains_not_found(input_file):
    not_found_domains = []

    with open(input_file, "r") as infile:
        domains = infile.read().splitlines()

    for domain in domains:
        if is_domain_not_found(domain):
            not_found_domains.append(domain)

    return not_found_domains

if __name__ == "__main__":
    input_file = "dm1.txt"  # Replace with the path to your input file

    not_found_domains = check_domains_not_found(input_file)

    print("Domains not found:")
    for domain in not_found_domains:
        print(domain)
