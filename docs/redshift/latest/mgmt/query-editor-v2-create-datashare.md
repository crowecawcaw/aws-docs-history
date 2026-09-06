

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Creating datashares
<a name="query-editor-v2-create-datashare"></a>

You create a datashare on the cluster that you want to use as the producer cluster. To learn more about datashare considerations, see [Data sharing considerations in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/datashare-considerations.html) in the *Amazon Redshift Database Developer Guide*. 

1. Choose the database on the producer cluster that you want to use.

1. Create the datashare. For example:

   ```
   create datashare mysource;
   ```

1. Set permissions on the datashare. For example:

   ```
   grant alter, share on datashare mysource to admin;
   ```

1. Set permissions on the database objects that you want to share. For example:

   ```
   alter datashare mysource add schema public;
   ```

   ```
   alter datashare mysource add table public.event;
   ```

1. Set permissions on the consumer cluster namespace to access the datashare. For example:

   ```
   grant usage on datashare mysource to namespace '2b12345-1234-5678-9012-bb1234567890';
   ```