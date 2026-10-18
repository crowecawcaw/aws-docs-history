

# Country support
<a name="nx-voice-scale-country-support"></a>

Voice availability, supported origination options, and calling requirements vary by country. Review the countries where voice is supported and the options for each before you request a number or send to a new destination.

**Note**  
The specific list of countries where AWS End User Messaging voice is available, together with the supported origination options and per-country calling requirements, is [needs SME confirmation]. Do not rely on the SMS country-support list for voice, because voice coverage and requirements differ. For the current list of AWS Regions where AWS End User Messaging is available, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/pinpoint.html), and for voice pricing by destination, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

## How to launch in a country
<a name="nx-voice-scale-country-support-process"></a>

To send voice messages to recipients in a country, follow these steps.

1. Confirm that voice is supported for your destination country and review the origination options and calling requirements for it. Because voice coverage differs from SMS, confirm the country against the voice availability information rather than the SMS country list.

1. Request a voice-capable phone number for that country. The number types available depend on the country. For more information, see [Sender IDs](nx-features-senders.md).

1. Complete any per-country calling requirements that apply before you send.

1. Send a test message to confirm your setup, then move out of the sandbox to send at production volumes. See [Move out of the sandbox](nx-voice-scale-sandbox.md).

**Note**  
The exact per-country origination options and calling requirements for voice [needs SME confirmation]. Confirm them for each destination country before you launch.