

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Showing datashares
<a name="query-editor-v2-show-datashare"></a>

You can show the datashares that you've created on the producer cluster. 

1. Choose the producer cluster.

1. Show the datashares. For example:

   ```
   show datashares;
   ```

   ```
   share_name	share_owner	source_database		consumer_database	share_type	createdate	is_publicaccessible	share_acl	producer_account	producer_namespace
   test_datashare	100		db_producer		NULL			OUTBOUND	2/15/2022		FALSE		admin		123456789012		p1234567-8765-4321-p10987654321
   ```