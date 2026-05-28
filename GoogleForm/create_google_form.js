/**
 * Highlighting Social Issues in Fair Trade Practices - Google Apps Script
 * 
 * INSTRUCTIONS:
 * 1. Go to https://script.google.com/
 * 2. Create a new project
 * 3. Copy and paste this entire script
 * 4. Run the createGymRegistrationForm() function
 * 5. Grant necessary permissions when prompted
 * 6. The form URL will be logged in the console
 * 
 * To add the logo:
 * 1. Upload the logo (logo_0_0.png) to Google Drive
 * 2. Make it publicly accessible (Anyone with link)
 * 3. Get the file ID from the share link
 * 4. Update the LOGO_URL variable below with the proper URL
 */

// Replace with your logo's public Google Drive URL or other hosted URL
const LOGO_URL = 'https://drive.google.com/uc?id=YOUR_LOGO_FILE_ID';

function createFairTradeSurveyForm() {
  // Create the form
  const form = FormApp.create('Highlighting Social Issues in Fair Trade Practices');
  
  // Set form description
  form.setDescription('This survey aims to gather insights on social issues related to fair trade practices. Your responses will help us understand the impact of fair trade on communities and workers. All fields marked with * are required.');
  
  // Enable progress bar
  form.setProgressBar(true);
  
  // ===========================================
  // SECTION 1: PERSONAL INFORMATION
  // ===========================================
  form.addPageBreakItem()
    .setTitle('PERSONAL INFORMATION');
  
  form.addTextItem()
    .setTitle('Full Name')
    .setRequired(true);
  
  form.addDateItem()
    .setTitle('Date of Birth')
    .setRequired(true);
  
  form.addParagraphTextItem()
    .setTitle('Address')
    .setRequired(true);
  
  form.addTextItem()
    .setTitle('City')
    .setRequired(true);
  
  form.addTextItem()
    .setTitle('State')
    .setRequired(true);
  
  form.addTextItem()
    .setTitle('Pin Code')
    .setRequired(true)
    .setValidation(FormApp.createTextValidation()
      .requireTextMatchesPattern('[0-9]{6}')
      .setHelpText('Please enter a valid 6-digit PIN code')
      .build());
  
  form.addTextItem()
    .setTitle('Phone Number')
    .setRequired(true)
    .setValidation(FormApp.createTextValidation()
      .requireTextMatchesPattern('[0-9]{10}')
      .setHelpText('Please enter a valid 10-digit phone number')
      .build());
  
  form.addTextItem()
    .setTitle('Email Address')
    .setRequired(true)
    .setValidation(FormApp.createTextValidation()
      .requireTextIsEmail()
      .build());
  
  // ===========================================
  // SECTION 2: EMERGENCY CONTACT INFORMATION
  // ===========================================
  form.addPageBreakItem()
    .setTitle('EMERGENCY CONTACT INFORMATION');
  
  form.addTextItem()
    .setTitle('Emergency Contact Full Name')
    .setRequired(true);
  
  form.addTextItem()
    .setTitle('Emergency Contact Phone Number')
    .setRequired(true)
    .setValidation(FormApp.createTextValidation()
      .requireTextMatchesPattern('[0-9]{10}')
      .setHelpText('Please enter a valid 10-digit phone number')
      .build());
  
  form.addTextItem()
    .setTitle('Relationship with Emergency Contact')
    .setRequired(true);
  
  // ===========================================
  // SECTION 3: HEALTH & FITNESS INFORMATION
  // ===========================================
  form.addPageBreakItem()
    .setTitle('HEALTH & FITNESS INFORMATION');
  
  form.addMultipleChoiceItem()
    .setTitle('Do you have any medical condition or injuries we should be aware of?')
    .setChoiceValues(['Yes', 'No'])
    .setRequired(true);
  
  form.addParagraphTextItem()
    .setTitle('If yes, please explain your medical conditions or injuries')
    .setHelpText('Leave blank if not applicable')
    .setRequired(false);
  
  form.addCheckboxItem()
    .setTitle('Fitness Goals (Select all that apply)')
    .setChoiceValues([
      'Weight Loss',
      'Muscle Gain',
      'General Fitness',
      'Strength Training',
      'Cardio Improvement',
      'Flexibility',
      'Sports Training',
      'Stress Relief',
      'Other'
    ])
    .setRequired(true);
  
  form.addTextItem()
    .setTitle('Other Fitness Goals (if selected above)')
    .setRequired(false);
  
  // ===========================================
  // SECTION 4: MEMBERSHIP OPTIONS
  // ===========================================
  form.addPageBreakItem()
    .setTitle('MEMBERSHIP OPTIONS');
  
  form.addMultipleChoiceItem()
    .setTitle('Please select your membership plan')
    .setChoiceValues([
      'Monthly',
      'Quarterly',
      'Annual',
      'Other'
    ])
    .setRequired(true);
  
  form.addTextItem()
    .setTitle('If you selected "Other", please specify')
    .setRequired(false);
  
  // ===========================================
  // SECTION 5: PREFERRED PAYMENT OPTIONS
  // ===========================================
  form.addPageBreakItem()
    .setTitle('PREFERRED PAYMENT OPTIONS');
  
  form.addMultipleChoiceItem()
    .setTitle('Please choose your preferred payment method')
    .setChoiceValues([
      'Cash',
      'Paytm',
      'PhonePe',
      'Google Pay'
    ])
    .setRequired(true);
  
  form.addCheckboxItem()
    .setTitle('Payment Authorization')
    .setChoiceValues([
      'I authorize the gym to automatically charge my selected payment method for membership renewals and other related charges. I understand that I can update or cancel this authorization at any time.'
    ])
    .setRequired(true);
  
  // ===========================================
  // SECTION 6: CONSENT AND WAIVERS
  // ===========================================
  form.addPageBreakItem()
    .setTitle('CONSENT AND WAIVERS');
  
  // Consent 1: Exercise at Your Own Risk
  form.addSectionHeaderItem()
    .setTitle('1. Exercise at Your Own Risk')
    .setHelpText('I understand that participating in physical activity at this gym carries risks. I agree to exercise at my own risk and acknowledge that the gym is not responsible for any injuries or health issues that may arise. I have consulted with my physician and am fit to undertake an exercise program.');
  
  form.addCheckboxItem()
    .setTitle('Exercise Risk Acknowledgement')
    .setChoiceValues([
      'I acknowledge and accept the exercise risks as stated above'
    ])
    .setRequired(true);
  
  // Consent 2: Marketing Consent
  form.addSectionHeaderItem()
    .setTitle('2. Marketing Consent')
    .setHelpText('I consent to receive marketing communications, newsletters, and promotions from the gym via email, SMS, or phone. I understand that I can unsubscribe at any time by following the instructions provided in the communications.');
  
  form.addMultipleChoiceItem()
    .setTitle('Marketing Communications')
    .setChoiceValues([
      'Yes, I consent to receive marketing communications',
      'No, I do not wish to receive marketing communications'
    ])
    .setRequired(true);
  
  // Consent 3: Consent to Use of Image
  form.addSectionHeaderItem()
    .setTitle('3. Consent to Use of Image')
    .setHelpText('I give permission for the gym to take photographs or videos of me during workouts or gym events for promotional purposes (social media, website, advertising). I understand that I will not receive compensation for the use of these images.');
  
  form.addMultipleChoiceItem()
    .setTitle('Image/Video Consent')
    .setChoiceValues([
      'Yes, I give permission to use my image/video',
      'No, I do not give permission to use my image/video'
    ])
    .setRequired(true);
  
  // Consent 4: Personal Data Protection
  form.addSectionHeaderItem()
    .setTitle('4. Personal Data Protection')
    .setHelpText('I understand that my personal data will be processed in accordance with applicable privacy laws, including GDPR and the California Consumer Privacy Act (CCPA). The gym may collect, store, and use my personal data for membership management, billing, and communication purposes. I acknowledge that I have the right to access, correct, or request deletion of my personal data by contacting the gym.');
  
  form.addCheckboxItem()
    .setTitle('Data Protection Acknowledgement')
    .setChoiceValues([
      'I acknowledge and accept the personal data protection terms as stated above'
    ])
    .setRequired(true);
  
  // ===========================================
  // SECTION 7: FINAL ACKNOWLEDGEMENT
  // ===========================================
  form.addPageBreakItem()
    .setTitle('ACKNOWLEDGEMENT');
  
  form.addCheckboxItem()
    .setTitle('Final Acknowledgement')
    .setChoiceValues([
      'By checking this box, I confirm that I have read and understood the gym\'s terms and conditions, including the waivers, consents, and privacy policies outlined above.'
    ])
    .setRequired(true);
  
  form.addTextItem()
    .setTitle('Your Full Name (as digital signature)')
    .setHelpText('Please type your full name as acknowledgement of this registration')
    .setRequired(true);
  
  form.addDateItem()
    .setTitle('Date')
    .setRequired(true);
  
  // Set confirmation message
  form.setConfirmationMessage('Thank you for registering with our gym! A gym representative will contact you shortly to complete the registration process. Welcome to the fitness family!');
  
  // Log the form URL
  Logger.log('Form created successfully!');
  Logger.log('Edit URL: ' + form.getEditUrl());
  Logger.log('Published URL: ' + form.getPublishedUrl());
  
  // Return form URLs
  return {
    editUrl: form.getEditUrl(),
    publishedUrl: form.getPublishedUrl()
  };
}

