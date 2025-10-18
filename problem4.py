
import os

def list_directory(path='/ Users'):
    """
    Prints the contents (files + subdirectories) of the given directory path.
    If no path is given, uses the current working directory.
    """
    try:
        entries = os.listdir(path)        # list all entries
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")
        return
    except OSError as e:
        print(f"OS error while listing directory '{path}': {e}")
        return

    print(f"Contents of directory '{path}':")
    for name in entries:
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            print(f"[DIR]  {name}")
        else:
            print(f"[FILE] {name}")

if __name__ == "__main__":
    # Example usage
    dir_to_list = input("Enter directory path (or press Enter for current directory): ").strip()
    if not dir_to_list:
        dir_to_list = '.'
    list_directory(dir_to_list)
