Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_WLM_ERROR

Records all WLM-related errors as they occur.

STL_WLM_ERROR is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name  | Data type      | Description                                  |
| ------------ | -------------- | -------------------------------------------- |
| userid       | integer        | ID of the user who generated the entry.      |
| recordtime   | timestamp      | Time that the error occurred.                |
| pid          | integer        | ID for the process that generated the error. |
| error_string | character(256) | Error description.                           |
