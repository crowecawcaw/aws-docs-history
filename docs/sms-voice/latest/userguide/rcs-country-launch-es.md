

# Launching RCS in Spain
<a name="rcs-country-launch-es"></a>

To launch your AWS RCS Agent in Spain, submit a country launch registration using the `ES_RCS_LAUNCH_REGISTRATION` registration type. The Spain registration form includes additional company detail fields beyond the standard baseline.

## Registration form (console)
<a name="rcs-country-launch-es-console"></a>

The Spain launch registration uses a custom form with additional fields. The registration form collects the following information:
+ **Brand information** — Auto-populated from your testing agent configuration.
+ **Use case selection** — Select the use case category for your RCS messaging.
+ **Company name** — Your legal company name.
+ **Industry** — The industry sector your company operates in.
+ **Company address** — Your company's registered address (address, city, region, postal code, country).
+ **Brand contact mobile number** — Mobile phone number for the brand contact person in international format.
+ **Estimated monthly volume** — Expected number of RCS messages per month.
+ **Screen recording** — A screen recording that demonstrates your RCS messaging experience. For detailed video requirements, see [Launch video requirements](rcs-compliance-video.md).
+ **Privacy policy and terms of service** — URLs to your privacy policy and terms of service pages.

Spain does not require any out-of-band emails or third-party brand verification letters. However, Spain does require registration in the CNMC National Alias Registry before your RCS agent can be launched.

## CNMC National Alias Registry requirement
<a name="rcs-country-launch-es-cnmc"></a>

**Important**  
All RCS agents used to send messages to Spanish mobile numbers (\+34) must be registered in the CNMC (Comisión Nacional de los Mercados y la Competencia) National Alias Registry. This is the same regulatory body that governs SMS sender ID registration in Spain.

The CNMC registration process for RCS follows the same general pattern as SMS sender ID registration in Spain:

1. **Obtain a qualifying digital certificate** — The CNMC portal requires authentication with a valid digital certificate issued by the Spanish government, a qualifying EU eIDAS certificate, or a certificate from a recognized EU trust service provider.

1. **Register on the CNMC portal** — Go to [https://tramites.cnmc.gob.es/formulario/213/](https://tramites.cnmc.gob.es/formulario/213/) and authenticate with your digital certificate. Register your RCS agent name in the National Alias Registry.

1. **Approve the CNMC verification** — After submission, CNMC sends a verification email. You must log into the portal and approve the registration within 10 business days.

1. **Submit your RCS country launch registration** in the AWS End User Messaging console.

**Note**  
If you do not have a qualifying digital certificate or a representative in Spain or a qualifying EU country, you must appoint one. The representative must hold a valid digital certificate and have an apostilled notarized power of attorney authorizing them to act on your behalf. We recommend engaging legal counsel to advise on this process.

For detailed instructions on the CNMC registration process (including portal field values for SMS), see [Spain sender ID registration in AWS End User Messaging SMS](registrations-spain.md).

**Important**  
We are currently processing new information about the specific field values customers need to enter on the CNMC portal for RCS agent registrations. We will update this documentation as soon as we have concrete details. This does not affect your ability to submit a Spain RCS country launch registration in the AWS End User Messaging console.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).