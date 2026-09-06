

# Example of sending a template message in AWS End User Messaging Social
<a name="send-message-text"></a>

For more information on the types of message templates that can be sent, see [Message template](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates) in the *WhatsApp Business Platform Cloud API Reference*. For a list of message types that can be sent, see [Messages](https://developers.facebook.com/docs/whatsapp/conversation-types/) in the *WhatsApp Business Platform Cloud API Reference*. 

The following example shows how to use a template to [send a message](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html) to your customer using the AWS CLI. For more information on configuring the AWS CLI, see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

**Note**  
You must specify base64 encoding when you use the AWS CLI version 2. This can be done by adding the AWS CLI paramater `--cli-binary-format raw-in-base64-out` or changing the AWS CLI global configuration file. For more information, see [`cli_binary_format`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-settings) in the *AWS Command Line Interface User Guide for Version 2*.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","to":"'{{{PHONE_NUMBER}}}'","type":"template","template":{"name":"statement","language":{"code":"en_US"},"components":[{"type":"body","parameters":[{"type":"text","text":"1000"}]}]}}' --origination-phone-number-id {{{ORIGINATION_PHONE_NUMBER_ID}}} --meta-api-version v20.0
```

In the preceding command, do the following:
+ Replace {{{PHONE\_NUMBER}}} with your customer's phone number.
+ Replace {{{ORIGINATION\_PHONE\_NUMBER\_ID}}} with your phone number's ID.

The following example shows how to send a template message that doesn't contain any components.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product": "whatsapp","to": "'{{{PHONE_NUMBER}}}'","type": "template","template": {"name":"simple_template","language": {"code": "en_US"}}}' --origination-phone-number-id {{{ORIGINATION_PHONE_NUMBER_ID}}} --meta-api-version v20.0
```
+ Replace {{{PHONE\_NUMBER}}} with your customer's phone number.
+ Replace {{{ORIGINATION\_PHONE\_NUMBER\_ID}}} with your phone number's ID.