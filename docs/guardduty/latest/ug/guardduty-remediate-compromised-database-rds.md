# Remediating a potentially

compromised database

GuardDuty generates [RDS Protection finding types](findings-rds-protection.md "findings-rds-protection.md") that indicate potentially suspicious and
anomalous login behavior in your [Supported databases](rds-protection.md#rds-pro-supported-db "rds-protection.md#rds-pro-supported-db") after you enable [RDS Protection](rds-protection.md "rds-protection.md"). Using RDS login activity, GuardDuty analyzes and profiles threats
by identifying unusual patterns in login attempts.

###### Note

You can access the full information about a finding type by selecting it from the [GuardDuty active finding types](guardduty_finding-types-active.md#findings-table "guardduty_finding-types-active.md#findings-table").

Follow these recommended steps to remediate a potentially compromised Amazon Aurora database in
your AWS environment.

###### Topics

- [Remediating potentially compromised
  database with successful login events](#gd-compromised-db-successful-attempt "#gd-compromised-db-successful-attempt")
- [Remediating potentially compromised database
  with failed login events](#gd-compromised-db-failed-attempt "#gd-compromised-db-failed-attempt")
- [Remediating potentially compromised
  credentials](#gd-rds-database-compromised-credentials "#gd-rds-database-compromised-credentials")
- [Restrict network access](#gd-rds-database-restrict-network-access "#gd-rds-database-restrict-network-access")

## Remediating potentially compromised

database with successful login events

The following recommended steps can help you remediate a potentially compromised Aurora
database that exhibits unusual behavior related to successful login events.

1. **Identify the affected database and user.**

The generated GuardDuty finding provides the name of the affected database and the
corresponding user details. For more information, see [Finding details](guardduty_findings-summary.md "guardduty_findings-summary.md"). 2. **Confirm whether this behavior is expected or unexpected.**

The following list specifies potential scenarios that may have caused GuardDuty to generate a
finding:

    * A user who logs in to their database after a long time has passed.
    * A user who logs in to their database on an occasional basis, for example, a financial
     analyst who logs in each quarter.
    * A potentially suspicious actor who is involved in a successful login attempt potentially
     compromises the database.

3.  **Begin this step if the behavior is unexpected.**
    1. **Restrict database access**

    Restrict database access for the suspected accounts and the source of this login
    activity. For more information, see [Remediating potentially compromised
    credentials](#gd-rds-database-compromised-credentials "#gd-rds-database-compromised-credentials") and [Restrict network access](#gd-rds-database-restrict-network-access "#gd-rds-database-restrict-network-access"). 2. **Assess the impact and determine what information was
    accessed.**

        * If available, review the audit logs to identify the pieces of information that might
         have been accessed. For more information, see [Monitoring events,
         logs, and streams in an Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_Monitor_Logs_Events.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_Monitor_Logs_Events.md") in the
         *Amazon Aurora User Guide*.
        * Determine if any sensitive or protected information was accessed or modified.

## Remediating potentially compromised database

with failed login events

The following recommended steps can help you remediate a potentially compromised Aurora
database that exhibits unusual behavior related to failed login events.

1. **Identify the affected database and user.**

The generated GuardDuty finding provides the name of the affected database and the
corresponding user details. For more information, see [Finding details](guardduty_findings-summary.md "guardduty_findings-summary.md"). 2. **Identify the source of the failed login attempts.**

The generated GuardDuty finding provides the **IP address** and **ASN
organization** (if it was a public connection) under the **Actor**
section of the finding panel.

An Autonomous System (AS) is a group of one or more IP prefixes (lists of IP addresses
accessible on a network) run by one or more network operators that maintain a single,
clearly-defined routing policy. Network operators need Autonomous System Numbers (ASNs) to
control routing within their networks and to exchange routing information with other internet
service providers (ISPs). 3. **Confirm that this behavior is unexpected.**

Examine if this activity represents an attempt to gain additional unauthorized access to
the database as follows:

    * If the source is internal, examine if an application is misconfigured and attempting a
     connection repeatedly.
    * If this is an external actor, examine whether the corresponding database is public
     facing or is misconfigured and thus allowing potential malicious actors to brute force common
     user names.

4. **Begin this step if the behavior is unexpected.**
   1. **Restrict database access**

   Restrict database access for the suspected accounts and the source of this login
   activity. For more information, see [Remediating potentially compromised
   credentials](#gd-rds-database-compromised-credentials "#gd-rds-database-compromised-credentials") and [Restrict network access](#gd-rds-database-restrict-network-access "#gd-rds-database-restrict-network-access"). 2. **Perform root-cause analysis and determine the steps that
   potentially led to this activity.**

   Set up an alert to get notified when an activity modifies a networking policy and
   creates an insecure state. For more information, see [Firewall policies in
   AWS Network Firewall](../../../network-firewall/latest/developerguide/firewall-policies.md "../../../network-firewall/latest/developerguide/firewall-policies.md") in the _AWS Network Firewall Developer Guide_.

## Remediating potentially compromised

credentials

A GuardDuty finding may indicate that the user credentials for an affected database have been
compromised when the user identified in the finding has performed an unexpected database
operation. You can identify the user in the **RDS DB user details** section
within the finding panel in the console, or within the `resource.rdsDbUserDetails` of
the findings JSON. These user details include user name, application used, database accessed, SSL
version, and authentication method.

- To revoke access or rotate passwords for specific users that are involved in the finding,
  see [Security with Amazon Aurora MySQL](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md"), or [Security with Amazon Aurora PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md") in the
  _Amazon Aurora User Guide_.
- Use AWS Secrets Manager to securely store and automatically rotate the secrets for Amazon Relational Database Service(RDS)
  databases. For more information, see [AWS Secrets Manager tutorials](../../../secretsmanager/latest/userguide/tutorials.md "../../../secretsmanager/latest/userguide/tutorials.md") in the
  _AWS Secrets Manager User Guide_.
- Use IAM database authentication to manage database users' access without the need for
  passwords. For more information, see [IAM database
  authentication](../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.md") in the _Amazon Aurora User Guide_.

For more information, see [Security best practices for
Amazon Relational Database Service](../../../AmazonRDS/latest/UserGuide/CHAP_BestPractices.md "../../../AmazonRDS/latest/UserGuide/CHAP_BestPractices.md") in the _Amazon RDS User Guide_.

## Restrict network access

A GuardDuty finding may indicate that a database is accessible beyond your applications, or
Virtual Private Cloud (VPC). If the remote IP address in the finding is an unexpected connection
source, audit the security groups. A list of security groups attached to the database is
available under **Security groups** in the [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/") console, or in the
`resource.rdsDbInstanceDetails.dbSecurityGroups` of the findings JSON. For more
information on configuring security groups, see [Controlling access with
security groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md") in the _Amazon RDS User Guide_.

If you're using a firewall, restrict network access to the database by reconfiguring the
Network Access Control Lists (NACLs). For more information, see [Firewalls in AWS Network Firewall](../../../network-firewall/latest/developerguide/firewalls.md "../../../network-firewall/latest/developerguide/firewalls.md") in
the _AWS Network Firewall Developer Guide_.
