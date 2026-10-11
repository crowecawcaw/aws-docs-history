

# GuardDuty RDS Protection finding types
<a name="findings-rds-protection"></a>

GuardDuty RDS Protection detects anomalous login behavior on your database instance. The following findings are specific to the [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db) and will have a **Resource Type** of `RDSDBInstance` or `RDSLimitlessDB`. The severity and details of the findings will differ based on the finding type.

**Topics**
+ [CredentialAccess:RDS/AnomalousBehavior.SuccessfulLogin](#credaccess-rds-anombehavior-successlogin)
+ [CredentialAccess:RDS/AnomalousBehavior.FailedLogin](#credaccess-rds-anombehavior-failedlogin)
+ [CredentialAccess:RDS/AnomalousBehavior.SuccessfulBruteForce](#credaccess-rds-anombehavior-successfulbruteforce)
+ [CredentialAccess:RDS/MaliciousIPCaller.SuccessfulLogin](#credaccess-rds-maliciousipcaller-successfullogin)
+ [CredentialAccess:RDS/MaliciousIPCaller.FailedLogin](#credaccess-rds-maliciousipcaller-failedlogin)
+ [Discovery:RDS/MaliciousIPCaller](#discovery-rds-maliciousipcaller)
+ [CredentialAccess:RDS/TorIPCaller.SuccessfulLogin](#credaccess-rds-toripcaller-successfullogin)
+ [CredentialAccess:RDS/TorIPCaller.FailedLogin](#credaccess-rds-toripcaller-failedlogin)
+ [Discovery:RDS/TorIPCaller](#discovery-rds-toripcaller)
+ [Exfiltration:RDS/AnomalousBehavior](#exfiltration-rds-anomalousbehavior)
+ [Impact:RDS/AnomalousBehavior.Drop](#impact-rds-anomalousbehavior-drop)
+ [Impact:RDS/AnomalousBehavior.Delete](#impact-rds-anomalousbehavior-delete)
+ [Exfiltration:RDS/MaliciousIPCaller](#exfiltration-rds-maliciousipcaller)
+ [Exfiltration:RDS/TorIPCaller](#exfiltration-rds-toripcaller)
+ [Impact:RDS/MaliciousIPCaller](#impact-rds-maliciousipcaller)
+ [Impact:RDS/TorIPCaller](#impact-rds-toripcaller)

## CredentialAccess:RDS/AnomalousBehavior.SuccessfulLogin
<a name="credaccess-rds-anombehavior-successlogin"></a>

### A user successfully logged into an RDS database in your account in an anomalous way.
<a name="credaccess-rds-anombehavior-successlogin_description"></a>

**Default severity: Variable**

**Note**  
Depending on the anomalous behavior associated with this finding, the default severity can Low, Medium, and High.   
**Low** – If the user name associated with this finding logged in from an IP address that is associated with a private network.
**Medium** – If the user name associated with this finding logged in from a public IP address.
**High** – If there is a consistent pattern of failed login attempts from public IP addresses indicative of overly permissive access policies.
+ **Feature: **RDS login activity monitoring

This finding informs you that an anomalous successful login was observed on an RDS database in your AWS environment. This may indicate that a previous unseen user logged into an RDS database for the first time. A common scenario is an internal user logging into a database that is accessed programmatically by applications and not by individual users. 

This successful login was identified as anomalous by the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates all database login events in your [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db) and identifies anomalous events that are associated with techniques used by adversaries. The ML model tracks various factors of the RDS login activity such as the user that made the request, the location the request was made from, and the specific database connection details that were used. For information about the login events that are potentially unusual, see [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly).

**Remediation recommendations:**

If this activity is unexpected for the associated database, it is recommended to change the password of the associated database user, and review available audit logs for activity performed by the anomalous user. Medium and high severity findings may indicate that there is an overly permissive access policy to the database, and user credentials may have been exposed or compromised. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with successful login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt).

## CredentialAccess:RDS/AnomalousBehavior.FailedLogin
<a name="credaccess-rds-anombehavior-failedlogin"></a>

### One or more unusual failed login attempts were observed on an RDS database in your account.
<a name="credaccess-rds-anombehavior-failedlogin_description"></a>

**Default severity: Low**
+ **Feature: **RDS login activity monitoring

This finding informs you that one or more anomalous failed logins were observed on an RDS database in your AWS environment. A failed login attempts from public IP addresses may indicate that the RDS database in your account has been subject to an attempted brute force attack by a potentially malicious actor.

These failed logins were identified as anomalous by the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates all database login events in your [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db) and identifies anomalous events that are associated with techniques used by adversaries. The ML model tracks various factors of the RDS login activity such as the user that made the request, the location the request was made from, and the specific database connection details that were used. For information about the RDS login activity that are potentially unusual, see [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly).

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the database is publicly exposed or there is an overly permissive access policy to the database. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt).

## CredentialAccess:RDS/AnomalousBehavior.SuccessfulBruteForce
<a name="credaccess-rds-anombehavior-successfulbruteforce"></a>

### A user successfully logged into an RDS database in your account from a public IP address in an anomalous way after a consistent pattern of unusual failed login attempts.
<a name="credaccess-rds-anombehavior-successfulbruteforce_description"></a>

**Default severity: High**
+ **Feature: **RDS login activity monitoring

This finding informs you that an anomalous login indicative of a successful brute force was observed on an RDS database in your AWS environment. Prior to an anomalous successful login, a consistent pattern of unusual failed login attempts was observed. This indicates that the user and password associated with the RDS database in your account may have been compromised, and the RDS database may have been accessed by a potentially malicious actor.

This successful brute force login was identified as anomalous by the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates all database login events in your [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db) and identifies anomalous events that are associated with techniques used by adversaries. The ML model tracks various factors of the RDS login activity such as the user that made the request, the location the request was made from, and the specific database connection details that were used. For information about the RDS login activity that are potentially unusual, see [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly).

**Remediation recommendations:**

This activity indicates that database credentials may have been exposed or compromised. It is recommended to change the password of the associated database user, and review available audit logs for activity performed by the potentially compromised user. A consistent pattern of unusual failed login attempts indicate an overly permissive access policy to the database or the database may have also been public exposed. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with successful login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt).

## CredentialAccess:RDS/MaliciousIPCaller.SuccessfulLogin
<a name="credaccess-rds-maliciousipcaller-successfullogin"></a>

### A user successfully logged into an RDS database in your account from a known malicious IP address.
<a name="credaccess-rds-maliciousipcaller-successfullogin_description"></a>

**Default severity: High**
+ **Feature: **RDS login activity monitoring

This finding informs you that a successful RDS login activity occurred from an IP address that is associated with a known malicious activity in your AWS environment. This indicates that the user and password associated with the RDS database in your account may have been compromised, and the RDS database may have been accessed by a potentially malicious actor.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the user credentials may have been exposed or compromised. It is recommended to change the password of the associated database user, and review the available audit logs for activity performed by the compromised user. This activity may also indicate that there is an overly permissive access policy to the database or the database is publicly exposed. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with successful login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt).

## CredentialAccess:RDS/MaliciousIPCaller.FailedLogin
<a name="credaccess-rds-maliciousipcaller-failedlogin"></a>

### An IP address that is associated with a known malicious activity unsuccessfully attempted to log in to an RDS database in your account.
<a name="credaccess-rds-maliciousipcaller-failedlogin_description"></a>

**Default severity: Medium**
+ **Feature: **RDS login activity monitoring

This finding informs you that an IP address associated with known malicious activity attempted to log in to an RDS database in your AWS environment, but failed to provide the correct user name or password. This indicates that a potentially malicious actor may be attempting to compromise the RDS database in your account.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that there is an overly permissive access policy to the database or the database is publicly exposed. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt).

## Discovery:RDS/MaliciousIPCaller
<a name="discovery-rds-maliciousipcaller"></a>

### An IP address that is associated with a known malicious activity probed an RDS database in your account; no authentication attempt was made.
<a name="discovery-rds-maliciousipcaller_description"></a>

**Default severity: Medium**
+ **Feature: **RDS login activity monitoring

This finding informs you that an IP address associated with known a malicious activity probed an RDS database in your AWS environment, though no login attempt was made. This may indicate that a potentially malicious actor is attempting to scan for a publicly accessible infrastructure.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that there is an overly permissive access policy to the database or the database is publicly exposed. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt).

## CredentialAccess:RDS/TorIPCaller.SuccessfulLogin
<a name="credaccess-rds-toripcaller-successfullogin"></a>

### A user successfully logged into an RDS database in your account from a Tor exit node IP address.
<a name="credaccess-rds-toripcaller-successfullogin_description"></a>

**Default severity: High**
+ **Feature: **RDS login activity monitoring

This finding informs you that a user successfully logged in to an RDS database in your AWS environment, from a Tor exit node IP address. Tor is a software for enabling anonymous communication. It encrypts and randomly bounces communications through relays between a series of network nodes. The last Tor node is called the exit node. This can indicate unauthorized access to the RDS resources in your account, with the intent of hiding the anonymous user's true identity.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the user credentials may have been exposed or compromised. It is recommended to change the password of the associated database user, and review the available audit logs for activity performed by the compromised user. This activity may also indicate that there is an overly permissive access policy to the database or the database is publicly exposed. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with successful login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt).

## CredentialAccess:RDS/TorIPCaller.FailedLogin
<a name="credaccess-rds-toripcaller-failedlogin"></a>

### A Tor IP address attempted to unsuccessfully log in to an RDS database in your account.
<a name="credaccess-rds-toripcaller-failedlogin_description"></a>

**Default severity: Medium**
+ **Feature: **RDS login activity monitoring

This finding informs you that a Tor exit node IP address attempted to log in to an RDS database in your AWS environment, but failed to provide the correct user name or password. Tor is a software for enabling anonymous communication. It encrypts and randomly bounces communications through relays between a series of network nodes. The last Tor node is called the exit node. This can indicate unauthorized access to the RDS resources in your account, with the intent of hiding the anonymous user's true identity.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that there is an overly permissive access policy to the database or the database is publicly exposed. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt).

## Discovery:RDS/TorIPCaller
<a name="discovery-rds-toripcaller"></a>

### A Tor exit node IP address probed an RDS database in your account, no authentication attempt was made.
<a name="discovery-rds-toripcaller_description"></a>

**Default severity: Medium**
+ **Feature: **RDS login activity monitoring

This finding informs you that a Tor exit node IP address probed an RDS database in your AWS environment, though no login attempt was made. This may indicate that a potentially malicious actor is attempting to scan for publicly accessible infrastructure. Tor is a software for enabling anonymous communication. It encrypts and randmonly bounces communications through relays between a series of network nodes. The last Tor node is called the exit node. This can indicate unauthorized access to the RDS resources in your account, with the intent of hiding the potentially malicious actor's true identity.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that there is an overly permissive access policy to the database or the database is publicly exposed. It is recommended to place the database in a private VPC, and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt).

## Exfiltration:RDS/AnomalousBehavior
<a name="exfiltration-rds-anomalousbehavior"></a>

### Anomalous activity from a user extracting large volume of data from an RDS database in your account.
<a name="exfiltration-rds-anomalousbehavior_description"></a>

**Default severity: Low**

**Note**  
Depending on the anomalous behavior associated with this finding, the default severity can be Low, Medium, or High.  
**Low** – If the user name associated with this finding executed `SELECT` statements from an IP address that is associated with a private network.
**Medium** – If the user name associated with this finding executed `SELECT` statements from a public IP address.
**High** – If the user name associated with this finding executed `SELECT` statements returning an unusually large volume of rows, and the activity either originated from a previously unseen public network or was performed by a high-privilege database role or administrative client.
+ **Feature: **RDS DB Activity Monitoring

This finding informs you that anomalous database activity consistent with data exfiltration was observed on an RDS database in your AWS environment. This may indicate that a database user selected a significantly higher number of rows than usual, or that the activity involved a previously unseen database attribute such as a new user, IP address, or database name that contributed to the volume spike. A common scenario is a compromised database credential being used to extract data through a combination of unusual access patterns and elevated query volume.

This activity was identified as anomalous by the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates all database activity events in your [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db) and identifies anomalous events that are associated with techniques used by adversaries. The ML model tracks various factors of the RDS database activity such as the user that made the request, the queries executed, the volume of data accessed, and the specific database connection details that were used. For information about the database activity that is potentially unusual, see [RDS data activity-based anomalies](guardduty_findings-summary.md#rds-pro-data-activity-anomaly).

**Remediation recommendations:**

If this activity is unexpected for the associated database, it is recommended to change the password of the associated database user, and review available audit logs to determine what data the anomalous user accessed. It is recommended to place the database in a private VPC and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with anomalous exfiltration activity](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-exfiltration-activity).

## Impact:RDS/AnomalousBehavior.Drop
<a name="impact-rds-anomalousbehavior-drop"></a>

### Anomalous activity from a user dropping data from an RDS database in your account.
<a name="impact-rds-anomalousbehavior-drop_description"></a>

**Default severity: Medium**

**Note**  
Depending on the anomalous behavior associated with this finding, the default severity can be Medium or High.  
**Medium** – If the user name associated with this finding executed anomalous `DROP` statements.
**High** – If the user name associated with this finding executed multiple `DROP` statements, and the activity either originated from a previously unseen public network or was performed by a high-privilege database role or administrative client.
+ **Feature: **RDS DB Activity Monitoring

This finding informs you that anomalous database activity consistent with destructive operations was observed on an RDS database in your AWS environment. This may indicate that a database user dropped a significantly higher number of tables or database objects than usual, or that the activity involved a previously unseen database attribute such as a new user, IP address, or application name that contributed to the destructive operation. A common scenario is a compromised database credential being used to destroy database structures through a combination of unusual access patterns and elevated `DROP` statement volume.

This activity was identified as anomalous by the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates all database activity events in your [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db) and identifies anomalous events that are associated with techniques used by adversaries. The ML model tracks various factors of the RDS database activity such as the user that made the request, the statements executed, the database objects targeted, and the specific database connection details that were used. For information about the database activity that is potentially unusual, see [RDS data activity-based anomalies](guardduty_findings-summary.md#rds-pro-data-activity-anomaly).

**Remediation recommendations:**

If this activity is unexpected for the associated database, it is recommended to immediately change the password of the associated database user and revoke their access. Review available audit logs to determine the scope of objects dropped, and initiate recovery from backups if necessary. It is also recommended to place the database in a private VPC and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with anomalous destructive activity](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-destructive-activity).

## Impact:RDS/AnomalousBehavior.Delete
<a name="impact-rds-anomalousbehavior-delete"></a>

### Anomalous activity from a user deleting data from an RDS database in your account.
<a name="impact-rds-anomalousbehavior-delete_description"></a>

**Default severity: Low**

**Note**  
Depending on the anomalous behavior associated with this finding, the default severity can be Low, Medium, or High.  
**Low** – If the user name associated with this finding executed `DELETE` statements from an IP address that is associated with a private network.
**Medium** – If the user name associated with this finding executed `DELETE` statements from a public IP address.
**High** – If the user name associated with this finding executed `DELETE` statements returning an unusually large volume of rows, and the activity either originated from a previously unseen public network or was performed by a high-privilege database role or administrative client.
+ **Feature: **RDS DB Activity Monitoring

This finding informs you that anomalous database activity consistent with destructive operations was observed on an RDS database in your AWS environment. This may indicate that a database user deleted a significantly higher number of rows than usual, or that the activity involved a previously unseen database attribute, such as a new user, IP address, or application name, that contributed to the destructive operation. A common scenario is a compromised database credential being used to systematically remove data through a combination of unusual access patterns and elevated `DELETE` statement volume.

This activity was identified as anomalous by the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates all database activity events in your [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db) and identifies anomalous events that are associated with techniques used by adversaries. The ML model tracks various factors of the RDS database activity such as the user that made the request, the statements executed, the number of rows affected, and the specific database connection details that were used. For information about the database activity that is potentially unusual, see [RDS data activity-based anomalies](guardduty_findings-summary.md#rds-pro-data-activity-anomaly).

**Remediation recommendations:**

If this activity is unexpected for the associated database, it is recommended to immediately change the password of the associated database user and revoke their access. Review available audit logs to determine the scope of data deleted, and initiate point-in-time recovery from automated backups if data loss is confirmed. It is also recommended to place the database in a private VPC and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with anomalous destructive activity](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-destructive-activity).

## Exfiltration:RDS/MaliciousIPCaller
<a name="exfiltration-rds-maliciousipcaller"></a>

### An IP address that is associated with known malicious activity executed data extraction queries on an RDS database in your account.
<a name="exfiltration-rds-maliciousipcaller_description"></a>

**Default severity: High**
+ **Feature: **RDS DB Activity Monitoring

This finding informs you that an IP address associated with known malicious activity executed database queries consistent with data exfiltration on an RDS database in your AWS environment. This indicates that the user and password associated with the RDS database in your account may have been compromised, and the RDS database data may have been exfiltrated by a potentially malicious actor.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the user credentials may have been exposed or compromised. It is recommended to change the password of the associated database user, and review available RDS data logs for activity performed by the compromised user. It is recommended to identify the data that was accessible to the affected user and assess the business impact of any potentially exfiltrated data. It is also recommended to place the database in a private VPC and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with anomalous exfiltration activity](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-exfiltration-activity).

## Exfiltration:RDS/TorIPCaller
<a name="exfiltration-rds-toripcaller"></a>

### A Tor exit node IP address executed data extraction queries on an RDS database in your account.
<a name="exfiltration-rds-toripcaller_description"></a>

**Default severity: High**
+ **Feature: **RDS DB Activity Monitoring

This finding informs you that a Tor exit node IP address executed database queries consistent with data exfiltration on an RDS database in your AWS environment. Tor is a software for enabling anonymous communication. It encrypts and randomly bounces communications through relays between a series of network nodes. The last Tor node is called the exit node. This can indicate unauthorized access to the RDS resources in your account, with the intent of hiding the anonymous user's true identity while exfiltrating data.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the user credentials may have been exposed or compromised. It is recommended to change the password of the associated database user, and review available RDS data logs for activity performed by the compromised user. It is recommended to identify the data that was accessible to the affected user and assess the business impact of any potentially exfiltrated data. It is also recommended to place the database in a private VPC and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with anomalous exfiltration activity](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-exfiltration-activity).

## Impact:RDS/MaliciousIPCaller
<a name="impact-rds-maliciousipcaller"></a>

### An IP address that is associated with known malicious activity executed destructive statements on an RDS database in your account.
<a name="impact-rds-maliciousipcaller_description"></a>

**Default severity: High**
+ **Feature: **RDS DB Activity Monitoring

This finding informs you that an IP address associated with known malicious activity executed database statements with destructive impact on an RDS database in your AWS environment. This indicates that the user and password associated with the RDS database in your account may have been compromised, and the RDS database may have been subjected to destructive operations by a potentially malicious actor.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the user credentials may have been exposed or compromised. It is recommended to immediately change the password of the associated database user and revoke their access. Review available RDS data logs to determine the scope of destructive operations performed, and initiate recovery from backups if necessary. It is also recommended to place the database in a private VPC and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with anomalous destructive activity](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-destructive-activity).

## Impact:RDS/TorIPCaller
<a name="impact-rds-toripcaller"></a>

### A Tor exit node IP address executed destructive statements on an RDS database in your account.
<a name="impact-rds-toripcaller_description"></a>

**Default severity: High**
+ **Feature: **RDS DB Activity Monitoring

This finding informs you that a Tor exit node IP address executed database statements with destructive impact on an RDS database in your AWS environment. Tor is an overlay network for enabling anonymous communication. It encrypts and randomly bounces communications through relays between a series of network nodes. The last Tor node is called the exit node. This can indicate unauthorized access to the RDS resources in your account, with the intent of hiding the anonymous user's true identity while performing destructive operations.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the user credentials may have been exposed or compromised. It is recommended to immediately change the password of the associated database user and revoke their access. Review available RDS data logs to determine the scope of destructive operations performed, and initiate recovery from backups if necessary. It is also recommended to place the database in a private VPC and limit the security group rules to allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database with anomalous destructive activity](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-destructive-activity).