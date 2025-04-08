def modify_content(text):
   return text.upper()

try:
    input_file = input("Enter the name of the file to read: ")

    
    with open(input_file, "r") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Write the modified content to a new file
    output_file = "modified_" + input_file
    with open(output_file, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified content has been written to '{output_file}'.")

except FileNotFoundError:
    print("❌ Error: The file you entered was not found.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
