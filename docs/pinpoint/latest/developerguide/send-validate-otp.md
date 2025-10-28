**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Generate one-time passwords (OTPs) with Amazon Pinpoint

Amazon Pinpoint includes a one-time password (OTP) management feature that you can use to
generate new one-time passwords and send them to your recipients as SMS messages.

###### Important

To use this feature, your account must have production access and an active
origination identity. For more information, see [About the SMS/MMS and Voice sandbox](../../../sms-voice/latest/userguide/sandbox.md "../../../sms-voice/latest/userguide/sandbox.md")
and [Request a phone number](../../../sms-voice/latest/userguide/phone-numbers-request.md "../../../sms-voice/latest/userguide/phone-numbers-request.md") in the _AWS End User Messaging SMS User
Guide_.

In some countries and Regions, you must obtain a dedicated phone number or origination
ID before you can send SMS messages. For example, when you send messages to the
recipients in the United States, you must have a dedicated toll-free number, 10DLC
number, or short code. When you send messages to recipients in India, you must have a
registered sender ID, which includes a Principal Entity ID (PEID) and a Template ID.
These requirements still apply when you use the OTP feature.

To use this feature you need permissions to send and verify OTP messages, see [One-time passwords](permissions-actions.md#permissions-actions-apiactions-otp "permissions-actions.md#permissions-actions-apiactions-otp"). If you
need help determining permissions, see [Troubleshooting Amazon Pinpoint identity and
access management](security_iam_troubleshoot.md "security_iam_troubleshoot.md").

You can use the `SendOtpMessages` operation in the Amazon Pinpoint API to send an OTP
code to a user of your application. When you use this API, Amazon Pinpoint generates a random code
and sends it to your user as an SMS message. Your request can include the following
parameters:

- `Channel` – The communication channel that the OTP code is
  sent through. Currently, only SMS messages are supported, so the only acceptable
  value is SMS.
- `BrandName` – The name of the brand, company, or product that
  is associated with the OTP code. This name can contain up to 20
  characters.

###### Note

When Amazon Pinpoint sends the OTP message, the brand name is automatically inserted
into the following message template:

```
This is your One Time Password: {{otp}} from {{brand}}
```

So, if you specify ExampleCorp as your brand name, and Amazon Pinpoint
generates a one-time password of 123456, it sends the following message to
your user:

```
This is your One Time Password: 123456 from ExampleCorp
```

- `CodeLength` – The number of digits that will be in the OTP
  code that's sent to the recipient. OTP codes can contain between 5 and 8 digits,
  inclusive.
- `ValidityPeriod` – The amount of time, in minutes, that the
  OTP code will be valid. The validity period can be between 5 and 60 minutes,
  inclusive.
- `AllowedAttempts` – The number of times the recipient can
  unsuccessfully attempt to verify the OTP. If the number of attempts exceeds this
  value, the OTP automatically becomes invalid. The maximum number of allowed
  attempts is 5.
- `Language` – The language, in IETF BCP-47 format, to use when
  sending the message. Acceptable values are:
  - `de-DE` – German
  - `en-GB` – English (UK)
  - `en-US` – English (US)
  - `es-419` – Spanish (Latin America)
  - `es-ES` – Spanish
  - `fr-CA` – French (Canada)
  - `fr-FR` – French
  - `it-IT` – Italian
  - `ja-JP` – Japanese
  - `ko-KR` – Korean
  - `pt-BR` – Portuguese (Brazil)
  - `zh-CN` – Chinese (Simplified)
  - `zh-TW` – Chinese (Traditional)

- `OriginationIdentity` – The originating identity (such as a
  long code, short code, or sender ID) that is used to send the OTP code. If you
  use a long code or toll-free number to send the OTP, the phone number must be in
  E.164 format.
- `DestinationIdentity` – The phone number, in E.164 format,
  that the OTP code was sent to.
- `ReferenceId` – A unique reference ID for the request. The
  reference ID exactly match the reference ID that you provide when you verify the
  OTP. The reference ID can contain between 1 and 48 characters, inclusive.
- `EntityId` – An Entity ID that is registered with a
  regulatory agency. This parameter is currently only used when sending messages
  to recipients in India. If you aren't sending to recipients in India, you can
  omit this parameter.
- `TemplateId` – A Template ID that is registered with a
  regulatory agency. This parameter is currently only used when sending messages
  to recipients in India. If you aren't sending to recipients in India, you can
  omit this parameter.

###### Note

For more information about the requirements for sending messages to
recipients in India, see [India sender ID registration process](../../../sms-voice/latest/userguide/registrations-sms-senderid-india.md "../../../sms-voice/latest/userguide/registrations-sms-senderid-india.md") in the
_Amazon Pinpoint User Guide_.
To ensure that your Amazon Pinpoint account is properly configured to send OTP messages, you can
use the AWS CLI to send a test message. For more information about the AWS CLI, see the
[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

To send a test OTP message using the AWS CLI, run the [send-otp-message](../../../cli/latest/reference/pinpoint/send-otp-message.md "../../../cli/latest/reference/pinpoint/send-otp-message.md") command in the terminal:

```
aws pinpoint send-otp-message --application-id `7353f53e6885409fa32d07cedexample` --send-otp-message-request-parameters Channel=SMS,BrandName=`ExampleCorp`,CodeLength=`5`,ValidityPeriod=`20`,AllowedAttempts=`5`,OriginationIdentity=`+18555550142`,DestinationIdentity=`+12065550007`,ReferenceId=`SampleReferenceId`
```

In the preceding command, do the following:

- Replace `7353f53e6885409fa32d07cedexample` with your
  application id.
- Replace `ExampleCorp` with the name of your
  company.
- Replace `5` in `CodeLegth` with the number
  of digits that will be in the OTP code that's sent to the recipient.
- Replace `20` in `ValidityPeriod` with
  amount of time, in minutes, that the OTP code will be valid.
- Replace `5` in `AllowedAttempts` with the
  number of times the recipient can unsuccessfully attempt to verify the
  OTP.
- Replace `+18555550142` in
  `OriginationIdentity` with the originating identity that is used
  to send the OTP code.
- Replace `+12065550007` in
  `DestinationIdentity` with the phone number to send the OTP code
  to.
- Replace `SampleReferenceId` in
  `ReferenceId` with a unique reference ID for the request.

## `SendOtpMessage`

response

When you successfully send an OTP message, you receive a response that resembles
the following example:

```
{
    "MessageResponse": {
        "ApplicationId": "7353f53e6885409fa32d07cedexample",
        "RequestId": "255d15ea-75fe-4040-b919-096f2example",
        "Result": {
            "+12065550007": {
                "DeliveryStatus": "SUCCESSFUL",
                "MessageId": "nvrmgq9kq4en96qgp0tlqli3og1at6aexample",
                "StatusCode": 200,
                "StatusMessage": "MessageId: nvrmgq9kq4en96qgp0tlqli3og1at6aexample"
            }
        }
    }
}
```
