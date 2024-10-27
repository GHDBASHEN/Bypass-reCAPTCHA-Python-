reCAPTCHA Bypassing with OpenAI Whisper Model

This project demonstrates how to bypass audio-based reCAPTCHA using OpenAI’s Whisper model for speech-to-text conversion. The solution automates the transcription of the audio challenge using Python.

## Overview

This project leverages Selenium and the OpenAI Whisper model to transcribe audio reCAPTCHA challenges into text automatically. The script navigates through the reCAPTCHA challenge using a web driver and extracts audio, which is then passed to the Whisper model for transcription.

## Features

- **Audio reCAPTCHA extraction**: Extracts the audio challenge file from a web page.
- **Automated transcription**: Uses OpenAI Whisper to transcribe the audio to text.
- **Bypassing reCAPTCHA**: Inputs the transcribed text into the reCAPTCHA field to complete the challenge.

## Prerequisites

- Python 3.7 or above
- Google Chrome installed
- **Python Packages**:
  - selenium
  - openai-whisper
  - webdriver-manager
  - torch
  - tqdm

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
Create a virtual environment:

bash
Always show details

Copy code
python -m venv myenv
source myenv/bin/activate  # For Linux/MacOS
myenv\\Scripts\\activate     # For Windows
Install the dependencies:

bash
Always show details

Copy code
pip install -r requirements.txt
Usage
Run the script:

bash
Always show details

Copy code
python main.py
Process:

The script uses a Selenium WebDriver to navigate to the web page with a reCAPTCHA.
It clicks on the audio reCAPTCHA option and downloads the audio.
Whisper transcribes the audio file and inputs the transcribed text to complete the challenge.
Troubleshooting
FileNotFoundError: Ensure that ffmpeg is installed and added to your system's PATH.
Driver Issues: Ensure that the correct version of ChromeDriver is installed and matches your Google Chrome version.
Contributing
If you find issues or have suggestions for improvements, feel free to open an issue or a pull request.

License
This project is licensed under the MIT License.
