

# Launching RCS in the United Kingdom
<a name="rcs-country-launch-gb"></a>

To launch your AWS RCS agent in the United Kingdom, submit a country launch registration using the `GB_RCS_LAUNCH_REGISTRATION` registration type. The United Kingdom has a multi-step out-of-band approval process that involves direct communication with multiple carriers and third-party verification services.

**Important**  
The UK approval process is more complex than it is for most other countries. Plan for additional time and make sure that your team is prepared to respond to emails from multiple parties. Read this entire section before submitting your registration.

## Registration form (console)
<a name="rcs-country-launch-gb-console"></a>

The United Kingdom launch registration uses a custom form with additional fields beyond the standard baseline. The registration form collects the following information:
+ **Brand information** — Auto-populated from your testing agent configuration.
+ **Use case selection** — Select the use case category for your RCS messaging.
+ **Company name** — Your registered company name as it appears on Companies House.
+ **Industry** — The industry sector your company operates in.
+ **Registered company address** — Your company's registered address as listed on Companies House.
+ **Company registration number** — Your Companies House registration number.
+ **Screen recording** — A screen recording that demonstrates your RCS messaging experience. For detailed video requirements, see [Launch video requirements](rcs-compliance-video.md).
+ **Privacy policy and terms of service** — URLs to your privacy policy and terms of service pages.

**Note**  
Your company name and address must exactly match your Companies House registration. Discrepancies cause delays in the approval process.

## Multi-step carrier approval (out-of-band requirement)
<a name="rcs-country-launch-gb-out-of-band"></a>

**Important**  
In addition to the console registration, you must complete a multi-step out-of-band approval process. Different carriers use different verification methods, and you receive emails from multiple parties. Your registration cannot be fully approved until all carrier approvals are complete.

### Step 1: Proactive brand approval email (Vodafone and Three)
<a name="rcs-country-launch-gb-step1"></a>

After you submit your registration in the AWS End User Messaging console, you must send a proactive brand approval email to Three and Vodafone. This email authorizes these carriers to enable RCS messaging for your brand.

Send the email to `wholesaleorders@vodafone.com`. This address covers both Vodafone and Three.

CC both `aws-end-user-messaging-rcs-approvals@amazon.com` and `rcs_registrations@infobip.com` on all emails you send as part of this process.

Use the following email template:

```
Subject: [Agent Name] RBM Brand approval
CC: aws-end-user-messaging-rcs-approvals@amazon.com, rcs_registrations@infobip.com

Approval for Agent: [Agent ID]

I at [Brand/Company Name] confirm that I am authorized to use the following
name: [Agent Name], logo and images, as shown in the attached image file(s)
for the RBM agent.

I hereby confirm that I give permission to Infobip to register this RBM agent
and use the logo for the purpose of sending RBM messages to users of Three and
Vodafone Network(s) on our behalf.

[Full Name]
[Job Title]
[Company Name]
```

**Important**  
Attach both your agent logo and banner image to this email. The carriers use these images to validate your agent before they begin their checks. Without these images, the carriers cannot act on your email.

**Note**  
You can find your Agent ID (RCS for Business ID) in the AWS End User Messaging console. Navigate to **SMS > RCS agents**, select your agent, then open the **Country launch status** tab. The Agent ID is listed as the **RCS for Business ID** in the Launch Status by Country section. The format is `{agent_name}_{unique_id}_agent`.

### Step 2: Google brand approval email (Sky and Lycamobile)
<a name="rcs-country-launch-gb-step2"></a>

Google manages Sky and Lycamobile. For these carriers, the brand point of contact listed in your registration receives a brand approval email directly from Google. You do not need to initiate this step — it happens automatically after you submit your registration.
+ Check your inbox for an email from `rbm-support-noreply@google.com` with the subject "Please approve brand use for RCS for Business agent: <Agent ID>".
+ The approval confirms that the agent information is correct and authorizes the agent to represent your brand.

To grant approval, reply to the email with the following statement. Replace [Brand Contact Name] with the name of your brand's point of contact:

```
I, [Brand Contact Name] as a company representative, grant Infobip the right to
operate an RCS for Business agent using the information specified in this email.
```

**Important**  
Make sure that your email system does not block or filter emails from the `@google.com` domain. Add this domain to your email allowlist before submitting your registration. If this email is blocked or filtered, you miss the brand approval request from Google, and your registration cannot proceed until you locate and respond to it.

### Step 3: Brand Assure verification (BT/EE)
<a name="rcs-country-launch-gb-step3"></a>

For BT and EE carrier approval, a third-party service called Brand Assure contacts your brand's point of contact directly. You do not need to initiate this step — it happens automatically after you submit your registration.
+ Brand Assure sends an email from `uksupport@brandassure.com` to the contact person listed in your registration.
+ The email contains instructions for verifying your brand identity for BT/EE.
+ Review all of the information in the email. If everything is correct and you are ready to authorize Infobip to represent your brand, select **Approve**.
+ If anything is incorrect, or you do not approve the request, select **Reject** and provide the reason.

**Warning**  
Make sure that your email system does not block or filter emails from the `@brandassure.com` domain. Add this domain to your email allowlist before submitting your registration.

### Step 4: Aegis verification (O2)
<a name="rcs-country-launch-gb-step4"></a>

For O2 carrier approval, a third-party service called Aegis contacts your brand's point of contact directly. You do not need to initiate this step — it happens automatically after you submit your registration.
+ Aegis sends an email from `certify@aegismobile.com` with the subject "Action Required: Verify Your Email Address" to the contact person listed in your registration.
+ The email contains a two-factor authentication (2FA) PIN that you must use to complete the verification.
+ The 2FA PIN is valid for **7 days**. Aegis sends a reminder 48 hours before the PIN expires.
+ Brand vetting and verification remain valid for **45 days**. If you do not complete the 2FA verification within this period, resubmit the Brand Validation form.

**Warning**  
Make sure that your email system does not block or filter emails from the `@aegismobile.com` domain. Add this domain to your email allowlist before submitting your registration. If the Aegis email is filtered to spam or blocked, you will miss the 2FA PIN and the verification will expire.

## Approval timeline
<a name="rcs-country-launch-gb-timeline"></a>

The United Kingdom approval process includes the following steps:

1. Submit the country launch registration in the AWS End User Messaging console.

1. Send the proactive brand approval email for Vodafone and Three.

1. Approve the Google brand use email for Sky and Lycamobile (arrives automatically).

1. Respond to the Brand Assure email for BT/EE approval by choosing Approve or Reject (arrives automatically).

1. Complete the Aegis 2FA verification for O2 approval (arrives automatically).

1. Each carrier independently completes their review.

**Note**  
Because each carrier has an independent approval process, your agent might reach PARTIAL status (some carriers approved) before all carriers complete their review. You can begin sending RCS messages to recipients on approved carriers while waiting for remaining approvals.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).