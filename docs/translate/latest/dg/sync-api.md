# Real-time translation using the API

Amazon Translate provides the following real-time translation operations to support interactive
applications:

- [TranslateText](../APIReference/API_TranslateText.md "../APIReference/API_TranslateText.md") – translates a block of text.
- [TranslateDocument](../APIReference/API_TranslateDocument.md "../APIReference/API_TranslateDocument.md") – translates the contents of a file (plain text, HTML, or .docx).
  These synchronous operations return the translation result directly to your application.
  If you use auto language detection with these operations, you may incur a charge. For more
  information, see [Automatic language detection](how-it-works.md#how-to-auto "how-it-works.md#how-to-auto").

## Translate text

Use the [TranslateText](../APIReference/API_TranslateText.md "../APIReference/API_TranslateText.md") operation to translate a single block of text.

### Translate text using the command line

The following example shows how to use the [TranslateText](../APIReference/API_TranslateText.md "../APIReference/API_TranslateText.md") operation from the
command line. The example is formatted for Unix, Linux, and macOS. For Windows,
replace the backslash (\) Unix continuation character at the end of each line with a
caret (^).

At the command line, enter the following command.

```
aws translate translate-text \
            --region `region` \
            --source-language-code "en" \
            --target-language-code "es" \
            --text "hello, world"
```

The command responds with the following JSON:

```
{
    "TargetLanguageCode": "es",
    "TranslatedText": "Hola, mundo",
    "SourceLanguageCode": "en"
}
```

### Translate text using a JSON file

This example shows how to use a JSON file to translate a longer text block. You
can specify the source and target language on the command line, or you specify them
in the JSON file.

###### Note

The example JSON file is formatted for readability. Reformat the
`"Text"` field to remove line breaks.

The example is formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

###### To translate text using a JSON file

1. Copy the following text into a JSON file called
   `translate.json`:

```
{
    "Text": "Amazon Translate translates documents between languages in
    real time. It uses advanced machine learning technologies
    to provide high-quality real-time translation. Use it to
    translate documents or to build applications that work in
    multiple languages.",
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "fr"
}
```

2. In the AWS CLI, run the following command:

```
aws translate translate-text \
            --region `region` \
            --cli-input-json file://translate.json > translated.json
```

The command outputs a JSON file that contains the following JSON text:

```
{
    "TargetLanguageCode": "fr",
    "TranslatedText": "Amazon Translate traduit les documents entre
    les langue en temps réel. Il utilise des technologies
    avancées d'apprentissage de la machine pour fournir
    une traduction en temps réel de haute qualité. Utilisez-le
    pour traduire des documents ou pour créer des applications
    qui fonctionnent en plusieurs langues.",
    "SourceLanguageCode": "en"
}

```

## Translate document

Use the [TranslateDocument](../APIReference/API_TranslateDocument.md "../APIReference/API_TranslateDocument.md") operation to translate a text, HTML, or Word (.docx) document and
return the translation result directly to your application.

Real-time document translation supports translations from English to any supported
language, and from any supported language to English. You can specify the source
language code or use auto detect.

### Translate document using the command line

The following example shows how to use the [TranslateDocument](../APIReference/API_TranslateDocument.md "../APIReference/API_TranslateDocument.md") operation from the
command line. The example is formatted for Unix, Linux, and macOS. For Windows,
replace the backslash (\) Unix continuation character at the end of each line with a
caret (^).

At the command line, enter the following command.

```
aws translate translate-document \
            --region `region` \
            --source-language-code "en" \
            --target-language-code "es" \
            --document-content fileb://source-lang.txt
            --document ContentType=text/plain
            --query "TranslatedDocument.Content"
            --output text | base64
            --decode > target-lang.txt

```

The command responds with the following JSON:

```
{
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "es",
    "TranslatedDocument":{
      "Content": blob
    }
}
```
