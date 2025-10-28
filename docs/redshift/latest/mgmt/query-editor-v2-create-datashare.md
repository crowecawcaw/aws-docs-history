Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating datashares

You create a datashare on the cluster that you want to use as the producer
cluster. To learn more about datashare considerations, see [Data sharing
considerations in Amazon Redshift](../dg/datashare-considerations.md "../dg/datashare-considerations.md") in the _Amazon Redshift Database Developer Guide_.

1. Choose the database on the producer cluster that you want to use.
2. Create the datashare. For example:

```
create datashare *mysource*;
```

3. Set permissions on the datashare. For example:

```
grant alter, share on datashare *mysource* to *admin*;
```

4. Set permissions on the database objects that you want to share. For
   example:

```
alter datashare *mysource* add schema *public*;
```

```
alter datashare *mysource* add table *public.event*;
```

5. Set permissions on the consumer cluster namespace to access the datashare.
   For example:

```
grant usage on datashare *mysource* to namespace '*2b12345-1234-5678-9012-bb1234567890*';
```
