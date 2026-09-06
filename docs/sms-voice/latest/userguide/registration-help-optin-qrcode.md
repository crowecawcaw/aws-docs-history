

# QR code opt-in
<a name="registration-help-optin-qrcode"></a>

Use this pattern for **physical signage** (in-store displays, receipts, mailers, posters) with a QR code or NFC tag. All required disclosures must be printed directly on the signage — the user sees them before scanning. Scanning the QR code deeplinks to the native messaging app to send an inbound message to the registered number.

![QR code physical signage example](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/optin-qrcode.png)


## What makes this compliant
<a name="registration-help-optin-qrcode-compliant"></a>
+ **All disclosures on the physical sign** — Brand name, message purpose, frequency, data rates, STOP/HELP instructions, Privacy Policy URL, and SMS Terms URL are all printed on the signage.
+ **No checkbox needed** — Scanning the QR code and sending the inbound message is the consent action (user-initiated).
+ **Shortened URLs for policies** — Privacy Policy and SMS Terms are accessible via shortened URLs printed on the sign (e.g., yourbrand.com/privacy/).
+ **QR deeplinks to messaging app** — The QR code opens the device's native messaging app with a pre-populated SMS to the registered number.
+ **Registration describes placement** — The registration submission must describe where the signage is displayed and provide a photo as proof.

## Common mistakes that cause denial
<a name="registration-help-optin-qrcode-mistakes"></a>
+ Hiding disclosures behind the QR code (on a landing page instead of the sign itself)
+ Missing Privacy Policy or Terms URL on the physical signage
+ Not describing where the signage is displayed in the registration submission
+ Not providing a photo of the physical signage during registration
+ Using a URL shortener that is not your own branded domain