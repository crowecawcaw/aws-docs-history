# Example of sending a template message in AWS End User Messaging Social

For more information on the types of message templates that can be sent, see [Message template](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates "https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates") in the _WhatsApp Business Platform Cloud API
Reference_. For a list of
message types that can be sent, see [Messages](https://developers.facebook.com/docs/whatsapp/conversation-types/ "https://developers.facebook.com/docs/whatsapp/conversation-types/")
in the _WhatsApp Business Platform Cloud API Reference_.

The following example shows how to use a template to [send a message](../APIReference/API_SendWhatsAppMessage.md "../APIReference/API_SendWhatsAppMessage.md") to your customer using the AWS CLI. For
more information on configuring the AWS CLI, see [Configure
the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### Note

You must specify base64 encoding when you use the AWS CLI version 2. This
can be done by adding the AWS CLI paramater `--cli-binary-format
 raw-in-base64-out` or changing the AWS CLI global configuration file. For more
information, see [`cli_binary_format`](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings") in the
_AWS Command Line Interface User Guide for Version
2_.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","to":"'`{PHONE_NUMBER}`'","type":"template","template":{"name":"statement","language":{"code":"en_US"},"components":[{"type":"body","parameters":[{"type":"text","text":"1000"}]}]}}' --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}` --meta-api-version v20.0
```

In the preceding command, do the following:

- Replace `{PHONE_NUMBER}` with your customer's phone
  number.
- Replace `{ORIGINATION_PHONE_NUMBER_ID}` with your
  phone number's ID.
  The following example shows how to send a template message that doesn't contain any
  components.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product": "whatsapp","to": "'`{PHONE_NUMBER}`'","type": "template","template": {"name":"simple_template","language": {"code": "en_US"}}}' --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}` --meta-api-version v20.0
```

- Replace `{PHONE_NUMBER}` with your customer's phone
  number.
- Replace `{ORIGINATION_PHONE_NUMBER_ID}` with your
  phone number's ID.
