

# Transactional opt-in
<a name="registration-help-optin-transactional"></a>

Use this pattern when your campaign sends **transactional or informational** messages (order confirmations, account alerts, appointment reminders). Transactional messages have two variants depending on whether the phone number is optional or required for the service.

![Transactional opt-in — optional phone, no checkbox](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/optin-transactional-optional.png)


![Transactional opt-in — required phone, separate checkbox](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/optin-transactional-required.png)


## What makes this compliant
<a name="registration-help-optin-transactional-compliant"></a>
+ **Optional phone (first image)** — No checkbox is needed. Providing the phone number is the consent action. Disclosure text near the phone field covers all required elements (brand, purpose, frequency, data rates, STOP/HELP, Terms, Privacy).
+ **Required phone (second image)** — When the phone is required for the service (e.g., delivery tracking), a separate SMS consent checkbox is needed because providing the number does not imply consent to receive messages.
+ **Brand clearly identified** — The brand name appears at the top of the form and in the disclosure/consent text.
+ **Message purpose is specific** — The disclosure describes the exact types of messages (account notifications, order updates, customer care).
+ **Terms and Privacy are a separate checkbox** — When a checkbox is present, Terms/Privacy acceptance is collected independently from SMS consent.

## Common mistakes that cause denial
<a name="registration-help-optin-transactional-mistakes"></a>
+ Using a checkbox when the phone number is optional (unnecessary — disclosure text is sufficient)
+ Omitting the checkbox when the phone number is required (phone required for service does not equal SMS consent)
+ Missing HELP or STOP instructions in the disclosure text
+ Not identifying the brand name in the consent language
+ Placing the disclosure below the submit button instead of near the phone field