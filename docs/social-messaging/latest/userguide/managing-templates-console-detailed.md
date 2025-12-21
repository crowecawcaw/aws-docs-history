# Managing message templates in the AWS Console

## Creating a message template

1. Open the AWS End User Messaging Social console at
   [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/ "https://console.aws.amazon.com/social-messaging/").
2. Choose **Business account**, and then choose a WABA.
3. On the **Message templates** tab, choose **Create template**.
4. Configure your template:
   - **Template name**: Enter a unique name for your template (lowercase letters, numbers, and underscores only)
   - **Category**: Select the template category (Marketing, Utility, or Authentication)
   - **Language**: Choose the language for your template content
   - **Header (optional)**: Add text, media, or a variable to the header
   - **Body**: Enter your message text (you can include variables using `{{1}}`, `{{2}}`, etc.)
   - **Footer (optional)**: Add footer text (up to 60 characters)
   - **Buttons (optional)**: Add call-to-action or quick reply buttons

5. Choose **Create template**.

Your template is submitted to Meta for review. Approval typically takes a few minutes to 24 hours.

## Viewing template status

Templates can have the following statuses:

- **Approved**: The template is ready to use
- **Pending**: The template is under review by Meta
- **Rejected**: The template was not approved (hover over the status to see the reason)
- **Disabled**: The template was paused due to low quality ratings

To view your templates, navigate to the **Message templates** tab in your WABA details page.

## Editing a message template

1. Select the template you want to modify.
2. Choose **Edit**.
3. Make your changes to the template content.
4. Choose **Save**.

###### Important

When you edit and submit an approved template, it enters a pending state and requires Meta approval. The template becomes unavailable for use until Meta approves your changes. Consider the impact on your messaging workflows before editing templates that are actively being used.

## Deleting a message template

1. Select the template you want to remove.
2. Choose **Delete**.
3. Confirm the deletion.

Deleted templates cannot be recovered. If you're using the template in active campaigns, those messages will fail after deletion.

## Template quality ratings

Meta assigns quality ratings to your templates based on customer feedback and engagement. Templates with low quality ratings may be paused or disabled. To maintain good quality ratings:

- Send relevant, valuable content to your customers
- Avoid sending messages too frequently
- Provide clear opt-out options
- Respond promptly to customer replies

You can view quality ratings in the template details page.

## Template variables

Use variables to personalize your messages. Variables are defined using double curly braces with numbers (`{{1}}`, `{{2}}`, etc.). When sending a message, you provide the actual values for these variables.

Variables must be provided in sequential order starting from `{{1}}`.

###### Example Template with variables

Template text: `Hello {{1}}, your order {{2}} will be delivered on {{3}}.`

When sending: Replace `{{1}}` with customer name, `{{2}}` with order number, and `{{3}}` with delivery date.

## Template categories

Marketing

Promotional content, product announcements, or offers. These templates may have sending limitations.

Utility

Account updates, order notifications, or customer service messages. These templates typically have higher sending limits.

Authentication

One-time passwords or verification codes. These templates have the highest priority and sending limits.

Choose the category that best matches your use case. Misclassifying templates may result in rejection or account restrictions.
