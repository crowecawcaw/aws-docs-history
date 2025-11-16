# Understanding Amazon Lex V2 bot conversations

After you build a bot, you integrate your client application with the Amazon Lex V2 runtime operations
to hold conversations with your bot. When a user starts a conversation with your bot, Amazon Lex V2
creates a _session_. A session encapsulates the information exchanged between
your application and the bot. For more information,
see [Understanding Amazon Lex V2 bot sessions](managing-sessions.md "managing-sessions.md").

A typical conversation involves a back and forth flow between the user
and a bot. For example:

```
User : I'd like to make an appointment
Bot : What type of appointment would you like to schedule?
User : dental
Bot : When should I schedule your dental appointment?
User : Tomorrow
Bot : At what time do you want to schedule the dental appointment on 2021-01-01?
User : 9 am
Bot : 09:00 is available, should I go ahead and book your appointment?
User : Yes
Bot : Thank you. Your appointment has been set successfully.

```

Use the [RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md") or [RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md")
API operations to manage the conversations yourself. Use the
[StartConversation](../APIReference/API_runtime_StartConversation.md "../APIReference/API_runtime_StartConversation.md") API operation to let Amazon Lex V2 manage
the conversation for you.

To manage the conversation, you must send user utterances to the bot
until the conversation reaches a logical end. The current conversation
is captured in session state. The session state is updated after each
user utterance. The session state contains the current state of the
conversation and is returned by the bot in a response to each user
utterance.

A conversation can be in any of the following states:

- **ElicitIntent** –
  Indicates that the bot has not yet determined the user's
  intent.
- **ElicitSlot** – Indicates
  that the bot has detected the user's intent and is gathering the
  required information to fulfill the intent.
- **ConfirmIntent** –
  Indicates that the bot is waiting for the user to confirm that
  the information collected is correct.
- **Closed** – Indicates that
  the user's intent is complete and that the conversation with the
  bot reached a logical end.
  A user can specify a new intent after the first intent is completed.
  For more information, see [Conversation context with your Lex V2 bots](conversation-contexts.md "conversation-contexts.md").

An intent can have the one of the following states:

- **InProgress** – Indicates
  that the bot is gathering information necessary to complete the
  intent. This is in conjunction with the `ElicitSlot`
  conversation state.
- **Waiting** – Indicates
  that the user requested the bot to wait when the bot asked for
  information for a specific slot.
- **Fulfilled** – Indicates
  that the business logic in a Lambda function associated with the
  intent ran successfully.
- **ReadyForFulfillment** –
  Indicates that the bot gathered all of the information required
  to fulfill the intent and that the client application can run
  fulfillment business logic.
- **Failed** – Indicates that
  an intent has failed.
  See the following topics to learn how to use Amazon Lex V2 APIs to manage conversation context and sessions between your bot and users.

###### Topics

- [Conversation context with your Lex V2 bots](conversation-contexts.md "conversation-contexts.md")
- [Understanding Amazon Lex V2 bot sessions](managing-sessions.md "managing-sessions.md")
