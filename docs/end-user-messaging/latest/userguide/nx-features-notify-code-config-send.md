

# Send a passcode
<a name="nx-features-notify-code-config-send"></a>

Send a one-time passcode to a recipient over the text, voice, or WhatsApp channel. The passcode policy is captured from the referenced notify code configuration at send time, so later updates to the configuration do not affect verifications already in progress. Supply a reference identifier to bind this send to a later validate request. In the console, you can send a test verification without creating any resources.

------
#### [ AWS Management Console ]

**To send a passcode using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Testing**, then choose the **Send code** tab.

1. Under **Step 1: Select a channel and sender type**, choose a **Channel** (**Text**, **Voice**, or **WhatsApp**). For **Send using**, choose **Use Notify Configuration** (origination and template come from the configuration) or **Bring your own origination** (choose a phone number, pool, sender ID, or RCS agent and write an inline template).

1. Under **Step 2: Choose a destination**, enter the **Destination phone number** in E.164 format.

1. Under **Step 3: Choose a code configuration**, select a code configuration. (Optional) Expand **Advanced options** to override the passcode policy, set a message template, add request context, set a **Reference ID**, or restrict destination countries.

1. Choose **Send verification code**.

------
#### [ AWS CLI ]

**To send a passcode using the AWS CLI**

1. At the command line, enter the following command:

   ```
   $ aws endusermessaging send-notify-code-verification \
   > --channel {{TEXT}} \
   > --origination-identity {{+15550000000}} \
   > --destination-identity {{+15550123456}} \
   > --notify-code-configuration {{cc-3bnvvqhwq05xr3fkj}} \
   > --reference-id {{signup-flow-1}}
   ```

   In the preceding command, make the following changes:
   + Set **--channel** to `TEXT`, `VOICE`, or `WHATSAPP`.
   + Replace {{\+15550000000}} with your origination identity (phone number, sender ID, or pool).
   + Replace {{\+15550123456}} with the recipient (an E.164 phone number for text and voice, or a WhatsApp address).
   + Set **--notify-code-configuration** to the configuration that supplies the policy and templates. If you omit it, supply the template inline with **--override-channel-parameters**.
   + Set the same **--reference-id** here and in the validate request to bind the two together.

   Use **--override-code-configuration-parameters** to override the policy for a single send.

1. The response resembles the following:

   ```
   {
       "messageId": "sms-abc123",
       "verificationId": "ver-xyz789"
   }
   ```

------