/**
 * Function to set the form header image (logo)
 * 
 * IMPORTANT: You need to:
 * 1. Upload logo_0_0.png to Google Drive
 * 2. Get the file ID from the share link
 * 3. Run this function with the file ID
 * 
 * Example: If your share link is https://drive.google.com/file/d/1ABC123xyz/view
 * Then the file ID is: 1ABC123xyz
 */
function setFormLogo(formId, logoFileId) {
  const form = FormApp.openById(formId);
  const logoFile = DriveApp.getFileById(logoFileId);
  const logoBlob = logoFile.getBlob();
  
  // Note: Google Forms API doesn't directly support setting header images via Apps Script
  // You'll need to set this manually in the form editor
  Logger.log('To add the logo:');
  Logger.log('1. Open the form in edit mode');
  Logger.log('2. Click on the header area');
  Logger.log('3. Select "Choose image"');
  Logger.log('4. Upload the logo_0_0.png file');
}

/**
 * Run this function to create the form
 */
function main() {
  const result = createGymRegistrationForm();
  Logger.log('==========================================');
  Logger.log('GYM REGISTRATION FORM CREATED SUCCESSFULLY');
  Logger.log('==========================================');
  Logger.log('');
  Logger.log('Share this link with members to fill out the form:');
  Logger.log(result.publishedUrl);
  Logger.log('');
  Logger.log('Use this link to edit the form:');
  Logger.log(result.editUrl);
  Logger.log('');
  Logger.log('NEXT STEPS:');
  Logger.log('1. Open the edit URL');
  Logger.log('2. Click the paint palette icon to customize colors');
  Logger.log('3. Click the header area and upload your logo (logo_0_0.png)');
}
