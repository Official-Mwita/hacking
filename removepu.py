def remove_duplicates(input_file, output_file):
    unique_lines = set()

    with open(input_file, "r") as infile:
        for line in infile:
            line = line.strip()
            if line not in unique_lines:
                unique_lines.add(line)

    with open(output_file, "w") as outfile:
        for line in unique_lines:
            outfile.write(line + "\n")

if __name__ == "__main__":
    input_file = "input.txt"    # Replace with the path to your input file
    output_file = "dm1.txt"  # Replace with the desired output file path

    remove_duplicates(input_file, output_file)
