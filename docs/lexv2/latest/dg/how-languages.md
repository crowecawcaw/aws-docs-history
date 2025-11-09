# Languages and locales supported by

Amazon Lex V2

Amazon Lex V2 supports a variety of languages and locales. This topic lists
the languages that are supported and the features that support these languages.

## Supported languages and

locales

Amazon Lex V2 supports the following languages and locales.

| Code   | Language and locale                  |
| ------ | ------------------------------------ |
| ar_AE  | Gulf Arabic (United Arab Emirates)\* |
| ca_ES  | Catalan (Spain)                      |
| de_AT  | German (Austria)                     |
| de_DE  | German (Germany)                     |
| en_AU  | English (Australia)                  |
| en_GB  | English (UK)                         |
| en_IN  | English (India)                      |
| en_US  | English (US)                         |
| en_ZA  | English (South Africa)               |
| es_419 | Spanish (Latin America)              |
| es_ES  | Spanish (Spain)                      |
| es_US  | Spanish (US)                         |
| fi_FI  | Finnish (Finland)                    |
| fr_CA  | French (Canada)                      |
| fr_FR  | French (France)                      |
| hi_IN  | Hindi (India)\*\*                    |
| it_IT  | Italian (Italy)                      |
| ja_JP  | Japanese (Japan)                     |
| ko_KR  | Korean (Korea)                       |
| nl_NL  | Dutch (The Netherlands)              |
| no_NO  | Norwegian (Norway)                   |
| pl_PL  | Polish (Poland)                      |
| pt_BR  | Portuguese (Brazil)                  |
| pt_PT  | Portuguese (Portugal)                |
| sv_SE  | Swedish (Sweden)                     |
| zh_CN  | Mandarin (PRC)                       |
| zh_HK  | Cantonese (Hong Kong)                |

**\*Arabic**

The variety of Arabic that Amazon Lex V2 is trained on is Gulf Arabic.
Keep this in mind when providing sample utterances for your bot.
Note that Arabic script is written from right to left.

**\*\*Hindi**

Amazon Lex V2 is able to serve Hindi end-users who switch freely between Hindi
and English. If you plan to build a bot that supports this
language switching, we recommend the following best practices:

- In the bot definition, write English words in Latin script.
- At least 50% of your sample utterances should represent language switching
  within the same sentence. In these utterances, use Devanagari script for
  Hindi words and Latin script for English words
  (for example, "मैं ticket book करना चाहता हूं।").
- If you expect users to communicate with the bot using Hindi words in
  Latin script or English words in Devanagari script, then you should include
  examples of Hindi words in Latin script (for example, "mujhe ek ticket
  book karni hai") and English words in Devanagari script (for example,
  "मुझे टिकट की बुकिंग में मदद चाहिए") in your sample utterances.
- If you expect users to communicate with the bot using sentences that
  are completely in Hindi or completely in English, then you should include
  sample utterances that are fully in one language (for example, "I want to
  book a ticket").

## Languages and locales supported

by Amazon Lex V2 features

The following table lists Amazon Lex V2 features that are limited to
certain languages and locales. All other Amazon Lex V2 features are
supported in all languages and locales.

| Feature                                                                                                          | Supported languages and locales                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AMAZON.AlphaNumeric](built-in-slot-alphanumeric.md "built-in-slot-alphanumeric.md")                             | All languages and locales except Korean<br>(ko_KR)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [AMAZON.KendraSearchIntent](built-in-intent-kendra-search.md "built-in-intent-kendra-search.md")                 | English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Improving speech recognition with a custom vocabulary](vocab.md "vocab.md")                                     | English (UK) (en_GB)<br>English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Automated<br>Chatbot Designer](designing.md "designing.md")                                                     | English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Region availability                                                                                              | The following languages and locales are not available in the<br>Asia Pacific (Singapore) (ap-southeast-1) and Africa (Cape Town)<br>(ap-south-1) Regions:<br>• Gulf Arabic (United Arab Emirates) (ar_AE)<br>• Catalan (Spain) (ca_ES)<br>• Finnish (Finland) (fi_FI)<br>• Hindi (India) (hi_IN)<br>• Dutch (The Netherlands) (nl_NL)<br>• Norwegian (Norway) (no_NO)<br>• Polish (pl_PL)<br>• Portuguese (Brazil) (pt_BR)<br>• Portuguese (Portugal) (pt_PT)<br>• Swedish (sv_SE)<br>• Mandarin (PRC) (zh_CN)<br>• Cantonese (Hong Kong) (zh_HK) |
| [Setting intent<br>context for your Lex V2 bot](context-mgmt-active-context.md "context-mgmt-active-context.md") | English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Grammar slot type](building-srgs.md "building-srgs.md")                                                         | English (Australia) (en_AU)<br>English (UK) (en_GB)<br>English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Using multiple values in a<br>slot](multi-valued-slots.md "multi-valued-slots.md")                              | English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Improving recognition of slot values with runtime hints in the conversation](using-hints.md "using-hints.md")   | English (UK) (en_GB)<br>English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Capturing slot values with spelling styles during the conversation](spelling-styles.md "spelling-styles.md")    | English (Australia) (en_AU)<br>English (UK) (en_GB)<br>English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Using confidence<br>scores to improve conversation accuracy](confidence-scores.md "confidence-scores.md")       | English (UK) (en_GB)<br>English (US) (en_US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Regions

For a list of AWS Regions where Amazon Lex V2 is available, see [AWS regions and endpoints](../../../general/latest/gr/lex.md "../../../general/latest/gr/lex.md") in the
AWS General Reference.
