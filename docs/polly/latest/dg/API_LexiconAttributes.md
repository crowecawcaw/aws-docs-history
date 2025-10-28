# LexiconAttributes

Contains metadata describing the lexicon such as the number of
lexemes, language code, and so on. For more information, see [Managing Lexicons](managing-lexicons.md "managing-lexicons.md").

## Contents

**Alphabet**

Phonetic alphabet used in the lexicon. Valid values are
`ipa` and `x-sampa`.

Type: String

Required: No

**LanguageCode**

Language code that the lexicon applies to. A lexicon with a
language code such as "en" would be applied to all English languages
(en-GB, en-US, en-AUS, en-WLS, and so on.

Type: String

Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH`

Required: No

**LastModified**

Date lexicon was last modified (a timestamp value).

Type: Timestamp

Required: No

**LexemesCount**

Number of lexemes in the lexicon.

Type: Integer

Required: No

**LexiconArn**

Amazon Resource Name (ARN) of the lexicon.

Type: String

Required: No

**Size**

Total size of the lexicon, in characters.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/LexiconAttributes.md "../../../goto/SdkForCpp/polly-2016-06-10/LexiconAttributes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/LexiconAttributes.md "../../../goto/SdkForJavaV2/polly-2016-06-10/LexiconAttributes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/LexiconAttributes.md "../../../goto/SdkForRubyV3/polly-2016-06-10/LexiconAttributes.md")
