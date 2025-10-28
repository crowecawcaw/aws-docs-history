# Customizing your translations with custom

terminology

Use custom terminologies along with your translation requests to make sure that your brand
names, character names, model names, and other unique content get translated to the desired
result.

You can create terminology files and upload them to your Amazon Translate account. For information about file sizes and
number of terminology files, see [Service quotas](what-is-limits.md#limits "what-is-limits.md#limits").
When you translate text, you can optionally choose a custom
terminology file to use. When Amazon Translate finds a match between source text and the terminology
file, it uses the translation from the terminology file.

Consider the following example: _Amazon Photos_ provides free photo and
video storage to Amazon Prime members. In French, the name isn't translated: it remains as
_Amazon Photos_.

When you use Amazon Translate to translate _Amazon Photos_ into French without any
additional context, the result is _Photos d'Amazon_, which
isn't the desired translation.

If you add a custom terminology entry for the term _Amazon Photos_,
specifying that the French translation is _Amazon Photos_, Amazon Translate uses the
custom terminology to translate the phrase to the desired result.

Amazon Translate doesn't guarantee that it will use the target term for every translation. Custom
terminology uses the meaning of the source and target term in the translation context to
decide whether to use the target term. For more information, see [Best practices](ct-best-practices.md "ct-best-practices.md").

###### Topics

- [Creating a custom terminology](creating-custom-terminology.md "creating-custom-terminology.md")
- [Using custom terminologies](using-ct.md "using-ct.md")
- [Custom Terminology example using the AWS SDK for Python (Boto)](examples-ct.md "examples-ct.md")
- [Encrypting your terminology](protect-terminology.md "protect-terminology.md")
- [Best practices](ct-best-practices.md "ct-best-practices.md")
