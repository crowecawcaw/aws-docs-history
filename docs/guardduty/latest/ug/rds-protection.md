# GuardDuty RDS Protection

RDS Protection in Amazon GuardDuty analyzes and profiles RDS login activity for potential access threats to your
[Amazon Aurora
databases](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md") (Amazon Aurora MySQL-Compatible Edition and Aurora PostgreSQL-Compatible Edition) and
[Amazon RDS for PostgreSQL](../../../AmazonRDS/latest/UserGuide/Welcome.md "../../../AmazonRDS/latest/UserGuide/Welcome.md").

RDS Protection helps you identify potentially suspicious login behavior on
these supported databases. GuardDuty continuously monitors and
profiles [RDS login activity](#guardduty-rds-login-events "#guardduty-rds-login-events") for anomalous activity. For example, a previously unseen external actor
has unauthorized access to your database, or adversary attempts brute-force access by guessing
the database's password.

With the launch of [Amazon Aurora PostgreSQL Limitless Database](../../../AmazonRDS/latest/AuroraUserGuide/limitless.md "../../../AmazonRDS/latest/AuroraUserGuide/limitless.md"), GuardDuty expands RDS Protection to now also support monitoring
login activity from Limitless Databases. For AWS accounts that have already enabled
RDS Protection, GuardDuty will automatically start monitoring login data from their Limitless Databases.
For accounts that have not yet enabled RDS Protection, you can learn more about the
[30-day free trial](#gdu-rds-protection-30-day-free-trial "#gdu-rds-protection-30-day-free-trial") and choose
to enable this feature. To enable this feature, see [Enabling RDS Protection in multiple-account
environments](configure-rds-pro-multi-account.md "configure-rds-pro-multi-account.md") or
[Enabling RDS Protection for a standalone
account](configure-rds-pro-standalone.md "configure-rds-pro-standalone.md").

###### Note

RDS for PostgreSQL read replica instances require the primary database instance
to be on a supported database version, and to be successfully replicated from
primary database. For information about read replicas, see [Working with DB instance read replicas](../../../AmazonRDS/latest/UserGuide/USER_ReadRepl.md "../../../AmazonRDS/latest/UserGuide/USER_ReadRepl.md")
in _Amazon RDS User Guide_.

RDS Protection doesn't require additional infrastructure; it is designed so as not to affect the
performance of your database instances. When RDS Protection detects a potentially suspicious or
m anomalous login attempt, GuardDuty generates one or more [RDS Protection finding types](findings-rds-protection.md "findings-rds-protection.md") with details about the potentially compromised
database.

**30-day free trial**

- When you enable GuardDuty in an AWS account in a new Region for the first time, you
  get a 30-day free trial. In this case, GuardDuty will also enable RDS Protection, which is
  included in the free trial. RDS Protection will start monitoring the login behavior of your database.
- When you are already using GuardDuty and decide to enable RDS Protection in a new Region
  for the first time, your account in this Region will get a 30-day free trial for RDS Protection.
- If you have already enabled RDS Protection, then with the launch of
  [Amazon Aurora PostgreSQL Limitless Database](../../../AmazonRDS/latest/AuroraUserGuide/limitless.md "../../../AmazonRDS/latest/AuroraUserGuide/limitless.md"), GuardDuty will automatically start monitoring
  login activity for the Limitless Databases. If your RDS Protection 30-day free trial has expired already,
  then you will start incurring usage costs related to monitoring of Limitless Databases.
- You can choose to disable RDS Protection in any Region at any time.
- During the 30-day free trial, you can get an estimate of your usage costs in that
  account and Region. After the 30-day free trial ends, RDS Protection doesn't get
  disabled automatically. Your account in this Region will start incurring usage cost.
  For more information, see [Estimating GuardDuty usage cost](monitoring_costs.md "monitoring_costs.md").

When the RDS Protection feature is not enabled, GuardDuty does't detect anomalous or suspicious
login behavior. If you disable RDS Protection, GuardDuty immediately stops
monitoring RDS login activity, and will not detect any potential threat to your supported database
instances or generate associated finding types.

For AWS Regions where Aurora PostgreSQL Limitless Databases are supported, see
[Requirements for Aurora PostgreSQL Limitless Database](../../../AmazonRDS/latest/AuroraUserGuide/limitless-reqs-limits.md#limitless-requirements "../../../AmazonRDS/latest/AuroraUserGuide/limitless-reqs-limits.md#limitless-requirements").

## Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases

The following table shows the supported Aurora and Amazon RDS database versions for
RDS Protection.

| Amazon Aurora and Amazon RDS DB engine      | Supported engine versions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Aurora MySQL                                | <br>• 2.10.2 or later <br>• 3.02.1 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Aurora PostgreSQL                           | <br>• 10.23 or later <br>• 11.12 or later <br>• 12.7 or later <br>• 13.3 or later <br>• 14.3 or later <br>• 15.2 or later <br>• 16.1 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| RDS for PostgreSQL                          | <br>• 11.17 or later <br>• 12.12 or later <br>• 13.8 or later <br>• 14.5 or later <br>• [RDS for PostgreSQL version 15](../../../AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.md#postgresql-version15 "../../../AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.md#postgresql-version15") <br>• [RDS for PostgreSQL version 16](../../../AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.md#postgresql-version16 "../../../AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.md#postgresql-version16") <br>• [RDS for PostgreSQL version 17](../../../AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.md#postgresql-version17 "../../../AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-versions.md#postgresql-version17") |
| Amazon Aurora PostgreSQL Limitless Database | `16.4-limitless`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ## RDS login activity When you enable the RDS Protection feature, GuardDuty automatically starts monitoring RDS login activity for your databases, directly from the Aurora and Amazon RDS services. RDS login activity captures both successful and failed login attempts made to the [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](#rds-pro-supported-db "#rds-pro-supported-db") in your AWS environment. If there is an indication of anomalous login behavior, GuardDuty generates a finding with details about the potentially compromised database. When you enable RDS Protection for the first time or you have a newly created database instance, there is a learning period to baseline normal behavior. For this reason, newly enabled or newly created database instances may not have an associated anomalous login finding for up to two weeks. When RDS Protection detects a potential threat, such as an unusual pattern in a series of successful, failed, or incomplete login attempts, GuardDuty generates one or more [RDS Protection finding types](findings-rds-protection.md "findings-rds-protection.md"). Based on the finding type, it may include details about the anomalous behavior, such as [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly "guardduty_findings-summary.md#rds-pro-login-anomaly"). GuardDuty doesn't manage your [Supported databases](#rds-pro-supported-db "#rds-pro-supported-db") or RDS login activity, or make RDS login activity available to you. |
