# Creating intents and slot types

After the chatbot designer creates intents and slot types, you select
the intents and slot types to add to your bot. You can review the details
of each intent and slot type to help you decide which recommendations are
the most relevant to your use case.

You can click on a recommended intent’s name to view the sample utterances
and slots that the chatbot designer has suggested. If you select **Show associated
transcripts**, you can also scroll through the conversations that you provided.
These transcripts influence the chatbot designer’s recommendation of this intent.
If you click on a sample utterance, you can review the primary conversation and the
relevant turn of dialog, which influenced that specific utterance.

You can click on a specific slot type’s name to view the slot values that have
been recommended. If you select **Show associated transcripts**, you can review
the conversations that influenced this slot type, with the agent prompt that
elicits for the slot type highlighted. If you click on a specific slot type value,
you can review the primary conversation and the relevant turn of dialog that influenced
this value.

###### To review and add intents and slot type

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the list of bots, choose the bot you want to work
   with.
3. Choose **View languages**.
4. From the list of languages, choose the language to work
   with.
5. In **Conversation structure**, choose
   **Review**.
6. In the list of intents and slot types, choose the ones to
   add to the bot. You can choose an intent or slot type to see
   details and the associated transcripts.
   Intents are sorted by the confidence that Amazon Lex V2 has that the
   intent is associated with the processed transcripts.
