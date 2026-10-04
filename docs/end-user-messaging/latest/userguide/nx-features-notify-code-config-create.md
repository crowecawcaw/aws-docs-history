

# Create a notify code configuration
<a name="nx-features-notify-code-config-create"></a>

A notify code configuration is a reusable passcode policy and message-template set for one-time passcode verifications. It defines the code type, length, validity period, and maximum attempts, plus per-channel templates for the text, voice, and WhatsApp channels. Any policy field you leave blank uses the service default at send time.

------
#### [ AWS Management Console ]

**To create a notify code configuration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Code configurations**.

1. On the **Code configurations** page, choose **Create code configuration**.

1. Under **Configuration details**, for **Name** enter a display name (1–64 characters). The name does not need to be unique.

1. Under **Passcode policy**, set any of the following. Leave a field blank to use the service default at send time.
   + **Code type** — the character set for generated passcodes.
   + **Code length** — 4 to 8 characters (defaults to 6).
   + **Validity period (minutes)** — 1 to 60 minutes (defaults to 10).
   + **Maximum attempts** — 1 to 5 attempts (defaults to 3).

1. (Optional) Expand **Advanced settings** to add per-channel message templates for **Text**, **Voice**, and **WhatsApp**, a pre-approved notify template, and tags.

1. Choose **Create code configuration**.

------
#### [ AWS CLI ]

**To create a notify code configuration using the AWS CLI**

1. At the command line, enter the following command:

   ```
   $ aws endusermessaging create-notify-code-configuration \
   > --notify-code-configuration-name {{MyVerificationPolicy}} \
   > --code-configuration-parameters codeLength=6,validityPeriodMinutes=10,maxAttempts=3
   ```

   In the preceding command, make the following changes:
   + Replace {{MyVerificationPolicy}} with a name for the configuration (1–64 characters).
   + In **--code-configuration-parameters**, set any of `codeType`, `codeLength` (4–8), `validityPeriodMinutes` (1–60), and `maxAttempts` (1–5). Omit a value to use the service default at send time.

   To add per-channel templates, use **--channel-parameters** (`text`, `voice`, `whatsApp`, `notify`). To protect the configuration, add **--deletion-protection-enabled**.

1. The response resembles the following:

   ```
   {
       "notifyCodeConfiguration": {
           "notifyCodeConfigurationId": "cc-3bnvvqhwq05xr3fkj",
           "notifyCodeConfigurationName": "MyVerificationPolicy",
           "codeConfigurationParameters": {"codeLength": 6, "validityPeriodMinutes": 10, "maxAttempts": 3},
           "deletionProtectionEnabled": false
       }
   }
   ```

------