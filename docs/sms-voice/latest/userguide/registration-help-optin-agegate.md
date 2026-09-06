

# Age-restricted content opt-in
<a name="registration-help-optin-agegate"></a>

Use this pattern when your campaign involves **age-restricted content** that is legally permitted (such as restaurants serving alcohol, tobacco products over short codes, or gun advocacy/safety training). A full date-of-birth age gate must appear before the SMS consent — the user cannot consent to messages until age is verified.

![Age-restricted content opt-in with DOB age gate](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/optin-agegate.png)


## What makes this compliant
<a name="registration-help-optin-agegate-compliant"></a>
+ **Full date-of-birth collection** — The age gate requires day, month, AND year. A simple "Are you 21\+? Yes/No" button is not sufficient and will be automatically denied.
+ **Age gate appears before consent** — The DOB fields are positioned above the SMS consent checkbox. The user must verify age before they can opt in.
+ **Phone number is optional** — Same as other marketing forms, the phone field is not required to submit.
+ **Standard SMS consent checkbox** — After age verification, the same two-checkbox pattern applies (SMS consent \+ Terms/Privacy).
+ **All standard disclosures present** — Brand name, message type, frequency, data rates, STOP/HELP, Terms, and Privacy are all included.

## Common mistakes that cause denial
<a name="registration-help-optin-agegate-mistakes"></a>
+ Using a simple Yes/No age confirmation instead of full date-of-birth
+ Placing the age gate after the SMS consent checkbox
+ Missing the age gate entirely for age-restricted content
+ Not clearly identifying the content as age-restricted in the registration
+ Attempting to register content that is not approvable even with an age gate (e.g., direct firearms sales, vapes, cannabis)