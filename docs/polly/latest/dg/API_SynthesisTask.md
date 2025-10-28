# SynthesisTask

SynthesisTask object that provides information about a speech
synthesis task.

## Contents

**CreationTime**

Timestamp for the time the synthesis task was started.

Type: Timestamp

Required: No

**Engine**

Specifies the engine (`standard`, `neural`,
`long-form` or `generative`) for Amazon Polly to use
when processing input text for speech synthesis. Using a voice that
is not supported for the engine selected will result in an error.

Type: String

Valid Values: `standard | neural | long-form | generative`

Required: No

**LanguageCode**

Optional language code for a synthesis task. This is only necessary if
using a bilingual voice, such as Aditi, which can be used for either
Indian English (en-IN) or Hindi (hi-IN).

If a bilingual voice is used and no language code is specified, Amazon Polly
uses the default language of the bilingual voice. The default language for
any voice is the one returned by the [DescribeVoices](API_DescribeVoices.md "API_DescribeVoices.md") operation for the `LanguageCode`
parameter. For example, if no language code is specified, Aditi will use
Indian English rather than Hindi.

Type: String

Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH`

Required: No

**LexiconNames**

List of one or more pronunciation lexicon names you want the service
to apply during synthesis. Lexicons are applied only if the language of
the lexicon is the same as the language of the voice.

Type: Array of strings

Array Members: Maximum number of 5 items.

Pattern: `[0-9A-Za-z]{1,20}`

Required: No

**OutputFormat**

The format in which the returned output will be encoded. For audio
stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will
be json.

Type: String

Valid Values: `json | mp3 | ogg_vorbis | pcm`

Required: No

**OutputUri**

Pathway for the output speech file.

Type: String

Required: No

**RequestCharacters**

Number of billable characters synthesized.

Type: Integer

Required: No

**SampleRate**

The audio frequency specified in Hz.

The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050",
and "24000". The default value for standard voices is "22050". The default
value for neural voices is "24000". The default value for long-form voices
is "24000". The default value for generative voices is "24000".

Valid values for pcm are "8000" and "16000" The default value is
"16000".

Type: String

Required: No

**SnsTopicArn**

ARN for the SNS topic optionally used for providing status
notification for a speech synthesis task.

Type: String

Pattern: `^arn:aws(-(cn|iso(-b)?|us-gov))?:sns:[a-z0-9_-]{1,50}:\d{12}:[a-zA-Z0-9_-]{1,251}([a-zA-Z0-9_-]{0,5}|\.fifo)$`

Required: No

**SpeechMarkTypes**

The type of speech marks returned for the input text.

Type: Array of strings

Array Members: Maximum number of 4 items.

Valid Values: `sentence | ssml | viseme | word`

Required: No

**TaskId**

The Amazon Polly generated identifier for a speech synthesis task.

Type: String

Pattern: `^[a-zA-Z0-9_-]{1,100}$`

Required: No

**TaskStatus**

Current status of the individual speech synthesis task.

Type: String

Valid Values: `scheduled | inProgress | completed | failed`

Required: No

**TaskStatusReason**

Reason for the current status of a specific speech synthesis task,
including errors if the task has failed.

Type: String

Required: No

**TextType**

Specifies whether the input text is plain text or SSML. The default
value is plain text.

Type: String

Valid Values: `ssml | text`

Required: No

**VoiceId**

Voice ID to use for the synthesis.

Type: String

Valid Values: `Aditi | Amy | Astrid | Bianca | Brian | Camila | Carla | Carmen | Celine | Chantal | Conchita | Cristiano | Dora | Emma | Enrique | Ewa | Filiz | Gabrielle | Geraint | Giorgio | Gwyneth | Hans | Ines | Ivy | Jacek | Jan | Joanna | Joey | Justin | Karl | Kendra | Kevin | Kimberly | Lea | Liv | Lotte | Lucia | Lupe | Mads | Maja | Marlene | Mathieu | Matthew | Maxim | Mia | Miguel | Mizuki | Naja | Nicole | Olivia | Penelope | Raveena | Ricardo | Ruben | Russell | Salli | Seoyeon | Takumi | Tatyana | Vicki | Vitoria | Zeina | Zhiyu | Aria | Ayanda | Arlet | Hannah | Arthur | Daniel | Liam | Pedro | Kajal | Hiujin | Laura | Elin | Ida | Suvi | Ola | Hala | Andres | Sergio | Remi | Adriano | Thiago | Ruth | Stephen | Kazuha | Tomoko | Niamh | Sofie | Lisa | Isabelle | Zayd | Danielle | Gregory | Burcu | Jitka | Sabrina`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/SynthesisTask.md "../../../goto/SdkForCpp/polly-2016-06-10/SynthesisTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/SynthesisTask.md "../../../goto/SdkForJavaV2/polly-2016-06-10/SynthesisTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/SynthesisTask.md "../../../goto/SdkForRubyV3/polly-2016-06-10/SynthesisTask.md")
