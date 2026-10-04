

# Managing message templates in the console
<a name="nx-features-whatsapp-templates-console"></a>

Create and manage your WhatsApp message templates directly in the AWS End User Messaging Social console. Templates must be approved by Meta before they can be used to send messages to your customers. You can monitor the approval status of your templates in the console.

## Creating a message template
<a name="nx-features-whatsapp-templates-create"></a>

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. Choose **Business account**, and then choose a WABA.

1. On the **Message templates** tab, choose **Create template**.

1. Configure your template:
   + **Template name**: Enter a unique name for your template (lowercase letters, numbers, and underscores only)
   + **Category**: Select the template category (Marketing, Utility, or Authentication)
   + **Language**: Choose the language for your template content
   + **Header (optional)**: Add text, media, or a variable to the header
   + **Body**: Enter your message text (you can include variables using `{{1}}`, `{{2}}`, and so on)
   + **Footer (optional)**: Add footer text (up to 60 characters)
   + **Buttons (optional)**: Add call-to-action or quick reply buttons

1. Choose **Create template**.

Your template is submitted to Meta for review. Approval typically takes a few minutes to 24 hours.

## Viewing template status
<a name="nx-features-whatsapp-templates-status-view"></a>

Templates can have the following statuses:
+ **Approved**: The template is ready to use
+ **Pending**: The template is under review by Meta
+ **Rejected**: The template was not approved (hover over the status to see the reason)
+ **Disabled**: The template was paused due to low quality ratings

To view your templates, navigate to the **Message templates** tab in your WABA details page.

## Editing a message template
<a name="nx-features-whatsapp-templates-edit"></a>

1. Select the template you want to modify.

1. Choose **Edit**.

1. Make your changes to the template content.

1. Choose **Save**.

**Important**  
When you edit and submit an approved template, it enters a pending state and requires Meta approval. The template becomes unavailable for use until Meta approves your changes. Consider the impact on your messaging workflows before editing templates that are actively being used.

## Deleting a message template
<a name="nx-features-whatsapp-templates-delete"></a>

1. Select the template you want to remove.

1. Choose **Delete**.

1. Confirm the deletion.

Deleted templates cannot be recovered. If you're using the template in active campaigns, those messages will fail after deletion.

## Template quality ratings
<a name="nx-features-whatsapp-templates-quality"></a>

Meta assigns quality ratings to your templates based on customer feedback and engagement. Templates with low quality ratings may be paused or disabled. To maintain good quality ratings:
+ Send relevant, valuable content to your customers
+ Avoid sending messages too frequently
+ Provide clear opt-out options
+ Respond promptly to customer replies

You can view quality ratings in the template details page.

## Template variables
<a name="nx-features-whatsapp-templates-variables"></a>

Use variables to personalize your messages. Variables are defined using double curly braces with numbers (`{{1}}`, `{{2}}`, and so on). When sending a message, you provide the actual values for these variables.

Variables must be provided in sequential order starting from `{{1}}`.

**Example Template with variables**  
Template text: `Hello {{1}}, your order {{2}} will be delivered on {{3}}.`  
When sending: Replace `{{1}}` with customer name, `{{2}}` with order number, and `{{3}}` with delivery date.

## Template categories
<a name="nx-features-whatsapp-templates-categories"></a>

Marketing  
Promotional content, product announcements, or offers. These templates may have sending limitations.

Utility  
Account updates, order notifications, or customer service messages. These templates typically have higher sending limits.

Authentication  
One-time passwords or verification codes. These templates have the highest priority and sending limits.

Choose the category that best matches your use case. Misclassifying templates may result in rejection or account restrictions.