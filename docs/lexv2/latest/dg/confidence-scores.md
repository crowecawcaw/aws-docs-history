# Using confidence

scores to improve conversation accuracy

There are two steps that Amazon Lex V2 uses to determine what a user says.
The first, automatic speech recognition (ASR), creates a transcript of
the user's audio utterance. The second, natural language understanding
(NLU), determines the meaning of the user's utterance to recognize the
user's intent or the value of slots.

By default, Amazon Lex V2 returns the most likely result from ASR and NLU. At
times it may be difficult for Amazon Lex V2 to determine the most likely
result. In that case, it returns several possible results along with a
_confidence score_ that indicates how likely the
result is correct. A confidence score is a rating that Amazon Lex V2 provides
that shows the relative confidence that it has in the result. Confidence
scores range from 0.0 to 1.0.

You can use your domain knowledge with the confidence score to help
determine the correct interpretation of the ASR or NLU result.

The ASR, or transcription, confidence score is a rating on how
confident Amazon Lex V2 is that a particular transcription is correct. The NLU,
or intent, confidence score is a rating on how confident Amazon Lex V2 is that
the intent specified by the top transcription is correct. Use the
confidence score that best fits your application.

###### Topics

- [Using intent confidence
  scores to improve intent selection with Lex V2](using-intent-confidence-scores.md "using-intent-confidence-scores.md")
- [Using voice transcription confidence scores to improve conversations with your Lex V2 bot](using-transcript-confidence-scores.md "using-transcript-confidence-scores.md")
