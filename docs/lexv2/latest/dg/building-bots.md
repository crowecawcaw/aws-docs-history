# Working with Amazon Lex V2 bots

You create an Amazon Lex V2 bot to interact with your users to elicit
information to accomplish a task. For example, you can create a bot that
gathers the information needed to order a bouquet of flowers or to book a
hotel room.

To build a bot, you need the following information:

1. The language that the bot uses to interact with the customer.
   You can choose one or more languages, each language contains
   independent intents, slots, and slot types.
2. The intents, or goals, that the bot helps the user fulfill.
   A bot can contain one or more intents, such as ordering flowers,
   or booking a hotel and rental car. You need to decide which
   statements, or utterances, that the user makes to initiate the intent.
3. The information, or slots, that you need to gather from the
   user to fulfill an intent. For example, you might need to get
   the type of flowers from the user or the start date of a hotel
   reservation. You need to define one or more prompts that Amazon Lex V2
   uses to elicit the slot value from the user.
4. The type of the slots that you need from the user. You may need to create a custom
   slot type, such as a list of flowers that a user can order, or
   you can use a built-in slot type, such as using the `AMAZON.Date` slot type for the
   start date of a reservation.
5. The user interaction flow within and between intents. You can
   configure the conversation flow to define
   the interaction between the user and the bot once the intent is
   invoked. You can create a Lambda function to validate and fulfill
   the intent.

###### Topics

- [Changes to conversation flows in Amazon Lex V2](understanding-new-flows.md "understanding-new-flows.md")
- [Different ways to create a bot with Amazon Lex V2](create-bot.md "create-bot.md")
- [Adding a new language to an Amazon Lex V2 bot](add-language.md "add-language.md")
- [Adding intents](add-intents.md "add-intents.md")
- [Adding slot types](add-slot-types.md "add-slot-types.md")
- [Testing a bot using the console](test-bot.md "test-bot.md")

###### Note

On August 17, 2022, Amazon Lex V2 released a change to the way conversations are
managed with the user. This change gives you more control over the
path that the user takes through the conversation. For more information,
see [Changes to conversation flows in Amazon Lex V2](understanding-new-flows.md "understanding-new-flows.md").
Bots created before August 17, 2022 do not support dialog code hook messages,
setting values, configuring next steps, and adding conditions.
