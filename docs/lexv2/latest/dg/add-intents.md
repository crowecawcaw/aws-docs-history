# Adding intents

Intents are the goals that your users want to accomplish, such as ordering flowers or
booking a hotel. Your bot must have at least one intent.

By default, all bots contain a single built-in intent, the
fallback intent. This intent is used when Amazon Lex V2 does not recognize
any other intent. For example, if a user says "I want to order
flowers" to a hotel booking intent, the fallback intent is
triggered.

###### To add an intent

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the list of bots, choose the bot that you want to add
   the intent to, then from **Add languages**
   choose **View languages**.
3. Choose the language to add the intent to, then choose
   **Intents**.
4. Choose **Add intent**, give your intent a
   name, and then choose **Add**.
5. In the intent editor, add the details of your
   intent.
   - **Conversation flow**
     – Use the conversation flow diagram to see how
     a dialog with your bot might look. You can choose
     different sections of the conversation to jump to
     that section of the intent editor.
   - **Intent details**
     – Give the intent a name and description to
     help identify the purpose of the intent. You can
     also see the unique identifier that Amazon Lex V2 assigned
     to the intent.
   - **Contexts** –
     Set the input and output contexts for the intent. A
     context is a state variable associated with an
     intent. An output context is set when an intent is
     fulfilled. An intent with an input context can only
     be recognized if the context is active. An intent
     with no input contexts can always be
     recognized.
   - **Sample utterances**
     – You should provide 10 or more phrases that
     you expect your users to use to initiate an intent.
     Amazon Lex V2 generalizes from these phrases to recognize
     that the user wants to initiate the intent.
   - **Initial response**
     – The initial message sent to the user after
     the intent is invoked. You can provide responses,
     initialize values, and define the next step that Amazon Lex V2
     takes to respond to the user at the beginning of the
     intent.
   - **Slots** –
     Define the slots, or parameters, required to fulfill
     the intent. Each slot has a type that defines the
     values that can be entered in the slot. You can
     choose from your custom slot types, or you can
     choose a built-in slot type.
   - **Confirmation**
     – These prompts and
     responses are used to confirm or decline fulfillment
     of the intent. The confirmation prompt asks the user to
     review slot values. For example, "I've booked a
     hotel room for Friday. Is this correct?" The
     declination response is sent to the user when they
     decline the confirmation. You can provide responses,
     set values, and define the next step that Amazon Lex V2
     takes corresponding to a confirmation or declination
     response from the user.
   - **Fulfillment** – Response sent to
     the user during the course of fulfillment.
     You can set fulfillment progress updates at the start of fulfillment and
     periodically while the fulfillment is in progress. For example, "I'm
     changing your password, this may take a few minutes" and "I'm still
     working on your request." Fulfillment updates are used only for
     streaming conversations. You can also set a post-fulfillment success
     message, a failure message, and a timeout message. You can send
     post-fulfillment messages for both streaming and regular conversations.
     For example, if the fulfillment succeeds, you can send "I've changed
     your password." If the fulfillment doesn't succeed, you can send
     a response with more information, such as "I couldn't change your
     password, contact the help desk for assistance." If the fulfillment
     takes longer than the configured timeout period, you can send a message
     informing the user, such as "Our servers are very busy right now. Try
     your request again later." You can provide responses, set values, and
     define the next step that Amazon Lex V2 takes to respond to the user.
   - **Closing responses**
     – Response sent to the user after the intent
     is fulfilled and all other messages are played. For
     example, a thank you for booking a hotel room. Or it
     can prompt the user to start a different intent,
     such as, "Thank you for booking a room, would you
     like to book a rental car?" You can provide
     responses and configure follow-up next actions after
     fulfilling the intent and responding with the closing
     response.
   - **Code hooks**
     – Indicate whether you are using an AWS Lambda
     function to initialize the intent and validate user
     input. You specify the Lambda function in the alias
     that you use to run the bot.

6. Choose **Save intent** to save the
   intent.

###### Note

On August 17, 2022, Amazon Lex V2 released a change to the way conversations are
managed with the user. This change gives you more control over the path
that the user takes through the conversation. For more information,
see [Changes to conversation flows in Amazon Lex V2](understanding-new-flows.md "understanding-new-flows.md").
Bots created before August 17, 2022 do not support dialog code hook messages,
setting values, configuring next steps, and adding conditions.

## Configuring prompts in a specific order

You can configure the bot to play messages in a predefined order
by checking the box for **Play messages in order**.
Otherwise, the bot plays the message and the variations in
random order.

Ordered prompts
allow the message and variations of a message group to play in order
among retries. You can use alternate rephrasing of a message when an
invalid response for the prompt is given by the user, or for intent
confirmation. Up to two variations of the original message may be set
in each slot. You can choose whether to play the messages in order or
randomly.

Ordered prompt supports all four types of messages: text, custom
payload response, SSML, and card group. Responses are ordered within
the same message group. Different message groups are independent.

###### Topics

- [Sample utterances](sample-utterances.md "sample-utterances.md")
- [Intent structure](intent-structure.md "intent-structure.md")
- [Creating conversation paths](building-paths.md "building-paths.md")
- [Using Visual conversation builder](visual-conversation-builder.md "visual-conversation-builder.md")
- [Built-in intents](built-in-intents.md "built-in-intents.md")
