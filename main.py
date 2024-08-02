import os
from flask import Flask, request, jsonify
from src.manager.extract_text import extract_text
from src.manager.clean_text import clean_text
from src.manager.resume_parser import resume_parser
from src.manager.save_json import save_json
from src.utility.logger_util import get_logger
from src.service.swagger import initialize_swagger

app = Flask(__name__)

initialize_swagger(app)

logger = get_logger(__name__)

os.makedirs('data/raw_resumes', exist_ok=True)
os.makedirs('data/processed_json', exist_ok=True)

@app.route('/parse_resume', methods=['POST'])
def parse_resume():
    
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        raw_resume_path = os.path.join('data', 'raw_resumes', file.filename)
        file.save(raw_resume_path)

        logger.info("Extracting text from PDF")
        extract_result = extract_text(raw_resume_path)
        if 'error' in extract_result:
            return jsonify({'error': extract_result['error']}), 500

        logger.info("Cleaning extracted text")
        cleaned_text = clean_text(extract_result['text'])

        logger.info("Generating resume JSON")
        resume_json = resume_parser(cleaned_text)

        logger.info("Saving JSON output")
        save_json(resume_json, 'data/processed_json', file.filename)

        return jsonify({'resume': resume_json}), 200

    except Exception as e:
        logger.error(f"Error parsing resume: {str(e)}")
        # return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
