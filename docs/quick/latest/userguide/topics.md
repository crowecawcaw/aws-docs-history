# Working with Amazon Quick Sight Topics

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                                               |
| ------------------------------------------------------------- |
| Intended audience:<br>Amazon Quick administrators and authors |

_Topics_ are collections of one or more datasets that represent a
subject area that your business users can ask questions about.

With Quick Sight automated data prep, you get an ML-powered assist to help you create a
topic that is relevant to your end users. The first process begins with automated field
selection and classification, something like this:

- Automated data prep chooses a small number of fields to include by default to
  create a focused data space for readers to explore.
- Automated data prep selects fields that you use in other assets like reports and
  dashboards.
- Automated data prep also imports any additional fields from any related analysis
  where a topic is enabled.
- It identifies dates, dimensions, and measures, to learn how fields can be used in
  answers.
  This automatic set of fields help the author quickly get started with natural language
  analytics. Authors can always exclude fields, or include additional fields, as needed by
  using the **Include** toggle.

Next, automated data prep continues with the process by automatically labeling fields and
identifying synonyms. Automated data prep updates field names with friendly names and
synonyms using common terms. For example, a `SLS_PERSON` field might be renamed
to `Sales person`, and assigned synonyms including: `salesman`,
`saleswoman`, agent, and `sales representative`. Although you can
let automated data prep do much of the work, it's worthwhile to review the fields, names,
and synonyms to further customize them for your end users. For example, if the users refer
to a sales person as a "rep" or a "dealer" in casual conversation, then you support this
term by adding `rep` and `dealer` to the synonyms for
`SLS_PERSON`.

Finally, automated data prep detects the semantic type of each field, by sampling its data
and examining the formats applied to it by the author during analysis. Automated data prep
updates the field configuration automatically, setting formats for values used for each
field. Answers to questions are thus provided in expected formats for dates, currencies,
identifiers, Booleans, persons, and so on.

To learn more about working with topics, continue on to the following sections in this
chapter.

###### Topics

- [Navigating Topics](navigating-topics.md "navigating-topics.md")
- [Creating Quick Sight topics](topics-create.md "topics-create.md")
- [Topic workspace](topics-interface.md "topics-interface.md")
- [Working with datasets in an Quick Sight
  topic](topics-data.md "topics-data.md")
- [Making Quick Sight topics
  natural-language-friendly](topics-natural-language.md "topics-natural-language.md")
- [Sharing Quick Sight topics](topics-sharing.md "topics-sharing.md")
- [Managing Amazon Quick Sight topic
  permissions](topics-sharing-permissions.md "topics-sharing-permissions.md")
- [Reviewing Quick Sight topic
  performance and feedback](topics-performance.md "topics-performance.md")
- [Refreshing Quick Sight topic
  indexes](topics-index.md "topics-index.md")
- [Work with Quick Sight topics using the
  Amazon Quick Sight APIs](topics-cli.md "topics-cli.md")
