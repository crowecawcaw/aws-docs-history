# Remediation logs in Trusted Remediator

Trusted Remediator creates logs in JSON format and uploads them to Amazon Simple Storage Service The log files are uploaded to an S3 bucket created by AMS and named
`ams-trusted-remediator-{your-account-id}-logs`. AMS creates the S3 bucket in the Delegated Administrator account. You can import the log files into Quick Suite to
generate customized remediation reports.

For more information, see [Trusted Remediator integration with Quick Suite](tr-qs-integration.md "tr-qs-integration.md").

## Remediation item log

Trusted Remediator creates the `Remediation item log` when a remediation OpsItem is created. This log contains manual remediation OpsItem and automated remediation OpsItem. You can use the
`Remediation item log` to track the overview of all remediations.

**Remediation item log location for Compute Optimizer recommendations**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs/compute_optimizer_remediation_items/`remediation creation time in
yyyy-mm-dd format`/`10 digits epoch time or unix timestamp`-`Trusted Advisor check ID`-
 `Resource ID`.json`

**Remediation item log location for Trusted Advisor checks**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs/remediation_items/`remediation creation time in
yyyy-mm-dd format`/`10 digits epoch time or unix timestamp`-`Trusted Advisor check ID`-
 `Resource ID`.json`

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

## Automated remediation execution log, Compute Optimizer and Trusted Advisor

Trusted Remediator creates the `Automated remediation execution log` when an automated SSM document run is completed. This log contains SSM run details for
automated remediation OpsItem only. You can use this log file to track automated remediations.

**Compute Optimizer Automated remediation log location**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs//remediation_executions/`remediation creation time in
yyyy-mm-dd format`/`10 digits epoch time or unix timestamp`-`Compute Optimizer recommendation ID`.json`

**Trusted Advisor Automated remediation log location**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs//remediation_executions/`remediation creation time in
yyyy-mm-dd format`/`10 digits epoch time or unix timestamp`-`Trusted Advisor check ID`-`Resource ID`.json`

**Compute Optimizer Automated remediation log location example**

`s3://ams-trusted-remediator-`111122223333`-logs/remediation_executions/2025-06-26/1750908858-123456789012-compute-optimizer-ec2-i-1235173471d2cd789.json`

**Trusted Advisor Automated remediation log location example**

`s3://ams-trusted-remediator-`111122223333`-logs/remediation_executions/2023-02-06/1675660573-DAvU99Dc4C-vol-00bd8965660b4c16d.json`

**Automated remediation log format sample content**

```
{
    "OpsItemID": "oi-767c77e05301",
    "SSMExecutionID": "93d091b2-778a-4cbc-b672-006954d76b86",
    "SSMExecutionStatus": "Success"}
```

## Member accounts log

Trusted Remediator creates the `Member accounts log` when your account is onboarded or offboarded. You can use the `Member accounts log` to find the account ID, onboarded
AWS Regions, and execution time of each member account.

**Member accounts log location**

`s3://ams-trusted-remediator-`delegated-administrator-account-id`-logs/configuration_logs/member_accounts.json`

**Member accounts log sample file URL**

`s3://ams-trusted-remediator-`111122223333`-logs/configuration_logs/member_accounts.json`

**Member accounts log format**

```
{
    "delegated_administrator_account_id": `Delegated Administrator account id`,
    "appconfig_configuration_region": `Trusted Remediator AppConfig Region`,
    "member_accounts": [
        {
            "account_id": `Member account id`
            "account_partition": `Member account partition (for example, aws)`,
            "regions": [
                {
                    "execution_time": `Remediation execution time in cron schedule expression`,
                    "execution_timezone": `Timezone for the remediation execution time`,
                    "region_name": `AWS Region name`
                }
                ...
            ]
        }
        ...
    ],
    "updated_at": `Log update time`,
}
```

**Member accounts log format sample content**

```
{
    "delegated_administrator_account_id": "111122223333",
    "appconfig_configuration_region": "ap-southeast-2",
    "member_accounts": [
        {
            "account_id": "222233334444",
            "account_partition": "aws",
            "regions": [
                {
                    "execution_time": "0 9 * * 6",
                    "execution_timezone": "Australia/Sydney",
                    "region_name": "ap-southeast-2"
                },
                {
                    "execution_time": "0 5 * * 7",
                    "execution_timezone": "UTC",
                    "region_name": "us-east-1"
                }
            ]
        },
        {
            "account_id": "333344445555",
            "account_partition": "aws",
            "regions": [
                {
                    "execution_time": "0 1 * * 5",
                    "execution_timezone": "Asia/Seoul",
                    "region_name": "ap-northeast-2"
                }
            ]
        }
    ],
    "updated_at": "1730869607"
}
```
