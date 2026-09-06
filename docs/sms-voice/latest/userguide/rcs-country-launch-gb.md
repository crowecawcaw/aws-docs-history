

# Launching RCS in the United Kingdom
<a name="rcs-country-launch-gb"></a>

To launch your AWS RCS Agent in the United Kingdom, submit a country launch registration using the `GB_RCS_LAUNCH_REGISTRATION` registration type. The United Kingdom has a multi-step out-of-band approval process that involves direct communication with multiple carriers and third-party verification services.

**Important**  
The UK approval process is more complex than most countries. Plan for additional time and ensure your team is prepared to respond to emails from multiple parties. Read this entire section before submitting your registration.

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
Your company name and address must exactly match your Companies House registration. Discrepancies will cause delays in the approval process.

## Multi-step carrier approval (out-of-band requirement)
<a name="rcs-country-launch-gb-out-of-band"></a>

**Important**  
In addition to the console registration, you must complete a multi-step out-of-band approval process. Different carriers use different verification methods, and you will receive emails from multiple parties. Your registration cannot be fully approved until all carrier approvals are complete.

### Step 1: Proactive brand approval email (Three and Vodafone)
<a name="rcs-country-launch-gb-step1"></a>

After you submit your registration in the AWS End User Messaging console, you must send a proactive brand approval email to Three and Vodafone. This email authorizes these carriers to enable RCS messaging for your brand.

Send the email to both of the following addresses:
+ **Three**: `dan.cottle@three.co.uk`
+ **Vodafone**: `wholesaleorders@vodafone.com`

CC `aws-end-user-messaging-rcs-approvals@amazon.com` on all emails you send as part of this process.

Use the following email template:

```
Subject: [Agent Name] RBM Brand approval
CC: aws-end-user-messaging-rcs-approvals@amazon.com

Approval for Agent: [Agent ID]

I at [Brand/Company Name] confirm that I am authorized to use the following
name: [Agent Name], logo and images, as shown in the attached image file(s)
for the RBM agent.

I hereby confirm that I give permission to Amazon Web Services to register
this RBM agent and use the logo for the purpose of sending RBM messages to
users of Three and Vodafone Network(s) on our behalf.

[Full Name]
[Job Title]
[Company Name]
```

**Note**  
Your Agent ID (RCS for Business ID) can be found in the AWS End User Messaging console. Navigate to **SMS > RCS agents**, select your agent, then open the **Country launch status** tab. The Agent ID is listed as the **RCS for Business ID** in the Launch Status by Country section. The format is `{agent_name}_{unique_id}_agent`.

### Step 2: Brand Assure verification (BT/EE)
<a name="rcs-country-launch-gb-step2"></a>

For BT and EE carrier approval, a third-party service called Brand Assure contacts your brand's point of contact directly. You do not need to initiate this step — it happens automatically after your registration is submitted.
+ Brand Assure sends an email from `uksupport@brandassure.com` to the contact person listed in your registration.
+ The email contains instructions for verifying your brand identity for BT/EE.
+ You must respond to this email to complete the BT/EE approval.

**Warning**  
Ensure that your email system does not block or filter emails from the `@brandassure.com` domain. Add this domain to your email allowlist before submitting your registration.

**Warning**  
The Brand Assure approval has a **30-day validity period**. If the approval expires before your registration is complete, you must restart the Brand Assure verification process, which may incur additional fees.

### Step 3: Aegis verification (O2)
<a name="rcs-country-launch-gb-step3"></a>

For O2 carrier approval, a third-party service called Aegis contacts your brand's point of contact directly. You do not need to initiate this step — it happens automatically after your registration is submitted.
+ Aegis sends an email from `certify@aegismobile.com` to the contact person listed in your registration.
+ The email contains a two-factor authentication (2FA) PIN that you must use to complete the verification.
+ The 2FA PIN is valid for **7 days**. If the PIN expires, you must request a new one.
+ The overall Aegis verification process is valid for **45 days**.

**Warning**  
Ensure that your email system does not block or filter emails from the `@aegismobile.com` domain. Add this domain to your email allowlist before submitting your registration. If the Aegis email is filtered to spam or blocked, you will miss the 2FA PIN and the verification will expire.

## Approval timeline
<a name="rcs-country-launch-gb-timeline"></a>

The United Kingdom approval process includes the following steps:

1. Submit the country launch registration in the AWS End User Messaging console.

1. Send the proactive brand approval email to Three and Vodafone.

1. Respond to the Brand Assure email for BT/EE approval (arrives automatically).

1. Complete the Aegis 2FA verification for O2 approval (arrives automatically).

1. Each carrier independently completes their review.

**Note**  
Because each carrier has an independent approval process, your agent may reach PARTIAL status (some carriers approved) before all carriers complete their review. You can begin sending RCS messages to recipients on approved carriers while waiting for remaining approvals.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).