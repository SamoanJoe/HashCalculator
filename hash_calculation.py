# # # # # # # # # # # # import os
# # # # # # # # # # # # from hashlib import sha256, md5
# # # # # # # # # # # # path = input("Please give me the whole path including file name: ")

# # # # # # # # # # # # print("SHA256: " + sha256(path.encode('utf-8')).hexdigest())
# # # # # # # # # # # # print("Md5: " + md5(path.encode('utf-8')).hexdigest())

# # # # # # # # # # # import os
# # # # # # # # # # # from hashlib import sha256, md5

# # # # # # # # # # # def calculate_hashes(directory):
# # # # # # # # # # #     # Check if the provided path is a directory
# # # # # # # # # # #     if not os.path.isdir(directory):
# # # # # # # # # # #         print(f"The path '{directory}' is not a directory.")
# # # # # # # # # # #         return

# # # # # # # # # # #     # Iterate through all files in the directory
# # # # # # # # # # #     for filename in os.listdir(directory):
# # # # # # # # # # #         filepath = os.path.join(directory, filename)

# # # # # # # # # # #         # Check if the current item is a file
# # # # # # # # # # #         if os.path.isfile(filepath):
# # # # # # # # # # #             print(f"File: {filename}")

# # # # # # # # # # #             # Calculate and print SHA256 hash
# # # # # # # # # # #             sha256_hash = sha256()
# # # # # # # # # # #             with open(filepath, "rb") as file:
# # # # # # # # # # #                 # Read the file in chunks to avoid memory issues with large files
# # # # # # # # # # #                 for chunk in iter(lambda: file.read(4096), b""):
# # # # # # # # # # #                     sha256_hash.update(chunk)
# # # # # # # # # # #             print(f"  SHA256: {sha256_hash.hexdigest()}")

# # # # # # # # # # #             # Calculate and print MD5 hash
# # # # # # # # # # #             md5_hash = md5()
# # # # # # # # # # #             with open(filepath, "rb") as file:
# # # # # # # # # # #                 for chunk in iter(lambda: file.read(4096), b""):
# # # # # # # # # # #                     md5_hash.update(chunk)
# # # # # # # # # # #             print(f"  MD5: {md5_hash.hexdigest()}")
# # # # # # # # # # #             print()

# # # # # # # # # # # # Get the directory path from the user
# # # # # # # # # # # directory_path = input("Please provide the directory path: ")
# # # # # # # # # # # calculate_hashes(directory_path)

# # # # # # # # # # import os
# # # # # # # # # # import tkinter as tk
# # # # # # # # # # from tkinter import filedialog
# # # # # # # # # # from hashlib import sha256, md5

# # # # # # # # # # def calculate_hashes(directory):
# # # # # # # # # #     if not os.path.isdir(directory):
# # # # # # # # # #         result_label.config(text=f"The path '{directory}' is not a directory.")
# # # # # # # # # #         return

# # # # # # # # # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # # # # # # # # #     for filename in os.listdir(directory):
# # # # # # # # # #         filepath = os.path.join(directory, filename)
# # # # # # # # # #         if os.path.isfile(filepath):
# # # # # # # # # #             result_text.insert(tk.END, f"File: {filename}\n")

# # # # # # # # # #             sha256_hash = sha256()
# # # # # # # # # #             with open(filepath, "rb") as file:
# # # # # # # # # #                 for chunk in iter(lambda: file.read(4096), b""):
# # # # # # # # # #                     sha256_hash.update(chunk)
# # # # # # # # # #             result_text.insert(tk.END, f"  SHA256: {sha256_hash.hexdigest()}\n")

# # # # # # # # # #             md5_hash = md5()
# # # # # # # # # #             with open(filepath, "rb") as file:
# # # # # # # # # #                 for chunk in iter(lambda: file.read(4096), b""):
# # # # # # # # # #                     md5_hash.update(chunk)
# # # # # # # # # #             result_text.insert(tk.END, f"  MD5: {md5_hash.hexdigest()}\n\n")

# # # # # # # # # # # Function to open file dialog and get directory path
# # # # # # # # # # def browse_directory():
# # # # # # # # # #     directory_path = filedialog.askdirectory()
# # # # # # # # # #     directory_entry.delete(0, tk.END)
# # # # # # # # # #     directory_entry.insert(0, directory_path)

# # # # # # # # # # # GUI setup
# # # # # # # # # # root = tk.Tk()
# # # # # # # # # # root.title("File Hash Calculator")

# # # # # # # # # # # Entry for directory path
# # # # # # # # # # directory_label = tk.Label(root, text="Enter Directory:")
# # # # # # # # # # directory_label.pack(pady=5)

# # # # # # # # # # directory_entry = tk.Entry(root, width=40)
# # # # # # # # # # directory_entry.pack(pady=5)

# # # # # # # # # # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # # # # # # # # # browse_button.pack(pady=10)

# # # # # # # # # # # Button to calculate hashes
# # # # # # # # # # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get()))
# # # # # # # # # # calculate_button.pack(pady=10)

# # # # # # # # # # # Result display
# # # # # # # # # # result_label = tk.Label(root, text="")
# # # # # # # # # # result_label.pack(pady=5)

# # # # # # # # # # result_text = tk.Text(root, width=50, height=15)
# # # # # # # # # # result_text.pack(pady=10)

# # # # # # # # # # root.mainloop()

# # # # # # # # # import os
# # # # # # # # # import tkinter as tk
# # # # # # # # # from tkinter import filedialog
# # # # # # # # # from hashlib import sha256, md5
# # # # # # # # # from datetime import datetime

# # # # # # # # # def calculate_hashes(directory, log_file):
# # # # # # # # #     if not os.path.isdir(directory):
# # # # # # # # #         result_label.config(text=f"The path '{directory}' is not a directory.")
# # # # # # # # #         return

# # # # # # # # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # # # # # # # #     # Open the logfile in append mode
# # # # # # # # #     with open(log_file, "a") as logfile:
# # # # # # # # #         # Log the date and time
# # # # # # # # #         logfile.write(f"\n\nLog Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
# # # # # # # # #         logfile.write(f"Directory: {directory}\n")

# # # # # # # # #         for filename in os.listdir(directory):
# # # # # # # # #             filepath = os.path.join(directory, filename)
# # # # # # # # #             if os.path.isfile(filepath):
# # # # # # # # #                 result_text.insert(tk.END, f"File: {filename}\n")
# # # # # # # # #                 logfile.write(f"\nFile: {filename}\n")

# # # # # # # # #                 sha256_hash = sha256()
# # # # # # # # #                 with open(filepath, "rb") as file:
# # # # # # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # # # # # #                         sha256_hash.update(chunk)
# # # # # # # # #                 hash_value = sha256_hash.hexdigest()
# # # # # # # # #                 result_text.insert(tk.END, f"  SHA256: {hash_value}\n")
# # # # # # # # #                 logfile.write(f"  SHA256: {hash_value}\n")

