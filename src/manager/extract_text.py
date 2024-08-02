import fitz
from src.utility.logger_util import get_logger

logger = get_logger(__name__)

def extract_text(path):
    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        
        logger.info(f'Successfully extracted text from PDF. {str(path)}')
        return {'message': 'Successfully extracted text', 'text': text}
    except Exception as e:
        logger.error(f'Error extracting text: {str(e)}')
        return {'error': str(e)}
