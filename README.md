
# Keyboard Event Lab — Safe Cybersecurity Demo

A beginner-friendly Python GUI project demonstrating input validation, session controls, local file handling, and automated testing.

## Project Overview

Keyboard Event Lab is an educational application built with Python and Tkinter. It allows a user to enter sample text into the application's own input field and explicitly save it as a local test record.

**This project does not monitor keystrokes in other applications.**

## Features

- Start and Stop session controls
- Dedicated sample-text input field
- Input validation
- Explicitly save sample records
- View saved test records
- Clear the input field
- Delete saved logs with confirmation
- Local file storage
- Automated tests using Python's `unittest`

## Technologies

- Python 3.14
- Tkinter
- pathlib
- datetime
- unittest

## Project Structure

```text
BasicKeylogger/
├── main.py
├── logger_utils.py
├── test_logger.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.14 or another compatible Python version
- Tkinter available in your Python installation

No third-party Python packages are required by the supplied application and tests.

## Run the Application

Open Command Prompt in the project folder and run:

```bat
py main.py
```

Start a session, enter harmless sample text, and select **Save Record** to create a test record.

## Run Automated Tests

Run:

```bat
py -m unittest -v test_logger
```

The test suite checks input validation, record formatting, saving, reading, and deleting logs using temporary files.

## Privacy and Responsible Use

- Use only sample text that contains no sensitive information.
- Records are saved locally on the computer.
- Do not enter passwords, authentication codes, or confidential information.
- The application is intended for learning and controlled demonstrations.
- Do not modify it to collect input from other applications without appropriate authorization and safeguards.

## Limitations

This is a learning prototype, not a production security tool, malware detector, or comprehensive endpoint-security solution.

## Future Improvements

- Additional automated GUI tests
- Accessibility improvements
- Improved error handling
- Session statistics
- Security-awareness educational material

## Author

Student cybersecurity learning project.