# # # # # # # # #                 md5_hash = md5()
# # # # # # # # #                 with open(filepath, "rb") as file:
# # # # # # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # # # # # #                         md5_hash.update(chunk)
# # # # # # # # #                 hash_value = md5_hash.hexdigest()
# # # # # # # # #                 result_text.insert(tk.END, f"  MD5: {hash_value}\n\n")
# # # # # # # # #                 logfile.write(f"  MD5: {hash_value}\n\n")

# # # # # # # # # # Function to open file dialog and get directory path
# # # # # # # # # def browse_directory():
# # # # # # # # #     directory_path = filedialog.askdirectory()
# # # # # # # # #     directory_entry.delete(0, tk.END)
# # # # # # # # #     directory_entry.insert(0, directory_path)

# # # # # # # # # # Function to open file dialog and get logfile path
# # # # # # # # # def browse_logfile():
# # # # # # # # #     logfile_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
# # # # # # # # #     logfile_entry.delete(0, tk.END)
# # # # # # # # #     logfile_entry.insert(0, logfile_path)

# # # # # # # # # # GUI setup
# # # # # # # # # root = tk.Tk()
# # # # # # # # # root.title("File Hash Calculator")

# # # # # # # # # # Entry for directory path
# # # # # # # # # directory_label = tk.Label(root, text="Enter Directory:")
# # # # # # # # # directory_label.pack(pady=5)

# # # # # # # # # directory_entry = tk.Entry(root, width=40)
# # # # # # # # # directory_entry.pack(pady=5)

# # # # # # # # # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # # # # # # # # browse_button.pack(pady=10)

# # # # # # # # # # Entry for logfile path
# # # # # # # # # logfile_label = tk.Label(root, text="Save Log to File:")
# # # # # # # # # logfile_label.pack(pady=5)

# # # # # # # # # logfile_entry = tk.Entry(root, width=40)
# # # # # # # # # logfile_entry.pack(pady=5)

# # # # # # # # # logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# # # # # # # # # logfile_button.pack(pady=10)

# # # # # # # # # # Button to calculate hashes
# # # # # # # # # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get(), logfile_entry.get()))
# # # # # # # # # calculate_button.pack(pady=10)

# # # # # # # # # # Result display
# # # # # # # # # result_label = tk.Label(root, text="")
# # # # # # # # # result_label.pack(pady=5)

# # # # # # # # # result_text = tk.Text(root, width=50, height=15)
# # # # # # # # # result_text.pack(pady=10)

# # # # # # # # # root.mainloop()
# # # # # # # # import os
# # # # # # # # import tkinter as tk
# # # # # # # # from tkinter import filedialog
# # # # # # # # from hashlib import sha256, md5
# # # # # # # # from datetime import datetime

# # # # # # # # def calculate_hashes(directory, log_file):
# # # # # # # #     if not os.path.isdir(directory):
# # # # # # # #         result_label.config(text=f"The path '{directory}' is not a directory.")
# # # # # # # #         return

# # # # # # # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # # # # # # #     # Open the logfile in append mode
# # # # # # # #     with open(log_file, "a") as logfile:
# # # # # # # #         # Log the date and time
# # # # # # # #         logfile.write(f"\n\nLog Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
# # # # # # # #         logfile.write(f"Directory: {directory}\n")

# # # # # # # #         for filename in os.listdir(directory):
# # # # # # # #             filepath = os.path.join(directory, filename)
# # # # # # # #             if os.path.isfile(filepath):
# # # # # # # #                 result_text.insert(tk.END, f"File: {filename}\n")
# # # # # # # #                 logfile.write(f"\nFile: {filename}\n")

# # # # # # # #                 sha256_hash = sha256()
# # # # # # # #                 with open(filepath, "rb") as file:
# # # # # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # # # # #                         sha256_hash.update(chunk)
# # # # # # # #                 hash_value = sha256_hash.hexdigest()
# # # # # # # #                 result_text.insert(tk.END, f"  SHA256: {hash_value}\n")
# # # # # # # #                 logfile.write(f"  SHA256: {hash_value}\n")

# # # # # # # #                 md5_hash = md5()
# # # # # # # #                 with open(filepath, "rb") as file:
# # # # # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # # # # #                         md5_hash.update(chunk)
# # # # # # # #                 hash_value = md5_hash.hexdigest()
# # # # # # # #                 result_text.insert(tk.END, f"  MD5: {hash_value}\n\n")
# # # # # # # #                 logfile.write(f"  MD5: {hash_value}\n\n")

# # # # # # # # # Function to open file dialog and get directory path
# # # # # # # # def browse_directory():
# # # # # # # #     directory_path = filedialog.askdirectory()
# # # # # # # #     directory_entry.delete(0, tk.END)
# # # # # # # #     directory_entry.insert(0, directory_path)

# # # # # # # # # Function to open file dialog and get logfile path
# # # # # # # # def browse_logfile():
# # # # # # # #     default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", "hash_log.txt")
# # # # # # # #     logfile_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], initialfile=default_logfile_path)
# # # # # # # #     logfile_entry.delete(0, tk.END)
# # # # # # # #     logfile_entry.insert(0, logfile_path)

# # # # # # # # # GUI setup
# # # # # # # # root = tk.Tk()
# # # # # # # # root.title("File Hash Calculator")

# # # # # # # # # Entry for directory path
# # # # # # # # directory_label = tk.Label(root, text="Enter Directory:")
# # # # # # # # directory_label.pack(pady=5)

# # # # # # # # directory_entry = tk.Entry(root, width=40)
# # # # # # # # directory_entry.pack(pady=5)

# # # # # # # # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # # # # # # # browse_button.pack(pady=10)

# # # # # # # # # Entry for logfile path
# # # # # # # # logfile_label = tk.Label(root, text="Save Log to File:")
# # # # # # # # logfile_label.pack(pady=5)

# # # # # # # # default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", "hash_log.log")
# # # # # # # # logfile_entry = tk.Entry(root, width=40)
# # # # # # # # logfile_entry.insert(0, default_logfile_path)
# # # # # # # # logfile_entry.pack(pady=5)

# # # # # # # # logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# # # # # # # # logfile_button.pack(pady=10)

# # # # # # # # # Button to calculate hashes
# # # # # # # # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get(), logfile_entry.get()))
# # # # # # # # calculate_button.pack(pady=10)

# # # # # # # # # Result display
# # # # # # # # result_label = tk.Label(root, text="")
# # # # # # # # result_label.pack(pady=5)

# # # # # # # # result_text = tk.Text(root, width=50, height=15)
# # # # # # # # result_text.pack(pady=10)

# # # # # # # # root.mainloop()

# # # # # # # import os
# # # # # # # import tkinter as tk
# # # # # # # from tkinter import filedialog
# # # # # # # from hashlib import sha256, md5
# # # # # # # from datetime import datetime

# # # # # # # def calculate_hashes(directory, log_file):
# # # # # # #     if not os.path.isdir(directory):
# # # # # # #         result_label.config(text=f"The path '{directory}' is not a directory.")
# # # # # # #         return

# # # # # # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # # # # # #     # Open the logfile in append mode
# # # # # # #     with open(log_file, "a") as logfile:
# # # # # # #         # Log the date and time
# # # # # # #         log_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# # # # # # #         logfile.write(f"\n\nLog Entry Date and Time: {log_timestamp}\n")
# # # # # # #         logfile.write(f"Directory: {directory}\n")

# # # # # # #         for filename in os.listdir(directory):
# # # # # # #             filepath = os.path.join(directory, filename)
# # # # # # #             if os.path.isfile(filepath):
# # # # # # #                 result_text.insert(tk.END, f"File: {filename}\n")
# # # # # # #                 logfile.write(f"\nFile: {filename}\n")

# # # # # # #                 sha256_hash = sha256()
# # # # # # #                 with open(filepath, "rb") as file:
# # # # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # # # #                         sha256_hash.update(chunk)
# # # # # # #                 hash_value = sha256_hash.hexdigest()
# # # # # # #                 result_text.insert(tk.END, f"  SHA256: {hash_value}\n")
# # # # # # #                 logfile.write(f"  SHA256: {hash_value}\n")

# # # # # # #                 md5_hash = md5()
# # # # # # #                 with open(filepath, "rb") as file:
# # # # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # # # #                         md5_hash.update(chunk)
# # # # # # #                 hash_value = md5_hash.hexdigest()
# # # # # # #                 result_text.insert(tk.END, f"  MD5: {hash_value}\n\n")
# # # # # # #                 logfile.write(f"  MD5: {hash_value}\n\n")

# # # # # # # # Function to open file dialog and get directory path
# # # # # # # def browse_directory():
# # # # # # #     directory_path = filedialog.askdirectory()
# # # # # # #     directory_entry.delete(0, tk.END)
# # # # # # #     directory_entry.insert(0, directory_path)

# # # # # # # # Function to open file dialog and get logfile path
# # # # # # # def browse_logfile():
# # # # # # #     default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", "hash_log.txt")
# # # # # # #     logfile_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], initialfile=default_logfile_path)
# # # # # # #     logfile_entry.delete(0, tk.END)
# # # # # # #     logfile_entry.insert(0, logfile_path)

# # # # # # # # GUI setup
# # # # # # # root = tk.Tk()
# # # # # # # root.title("File Hash Calculator")

# # # # # # # # Entry for directory path
# # # # # # # directory_label = tk.Label(root, text="Enter Directory:")
# # # # # # # directory_label.pack(pady=5)

# # # # # # # directory_entry = tk.Entry(root, width=40)
# # # # # # # directory_entry.pack(pady=5)

# # # # # # # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # # # # # # browse_button.pack(pady=10)

# # # # # # # # Entry for logfile path
# # # # # # # logfile_label = tk.Label(root, text="Save Log to File:")
# # # # # # # logfile_label.pack(pady=5)

# # # # # # # default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", "hash_log.txt")
# # # # # # # logfile_entry = tk.Entry(root, width=40)
# # # # # # # logfile_entry.insert(0, default_logfile_path)
# # # # # # # logfile_entry.pack(pady=5)

# # # # # # # logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# # # # # # # logfile_button.pack(pady=10)

# # # # # # # # Button to calculate hashes
# # # # # # # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get(), logfile_entry.get()))
# # # # # # # calculate_button.pack(pady=10)

# # # # # # # # Result display
# # # # # # # result_label = tk.Label(root, text="")
# # # # # # # result_label.pack(pady=5)

# # # # # # # result_text = tk.Text(root, width=50, height=15)
# # # # # # # result_text.pack(pady=10)

# # # # # # # root.mainloop()

# # # # # # import os
# # # # # # import tkinter as tk
# # # # # # from tkinter import filedialog
# # # # # # from hashlib import sha256, md5
# # # # # # from datetime import datetime

# # # # # # def calculate_hashes(directory, log_file):
# # # # # #     if not os.path.isdir(directory):
# # # # # #         result_label.config(text=f"The path '{directory}' is not a directory.")
# # # # # #         return

# # # # # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # # # # #     # Open the logfile in append mode
# # # # # #     with open(log_file, "a") as logfile:
# # # # # #         # Log the date and time
# # # # # #         log_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# # # # # #         logfile.write(f"\n\nLog Entry Date and Time: {log_timestamp}\n")
# # # # # #         logfile.write(f"Directory: {directory}\n")

# # # # # #         for filename in os.listdir(directory):
# # # # # #             filepath = os.path.join(directory, filename)
# # # # # #             if os.path.isfile(filepath):
# # # # # #                 result_text.insert(tk.END, f"File: {filename}\n")
# # # # # #                 logfile.write(f"\nFile: {filename}\n")

# # # # # #                 sha256_hash = sha256()
# # # # # #                 with open(filepath, "rb") as file:
# # # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # # #                         sha256_hash.update(chunk)
# # # # # #                 hash_value = sha256_hash.hexdigest()
# # # # # #                 result_text.insert(tk.END, f"  SHA256: {hash_value}\n")
# # # # # #                 logfile.write(f"  SHA256: {hash_value}\n")

# # # # # #                 md5_hash = md5()
# # # # # #                 with open(filepath, "rb") as file:
# # # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # # #                         md5_hash.update(chunk)
# # # # # #                 hash_value = md5_hash.hexdigest()
# # # # # #                 result_text.insert(tk.END, f"  MD5: {hash_value}\n\n")
# # # # # #                 logfile.write(f"  MD5: {hash_value}\n\n")

# # # # # # # Function to open file dialog and get directory path
# # # # # # def browse_directory():
# # # # # #     directory_path = filedialog.askdirectory()
# # # # # #     directory_entry.delete(0, tk.END)
# # # # # #     directory_entry.insert(0, directory_path)

# # # # # # # Function to open file dialog and get logfile path
# # # # # # def browse_logfile():
# # # # # #     default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", "hash_log.log")
# # # # # #     logfile_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log")], initialfile=default_logfile_path)

# # # # # #     # Ensure the directory exists
# # # # # #     log_directory = os.path.dirname(logfile_path)
# # # # # #     if not os.path.exists(log_directory):
# # # # # #         os.makedirs(log_directory)

# # # # # #     logfile_entry.delete(0, tk.END)
# # # # # #     logfile_entry.insert(0, logfile_path)

# # # # # # # GUI setup
# # # # # # root = tk.Tk()
# # # # # # root.title("File Hash Calculator")

# # # # # # # Entry for directory path
# # # # # # directory_label = tk.Label(root, text="Enter Directory:")
# # # # # # directory_label.pack(pady=5)

# # # # # # directory_entry = tk.Entry(root, width=40)
# # # # # # directory_entry.pack(pady=5)

# # # # # # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # # # # # browse_button.pack(pady=10)

