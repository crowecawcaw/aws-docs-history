# Using custom terminologies

To use a Custom Terminology when translating text with the [TranslateText](../APIReference/API_TranslateText.md "../APIReference/API_TranslateText.md") operation,
include the optional `TerminologyNames` parameter.

For example, if you upload the following terminology file called
`Amazon_Family.csv` to your account:

```
     *en,fr*
     *Amazon Family,Amazon Famille*
```

You can use the following CLI command to translate your text using Custom
Terminology.

###### Note

This example is formatted for Unix, Linux, and macOS. For Windows, replace the backslash (\) Unix continuation
character at the end of each line with a caret (^).

```
aws translate translate-text \
     --region `region` \
     --source-language-code "en" \
     --target-language-code "fr" \
     --terminology-names "Amazon_Family" \
     --text "Have you ever stored videos in Amazon Family?"
```

This uses the selected Custom Terminology to translate this text as "Avez-vous déjà fait des achats avec Amazon Famille?"
instead of the direct (but undesirable) translation "Avez-vous déjà fait des achats avec Famille Amazon?"

The following example shows how to use the same terminology file in Python.

```
import boto3

translate = boto3.client(service_name='translate')

print("Translating 'Have you ever shopped with Amazon Family?' from English to French with the 'Amazon_Family' custom terminology...")
response = translate.translate_text(Text="Have you ever shopped with Amazon Family?", TerminologyNames=["Amazon_Family"], SourceLanguageCode="en", TargetLanguageCode="fr")
print("Translated text: " + response.get('TranslatedText'))
print("\n")

```

For more information on using the Amazon Translate operations with Custom Terminologies, see
[API Operations](../APIReference/API_Operations.md "../APIReference/API_Operations.md").
