

# Healthcare Providers
<a name="registration-help-vertical-healthcare"></a>

This guide covers A2P SMS registration requirements specific to healthcare providers, clinics, hospitals, and medical practices. Healthcare messaging is permitted but requires careful attention to patient privacy, consent mechanisms, and content restrictions.

## What's allowed
<a name="registration-help-vertical-healthcare-what-s-allowed"></a>
+ Appointment reminders and scheduling confirmations
+ Prescription refill notifications
+ Lab result availability alerts (without including results in the message)
+ Post-visit follow-up and care instructions
+ Billing and payment reminders
+ Patient portal notifications
+ Preventive care and wellness check reminders
+ Telehealth session links and reminders

## What's prohibited
<a name="registration-help-vertical-healthcare-what-s-prohibited"></a>
+ **Third-party lead generation** – Healthcare marketing from third-party aggregators who sell patient data to multiple clinics is prohibited.
+ **Medical debt collection** – Messaging related to medical debt collection or credit repair is highly restricted and often blocked.
+ **Shared opt-ins** – You cannot use a blanket consent form. A patient opting into a hospital's alerts does not automatically opt them into messages from an unrelated pharmacy or specialist.
+ **High-risk marketing** – Promotional cold texts for elective procedures or supplements to individuals who have not provided express consent are strictly forbidden.
+ **Public URL shorteners** – Using generic URL shorteners (like bit.ly) is flagged as spam. Use full, branded domains.

## Common denial reasons
<a name="registration-help-vertical-healthcare-common-denial-reasons"></a>

### Brand identity issues
<a name="registration-help-vertical-healthcare-brand-identity-issues"></a>


**Denial title reference**  

| Denial title | What it means for healthcare providers | 
| --- | --- | 
| Invalid brand URL | Your practice website is inaccessible or under construction. Reviewers must verify your medical practice exists and offers healthcare services. | 
| Insufficient website content | A patient portal login page alone is insufficient. Your site must show practice information, services offered, provider details, and contact information. | 
| Website requires authentication | Your primary URL leads to a patient portal login. Provide a publicly accessible page describing your practice – not the portal login screen. | 
| Website contains only a form | A standalone appointment booking form without surrounding practice context is insufficient. Add practice details, provider bios, and service descriptions around the form. | 
| Invalid brand business connection | The brand name on your registration doesn't match the entity on your website or medical license. Common when practices operate under a health system umbrella but register independently. | 
| DBA name mismatch | Your "Doing Business As" name doesn't match what appears on your website or patient-facing materials. Common when practices rebrand or join a health network. | 
| Public email domain | Using Gmail or Yahoo for a medical practice appears unprofessional and raises legitimacy concerns. Use your practice domain (e.g., info@smithfamilymedicine.com). | 

### Campaign description issues
<a name="registration-help-vertical-healthcare-campaign-description-issues"></a>


**Denial title reference**  

| Denial title | What it means for healthcare providers | 
| --- | --- | 
| Campaign unclear | Your description doesn't clearly explain what messages patients will receive. "Healthcare communications" is too vague. Specify something like: "Appointment reminders, prescription refill notifications, and billing alerts for established patients of Smith Family Medicine." | 
| Campaign not qualified for use case | The selected use case category doesn't match your actual messaging. Healthcare providers typically register under "Customer Care" or "Account Notifications" – not "Marketing" unless sending promotional wellness content. | 
| Campaign to brand mismatch | The campaign describes services for a different practice or health system than what's registered. Each practice location or brand needs its own registration. | 
| Multiple brands in one campaign | If your health system has multiple practice brands, each needs a separate campaign. Don't combine "Smith Cardiology" and "Smith Primary Care" in one registration. | 
| Campaign mismatch | Your campaign description says "appointment reminders" but your samples include marketing offers for elective procedures. Description and samples must align. | 

### Opt-in workflow issues
<a name="registration-help-vertical-healthcare-opt-in-workflow-issues"></a>


**Denial title reference**  

