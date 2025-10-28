# Using write forwarding in an Amazon Aurora global database

You can reduce the number of endpoints that you need to manage for applications running on
your Aurora global database, by using _write forwarding_. With write
forwarding enabled, secondary clusters in an Aurora global database forward SQL statements that
perform write operations to the primary cluster. The primary cluster updates the source and then
propagates resulting changes back to all secondary AWS Regions.

The write forwarding configuration saves you from implementing your own mechanism to send
write operations from a secondary AWS Region to the primary Region. Aurora handles the
cross-Region networking setup. Aurora also transmits all necessary session and transactional
context for each statement. The data is always changed first on the primary cluster and then
replicated to the secondary clusters in the Aurora global database. This way, the primary cluster
is the source of truth and always has an up-to-date copy of all your data.

###### Topics

- [Using write forwarding in an Aurora MySQL global database](aurora-global-database-write-forwarding-ams.md "aurora-global-database-write-forwarding-ams.md")
- [Using write forwarding in an Aurora PostgreSQL global database](aurora-global-database-write-forwarding-apg.md "aurora-global-database-write-forwarding-apg.md")
