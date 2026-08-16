# Generative voices

Amazon Polly's **generative** text-to-speech (TTS) engine offers
the most human-like, emotionally engaged, and adaptive conversational voices available
for the use via the Amazon Polly console.

The **Generative engine** is the largest Amazon Polly TTS model
to-date. It deploys a
billion-parameter transformer that converts raw text into speech codes, followed by a
convolution-based decoder that converts these speech codes into waveforms in an
incremental, streamable manner. This method shows the widely-reported emergent abilities
of Large Language Models (LLMs) when trained on increasing volumes of publicly available
and proprietary data comprising a variety of voices, languages, and styles.

The Generative engine creates synthetic speech which is emotionally engaged, assertive,
and highly colloquial in a way that is remarkably similar to a human voice. You can use
these voices as a knowledgeable customer assistant, a virtual trainer, or an advertiser
with a near-human synthetic speech.

###### Note

The state-of-the-art technology underlying these voices falls within the paradigm
of generative AI for language and voice modelling. A side effect of the technology is
that any updates to the training data and the model could result in slight variations
to the way the voices sound, even in case when their overall quality improves with model
updates. This could have an impact on use cases with different content parts synthesized
over a long time period – for example, a season of podcasts.

## Available generative voices

Amazon Polly currently offers 43 voices in a generative
variant.

|     | Language                    | Language code | Name/ID                                                              | Gender                                                         |
| --- | --------------------------- | ------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| 1   | **English (Australian)**    | en-AU         | Olivia                                                               | Female                                                         |
| 2   | **English (British)**       | en-GB         | Amy<br>Brian                                                         | Female<br>Male                                                 |
| 3   | **English (Indian)**        | en-IN         | Kajal                                                                | Female                                                         |
| 4   | **English (Ireland)**       | en-IE         | Niamh                                                                | Female                                                         |
| 5   | **English (New Zealand)**   | en-NZ         | Aria                                                                 | Female                                                         |
| 6   | **English (Singaporean)**   | en-SG         | Jasmine                                                              | Female                                                         |
| 7   | **English (South African)** | en-ZA         | Ayanda                                                               | Female                                                         |
| 8   | **English (US)**            | en-US         | Danielle<br>Joanna<br>Matthew<br>Ruth<br>Salli<br>Stephen<br>Tiffany | Female<br>Female<br>Male<br>Female<br>Female<br>Male<br>Female |
| 9   | **Dutch (Belgium)**         | nl-BE         | Lisa                                                                 | Female                                                         |
| 10  | **Dutch (Netherlands)**     | nl-NL         | Laura                                                                | Female                                                         |
| 11  | **French (Belgian)**        | fr-BE         | Isabelle                                                             | Female                                                         |
| 12  | **French (Canadian)**       | fr-CA         | Gabrielle<br>Liam                                                    | Female<br>Male                                                 |
| 13  | **French (France)**         | fr-FR         | Ambre<br>Céline<br>Florian<br>Léa<br>Rémi                            | Female<br>Female<br>Male<br>Female<br>Male                     |
| 14  | **German (Austria)**        | de-AT         | Hannah                                                               | Female                                                         |
| 15  | **German (Germany)**        | de-DE         | Daniel<br>Lennart<br>Vicki                                           | Male<br>Male<br>Female                                         |
| 16  | **German (Swiss)**          | de-CH         | Sabrina                                                              | Female                                                         |
| 17  | **Italian (Italy)**         | it-IT         | Beatrice<br>Bianca<br>Lorenzo                                        | Female<br>Female<br>Male                                       |
| 18  | **Korean (Korea)**          | ko-KR         | Seoyeon                                                              | Female                                                         |
| 19  | **Polish (Poland)**         | pl-PL         | Ewa<br>Ola                                                           | Female<br>Female                                               |
| 20  | **Portuguese (Brazilian)**  | pt-BR         | Camila                                                               | Female                                                         |
| 21  | **Spanish (Mexican)**       | es-MX         | Andrés<br>Mía                                                        | Male<br>Female                                                 |
| 22  | **Spanish (Spain)**         | es-ES         | Lucia<br>Sergio                                                      | Female<br>Male                                                 |
| 23  | **Spanish (US)**            | es-US         | Lupe<br>Pedro                                                        | Female<br>Male                                                 |

###### Note

Generative voices cost is specified on the [Amazon Polly pricing information page](https://aws.amazon.com/polly/pricing/ "https://aws.amazon.com/polly/pricing/").

## Feature and region compatibility

Amazon Polly generative voices are available in the following regions:

- US East (N. Virginia): us-east-1
- Europe (Frankfurt): eu-central-1
- US West (Oregon): us-west-2
- Asia Pacific (Tokyo): ap-northeast-1
- Asia Pacific (Seoul): ap-northeast-2
- Asia Pacific (Singapore): ap-southeast-1
- Asia Pacific (Sydney): ap-southeast-2
- Europe (London): eu-west-2
- Canada (Central): ca-central-1
- Europe (Zurich): eu-central-2
- Other Regions are not available

**The following features are supported for generative
voices:**

- Bidirectional Streaming API is now offered in Generative engine and allows for streaming input
  and output at the same time. This API is available in the following AWS regions: US East (N. Virginia),
  Europe (Frankfurt), US West (Oregon), Asia Pacific (Singapore),
  Asia Pacific (Sydney), Europe (London), Canada (Central), and Europe (Zurich). Visit the
  [documentation](API_StartSpeechSynthesisStream.md "API_StartSpeechSynthesisStream.md")
  to learn more about how to use it.
- Real-time and asynchronous speech synthesis operations.
- Newscaster speaking style is not supported in the **Generative** engine.
- Many (but not all) SSML tags are supported by Amazon Polly. For more
  information about NTTS-supported SSML tags, see [Supported SSML tags](supportedtags.md "supportedtags.md")
- As with standard voices, you can choose from various sampling rates to
  optimize the bandwidth and audio quality for your application. Valid
  sampling rates for standard and neural voices are 8 kHz, 16 kHz, 22 kHz, or
  24 kHz. The default for standard voices is 22 kHz. The default for
  generative voices is 24 kHz. Amazon Polly supports MP3, OGG (Vorbis), and raw PCM
  audio stream formats.

_Support for generating speech marks is currently not available._

###### Note

Currently Europe (London), Canada (Central) and Europe (Zurich) regions only support the following Generative voices:
Joanna (en-US), Ruth (en-US), Salli (en-US), Stephen (en-US), Tiffany (en-US), Amy (en-GB), Brian (en-GB),
Olivia (en-AU), Florian (fr-FR), Ambre (fr-FR), Lorenzo (it-IT), Beatrice (it-IT), Jasmine (en-SG), Aria (en-NZ),
Lennart (de-DE), Vicki (de-DE), Sabrina (de-CH), Hannah (de-AT), Niamh (en-IE), Camila (pt-BR), Lisa (nl-BE),
and Seoyeon (ko-KR)

###### Note

In the unlikely event of model hallucination, (and with the Generative engine's model
behavior of rendering the speech token by token) an imposed emergency stop mechanism is
in place. The built-in mechanism stops the model from rendering speech any further. This
safety feature is based on data analysis where the model has the potential to
hallucinate, usually at the end of the sentence.

There could be cases where the model thinks it is going to hallucinate and then might
end up cutting a word during a generation step, thus rendering half the word. This could
potentially generate inappropriate results.

This safety feature reduces but does not eliminate the risk. In some edge cases, the
model might continue generating random content beyond the stop threshold. Do not assume
complete protection against hallucinated speech output.
