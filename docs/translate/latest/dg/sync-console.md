# Real-time translation using the console

To use the console for real-time translations, paste input text into the **Source
language** text box or provide the input text as a file. Optionally, you can
set features such as the desired formality level, profanity masking, brevity, and custom
terminology.

You can use auto language detection with real-time translations, but you may incur a charge. For more information,
see [Automatic language detection](how-it-works.md#how-to-auto "how-it-works.md#how-to-auto").

###### Topics

- [Translate text](#sync-console-text "#sync-console-text")
- [Translate a document](#sync-console-document "#sync-console-document")
- [View equivalent API request and response
  data](#sync-console-output "#sync-console-output")
- [Use translation features](#sync-console-features "#sync-console-features")

## Translate text

Use the Amazon Translate console to translate up to 10,000 bytes of text.

1. Open the [Amazon Translate console](https://console.aws.amazon.com/translate/home "https://console.aws.amazon.com/translate/home").
2. In the navigation menu on the left, choose **Real-time
   translation**.
3. For **Source language**, select the language of the source
   text, or keep the value as **Auto** for auto detection.
4. For **Target language**, select a language.
5. Enter or paste text into the **Source language** text box. The console
   displays the translated text in the **Target language** text box.

![The translate text page of the Amazon Translate console.](/images/translate/latest/dg/images/gs-10.png)

## Translate a document

Real-time document translation supports translations from English to any supported language,
and from any supported language to English.

To translate a document using the Amazon Translate console:

1. Open the [Amazon Translate console](https://console.aws.amazon.com/translate/home "https://console.aws.amazon.com/translate/home").
2. In the navigation menu on the left, choose **Real-time
   translation**.
3. In the Translation panel, choose the **Documents** tab.

![The translate document screen of the Amazon Translate console.](images/gs-12.png) 4. For **Source language**, select the language of the source
text, or select **Auto** for auto detection. 5. For **Target language**, select a language. If the source language
is not English, you must select English for the target language. 6. Under **Upload file**, choose **Choose
file** and enter the path to the source file. The maximum file size
is 100 KB. 7. For **Document type**, select the format of the translation
source file. Document translation supports plain text, HTML, or Word (.docx) input files. 8. Choose **Translate**.

After the translation task completes, choose **Download
translation** to download the translated document to your local
hard drive. The format of the translated document (text, HTML, or Word) matches the
input document.

## View equivalent API request and response

data

After you use the console to translate the input text or document, you can view the
equivalent API request data and response data in JSON format.

1. Below the **Translation** panel, expand the **Application integration** panel.

The console displays the equivalent translation request data in JSON format.

![JSON code samples for translating text.](images/gs-20.png) 2. You can copy the **JSON request** to use in a
[TranslateText](../APIReference/API_TranslateText.md "../APIReference/API_TranslateText.md") or [TranslateDocument](../APIReference/API_TranslateDocument.md "../APIReference/API_TranslateDocument.md") API operation. 3. The JSON output in the **JSON response panel** matches the output that the API generates.

## Use translation features

To use translation features with the Amazon Translate console:

1. Open the [Amazon Translate console](https://console.aws.amazon.com/translate/home "https://console.aws.amazon.com/translate/home").
2. In the navigation menu on the left, choose **Real-time
   translation**.
3. Provide the source language, target language, and the input data (text or document) as
   described in the previous procedures.
4. Under **Additional settings**, you can choose to
   customize the output of your translation job with the following
   settings:

**Custom terminology**

Select a custom terminology file.
If the file has an entry for a source term in the input text,
Amazon Translate uses the translation from the terminology file.

For more information, see [Customizing your translations with custom
terminology](how-custom-terminology.md "how-custom-terminology.md").

**Brevity**

Reduces the length of the translation output for most translations
(compared to the translation output without brevity). Amazon Translate supports
brevity for translating text, but not for translating a document.
Amazon Translate ignores the brevity setting if the source and target language
form an unsupported language pair for brevity.

For information about supported languages, see [Using brevity in Amazon Translate](customizing-translations-brevity.md "customizing-translations-brevity.md").

**Profanity**

Masks profane words and phrases in your translation output. Amazon Translate
doesn't support profanity masking in all supported languages.

For more information, see [Masking profane words and phrases in
Amazon Translate](customizing-translations-profanity.md "customizing-translations-profanity.md").

**Formality**

For some target languages, you can set
**Formality** to formal or informal. Amazon Translate
ignores the formality setting if formality doesn't support the
target language.

For more information, see [Setting formality in Amazon Translate](customizing-translations-formality.md "customizing-translations-formality.md"). 5. For document translation, choose **Translate** to translate the document using the chosen features.

For text translation, the console applies the translation feature to the
translated text when you choose each feature.
