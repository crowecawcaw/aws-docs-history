# Using Oracle GoldenGate with Amazon RDS for Oracle

Oracle GoldenGate collects, replicates, and manages transactional data between databases. It
is a log-based change data capture (CDC) and replication software package used with
databases for online transaction processing (OLTP) systems. Oracle GoldenGate creates trail
files that contain the most recent changed data from the source database. It then pushes
these files to the server, where a process converts the trail file into standard SQL to be
applied to the target database.

Oracle GoldenGate with RDS for Oracle supports the following features:

- Active-Active database replication
- Disaster recovery
- Data protection
- In-Region and cross-Region replication
- Zero-downtime migration and upgrades
- Data replication between an RDS for Oracle DB instance and a non-Oracle database

###### Note

For a list of supported databases, see [Oracle Fusion Middleware Supported System Configurations](https://www.oracle.com/middleware/technologies/fusion-certification.html "https://www.oracle.com/middleware/technologies/fusion-certification.html") in the
Oracle documentation.
You can use Oracle GoldenGate with RDS for Oracle to upgrade to major versions of Oracle Database. For example,
you can use Oracle GoldenGate to upgrade from an Oracle Database 11g on-premises database to Oracle Database 19c on an Amazon RDS DB instance.

###### Topics

- [Supported versions and licensing options for Oracle GoldenGate](#Appendix.OracleGoldenGate.licensing "#Appendix.OracleGoldenGate.licensing")
- [Requirements and limitations for
  Oracle GoldenGate](#Appendix.OracleGoldenGate.requirements "#Appendix.OracleGoldenGate.requirements")
- [Oracle GoldenGate architecture](Appendix.OracleGoldenGate.md "Appendix.OracleGoldenGate.md")
- [Setting up Oracle GoldenGate](Appendix.OracleGoldenGate.md "Appendix.OracleGoldenGate.md")
- [Working with the EXTRACT and REPLICAT utilities of
  Oracle GoldenGate](Appendix.OracleGoldenGate.md "Appendix.OracleGoldenGate.md")
- [Monitoring Oracle GoldenGate](Appendix.OracleGoldenGate.md "Appendix.OracleGoldenGate.md")
- [Troubleshooting Oracle GoldenGate](Appendix.OracleGoldenGate.md "Appendix.OracleGoldenGate.md")

## Supported versions and licensing options for Oracle GoldenGate

You can use Standard Edition 2 (SE2) or Enterprise Edition (EE) of RDS for Oracle with Oracle GoldenGate version 12c and higher.
You can use the following Oracle GoldenGate features:

- Oracle GoldenGate Remote Capture (extract) is supported.
- Capture (extract) is supported on RDS for Oracle DB instances that use the traditional non-CDB database
  architecture. Oracle GoldenGate Remote PDB capture is supported on CDBs running Oracle Database 21c or
  Oracle Database 19c version 19.0.0.0.ru-2024-04.rur-2024-04.r1 or higher.
- Oracle GoldenGate Remote Delivery (replicat) is supported on RDS for Oracle DB
  instances that use either the non-CDB or CDB architectures. Remote Delivery
  supports Integrated Replicat, Parallel Replicat, Coordinated Replicat, and
  classic Replicat.
- RDS for Oracle supports the Classic and Microservices architectures of Oracle GoldenGate.
- Oracle GoldenGate DDL and Sequence value replication is supported when using Integrated capture
  mode.

You are responsible for managing Oracle GoldenGate licensing (BYOL) for use with Amazon RDS in all
AWS Regions. For more information, see [RDS for Oracle licensing options](Oracle.Concepts.md "Oracle.Concepts.md").

## Requirements and limitations for

Oracle GoldenGate

When you're working with Oracle GoldenGate and RDS for Oracle, consider the following requirements and
limitations:

- You're responsible for setting up and managing Oracle GoldenGate for use with RDS for Oracle.
- You're responsible for setting up an Oracle GoldenGate version that is certified with the
  source and the target databases. For more information, see [Oracle Fusion Middleware Supported System Configurations](https://www.oracle.com/middleware/technologies/fusion-certification.html "https://www.oracle.com/middleware/technologies/fusion-certification.html") in the Oracle
  documentation.
- You can use Oracle GoldenGate on many different AWS environments for many different use
  cases. If you have a support-related issue relating to Oracle GoldenGate, contact Oracle Support
  Services.
- You can use Oracle GoldenGate on RDS for Oracle DB instances that use Oracle Transparent Data Encryption (TDE). To
  maintain the integrity of replicated data, configure encryption on the Oracle GoldenGate hub
  using Amazon EBS encrypted volumes or trail file encryption. Also configure encryption
  for data sent between the Oracle GoldenGate hub and the source and target database instances.
  RDS for Oracle DB instances support encryption with [Oracle Secure Sockets Layer](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md") or [Oracle native network encryption](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md").
