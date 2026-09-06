

# Verbal script opt-in
<a name="registration-help-optin-verbal"></a>

Use this pattern when consent is collected **verbally** (call center, in-person enrollment, patient intake). The full script must be provided in the registration submission. Agents must read the script verbatim — paraphrasing risks missing required elements.

![Verbal script opt-in example](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/optin-verbal.png)


## What makes this compliant
<a name="registration-help-optin-verbal-compliant"></a>
+ **All disclosures spoken verbatim** — Brand name, message types, frequency, data rates, STOP/HELP instructions, and Terms/Privacy URL references are all included in the script text.
+ **Clear affirmative consent** — The customer must verbally agree ("Yes") before enrollment proceeds.
+ **Confirmation message promised** — The agent tells the customer a confirmation text will be sent, which serves as the opt-in confirmation message.
+ **Terms and Privacy referenced by URL** — The agent provides a URL where the customer can find the full Terms and Privacy Policy.
+ **Full script submitted with registration** — The exact script text must be provided in the registration submission (in the Message Flow field or as an attachment).

## Common mistakes that cause denial
<a name="registration-help-optin-verbal-mistakes"></a>
+ Allowing agents to paraphrase or skip disclosures
+ Not providing the full script text in the registration submission
+ Missing frequency or data rates disclosure in the script
+ Not referencing Terms of Service or Privacy Policy
+ Not sending a confirmation text message after verbal consent