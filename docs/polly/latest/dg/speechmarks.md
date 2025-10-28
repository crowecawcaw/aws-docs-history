# Speech marks

_Speech marks_ are metadata that describe the speech that you
synthesize, such as where a sentence or word starts and ends in the audio stream. When you
request speech marks for your text, Amazon Polly returns this metadata instead of synthesized
speech. By using speech marks in conjunction with the synthesized speech audio stream, you
can provide your applications with an enhanced visual experience.

For example, combining the
metadata with the audio stream from your text can enable you to synchronize speech with
facial animation (lip-syncing) or to highlight written words as they're spoken.

Speechmarks are available when using neural, long-form, or standard text-to-speech
engines.

###### Topics

- [Speech mark types](using-speechmarks.md "using-speechmarks.md")
- [Visemes and Amazon Polly](viseme.md "viseme.md")
- [Speech mark output](output.md "output.md")
- [Requesting speech marks](speechmarksconsole.md "speechmarksconsole.md")
- [Speech marks without SSML example](sp-mks-example1.md "sp-mks-example1.md")
- [Speech marks with SSML example](sp-mks-example2.md "sp-mks-example2.md")
