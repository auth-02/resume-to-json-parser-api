import re
from nltk.tokenize import word_tokenize
from src.utility.logger_util import get_logger

logger = get_logger(__name__)

def clean_text(text):
    
    try:
        tokens = word_tokenize(text)
        filtered_tokens = [token for token in tokens]
        filtered_text = ' '.join(filtered_tokens)
        
        special_chars_pattern = re.compile(r'[^a-zA-Z0-9\s]')
        filtered_tokens = [special_chars_pattern.sub('', token) for token in tokens if token.strip()]
        filtered_array = [item for item in filtered_tokens if item.strip()]
        
        cleaned_text = filtered_text.replace("..", "").replace("▪", "").replace("●", "").replace("\n\n", "\n").replace(":", "").replace("|", "").replace("", "")
        
        logger.info('Successfully cleaned the text.')
        return cleaned_text
    
    except Exception as e:
        logger.error(f'Error cleaning text: {str(e)}')
        return text
