# Integrating an Amazon Lex V2 bot with a

contact center

You can integrate Amazon Lex V2 bots with your contact centers to enable
self-service use-cases using the Amazon Lex V2 streaming API. Use these
bots as interactive voice response (IVR) agents on telephony or as a
text-based chatbot integrated into your contact center. For more
information about the streaming APIs, see [Streaming conversations to an Amazon Lex V2 bot](streaming.md "streaming.md").

With streaming APIs, you can enable the following features:

- **Interruptions**
  ("barge-in") – Callers can interrupt the bot and
  answer a question before the prompt is complete. For more
  information, see [Enabling your Amazon Lex V2 bot
  to be interrupted by the user](interrupt-bot.md "interrupt-bot.md").
- **Wait and continue** –
  Callers can instruct the bot to wait if they need time for
  retrieving additional information during a call, such as a
  credit card number or a booking ID. For more information,
  see [Enabling the
  Amazon Lex V2 bot to wait for the user to provide more information during a pause](wait-and-continue.md "wait-and-continue.md").
- **DTMF support** –
  Callers can provide information via speech or DTMF
  interchangeably.
- **SSML support** – You
  can configure Amazon Lex V2 bot prompts using SSML tags for greater
  control over speech generation from text. For more
  information, see [Generating speech from SSML
  documents](../../../polly/latest/dg/ssml.md "../../../polly/latest/dg/ssml.md") in the _Amazon Polly developer
  guide_.
- **Configurable timeouts**
  – You can configure how long to wait for customers to
  finish speaking before Amazon Lex V2 collects their speech input,
  such as answering a yes or no question, or providing a date
  or credit card number. For more information, see [Configuring timeouts for
  capturing user input with a Lex V2 bot](session-attribs-speech.md "session-attribs-speech.md").
- **Fulfillment progress updates** – You can configure the bot to respond with multiple messages based on the fulfillment status during the business logic execution for intent fulfillment. You can set the bot to respond with messages when the fulfillment begins and completes, and provides periodic updates for long running Lambda functions. For more information, see [Configuring fulfillment progress
  updates for your Lex V2 bot](streaming-progress.md "streaming-progress.md").
