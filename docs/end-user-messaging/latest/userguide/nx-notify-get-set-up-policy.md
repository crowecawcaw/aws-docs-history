

# Step 1: Create a notify code policy
<a name="nx-notify-get-set-up-policy"></a>

Complete this step only if you want AWS End User Messaging to generate and validate the passcode. If you generate the passcode in your own application, skip to [Step 2: Create a Notify configuration](nx-notify-get-set-up-create.md).

A notify code configuration is a reusable passcode policy for AWS End User Messaging-generated one-time passcodes. It defines the code type, length, validity period, and maximum attempts, plus optional per-channel templates. AWS End User Messaging applies this policy when you call `SendNotifyCodeVerification` and `ValidateNotifyCodeVerification`. Any field you leave blank uses the service default at send time.

------
#### [ AWS Management Console ]

**To create a notify code configuration**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Notify**, choose **Code configurations**.

1. Choose **Create code configuration**.

1. Under **Configuration details**, for **Name** enter a display name (1–64 characters). The name does not need to be unique.

1. Under **Passcode policy**, set the **Code type**, **Code length** (4 to 8, defaults to 6), **Validity period (minutes)** (1 to 60, defaults to 10), and **Maximum attempts** (1 to 5, defaults to 3). Leave a field blank to use the service default at send time.

1. (Optional) Expand **Advanced settings** to add per-channel message templates for **Text**, **Voice**, and **WhatsApp**, and tags.

1. Choose **Create code configuration**.

------
#### [ AWS CLI ]

Use the `create-notify-code-configuration` command in the `endusermessaging` namespace:

```
$ aws endusermessaging create-notify-code-configuration \
    --notify-code-configuration-name "{{MyVerificationPolicy}}" \
    --code-configuration-parameters codeLength=6,validityPeriodMinutes=10,maxAttempts=3
```

In `--code-configuration-parameters`, set any of `codeType`, `codeLength` (4–8), `validityPeriodMinutes` (1–60), and `maxAttempts` (1–5). The response includes a `notifyCodeConfigurationId`, such as `cc-3bnvvqhwq05xr3fkj`, that you pass to `send-notify-code-verification`.

------

For the full set of options, including per-channel templates and deletion protection, see [Create a notify code configuration](nx-features-notify-code-config-create.md).