# # # # # # # Entry for logfile path
# # # # # # logfile_label = tk.Label(root, text="Save Log to File:")
# # # # # # logfile_label.pack(pady=5)

# # # # # # default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", "hash_log.log")
# # # # # # logfile_entry = tk.Entry(root, width=40)
# # # # # # logfile_entry.insert(0, default_logfile_path)
# # # # # # logfile_entry.pack(pady=5)

# # # # # # logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# # # # # # logfile_button.pack(pady=10)

# # # # # # # Button to calculate hashes
# # # # # # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get(), logfile_entry.get()))
# # # # # # calculate_button.pack(pady=10)

# # # # # # # Result display
# # # # # # result_label = tk.Label(root, text="")
# # # # # # result_label.pack(pady=5)

# # # # # # result_text = tk.Text(root, width=50, height=15)
# # # # # # result_text.pack(pady=10)

# # # # # # root.mainloop()

# # # # # import os
# # # # # import tkinter as tk
# # # # # from tkinter import filedialog
# # # # # from hashlib import sha256, md5
# # # # # from datetime import datetime

# # # # # def calculate_hashes(directory, log_file):
# # # # #     if not os.path.isdir(directory):
# # # # #         result_label.config(text=f"The path '{directory}' is not a directory.")
# # # # #         return

# # # # #     # Ensure the directory for the logfile exists
# # # # #     log_directory = os.path.dirname(log_file)
# # # # #     if not os.path.exists(log_directory):
# # # # #         os.makedirs(log_directory)

# # # # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # # # #     # Open the logfile in append mode
# # # # #     with open(log_file, "a") as logfile:
# # # # #         # Log the date and time
# # # # #         log_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# # # # #         logfile.write(f"\n\nLog Entry Date and Time: {log_timestamp}\n")
# # # # #         logfile.write(f"Directory: {directory}\n")

# # # # #         for filename in os.listdir(directory):
# # # # #             filepath = os.path.join(directory, filename)
# # # # #             if os.path.isfile(filepath):
# # # # #                 result_text.insert(tk.END, f"File: {filename}\n")
# # # # #                 logfile.write(f"\nFile: {filename}\n")

# # # # #                 sha256_hash = sha256()
# # # # #                 with open(filepath, "rb") as file:
# # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # #                         sha256_hash.update(chunk)
# # # # #                 hash_value = sha256_hash.hexdigest()
# # # # #                 result_text.insert(tk.END, f"  SHA256: {hash_value}\n")
# # # # #                 logfile.write(f"  SHA256: {hash_value}\n")

# # # # #                 md5_hash = md5()
# # # # #                 with open(filepath, "rb") as file:
# # # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # # #                         md5_hash.update(chunk)
# # # # #                 hash_value = md5_hash.hexdigest()
# # # # #                 result_text.insert(tk.END, f"  MD5: {hash_value}\n\n")
# # # # #                 logfile.write(f"  MD5: {hash_value}\n\n")

# # # # # # Function to open file dialog and get directory path
# # # # # def browse_directory():
# # # # #     directory_path = filedialog.askdirectory()
# # # # #     directory_entry.delete(0, tk.END)
# # # # #     directory_entry.insert(0, directory_path)

# # # # # # Function to open file dialog and get logfile path
# # # # # def browse_logfile():
# # # # #     default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", "hash_log.log")
# # # # #     logfile_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log")], initialfile=default_logfile_path)

# # # # #     # Ensure the directory exists
# # # # #     log_directory = os.path.dirname(logfile_path)
# # # # #     if not os.path.exists(log_directory):
# # # # #         os.makedirs(log_directory)

# # # # #     logfile_entry.delete(0, tk.END)
# # # # #     logfile_entry.insert(0, logfile_path)

# # # # # # GUI setup
# # # # # root = tk.Tk()
# # # # # root.title("File Hash Calculator")

# # # # # # Entry for directory path
# # # # # directory_label = tk.Label(root, text="Enter Directory:")
# # # # # directory_label.pack(pady=5)

# # # # # directory_entry = tk.Entry(root, width=40)
# # # # # directory_entry.pack(pady=5)

# # # # # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # # # # browse_button.pack(pady=10)

# # # # # # Entry for logfile path
# # # # # logfile_label = tk.Label(root, text="Save Log to File:")
# # # # # logfile_label.pack(pady=5)

# # # # # default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", "hash_log.log")
# # # # # logfile_entry = tk.Entry(root, width=40)
# # # # # logfile_entry.insert(0, default_logfile_path)
# # # # # logfile_entry.pack(pady=5)

# # # # # logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# # # # # logfile_button.pack(pady=10)

# # # # # # Button to calculate hashes
# # # # # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get(), logfile_entry.get()))
# # # # # calculate_button.pack(pady=10)

# # # # # # Result display
# # # # # result_label = tk.Label(root, text="")
# # # # # result_label.pack(pady=5)

# # # # # result_text = tk.Text(root, width=50, height=15)
# # # # # result_text.pack(pady=10)

# # # # # root.mainloop()

# # # # import os
# # # # import tkinter as tk
# # # # from tkinter import filedialog
# # # # from hashlib import sha256, md5
# # # # from datetime import datetime

# # # # def calculate_hashes(directory, log_file):
# # # #     if not os.path.isdir(directory):
# # # #         result_label.config(text=f"The path '{directory}' is not a directory.")
# # # #         return

# # # #     # Ensure the directory for the logfile exists
# # # #     log_directory = os.path.dirname(log_file)
# # # #     if not os.path.exists(log_directory):
# # # #         os.makedirs(log_directory)

# # # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # # #     # Open the logfile in append mode
# # # #     with open(log_file, "a") as logfile:
# # # #         # Log the date and time
# # # #         log_timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
# # # #         logfile.write(f"\n\nLog Entry Date and Time: {log_timestamp}\n")
# # # #         logfile.write(f"Directory: {directory}\n")

# # # #         for filename in os.listdir(directory):
# # # #             filepath = os.path.join(directory, filename)
# # # #             if os.path.isfile(filepath):
# # # #                 result_text.insert(tk.END, f"File: {filename}\n")
# # # #                 logfile.write(f"\nFile: {filename}\n")

# # # #                 sha256_hash = sha256()
# # # #                 with open(filepath, "rb") as file:
# # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # #                         sha256_hash.update(chunk)
# # # #                 hash_value = sha256_hash.hexdigest()
# # # #                 result_text.insert(tk.END, f"  SHA256: {hash_value}\n")
# # # #                 logfile.write(f"  SHA256: {hash_value}\n")

# # # #                 md5_hash = md5()
# # # #                 with open(filepath, "rb") as file:
# # # #                     for chunk in iter(lambda: file.read(4096), b""):
# # # #                         md5_hash.update(chunk)
# # # #                 hash_value = md5_hash.hexdigest()
# # # #                 result_text.insert(tk.END, f"  MD5: {hash_value}\n\n")
# # # #                 logfile.write(f"  MD5: {hash_value}\n\n")

