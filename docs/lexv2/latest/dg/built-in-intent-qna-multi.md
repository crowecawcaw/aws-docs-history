# AMAZON.QnAIntent (multiple use support)

You can choose to have multiple AMAZON.QnAIntents within a locale. Amazon Lex V2 support up to 5 AMAZON.QnAIntents within a
bot locale.

AMAZON.QnAIntent can be triggered if one of the following cases is true:

- If a bot locale contains only 1 AMAZON.QnAIntent and that intent does not contain sample utterances, then it is activated
  when an utterance is not classified into any of the other intents present in the bot. This intent is activated when an utterance
  is not classified into any of the other intents present in the bot. Note that this intent will not be activated for missed
  utterances when eliciting a slot value.

###### Note

If the response from the FM is unsatisfactory or the call to the FM fails, Amazon Lex V2 then invokes the `AMAZON.FallbackIntent`.

- If AMAZON.QnAIntent does contain sample utterances, then it is only activated when Amazon Lex V2 recognizes that the user wants to initiate
  that intent based on user input.

###### Note

If the response from the FM is unsatisfactory or the call to the FM fails, Amazon Lex V2 invokes the failure next step, defined in the fulfillment block.

###### Note

If `botLocale` has more than 1 AMAZON.QnAIntent, then each AMAZON.QnAIntent needs to have at least 1 sample utterance.
