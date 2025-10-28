# Changes to conversation flows in Amazon Lex V2

On August 17, 2022 Amazon Lex V2 released a change to the way that conversations
are managed with the user. This change gives you more
control over the path that the user takes through the
conversation.

Before the change, Amazon Lex V2 managed the conversation by eliciting slots based on their
priorities in intent. You could modify this behavior dynamically and change the
conversation path based on user inputs by using DialogAction in Lambda function. This
could be done by keeping track of the conversation's current state
and programmatically deciding what to do next based on the session state.

With this change, you can create conversational paths and conditional branches using
the Amazon Lex V2 console or APIs without using a Lambda function. Amazon Lex V2 tracks the state
of the conversation and controls
what to do next based on conditions defined when the bot is created. This enables you to
easily create complex conversations while designing your bot.

These changes give you complete control over the conversation with your customer.
However, you are not required to define a path. If you do not specify a conversation
path, Amazon Lex V2 creates a default path based
on the priority of slots in your intent. You can continue to use Lambda functions to
define conversation paths dynamically. In such a
scenario, the conversation resumes based on the session state
configured in the Lambda function.

This update provides the following:

- A new console experience for creating bots with complex
  conversation flows.
- Updates to the existing APIs for creating bots to support
  the new conversation flows.
- An initial response to send a message on intent
  invocation.
- New responses for slot elicitation, Lambda invocation as
  dialog code hook and confirmation.
- Ability to specify next steps at each turn of the
  conversation.
- Evaluation of conditions to design multiple conversation
  paths.
- Setting of slot values and session attributes at any
  point during the conversation.
  Note the following for older bots:

- Bots created before August 17, 2022 continue to use the old
  mechanism to manage conversation flows. Bots created after
  that date use the new way of conversation flow management.
- New bots created via imports after August 17, 2022 use the new
  conversation flow management. Imports on existing bots
  continues to use the old way of conversation management.
- To enable the new conversation flow management for a bot created before August 17, 2022, export the
  bot, and then import the bot using a new bot name.
  The newly created bot from the import uses the new conversation flow
  management.
  Note the following for new bots created after August 17, 2022:

- Amazon Lex V2 follows the defined conversation flow exactly as designed to deliver
  the desired experience. You should configure
  all flow branches in order to avoid default conversation paths during
  runtime.
- Conversation steps following a code hook should be fully configured, because
  incomplete steps can lead to bot
  failure. We recommend that you validate bots created before August 17, 2022, because
  for these bots, there is no automatic validation of conversation steps following
  a code hook.
