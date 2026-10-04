

# Compliance and mobile carrier prerequisites
<a name="nx-notify-scale-compliance"></a>

When you use Notify, you are responsible for complying with applicable messaging laws and mobile carrier requirements in each country or region where your customers are located. Consult an attorney to assess your compliance obligations. Non-compliance may result in a carrier audit and removal of your access to Notify. These requirements apply to both the Basic and Advanced tiers. Before sending messages, you must publish your own terms and conditions and privacy policy pages that include the required language, and you must implement an opt-in flow that obtains explicit consent.

Regardless of tier, you are responsible for obtaining appropriate consent from recipients before sending messages, complying with applicable laws such as the Telephone Consumer Protection Act (TCPA) in the US and the GDPR in the EU, and following the carrier policies that apply to your messaging. Your use of Notify is also governed by the [AWS Service Terms](https://aws.amazon.com/service-terms/), including Section 29 (Amazon Pinpoint and AWS End User Messaging).

## Required terms and conditions
<a name="nx-notify-scale-compliance-terms"></a>

Mobile carriers require that you make a specific set of messaging terms and conditions available to your customers at a publicly accessible URL, and that you link to it from your opt-in flow. Your terms and conditions must include, at minimum, the following information. Replace the bracketed placeholders with your own values.

```
Subscribers will opt-in via [YOUR_WEBSITE_URL] to receive verification
messages from [YOUR_COMPANY_NAME], powered by Notify. Message frequency
may vary per user.

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

## Required privacy policy
<a name="nx-notify-scale-compliance-privacy"></a>

You must also make a privacy policy available to your customers at a publicly accessible URL. Your privacy policy must include, at minimum, statements that no mobile numbers will be shared with third parties or affiliates for marketing or promotional purposes, that text messaging originator opt-in data and consent will not be shared with any third parties, and that messages are delivered through Notify and that AWS does not share end user phone numbers with third parties for marketing or promotional purposes. Your terms and conditions page must link to your privacy policy, and your privacy policy must link to your terms and conditions.

## Required opt-in flow
<a name="nx-notify-scale-compliance-optin"></a>

Before sending messages through Notify, mobile carriers require you to implement an opt-in flow that obtains explicit consent from your end users. The opt-in flow must meet the following requirements:
+ End users must actively consent to receive messages, for example by selecting a checkbox, choosing a button, or providing verbal confirmation.
+ The opt-in must clearly state that the user will receive verification messages.
+ The opt-in must include the disclosures: "Message and data rates may apply. Message frequency varies. Reply HELP for help. Reply STOP to cancel."
+ The opt-in must include links to your terms and conditions and privacy policy.
+ You must maintain records of consent.

The following is an example of a digital opt-in for a web or mobile app. Replace the bracketed placeholders with your own values.

```
By entering my phone number and choosing "Send Code," I consent to
receive an automated one-time verification code from [YOUR_BRAND] at
the number provided. Messages are powered by Notify. Message and data
rates may apply. Message frequency varies. Reply HELP for help, STOP to
cancel.
Terms and conditions: [YOUR_TERMS_URL]
Privacy policy: [YOUR_PRIVACY_POLICY_URL]
```

**Note**  
OTP verification codes are considered informational rather than promotional, because the user initiates the request. STOP and HELP disclosures are required for all messages sent through Notify.

## Customer support requirements
<a name="nx-notify-scale-compliance-support"></a>

You must provide your own customer support contact information, an email address or a phone number, in your terms and conditions. This support contact must be accessible without requiring a login. Carrier and regulatory guidelines require that end users can reach support for questions about the messages they receive.