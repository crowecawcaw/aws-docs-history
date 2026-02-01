Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# JSON functions

###### Topics

- [JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md")
- [CAN_JSON_PARSE function](CAN_JSON_PARSE.md "CAN_JSON_PARSE.md")
- [JSON_SERIALIZE function](JSON_SERIALIZE.md "JSON_SERIALIZE.md")
- [JSON_SERIALIZE_TO_VARBYTE function](JSON_SERIALIZE_TO_VARBYTE.md "JSON_SERIALIZE_TO_VARBYTE.md")
- [Text-based JSON functions](text-json-functions.md "text-json-functions.md")

###### Note

We recommend that you use the following functions for working with JSON:

- [JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md")
- [CAN_JSON_PARSE function](CAN_JSON_PARSE.md "CAN_JSON_PARSE.md")
- [JSON_SERIALIZE function](JSON_SERIALIZE.md "JSON_SERIALIZE.md")
- [JSON_SERIALIZE_TO_VARBYTE function](JSON_SERIALIZE_TO_VARBYTE.md "JSON_SERIALIZE_TO_VARBYTE.md")
  With JSON_PARSE, you only need to convert JSON text to a SUPER type value once at ingestion,
  after which you can operate on the SUPER values. Amazon Redshift parses SUPER values more efficiently
  than VARCHAR, which is the output for the text-based JSON functions.
  For more information on working with the SUPER data type, go to
  [Semi-structured data in Amazon Redshift](super-overview.md "super-overview.md").

When you need to store a relatively small set of key-value pairs, you might save space
by storing the data in JSON format. Because JSON strings can be stored in a single column,
using JSON might be more efficient than storing your data in tabular format. For example,
suppose you have a sparse table, where you need to have many columns to fully represent all
possible attributes, but most of the column values are NULL for any given row or any given
column. By using JSON for storage, you might be able to store the data for a row in
key:value pairs in a single JSON string and eliminate the sparsely-populated table columns.

In addition, you can easily modify JSON strings to store additional key:value pairs
when your JSON schema changes
without needing to add columns to a table.

We recommend using JSON sparingly. JSON isn't a good choice for storing larger
datasets because, by storing disparate data in a single column, JSON doesn't use the
Amazon Redshift column store architecture. Though Amazon Redshift supports JSON functions over
CHAR and VARCHAR columns, we recommend using SUPER for processing data in JSON
serialization format. SUPER uses a post-parse schemaless representation that can
efficiently query hierarchical data. For more information about the SUPER data type, see
[Semi-structured data in Amazon Redshift](super-overview.md "super-overview.md").

JSON uses UTF-8 encoded text strings, so JSON strings can be stored as CHAR or VARCHAR
data types.

JSON strings must be properly formatted JSON, according to the following rules:

- The root level JSON can either be a JSON object or a JSON array. A JSON object is
  an unordered set of comma-separated key:value pairs enclosed by curly braces.

For example, `{"one":1, "two":2}`

- A JSON array is an ordered set of comma-separated values enclosed by
  brackets.

An example is the following: `["first", {"one":1}, "second", 3, null]`

- JSON arrays use a zero-based index; the first element in an array is at position

0.  In a JSON key:value pair, the key is a string in double quotation marks.

- A JSON value can be any of the following:
  - JSON object
  - array
  - string
    - Represented using double quotation marks

  - number
    - Includes integers, decimals, and floats

  - boolean
  - null

- Empty objects and empty arrays are valid JSON values.
- JSON fields are case-sensitive.
- White space between JSON structural elements (such as `{ }, [ ]`) is
  ignored.
  The Amazon Redshift JSON functions and the Amazon Redshift COPY command use the same methods to work
  with JSON-formatted data. For more information about working with JSON, see [COPY from JSON format](copy-usage_notes-copy-from-json.md "copy-usage_notes-copy-from-json.md")
