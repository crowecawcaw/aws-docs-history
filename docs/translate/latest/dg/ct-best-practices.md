# Best practices

Use following general best practices when using custom terminologies:

- Keep your custom terminology uncluttered. Only include terms for which you need to control the translated
  values.
- Custom terminologies are case-sensitive. If you want a target translation for the capitalized
  and non-capitalized versions of a word, include an entry for each version.
- Custom terminology isn't intended as a tool for controlling spacing, punctuation,
  or capitalization. For example, avoid the following types of entries:
  - Adding spaces – EN: USA FR: U S A
  - Adding punctuation – EN: USA FR: U.S.A
  - Changing the capitalization – EN: USA FR: Usa

- Don't include different translations for the same source phrase. For example:
  - Entry #1 – EN: Amazon FR: Amazon
  - Entry #2 – EN: Amazon FR: Amazone

- You can create custom terminology files for any of the languages that Amazon Translate
  supports.
  Amazon Translate doesn't guarantee that custom terminology will use the target term for every
  translation. To achieve high accuracy with custom terminology, follow these best practices
  when you create the content for the terminology file:

- Custom terminology works well with any words, including verbs and
  homographs. Proper names, such as brand names and product names, are ideal
  entries.
- Target terms should be fluent in the target language. Custom terminology isn't
  recommended for target terms that contain numerous special characters or formatting.
- You can include multi-word phrases or clauses in your terminology file. However,
  terms that contain multiple words are less likely to read fluently in the target
  languages.
- Custom terminology uses the meaning of the source and target term in the
  translation context to decide whether to use the target term. If a target term isn't
  a good fit in a given translation context, Amazon Translate may not use the target term.

For example, if your terminology file contains the following entry for English to
French:

`EN: order, FR: commande` (based on the English "to order"
translating into French "commander").

Amazon Translate doesn't use this entry when translating the following sentence,
because the translation context doesn't match:

"In **order** for us to help you, please share
your name."

Suggestions for avoiding this type of situation:

    + Make sure that the target term for each language is semantically
     equivalent to the source term.
    + Avoid source or target terms that have multiple meanings.
