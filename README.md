#UpdateBatchArchive
Overview
UpdateBatchArchive is a Python utility designed to streamline the process of updating and archiving batches of files. This tool aims to simplify the task of managing file updates and maintaining a clean archive of previous versions. It incorporates robust exception handling to ensure smooth execution even in the face of unexpected errors.

Features
Batch Update: Easily update multiple files at once by specifying a source directory and a destination directory.
Archive Functionality: Automatically archives the previous versions of updated files, ensuring a history of changes is preserved.
Customizable Options: Configurable options allow users to tailor the behavior of the tool to their specific needs.
Logging: Comprehensive logging functionality provides insight into the update and archive processes, aiding in troubleshooting and auditing.
Exception Handling: Built-in exception handling ensures graceful handling of errors, preventing abrupt termination of the program and providing informative error messages for debugging.
Requirements
Python 3.x
Google Sheets API Credentials (for moving data between spreadsheets)

Usage
Google Sheets API Credentials:
Obtain your own Google Sheets API credentials and save the JSON file containing the credentials securely.
Configuration:
Modify the config.json file to specify source and destination directories, archive settings, Google Sheets API credentials file path, and any other desired options.
Execution:
Run the script using the following command: python update_batch_archive.py

Contribution
Contributions are welcome! If you encounter any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.
