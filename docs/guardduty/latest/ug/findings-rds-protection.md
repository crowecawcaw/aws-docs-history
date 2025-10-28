# GuardDuty RDS Protection finding types

GuardDuty RDS Protection detects anomalous login behavior on your database instance. The following findings
are specific to the [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db "rds-protection.md#rds-pro-supported-db")
and will have a **Resource Type** of `RDSDBInstance` or `RDSLimitlessDB`. The severity and
details of the findings will differ based on the finding type.

###### Topics

- [CredentialAccess:RDS/AnomalousBehavior.SuccessfulLogin](#credaccess-rds-anombehavior-successlogin "#credaccess-rds-anombehavior-successlogin")
- [CredentialAccess:RDS/AnomalousBehavior.FailedLogin](#credaccess-rds-anombehavior-failedlogin "#credaccess-rds-anombehavior-failedlogin")
- [CredentialAccess:RDS/AnomalousBehavior.SuccessfulBruteForce](#credaccess-rds-anombehavior-successfulbruteforce "#credaccess-rds-anombehavior-successfulbruteforce")
- [CredentialAccess:RDS/MaliciousIPCaller.SuccessfulLogin](#credaccess-rds-maliciousipcaller-successfullogin "#credaccess-rds-maliciousipcaller-successfullogin")
- [CredentialAccess:RDS/MaliciousIPCaller.FailedLogin](#credaccess-rds-maliciousipcaller-failedlogin "#credaccess-rds-maliciousipcaller-failedlogin")
- [Discovery:RDS/MaliciousIPCaller](#discovery-rds-maliciousipcaller "#discovery-rds-maliciousipcaller")
- [CredentialAccess:RDS/TorIPCaller.SuccessfulLogin](#credaccess-rds-toripcaller-successfullogin "#credaccess-rds-toripcaller-successfullogin")
- [CredentialAccess:RDS/TorIPCaller.FailedLogin](#credaccess-rds-toripcaller-failedlogin "#credaccess-rds-toripcaller-failedlogin")
- [Discovery:RDS/TorIPCaller](#discovery-rds-toripcaller "#discovery-rds-toripcaller")

## CredentialAccess:RDS/AnomalousBehavior.SuccessfulLogin

### A user successfully

logged into an RDS database in your account in an anomalous way.

**Default severity: Variable**

###### Note

Depending on the anomalous behavior associated with this finding, the default severity
can Low, Medium, and High.

- **Low** – If the user name associated with this
  finding logged in from an IP address that is associated with a private network.
- **Medium** – If the user name associated with this
  finding logged in from a public IP address.
- **High** – If there is a consistent pattern of
  failed login attempts from public IP addresses indicative of overly permissive access
  policies.

- **Feature:** RDS login activity monitoring

This finding informs you that an anomalous successful login was observed on an RDS
database in your AWS environment. This may indicate that a previous unseen user logged into
an RDS database for the first time. A common scenario is an internal user logging into a
database that is accessed programmatically by applications and not by individual users.

This successful login was identified as anomalous by the GuardDuty anomaly detection machine
learning (ML) model. The ML model evaluates all database login events in your [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db "rds-protection.md#rds-pro-supported-db") and identifies anomalous
events that are associated with techniques used by adversaries. The ML model tracks various
factors of the RDS login activity such as the user that made the request, the location the request
was made from, and the specific database connection details that were used. For information
about the login events that are potentially unusual, see [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly "guardduty_findings-summary.md#rds-pro-login-anomaly").

**Remediation recommendations:**

If this activity is unexpected for the associated database, it is recommended to change
the password of the associated database user, and review available audit logs for activity
performed by the anomalous user. Medium and high severity findings may indicate that there is
an overly permissive access policy to the database, and user credentials may have been exposed
or compromised. It is recommended to place the database in a private VPC, and limit the
security group rules to allow traffic only from the necessary sources. For more information,
see [Remediating potentially compromised
database with successful login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt").

## CredentialAccess:RDS/AnomalousBehavior.FailedLogin

### One or more unusual failed

login attempts were observed on an RDS database in your account.

**Default severity: Low**

- **Feature:** RDS login activity monitoring

This finding informs you that one or more anomalous failed logins were observed on an RDS
database in your AWS environment. A failed login attempts from public IP addresses may
indicate that the RDS database in your account has been subject to an attempted brute force
attack by a potentially malicious actor.

These failed logins were identified as anomalous by the GuardDuty anomaly detection machine
learning (ML) model. The ML model evaluates all database login events in your [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db "rds-protection.md#rds-pro-supported-db") and identifies anomalous
events that are associated with techniques used by adversaries. The ML model tracks various
factors of the RDS login activity such as the user that made the request, the location the request
was made from, and the specific database connection details that were used. For information
about the RDS login activity that are potentially unusual, see [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly "guardduty_findings-summary.md#rds-pro-login-anomaly").

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the
database is publicly exposed or there is an overly permissive access policy to the database. It
is recommended to place the database in a private VPC, and limit the security group rules to
allow traffic only from the necessary sources. For more information, see [Remediating potentially compromised database
with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt").

## CredentialAccess:RDS/AnomalousBehavior.SuccessfulBruteForce

### A user

successfully logged into an RDS database in your account from a public IP address in an
anomalous way after a consistent pattern of unusual failed login attempts.

**Default severity: High**

- **Feature:** RDS login activity monitoring

This finding informs you that an anomalous login indicative of a successful brute force
was observed on an RDS database in your AWS environment. Prior to an anomalous successful
login, a consistent pattern of unusual failed login attempts was observed. This indicates that
the user and password associated with the RDS database in your account may have been
compromised, and the RDS database may have been accessed by a potentially malicious
actor.

This successful brute force login was identified as anomalous by the GuardDuty anomaly
detection machine learning (ML) model. The ML model evaluates all database login events in your
[Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](rds-protection.md#rds-pro-supported-db "rds-protection.md#rds-pro-supported-db") and identifies
anomalous events that are associated with techniques used by adversaries. The ML model tracks
various factors of the RDS login activity such as the user that made the request, the location the
request was made from, and the specific database connection details that were used. For
information about the RDS login activity that are potentially unusual, see [RDS login activity-based anomalies](guardduty_findings-summary.md#rds-pro-login-anomaly "guardduty_findings-summary.md#rds-pro-login-anomaly").

**Remediation recommendations:**

This activity indicates that database credentials may have been exposed or compromised. It
is recommended to change the password of the associated database user, and review available
audit logs for activity performed by the potentially compromised user. A consistent pattern of
unusual failed login attempts indicate an overly permissive access policy to the database or
the database may have also been public exposed. It is recommended to place the database in a
private VPC, and limit the security group rules to allow traffic only from the necessary
sources. For more information, see [Remediating potentially compromised
database with successful login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt").

## CredentialAccess:RDS/MaliciousIPCaller.SuccessfulLogin

### A user

successfully logged into an RDS database in your account from a known malicious IP
address.

**Default severity: High**

- **Feature:** RDS login activity monitoring

This finding informs you that a successful RDS login activity occurred from an IP address
that is associated with a known malicious activity in your AWS environment. This indicates
that the user and password associated with the RDS database in your account may have been
compromised, and the RDS database may have been accessed by a potentially malicious
actor.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the user
credentials may have been exposed or compromised. It is recommended to change the password of
the associated database user, and review the available audit logs for activity performed by the
compromised user. This activity may also indicate that there is an overly permissive access
policy to the database or the database is publicly exposed. It is recommended to place the
database in a private VPC, and limit the security group rules to allow traffic only from the
necessary sources. For more information, see [Remediating potentially compromised
database with successful login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt").

## CredentialAccess:RDS/MaliciousIPCaller.FailedLogin

### An IP address that is

associated with a known malicious activity unsuccessfully attempted to log in to an RDS
database in your account.

**Default severity: Medium**

- **Feature:** RDS login activity monitoring

This finding informs you that an IP address associated with known malicious activity
attempted to log in to an RDS database in your AWS environment, but failed to provide the
correct user name or password. This indicates that a potentially malicious actor may be
attempting to compromise the RDS database in your account.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that there is
an overly permissive access policy to the database or the database is publicly exposed. It is
recommended to place the database in a private VPC, and limit the security group rules to allow
traffic only from the necessary sources. For more information, see [Remediating potentially compromised database
with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt").

## Discovery:RDS/MaliciousIPCaller

### An IP address that is associated

with a known malicious activity probed an RDS database in your account; no authentication
attempt was made.

**Default severity: Medium**

- **Feature:** RDS login activity monitoring

This finding informs you that an IP address associated with known a malicious activity
probed an RDS database in your AWS environment, though no login attempt was made. This may
indicate that a potentially malicious actor is attempting to scan for a publicly accessible
infrastructure.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that there is
an overly permissive access policy to the database or the database is publicly exposed. It is
recommended to place the database in a private VPC, and limit the security group rules to allow
traffic only from the necessary sources. For more information, see [Remediating potentially compromised database
with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt").

## CredentialAccess:RDS/TorIPCaller.SuccessfulLogin

### A user successfully

logged into an RDS database in your account from a Tor exit node IP address.

**Default severity: High**

- **Feature:** RDS login activity monitoring

This finding informs you that a user successfully logged in to an RDS database in your
AWS environment, from a Tor exit node IP address. Tor is a software for enabling anonymous
communication. It encrypts and randomly bounces communications through relays between a series
of network nodes. The last Tor node is called the exit node. This can indicate unauthorized
access to the RDS resources in your account, with the intent of hiding the anonymous user's
true identity.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that the user
credentials may have been exposed or compromised. It is recommended to change the password of
the associated database user, and review the available audit logs for activity performed by the
compromised user. This activity may also indicate that there is an overly permissive access
policy to the database or the database is publicly exposed. It is recommended to place the
database in a private VPC, and limit the security group rules to allow traffic only from the
necessary sources. For more information, see [Remediating potentially compromised
database with successful login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-successful-attempt").

## CredentialAccess:RDS/TorIPCaller.FailedLogin

### A Tor IP address attempted

to unsuccessfully log in to an RDS database in your account.

**Default severity: Medium**

- **Feature:** RDS login activity monitoring

This finding informs you that a Tor exit node IP address attempted to log in to an RDS
database in your AWS environment, but failed to provide the correct user name or password.
Tor is a software for enabling anonymous communication. It encrypts and randomly bounces
communications through relays between a series of network nodes. The last Tor node is called
the exit node. This can indicate unauthorized access to the RDS resources in your account, with
the intent of hiding the anonymous user's true identity.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that there is
an overly permissive access policy to the database or the database is publicly exposed. It is
recommended to place the database in a private VPC, and limit the security group rules to allow
traffic only from the necessary sources. For more information, see [Remediating potentially compromised database
with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt").

## Discovery:RDS/TorIPCaller

### A Tor exit node IP address probed an RDS

database in your account, no authentication attempt was made.

**Default severity: Medium**

- **Feature:** RDS login activity monitoring

This finding informs you that a Tor exit node IP address probed an RDS database in your
AWS environment, though no login attempt was made. This may indicate that a potentially
malicious actor is attempting to scan for publicly accessible infrastructure. Tor is a software
for enabling anonymous communication. It encrypts and randmonly bounces communications through
relays between a series of network nodes. The last Tor node is called the exit node. This can
indicate unauthorized access to the RDS resources in your account, with the intent of hiding
the potentially malicious actor's true identity.

**Remediation recommendations:**

If this activity is unexpected for the associated database, it may indicate that there is
an overly permissive access policy to the database or the database is publicly exposed. It is
recommended to place the database in a private VPC, and limit the security group rules to allow
traffic only from the necessary sources. For more information, see [Remediating potentially compromised database
with failed login events](guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt "guardduty-remediate-compromised-database-rds.md#gd-compromised-db-failed-attempt").
