#!/usr/bin/env python3
"""
Highlighting Social Issues in Fair Trade Practices - Google Forms Creator
Uses Google Forms API to create the form programmatically.

SETUP INSTRUCTIONS:
1. Go to https://console.cloud.google.com/
2. Create a new project (or select existing)
3. Enable "Google Forms API" and "Google Drive API"
4. Go to "APIs & Services" > "Credentials"
5. Click "Create Credentials" > "OAuth client ID"
6. Select "Desktop app" and create
7. Download the JSON file and save as "credentials.json" in this folder
8. Run this script: python create_form.py
"""

import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes required for Forms and Drive API
SCOPES = [
    'https://www.googleapis.com/auth/forms.body',
    'https://www.googleapis.com/auth/drive'
]

def get_credentials():
    """Get or refresh OAuth credentials."""
    creds = None
    
    # Check for existing token
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Refresh or get new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("\n❌ ERROR: credentials.json not found!")
                print("\nPlease follow these steps:")
                print("1. Go to https://console.cloud.google.com/")
                print("2. Create/select a project")
                print("3. Enable 'Google Forms API' and 'Google Drive API'")
                print("4. Go to 'APIs & Services' > 'Credentials'")
                print("5. Click 'Create Credentials' > 'OAuth client ID'")
                print("6. Select 'Desktop app' and create")
                print("7. Download JSON and save as 'credentials.json' here")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def create_gym_registration_form():
    """Create the complete gym registration form."""
    
    creds = get_credentials()
    if not creds:
        return None
    
    # Build the Forms API service
    forms_service = build('forms', 'v1', credentials=creds)
    
    # Create the form with title
    form = {
        "info": {
            "title": "GYM MEMBER REGISTRATION FORM",
            "documentTitle": "GYM MEMBER REGISTRATION FORM"
        }
    }
    
    result = forms_service.forms().create(body=form).execute()
    form_id = result['formId']
    print(f"✅ Form created with ID: {form_id}")
    
    # Build all form items
    requests = []
    index = 0
    
    # Form description
    requests.append({
        "updateFormInfo": {
            "info": {
                "description": "Please fill out this registration form to become a member of our gym. All fields marked with * are required."
            },
            "updateMask": "description"
        }
    })
    
    # ========== PERSONAL INFORMATION ==========
    requests.append(create_section_header(index, "PERSONAL INFORMATION"))
    index += 1
    
    requests.append(create_text_question(index, "Full Name", True))
    index += 1
    
    requests.append(create_date_question(index, "Date of Birth", True))
    index += 1
    
    requests.append(create_paragraph_question(index, "Address", True))
    index += 1
    
    requests.append(create_text_question(index, "City", True))
    index += 1
    
    requests.append(create_text_question(index, "State", True))
    index += 1
    
    requests.append(create_text_question(index, "Pin Code", True, regex="[0-9]{6}"))
    index += 1
    
    requests.append(create_text_question(index, "Phone Number", True, regex="[0-9]{10}"))
    index += 1
    
    requests.append(create_text_question(index, "Email Address", True))
    index += 1
    
    # ========== EMERGENCY CONTACT ==========
    requests.append(create_section_header(index, "EMERGENCY CONTACT INFORMATION"))
    index += 1
    
    requests.append(create_text_question(index, "Emergency Contact Full Name", True))
    index += 1
    
    requests.append(create_text_question(index, "Emergency Contact Phone Number", True, regex="[0-9]{10}"))
    index += 1
    
    requests.append(create_text_question(index, "Relationship with Emergency Contact", True))
    index += 1
    
    # ========== HEALTH & FITNESS ==========
    requests.append(create_section_header(index, "HEALTH & FITNESS INFORMATION"))
    index += 1
    
    requests.append(create_multiple_choice(index, "Do you have any medical condition or injuries we should be aware of?", ["Yes", "No"], True))
    index += 1
    
    requests.append(create_paragraph_question(index, "If yes, please explain your medical conditions or injuries", False))
    index += 1
    
    requests.append(create_checkbox_question(index, "Fitness Goals (Select all that apply)", [
        "Weight Loss", "Muscle Gain", "General Fitness", "Strength Training",
        "Cardio Improvement", "Flexibility", "Sports Training", "Stress Relief", "Other"
    ], True))
    index += 1
    
    requests.append(create_text_question(index, "Other Fitness Goals (if selected above)", False))
    index += 1
    
    # ========== MEMBERSHIP OPTIONS ==========
    requests.append(create_section_header(index, "MEMBERSHIP OPTIONS"))
    index += 1
    
    requests.append(create_multiple_choice(index, "Please select your membership plan", ["Monthly", "Quarterly", "Annual", "Other"], True))
    index += 1
    
    requests.append(create_text_question(index, "If you selected 'Other', please specify", False))
    index += 1
    
    # ========== PAYMENT OPTIONS ==========
    requests.append(create_section_header(index, "PREFERRED PAYMENT OPTIONS"))
    index += 1
    
    requests.append(create_multiple_choice(index, "Please choose your preferred payment method", ["Cash", "Paytm", "PhonePe", "Google Pay"], True))
    index += 1
    
    requests.append(create_checkbox_question(index, "Payment Authorization", [
        "I authorize the gym to automatically charge my selected payment method for membership renewals and other related charges."
    ], True))
    index += 1
    
    # ========== CONSENT AND WAIVERS ==========
    requests.append(create_section_header(index, "CONSENT AND WAIVERS"))
    index += 1
    
    requests.append(create_checkbox_question(index, "1. Exercise at Your Own Risk - I understand that participating in physical activity carries risks. I agree to exercise at my own risk.", [
        "I acknowledge and accept the exercise risks"
    ], True))
    index += 1
    
    requests.append(create_multiple_choice(index, "2. Marketing Consent - Do you consent to receive marketing communications?", [
        "Yes, I consent to receive marketing communications",
        "No, I do not wish to receive marketing communications"
    ], True))
    index += 1
    
    requests.append(create_multiple_choice(index, "3. Consent to Use of Image - Do you give permission for photos/videos during workouts?", [
        "Yes, I give permission",
        "No, I do not give permission"
    ], True))
    index += 1
    
    requests.append(create_checkbox_question(index, "4. Personal Data Protection - I understand my data will be processed according to privacy laws.", [
        "I acknowledge and accept the data protection terms"
    ], True))
    index += 1
    
    # ========== ACKNOWLEDGEMENT ==========
    requests.append(create_section_header(index, "ACKNOWLEDGEMENT"))
    index += 1
    
    requests.append(create_checkbox_question(index, "Final Acknowledgement", [
        "I confirm that I have read and understood the gym's terms, waivers, and privacy policies."
    ], True))
    index += 1
    
    requests.append(create_text_question(index, "Your Full Name (as digital signature)", True))
    index += 1
    
    requests.append(create_date_question(index, "Date", True))
    
    # Execute batch update
    batch_update = {"requests": requests}
    forms_service.forms().batchUpdate(formId=form_id, body=batch_update).execute()
    
    # Get form URLs
    form_url = f"https://docs.google.com/forms/d/{form_id}/viewform"
    edit_url = f"https://docs.google.com/forms/d/{form_id}/edit"
    
    print("\n" + "="*50)
    print("✅ GYM REGISTRATION FORM CREATED SUCCESSFULLY!")
    print("="*50)
    print(f"\n📝 Form URL (share with members):\n   {form_url}")
    print(f"\n✏️  Edit URL (to customize):\n   {edit_url}")
    print("\n📌 NEXT STEPS:")
    print("   1. Open the Edit URL above")
    print("   2. Click the header area to add your logo")
    print("   3. Use the palette icon to customize colors")
    
    return form_id

