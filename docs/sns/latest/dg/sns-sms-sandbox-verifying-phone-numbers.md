# Adding and verifying phone numbers

in the Amazon SNS SMS sandbox

Before you can start sending SMS messages from your AWS account while in the [SMS sandbox](sns-sms-sandbox.md "sns-sms-sandbox.md"), you must complete the following setup
steps. This ensures that your account is ready for SMS messaging and that your destination
phone numbers are properly verified.

1. Create an **[origination
   ID](../../../sms-voice/latest/userguide/phone-number-types.md "../../../sms-voice/latest/userguide/phone-number-types.md")**. Similar to accounts outside of the SMS sandbox, an
   origination ID is necessary before you can send SMS messages to recipients in some
   countries or regions.
2. Add the **destination phone numbers** you want to
   send messages to within the SMS sandbox.
3. Verify the **phone numbers** to ensure that the
   destination phone numbers are valid for use in your SMS messages.

###### Add and verify destination phone numbers

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console menu, choose a [region that supports SMS
   messaging](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md").
3. In the navigation pane, choose **Text messaging (SMS)**.
4. In the **Sandbox destination phone numbers** section, select
   **Add phone number**.
5. Under **Destination details**, provide the following information,
   and then select **Add phone number**:
   - **Country code** and **phone number** of
     the destination.
   - The **language** you want the verification message to be
     sent in.

6. After adding the phone number, Amazon SNS will send an OTP to the provided destination
   phone number. This OTP is required for verification.
7. You will receive the OTP as a standard SMS message on the **destination
   phone number** you provided.
   - If you don’t receive the OTP within 15 minutes, select **Resend
     verification** code in the Amazon SNS console.
   - You can resend the OTP up to five times in a 24-hour period.

8. Once you receive the OTP, enter it in the **Verification code**
   box and select **Verify phone number**.
9. Check the **verification status**.
   - After successfully verifying the phone number, the phone number and its
     verification status will appear in the **Sandbox destination phone
     numbers** section.
   - If the status is **Pending**, the verification was
     unsuccessful. This may happen if, for example, you didn’t enter the country
     code correctly.
   - You can only delete pending or verified phone numbers after 24 hours or
     more have passed since the last verification attempt.

10. If you wish to use the same destination phone number in other regions, **repeat** the previous steps for each region where you
    intend to use it.

## Troubleshooting

non-receipt of an OTP text

Troubleshoot common problems that may prevent a phone number from receiving OTP
texts.

- **Amazon SNS SMS spending limit:** If your
  AWS account has exceeded the spending limit for sending SMS messages, further
  messages, including OTP texts, might not be delivered until the limit is
  increased or the billing issue is resolved.
- **Phone number not opted in for SMS
  notifications:** In some countries or regions, recipients must opt
  in to receive SMS messages from short codes, which are commonly used for OTP
  texts. If the recipient's phone number is not opted in, they will not receive
  the OTP text.
- **Carrier restrictions or filtering:** Some
  mobile carriers may have restrictions or filtering mechanisms in place that
  prevent delivery of certain types of SMS messages, including OTP texts. This
  could be due to security policies or anti-spam measures implemented by the
  carrier.
- **Invalid or incorrect phone number:** If the
  phone number provided by the recipient is incorrect or invalid, the OTP text
  will not be delivered.
- **Network issues:** Temporary network issues or
  outages could prevent the delivery of SMS messages, including OTP texts, to the
  recipient's phone.
- **Delayed delivery:** In some cases, SMS messages
  may experience delays in delivery due to network congestion or other factors.
  The OTP text may eventually be delivered, but it could be delayed beyond the
  expected timeframe.
- **Account suspension or termination:** If there
  are issues with your AWS account, such as non-payment or violation of AWS terms of service, Amazon SNS messaging capabilities, including OTP
  texts, may be suspended or terminated.
