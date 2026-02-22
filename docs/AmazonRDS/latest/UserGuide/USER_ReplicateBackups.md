# Replicating automated backups to another AWS Region

For added disaster recovery capability, you can configure your Amazon RDS database instance to
replicate snapshots and transaction logs to a destination AWS Region of your choice. When
backup replication is configured for a DB instance, RDS initiates a cross-Region copy of all
snapshots and transaction logs as soon as they are ready on the DB instance.

DB snapshot copy charges apply to the data transfer. After the DB snapshot is copied, standard charges apply to storage in the
destination Region. For more details, see [RDS Pricing](https://aws.amazon.com/rds/oracle/pricing/ "https://aws.amazon.com/rds/oracle/pricing/").

For an example of using backup replication, see the AWS online tech talk [Managed Disaster Recovery with Amazon RDS for Oracle Cross-Region Automated Backups](https://pages.awscloud.com/Managed-Disaster-Recovery-with-Amazon-RDS-for-Oracle-Cross-Region-Automated-Backups_2021_0908-DAT_OD.html "https://pages.awscloud.com/Managed-Disaster-Recovery-with-Amazon-RDS-for-Oracle-Cross-Region-Automated-Backups_2021_0908-DAT_OD.html").

###### Note

Automated backup replication isn't supported for Multi-AZ DB clusters. However, it is supported for
Multi-AZ DB instance deployments. For more information about limitations for automated
backups, see [Quotas and constraints for Amazon RDS](CHAP_Limits.md "CHAP_Limits.md").

For information about configuring and managing automated backups for Amazon RDS, see the following topics.

###### Topics

- [Enabling cross-Region automated backups for Amazon RDS](AutomatedBackups.Replicating.md "AutomatedBackups.Replicating.md")
- [Finding information about replicated backups for Amazon RDS](AutomatedBackups.Replicating.md "AutomatedBackups.Replicating.md")
- [Restoring to a specified time from a replicated backup for Amazon RDS](AutomatedBackups.md "AutomatedBackups.md")
- [Stopping automated backup replication for Amazon RDS](AutomatedBackups.md "AutomatedBackups.md")
- [Deleting replicated backups for Amazon RDS](AutomatedBackups.md "AutomatedBackups.md")
- [Troubleshooting stopped cross-Region automated backups](AutomatedXREGBackups.md "AutomatedXREGBackups.md")

## Multi-AZ deployment support

Cross-Region automated backup replication is supported for Multi-AZ DB instance
deployments for the following engines:

- RDS for Db2
- RDS for MariaDB
- RDS for MySQL
- RDS for Oracle
- RDS for PostgreSQL
- RDS for SQL Server

Cross-Region automated backup replication isn't supported for Multi-AZ DB clusters.

## Region and version availability

Feature availability and support varies across specific versions of each database engine, and across AWS Regions.
For more information on version and Region availability with cross-Region automated backups, see
[Supported
Regions and DB engines for cross-Region automated backups in
Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").

## Source and destination AWS Region support

Backup replication is supported between the following AWS Regions.

| Source Region             | Destination Regions available                                                                                                                                                                                                                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Africa (Cape Town)        | Europe (Frankfurt), Europe (Ireland), Europe (London)                                                                                                                                                                                                                                                                               |
| Asia Pacific (Hong Kong)  | Asia Pacific (Singapore), Asia Pacific (Tokyo)                                                                                                                                                                                                                                                                                      |
| Asia Pacific (Hyderabad)  | Asia Pacific (Mumbai)                                                                                                                                                                                                                                                                                                               |
| Asia Pacific (Melbourne)  | Asia Pacific (Sydney)                                                                                                                                                                                                                                                                                                               |
| Asia Pacific (Malaysia)   | Asia Pacific (Singapore)                                                                                                                                                                                                                                                                                                            |
| Asia Pacific (Mumbai)     | Asia Pacific (Hyderabad), Asia Pacific (Singapore)<br>US East (N. Virginia), US East (Ohio), US West (Oregon)                                                                                                                                                                                                                       |
| Asia Pacific (Osaka)      | Asia Pacific (Tokyo)                                                                                                                                                                                                                                                                                                                |
| Asia Pacific (Seoul)      | Asia Pacific (Singapore), Asia Pacific (Tokyo)<br>US East (N. Virginia), US East (Ohio), US West (Oregon)                                                                                                                                                                                                                           |
| Asia Pacific (Singapore)  | Asia Pacific (Hong Kong), Asia Pacific (Malaysia), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Sydney), Asia Pacific (Tokyo)<br>US East (N. Virginia), US East (Ohio), US West (Oregon)                                                                                                                              |
| Asia Pacific (Sydney)     | Asia Pacific (Melbourne), Asia Pacific (Singapore)<br>US East (N. Virginia), US West (N. California), US West (Oregon)                                                                                                                                                                                                              |
| Asia Pacific (Tokyo)      | Asia Pacific (Hong Kong), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore)<br>US East (N. Virginia), US East (Ohio), US West (Oregon)                                                                                                                                                                           |
| Canada (Central)          | Canada West (Calgary)<br>Europe (Ireland)<br>US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon)                                                                                                                                                                                                       |
| Canada West (Calgary)     | Canada (Central)                                                                                                                                                                                                                                                                                                                    |
| China (Beijing)           | China (Ningxia)                                                                                                                                                                                                                                                                                                                     |
| China (Ningxia)           | China (Beijing)                                                                                                                                                                                                                                                                                                                     |
| Europe (Frankfurt)        | Africa (Cape Town)<br>Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), Europe (Zurich)<br>US East (N. Virginia), US East (Ohio), US West (Oregon)                                                                                                                                                             |
| Europe (Ireland)          | Africa (Cape Town)<br>Canada (Central)<br>Europe (Frankfurt), Europe (London), Europe (Paris), Europe (Stockholm), Europe (Zurich)<br>US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon)                                                                                                              |
| Europe (London)           | Africa (Cape Town)<br>Europe (Frankfurt), Europe (Ireland), Europe (Paris), Europe (Stockholm)<br>US East (N. Virginia)                                                                                                                                                                                                             |
| Europe (Paris)            | Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Stockholm)<br>US East (N. Virginia)                                                                                                                                                                                                                                  |
| Europe (Stockholm)        | Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris)<br>US East (N. Virginia)                                                                                                                                                                                                                                      |
| Europe (Zurich)           | Europe (Frankfurt), Europe (Ireland)                                                                                                                                                                                                                                                                                                |
| South America (São Paulo) | US East (N. Virginia), US East (Ohio)                                                                                                                                                                                                                                                                                               |
| AWS GovCloud (US-East)    | AWS GovCloud (US-West)                                                                                                                                                                                                                                                                                                              |
| AWS GovCloud (US-West)    | AWS GovCloud (US-East)                                                                                                                                                                                                                                                                                                              |
| US East (N. Virginia)     | Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Tokyo)<br>Canada (Central)<br>Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris),<br>Europe (Stockholm)<br>South America (São Paulo)<br>US East (Ohio), US West (N. California), US West (Oregon) |
| US East (Ohio)            | Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Tokyo)<br>Canada (Central)<br>Europe (Frankfurt), Europe (Ireland)<br>South America (São Paulo)<br>US East (N. Virginia), US West (N. California), US West (Oregon)                                                                            |
| US West (N. California)   | Asia Pacific (Sydney)<br>Canada (Central)<br>Europe (Ireland)<br>US East (N. Virginia), US East (Ohio), US West (Oregon)                                                                                                                                                                                                            |
| US West (Oregon)          | Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney),<br>Asia Pacific (Tokyo)<br>Canada (Central)<br>Europe (Frankfurt), Europe (Ireland)<br>US East (N. Virginia), US East (Ohio), US West (N. California)                                                                                 |

You can also use the `describe-source-regions` AWS CLI command to find out which AWS Regions can replicate to each
other. For more information, see [Finding information about replicated backups for Amazon RDS](AutomatedBackups.Replicating.md "AutomatedBackups.Replicating.md").

## Limitations

Following are limitations for cross–Region automated backups for Amazon RDS.

- Automated backup replication isn't supported for Multi-AZ DB clusters.
- By default, you can have up to 20 cross–Region automated backups per AWS account.
