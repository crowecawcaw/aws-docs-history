

# Step 1: Link your WhatsApp Business Account
<a name="nx-whatsapp-gsu-link-waba"></a>

You link a WhatsApp Business Account (WABA) through an embedded sign-up flow that connects Meta's WhatsApp Business Platform to your AWS account. During sign-up you give AWS End User Messaging access to your WABA and allow it to bill you for messages. You can create a new WABA or migrate an existing one. A WABA can exist in only one AWS Region.

**Note**  
You link a WABA through the console, using Meta's embedded sign-up. There is no AWS CLI or API command to link a WABA or add a WhatsApp phone number, because the flow requires you to sign in to Meta and grant access interactively. After the WABA is linked, you manage templates, flows, and messages with the Social messaging API.

------
#### [ Console ]

**To link a WhatsApp Business Account**

1. Open the AWS End User Messaging Social console at [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/).

1. Choose **Business accounts**.

1. On the **Link business account** page, choose **Launch Facebook portal**. A Meta login window opens.

1. Sign in with your Facebook account credentials and choose **Continue** to give AWS End User Messaging access to your WABA and permission to bill you for messages.

1. For **Meta Business account**, choose an existing account or choose **Create a Meta Business account** and enter your business name, website or profile page, and country. Choose **Next**.

1. For **Choose a WhatsApp Business Account**, choose an existing WABA or choose **Create a WhatsApp Business Account**, then choose or create a WhatsApp Business Profile. Choose **Next**.

1. For **Create a Business Profile**, enter your WhatsApp Business Account name, the display name customers see, time zone, category, business description, and website. Meta reviews the display name and emails you the result. If Meta rejects the display name, your daily messaging limit is lowered and you can be disconnected from WhatsApp. Changing the display name later requires a support ticket with Meta, so choose it carefully. Choose **Next**.

Continue to [Step 2: Add a WhatsApp business phone number](nx-whatsapp-gsu-add-number.md) to add and verify the phone number in the same flow.

------