# # # # # Function to open file dialog and get directory path
# # # # def browse_directory():
# # # #     directory_path = filedialog.askdirectory()
# # # #     directory_entry.delete(0, tk.END)
# # # #     directory_entry.insert(0, directory_path)

# # # # # Function to open file dialog and get logfile path
# # # # def browse_logfile():
# # # #     default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y%m%d%H%M%S')}.log")
# # # #     logfile_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log")], initialfile=default_logfile_path)

# # # #     # Ensure the directory exists
# # # #     log_directory = os.path.dirname(logfile_path)
# # # #     if not os.path.exists(log_directory):
# # # #         os.makedirs(log_directory)

# # # #     logfile_entry.delete(0, tk.END)
# # # #     logfile_entry.insert(0, logfile_path)

# # # # # Function to open file dialog and get log file for reading
# # # # def browse_read_logfile():
# # # #     read_logfile_path = filedialog.askopenfilename(defaultextension=".log", filetypes=[("Log files", "*.log")])
# # # #     read_logfile_entry.delete(0, tk.END)
# # # #     read_logfile_entry.insert(0, read_logfile_path)

# # # # # Function to read in an existing log file
# # # # def read_existing_log():
# # # #     read_logfile_path = read_logfile_entry.get()
# # # #     if not os.path.isfile(read_logfile_path):
# # # #         result_label.config(text=f"The path '{read_logfile_path}' is not a valid log file.")
# # # #         return

# # # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # # #     # Read the existing log file
# # # #     with open(read_logfile_path, "r") as read_logfile:
# # # #         result_text.insert(tk.END, read_logfile.read())

# # # # # GUI setup
# # # # root = tk.Tk()
# # # # root.title("File Hash Calculator")

# # # # # Entry for directory path
# # # # directory_label = tk.Label(root, text="Enter Directory:")
# # # # directory_label.pack(pady=5)

# # # # directory_entry = tk.Entry(root, width=40)
# # # # directory_entry.pack(pady=5)

# # # # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # # # browse_button.pack(pady=10)

# # # # # Entry for logfile path
# # # # logfile_label = tk.Label(root, text="Save Log to File:")
# # # # logfile_label.pack(pady=5)

# # # # default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y%m%d%H%M%S')}.log")
# # # # logfile_entry = tk.Entry(root, width=40)
# # # # logfile_entry.insert(0, default_logfile_path)
# # # # logfile_entry.pack(pady=5)

# # # # logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# # # # logfile_button.pack(pady=10)

# # # # # Entry for reading an existing log file
# # # # read_logfile_label = tk.Label(root, text="Read Existing Log File:")
# # # # read_logfile_label.pack(pady=5)

# # # # read_logfile_entry = tk.Entry(root, width=40)
# # # # read_logfile_entry.pack(pady=5)

# # # # browse_read_logfile_button = tk.Button(root, text="Browse", command=browse_read_logfile)
# # # # browse_read_logfile_button.pack(pady=10)

# # # # # Button to calculate hashes
# # # # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get(), logfile_entry.get()))
# # # # calculate_button.pack(pady=10)

# # # # # Button to read an existing log file
# # # # read_log_button = tk.Button(root, text="Read Existing Log", command=read_existing_log)
# # # # read_log_button.pack(pady=10)

# # # # # Result display
# # # # result_label = tk.Label(root, text="")
# # # # result_label.pack(pady=5)

# # # # result_text = tk.Text(root, width=50, height=15)
# # # # result_text.pack(pady=10)

# # # # root.mainloop()

# # # import os
# # # import tkinter as tk
# # # from tkinter import filedialog
# # # from hashlib import sha256, md5
# # # from datetime import datetime

# # # def calculate_hashes(directory, log_file):
# # #     if not os.path.isdir(directory):
# # #         result_label.config(text=f"The path '{directory}' is not a directory.")
# # #         return

# # #     # Ensure the directory for the logfile exists
# # #     log_directory = os.path.dirname(log_file)
# # #     if not os.path.exists(log_directory):
# # #         os.makedirs(log_directory)

# # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # #     # Open the logfile in append mode
# # #     with open(log_file, "a") as logfile:
# # #         # Log the date and time
# # #         log_timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
# # #         logfile.write(f"\n\nLog Entry Date and Time: {log_timestamp}\n")
# # #         logfile.write(f"Directory: {directory}\n")

# # #         for filename in os.listdir(directory):
# # #             filepath = os.path.join(directory, filename)
# # #             if os.path.isfile(filepath):
# # #                 result_text.insert(tk.END, f"File: {filename}\n")
# # #                 logfile.write(f"\nFile: {filename}\n")

# # #                 sha256_hash = sha256()
# # #                 with open(filepath, "rb") as file:
# # #                     for chunk in iter(lambda: file.read(4096), b""):
# # #                         sha256_hash.update(chunk)
# # #                 hash_value = sha256_hash.hexdigest()
# # #                 result_text.insert(tk.END, f"  SHA256: {hash_value}\n")
# # #                 logfile.write(f"  SHA256: {hash_value}\n")

# # #                 md5_hash = md5()
# # #                 with open(filepath, "rb") as file:
# # #                     for chunk in iter(lambda: file.read(4096), b""):
# # #                         md5_hash.update(chunk)
# # #                 hash_value = md5_hash.hexdigest()
# # #                 result_text.insert(tk.END, f"  MD5: {hash_value}\n\n")
# # #                 logfile.write(f"  MD5: {hash_value}\n\n")

# # # # Function to open file dialog and get directory path
# # # def browse_directory():
# # #     directory_path = filedialog.askdirectory()
# # #     directory_entry.delete(0, tk.END)
# # #     directory_entry.insert(0, directory_path)

# # # # Function to open file dialog and get logfile path
# # # def browse_logfile():
# # #     default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
# # #     logfile_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log")], initialfile=default_logfile_path)

# # #     # Ensure the directory exists
# # #     log_directory = os.path.dirname(logfile_path)
# # #     if not os.path.exists(log_directory):
# # #         os.makedirs(log_directory)

# # #     logfile_entry.delete(0, tk.END)
# # #     logfile_entry.insert(0, logfile_path)

# # # # Function to open file dialog and get log file for reading
# # # def browse_read_logfile():
# # #     read_logfile_path = filedialog.askopenfilename(defaultextension=".log", filetypes=[("Log files", "*.log")])
# # #     read_logfile_entry.delete(0, tk.END)
# # #     read_logfile_entry.insert(0, read_logfile_path)

# # # # Function to read in an existing log file
# # # def read_existing_log():
# # #     read_logfile_path = read_logfile_entry.get()
# # #     if not os.path.isfile(read_logfile_path):
# # #         result_label.config(text=f"The path '{read_logfile_path}' is not a valid log file.")
# # #         return

# # #     result_text.delete(1.0, tk.END)  # Clear previous results

# # #     # Read the existing log file
# # #     with open(read_logfile_path, "r") as read_logfile:
# # #         result_text.insert(tk.END, read_logfile.read())

