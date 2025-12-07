# Using a Service Master Key with RDS Custom for SQL Server

RDS Custom for SQL Server supports using a Service Master Key (SMK). RDS Custom retains the same SMK throughout the lifespan of your RDS Custom for SQL Server DB instance.
By retaining the same SMK, your DB instance can use objects that are encrypted with the SMK, such as linked server passwords and credentials.
If you use a Multi-AZ deployment, RDS Custom also synchronizes and maintains the SMK between primary and secondary DB instances.

###### Topics

- [Region and version availability](#custom-sqlserver-features.smk.list "#custom-sqlserver-features.smk.list")
- [Supported features](#custom-sqlserver-features.smk.supportedfeatures "#custom-sqlserver-features.smk.supportedfeatures")
- [Using TDE](#custom-sqlserver-features.smk.tde "#custom-sqlserver-features.smk.tde")
- [Configuring features](#custom-sqlserver-features.smk.configuringfeatures "#custom-sqlserver-features.smk.configuringfeatures")
- [Requirements and limitations](#custom-sqlserver-features.smk.reqlimits "#custom-sqlserver-features.smk.reqlimits")

## Region and version availability

Using an SMK is supported in all Regions where RDS Custom for SQL Server is available, for all SQL Server versions available on RDS Custom.
For more information on version and Region availability of Amazon RDS with RDS Custom for SQL Server, see
[Supported
Regions and DB engines for RDS Custom for SQL Server](Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.sq "Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.sq").

## Supported features

When using a SMK with RDS Custom for SQL Server, the following features are supported:

- Transparent Data Encryption (TDE)
- Column-level encryption
- Database Mail
- Linked Servers
- SQL Server Integration Services (SSIS)

## Using TDE

An SMK enables the ability to configure Transparent Data Encryption (TDE), which encrypts data before it is written to storage, and automatically decrypts data when the data is read from storage.
Unlike RDS for SQL Server, configuring TDE on an RDS Custom for SQL Server DB instance doesn't require using option groups. Instead, once you've created a certificate and database encryption key, you can run the following command
to turn on TDE at the database level:

```
ALTER DATABASE [myDatabase] SET ENCRYPTION ON;
```

For more information on using TDE with RDS for SQL Server, see [Support for Transparent Data Encryption in SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").

For detailed information on TDE in Microsoft SQL Server, see
[Transparent data encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver15 "https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver15") in the Microsoft documentation.

## Configuring features

For detailed steps on configuring features that use a SMK with RDS Custom for SQL Server, you can use the following posts in the Amazon RDS database blog:

- Linked servers: [Configuring linked servers on RDS Custom for SQL Server](https://aws.amazon.com/blogs/database/configure-linked-servers-on-amazon-rds-custom-for-sql-server/ "https://aws.amazon.com/blogs/database/configure-linked-servers-on-amazon-rds-custom-for-sql-server/").
- SSIS: [Migrate SSIS packages to RDS Custom for SQL Server](https://aws.amazon.com/blogs/database/migrate-microsoft-sql-server-ssis-packages-to-amazon-rds-custom-for-sql-server/ "https://aws.amazon.com/blogs/database/migrate-microsoft-sql-server-ssis-packages-to-amazon-rds-custom-for-sql-server/").
- TDE: [Secure your data using TDE on RDS Custom for SQL Server](https://aws.amazon.com/blogs/database/secure-your-data-at-rest-on-amazon-rds-custom-for-sql-server-using-transparent-data-encryption-tde-or-column-level-encryption-cle/ "https://aws.amazon.com/blogs/database/secure-your-data-at-rest-on-amazon-rds-custom-for-sql-server-using-transparent-data-encryption-tde-or-column-level-encryption-cle/").

## Requirements and limitations

When using an SMK with an RDS Custom for SQL Server DB instance, keep in mind the following requirements and limitations:

- If you re-generate the SMK on your DB instance, you should immediately perform a manual DB snapshot. We recommend avoiding re-generating the SMK if possible.
- You must maintain backups of the server certificates and database master key passwords. If you don't maintain backups of these, it may result in data loss.
- If you configure SSIS, you should use an SSM document to join the RDS Custom for SQL Server DB instance to the domain in case of a scale compute or host replacement.
- When TDE or column-encryption is enabled, database backups are automatically encrypted. When you perform a snapshot restore or point in time recovery, the SMK from the
  source DB instance will be restored to decrypt data for the restore, and a new SMK will be generated to re-encrypt data on the restored instance.

For more information on Service Master Keys in Microsoft SQL Server, see
[SQL Server and Database Encryption Keys](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-and-database-encryption-keys-database-engine?view=sql-server-ver15 "https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-and-database-encryption-keys-database-engine?view=sql-server-ver15") in the Microsoft documentation.
