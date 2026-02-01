Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting issues for

Amazon Redshift Data API

Use the following sections, titled with common error messages, to help troubleshoot
problems that you have with the Data API.

###### Topics

- [Packet for query is too
  large](#data-api-troubleshooting-packet-too-large "#data-api-troubleshooting-packet-too-large")
- [Database response
  exceeded size limit](#data-api-troubleshooting-response-size-too-large "#data-api-troubleshooting-response-size-too-large")

## Packet for query is too

large

If you see an error indicating that the packet for a query is too large, generally
the result set returned for a row is too large. The Data API size limit is 64
KB per row in the result set returned by the database.

To solve this issue, make sure that each row in a result set is 64 KB or
less.

## Database response

exceeded size limit

If you see an error indicating that the database response has exceeded the size
limit, generally the size of the result set returned by the database was too large.
The Data API limit is 500 MB in the result set returned by the database.

To solve this issue, make sure that calls to the Data API return 500 MB of
data or less. If you need to return more than 500 MB, you can run multiple statement
calls with the `LIMIT` clause in your query.
