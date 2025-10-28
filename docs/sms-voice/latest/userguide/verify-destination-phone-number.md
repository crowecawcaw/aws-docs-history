# Add a destination phone number while in the

AWS End User Messaging SMS sandbox

###### Note

Verified destination phone numbers are only required for testing while your account is in
the sandbox. If your account is in production, you don't need to add verified destination phone
numbers.

When your account is in the SMS/MMS or voice sandbox you can only send messages to verified
destination phone numbers. You can add up to 10 verified destination phone numbers to your
account. Adding a verified destination phone number requires you to send a text or voice message
to the destination phone number and then entering the code the device received.

Before you begin you need an origination identity in your account that is active and has
text or voice message capabilities. If you don't have an origination identity available you can
use **Origination simulator phone numbers** and **Destination simulator phone numbers** to test sending and receiving
messages. For more information about simulated phone numbers, see [Simulator phone numbers](test-phone-numbers.md "test-phone-numbers.md"). The origination
identity can only send messages within its country or region. For example, an origination
identity for the United States can only send verification messages to destination phone numbers
in the United States.

###### Important

Simulator phone numbers can only send to other simulator destination phone numbers however
they behave like actual phone numbers without sending over the carrier network. You can not use
a simulator phone number to verify a destination phone number. For example, US simulator phone
numbers can only send to US destination simulator phone numbers.

For more information about installing and configuring the AWS CLI, see the
[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

1. Add the phone number to your account by using the [create-verified-destination-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/create-verified-destination-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/create-verified-destination-number.md") CLI command.

At the command line, enter the following command:

```
aws pinpoint-sms-voice-v2 create-verified-destination-number --destination-phone-number `PhoneNumber`
```

In the preceding command, make the following changes:

    * Replace `PhoneNumber` with the E.164 formatted phone number to
     send the message to. For example, `+1 (206) 555-0142` is not in the correct
     format, but `+12065550142` is.

On completion the command will return the verified phone numbers
`VerifiedDestinationNumberId` which is needed in the next steps. 2. Use the [send-destination-number-verification-code](../../../cli/latest/reference/pinpoint-sms-voice-v2/send-destination-number-verification-code.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/send-destination-number-verification-code.md") CLI command to send a verification message
to the device. Only the first verification code is free.

At the command line, enter the following command:

```
aws pinpoint-sms-voice-v2 send-destination-number-verification-code --verified-destination-number-id `PhoneNumberID` --verification-channel `Channel`
```

In the preceding command, make the following changes:

    * Replace `PhoneNumberID` with the
     `VerifiedDestinationNumberId` you received in the previous step.
    * Replace `Channel` with the channel to use to send the message.
     You need to have an origination identity that supports the channel you use. This can be
     `TEXT` or `VOICE` and is case sensitive.

The device should receive a message with a randomly generated code. You will need this
code in the next step. 3. Use the [verify-destination-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/verify-destination-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/verify-destination-number.md") CLI command to send a verification message.

At the command line, enter the following command:

```
aws pinpoint-sms-voice-v2 verify-destination-number --verified-destination-number-id `PhoneNumberID` --verification-code `Code`
```

In the preceding command, make the following changes:

    * Replace `PhoneNumberID` with the
     `VerifiedDestinationNumberId` you received in the previous step.
    * Replace `Code` with the verification code the destination
     device received.

Upon successful completion the status of the verified destination phone number is
`VERIFIED`. You can now send messages to the verified destination phone number while
you are in the sandbox.
