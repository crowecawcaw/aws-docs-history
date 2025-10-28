Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# enable_result_cache_for_session

## Values (default in

bold)

**on (true)**, off (false)

## Description

Specifies whether to use query results caching. If
`enable_result_cache_for_session` is `on`, Amazon Redshift checks for a
valid, cached copy of the query results when a query is submitted. If a match is found
in the result cache, Amazon Redshift uses the cached results and doesn’t run the query. If
`enable_result_cache_for_session` is `off`, Amazon Redshift ignores the
results cache and runs all queries when they are submitted.

## Example

```
SET enable_result_cache_for_session TO off;
--Amazon Redshift now ignores the results cache
```
