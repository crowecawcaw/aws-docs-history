Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Text-based JSON functions

The functions in this section parse JSON values as VARCHAR. For parsing JSON, we recommend you instead
use the following functions, which parse JSON values as SUPER. Amazon Redshift parses SUPER values more
efficiently than VARCHAR.

- [JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md")
- [CAN_JSON_PARSE function](CAN_JSON_PARSE.md "CAN_JSON_PARSE.md")
- [JSON_SERIALIZE function](JSON_SERIALIZE.md "JSON_SERIALIZE.md")
- [JSON_SERIALIZE_TO_VARBYTE function](JSON_SERIALIZE_TO_VARBYTE.md "JSON_SERIALIZE_TO_VARBYTE.md")

###### Topics

- [IS_VALID_JSON function](IS_VALID_JSON.md "IS_VALID_JSON.md")
- [IS_VALID_JSON_ARRAY function](IS_VALID_JSON_ARRAY.md "IS_VALID_JSON_ARRAY.md")
- [JSON_ARRAY_LENGTH function](JSON_ARRAY_LENGTH.md "JSON_ARRAY_LENGTH.md")
- [JSON_EXTRACT_ARRAY_ELEMENT_TEXT
  function](JSON_EXTRACT_ARRAY_ELEMENT_TEXT.md "JSON_EXTRACT_ARRAY_ELEMENT_TEXT.md")
- [JSON_EXTRACT_PATH_TEXT function](JSON_EXTRACT_PATH_TEXT.md "JSON_EXTRACT_PATH_TEXT.md")
