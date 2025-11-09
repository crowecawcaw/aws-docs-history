Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_S3RETRIES

Use the SVL_S3RETRIES view to get information about why an Amazon Redshift Spectrum query based
on Amazon S3 has failed.

SVL_S3RETRIES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name        | Data type                   | Description                                                                                                                                                                                |
| ------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| query              | integer                     | The query ID.                                                                                                                                                                              |
| segment            | integer                     | Segment number.<br>A query consists of multiple segments, and each segment<br>consists of one or more steps. Query segments can run in<br>parallel. Each segment runs in a single process. |
| node               | integer                     | The node number.                                                                                                                                                                           |
| slice              | integer                     | The data slice that a particular segment ran<br>against.                                                                                                                                   |
| eventtime          | timestamp without time zone | Time in UTC that the step started<br>executing.                                                                                                                                            |
| retries            | integer                     | The number of retries for the query.                                                                                                                                                       |
| successful_fetches | integer                     | The number of times data was returned.                                                                                                                                                     |
| file_size          | bigint                      | This size of the file in bytes.                                                                                                                                                            |
| location           | text                        | The location of the table.                                                                                                                                                                 |
| message            | text                        | The error message.                                                                                                                                                                         |

## Sample query

The following example retrieves data about failed S3 queries.

```

SELECT svl_s3retries.query, svl_s3retries.segment, svl_s3retries.node, svl_s3retries.slice, svl_s3retries.eventtime, svl_s3retries.retries,
svl_s3retries.successful_fetches, svl_s3retries.file_size, btrim((svl_s3retries."location")::text) AS "location", btrim((svl_s3retries.message)::text)
AS message FROM svl_s3retries;
```
