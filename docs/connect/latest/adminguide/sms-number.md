# Request an SMS-enabled phone number through

AWS End User Messaging SMS

###### Important

Some countries require phone numbers and sender IDs to be registered for use
in the country. It can take up to 15 business days to process a registration
request after it is submitted. We strongly recommend you begin this process
early. For more information about registering, see [Registrations](../../../sms-voice/latest/userguide/registrations.md "../../../sms-voice/latest/userguide/registrations.md").

Using AWS End User Messaging SMS, you can request new SMS-enabled phone numbers or reuse existing
SMS-enabled phone numbers for use in Amazon Connect. You can request short codes, 10-digit
long codes (10DLC), and toll-free numbers. These are also known as Origination
Identities (OIDs).

For instructions about procuring a number for SMS messaging, see [Requesting a phone number](../../../sms-voice/latest/userguide/phone-numbers-request.md "../../../sms-voice/latest/userguide/phone-numbers-request.md") in the _AWS End User Messaging SMS User
Guide_.

## Best practices for requesting SMS

numbers

- Each type of OID has a different registration process and the leasing
  costs vary. Review the pricing here: [AWS End User Messaging SMS pricing](https://aws.amazon.com/pinpoint/pricing/#Numbers "https://aws.amazon.com/pinpoint/pricing/#Numbers").
- When deciding what type of phone number to request, we recommend
  considering your throughput needs. SMS messages are delivered in
  140-byte sections known as [message
  parts](../../../sms-voice/latest/userguide/sms-limitations-mps.md "../../../sms-voice/latest/userguide/sms-limitations-mps.md"). Your throughput rate is the number of message parts
  that you can send each second.
  - **1–3 message parts per second**:
    Use a toll-free number. We recommend using a 10DLC number or
    short code if your throughput needs will exceed these limits as
    you expand your use cases. These number types provide plenty of
    room for growth, but also cost more and currently take longer to
    obtain than a toll-free number. For more information about
    requesting a toll-free number in Amazon Pinpoint, see [Requesting a phone number](../../../sms-voice/latest/userguide/phone-numbers-request.md "../../../sms-voice/latest/userguide/phone-numbers-request.md").
  - **10–75 message parts per
    second**: Use a 10DLC number. You can also use a
    short code, which would provide additional room for growth, but
    would also cost more. For more information, see [Requesting dedicated long codes for SMS messaging with
    Amazon Pinpoint SMS](../../../sms-voice/latest/userguide/phone-numbers-long-code.md "../../../sms-voice/latest/userguide/phone-numbers-long-code.md").
  - **100 message parts per second or
    more**: Use a short code. When you create your
    request in the AWS Support Center Console, specify the
    throughput rate that you want your short code to support.

  By default US short codes support 100 message parts per
  second, but the throughput rate can be increased beyond that
  rate for an additional monthly fee. For more information, see
  [Requesting short codes for SMS messaging with Amazon
  Pinpoint SMS](../../../sms-voice/latest/userguide/phone-numbers-request-short-code.md "../../../sms-voice/latest/userguide/phone-numbers-request-short-code.md").

- Request at least one of the above OIDs as a `TRANSACTIONAL`
  number from Amazon Pinpoint.
- Be sure to provide all of the information requested during the
  registration process. There are no exceptions to the questions being
  asked.

###### Important

Providing incomplete or inaccurate information will increase the
registration time. Your registration will need to be edited and
returned to be reviewed again.

Registration for all types of OIDs in the US are managed by a
third-party registrar. Amazon does not review applications.

- Toll-free phone number registration requires the least amount of time
  to procure.
- Review the [10DLC
  registration process](../../../sms-voice/latest/userguide/registration-10dlc.md "../../../sms-voice/latest/userguide/registration-10dlc.md") explained in the _AWS End User Messaging SMS
  User Guide_.
