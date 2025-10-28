# Set up customer authentication in Amazon Connect for chat

contacts

You can prompt your customers to sign in and authenticate during a chat. For example,
unauthenticated customers engaged with a chat bot can be prompted to sign in before to being
routed to an agent.

This built-in capability leverages Amazon Connect Customer Profiles and [Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/"). There are no additional costs for using Customer Profiles, which is already [enabled](enable-customer-profiles.md "enable-customer-profiles.md") in your Amazon Connect instance if you chose
the default settings during setup. For information about Amazon Cognito pricing, see the [Amazon Cognito pricing](https://aws.amazon.com/cognito/pricing/ "https://aws.amazon.com/cognito/pricing/") page.

To set up customer authentication for chat:

1. [Enable customer authentication](enable-connect-managed-auth.md#enable-customer-auth "enable-connect-managed-auth.md#enable-customer-auth") for
   your Amazon Connect instance.
2. [Enable the authentication
   message](enable-connect-managed-auth.md#enable-auth-message "enable-connect-managed-auth.md#enable-auth-message").
3. Add an [Authenticate Customer](authenticate-customer.md "authenticate-customer.md") block to your flow.
   If your contact center is using an existing authentication solution external to Amazon Connect, see
   [Pre-chat authentication](pre-chat-auth.md "pre-chat-auth.md").
