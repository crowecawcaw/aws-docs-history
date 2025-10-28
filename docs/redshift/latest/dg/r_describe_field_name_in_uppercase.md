Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# describe_field_name_in_uppercase

## Values (default in

bold)

**off (false)**, on (true)

## Description

Specifies whether column names returned by SELECT statements are uppercase or
lowercase. If this parameter is on, column names are returned in uppercase. If this
parameter is off, column names are returned in lowercase. Amazon Redshift stores column names in
lowercase regardless of the setting for
`describe_field_name_in_uppercase`.

## Example

```
set describe_field_name_in_uppercase to on;

show describe_field_name_in_uppercase;

DESCRIBE_FIELD_NAME_IN_UPPERCASE
--------------------------------
on
```