def create_section_header(index, title):
    return {
        "createItem": {
            "item": {
                "title": title,
                "description": "",
                "textItem": {}
            },
            "location": {"index": index}
        }
    }

def create_text_question(index, title, required, regex=None):
    item = {
        "createItem": {
            "item": {
                "title": title,
                "questionItem": {
                    "question": {
                        "required": required,
                        "textQuestion": {
                            "paragraph": False
                        }
                    }
                }
            },
            "location": {"index": index}
        }
    }
    return item

def create_paragraph_question(index, title, required):
    return {
        "createItem": {
            "item": {
                "title": title,
                "questionItem": {
                    "question": {
                        "required": required,
                        "textQuestion": {
                            "paragraph": True
                        }
                    }
                }
            },
            "location": {"index": index}
        }
    }

def create_date_question(index, title, required):
    return {
        "createItem": {
            "item": {
                "title": title,
                "questionItem": {
                    "question": {
                        "required": required,
                        "dateQuestion": {
                            "includeTime": False,
                            "includeYear": True
                        }
                    }
                }
            },
            "location": {"index": index}
        }
    }

def create_multiple_choice(index, title, options, required):
    return {
        "createItem": {
            "item": {
                "title": title,
                "questionItem": {
                    "question": {
                        "required": required,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [{"value": opt} for opt in options]
                        }
                    }
                }
            },
            "location": {"index": index}
        }
    }

def create_checkbox_question(index, title, options, required):
    return {
        "createItem": {
            "item": {
                "title": title,
                "questionItem": {
                    "question": {
                        "required": required,
                        "choiceQuestion": {
                            "type": "CHECKBOX",
                            "options": [{"value": opt} for opt in options]
                        }
                    }
                }
            },
            "location": {"index": index}
        }
    }

if __name__ == "__main__":
    create_gym_registration_form()