# # # # GUI setup
# # # root = tk.Tk()
# # # root.title("File Hash Calculator")

# # # # Entry for directory path
# # # directory_label = tk.Label(root, text="Enter Directory:")
# # # directory_label.pack(pady=5)

# # # directory_entry = tk.Entry(root, width=40)
# # # directory_entry.pack(pady=5)

# # # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # # browse_button.pack(pady=10)

# # # # Entry for logfile path
# # # logfile_label = tk.Label(root, text="Save Log to File:")
# # # logfile_label.pack(pady=5)

# # # default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
# # # logfile_entry = tk.Entry(root, width=40)
# # # logfile_entry.insert(0, default_logfile_path)
# # # logfile_entry.pack(pady=5)

# # # logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# # # logfile_button.pack(pady=10)

# # # # Entry for reading an existing log file
# # # read_logfile_label = tk.Label(root, text="Read Existing Log File:")
# # # read_logfile_label.pack(pady=5)

# # # read_logfile_entry = tk.Entry(root, width=40)
# # # read_logfile_entry.pack(pady=5)

# # # browse_read_logfile_button = tk.Button(root, text="Browse", command=browse_read_logfile)
# # # browse_read_logfile_button.pack(pady=10)

# # # # Button to calculate hashes
# # # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get(), logfile_entry.get()))
# # # calculate_button.pack(pady=10)

# # # # Button to read an existing log file
# # # read_log_button = tk.Button(root, text="Read Existing Log", command=read_existing_log)
# # # read_log_button.pack(pady=10)

# # # # Button for comparing logs (no functionality for now)
# # # compare_button = tk.Button(root, text="Compare", command=lambda: result_label.config(text="Comparison functionality not implemented yet"))
# # # compare_button.pack(pady=10)

# # # # Result display
# # # result_label = tk.Label(root, text="")
# # # result_label.pack(pady=5)

# # # result_text = tk.Text(root, width=50, height=15)
# # # result_text.pack(pady=10)

# # # root.mainloop()

# # import os
# # import tkinter as tk
# # from tkinter import filedialog
# # from hashlib import sha256, md5
# # from datetime import datetime

# # def calculate_hashes(directory):
# #     if not os.path.isdir(directory):
# #         result_label.config(text=f"The path '{directory}' is not a directory.")
# #         return

# #     result_text.delete(1.0, tk.END)  # Clear previous results

# #     hash_dict = {}

# #     for filename in os.listdir(directory):
# #         filepath = os.path.join(directory, filename)
# #         if os.path.isfile(filepath):
# #             result_text.insert(tk.END, f"File: {filename}\n")

# #             sha256_hash = sha256()
# #             with open(filepath, "rb") as file:
# #                 for chunk in iter(lambda: file.read(4096), b""):
# #                     sha256_hash.update(chunk)
# #             sha256_value = sha256_hash.hexdigest()
# #             result_text.insert(tk.END, f"  SHA256: {sha256_value}\n")

# #             md5_hash = md5()
# #             with open(filepath, "rb") as file:
# #                 for chunk in iter(lambda: file.read(4096), b""):
# #                     md5_hash.update(chunk)
# #             md5_value = md5_hash.hexdigest()
# #             result_text.insert(tk.END, f"  MD5: {md5_value}\n\n")

# #             hash_dict[filename] = {"SHA256": sha256_value, "MD5": md5_value}

# #     return hash_dict

# # def compare_hashes(directory, log_file):
# #     directory_hashes = calculate_hashes(directory)
# #     if not directory_hashes:
# #         return

# #     if not os.path.isfile(log_file):
# #         result_label.config(text=f"The path '{log_file}' is not a valid log file.")
# #         return

# #     result_text.delete(1.0, tk.END)  # Clear previous results

# #     # Read the existing log file
# #     with open(log_file, "r") as read_logfile:
# #         log_lines = read_logfile.readlines()

# #     result_text.insert(tk.END, "Comparison Results:\n\n")

# #     while log_lines:
# #         if log_lines[0].startswith("File: "):
# #             filename = log_lines.pop(0).split(":")[1].strip()
# #             sha256_log = log_lines.pop(0).split(":")[1].strip() if log_lines else ""
# #             md5_log = log_lines.pop(0).split(":")[1].strip() if log_lines else ""

# #             if filename in directory_hashes:
# #                 sha256_dir = directory_hashes[filename]["SHA256"]
# #                 md5_dir = directory_hashes[filename]["MD5"]

# #                 result_text.insert(tk.END, f"File: {filename}\n")
# #                 result_text.insert(tk.END, f"  SHA256: {sha256_dir} (Calculated) vs {sha256_log} (From Log)\n")
# #                 result_text.insert(tk.END, f"  MD5: {md5_dir} (Calculated) vs {md5_log} (From Log)\n")

# #                 if sha256_dir == sha256_log and md5_dir == md5_log:
# #                     result_text.insert(tk.END, "  Hashes match!\n\n")
# #                 else:
# #                     result_text.insert(tk.END, "  Hashes do not match!\n\n")
# #             else:
# #                 result_text.insert(tk.END, f"File: {filename} not found in the calculated hashes.\n\n")
# #         else:
# #             log_lines.pop(0)


# # # Function to open file dialog and get directory path
# # def browse_directory():
# #     directory_path = filedialog.askdirectory()
# #     directory_entry.delete(0, tk.END)
# #     directory_entry.insert(0, directory_path)

# # # Function to open file dialog and get logfile path
# # def browse_logfile():
# #     default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
# #     logfile_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log")], initialfile=default_logfile_path)

# #     # Ensure the directory exists
# #     log_directory = os.path.dirname(logfile_path)
# #     if not os.path.exists(log_directory):
# #         os.makedirs(log_directory)

# #     logfile_entry.delete(0, tk.END)
# #     logfile_entry.insert(0, logfile_path)

# # # Function to open file dialog and get log file for reading
# # def browse_read_logfile():
# #     read_logfile_path = filedialog.askopenfilename(defaultextension=".log", filetypes=[("Log files", "*.log")])
# #     read_logfile_entry.delete(0, tk.END)
# #     read_logfile_entry.insert(0, read_logfile_path)

# # # Function to read in an existing log file
# # def read_existing_log():
# #     read_logfile_path = read_logfile_entry.get()
# #     if not os.path.isfile(read_logfile_path):
# #         result_label.config(text=f"The path '{read_logfile_path}' is not a valid log file.")
# #         return

# #     result_text.delete(1.0, tk.END)  # Clear previous results

# #     # Read the existing log file
# #     with open(read_logfile_path, "r") as read_logfile:
# #         result_text.insert(tk.END, read_logfile.read())

# # # Function for comparing hashes
# # def compare_hashes_wrapper():
# #     compare_hashes(directory_entry.get(), read_logfile_entry.get())

# # # GUI setup
# # root = tk.Tk()
# # root.title("File Hash Calculator")

