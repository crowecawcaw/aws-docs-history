

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Consumer actions for new datashares in Amazon Redshift
<a name="writes-consumer-new"></a>

With Amazon Redshift, you can consume datashares from other AWS accounts, enabling cross-account data sharing and collaboration. A datashare is a secure way to share live data across Amazon Redshift clusters, even if they are in different AWS accounts. The following sections provide detailed steps for configuring access, creating databases from datashares, granting object level permissions, and querying shared data.

**Topics**
+ [Associating a datashare from a different AWS account in Amazon Redshift](writes-associating.md)
+ [Creating a database from a datashare in Amazon Redshift](writes-creating-database.md)
+ [Granting object level permissions to consumer users and roles in Amazon Redshift](writes-granting.md)
+ [Querying data in a datashare in Amazon Redshift](writes-querying.md)