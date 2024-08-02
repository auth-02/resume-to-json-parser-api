import openai
from src.utility.logger_util import get_logger
from src.config.config import OPENAI_API_KEY, OPENAI_ORGNIZATION

openai.api_key = OPENAI_API_KEY
openai.organization = OPENAI_ORGNIZATION

logger = get_logger(__name__)

def resume_parser(cleaned_text):
    SYSTEM_PROMPT = "You are an expert recruiter extracting structured data from resumes."
    USER_PROMPT = (
        """Extract the following details from the resume:\n
        1. name
        2. first_name
        3. last_name
        4. summary
        5. resume_title
        6. dob
        7. spoken_language
        8. family_type
        9. phone_no
        10. email_id_primary
        11. email_id_secondary
        12. current_address
        13. name_of_city
        14. name_of_state
        15. permanant_address
        16. aadhar_card_number
        17. pan_card_number
        18. passport_no
        19. marriage_status
        20. gender
        21. linkedin_id
        22. git_id
        23. twitter_id
        24. medium_id
        25. stackflow_id
        26. last_job_change_date
        27. technical_skills
        28. functional_skills
        29. key_skill
        30. soft_skills
        31. no_of_yrs_of_exp
        32. skills_recently_used
        33. all_cand_qualification
        34. awards
        35. certifications
        36. country
        37. skill_exp
        \n\nResume text:\n%s"""
        % cleaned_text
    )
    
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT},
                {"role": "assistant", "content": "Provide output in JSON format."}
            ]
        )
        
        resume_json = completion.choices[0].message.content
        logger.info('Successfully generated JSON from cleaned text.')
        return resume_json
    
    except Exception as e:
        logger.error(f'Error generating resume JSON: {str(e)}')
        return {'error': str(e)}