# # # Entry for directory path
# # directory_label = tk.Label(root, text="Enter Directory:")
# # directory_label.pack(pady=5)

# # directory_entry = tk.Entry(root, width=40)
# # directory_entry.pack(pady=5)

# # browse_button = tk.Button(root, text="Browse", command=browse_directory)
# # browse_button.pack(pady=10)

# # # Entry for logfile path
# # logfile_label = tk.Label(root, text="Save Log to File:")
# # logfile_label.pack(pady=5)

# # default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
# # logfile_entry = tk.Entry(root, width=40)
# # logfile_entry.insert(0, default_logfile_path)
# # logfile_entry.pack(pady=5)

# # logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# # logfile_button.pack(pady=10)

# # # Entry for reading an existing log file
# # read_logfile_label = tk.Label(root, text="Read Existing Log File:")
# # read_logfile_label.pack(pady=5)

# # read_logfile_entry = tk.Entry(root, width=40)
# # read_logfile_entry.pack(pady=5)

# # browse_read_logfile_button = tk.Button(root, text="Browse", command=browse_read_logfile)
# # browse_read_logfile_button.pack(pady=10)

# # # Button to calculate hashes
# # calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get()))
# # calculate_button.pack(pady=10)

# # # Button to read an existing log file
# # read_log_button = tk.Button(root, text="Read Existing Log", command=read_existing_log)
# # read_log_button.pack(pady=10)

# # # Button for comparing hashes
# # compare_button = tk.Button(root, text="Compare", command=compare_hashes_wrapper)
# # compare_button.pack(pady=10)

# # # Result display
# # result_label = tk.Label(root, text="")
# # result_label.pack(pady=5)

# # result_text = tk.Text(root, width=50, height=15)
# # result_text.pack(pady=10)

# # root.mainloop()

# import os
# import tkinter as tk
# from tkinter import filedialog
# from hashlib import sha256, md5
# from datetime import datetime

# def calculate_hashes(directory):
#     if not os.path.isdir(directory):
#         result_label.config(text=f"The path '{directory}' is not a directory.")
#         return

#     result_text.delete(1.0, tk.END)  # Clear previous results

#     hash_dict = {}

#     for filename in os.listdir(directory):
#         filepath = os.path.join(directory, filename)
#         if os.path.isfile(filepath):
#             sha256_hash = sha256()
#             with open(filepath, "rb") as file:
#                 for chunk in iter(lambda: file.read(4096), b""):
#                     sha256_hash.update(chunk)
#             sha256_value = sha256_hash.hexdigest()

#             md5_hash = md5()
#             with open(filepath, "rb") as file:
#                 for chunk in iter(lambda: file.read(4096), b""):
#                     md5_hash.update(chunk)
#             md5_value = md5_hash.hexdigest()

#             hash_dict[filename] = {"SHA256": sha256_value, "MD5": md5_value}

#             # Display only filename without the actual checksum in the result_text
#             result_text.insert(tk.END, f"File: {filename}\n")

#     return hash_dict

# def compare_hashes(directory, log_file):
#     directory_hashes = calculate_hashes(directory)
#     if not directory_hashes:
#         return

#     if not os.path.isfile(log_file):
#         result_label.config(text=f"The path '{log_file}' is not a valid log file.")
#         return

#     result_text.delete(1.0, tk.END)  # Clear previous results

#     # Read the existing log file
#     with open(log_file, "r") as read_logfile:
#         log_lines = read_logfile.readlines()

#     results_window = tk.Toplevel(root)
#     results_window.title("Comparison Results")

#     result_text_window = tk.Text(results_window, width=50, height=15)
#     result_text_window.pack(pady=10)

#     result_text_window.insert(tk.END, "Comparison Results:\n\n")

#     while log_lines:
#         if log_lines[0].startswith("File: "):
#             filename = log_lines.pop(0).split(":")[1].strip()
#             sha256_log = log_lines.pop(0).split(":")[1].strip() if log_lines else ""
#             md5_log = log_lines.pop(0).split(":")[1].strip() if log_lines else ""

#             if filename in directory_hashes:
#                 sha256_dir = directory_hashes[filename]["SHA256"]
#                 md5_dir = directory_hashes[filename]["MD5"]

#                 result_text_window.insert(tk.END, f"File: {filename}\n")

#                 if sha256_dir == sha256_log and md5_dir == md5_log:
#                     result_text_window.insert(tk.END, "  Hashes match!\n\n")
#                 else:
#                     result_text_window.insert(tk.END, "  Hashes do not match!\n\n")
#             else:
#                 result_text_window.insert(tk.END, f"File: {filename} not found in the calculated hashes.\n\n")
#         else:
#             log_lines.pop(0)

# def browse_directory():
#     directory_path = filedialog.askdirectory()
#     directory_entry.delete(0, tk.END)
#     directory_entry.insert(0, directory_path)

# def browse_logfile():
#     default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
#     logfile_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log")], initialfile=default_logfile_path)

#     # Ensure the directory exists
#     log_directory = os.path.dirname(logfile_path)
#     if not os.path.exists(log_directory):
#         os.makedirs(log_directory)

#     logfile_entry.delete(0, tk.END)
#     logfile_entry.insert(0, logfile_path)

# # Function to open file dialog and get log file for reading
# def browse_read_logfile():
#     read_logfile_path = filedialog.askopenfilename(defaultextension=".log", filetypes=[("Log files", "*.log")])
#     read_logfile_entry.delete(0, tk.END)
#     read_logfile_entry.insert(0, read_logfile_path)

# # Function to read in an existing log file
# def read_existing_log():
#     read_logfile_path = read_logfile_entry.get()
#     if not os.path.isfile(read_logfile_path):
#         result_label.config(text=f"The path '{read_logfile_path}' is not a valid log file.")
#         return

#     result_text.delete(1.0, tk.END)  # Clear previous results

#     # Read the existing log file
#     with open(read_logfile_path, "r") as read_logfile:
#         result_text.insert(tk.END, read_logfile.read())

# # Function for comparing hashes
# def compare_hashes_wrapper():
#     compare_hashes(directory_entry.get(), read_logfile_entry.get())

# # GUI setup
# root = tk.Tk()
# root.title("File Hash Calculator")

# # Entry for directory path
# directory_label = tk.Label(root, text="Enter Directory:")
# directory_label.pack(pady=5)

# directory_entry = tk.Entry(root, width=40)
# directory_entry.pack(pady=5)

# browse_button = tk.Button(root, text="Browse", command=browse_directory)
# browse_button.pack(pady=10)

# # Entry for logfile path
# logfile_label = tk.Label(root, text="Save Log to File:")
# logfile_label.pack(pady=5)

# default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
# logfile_entry = tk.Entry(root, width=40)
# logfile_entry.insert(0, default_logfile_path)
# logfile_entry.pack(pady=5)

# logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
# logfile_button.pack(pady=10)

# # Entry for reading an existing log file
# read_logfile_label = tk.Label(root, text="Read Existing Log File:")
# read_logfile_label.pack(pady=5)

