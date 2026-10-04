

# Step 3: Get a message template
<a name="nx-whatsapp-gsu-template"></a>

WhatsApp business messaging is template-first: to open a conversation with a customer you must send a message built from a template that Meta has approved. Create a template and submit it for approval before you send. After the template is approved, you can use it to open conversations with opted-in recipients, and then exchange free-form messages within the open conversation window.

You can create and submit a template from the AWS End User Messaging Social console or with the social messaging API.

------
#### [ Console ]

**To create a message template**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. Choose **Business account**, and then choose a WABA.

1. On the **Message templates** tab, choose **Create template**.

1. Configure the template:
   + **Template name**: a unique name (lowercase letters, numbers, and underscores only).
   + **Category**: **Marketing**, **Utility**, or **Authentication**.
   + **Language**: the language for the template content.
   + **Body**: the message text. Use `{{1}}`, `{{2}}`, and so on for variables. Add an optional header, footer, and buttons.

1. Choose **Create template**, and then submit the template for review. Meta reviews most templates within a few minutes.

------
#### [ AWS CLI ]

Use the `create-whatsapp-message-template` command. Pass the WABA ID and a template definition that sets the name, language, category, and components. The following example creates a basic English utility template with variable placeholders in the body.

```
aws socialmessaging create-whatsapp-message-template --region {{us-east-1}} \\
--id {{WABA_ID}} \\
--template-definition '{
    "name": "order_update_basic",
    "language": "en_US",
    "allow_category_change": true,
    "category": "UTILITY",
    "components": [
        {
            "type": "BODY",
            "text": "Hi {{1}}, your order #{{2}} has been shipped. Track your delivery below.",
            "example": { "body_text": [ [ "Jane", "12345" ] ] }
        }
    ]
}'
```

After the request succeeds, submit the template for review with WhatsApp. You can send with it once Meta approves it.

------

For the full set of template operations – creating, editing, checking approval status, and deleting templates, with more component examples – see [WhatsApp Message Templates](nx-features-whatsapp-templates.md).