# Step 5: Use keyboard shortcuts and typeahead suggestions

The Athena query editor provides numerous keyboard shortcuts for actions like running a
query, formatting a query, line operations, and find and replace. For more information
and a complete list of shortcuts, see [Improve productivity by using keyboard shortcuts in Amazon Athena query editor](https://aws.amazon.com/blogs/big-data/improve-productivity-by-using-keyboard-shortcuts-in-amazon-athena-query-editor/ "https://aws.amazon.com/blogs/big-data/improve-productivity-by-using-keyboard-shortcuts-in-amazon-athena-query-editor/")
in the _AWS Big Data Blog_.

The Athena query editor supports typeahead code suggestions for a faster query
authoring experience. To help you write SQL queries with enhanced accuracy and increased
efficiency, it offers the following features:

- As you type, suggestions appear in real time for keywords, local variables,
  snippets, and catalog items.
- When you type a database name or table name followed by a dot, the editor
  conveniently displays a list of tables or columns to choose from.
- When you hover over a snippet suggestion, a synopsis shows a brief overview of
  the snippet's syntax and usage.
- To improve code readability, keywords and their highlighting rules have also
  been updated to align with latest syntax of Trino and Hive.
  This feature is enabled by default. To enable or disable the feature, use the
  **Code editor preferences** (gear icon) at the bottom right of the
  query editor window.
