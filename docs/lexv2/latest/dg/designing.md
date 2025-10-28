# Creating Amazon Lex V2 bots using the Automated Chatbot Designer

The Automated Chatbot Designer helps you design bots from existing
conversation transcripts. It analyzes the transcripts and suggests an
initial design with intents and slot types. You can iterate on the bot
design, add prompts, build, test, and deploy the bot.

After you create a new bot or add a language to your bot using the
Amazon Lex V2 console or API, you can upload transcripts of conversations
between two parties. The automated chatbot designer analyzes the
transcripts and determines the intents and slot types for the bot. It
also labels the conversations that influenced the creation of a
particular intent or slot type for your review.

You use the Amazon Lex V2 console or the API to analyze conversation
transcripts and suggest intents and slot types for a bot.

###### Note

You can only use transcripts in the English (US)
language.

You can review the suggested intents and slot types after the chatbot
designer finishes the analysis. After you've added a suggested intent or
slot type, you can modify it or delete it from the bot design using the
console or the API.

The automated chatbot designer supports conversation transcript files
using the Contact Lens for Amazon Connect schema. If you are using a different
contact center application, you must transform the conversation
transcripts to the format used by the chatbot designer. For information,
see [Input transcript
format](designing-input-format.md "designing-input-format.md").

To use the automated chatbot designer, you must allow the IAM role
that is running the designer access. For the specific IAM policy, see
[Allow users to use the
Automated Chatbot Designer](security_iam_id-based-policy-examples.md#security_iam-bot-designer "security_iam_id-based-policy-examples.md#security_iam-bot-designer"). To enable Amazon Lex V2 to
encrypt output data with an optional AWS KMS key, you need to update the
key with the policy shown in [Allow users to use a AWS KMS key
to encrypt and decrypt files](security_iam_id-based-policy-examples.md#security_iam-bot-key "security_iam_id-based-policy-examples.md#security_iam-bot-key").

###### Note

If you use a KMS key, you must provide a
**KMS key policy**,
regardless of the IAM role used.

###### Topics

- [Importing conversation
  transcripts](designing-import.md "designing-import.md")
- [Creating intents and slot types](designing-create.md "designing-create.md")
- [Input transcript
  format](designing-input-format.md "designing-input-format.md")
- [Output transcript
  format](designing-output-format.md "designing-output-format.md")
