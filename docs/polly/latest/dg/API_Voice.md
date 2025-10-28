# Voice

Description of the voice.

## Contents

**AdditionalLanguageCodes**

Additional codes for languages available for the specified voice in
addition to its default language.

For example, the default language for Aditi is Indian English (en-IN)
because it was first used for that language. Since Aditi is bilingual and
fluent in both Indian English and Hindi, this parameter would show the
code `hi-IN`.

Type: Array of strings

Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH`

Required: No

**Gender**

Gender of the voice.

Type: String

Valid Values: `Female | Male`

Required: No

**Id**

Amazon Polly assigned voice ID. This is the ID that you specify when
calling the `SynthesizeSpeech` operation.

Type: String

Valid Values: `Aditi | Amy | Astrid | Bianca | Brian | Camila | Carla | Carmen | Celine | Chantal | Conchita | Cristiano | Dora | Emma | Enrique | Ewa | Filiz | Gabrielle | Geraint | Giorgio | Gwyneth | Hans | Ines | Ivy | Jacek | Jan | Joanna | Joey | Justin | Karl | Kendra | Kevin | Kimberly | Lea | Liv | Lotte | Lucia | Lupe | Mads | Maja | Marlene | Mathieu | Matthew | Maxim | Mia | Miguel | Mizuki | Naja | Nicole | Olivia | Penelope | Raveena | Ricardo | Ruben | Russell | Salli | Seoyeon | Takumi | Tatyana | Vicki | Vitoria | Zeina | Zhiyu | Aria | Ayanda | Arlet | Hannah | Arthur | Daniel | Liam | Pedro | Kajal | Hiujin | Laura | Elin | Ida | Suvi | Ola | Hala | Andres | Sergio | Remi | Adriano | Thiago | Ruth | Stephen | Kazuha | Tomoko | Niamh | Sofie | Lisa | Isabelle | Zayd | Danielle | Gregory | Burcu | Jitka | Sabrina`

Required: No

**LanguageCode**

Language code of the voice.

Type: String

Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH`

Required: No

**LanguageName**

Human readable name of the language in English.

Type: String

Required: No

**Name**

Name of the voice (for example, Salli, Kendra, etc.). This provides
a human readable voice name that you might display in your
application.

Type: String

Required: No

**SupportedEngines**

Specifies which engines (`standard`, `neural`,
`long-form` or `generative`) are supported by a given voice.

Type: Array of strings

Valid Values: `standard | neural | long-form | generative`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/Voice.md "../../../goto/SdkForCpp/polly-2016-06-10/Voice.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/Voice.md "../../../goto/SdkForJavaV2/polly-2016-06-10/Voice.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/Voice.md "../../../goto/SdkForRubyV3/polly-2016-06-10/Voice.md")
