

# Validate OTP code
<a name="nx-notify-send-validate"></a>

**Note**  
Validation is available only when AWS End User Messaging generates the code. If you generate the passcode yourself and send it with `SendNotifyTextMessage` or `SendNotifyVoiceMessage`, you validate it in your own application – there is no validate API call for that path.

When AWS End User Messaging generates the code with `SendNotifyCodeVerification`, confirm the code the recipient entered with the `ValidateNotifyCodeVerification` operation in the `endusermessaging` namespace. Use the same `--reference-id` you sent with, so the service matches the validation to the original send.

------
#### [ Console ]

**To validate a test passcode**

1. On the **Send a test verification** page, choose the **Validate code** tab.

1. Enter the destination phone number and the code the recipient received, and choose validate to confirm the result.

------
#### [ AWS CLI ]

Validate the code with the [validate-notify-code-verification](https://docs.aws.amazon.com/cli/latest/reference/endusermessaging/validate-notify-code-verification.html) command.

```
$ aws endusermessaging validate-notify-code-verification \
> --destination-identity {{+15550123456}} \
> --code {{483921}} \
> --reference-id {{signup-flow-1}}
```

The response `status` is `VALID` or `INVALID`.

------

For the full console procedure and parameters, see [Validate a passcode](nx-features-notify-code-config-validate.md).