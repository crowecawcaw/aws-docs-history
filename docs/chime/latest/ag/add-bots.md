**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Step 3: Add the chatbot to an Amazon Chime chat room

Only a chat room administrator can add a chatbot to a chat room. They use the chatbot email address created in [Step 1](integrate-bots.md "integrate-bots.md").

###### To add a chatbot to a chat room

1. Open the Amazon Chime desktop client or web application.
2. Choose the gear icon in the upper-right corner, and choose **Manage webhooks and
   bots**.
3. Choose **Add bot**.
4. For **Email address**, enter the bot email address.
5. Choose **Add**.
   The bot name appears in the chat room roster. If there are additional
   actions necessary to add a chatbot to a chat room, provide the actions to
   the chat room administrator.

After the chatbot is added to the chat room, provide the chatbot commands to
your chat room users. One way to do this is to program your chatbot to send command
help to the chat room when it receives the chat room invite. AWS also recommends
creating a help command for your chatbot users to use.
