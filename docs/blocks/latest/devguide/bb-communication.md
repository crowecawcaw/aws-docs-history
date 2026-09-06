

# Communication
<a name="bb-communication"></a>

This section covers Blocks for sending messages to users.

## EmailClient
<a name="bb-email-client"></a>

Transactional email sending. Configure a from address and send emails with text or HTML bodies. Supports batch sending for up to 50 emails in one call.

Locally, EmailClient captures sent emails and logs them to the console for development testing. On AWS, it sends via Amazon SES. Best for signup confirmations, password resets, notifications, and any transactional communication.

For more information, see [bb-email-client on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-email-client).