# read_logfile_entry = tk.Entry(root, width=40)
# read_logfile_entry.pack(pady=5)

# browse_read_logfile_button = tk.Button(root, text="Browse", command=browse_read_logfile)
# browse_read_logfile_button.pack(pady=10)

# # Button to calculate hashes
# calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: calculate_hashes(directory_entry.get()))
# calculate_button.pack(pady=10)

# # Button to read an existing log file
# read_log_button = tk.Button(root, text="Read Existing Log", command=read_existing_log)
# read_log_button.pack(pady=10)

# # Button for comparing hashes
# compare_button = tk.Button(root, text="Compare", command=compare_hashes_wrapper)
# compare_button.pack(pady=10)

# # Result display
# result_label = tk.Label(root, text="")
# result_label.pack(pady=5)

# result_text = tk.Text(root, width=50, height=15)
# result_text.pack(pady=10)

# root.mainloop()

import os
import tkinter as tk
from tkinter import filedialog
from hashlib import sha256, md5
from datetime import datetime

def calculate_hashes(directory):
    if not os.path.isdir(directory):
        result_label.config(text=f"The path '{directory}' is not a directory.")
        return

    result_text.delete(1.0, tk.END)  # Clear previous results

    hash_dict = {}

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            sha256_hash = sha256()
            with open(filepath, "rb") as file:
                for chunk in iter(lambda: file.read(4096), b""):
                    sha256_hash.update(chunk)
            sha256_value = sha256_hash.hexdigest()

            md5_hash = md5()
            with open(filepath, "rb") as file:
                for chunk in iter(lambda: file.read(4096), b""):
                    md5_hash.update(chunk)
            md5_value = md5_hash.hexdigest()

            hash_dict[filename] = {"SHA256": sha256_value, "MD5": md5_value}

            # Display only filename without the actual checksum in the result_text
            result_text.insert(tk.END, f"File: {filename}\n")

    return hash_dict

def save_to_logfile(log_file, hash_dict):
    with open(log_file, "w") as logfile:
        for filename, hashes in hash_dict.items():
            logfile.write(f"File: {filename}\n")
            logfile.write(f"  SHA256: {hashes['SHA256']}\n")
            logfile.write(f"  MD5: {hashes['MD5']}\n\n")

def compare_hashes(directory, log_file):
    directory_hashes = calculate_hashes(directory)
    if not directory_hashes:
        return

    if not os.path.isfile(log_file):
        result_label.config(text=f"The path '{log_file}' is not a valid log file.")
        return

    result_text.delete(1.0, tk.END)  # Clear previous results

    # Read the existing log file
    with open(log_file, "r") as read_logfile:
        log_lines = read_logfile.readlines()

    results_window = tk.Toplevel(root)
    results_window.title("Comparison Results")

    result_text_window = tk.Text(results_window, width=50, height=15)
    result_text_window.pack(pady=10)

    result_text_window.insert(tk.END, "Comparison Results:\n\n")

    while log_lines:
        if log_lines[0].startswith("File: "):
            filename = log_lines.pop(0).split(":")[1].strip()
            sha256_log = log_lines.pop(0).split(":")[1].strip() if log_lines else ""
            md5_log = log_lines.pop(0).split(":")[1].strip() if log_lines else ""

            if filename in directory_hashes:
                sha256_dir = directory_hashes[filename]["SHA256"]
                md5_dir = directory_hashes[filename]["MD5"]

                result_text_window.insert(tk.END, f"File: {filename}\n")

                if sha256_dir == sha256_log and md5_dir == md5_log:
                    result_text_window.insert(tk.END, "  Hashes match!\n\n")
                else:
                    result_text_window.insert(tk.END, "  Hashes do not match!\n\n")
            else:
                result_text_window.insert(tk.END, f"File: {filename} not found in the calculated hashes.\n\n")
        else:
            log_lines.pop(0)

def browse_directory():
    directory_path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory_path)

def browse_logfile():
    default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
    logfile_path = filedialog.asksaveasfilename(defaultextension=".log", filetypes=[("Log files", "*.log")], initialfile=default_logfile_path)

    # Ensure the directory exists
    log_directory = os.path.dirname(logfile_path)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logfile_entry.delete(0, tk.END)
    logfile_entry.insert(0, logfile_path)

# Function to open file dialog and get log file for reading
def browse_read_logfile():
    read_logfile_path = filedialog.askopenfilename(defaultextension=".log", filetypes=[("Log files", "*.log")])
    read_logfile_entry.delete(0, tk.END)
    read_logfile_entry.insert(0, read_logfile_path)

# Function to read in an existing log file
def read_existing_log():
    read_logfile_path = read_logfile_entry.get()
    if not os.path.isfile(read_logfile_path):
        result_label.config(text=f"The path '{read_logfile_path}' is not a valid log file.")
        return

    result_text.delete(1.0, tk.END)  # Clear previous results

    # Read the existing log file
    with open(read_logfile_path, "r") as read_logfile:
        result_text.insert(tk.END, read_logfile.read())

# Function for comparing hashes
def compare_hashes_wrapper():
    compare_hashes(directory_entry.get(), read_logfile_entry.get())

# GUI setup
root = tk.Tk()
root.title("File Hash Calculator")

# Entry for directory path
directory_label = tk.Label(root, text="Enter Directory:")
directory_label.pack(pady=5)

directory_entry = tk.Entry(root, width=40)
directory_entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=10)

# Entry for logfile path
logfile_label = tk.Label(root, text="Save Log to File:")
logfile_label.pack(pady=5)

default_logfile_path = os.path.join("C:", os.sep, "HashCalculator", "Logs", f"hash_log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
logfile_entry = tk.Entry(root, width=40)
logfile_entry.insert(0, default_logfile_path)
logfile_entry.pack(pady=5)

logfile_button = tk.Button(root, text="Browse", command=browse_logfile)
logfile_button.pack(pady=10)

# Entry for reading an existing log file
read_logfile_label = tk.Label(root, text="Read Existing Log File:")
read_logfile_label.pack(pady=5)

read_logfile_entry = tk.Entry(root, width=40)
read_logfile_entry.pack(pady=5)

browse_read_logfile_button = tk.Button(root, text="Browse", command=browse_read_logfile)
browse_read_logfile_button.pack(pady=10)

# Button to calculate hashes
calculate_button = tk.Button(root, text="Calculate Hashes", command=lambda: save_to_logfile(logfile_entry.get(), calculate_hashes(directory_entry.get())))
calculate_button.pack(pady=10)

# Button to read an existing log file
read_log_button = tk.Button(root, text="Read Existing Log", command=read_existing_log)
read_log_button.pack(pady=10)

# Button for comparing hashes
compare_button = tk.Button(root, text="Compare", command=compare_hashes_wrapper)
compare_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

result_text = tk.Text(root, width=50, height=15)
result_text.pack(pady=10)

root.mainloop()