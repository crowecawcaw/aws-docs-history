

# Launching RCS in Brazil
<a name="rcs-country-launch-br"></a>

To launch your AWS RCS Agent in Brazil, submit a country launch registration using the `BR_RCS_LAUNCH_REGISTRATION` registration type. Brazil requires additional form fields and a brand approval email that you must send after submitting your registration.

## Registration form (console)
<a name="rcs-country-launch-br-console"></a>

The Brazil launch registration uses a custom form with additional fields beyond the standard baseline. The registration form collects the following information:
+ **Brand information** — Auto-populated from your testing agent configuration. You can review and adjust the brand name, description, website URL, and contact information.
+ **Use case selection** — Select the use case category for your RCS messaging.
+ **Tax code (CNPJ)** — Your Brazilian tax identification number (Cadastro Nacional da Pessoa Jurídica). This is required for all businesses operating in Brazil.
+ **Screenshot URL** — A URL to a screenshot demonstrating your RCS messaging experience.
+ **Brand approval** — Confirmation that you have authorization to use the brand for RCS messaging in Brazil.
+ **Privacy policy and terms of service** — URLs to your privacy policy and terms of service pages.

**Note**  
The Brazil registration form does not require a video URL. A screenshot URL is used instead.

## Brand approval email (required after registration)
<a name="rcs-country-launch-br-loa"></a>

**Important**  
After you submit your registration in the AWS End User Messaging console, you must send a brand approval email. Your registration cannot be approved until this email is received and validated.

The brand approval email is your authorization for AWS to operate an RCS agent on your behalf in Brazil. There is no separate document to sign or upload — the email itself serves as your Letter of Authorization (LOA).

Send the following email after you submit your registration:

```
To: aws-end-user-messaging-rcs-approvals@amazon.com
Subject: RCS Brand Approval [Agent Name] [Agent ID]

I, [Name] as [Role] at [Company Name], grant Amazon Web Services the right
to operate an RCS Business Messaging agent using the information specified
in this email.

Yours sincerely,

[Name]
[Role]
[Company Name]

Agent name: [Your Agent Display Name]
Brand CNPJ: [Your CNPJ Number]
Agent logo: [Attached or URL]
Agent hero image: [Attached or URL]
Agent description: [Your Agent Description]
Terms of service: [Your Terms of Service URL]
Privacy policy: [Your Privacy Policy URL]
Agent ID: [Your RCS for Business ID]
```

**Note**  
Your Agent ID (RCS for Business ID) can be found in the AWS End User Messaging console. Navigate to **SMS > RCS agents**, select your agent, then open the **Country launch status** tab. The Agent ID is listed as the **RCS for Business ID** in the Launch Status by Country section. The format is `{agent_name}_{unique_id}_agent`.

**Important**  
Send this email from the same email address you provided as the brand contact email in your registration form. Emails sent from a different address will not be accepted.
+ The sender (From address) must be the brand contact person listed in your registration form.
+ The CNPJ in the email must match what you entered in the registration form.
+ No additional paperwork, signatures, or uploads are needed — the email is the complete authorization.

## Approval timeline
<a name="rcs-country-launch-br-timeline"></a>

The Brazil approval process includes the following steps:

1. Submit the country launch registration in the AWS End User Messaging console.

1. Send the brand approval email to `aws-end-user-messaging-rcs-approvals@amazon.com`.

1. AWS validates the email and forwards the authorization to the carriers on your behalf.

1. Carrier review proceeds after brand authorization is validated.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).