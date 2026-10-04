

# Country support
<a name="nx-mms-scale-country-support"></a>

MMS messaging in AWS End User Messaging is available in a limited set of countries. Unlike SMS, which you can send to recipients in many countries worldwide, MMS is currently supported for sending to recipients in the United States and Canada. The number types that support MMS, and whether a given number type is available for each country, also differ from SMS.

Before you request a number for MMS, review the countries where MMS is supported and the number options available for each. For the authoritative list of countries and regions where you can send MMS messages, along with which number types (short codes, long codes, and toll-free) support MMS in each, see [Supported countries](nx-supported-countries.md).

**Note**  
MMS is supported for sending to the United States and Canada. Any expansion of MMS country availability beyond the United States and Canada, and any change to the number types that support MMS in each country [needs SME confirmation]. Always confirm the current MMS country list against [Supported countries](nx-supported-countries.md).

## How to launch in a country
<a name="nx-mms-scale-country-support-process"></a>

To send MMS messages to recipients in a supported country, follow these steps.

1. Confirm the country is supported for MMS and review the number types available for it in [Supported countries](nx-supported-countries.md).

1. Request an MMS-capable number for that country, such as a short code, a 10DLC long code, or a toll-free number. The available number types depend on the country. For more information, see [Sender IDs](nx-features-senders.md).

1. If the number type requires registration, for example a US toll-free number or a 10DLC long code, complete the registration and wait for approval before you send.

1. Send a test message to confirm your setup, then move out of the sandbox to send at production volumes. See [Move out of the sandbox](nx-mms-scale-sandbox.md).