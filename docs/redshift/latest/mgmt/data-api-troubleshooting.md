

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Troubleshooting issues for Amazon Redshift Data API
<a name="data-api-troubleshooting"></a>

Use the following sections, titled with common error messages, to help troubleshoot problems that you have with the Data API. 

**Topics**
+ [Packet for query is too large](#data-api-troubleshooting-packet-too-large)
+ [Database response exceeded size limit](#data-api-troubleshooting-response-size-too-large)

## Packet for query is too large
<a name="data-api-troubleshooting-packet-too-large"></a>

If you see an error indicating that the packet for a query is too large, generally the result set returned for a row is too large. The Data API size limit is 64 KB per row in the result set returned by the database.

To solve this issue, make sure that each row in a result set is 64 KB or less.

## Database response exceeded size limit
<a name="data-api-troubleshooting-response-size-too-large"></a>

If you see an error indicating that the database response has exceeded the size limit, generally the size of the result set returned by the database was too large. The Data API limit is 500 MB in the result set returned by the database.

To solve this issue, make sure that calls to the Data API return 500 MB of data or less. If you need to return more than 500 MB, you can run multiple statement calls with the `LIMIT` clause in your query.