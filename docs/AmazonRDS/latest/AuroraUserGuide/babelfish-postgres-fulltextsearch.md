# Using Full Text Search in Babelfish

Starting with version 4.0.0, Babelfish provides limited support for Full Text Search (FTS). FTS is a powerful feature in relational databases that enables efficient searching and indexing of text-heavy data.
It allows you to perform complex text searches and retrieve relevant results quickly. FTS is particularly valuable for applications that deal
with large volumes of textual data, such as content management systems, e-commerce platforms, and document archives.

## Understanding Babelfish Full Text Search supported features

Babelfish supports the following Full Text Search features:

- CONTAINS Clause:
  - Basic support for the CONTAINS clause.

  ```
  CONTAINS (
       {
          column_name
       }
       , '<contains_search_condition>'
  )
  ```

  ###### Note

  Currently, only English language is supported.
  - Comprehensive handling and translation of `simple_term` search strings.

- `FULLTEXT INDEX` Clause:
  - Supports only `CREATE FULLTEXT INDEX ON table_name(column_name [...n]) KEY INDEX index_name` statement.
  - Supports full `DROP FULLTEXT INDEX` statement.

###### Note

In order to re-index the Full Text Index, you need to drop the Full Text Index and create a new one on the same column.

- Special characters in search condition:
  - Babelfish ensures that single occurrences of special characters in search strings are handled effectively.

  ###### Note

  While Babelfish now identifies special characters in search string, it's essential to recognize that the results obtained may vary compared to those obtained with T-SQL.

- Table alias in column_name:
  - With table alias support, users can create more concise and readable SQL queries for Full-Text Search.

## Limitations in Babelfish Full Text Search

- Currently, the following options aren't supported in Babelfish for `CONTAINS` Clause.
  - Special characters and Languages other than English aren't supported. You will receive the generic error message for unsupported
    characters and language

  ```

  `Full-text search conditions with special characters or languages other than English are not currently supported in Babelfish`

  ```

  - Multiple columns like `column_list`
  - PROPERTY attribute
  - `prefix_term`, `generation_term`, `generic_proximity_term`,
    `custom_proximity_term`, and `weighted_term`
  - Boolean operators aren't supported and you will receive the following error message when used:

  ```
  `boolean operators not supported`
  ```

  - Identifier names with dots aren't supported.

- Currently, the following options aren't supported in Babelfish for `CREATE FULLTEXT INDEX` Clause.
  - [ TYPE COLUMN type\_column\_name ]
  - [ LANGUAGE language\_term ]
  - [ STATISTICAL\_SEMANTICS ]
  - catalog filegroup options
  - with options

- Creating a full text catalog isn't supported. Creating a full text index doesn't require a full text catalog.
- `CREATE FULLTEXT INDEX` doesn't support identifier names with dots.
- Babelfish doesn't currently support consecutive special characters in search strings. You will receive the following error message when used:

```
`Consecutive special characters in the full-text search condition are not currently supported in Babelfish`
```
