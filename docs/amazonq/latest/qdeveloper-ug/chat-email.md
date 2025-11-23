# Chatting about email sending

Amazon Q can help you set up email sending in Amazon Simple Email Service (Amazon SES),
helping you to optimize your sending delivery and engagement rates, and troubleshoot sending problems. When you ask
Amazon Q about Amazon SES, it’s responses include information about the sending identities, configuration sets,
and other Amazon SES resources in your account. It is also able to answer questions about your email
sending patterns, as well as patterns of responses from mailbox providers such as Gmail and Yahoo.

## Prerequisites

You can chat about your Amazon SES in the AWS Management Console and in [configured chat applications](q-in-chat-applications.md "q-in-chat-applications.md").

For Amazon Q to answer questions about your email sending, the following
prerequisites must be met.

### Add permissions

To chat about your email sending, your IAM identity must have permissions to
chat with Amazon Q. For an IAM policy that grants the required
permissions, see [Allow users to chat with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-chat"). You must also have permissions to access the Amazon SES resources you ask about.

## Example questions

Following are example questions about email sending that you can ask Amazon Q:

- Do I need to do anything to finish setting up SES for email sending?
- Tell me which sending identities have the best deliverability performance.
- How is my deliverability for emails sent to Yahoo?
- Do you have any recommendations to improve my sending?
- Tell me if there have been any recent events where my deliverability performance suddenly improved or worsened.
