

# Marketing opt-in
<a name="registration-help-optin-marketing"></a>

Use this pattern when your campaign sends **promotional or marketing** messages (offers, discounts, product announcements). Marketing messages require express written consent under TCPA, which means the user must actively check a box — providing a phone number alone is not sufficient.

![Marketing opt-in form example](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/optin-marketing.png)


## What makes this form compliant
<a name="registration-help-optin-marketing-compliant"></a>
+ **Phone number is optional** — The form can be submitted without providing a phone number. Email is the primary contact method; SMS is an additional opt-in channel.
+ **SMS consent is a separate, unchecked checkbox** — The user must actively check the box to consent. It is not pre-selected and is not required to complete the form submission.
+ **Consent text identifies the brand and message type** — The checkbox label names the brand and explicitly states "promotional/marketing SMS communications."
+ **All required disclosures in the consent text** — Frequency ("Frequency may vary"), data rates ("Message and data rates may apply"), and opt-out/help instructions ("reply HELP for help or STOP to opt-out") are all present in the checkbox label.
+ **Terms and Privacy Policy are a separate checkbox** — Acceptance of Terms of Service and Privacy Policy is collected independently from SMS consent, with direct links to each document.

## Common mistakes that cause denial
<a name="registration-help-optin-marketing-mistakes"></a>
+ Pre-checking the SMS consent checkbox
+ Making the phone number a required field
+ Bundling SMS consent into the Terms of Service checkbox
+ Missing frequency or data rates disclosure in the consent text
+ Not identifying the brand name in the consent language