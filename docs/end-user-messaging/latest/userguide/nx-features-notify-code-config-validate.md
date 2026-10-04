

# Validate a passcode
<a name="nx-features-notify-code-config-validate"></a>

Validate a passcode that a recipient submitted. Validation succeeds when the passcode matches, the validity period has not elapsed, and the maximum number of attempts has not been exceeded. If you set a reference identifier on the send request, supply the same value here so validation matches only codes sent with that identifier. The result is `VALID` or `INVALID`.

------
#### [ AWS Management Console ]

**To validate a passcode using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Testing**, then choose the **Validate code** tab.

1. Enter the **Destination phone number** that received the code and the **Verification code**. (Optional) Enter the **Reference ID** used on the send request.

1. Choose **Validate code**.

------
#### [ AWS CLI ]

**To validate a passcode using the AWS CLI**

1. At the command line, enter the following command:

   ```
   $ aws endusermessaging validate-notify-code-verification \
   > --destination-identity {{+15550123456}} \
   > --code {{483921}} \
   > --reference-id {{signup-flow-1}}
   ```

   In the preceding command, make the following changes:
   + Replace {{\+15550123456}} with the recipient that received the code.
   + Replace {{483921}} with the passcode the recipient submitted.
   + Set **--reference-id** to the same value used on the send request, if any.

   The response `status` is `VALID` or `INVALID`.

1. The response resembles the following:

   ```
   {
       "status": "VALID"
   }
   ```

------