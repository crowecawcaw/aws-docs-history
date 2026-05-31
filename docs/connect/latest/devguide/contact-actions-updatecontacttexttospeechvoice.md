# UpdateContactTextToSpeechVoice

Updates the Amazon Polly voice used by text-to-speech for voice contacts (message with
text-to-speech, or Amazon Lex bots). This defaults to Joanna if this action is never run.

## Parameter object

```
{
  "TextToSpeechVoice": A string holding the name of an Amazon Polly voice. May be defined statically or dynamically. If this is an invalid text to speech voice, text to speech is no longer function for this contact.
  "TextToSpeechEngine": The engine associated with the Amazon Polly voice. May be defined statically or dynamically.
  "TextToSpeechStyle" : The speech style associated with the Amazon Polly Voice. It could be None, Coversational, or Newscaster. May be defined statically or dynamically.
}
```

## Results and conditions

Results in error if voice or engine are invalid, or if the selected voice does not
support the selected engine.

## Errors

- NoMatchingError - if no other Error matches. Must always be
  defined.

## Restrictions

None. This action is supported in all flow types, and across all channels.

## Corresponding block in the UI

[Set
voice](../adminguide/set-voice.md "../adminguide/set-voice.md")
