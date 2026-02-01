Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Removing data consumers from a

datashare in Amazon Redshift

You can remove one or more data consumers from a datashare. Data consumers can
be namespaces that uniquely identified Amazon Redshift clusters or AWS accounts.

Console
To remove one or more data consumers from a datashare on the console,
choose one or more data consumers either from the namespace IDs or AWS
account. Then, choose **Remove**.

Amazon Redshift removes the specified data consumers from the datashare. They
lose access to the datashare immediately.

SQL
Use REVOKE USAGE ON to revoke permissions on the datashare to certain
consumers. It revokes USAGE permissions on objects within a datashare and
instantly stops access to all consumer clusters. Listing datashares and
the metadata queries, such as listing databases and tables, doesn't
return the shared objects after access is revoked. Revoke access to the
datashare from namespaces if you don't want to share the data with
the consumers anymore.

```
REVOKE USAGE ON DATASHARE salesshare FROM NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```
