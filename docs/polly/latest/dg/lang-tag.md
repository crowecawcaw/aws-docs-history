# Specifying another language for

specific words

_<lang>_

This tag is supported by generative, long-form, neural, and standard TTS formats. For generative voices, the `<lang>` tag can be used only around full sentences.

Specify another language for a specific word, phrase, or
sentence with the <lang> tag. Foreign language words and
phrases are generally spoken better when they are enclosed
within a pair of `<lang>` tags. To specify the
language, use the `xml:lang` attribute. For a
complete list of available languages, see [Languages in Amazon Polly](supported-languages.md "supported-languages.md").

Unless you apply the `<lang>` tag, all of
the words in the input text are spoken in the language of the
voice specified in the `voice-id`. If you apply the
`<lang>` tag, the words are spoken in that
language.

For example, if the `voice-id` is Joanna (who
speaks US English), Amazon Polly speaks the following in the Joanna
voice without a French accent:

```
<speak>
     Je ne parle pas français.
</speak>
```

If you use the Joanna voice with the `<lang>`
tag, Amazon Polly speaks the sentence in the Joanna voice in
American-accented French:

```
<speak>
     <lang xml:lang="fr-FR">Je ne parle pas français.</lang>.
</speak>
```

Because Joanna is not a native French voice, pronunciation is
based on her native language, US English. For example, although
perfect French pronunciation features an uvual trill /R/ in the
word _français_, Joanna's US English
voice pronounces this phoneme as the corresponding sound /r/.

If you use the `voice-id` of Giorgio, who speaks
Italian, with the following text, Amazon Polly speaks the sentence in
Giorgio's voice with an Italian pronunciation:

```
<speak>
     Mi piace Bruce Springsteen.
</speak>
```

If you use the same voice with the following
`<lang>` tag, Amazon Polly pronounces Bruce
Springsteen in Italian-accented English:

```
<speak>
     Mi piace <lang xml:lang="en-US">Bruce Springsteen.</lang>
</speak>
```

This tag can also be used as a substitute for the optional
[DefaultLangCode](API_StartSpeechSynthesisTask.md#polly-StartSpeechSynthesisTask-request-DefaultLangCode "API_StartSpeechSynthesisTask.md#polly-StartSpeechSynthesisTask-request-DefaultLangCode") option when synthesizing speech.
However, doing so requires that you format your text using
SSML.
