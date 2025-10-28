**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Using chatbots with Amazon Chime

If you administer an Amazon Chime Enterprise account, you can create up to 10 chatbots for integration with Amazon Chime. Chatbots can only be used in chat rooms created by members of your account.
Only chat room administrators can add chatbots to a chat room. After a chatbot is added to a chat room, members of the chat room can interact with the bot using commands provided by the bot creator. For more information, see [Using chatbots](../ug/chat-bots.md "../ug/chat-bots.md") in the _Amazon Chime User Guide_.

You can also use the Amazon Chime API operation to enable or stop chatbots for your
Amazon Chime account. For more information, see [Update chatbots](update-bots.md "update-bots.md").

###### Note

You can't delete chatbots. To stop a chatbot from being used in your account, use the Amazon Chime
[UpdateBot](../APIReference/API_UpdateBot.md "../APIReference/API_UpdateBot.md") API operation in the _Amazon Chime API
Reference_. When you stop a chatbot, chat room administrators can remove
it from a chat room, but they cannot add it to a chat room. Users who @mention a
stopped chatbot in a chat room receive an error message.

Before you start the procedure to integrate chatbots with Amazon Chime, complete
the following prerequisites:

- Create a chatbot.
- Create the outbound endpoint for Amazon Chime to send events to your bot. Choose from an AWS Lambda
  function ARN or an HTTPS endpoint. For more information about Lambda, see the _[AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md")_.
  We recommend the following best practices when assigning DNS for your HTTPS endpoint:

- Use a DNS subdomain that is dedicated to the bot endpoint.
- Use only A-records to point to the bot endpoint.
- Protect your DNS servers and DNS registrar account to prevent domain hijacking.
- Use publicly valid TLS intermediate certificates that are dedicated to the bot endpoint.
- Cryptographically verify the bot message signature before acting on a bot message.
  After creating your chatbot, use the AWS Command Line Interface (AWS CLI) or the Amazon Chime API operation
  to complete the tasks described in the following sections.

###### Tasks

- [Step 1: Integrate a chatbot with Amazon Chime](integrate-bots.md "integrate-bots.md")
- [Step 2: Configure the outbound endpoint for an Amazon Chime chatbot](config-endpoints.md "config-endpoints.md")
- [Step 3: Add the chatbot to an Amazon Chime chat room](add-bots.md "add-bots.md")
- [Authenticate chatbot requests](auth-bots.md "auth-bots.md")
- [Update chatbots](update-bots.md "update-bots.md")
