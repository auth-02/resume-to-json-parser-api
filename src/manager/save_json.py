import os
import json
from src.utility.logger_util import get_logger

logger = get_logger(__name__)

def save_json(json_output, output_dir, file_name):
    output_file_path = os.path.join(output_dir, f"{file_name.split('.')[0].split('/')[-1]}.json")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(json_output, output_file, indent=4)
    
    logger.info(f'Successfully saved parsed JSON at {str(output_file_path)}')
