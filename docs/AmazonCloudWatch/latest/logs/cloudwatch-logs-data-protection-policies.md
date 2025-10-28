# Understanding data protection

policies

###### Topics

- [What are data protection
  policies?](#what-are-data-protection-policies "#what-are-data-protection-policies")
- [How is the data protection policy
  structured?](#overview-of-data-protection-policies "#overview-of-data-protection-policies")

## What are data protection

policies?

CloudWatch Logs uses **data protection policies** to select the
sensitive data for which you want to scan, and the actions that you want to take to
protect that data. To select the sensitive
data of interest, you use [data identifiers](CWL-managed-data-identifiers.md "CWL-managed-data-identifiers.md"). CloudWatch Logs data protection then detects the sensitive
data by using machine learning and pattern matching. To act upon data identifiers that
are found, you can define **audit** and **de-identify** operations. These operations let you log the sensitive
data that is found (or not found), and to mask the sensitive data when the log events are viewed.

## How is the data protection policy

structured?

As illustrated in the following figure, a data protection policy document includes the
following elements:

- Optional policy-wide information at the top of the document
- One statement that defines the audit and de-identify actions

Only one data protection policy can be defined per CloudWatch Logs log group. The data protection
policy can have one or more deny or de-identify statements, but only one audit
statement.

### JSON properties for the

data protection policy

A data protection policy requires the following basic policy information for
identification:

- **Name** – The policy name.
- **Description** (Optional) – The
  policy description.
- **Version** – The policy language
  version. The current version is 2021-06-01.
- **Statement** – A list of statements
  that specifies data protection policy actions.

```
{
  "Name": "CloudWatchLogs-PersonalInformation-Protection",
  "Description": "Protect basic types of sensitive data",
  "Version": "2021-06-01",
  "Statement": [
        ...
  ]
}
```

### JSON properties for a policy

statement

A policy statement sets the detection context for the data protection
operation.

- **Sid** (Optional) – The statement
  identifier.
- **DataIdentifier** – The sensitive
  data for which CloudWatch Logs should scan. For example, name, address, or
  phone number.
- **Operation** – The follow-on actions,
  either **Audit** or **De-identify**. CloudWatch Logs performs
  these actions when it finds sensitive data.

```
{
  ...
  "Statement": [
    {
      "Sid": "audit-policy",
      "DataIdentifier": [
        "arn:aws:dataprotection::aws:data-identifier/Address"
      ],
      "Operation": {
        "Audit": {
          "FindingsDestination": {}
        }
      }
    },
```

### JSON properties for a policy

statement operation

A policy statement sets one of the following data protection operations.

- **Audit** – Emits metrics and findings
  reports without interrupting logging. Strings that match
  increment the **LogEventsWithFindings** metric that CloudWatch Logs publishes to the
  **AWS/Logs** namespace in CloudWatch. You can use these metrics to create alarms.

For an example of a findings report,
see [Audit findings reports](mask-sensitive-log-data-audit-findings.md "mask-sensitive-log-data-audit-findings.md").

For more information
about metrics that CloudWatch Logs sends to CloudWatch, see
[Monitoring with CloudWatch metrics](CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md "CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md").

- **De-identify** – Mask the
  sensitive data without interrupting logging.
