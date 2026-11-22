

# Using write forwarding in an Amazon Aurora global database

You can reduce the number of endpoints that you need to manage for applications running on your Aurora global database by using *write forwarding*. With write forwarding enabled, an application that's connected to a secondary cluster can run SQL statements that perform write operations. The secondary cluster forwards these statements to the primary cluster, which runs them and updates its data. Aurora then replicates the resulting changes to all secondary clusters in the other AWS Regions.

The write forwarding configuration saves you from implementing your own mechanism to send write operations from a secondary AWS Region to the primary Region. Aurora handles the cross-Region networking setup. Aurora also transmits all necessary session and transactional context for each statement. The data is always changed first on the primary cluster and then replicated to the secondary clusters in the Aurora global database. This way, the primary cluster is the source of truth and always has an up-to-date copy of all your data.

**Topics**
+ [Using write forwarding in an Aurora MySQL global database](aurora-global-database-write-forwarding-ams.md)
+ [Using write forwarding in an Aurora PostgreSQL global database](aurora-global-database-write-forwarding-apg.md)