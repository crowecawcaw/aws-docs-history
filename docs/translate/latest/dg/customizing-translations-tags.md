# Using do-not-translate in Amazon Translate

For HTML content, you can add do-not-translate tags to text that you don't want to
translate. This feature is available for the console and API operations.

###### Topics

- [Using do-not-translate with the console](#console-tags "#console-tags")
- [Using do-not-translate with the API](#api-tags "#api-tags")

## Using do-not-translate with the console

In the source HTML content, specify `translate="no"` in HTML tags that
surround the content that you don't want to translate. For example, to translate the
following text from English to German:

```
In French, the Louvre Museum is Musée du Louvre.
```

The text “Musée du Louvre” needs to remain in French, so we use a span tag to skip
translation for this content :

```
<p>In French, the Louvre Museum  is <span translate="no">Musée du Louvre</span>.</p>
```

This sentence has the resulting translation into German:

```
<p>Auf Französisch ist <span translate="no">Musée du Louvre</span> das Louvre-Museum.</p>
```

## Using do-not-translate with the API

You can use do-not-translate with the real-time API operations
(`TranslateText` and `TranslateDocument`) and the asynchronous
`StartTextTranslationJob` API operation. In the source text that you
provide for the API request, you can use any type of HTML element to specify content
that needs to skip translation.

In the following example, we want to translate some text from English to Spanish, but
keep some text in English:

```
aws translate translate-text \
  --source-language-code "en" \
  --target-language-code "es" \
  --region us-west-2 \
  --text "<p>You can translate this paragraph to any language.</p> <p translate=no>But do not translate this.</p>"
```

This API request returns the following Spanish translation:

```
{
    "TranslatedText": "<p>Puede traducir este párrafo a cualquier idioma.</p>
                            <p translate=no>But do not translate this.</p>",
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "es"
}
```
