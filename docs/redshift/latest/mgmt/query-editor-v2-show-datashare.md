Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Showing datashares

You can show the datashares that you've created on the producer cluster.

1. Choose the producer cluster.
2. Show the datashares. For example:

```
show datashares;
```

```
share_name	share_owner	source_database		consumer_database	share_type	createdate	is_publicaccessible	share_acl	producer_account	producer_namespace
test_datashare	100		db_producer		NULL			OUTBOUND	2/15/2022		FALSE		admin		123456789012		p1234567-8765-4321-p10987654321
```
