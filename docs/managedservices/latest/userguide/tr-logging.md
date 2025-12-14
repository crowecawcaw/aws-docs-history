# Remediation logs in Trusted Remediator

Trusted Remediator creates logs in JSON format and uploads them to Amazon Simple Storage Service The log files are uploaded to an S3 bucket created by AMS and named
`ams-trusted-remediator-{your-account-id}-logs`. AMS creates the S3 bucket in the Delegated Administrator account. You can import the log files into Quick Suite to
generate customized remediation reports.

## Remediation item log

Trusted Remediator creates the `Remediation item log` when a remediation OpsItem is created. This log contains manual remediation OpsItem and automated remediation OpsItem. You can use the
`Remediation item log` to track the overview of all remediations.

**Remediation item log location for Compute Optimizer recommendations**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs/compute_optimizer_remediation_items/`remediation
creation time in yyyy-mm-dd format`/`10 digits epoch time or
unix timestamp`-`Compute Optimizer check ID`-
 `Resource ID`.json`

**Remediation item log location for Trusted Advisor checks**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs/remediation_items/`remediation creation time in
yyyy-mm-dd format`/`10 digits epoch time or unix timestamp`-`Trusted Advisor check ID`-
 `Resource ID`.json`

**Remediation item log location for Security Hub CSPM
recommendations**

`s3://ams-trusted-remediator-`delegated-administrator-account`-id-logs/security_hub_remediation_items/`remediation
creation time in yyyy-mm-dd format`/`10 digits epoch time or
unix timestamp-Security Hub CSPM check ID- Resource ID`.json`

**Remediation item log sample file URL**

`s3:///ams-trusted-remediator-`111122223333`-logs/remediation_items/`2023-02-06`/`1675660464-DAvU99Dc4C-vol-00bd8965660b4c16d.json``

**Compute Optimizer Remediation item log format**

```
{
  "AccountID": "`Account_ID`",
  "ComputeOptimizerCheckID": "`Compute Optimizer check ID`",
  "ComputeOptimizerCheckName": "`Compute Optimizer check name`",
  "ResourceID": "`Resource ID`",
  "RemediationTime": `Remediation creation time`,
  "ExecutionMode": "`Automated or Manual`",
  "OpsItemID": "`OpsItem ID`"
}
```

**Trusted Advisor Remediation item log format**

```
{
   "TrustedAdvisorCheckID": `Trusted Advisor check ID`,
   "TrustedAdvisorCheckName": `Trusted Advisor check name`,
   "TrustedAdvisorCheckResultTime": `10 digits epoch time or unix timestamp`,
   "ResourceID": `Resource ID`,
   "RemediationTime": `Remediation creation time`,
   "ExecutionMode": `Automated or Manual`,
   "OpsItemID": `OpsItem ID`
}
```

**Security Hub CSPM Remediation item log format**

```
{
 "AccountID": "`Account_ID`",
 "SecurityHubCheckID": "`Security Hub check ID`",
 "SecurityHubCheckName": "`Security Hub check name`",
 "ResourceID": "`Resource ID`",
 "RemediationTime": `Remediation creation time`,
 "ExecutionMode": "`Automated or Manual`",
 "OpsItemID": "`OpsItem ID`"
}
```

**Compute Optimizer Remediation item log format sample content**

```
{
  "AccountID": "123456789012",
  "ComputeOptimizerCheckID": "compute-optimizer-ebs",
  "ComputeOptimizerCheckName": "EBS volumes",
  "ResourceID": "vol-1235589366f77aca7",
  "RemediationTime": 1755044783,
  "ExecutionMode": "Manual",
  "OpsItemID": "oi-b8888b38fe78"
}
```

**Trusted Advisor Remediation item log format sample content**

```
{
    "TrustedAdvisorCheckID": "DAvU99Dc4C",
    "TrustedAdvisorCheckName": "Underutilized Amazon EBS Volumes",
    "TrustedAdvisorCheckResultTime": 1675614749,
    "ResourceID": "vol-00bd8965660b4c16d",
    "RemediationTime": 1675660464,
    "OpsItemID": "oi-cca5df7af718"
}
```

**Security Hub CSPM Remediation item log format sample content**

```
{
    "AccountID": "012345678901",
    "SecurityHubControlID": "security-hub-lambda-7",
    "SecurityHubControlName": "Lambda functions should have AWS X-Ray active tracing enabled",
    "SecurityHubControlResultTime": 1764580147,
    "ResourceID": "test-lambda-7-xray-disabled",
    "RemediationTime": 1764900171,
    "ExecutionMode": "Manual",
    "OpsItemID": "oi-ea12c3456d7f"
}
```

## Automated remediation execution log, Compute Optimizer, Security Hub CSPM, and

Trusted Advisor

Trusted Remediator creates the `Automated remediation execution log` when an automated SSM document run is completed. This log contains SSM run details for
automated remediation OpsItem only. You can use this log file to track automated remediations.

**Compute Optimizer Automated remediation log location**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs//remediation_executions/`remediation creation time in
yyyy-mm-dd format`/`10 digits epoch time or unix timestamp`-`Compute Optimizer recommendation ID`.json`

**Security Hub CSPM Automated remediation log location**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs//remediation_executions/`remediation
creation time in yyyy-mm-dd format`/`10 digits epoch time or
unix timestamp`-`Security Hub CSPM recommendation
ID`.json`

**Trusted Advisor Automated remediation log location**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs//remediation_executions/`remediation creation time in
yyyy-mm-dd format`/`10 digits epoch time or unix timestamp`-`Trusted Advisor check ID`-`Resource ID`.json`

**Compute Optimizer Automated remediation log location example**

`s3://ams-trusted-remediator-`111122223333`-logs/remediation_executions/2025-06-26/1750908858-123456789012-compute-optimizer-ec2-i-1235173471d2cd789.json`

**Security Hub CSPM Automated remediation log location example**

`s3://ams-trusted-remediator-`111122223333`-logs/remediation_executions/2025-06-26/763247655-066028476520-security-hub-rds-8-miz-tr-sh-test-rds-instance-1.json`

**Trusted Advisor Automated remediation log location example**

`s3://ams-trusted-remediator-`111122223333`-logs/remediation_executions/2023-02-06/1675660573-DAvU99Dc4C-vol-00bd8965660b4c16d.json`

**Automated remediation log format sample content**

```
{
    "OpsItemID": "oi-767c77e05301",
    "SSMExecutionID": "93d091b2-778a-4cbc-b672-006954d76b86",
    "SSMExecutionStatus": "Success"
}
```
