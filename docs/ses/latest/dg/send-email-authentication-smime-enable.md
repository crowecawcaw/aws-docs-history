

# Enabling S/MIME signing on a configuration set
<a name="send-email-authentication-smime-enable"></a>

You control S/MIME signing per configuration set. When you enable S/MIME signing on a configuration set, Amazon SES signs messages sent with that configuration set. Amazon SES signs the message only if the resolved email identity has an `ACTIVE` certificate attached for the From address.

## Enable S/MIME signing using the console
<a name="send-email-authentication-smime-enable-console"></a>

**To enable S/MIME signing on a configuration set**

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, under **Configuration**, choose **Configuration sets**.

1. Choose the configuration set you want to configure.

1. On the **Overview** tab, in the **General details** section, choose **Edit**.

1. Under **Secure email**, select the **Enable S/MIME signing** checkbox.

1. Choose **Save changes**.

After you enable S/MIME signing, the **Secure Email** field in **General details** displays "S/MIME Signing Enabled".

## Enable S/MIME signing using the AWS CLI
<a name="send-email-authentication-smime-enable-cli"></a>

To enable S/MIME signing on a configuration set, use the `update-configuration-set` command to set the `MessageSecurityOptions` with an S/MIME signing scheme:

```
aws sesv2 update-configuration-set \
    --configuration-set-name {{my-config-set}} \
    --message-security-options '{"SigningScheme":{"Smime":{}}}'
```

The `SignatureFormat` defaults to `DETACHED`, which is the only supported value. You can also specify it explicitly:

```
aws sesv2 update-configuration-set \
    --configuration-set-name {{my-config-set}} \
    --message-security-options '{"SigningScheme":{"Smime":{"SignatureFormat":"DETACHED"}}}'
```

To disable S/MIME signing, set the signing scheme back to the default:

```
aws sesv2 update-configuration-set \
    --configuration-set-name {{my-config-set}} \
    --message-security-options '{"SigningScheme":{"Default":{}}}'
```

## Send-time behavior
<a name="send-email-authentication-smime-send-behavior"></a>

When you enable both S/MIME and DKIM signing, Amazon SES applies the S/MIME signature before the DKIM signature. This ordering preserves the integrity of the DKIM signature because the S/MIME signature modifies the message body.

Amazon SES applies open and click tracking, template rendering, and subscription management link insertion before it signs the message. Because Amazon SES makes these modifications before signing, open and click tracking and subscription management remain compatible with S/MIME signing.

**Active certificate required at send time**  
If you send a message with S/MIME signing enabled on the configuration set, the resolved email identity must have an `ACTIVE` certificate for the From address. If no active certificate exists, Amazon SES rejects the message and returns an error.

To verify that S/MIME signing is working, you can use the **Send test email** action on the email identity detail page. When the configuration set used has S/MIME signing enabled, the test message is S/MIME signed.