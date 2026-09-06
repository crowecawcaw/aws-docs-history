

# Widget and ISV opt-in
<a name="registration-help-optin-widget"></a>

Use this pattern for **embedded widgets** (modals, pop-ups, chatbots) provided by an ISV (Independent Software Vendor) to their customers. The ISV is the message controller — they control the data and messaging flow. The Privacy Policy and Terms link to the ISV's policies. All disclosures must be visible within the widget itself.

![Widget/ISV opt-in modal example](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/optin-widget.png)


## What makes this compliant
<a name="registration-help-optin-widget-compliant"></a>
+ **All disclosures within the widget** — Brand name, message purpose, frequency, data rates, STOP/HELP, Privacy Policy, and Terms are all visible inside the modal without navigating away.
+ **No checkbox needed** — Submitting the phone number and choosing Send is the consent action (same as transactional optional phone pattern).
+ **'Powered by' identifies the ISV** — The footer identifies the platform provider. This allows the ISV to use their own SMS terms and privacy policy.
+ **Brand name in disclosure text** — The end brand is named in the consent disclosure so the user knows who will send messages.
+ **Privacy and Terms link to ISV policies** — The ISV controls the messaging flow, so their policies govern the SMS program.

## Common mistakes that cause denial
<a name="registration-help-optin-widget-mistakes"></a>
+ Placing disclosures on a separate page that requires navigation away from the widget
+ Not identifying the brand name in the disclosure
+ Missing the 'Powered by' ISV identification
+ Not providing hosted screenshots if the widget is behind authentication
+ Missing Privacy Policy or Terms links within the widget