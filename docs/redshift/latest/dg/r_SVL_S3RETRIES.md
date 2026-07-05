Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVL\_S3RETRIES

Use the SVL\_S3RETRIES view to get information about why a data lake query on Amazon S3 that uses Amazon Redshift Spectrum has failed.

SVL\_S3RETRIES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### RG provisioned clusters

`SVL_S3RETRIES` is not populated on RG provisioned clusters. The view exists and remains queryable, but returns no rows for queries that ran on RG clusters, because RG uses the cluster's native reader to query Amazon S3 and does not use the Spectrum request retry model.

For Amazon S3 client retry and error details on RG provisioned clusters, use `STL_S3CLIENT` and `STL_S3CLIENT_ERROR`.

## Table columns

| Column name         | Data type                   | Description                                                                                                                                                                                |
| ------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| query               | integer                     | The query ID.                                                                                                                                                                              |
| segment             | integer                     | Segment number.<br>A query consists of multiple segments, and each segment<br>consists of one or more steps. Query segments can run in<br>parallel. Each segment runs in a single process. |
| node                | integer                     | The node number.                                                                                                                                                                           |
| slice               | integer                     | The data slice that a particular segment ran<br>against.                                                                                                                                   |
| eventtime           | timestamp without time zone | Time in UTC that the step started<br>executing.                                                                                                                                            |
| retries             | integer                     | The number of retries for the query.                                                                                                                                                       |
| successful\_fetches | integer                     | The number of times data was returned.                                                                                                                                                     |
| file\_size          | bigint                      | This size of the file in bytes.                                                                                                                                                            |
| location            | text                        | The location of the table.                                                                                                                                                                 |
| message             | text                        | The error message.                                                                                                                                                                         |

## Sample query

The following example retrieves data about failed S3 queries.

```

SELECT svl_s3retries.query, svl_s3retries.segment, svl_s3retries.node, svl_s3retries.slice, svl_s3retries.eventtime, svl_s3retries.retries,
svl_s3retries.successful_fetches, svl_s3retries.file_size, btrim((svl_s3retries."location")::text) AS "location", btrim((svl_s3retries.message)::text)
AS message FROM svl_s3retries;
```
