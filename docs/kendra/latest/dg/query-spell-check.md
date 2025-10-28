# Query spell checker

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

Amazon Kendra
_Spell Checker_ suggests spell corrections for a query. This can help
you keep occurrences of zero search results to a minimum and return relevant results.
Your users might receive [zero search
results](search-analytics.md#search-analytics-metrics "search-analytics.md#search-analytics-metrics") from misspelled queries with no matching results or no returned
documents. Or, your users might receive [irrelevant
search results](search-analytics.md#search-analytics-metrics "search-analytics.md#search-analytics-metrics") from misspelled queries.

Spell Checker is designed to suggest corrections for misspelled words based on words
that appear in your indexed documents and how closely a corrected word matches a
misspelled word. For example, if the word 'statements' appears in your indexed
documents, then this could closely match the misspelled word 'statments' in the query
'year-end financial statments'.

Spell Checker returns the intended or corrected words that replace misspelled words in
the original query text. For example, 'depoying kendre search' could return 'deploying
Kendra search' You can also use offset locations provided in the API to highlight or
italicize the returned corrected words in a query in your front-end application. In the
console, the corrected words are highlighted or italicized by default. For example,
'_deploying_
_Kendra_ search'.

For business-specific or specialized terms that appear in your indexed documents,
Spell Checker does not misunderstand these terms as spellings mistakes in the query. For
example, 'amazon macie' is not corrected to 'amazon mace'.

For hyphenated words, such as 'year-end', Spell Checker treats these as individual
words to suggest corrections for these words. For example, the suggested correction for
'yaer-end' could be 'year-end'.

For `DOCUMENT` and `QUESTION_ANSWER` query response types, Spell
Checker suggests corrections to misspelled words based on words in the document body.
The document body is more reliable than the title for suggesting corrections that
closely match the misspelled words. For `ANSWER` query response types, Spell
Checker suggests corrections based on words in the default question and answer document
in your index.

You can activate Spell Checker using the [SpellCorrectionConfiguration](../APIReference/API_SpellCorrectionConfiguration.md "../APIReference/API_SpellCorrectionConfiguration.md") object. You set
`IncludeQuerySpellCheckSuggestions` to `TRUE`. Spell Checker
is activated by default in the console. It is built into the console by default.

Spell Checker can also suggest spell corrections for queries in multiple languages,
not only English. For a list of languages supported for Spell Checker, see [Amazon Kendra supported languages](in-adding-languages.md "in-adding-languages.md").

## Using the query spell checker with

default limits

Spell Checker is designed with certain defaults or limits. The following is a list
of current limits that apply when you activate spell correction suggestions.

- Suggested spell corrections cannot be returned for words that are less
  than three characters or more than 30 characters in length. To allow for
  more than 30 characters or less than three characters, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").
- Suggested spell corrections cannot restrict suggestions based on user
  access control or your access control list for [user context
  filtering](user-context-filter.md "user-context-filter.md"). Spell corrections are based on all words in your
  indexed documents, whether the words are restricted to certain users or not.
  If you want to avoid certain words appearing in the suggested spell
  corrections for queries, then do not activate
  `SpellCorrectionConfiguration`.
- Suggested spell corrections cannot be returned for words that include
  numbers. For example, 'how 2 not br8k ubun2'.
- Suggested spell corrections cannot use words that don't appear in your
  indexed documents.
- Suggested spell corrections cannot use words that are frequented less than
  0.01 percent in your indexed documents. To change the 0.01% threshold,
  contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").
