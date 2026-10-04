

# Launch in a country
<a name="nx-sms-country-support"></a>

SMS requirements vary by country. Before you send to a new country, confirm which origination identities that country supports, whether the country requires registration, and whether two-way messaging is available. Requirements differ by destination, so plan for the country you are sending to rather than the AWS Region you send from.

To launch SMS in a country, follow these steps:

1. Look up the country in [Supported countries](nx-supported-countries.md) to confirm it is supported and to see its origination identity options, registration requirements, and two-way support.

1. Request the origination identity that the country supports, such as a phone number or a sender ID. For more information, see [Sender IDs](nx-features-senders.md).

1. If the country requires registration, complete the registration and wait for approval before you send. For registration details by country, see [Supported countries](nx-supported-countries.md).

1. Send a test message to confirm your setup, then move out of the sandbox to send at production volumes. See [Move out of the sandbox](nx-sms-scale-sandbox.md).

For the full list of supported countries and their SMS capabilities, see [Supported countries](nx-supported-countries.md).