# src/service/swagger.py

from flasgger import Swagger

def initialize_swagger(app):
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "resume-to-json-parser-api",
            "version": "1.0.0",
            "description": "Transform plain text resumes into structured JSON format effortlessly with this API.",
            "termsOfService": "/tos"
        },
        "paths": {
            "/parse_resume": {
                "post": {
                    "summary": "Upload a resume file and get the parsed JSON output.",
                    "description": "Upload a resume in PDF format to receive a structured JSON response with the extracted details.",
                    "parameters": [
                        {
                            "name": "file",
                            "in": "formData",
                            "description": "The resume file to be parsed.",
                            "required": True,
                            "type": "file"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Resume successfully parsed.",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "resume": {
                                        "description": "The parsed resume JSON.",
                                        "type": "object"
                                    }
                                }
                            }
                        },
                        "400": {
                            "description": "Bad request if file is missing or invalid."
                        },
                        "500": {
                            "description": "Internal server error if processing fails."
                        }
                    }
                }
            }
        },
        "definitions": {}
    }

    Swagger(app, template=swagger_template)
