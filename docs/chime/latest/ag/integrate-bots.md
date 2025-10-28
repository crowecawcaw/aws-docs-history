**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Step 1: Integrate a chatbot with Amazon Chime

After you complete the [prerequisites](use-bots.md#bots-prereqs "use-bots.md#bots-prereqs"), integrate your chatbot with Amazon Chime using the AWS CLI or Amazon Chime API.

###### Note

These procedures create a name and email address for your chatbot. Chatbot names and email addresses cannot be changed after creation.

## AWS CLI

###### To integrate a chatbot using the AWS CLI

1. To integrate your chatbot with Amazon Chime, use the **create-bot** command in the
   AWS CLI.

```
aws chime create-bot --account-id `12a3456b-7c89-012d-3456-78901e23fg45` --display-name `exampleBot` --domain `example.com`
```

    1. Enter a chatbot display name of up to 55 alphanumeric or special characters (such as +, -, %).
    2. Enter the registered domain name for your Amazon Chime Enterprise account.

2. Amazon Chime returns a response that includes the bot ID.

```

"Bot": {
        "CreatedTimestamp": "`timeStamp`",
        "DisplayName": "`exampleBot`",
        "Disabled": exampleBotFlag,
        "UserId": "`1ab2345c-67de-8901-f23g-45h678901j2k`",
        "BotId": "`botId`",
        "UpdatedTimestamp": "`timeStamp`",
        "BotType": "ChatBot",
        "SecurityToken": "`securityToken`",
        "BotEmail": "`displayName`-chimebot@`example.com`"
         }

```

3. Copy and save the bot ID and bot email address to use in the following procedures.

## Amazon Chime API

###### To integrate a chatbot using the Amazon Chime API

1. To integrate your chatbot with Amazon Chime, use the [CreateBot](../APIReference/API_CreateBot.md "../APIReference/API_CreateBot.md")
   API operation in the _Amazon Chime API Reference_.
   1. Enter a chatbot display name of up to 55 alphanumeric or special characters (such as +, -, %).
   2. Enter the registered domain name for your Amazon Chime Enterprise account.

2. Amazon Chime returns a response that includes the bot ID. Copy and save the bot ID and email address. The bot email address looks like this: ``exampleBot`-chimebot@`example.com``.

## AWS SDK for Java

The following sample code demonstrates how to integrate a chatbot using the AWS SDK for Java.

```
CreateBotRequest createBotRequest = new CreateBotRequest()
    .withAccountId("`chimeAccountId`")
    .withDisplayName("`exampleBot`")
    .withDomain("`example.com`");

chime.createBot(createBotRequest);
```

Amazon Chime returns a response that includes the bot ID. Copy and save the bot ID and email address. The bot email address looks like this: ``exampleBot`-chimebot@`example.com``.
