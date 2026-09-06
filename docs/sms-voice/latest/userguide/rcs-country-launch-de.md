

# Launching RCS in Germany
<a name="rcs-country-launch-de"></a>

To launch your AWS RCS Agent in Germany, submit a country launch registration using the `DE_RCS_LAUNCH_REGISTRATION` registration type. Germany requires an additional out-of-band brand verification step that you must complete outside the AWS End User Messaging console.

## Registration form (console)
<a name="rcs-country-launch-de-console"></a>

The Germany launch registration uses the standard baseline form. The registration form collects the following information:
+ **Brand information** — Auto-populated from your testing agent configuration. You can review and adjust the brand name, description, website URL, and contact information.
+ **Use case selection** — Select the use case category for your RCS messaging.
+ **Screen recording** — A screen recording that demonstrates your RCS messaging experience. For detailed video requirements, see [Launch video requirements](rcs-compliance-video.md).
+ **Privacy policy and terms of service** — URLs to your privacy policy and terms of service pages.

**Important**  
Your privacy policy and terms of service URLs must link to pages written in the German language. Non-German privacy policies or terms of service will result in registration denial by German carriers.

## Brand Verification Letter (out-of-band requirement)
<a name="rcs-country-launch-de-brand-verification"></a>

**Important**  
In addition to the console registration, you must complete a brand verification step outside of AWS End User Messaging. Your registration cannot be approved until the Brand Verification Letter is received and validated.

After you submit your registration in the AWS End User Messaging console, you must send a signed Brand Verification Letter by email to the German RCS approval authority. This letter confirms that your organization authorizes the use of your brand for RCS messaging in Germany.

### Letter requirements
<a name="rcs-country-launch-de-letter-requirements"></a>
+ The letter must be signed by the brand's contact person (the same person listed in the registration form).
+ The contact person must use a business email address (free email providers such as Gmail or Yahoo are not accepted).
+ The letter can be signed by hand (scanned copy) or with a verified digital signature.

### Brand Verification Letter form
<a name="rcs-country-launch-de-brand-verification-form"></a>

Download the Brand Verification Letter template, fill in the required fields, sign it, and send it by email to the German RCS approval authority.

Download the Brand Verification Letter template: [Germany\_RCS\_BrandVerificationLetter.zip](samples/Germany_RCS_BrandVerificationLetter.zip)

The Brand Verification Letter is a bilingual (English/German) form (.docx) with the following fields to fill in:
+ **BRAND OWNER / MARKENINHABER** — Your company name (the brand owner).
+ **BRAND NAME / MARKENNAME** — Your RCS agent brand name.
+ **CONTACT NAME / KONTAKTPERSON** — The contact person for this registration. This must be the same person listed in the registration form.
+ **CONTACT EMAIL / KONTAKT EMAIL** — A business email address. Free email providers such as Gmail or Yahoo are not accepted.
+ **RBM SUPPLIER / DIENSTLEISTER** — Enter `Infobip`.

The letter body (pre-printed in the form) states:

"Dear German Mobile Network Operators, We hereby confirm the launch and operations of RBM agent(s) on our behalf. The Supplier of choice is authorised to use the Agent Name(s) and the Brand's logo as the originating name displayed to end users on the handset."

After filling in the fields, sign the letter. You can sign by hand (then scan the document) or use a verified digital signature.

### Email template
<a name="rcs-country-launch-de-email-template"></a>

After you have filled in and signed the Brand Verification Letter, compose an email with the signed letter and your brand logo attached. Use the following template:

```
FROM: [Your business email address]
TO: brandapproval@rcsbusinessmessaging.de
CC: aws-end-user-messaging-rcs-approvals@amazon.com
SUBJECT: RCS Brand Approval - [Your Brand Name]

Dear Team,

I at [Your Brand/Company Name] hereby give permission that Infobip may use
the brand name and logo for the use of sending RCS messages to users of the
German mobile networks.

Agent ID: [Your RCS for Business ID]

Regards,
[Your Name]
[Your Job Title]

ATTACHMENTS:
  1. Signed Brand Verification Letter (filled .docx or scanned PDF)
  2. Your brand logo file
```

**Note**  
Your Agent ID (RCS for Business ID) can be found in the AWS End User Messaging console. Navigate to **SMS > RCS agents**, select your agent, then open the **Country launch status** tab. The Agent ID is listed as the **RCS for Business ID** in the Launch Status by Country section. The format is `{agent_name}_{unique_id}_agent`.

**Important**  
Requirements for the email submission:  
The contact email in the Brand Verification Letter form must be a business email address. Free email providers such as Gmail or Yahoo are not accepted.
The contact person who signs the letter must be the same person listed in the registration form.
Enter `Infobip` in the RBM SUPPLIER / DIENSTLEISTER field.
The letter can be signed by hand (then scanned to PDF) or with a verified digital signature.
Attach both the signed Brand Verification Letter and your brand logo file to the email.

## Approval timeline
<a name="rcs-country-launch-de-timeline"></a>

The Germany approval process includes the following steps:

1. Submit the country launch registration in the AWS End User Messaging console.

1. Send the signed Brand Verification Letter to `brandapproval@rcsbusinessmessaging.de`.

1. The approval authority validates the letter and confirms your brand identity.

1. Carrier review proceeds after brand verification is complete.

**Note**  
Your registration remains in the REVIEWING state until both the brand verification and carrier review are complete. Submit the Brand Verification Letter promptly after submitting your registration to avoid delays.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).