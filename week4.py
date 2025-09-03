def modify_content(content):
    # Example modification: convert all text to uppercase
    return content.upper()

def main():
    try:
        # Ask user for the input filename
        input_file = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_file, 'r') as file:
            original_content = file.read()

        # Modify the content
        modified_content = modify_content(original_content)

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content written to '{output_file}' successfully.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()