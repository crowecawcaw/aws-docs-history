

# Using brevity in Amazon Translate
<a name="customizing-translations-brevity"></a>

When translating between languages, there are times when the translation output is longer (in character count) than desired. Longer output can cause a problem in some scenarios (such as captions, subtitles, headlines, or form fields), if there is no space for extra characters. 

You can turn on the *brevity* setting when you run real-time text translations with Amazon Translate. Brevity reduces the length of the translation output for most translations (compared to the translation output without brevity). 

**Topics**
+ [Using the brevity setting](#customizing-translations-brevity-using)
+ [Supported languages](#customizing-translations-brevity-languages)

## Using the brevity setting
<a name="customizing-translations-brevity-using"></a>

You can use the brevity setting with real-time text translation. Amazon Translate doesn't support brevity for real-time document translation or for asynchronous translation jobs.

To use brevity in a real-time text translation request, do one of the following:
+ **Console** – In the **Text** tab of the **Real-time translation** page, under **Additional settings**, choose the **Brevity** setting.
+ **AWS CLI** – In the `translate-text` command, set brevity in the `--settings` parameter to `Brevity=ON`. For more information, see [translate-text](https://docs.aws.amazon.com/cli/latest/reference/translate/translate-text.html) in the *AWS CLI Command Reference*.
+ **AWS API** – In the [TranslateText](https://docs.aws.amazon.com/translate/latest/dg/API_TranslateText.html) API operation, configure brevity in the Settings parameter.

## Supported languages
<a name="customizing-translations-brevity-languages"></a>

Amazon Translate supports brevity for the following language pairs:
+ From any [source language ](what-is-languages.md) to one of the languages in the following table.
+ From any of the languages in the following table to English.


| Language | Language code | 
| --- | --- | 
| French | fr | 
| German | de | 
| Italian | it | 
| Portuguese (Brazil) | pt | 
| Spanish | es | 

If you request brevity for translation with an unsupported language pair, **the translation proceeds** with the brevity setting turned off.