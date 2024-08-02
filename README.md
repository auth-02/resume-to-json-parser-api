# Resume to JSON Parser API

🚀 Transform plain text resumes into structured JSON format effortlessly with this Python project. Save time on manual data entry and streamline your hiring process. Perfect for HR professionals, developers, and tech enthusiasts. Revolutionize your resume handling today!

## Features

- Upload a resume in PDF format
- Extract and clean text from resumes
- Convert resume text to structured JSON format
- View API documentation with Swagger UI

## Directory Structure

```plaintext
resume-to-json-parser-api/
├── data/
│   ├── processed_json/
│   └── raw_resumes/
├── logs/
├── src/
│   ├── config/
│   │   └── config.py
│   ├── database/
│   ├── manager/
│   │   ├── clean_text.py
│   │   ├── extract_text.py
│   │   ├── resume_parser.py
│   │   ├── save_json.py
│   │ 
│   ├── service/
│   │   └── swagger.py
│   └── utility/
│       ├── logger_util.py
│    
├── main.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.8+
- `pip` package manager

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/auth-02/resume-to-json-parser-api.git
    cd resume-to-json-parser-api
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate   
    # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**

    update `config.py` file in the `src/config` directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Run the application:**

    ```sh
    python main.py
    ```

2. **Access the Swagger UI:**

    Open your browser and navigate to `http://localhost:5000/apidocs/#/` to access the Swagger UI.

3. **Upload a resume file:**

    Use the `/parse_resume` endpoint in the Swagger UI to upload a resume file and get the parsed JSON output.


