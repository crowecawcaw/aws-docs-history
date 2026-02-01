Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Producer actions for new datashares in

Amazon Redshift

With Amazon Redshift, you can share live data across Amazon Redshift clusters or AWS accounts using
datashares. A datashare is a consumer-producer object that allows you to share live
data from your Amazon Redshift cluster with other clusters or AWS accounts. Creating
datashares enables secure data sharing while maintaining control over access and
ensuring data remains up-to-date. The following sections provide details on creating
datashares and adding database objects such as schemas, tables, and views to share
live data securely.

###### Topics

- [Creating a datashare in Amazon Redshift](writes-creating-datashare.md "writes-creating-datashare.md")
- [Adding objects to a datashare in
  Amazon Redshift](writes-adding-datashare.md "writes-adding-datashare.md")
- [Adding data consumers to a datashare
  in Amazon Redshift](writes-adding-data-consumer.md "writes-adding-data-consumer.md")
- [Authorizing a datashare in Amazon Redshift](writes-authorizing.md "writes-authorizing.md")
