

# Notify mobile carrier prerequisites
<a name="notify-compliance"></a>

When using AWS End User Messaging Notify, you are responsible for complying with applicable messaging laws and mobile carrier requirements in each country or region where your customers are located. Consult an attorney to assess compliance obligations. Non-compliance with these requirements may result in carrier audit and removal of your access to Notify. This page specifies mobile-carrier mandated prerequisites for using Notify, including the minimum required language you must make available to your customers detailing your terms and conditions, privacy policy, and opt-in flow applicable to your messaging.

**Important**  
You must publish your own terms and conditions and privacy policy pages that include the required language described below. You must also implement an opt-in flow before sending messages through Notify. These requirements apply to both Basic and Advanced tiers.

## Required terms and conditions
<a name="notify-compliance-terms"></a>

Mobile carriers require that you make a specific set of messaging terms and conditions available to your customers. Your terms and conditions page must include, at minimum, the following information. Replace the bracketed placeholders with your own values.

```
Subscribers will opt-in via [YOUR_WEBSITE_URL] to receive verification
messages from [YOUR_COMPANY_NAME], powered by AWS Notify. Message
frequency may vary per user.

Text "HELP" for help. Text "STOP" to cancel.

Message and data rates may apply for any messages sent to you from us
and to us from you. Carriers are not liable for delayed or undelivered
messages.

If you have any questions about your text plan or data plan, contact
your wireless provider.

For all questions about the services provided, you can send an email
to [YOUR_SUPPORT_EMAIL] or call [YOUR_SUPPORT_PHONE_NUMBER].

If you have questions regarding privacy, please read our privacy policy
at [YOUR_PRIVACY_POLICY_URL].
```

**Important**  
You must host this content at a publicly accessible URL and link to it from your opt-in flow.

## Required privacy policy
<a name="notify-compliance-privacy"></a>

Mobile carriers also require that you make a privacy policy available to your customers. Your privacy policy page must include, at minimum, the following statements:
+ No mobile numbers will be shared with third parties or affiliates for marketing or promotional purposes.
+ Text messaging originator opt-in data and consent will not be shared with any third parties.
+ Messages are delivered through AWS Notify. AWS does not share end user phone numbers with third parties for marketing or promotional purposes.

**Important**  
You must host this content at a publicly accessible URL. Your terms and conditions page must link to your privacy policy, and your privacy policy must link to your terms and conditions.

Your use of Notify is also governed by the [AWS Service Terms](https://aws.amazon.com/service-terms/), including Section 29 (Amazon Pinpoint and AWS End User Messaging).

## Required opt-in flow
<a name="notify-compliance-optin"></a>

Before sending messages through Notify, mobile carriers require you to implement an opt-in flow that obtains explicit consent from your end users. The opt-in flow must meet the following requirements:
+ End users must actively consent to receive messages (for example, by selecting a checkbox, choosing a button, or providing verbal confirmation).
+ The opt-in must clearly state that the user will receive verification messages.
+ The opt-in must include the disclosures: "Message and data rates may apply. Message frequency varies. Reply HELP for help. Reply STOP to cancel."
+ The opt-in must include links to your terms and conditions and privacy policy.
+ You must maintain records of consent.

**Digital opt-in example (web or mobile app)**  
The following is an example of a digital opt-in. Replace the bracketed placeholders with your own values.

```
☐ By entering my phone number and choosing "Send Code," I consent to
receive an automated one-time verification code from [YOUR_BRAND] at
the number provided. Messages are powered by AWS Notify. Message and
data rates may apply. Message frequency varies. Reply HELP for help,
STOP to cancel.
Terms and conditions: [YOUR_TERMS_URL]
Privacy policy: [YOUR_PRIVACY_POLICY_URL]
```

**Verbal opt-in example (IVR or customer service call)**  
The following is an example of a verbal opt-in script.

```
"To verify your identity, we'll send a one-time verification code to
your mobile phone, powered by AWS Notify. By providing your phone
number, you consent to receive this automated text message. Message
and data rates may apply. Message frequency varies. Reply HELP for
help or STOP to cancel. Do you consent to receive this verification
code?"
```

**Note**  
These examples follow CTIA Messaging Principles and Best Practices for informational messaging. OTP verification codes are considered informational (not promotional) because the user initiates the request. STOP/HELP disclosures are required for all messages sent through Notify.

## Customer support requirements
<a name="notify-compliance-support"></a>

You must provide your own customer support contact information (email address and/or phone number) in your terms and conditions. This support contact must be accessible without requiring a login. Carrier and regulatory guidelines require that end users can reach support for questions about the messages they receive.

## Notify mobile-carrier prerequisites checklist
<a name="notify-compliance-summary"></a>

Before sending messages with Notify, verify that you have completed the following:
+ Published a terms and conditions page with the required language at a public URL.
+ Published a privacy policy page with the required statements at a public URL.
+ Implemented an opt-in flow that obtains explicit consent and includes all required disclosures.
+ Included links to your terms and privacy policy in your opt-in flow.
+ Provided a customer support contact (email and/or phone) that does not require a login.
+ Cross-linked your terms and privacy policy pages to each other.