| Denial title | What it means for healthcare providers | 
| --- | --- | 
| Opt-in workflow insufficient consent | Your patient intake form collects a phone number but doesn't explicitly state the patient will receive SMS messages. A phone number field on a medical form is not SMS consent. | 
| Opt-in workflow missing | No screenshot or URL showing where patients agree to receive texts. Provide your patient intake form, portal enrollment screen, or paper form showing the SMS consent section. | 
| Opt-in workflow mismatch | The practice name on your opt-in form doesn't match your registered brand. For example, your form might say "Downtown Medical Associates" but you registered as "DMA Health LLC." This difference triggers a mismatch. | 
| Marketing consent not separated | Your form bundles marketing SMS consent (wellness promotions, new service announcements) with transactional consent (appointment reminders). Marketing opt-in must be a separate, unchecked checkbox. | 
| Opt-in checkbox missing or pre-selected | Your patient intake form has a pre-checked SMS consent box. TCPA requires patients to actively check the box themselves – it cannot be pre-selected. | 
| Opt-in workflow non compliant message frequency disclosure | Your consent language doesn't tell patients how often they'll hear from you. Add: "You may receive up to 8 messages per month regarding appointments, prescriptions, and billing." | 
| Opt-in workflow non-compliant HELP or STOP | Your opt-in disclosure is missing instructions for how to get help or opt out. Include: "Reply STOP to unsubscribe. Reply HELP for support." | 
| Opt-in workflow non compliant message and data rates disclosure | Missing the "Message and data rates may apply" disclosure near your consent language. | 
| Opt-in workflow non compliant privacy policy | Your opt-in flow doesn't link to a privacy policy. Or it doesn't state that mobile opt-in data won't be shared with third parties. This is critical for healthcare – patients expect strict data handling. | 
| Opt-in data shared with third parties | Your opt-in indicates patient data may be shared with affiliated practices, referral networks, or marketing partners. Each entity that will send messages needs its own consent. | 
| Incomplete opt-in workflow details | You selected multiple opt-in methods (website \+ paper form) but only described one. Provide complete details for every opt-in method – especially paper forms common in healthcare. | 
| Non-compliant consent language | Your consent language is missing required elements. Must include: message types, frequency, "Message and data rates may apply," and opt-out instructions. | 

### Sample message issues
<a name="registration-help-vertical-healthcare-sample-message-issues"></a>


**Denial title reference**  

| Denial title | What it means for healthcare providers | 
| --- | --- | 
| Sample message(s) mismatch | Your sample messages don't match the use case you described. If you registered for "appointment reminders" but samples show marketing for cosmetic procedures, this triggers a mismatch. | 
| Sample message(s) URL shortener | Messages contain bit.ly or other shortened links. Use your full practice domain (e.g., smithmedicine.com/portal). | 
| Sample messages(s) embedded phone number | If you selected the 'embedded phone number' option during registration, your sample messages must contain a phone number. Otherwise, deselect that option during resubmission. | 
| Sample messages use case mismatch | Your samples show messages for a different use case than what you registered. Ensure samples reflect actual appointment reminders, billing alerts, or whatever you declared. | 

### Opt-out and HELP message issues
<a name="registration-help-vertical-healthcare-opt-out-and-help-message-issues"></a>


**Denial title reference**  

| Denial title | What it means for healthcare providers | 
| --- | --- | 
| Non-compliant opt-out message | Your opt-out confirmation must acknowledge the request and confirm no further messages will be sent. Include your practice name. | 
| Help message mismatch | The practice name or email domain in your HELP response doesn't match your registered brand. | 
| Non-compliant help message | Your HELP reply must include your practice name and at least one contact method (phone, email, or website). | 

## Healthcare-specific registration tips
<a name="registration-help-vertical-healthcare-healthcare-specific-registration-tips"></a>

### Describe your use case precisely
<a name="registration-help-vertical-healthcare-describe-your-use-case-precisely"></a>

**Bad:** "We send healthcare messages to patients."

**Good:** "We send appointment reminders, prescription refill notifications, lab result availability alerts, and billing statements to established patients of Smith Family Medicine who opted in during patient intake."

