<<<<<<< HEAD
# ai-model-server
=======
# AI Model Server

This project is designed to provide various AI functionalities, including speech-to-text, text-to-speech, PDF parsing, and question generation. Each component is modularized into separate directories for better organization and maintainability.

## Project Structure

```
ai-model-server/
├── stt/                 # Whisper API for speech-to-text processing
│   └── main.py
├── tts/                 # Coqui TTS API for text-to-speech processing
│   └── main.py
├── cv-parser/           # PDF parser for extracting text/data from PDF files
│   └── main.py
├── question-gen/        # Module for generating questions based on input data
│   └── main.py
├── shared/              # Shared utilities and functions
│   └── __init__.py
├── requirements.txt     # List of dependencies for the project
├── docker-compose.yml    # Docker configuration for the application
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ai-model-server
   ```

2. **Install dependencies:**
   Use the following command to install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can use Docker to run the application. Make sure Docker is installed and running, then execute:
   ```
   docker-compose up
   ```

## Usage Guidelines

- **STT (Speech-to-Text):** 
  - Navigate to the `stt` directory and run `main.py` to utilize the Whisper API for converting speech to text.

- **TTS (Text-to-Speech):**
  - Navigate to the `tts` directory and run `main.py` to utilize the Coqui TTS API for converting text to speech.

- **PDF Parsing:**
  - Navigate to the `cv-parser` directory and run `main.py` to extract text or data from PDF files.

- **Question Generation:**
  - Navigate to the `question-gen` directory and run `main.py` to generate questions based on provided input.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
>>>>>>> master
