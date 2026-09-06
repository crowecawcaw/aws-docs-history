

# UpdateContactTextToSpeechVoice
<a name="contact-actions-updatecontacttexttospeechvoice"></a>

Updates the Amazon Polly voice used by text-to-speech for voice contacts (message with text-to-speech, or Amazon Lex bots). This defaults to Joanna if this action is never run. 

## Parameter object
<a name="updatecontacttexttospeechvoice-parameter"></a>

```
{
  "TextToSpeechVoice": A string holding the name of an Amazon Polly voice. May be defined statically or dynamically. If this is an invalid text to speech voice, text to speech is no longer function for this contact.
  "TextToSpeechEngine": The engine associated with the Amazon Polly voice. May be defined statically or dynamically.
  "TextToSpeechStyle" : The speech style associated with the Amazon Polly Voice. It could be None, Coversational, or Newscaster. May be defined statically or dynamically.
}
```

## Results and conditions
<a name="updatecontacttexttospeechvoice-results"></a>

Results in error if voice or engine are invalid, or if the selected voice does not support the selected engine.

## Errors
<a name="updatecontacttexttospeechvoice-errors"></a>
+ NoMatchingError - if no other Error matches. Must always be defined.

## Restrictions
<a name="updatecontacttexttospeechvoice-restrictions"></a>

None. This action is supported in all flow types, and across all channels. 

## Corresponding block in the UI
<a name="updatecontacttexttospeechvoice-ui"></a>

[Set voice](https://docs.aws.amazon.com/connect/latest/adminguide/set-voice.html) 