### Separate marketing from patient care
<a name="registration-help-vertical-healthcare-separate-marketing-from-patient-care"></a>

If you send both care-related (appointment reminders, refill alerts) and marketing (new service announcements, wellness promotions) messages, register them as separate campaigns:
+ **Campaign 1 (Customer Care):** "Appointment reminders, prescription refill notifications, and billing alerts for established patients."
+ **Campaign 2 (Marketing):** "Preventive care promotions and new service announcements sent to patients who separately opted in to marketing communications."

### Paper form opt-in
<a name="registration-help-vertical-healthcare-paper-form-opt-in"></a>

Many healthcare practices collect SMS consent on paper intake forms. This is valid but requires:

1. A clearly labeled SMS consent section (not buried in general consent-to-treat)

1. An unchecked checkbox or signature line specifically for text messaging

1. Language stating: "I agree to receive text messages from [Practice Name] regarding appointments, prescriptions, and billing"

1. Message frequency disclosure

1. "Message and data rates may apply"

1. STOP/HELP instructions

1. Reference to privacy policy

**For registration:** Photograph or scan the relevant section of your paper form. Then host it at a publicly accessible URL, or upload a screenshot showing the SMS consent portion.

### Patient portal opt-in
<a name="registration-help-vertical-healthcare-patient-portal-opt-in"></a>

If patients opt in through your patient portal:

1. Capture a screenshot of the SMS preferences screen

1. Host it at a public URL (the portal itself requires login, but the screenshot must be accessible to reviewers)

1. Ensure the portal consent screen includes all required disclosures

### Multi-location practices
<a name="registration-help-vertical-healthcare-multi-location-practices"></a>

If your practice has multiple locations under one brand, you can use a single campaign registration. Locations might operate under different brand names (for example, "Smith Cardiology" vs. "Smith Orthopedics"). In that case, register each as a separate campaign.

### Privacy policy requirements
<a name="registration-help-vertical-healthcare-privacy-policy-requirements"></a>

Your privacy policy must explicitly state that mobile opt-in data will not be shared with third parties. For healthcare providers, this is especially important because:
+ Patients expect heightened privacy protections
+ Referral networks and affiliated practices are considered third parties for messaging purposes
+ Marketing partners or patient engagement platforms cannot receive opt-in data without explicit disclosure

## Opt-in form example
<a name="registration-help-vertical-healthcare-optin-example"></a>

For a healthcare paper form opt-in form example, see the form screenshots in this section. This vertical follows the [Transactional opt-in](registration-help-optin-transactional.md) with industry-specific disclosures.

![Patient intake form showing an unchecked SMS consent checkbox with message frequency, data rates, and opt-out disclosures](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/vertical-healthcare-optin.png)


## GLP-1 and metabolic medications
<a name="registration-help-vertical-healthcare-glp1"></a>

Campaigns involving GLP-1 receptor agonists and similar weight-loss or metabolic medications are subject to additional restrictions beyond standard healthcare messaging.

### Prohibited for GLP-1
<a name="registration-help-vertical-healthcare-glp1-prohibited"></a>

The use of SMS for the **marketing or promotion** of GLP-1 receptor agonists and related metabolic medications is strictly prohibited. Messages must not include the prescription drug or brand name.

### Approved use cases for GLP-1
<a name="registration-help-vertical-healthcare-glp1-allowed"></a>

Campaign submissions will only be approved if the messaging intent is purely informational or transactional:
+ Two-factor authentication (2FA) and identity verification
+ Transactional notifications (order confirmations, payment receipts, billing)
+ Logistics updates (delivery tracking, shipping status)
+ Account management (appointment reminders, account alerts)
+ Marketing for rewards programs unrelated to the prescription

### Regulatory requirements for GLP-1
<a name="registration-help-vertical-healthcare-glp1-requirements"></a>
+ **FDA approval required** – Products must have formal FDA approval. Lack of approval significantly increases the likelihood of rejection.
+ **Legal in all 50 states** – Products must be legal in all 50 U.S. states. If restricted in even one state, the campaign will be rejected.