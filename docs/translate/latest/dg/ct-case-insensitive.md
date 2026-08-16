# Case-insensitive matching

Amazon Translate matches the source terms in your custom terminology regardless of letter case. When
a source term in your terminology file matches text in the input document – ignoring
differences in capitalization – Amazon Translate applies the corresponding target term. You don't
need to create separate entries for the uppercase, lowercase, or mixed-case forms of a
source term.

Amazon Translate determines the capitalization of the applied target term from the matched source
text, as follows:

- If the matched source text is all lowercase, Amazon Translate applies the target term
  exactly as it appears in your terminology file.
- If the matched source text is all uppercase, Amazon Translate applies the target term
  in all uppercase.
- If the matched source text is in title case (each word begins with a capital
  letter), Amazon Translate capitalizes the first letter of each word of the target term.
- For any other capitalization, such as mixed case
  (`coNsole`) or a phrase in which only some words are capitalized, Amazon Translate
  applies the target term exactly as it appears in your terminology file.
  For example, if your terminology file maps the source term `console` to a target
  term, Amazon Translate matches `console`, `Console`, and `CONSOLE` in
  the input text. Amazon Translate applies the target term as it appears in the file for
  `console`, with an initial capital letter for `Console`, and in all
  uppercase for `CONSOLE`.

###### Important

Amazon Translate matches custom terminology source terms regardless of letter case. If
your terminology file contains entries that differ only by letter case, such as
`console` and `Console`, Amazon Translate treats them as the same source term.
Remove duplicate entries that differ only by case.

###### Note

These capitalization rules apply to languages that distinguish uppercase and
lowercase letters. For scripts without letter case, Amazon Translate applies the target term exactly as
it appears in your terminology file. Uppercasing follows the casing rules of the target
language.

###### Note

Case-insensitive matching applies to how Amazon Translate matches source terms. As with all
custom terminology, Amazon Translate doesn't guarantee that it applies the target term for every
translation; it uses the meaning of the source and target term in the translation context to
decide whether to apply the target term. For more information, see [Best practices](ct-best-practices.md "ct-best-practices.md").

A single custom terminology file can contain up to 30 target languages. For the file size
and language quotas, see [Service quotas](what-is-limits.md#limits "what-is-limits.md#limits").
