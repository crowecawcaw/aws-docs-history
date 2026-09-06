

# Set up customer authentication in Connect Customer for chat contacts
<a name="customer-auth"></a>

You can prompt your customers to sign in and authenticate during a chat. For example, unauthenticated customers engaged with a chat bot can be prompted to sign in before to being routed to an agent. 

This built-in capability uses Connect Customer Customer Profiles and [Amazon Cognito](https://aws.amazon.com/cognito/). There are no additional costs for using Customer Profiles, which is already [enabled](enable-customer-profiles.md) in your Connect Customer instance if you chose the default settings during setup. For information about Amazon Cognito pricing, see the [Amazon Cognito pricing](https://aws.amazon.com/cognito/pricing/) page.

To set up customer authentication for chat:

1. [Enable customer authentication](enable-connect-managed-auth.md#enable-customer-auth) for your Connect Customer instance.

1. [Enable the authentication message](enable-connect-managed-auth.md#enable-auth-message).

1. Add an [Authenticate Customer](authenticate-customer.md) block to your flow.

If your contact center is using an existing authentication solution external to Connect Customer, see [Pre-chat authentication](pre-chat-auth.md).