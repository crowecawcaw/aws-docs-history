

# Sending WhatsApp Flows to users
<a name="managing-flows-send"></a>

You send Flows to users through template messages using the existing `SendWhatsAppMessage` API. No changes to the send message API are required. The Flow is embedded in the template message as a button component with a `flow` sub-type.

Before you can send a Flow, the following must be true:
+ The Flow must be in PUBLISHED status.
+ You must have a message template that references the Flow (with a Flow button).
+ The user must have opted in to receive messages from you.

## Example: Sending a Flow via template message
<a name="managing-flows-send-example"></a>

The following example sends a template message that contains a Flow button. The `flow_token` is a unique identifier you provide to track the session, and `flow_action_data` specifies the starting screen and any initial data.

```
aws socialmessaging send-whatsapp-message \
    --origination-phone-number-id {{{PHONE_NUMBER_ID}}} \
    --meta-api-version v20.0 \
    --message '{
        "messaging_product": "whatsapp",
        "to": "{{+14085551234}}",
        "type": "template",
        "template": {
            "name": "{{flow_template_name}}",
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "button",
                    "sub_type": "flow",
                    "index": "0",
                    "parameters": [
                        {
                            "type": "action",
                            "action": {
                                "flow_token": "{{unique-session-token-123}}",
                                "flow_action_data": {
                                    "screen": "{{WELCOME_SCREEN}}",
                                    "data": {}
                                }
                            }
                        }
                    ]
                }
            ]
        }
    }'
```

In the preceding command, replace the following:
+ {{{PHONE\_NUMBER\_ID}}} — Your originating phone number's ID.
+ {{\+14085551234}} — The recipient's phone number in international format.
+ {{flow\_template\_name}} — The name of your approved message template that includes a Flow button.
+ {{unique-session-token-123}} — A unique token you generate to identify this Flow session. This token is returned in the webhook when the user completes the Flow.
+ {{WELCOME\_SCREEN}} — The ID of the first screen in your Flow JSON definition.

**Note**  
The `flow_token` should be unique per session to allow you to correlate Flow responses with specific send events. You can use a UUID or any other unique identifier.

## Setting up a template for Flows
<a name="managing-flows-send-template-setup"></a>

To send a Flow, you need a message template with a Flow button configured. When creating the template, add a call-to-action button of type `FLOW` that references your published Flow ID.

For more information about creating message templates, see [Using message templates in AWS End User Messaging Social](managing-templates.md). For information about Flow template configuration, see [Sending a Flow](https://developers.facebook.com/docs/whatsapp/flows/gettingstarted/sendingaflow) in the *Meta WhatsApp Business Platform documentation*.