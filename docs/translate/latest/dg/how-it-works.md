# How Amazon Translate works

Use the Amazon Translate service to
translate content from a source language (the language of the input content) to a target
language (the language that you select for the translation output). In a batch job, you can
translate files from one or more source languages to one or more target languages.
For more information about supported languages, see [Supported languages and language codes](what-is-languages.md "what-is-languages.md").

###### Topics

- [Supported formats for the input content](#how-to-inputs "#how-to-inputs")
- [Customizing your translations](#how-to-customize "#how-to-customize")
- [Automatic language detection](#how-to-auto "#how-to-auto")
- [Exception handling](#how-to-error-msg "#how-to-error-msg")

## Supported formats for the input content

Amazon Translate, supports the following formats for the input content:

- For real-time translations:
  - **Input text** – Plain text in UTF-8 format.
    Amazon Translate provides the output content as UTF-8 text.
  - **One input file** – A file containing
    plain text (.txt), HTML (.html), or Word (.docx) content. Amazon Translate provides the
    output content as a file in the same format as the input file.

- For batch translation jobs:
  - **Collection of input files** – One or more files
    that you upload to an Amazon S3 location. Supported file formats include plain text (.txt),
    HTML (.html), Word (.docx), Excel (.xlsx), PowerPoint (.pptx) and XLIFF 1.2 (.xlf).
    Amazon Translate provides the output content as files. The
    file format for each output file matches the input file format.

## Customizing your translations

You can use the following features to customize the translations that you produce with
Amazon Translate:

- **Do-not-translate tags** – Uses start and
  end tags to specify content that you don't want to translate (in HTML content).
- **Custom terminology** – Defines how you
  want Amazon Translate to translate specific terms, such as brand names.
- **Brevity** – Reduces the length of the translation output for most translations
  (compared to the translation output without brevity).
  Brevity is supported for real-time text translations.
- **Profanity** – Masks profane words and
  phrases in your translation output.
- **Formality** – Sets the level of language
  formality in your translation output.
- **Parallel data** – Adapts the translation
  output to reflect the style, tone, and word choices in the
  example translation samples that you provide.

For information, see
[Customizing your translations](customizing-translations.md "customizing-translations.md").

## Automatic language detection

Amazon Translate can automatically detect the language used in your source text. To use automatic
language detection, specify `auto` as the source language. Amazon Translate calls Amazon Comprehend
on your behalf to determine the language used in the source text. By choosing automatic
language detection, you agree to the service terms and agreements for Amazon Comprehend. For
information about pricing for Amazon Comprehend, see [Amazon Comprehend Pricing](https://aws.amazon.com/comprehend/pricing/ "https://aws.amazon.com/comprehend/pricing/").

## Exception handling

If you specify a source or target language that isn't supported, Amazon Translate returns the
following exceptions:

- **UnsupportedLanguagePairException** –
  Amazon Translate supports translation between all supported languages. This exception is
  returned if either the source language or target language is unsupported. For
  more information, see [Supported
  languages](what-is-languages.md "what-is-languages.md").
- **DetectedLanguageLowConfidenceException**
  – If you use automatic language detection, and Amazon Translate has low confidence
  that it detected the correct source language, it returns this exception. If a
  low confidence level is acceptable, you can use the source language returned in
  the exception.
