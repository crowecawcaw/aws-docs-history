

# GuardDuty RDS Protection
<a name="rds-protection"></a>

**Note**  
You can configure RDS Protection along with all other protection plans from a single page in the GuardDuty console. For more information, see [Configuring protection plans](protection-plans.md).

RDS Protection in Amazon GuardDuty analyzes and profiles RDS login and data activity for potential threats to your Amazon Aurora and RDS for PostgreSQL databases.

RDS Protection for login activity analyzes login events for potential access threats to [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) (Amazon Aurora MySQL-Compatible Edition and Aurora PostgreSQL-Compatible Edition), [RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html), [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html), and [Amazon RDS for MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html) databases. It helps you identify potentially suspicious login behavior on these supported databases. GuardDuty continuously monitors and profiles [RDS login activity](#guardduty-rds-login-events) for anomalous activity. For example, a previously unseen external actor has unauthorized access to your database, or adversary attempts brute-force access by guessing the database's password.

RDS Protection for data activity analyzes database query patterns on [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) for PostgreSQL and [RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) databases to detect potential data access and manipulation threats. GuardDuty continuously monitors and profiles [RDS data activity](#guardduty-rds-database-events) for anomalous behavior. For example, an actor reading significantly more rows than normal for that database or user, deleting or dropping data, or accessing your database from a known malicious or Tor IP address.

For accounts that have not yet enabled RDS Protection, you can learn more about the [30-day free trial](#gdu-rds-protection-30-day-free-trial) and choose to enable this feature. To enable this feature, see [Enabling RDS Protection in multiple-account environments](configure-rds-pro-multi-account.md) or [Enabling RDS Protection for a standalone account](configure-rds-pro-standalone.md).

**Note**  
RDS for PostgreSQL read replica instances require the primary database instance to be on a supported database version, and to be successfully replicated from the primary database. For information about read replicas, see [Working with DB instance read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) in *Amazon RDS User Guide*.

RDS Protection doesn't require additional infrastructure; it is designed so as not to affect the performance of your database instances. When RDS Protection detects a potentially suspicious or anomalous login attempt, exfiltration, or data-destructive activity, GuardDuty generates one or more [RDS Protection finding types](findings-rds-protection.md) with details about the potentially compromised database.

**30-day free trial**  
+ When you enable GuardDuty in an AWS account in a new Region for the first time, you receive a 30-day free trial. In this case, GuardDuty also enables RDS Protection, which is included in the free trial. RDS Protection login activity monitoring and RDS Protection data activity monitoring will begin monitoring the activity of your databases.
+ When you are already using GuardDuty and decide to enable RDS Protection in a new Region for the first time, your account in this Region will get a 30-day free trial for RDS Protection.
+ When you are already using RDS Protection for login activity in an AWS account and decide to enable RDS Protection for data activity for the first time, your account will get a 30-day free trial for RDS Protection for data activity.
+ You can choose to disable RDS Protection or RDS Protection data activity monitoring in any Region at any time.
+ During the 30-day free trial, you can get an estimate of your usage costs in that account and Region. After the 30-day free trial ends, RDS Protection doesn't get disabled automatically. Your account in this Region will start incurring usage cost. For more information, see [Monitoring GuardDuty Usage and Estimating Costs](monitoring_costs.md).

When the RDS Protection feature is not enabled, GuardDuty doesn't detect anomalous or suspicious login or data behavior. If you disable RDS Protection, GuardDuty immediately stops monitoring RDS activity and will not detect any potential threat to your supported database instances or generate associated finding types.

For AWS Regions where Aurora PostgreSQL Limitless Databases are supported, see [Requirements for Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reqs-limits.html#limitless-requirements).

## Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases
<a name="rds-pro-supported-db"></a>

The following table shows the supported Aurora and Amazon RDS database versions for RDS Protection *login activity monitoring* and *data activity monitoring*. GuardDuty may expand to additional Amazon RDS databases in the future.


| Amazon Aurora and Amazon RDS DB engine | Login activity monitoring supported engine versions | Data activity monitoring supported engine versions | 
| --- | --- | --- | 
| Aurora MySQL |  +  2.10.2 or later <br />+  3.02.1 or later <br />+  Subsequent major versions   | Not supported | 
| Aurora PostgreSQL |  +  10.23 or later <br />+  11.12 or later <br />+  12.7 or later <br />+  13.3 or later <br />+  14.3 or later <br />+  15.2 or later <br />+  16.1 or later <br />+  Subsequent major versions   |  +  11.19 or later <br />+  12.14 or later <br />+  13.10 or later <br />+  14.7 or later <br />+  15.2 or later <br />+  Subsequent major versions   | 
| RDS for PostgreSQL | +  11.17 or later <br />+  12.12 or later <br />+  13.8 or later <br />+  14.5 or later <br />+  [RDS for PostgreSQL version 15](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.html#postgresql-version15) <br />+  [RDS for PostgreSQL version 16](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.html#postgresql-version16) <br />+  [RDS for PostgreSQL version 17](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.html#postgresql-version17) <br />+  [RDS for PostgreSQL version 18](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.html#postgresql-version18) <br />+  Subsequent major versions  |  +  11.20 or later <br />+  12.15 or later <br />+  13.11 or later <br />+  14.8 or later <br />+  15.3 or later <br />+  Subsequent major versions   | 
| Amazon Aurora PostgreSQL Limitless Database |  +  `16.4-limitless` <br />+  Subsequent major versions   | Not supported | 
| Amazon RDS for MariaDB |  +  10.6.25 or later <br />+  10.11.16 or later <br />+  11.4.10 or later <br />+  11.8.6 or later <br />+  Subsequent major versions   | Not supported | 
| Amazon RDS for MySQL |  +  8.0.45 or later <br />+  8.4.8 or later <br />+  Subsequent major versions   | Not supported | 

## RDS login activity
<a name="guardduty-rds-login-events"></a>

When you enable the RDS Protection feature, GuardDuty automatically starts monitoring RDS login activity for your databases, directly from the Aurora and Amazon RDS services. RDS login activity captures both successful and failed login attempts made to the [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](#rds-pro-supported-db) in your AWS environment. If there is an indication of anomalous login behavior, GuardDuty generates a finding with details about the potentially compromised database. When you enable RDS Protection for the first time or you have a newly created database instance, there is a learning period to baseline normal behavior. For this reason, newly enabled or newly created database instances may not have an associated anomalous login finding for up to two weeks. 

When RDS Protection detects a potential threat, such as an unusual pattern in a series of successful, failed, or incomplete login attempts, GuardDuty generates one or more [RDS Protection finding types](findings-rds-protection.md). Based on the finding type, it may include details about the anomalous behavior, such as [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly). GuardDuty doesn't make RDS login activity logs available to you.

## RDS data activity
<a name="guardduty-rds-database-events"></a>

When you enable RDS Protection for data activity, GuardDuty analyzes database activity patterns in supported Aurora and Amazon RDS databases to identify potential data access and manipulation threats. If it detects an anomalous data activity, GuardDuty generates a finding with details about the potentially compromised database. When you enable RDS Protection for data activity for the first time, or when you create a new database instance, there is a learning period of up to two weeks to establish a baseline of normal behavior. During this time you may not have an associated anomalous data activity finding.

When RDS Protection for data activity detects a potential threat, GuardDuty generates one or more [RDS Protection finding types](findings-rds-protection.md). Examples include an actor reading significantly more rows than is normal for that database or user, deleting or dropping data, or accessing your database from a known malicious or Tor IP address. Depending on the finding type, the finding may include details about the anomalous behavior, such as [RDS data activity-based anomalies](guardduty_findings-summary.md#rds-pro-data-activity-anomaly). GuardDuty doesn't make RDS data activity logs available to you.