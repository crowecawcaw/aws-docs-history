# RDS for Oracle features

Amazon RDS for Oracle supports most of the features and capabilities of Oracle Database. Some features might have limited support or restricted
privileges. Some features are only available in Enterprise Edition, and some require additional licenses. For more information about Oracle
Database features for specific Oracle Database versions, see the _Oracle Database Licensing Information User Manual_ for
the version you're using.

###### Topics

- [New features in RDS for Oracle](#Oracle.Concepts.FeatureSupport.new "#Oracle.Concepts.FeatureSupport.new")
- [Supported features in RDS for Oracle](#Oracle.Concepts.FeatureSupport.supported "#Oracle.Concepts.FeatureSupport.supported")
- [Unsupported features in RDS for Oracle](#Oracle.Concepts.FeatureSupport.unsupported "#Oracle.Concepts.FeatureSupport.unsupported")

## New features in RDS for Oracle

To see new features in RDS for Oracle, search [Document history](WhatsNew.md "WhatsNew.md") for the keyword
`Oracle`.

## Supported features in RDS for Oracle

Amazon RDS for Oracle supports the following Oracle Database features:

###### Note

The following list isn't exhaustive.

- Advanced Compression
- AI Vector Search (Oracle Database 26ai and higher)

For more information, see [AI Vector Search](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/index.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/index.html") in the Oracle Database
documentation.

- Amazon Bedrock Integration (Oracle Database 26ai and higher)

For more information, see [Amazon Bedrock integration for RDS for Oracle](Oracle.BedrockIntegration.md "Oracle.BedrockIntegration.md").

- Oracle APEX

For more information, see [Oracle APEX](Appendix.Oracle.Options.APEX.md "Appendix.Oracle.Options.APEX.md").

- Automatic Memory Management
- Automatic SQL Error Mitigation (Oracle Database 26ai and higher)

For more information, see [SQL\_ERROR\_MITIGATION](https://docs.oracle.com/en/database/oracle/oracle-database/26/refrn/SQL_ERROR_MITIGATION.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/refrn/SQL_ERROR_MITIGATION.html") in the Oracle Database documentation.

- Automatic Undo Management
- Automatic Workload Repository (AWR)

For more information, see [Generating performance reports with Automatic Workload Repository (AWR)](Appendix.Oracle.CommonDBATasks.AWR.md "Appendix.Oracle.CommonDBATasks.AWR.md").

- Active Data Guard with Maximum Performance in the same AWS Region or across AWS Regions (Enterprise Edition only; requires the Oracle Active Data Guard option license)

For more information, see [Working with read replicas for Amazon RDS for Oracle](oracle-read-replicas.md "oracle-read-replicas.md").

- Blockchain tables (Oracle Database 21c and higher)

For more information, see [Managing Blockchain Tables](https://docs.oracle.com/en/database/oracle/oracle-database/21/admin/managing-tables.html#GUID-43470B0C-DE4A-4640-9278-B066901C3926 "https://docs.oracle.com/en/database/oracle/oracle-database/21/admin/managing-tables.html#GUID-43470B0C-DE4A-4640-9278-B066901C3926") in the Oracle Database documentation.

- Continuous Query Notification

For more information, see [Using Continuous Query Notification (CQN)](https://docs.oracle.com/en/database/oracle/oracle-database/19/adfns/cqn.html#GUID-373BAF72-3E63-42FE-8BEA-8A2AEFBF1C35 "https://docs.oracle.com/en/database/oracle/oracle-database/19/adfns/cqn.html#GUID-373BAF72-3E63-42FE-8BEA-8A2AEFBF1C35") in the Oracle documentation.

- Data Masking and Subsetting

For more information, see [Data masking in Amazon RDS for Oracle](https://aws.amazon.com/blogs/database/data-masking-in-amazon-rds-for-oracle/ "https://aws.amazon.com/blogs/database/data-masking-in-amazon-rds-for-oracle/") on the AWS Database Blog.

- Data Redaction
- Database In-Memory (Enterprise Edition only; requires the Oracle Database In-Memory option license)
- Distributed Queries and Transactions
- Edition-Based Redefinition

For more information, see [Setting the default edition for a DB instance](Appendix.Oracle.CommonDBATasks.DefaultEdition.md "Appendix.Oracle.CommonDBATasks.DefaultEdition.md").

- EM Express

For more information, see [Oracle Enterprise Manager](Oracle.Options.OEM.md "Oracle.Options.OEM.md").

- Fine-Grained Auditing
- Flashback Table, Flashback Query, Flashback Transaction Query
- Gradual password rollover for applications (Oracle Database 21c and higher)

For more information, see [Managing Gradual Database Password Rollover for Applications](https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/configuring-authentication.html#GUID-ACBA8DAE-C5B4-4811-A31D-53B97C50249B "https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/configuring-authentication.html#GUID-ACBA8DAE-C5B4-4811-A31D-53B97C50249B") in the Oracle Database
documentation.

- HugePages

For more information, see [Turning on HugePages for an RDS for Oracle instance](Oracle.Concepts.HugePages.md "Oracle.Concepts.HugePages.md").

- Import/export (legacy and Data Pump) and SQL\*Loader

For more information, see [Importing data into Oracle on Amazon RDS](Oracle.Procedural.Importing.md "Oracle.Procedural.Importing.md").

- Java Virtual Machine (JVM)

For more information, see [Oracle Java virtual machine](oracle-options-java.md "oracle-options-java.md").

- JavaScript (Oracle Database 21c and higher)

For more information, see [DBMS\_MLE](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_mle.html#GUID-3F5B47A5-2C73-4317-ACD7-E93AE8B8E301 "https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_mle.html#GUID-3F5B47A5-2C73-4317-ACD7-E93AE8B8E301") in the Oracle Database documentation.

- JavaScript stored procedures (Oracle Database 26ai and higher)

For more information, see [JavaScript Developer's Guide](https://docs.oracle.com/en/database/oracle/oracle-database/26/mlejs/index.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/mlejs/index.html") in the Oracle Database
documentation.

- JSON Duality Views (Oracle Database 26ai and higher)

For more information, see [JSON-Relational Duality](https://docs.oracle.com/en/database/oracle/oracle-database/26/jsnvu/index.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/jsnvu/index.html") in the Oracle
Database documentation.

- Label Security

For more information, see [Oracle Label Security](Oracle.Options.OLS.md "Oracle.Options.OLS.md").

- Locator

For more information, see [Oracle Locator](Oracle.Options.Locator.md "Oracle.Options.Locator.md").

- Materialized Views
- Multitenant

The Oracle multitenant architecture is supported for all Oracle Database 19c
and higher releases. For more information, see [Working with CDBs in RDS for Oracle](oracle-multitenant.md "oracle-multitenant.md").

- Network encryption

For more information, see [Oracle native network encryption](Appendix.Oracle.Options.NetworkEncryption.md "Appendix.Oracle.Options.NetworkEncryption.md") and [Oracle Secure Sockets Layer](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md").

- Partitioning
- PL/SQL to SQL Transpiler (Oracle Database 26ai and higher)

For more information, see [SQL\_TRANSPILER](https://docs.oracle.com/en/database/oracle/oracle-database/26/refrn/SQL_TRANSPILER.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/refrn/SQL_TRANSPILER.html") in the Oracle Database documentation.

- Property Graph Views (Oracle Database 26ai and higher)

For more information, see [Oracle Property Graph](https://docs.oracle.com/en/database/oracle/property-graph/index.html "https://docs.oracle.com/en/database/oracle/property-graph/index.html") in the Oracle Database documentation.

- Real Application Testing

To use the full capture and replay capabilities, you must use Amazon Elastic File System
(Amazon EFS) to access files generated by Oracle Real Application Testing. For more
information, see [Amazon EFS integration](oracle-efs-integration.md "oracle-efs-integration.md") and the blog post [Use Oracle Real Application Testing features with
Amazon RDS for Oracle](https://aws.amazon.com/blogs/database/use-oracle-real-application-testing-features-with-amazon-rds-for-oracle/ "https://aws.amazon.com/blogs/database/use-oracle-real-application-testing-features-with-amazon-rds-for-oracle/").

- Real-time SQL plan management (Oracle Database 26ai and higher)

For more information, see [Real-time SQL plan management in RDS for Oracle](Oracle.RealTimeSPM.md "Oracle.RealTimeSPM.md").

- Schema Privileges (Oracle Database 26ai and higher)

For more information, see [Managing Schema Privileges](https://docs.oracle.com/en/database/oracle/oracle-database/26/dbseg/configuring-privilege-and-role-authorization.html#GUID-483D04AF-BC5B-4B3D-9D9A-1D2C3CE8F12F "https://docs.oracle.com/en/database/oracle/oracle-database/26/dbseg/configuring-privilege-and-role-authorization.html#GUID-483D04AF-BC5B-4B3D-9D9A-1D2C3CE8F12F") in the Oracle Database documentation.

- Sharding at the application level (but not the Oracle Sharding feature)
- Shrinking Tablespaces (Oracle Database 26ai and higher)

For more information, see [Shrinking tablespaces in RDS for Oracle](Oracle.ShrinkTablespace.md "Oracle.ShrinkTablespace.md").

- Spatial and Graph

For more information, see [Oracle Spatial](Oracle.Options.Spatial.md "Oracle.Options.Spatial.md").

- Star Query Optimization
- Streams and Advanced Queuing
- Summary Management – Materialized View Query Rewrite
- Text. The `FILE` and `URL` data store types are not supported because Amazon RDS for Oracle doesn't provide host file system access or outbound file retrieval.
- Total Recall
- Transparent Data Encryption (TDE)

For more information, see [Oracle Transparent Data Encryption](Appendix.Oracle.Options.AdvSecurity.md "Appendix.Oracle.Options.AdvSecurity.md").

###### Note

After you enable TDE on a DB instance, you can't disable it.

- Unified Auditing, Mixed Mode

For more information, see [Mixed mode auditing](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/introduction-to-auditing.html#GUID-4A3AEFC3-5422-4320-A048-8219EC96EAC1 "https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/introduction-to-auditing.html#GUID-4A3AEFC3-5422-4320-A048-8219EC96EAC1") in the Oracle documentation.

- XML DB (without the XML DB Protocol Server)

For more information, see [Oracle XML DB](Appendix.Oracle.Options.XMLDB.md "Appendix.Oracle.Options.XMLDB.md").

- Virtual Private Database

## Unsupported features in RDS for Oracle

Amazon RDS for Oracle doesn't support the following Oracle Database features:

###### Note

The following list isn't exhaustive.

- Automatic Storage Management (ASM)
- Database Vault
- Flashback Database

###### Note

For alternative solutions, see the AWS Database Blog entry [Alternatives to the Oracle flashback database feature in
Amazon RDS for Oracle](https://aws.amazon.com/blogs/database/alternatives-to-the-oracle-flashback-database-feature-in-amazon-rds-for-oracle/ "https://aws.amazon.com/blogs/database/alternatives-to-the-oracle-flashback-database-feature-in-amazon-rds-for-oracle/").

- FTP and SFTP
- Hybrid partitioned tables
- Messaging Gateway
- Oracle Enterprise Manager Cloud Control Management Repository
- Priority Transactions
- Real Application Clusters (Oracle RAC)
- Real Application Security (RAS)
- SQL Firewall
- True Cache
- Unified Auditing, Pure Mode
- Workspace Manager (WMSYS) schema

###### Warning

In general, Amazon RDS doesn't prevent you from creating schemas for unsupported features. However, if you create schemas for
Oracle features and components that require SYSDBA privileges, you can damage the data dictionary and affect the availability of your
DB instance. Use only supported features and schemas that are available in [Adding options to Oracle DB instances](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md").
