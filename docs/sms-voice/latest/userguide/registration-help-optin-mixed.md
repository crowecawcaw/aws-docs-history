

# Mixed use-case opt-in
<a name="registration-help-optin-mixed"></a>

Use this pattern when your campaign sends **both transactional and marketing** messages. Carrier compliance requires that marketing and transactional consent are collected in separate checkboxes — a single checkbox cannot cover both. The user must be able to opt into transactional only, marketing only, both, or neither.

![Mixed use-case opt-in form example](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/optin-mixed.png)


## What makes this compliant
<a name="registration-help-optin-mixed-compliant"></a>
+ **Separate checkboxes for each message type** — Transactional SMS and marketing SMS each have their own checkbox with distinct consent language.
+ **Each checkbox has its own HELP/STOP instructions** — Both SMS consent checkboxes independently include frequency, data rates, and opt-out instructions.
+ **Terms and Privacy are a third checkbox** — Acceptance of Terms/Privacy is separate from both SMS consent types.
+ **Neither SMS checkbox is required** — The user can submit the form without checking either SMS consent box.
+ **Marketing checkbox specifies frequency** — "Up to 4 msgs/month" is more specific than "frequency varies" and is preferred for marketing campaigns.

## Common mistakes that cause denial
<a name="registration-help-optin-mixed-mistakes"></a>
+ Combining transactional and marketing consent into a single checkbox
+ Making either SMS checkbox required to submit the form
+ Missing HELP/STOP on one of the SMS checkboxes
+ Not clearly distinguishing which messages are marketing vs. transactional
+ Pre-checking either consent box