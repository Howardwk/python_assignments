import os

def read_and_modify_file():
    # Prompt the user for the file path
    file_path = input("Enter the filename to read: ")

    try:
        # Read and display the file content
        with open(file_path, "r") as file:
            content = file.read()
        print("File content:\n", content)

        # Prompt the user for information to append
        user_input = input("Enter the information you wish to append: ")

        # Append the user's input to the same file
        with open(file_path, "a") as file:
            file.write(user_input + "\n")

        print(f"File processed successfully! Your input appended to '{file_path}'.")

    except FileNotFoundError:
        print("❌ Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Execute the function
read_and_modify_file()