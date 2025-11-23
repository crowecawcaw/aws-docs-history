# Use the carrier lookup service

AWS End User Messaging SMS includes a carrier lookup service that you can use to obtain information about a phone number,
including if the phone number is valid. The carrier lookup service returns the following
information for a phone number:

- The phone number in E164 format (sanitized from the original input).
- The phone number type (such as invalid, landline, mobile, other).
- The name of the country or region for the phone number.
- The country or region numeric dialing code for the phone number.
- The two-character country or region code, in ISO 3166-1 alpha-2 format, for the phone number.
- For mobile numbers, the mobile country code (MCC).
- For mobile numbers, the mobile network code (MNC).
- The carrier or service provider that the phone number is currently registered with. In some countries and regions,
  this value may be the carrier or service provider that the phone number was originally registered with.
  There is an additional charge for using the carrier lookup service. For more
  information, see [AWS End User Messaging SMS pricing](https://aws.amazon.com/end-user-messaging/pricing/#Phone_number_validate "https://aws.amazon.com/end-user-messaging/pricing/#Phone_number_validate").

## Carrier lookup use

cases

You can use the carrier lookup service to enable several use cases, including
the following:

- **Lookup phone numbers provided on a web
  form** – If you use web-based forms to collect contact
  information for your customers, you can lookup the phone numbers that customers
  provide before submitting the form. Use your website's backend to lookup and validate the
  number by using the AWS End User Messaging SMS API. The API response states whether the
  number is valid—for example, if the phone number is formatted
  correctly. If you determine that the customer provided phone number
  is invalid, your web form can prompt the customer to provide a valid
  number.
- **Cleansing your existing contact database**
  – If you have a database of customer phone numbers, you can lookup each
  phone number, and update your database using the carrier lookup results. For example,
  if you find endpoints with phone numbers that aren't capable of receiving SMS
  messages, you can change the `ChannelType` property for the endpoint
  from `SMS` to `VOICE`.
- **Choosing the right channel before you send a
  message** – If you intend to send an SMS message but you
  determine that the destination number is invalid, you can send a message to the
  recipient through a different channel. For example, if the endpoint isn't able
  to receive SMS messages, you can send a voice message instead.

## Supported phone number formats

Phone numbers must be in E164 format, starting with a plus sign (+) followed by the country dialing code and phone number (for example, +12065551234). The carrier lookup service accepts various formatting characters and automatically removes them during processing. You can include the following formatting characters in your phone number input:

- Parentheses: `+1 (555) 123-4567`
- Brackets: `+1 [555] 123-4567`
- Spaces: `+1 555 123 4567`
- Hyphens: `+1-555-123-4567`
- Periods: `+1.555.123.4567`
- Commas: `+1,555,123,4567`
- Mixed formatting: `+1 (555)-123.4567`

All formatting characters are automatically removed during processing, and the service returns the phone number in standard E164 format (for example, `+15551234567`) in the `E164PhoneNumber` field of the response.

## Using the carrier lookup service in the AWS CLI

The following example shows how to use the carrier lookup service in the AWS CLI. The service accepts phone numbers with various formatting characters (parentheses, brackets, spaces, hyphens, periods, commas) and automatically converts them to E164 format for processing. For more
information, see [CarrierLookup](../../../pinpoint/latest/apireference_smsvoicev2/API_CarrierLookup.md "../../../pinpoint/latest/apireference_smsvoicev2/API_CarrierLookup.md")
in the AWS End User Messaging SMS API reference or [carrier-lookup](../../../cli/latest/reference/pinpoint-sms-voice-v2/carrier-lookup.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/carrier-lookup.md") in the AWS CLI Command Reference.

###### To use the carrier lookup service (CLI)

- At the command line, enter the following command. You can use various phone number formats - the service accepts special characters like parentheses, brackets, spaces, hyphens, periods, and commas:

```
`$` `aws pinpoint-sms-voice-v2 carrier-lookup --phone-number `"+1 (555) 555-5333"``
```

Or with E164 format:

```
`$` `aws pinpoint-sms-voice-v2 carrier-lookup --phone-number `+15555555333``
```

### Carrier lookup responses

The information that the carrier lookup service provides varies slightly
based on the data that's available for the phone number that you provide. This section
contains examples of the responses that the carrier lookup service
returns.

###### Note

The data that's provided by the carrier lookup service is based on
information provided by telecommunication providers and other entities around the
world. Providers in some countries might update this information less frequently
than providers in other countries do. For example, if you issue a request to
validate a mobile phone number, and the number that you provided was ported from one
mobile carrier to another, the response from the carrier lookup service
might include the name of the original carrier, as opposed to the current
one.

###### Valid mobile phone numbers

The following response is an example of the information `CarrierLookup` returns for a valid mobile phone number:

```
{
    "E164PhoneNumber": "+15555555333",
    "DialingCountryCode": "1",
    "IsoCountryCode": "US",
    "Country": "United States",
    "MCC": "310",
    "MNC": "260",
    "Carrier": "ExampleCorp Mobile",
    "PhoneNumberType": "MOBILE"
}
```

###### Valid landline phone numbers

The following response is an example of the information `CarrierLookup` returns for a valid landline phone number:

```
{
    "E164PhoneNumber": "+15555555333",
    "DialingCountryCode": "1",
    "IsoCountryCode": "CA",
    "Country": "Canada",
    "Carrier": "ExampleCorp Landline",
    "PhoneNumberType": "LANDLINE"
}
```

###### Invalid phone numbers

If your request contains an invalid phone number, the carrier lookup
service returns information that resembles the following example:

```
{
    "E164PhoneNumber": "+15555555333444666",
    "PhoneNumberType": "INVALID"
}}
```

Note that the `PhoneNumberType` property in this response indicates that this
phone number is `INVALID`, and that it doesn't include information about the
carrier or location associated with the phone number. You should avoid sending SMS or
voice messages to phone numbers where the `PhoneNumberType` is
`INVALID`, because these numbers are unlikely to belong to actual
recipients.

###### Other phone numbers

Phone numbers that are not classified as mobile, landline, or invalid are returned with a `PhoneNumberType` value of `OTHER`.
