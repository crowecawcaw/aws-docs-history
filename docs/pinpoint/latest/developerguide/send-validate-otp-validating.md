**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Validate OTP messages in Amazon Pinpoint

After you send a one-time-password, your application can call the Amazon Pinpoint API to verify it.
To verify an OTP code, call the `VerifyOtpMessages` API. Your request must
include the following parameters:

- `DestinationIdentity` – The phone number, in E.164 format,
  that the OTP code was sent to.
- `ReferenceId` – The reference ID that you used when you sent
  the OTP code to the recipient. The reference ID must be an exact match.
- `Otp` – The OTP code that you are validating.
  You can use the AWS CLI to test the validation process. For more information about
  installing and configuring the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

To verify an OTP using the AWS CLI, run the [verify-otp-message](../../../cli/latest/reference/pinpoint/verify-otp-message.md "../../../cli/latest/reference/pinpoint/verify-otp-message.md") command in the
terminal:

```
aws pinpoint verify-otp-message --application-id 7353f53e6885409fa32d07cedexample --verify-otp-message-request-parameters DestinationIdentity=`+12065550007`,ReferenceId=`SampleReferenceId`,Otp=`01234`
```

In the preceding command, do the following:

- Replace `7353f53e6885409fa32d07cedexample` with your
  application id.
- Replace `+12065550007` in
  `DestinationIdentity` with the phone number the OTP code was sent
  to.
- Replace `SampleReferenceId` in
  `ReferenceId` with a unique reference ID for the request. This value must match the `ReferenceID` that was used to send the request.
- Replace `01234` in
  `Otp` with a Otp that was sent to the `DestinationIdentity`.

## `VerifyOtpMessage` response

When you send a request to the `VerifyOTPMessage` API, it returns a
`VerificationResponse` object, which contains a single property,
`Valid`. If the reference ID, phone number, and OTP all match the
values that Amazon Pinpoint expects, and if the OTP hasn't expired, the value of
`Valid` is `true`; otherwise, it is `false`.
The following is an example of response for a successful OTP verification:

```
{
    "VerificationResponse": {
        "Valid": true
    }
}
```
