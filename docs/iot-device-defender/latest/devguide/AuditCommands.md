# Audit commands

## Manage audit settings

Use `UpdateAccountAuditConfiguration` to configure audit settings for your
account. This command allows you to enable those checks you want to be available for audits,
set up optional notifications, and configure permissions.

Check these settings with `DescribeAccountAuditConfiguration`.

Use `DeleteAccountAuditConfiguration` to delete your audit settings. This
restores all default values, and effectively disables audits because all checks are disabled
by default.

###

UpdateAccountAuditConfiguration

Configures or reconfigures the Device Defender audit settings for this account. Settings
include how audit notifications are sent and which audit checks are enabled or
disabled.

**Synopsis**

```
aws iot  update-account-audit-configuration \
    [--role-arn <value>] \
    [--audit-notification-target-configurations <value>] \
    [--audit-check-configurations <value>]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "roleArn": "string",
  "auditNotificationTargetConfigurations": {
    "string": {
      "targetArn": "string",
      "roleArn": "string",
      "enabled": "boolean"
    }
  },
  "auditCheckConfigurations": {
    "string": {
      "enabled": "boolean"
    }
  }
}
```

| `cli-input-json` Fields               | Name                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| ------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| roleArn                               | string<br>length<br>• max:2048 min:20 | The ARN of the role that grants permission to AWS IoT to access information<br>about your devices, policies, certificates, and other items when performing an<br>audit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| auditNotificationTargetConfigurations | map                                   | Information about the targets to which audit notifications are<br>sent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| targetArn                             | string                                | The ARN of the target (SNS topic) to which audit notifications are<br>sent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| roleArn                               | string<br>length<br>• max:2048 min:20 | The ARN of the role that grants permission to send notifications to the<br>target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| enabled                               | boolean                               | True if notifications to the target are enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| auditCheckConfigurations              | map                                   | Specifies which audit checks are enabled and disabled for this account. Use<br>`DescribeAccountAuditConfiguration` to see the list of all checks,<br>including those that are currently enabled.<br>Some data collection might start immediately when certain checks are enabled.<br>When a check is disabled, any data collected so far in relation to the check is<br>deleted.<br>You cannot disable a check if it is used by any scheduled audit. You must<br>first delete the check from the scheduled audit or delete the scheduled audit<br>itself.<br>On the first call to `UpdateAccountAuditConfiguration`, this<br>parameter is required and must specify at least one enabled check. |
| enabled                               | boolean                               | True if this audit check is enabled for this account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| configuration                         | map                                   | (Optional) custom configurations for specific audit checks, such as the<br>`CERT_AGE_THRESHOLD_IN_DAYS` and `CERT_EXPIRATION_THRESHOLD_IN_DAYS`, allowing you to<br>define when you want to be alerted about certificate age and impending<br>expiration.                                                                                                                                                                                                                                                                                                                                                                                                                                       |

Output

None

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

###

DescribeAccountAuditConfiguration

Gets information about the Device Defender audit settings for this account. Settings
include how audit notifications are sent and which audit checks are enabled or
disabled.

**Synopsis**

```
aws iot  describe-account-audit-configuration  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
}
```

Output

```
{
  "roleArn": "string",
  "auditNotificationTargetConfigurations": {
    "string": {
      "targetArn": "string",
      "roleArn": "string",
      "enabled": "boolean"
    }
  },
  "auditCheckConfigurations": {
    "string": {
      "enabled": "boolean"
    }
  }
}
```

| CLI output fields                     | Name                                  | Type                                                                                                                                                                                                                                                              | Description |
| ------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| roleArn                               | string<br>length<br>• max:2048 min:20 | The ARN of the role that grants permission to AWS IoT to access information<br>about your devices, policies, certificates, and other items when performing an<br>audit.<br>On the first call to `UpdateAccountAuditConfiguration`, this<br>parameter is required. |
| auditNotificationTargetConfigurations | map                                   | Information about the targets to which audit notifications are sent for this<br>account.                                                                                                                                                                          |
| targetArn                             | string                                | The ARN of the target (SNS topic) to which audit notifications are<br>sent.                                                                                                                                                                                       |
| roleArn                               | string<br>length<br>• max:2048 min:20 | The ARN of the role that grants permission to send notifications to the<br>target.                                                                                                                                                                                |
| enabled                               | boolean                               | True if notifications to the target are enabled.                                                                                                                                                                                                                  |
| auditCheckConfigurations              | map                                   | Which audit checks are enabled and disabled for this account.                                                                                                                                                                                                     |
| enabled                               | boolean                               | True if this audit check is enabled for this account.                                                                                                                                                                                                             |
| configuration                         | map                                   | (Optional) provides specific configurations for certain audit checks, such as<br>the maximum allowed age for certificates or the number of days before expiration<br>when an alert should be triggered.                                                           |

**Errors**

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

###

DeleteAccountAuditConfiguration

Restores the default settings for Device Defender audits for this account. Any
configuration data you entered is deleted and all audit checks are reset to disabled.

**Synopsis**

```
aws iot  delete-account-audit-configuration \
    [--delete-scheduled-audits | --no-delete-scheduled-audits]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "deleteScheduledAudits": "boolean"
}
```

| `cli-input-json` Fields | Name    | Type                                       | Description |
| ----------------------- | ------- | ------------------------------------------ | ----------- |
| deleteScheduledAudits   | boolean | If true, all scheduled audits are deleted. |

Output

None

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ResourceNotFoundException`

The specified resource does not exist.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

## Schedule audits

Use `CreateScheduledAudit` to create one or more scheduled audits. This command
allows you to specify the checks you want to perform during an audit and how often the audit
should be run.

Keep track of your scheduled audits with `ListScheduledAudits` and
`DescribeScheduledAudit`.

Change an existing scheduled audit with `UpdateScheduledAudit` or delete it
with `DeleteScheduledAudit`.

### CreateScheduledAudit

Creates a scheduled audit that is run at a specified time interval.

**Synopsis**

```
aws iot  create-scheduled-audit \
    --frequency <value> \
    [--day-of-month <value>] \
    [--day-of-week <value>] \
    --target-check-names <value> \
    [--tags <value>] \
    --scheduled-audit-name <value>  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "frequency": "string",
  "dayOfMonth": "string",
  "dayOfWeek": "string",
  "targetCheckNames": [
    "string"
  ],
  "tags": [
    {
      "Key": "string",
      "Value": "string"
    }
  ],
  "scheduledAuditName": "string"
}
```

| `cli-input-json` Fields | Name                                                            | Type                                                                                                                                                                                                                                                                                           | Description |
| ----------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- |
| frequency               | string                                                          | How often the scheduled audit takes place. Can be one of DAILY, WEEKLY,<br>BIWEEKLY, or MONTHLY. The actual start time of each audit is determined by the<br>system.<br>enum: DAILY                                                                                                            | WEEKLY      | BIWEEKLY | MONTHLY                                                                                                                                                                                                                                                                                                  |
| dayOfMonth              | string<br>pattern: ^([1-9]                                      | [12][0-9]                                                                                                                                                                                                                                                                                      | 3[01])$     | ^LAST$   | The day of the month on which the scheduled audit takes place. Can be 1<br>through 31 or LAST. This field is required if the `frequency` parameter<br>is set to MONTHLY. If days 29-31 are specified, and the month does not have that<br>many days, the audit takes place on the LAST day of the month. |
| dayOfWeek               | string                                                          | The day of the week on which the scheduled audit takes place. Can be one of<br>SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the<br>`frequency` parameter is set to WEEKLY or BIWEEKLY.<br>enum: SUN                                                                          | MON         | TUE      | WED                                                                                                                                                                                                                                                                                                      | THU | FRI | SAT |
| targetCheckNames        | list<br>member: AuditCheckName                                  | Which checks are performed during the scheduled audit. Checks must be enabled<br>for your account. (Use `DescribeAccountAuditConfiguration` to see the<br>list of all checks, including those that are enabled or<br>`UpdateAccountAuditConfiguration` to select which checks are<br>enabled.) |
| tags                    | list<br>member: Tag<br>java class: java.util.List               | Metadata that can be used to manage the scheduled audit.                                                                                                                                                                                                                                       |
| Key                     | string                                                          | The tag's key.                                                                                                                                                                                                                                                                                 |
| Value                   | string                                                          | The tag's value.                                                                                                                                                                                                                                                                               |
| scheduledAuditName      | string<br>length<br>• max:128 min:1<br>pattern: [a-zA-Z0-9\_-]+ | The name you want to give to the scheduled audit. (Maximum of 128<br>characters)                                                                                                                                                                                                               |

Output

```
{
  "scheduledAuditArn": "string"
}
```

| CLI output fields | Name   | Type                            | Description |
| ----------------- | ------ | ------------------------------- | ----------- |
| scheduledAuditArn | string | The ARN of the scheduled audit. |

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

`LimitExceededException`

A limit has been exceeded.

### ListScheduledAudits

Lists all of your scheduled audits.

**Synopsis**

```
aws iot  list-scheduled-audits \
    [--next-token <value>] \
    [--max-results <value>]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "nextToken": "string",
  "maxResults": "integer"
}
```

| `cli-input-json` Fields | Name                                | Type                                                                       | Description |
| ----------------------- | ----------------------------------- | -------------------------------------------------------------------------- | ----------- |
| nextToken               | string                              | The token for the next set of results.                                     |
| maxResults              | integer<br>range<br>• max:250 min:1 | The maximum number of results to return at one time. The default is<br>25. |

Output

```
{
  "scheduledAudits": [
    {
      "scheduledAuditName": "string",
      "scheduledAuditArn": "string",
      "frequency": "string",
      "dayOfMonth": "string",
      "dayOfWeek": "string"
    }
  ],
  "nextToken": "string"
}
```

| CLI output fields  | Name                                                                 | Type                                                                                                                | Description |
| ------------------ | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- |
| scheduledAudits    | list<br>member: ScheduledAuditMetadata<br>java class: java.util.List | The list of scheduled audits.                                                                                       |
| scheduledAuditName | string<br>length<br>• max:128 min:1<br>pattern: [a-zA-Z0-9\_-]+      | The name of the scheduled audit.                                                                                    |
| scheduledAuditArn  | string                                                               | The ARN of the scheduled audit.                                                                                     |
| frequency          | string                                                               | How often the scheduled audit takes place.<br>enum: DAILY                                                           | WEEKLY      | BIWEEKLY | MONTHLY                                                                                                                                                                                                                         |
| dayOfMonth         | string<br>pattern: ^([1-9]                                           | [12][0-9]                                                                                                           | 3[01])$     | ^LAST$   | The day of the month on which the scheduled audit is run (if the<br>`frequency` is MONTHLY). If days 29-31 are specified, and the month<br>does not have that many days, the audit takes place on the LAST day of the<br>month. |
| dayOfWeek          | string                                                               | The day of the week on which the scheduled audit is run (if the<br>`frequency` is WEEKLY or BIWEEKLY).<br>enum: SUN | MON         | TUE      | WED                                                                                                                                                                                                                             | THU | FRI | SAT |
| nextToken          | string                                                               | A token that can be used to retrieve the next set of results, or<br>`null` if there are no more results.            |

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

### DescribeScheduledAudit

Gets information about a scheduled audit.

**Synopsis**

```
aws iot  describe-scheduled-audit \
    --scheduled-audit-name <value>  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "scheduledAuditName": "string"
}
```

| `cli-input-json` Fields | Name                                                            | Type                                                                  | Description |
| ----------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------- | ----------- |
| scheduledAuditName      | string<br>length<br>• max:128 min:1<br>pattern: [a-zA-Z0-9\_-]+ | The name of the scheduled audit whose information you want to<br>get. |

Output

```
{
  "frequency": "string",
  "dayOfMonth": "string",
  "dayOfWeek": "string",
  "targetCheckNames": [
    "string"
  ],
  "scheduledAuditName": "string",
  "scheduledAuditArn": "string"
}
```

| CLI output fields  | Name                                                            | Type                                                                                                                                                                                                                                                                                               | Description |
| ------------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- | --- | --- |
| frequency          | string                                                          | How often the scheduled audit takes place. One of DAILY, WEEKLY, BIWEEKLY, or<br>MONTHLY. The actual start time of each audit is determined by the system.<br>enum: DAILY                                                                                                                          | WEEKLY      | BIWEEKLY | MONTHLY                                                                                                                                                                                                                        |
| dayOfMonth         | string<br>pattern: ^([1-9]                                      | [12][0-9]                                                                                                                                                                                                                                                                                          | 3[01])$     | ^LAST$   | The day of the month on which the scheduled audit takes place. Can be 1<br>through 31 or LAST. If days 29-31 are specified, and the month does not have that<br>many days, the audit takes place on the LAST day of the month. |
| dayOfWeek          | string                                                          | The day of the week on which the scheduled audit takes place. One of SUN, MON,<br>TUE, WED, THU, FRI, or SAT.<br>enum: SUN                                                                                                                                                                         | MON         | TUE      | WED                                                                                                                                                                                                                            | THU | FRI | SAT |
| targetCheckNames   | list<br>member: AuditCheckName                                  | Which checks are performed during the scheduled audit. Checks must be enabled<br>for your account. (Use `DescribeAccountAuditConfiguration` to see the<br>list of all checks, including those that are enabled or use<br>`UpdateAccountAuditConfiguration` to select which checks are<br>enabled.) |
| scheduledAuditName | string<br>length<br>• max:128 min:1<br>pattern: [a-zA-Z0-9\_-]+ | The name of the scheduled audit.                                                                                                                                                                                                                                                                   |
| scheduledAuditArn  | string                                                          | The ARN of the scheduled audit.                                                                                                                                                                                                                                                                    |

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ResourceNotFoundException`

The specified resource does not exist.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

### UpdateScheduledAudit

Updates a scheduled audit, including which checks are performed and how often the audit
takes place.

**Synopsis**

```
aws iot  update-scheduled-audit \
    [--frequency <value>] \
    [--day-of-month <value>] \
    [--day-of-week <value>] \
    [--target-check-names <value>] \
    --scheduled-audit-name <value>  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "frequency": "string",
  "dayOfMonth": "string",
  "dayOfWeek": "string",
  "targetCheckNames": [
    "string"
  ],
  "scheduledAuditName": "string"
}
```

| `cli-input-json` Fields | Name                                                            | Type                                                                                                                                                                                                                                                                                               | Description |
| ----------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- |
| frequency               | string                                                          | How often the scheduled audit takes place. Can be one of DAILY, WEEKLY,<br>BIWEEKLY, or MONTHLY. The actual start time of each audit is determined by the<br>system.<br>enum: DAILY                                                                                                                | WEEKLY      | BIWEEKLY | MONTHLY                                                                                                                                                                                                                                                                                                  |
| dayOfMonth              | string<br>pattern: ^([1-9]                                      | [12][0-9]                                                                                                                                                                                                                                                                                          | 3[01])$     | ^LAST$   | The day of the month on which the scheduled audit takes place. Can be 1<br>through 31 or LAST. This field is required if the `frequency` parameter<br>is set to MONTHLY. If days 29-31 are specified, and the month does not have that<br>many days, the audit takes place on the LAST day of the month. |
| dayOfWeek               | string                                                          | The day of the week on which the scheduled audit takes place. Can be one of<br>SUN, MON, TUE, WED, THU, FRI, or SAT. This field is required if the<br>`frequency` parameter is set to WEEKLY or BIWEEKLY.<br>enum: SUN                                                                             | MON         | TUE      | WED                                                                                                                                                                                                                                                                                                      | THU | FRI | SAT |
| targetCheckNames        | list<br>member: AuditCheckName                                  | Which checks are performed during the scheduled audit. Checks must be enabled<br>for your account. (Use `DescribeAccountAuditConfiguration` to see the<br>list of all checks, including those that are enabled or use<br>`UpdateAccountAuditConfiguration` to select which checks are<br>enabled.) |
| scheduledAuditName      | string<br>length<br>• max:128 min:1<br>pattern: [a-zA-Z0-9\_-]+ | The name of the scheduled audit. (Maximum of 128 characters)                                                                                                                                                                                                                                       |

Output

```
{
  "scheduledAuditArn": "string"
}
```

| CLI output fields | Name   | Type                            | Description |
| ----------------- | ------ | ------------------------------- | ----------- |
| scheduledAuditArn | string | The ARN of the scheduled audit. |

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ResourceNotFoundException`

The specified resource does not exist.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

### DeleteScheduledAudit

Deletes a scheduled audit.

**Synopsis**

```
aws iot  delete-scheduled-audit \
    --scheduled-audit-name <value>  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "scheduledAuditName": "string"
}
```

| `cli-input-json` Fields | Name                                                            | Type                                                | Description |
| ----------------------- | --------------------------------------------------------------- | --------------------------------------------------- | ----------- |
| scheduledAuditName      | string<br>length<br>• max:128 min:1<br>pattern: [a-zA-Z0-9\_-]+ | The name of the scheduled audit you want to delete. |

Output

None

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ResourceNotFoundException`

The specified resource does not exist.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

## Run an On-Demand audit

Use `StartOnDemandAuditTask` to specify the checks you want to perform and
start an audit running right away.

### StartOnDemandAuditTask

Starts an on-demand Device Defender audit.

**Synopsis**

```
aws iot  start-on-demand-audit-task \
    --target-check-names <value>  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "targetCheckNames": [
    "string"
  ]
}
```

| `cli-input-json` Fields | Name                           | Type                                                                                                                                                                                                                                                                                                                             | Description |
| ----------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| targetCheckNames        | list<br>member: AuditCheckName | Which checks are performed during the audit. The checks you specify must be<br>enabled for your account or an exception occurs. Use<br>`DescribeAccountAuditConfiguration` to see the list of all checks,<br>including those that are enabled or use<br>`UpdateAccountAuditConfiguration` to select which checks are<br>enabled. |

Output

```
{
  "taskId": "string"
}
```

| CLI output fields | Name                                                         | Type                                       | Description |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------ | ----------- |
| taskId            | string<br>length<br>• max:40 min:1<br>pattern: [a-zA-Z0-9-]+ | The ID of the on-demand audit you started. |

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

`LimitExceededException`

A limit has been exceeded.

## Manage audit instances

Use `DescribeAuditTask` to get information about a specific audit instance. If
it has already run, the results include which checks failed and which passed, those that the
system was unable to complete, and if the audit is still in progress, those it is still
working on.

Use `ListAuditTasks` to find the audits that were run during a specified time
interval.

Use `CancelAuditTask` to halt an audit in progress.

### DescribeAuditTask

Gets information about a Device Defender audit.

**Synopsis**

```
aws iot  describe-audit-task \
    --task-id <value>  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "taskId": "string"
}
```

| `cli-input-json` Fields | Name                                                         | Type                                                   | Description |
| ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------ | ----------- |
| taskId                  | string<br>length<br>• max:40 min:1<br>pattern: [a-zA-Z0-9-]+ | The ID of the audit whose information you want to get. |

Output

```
{
  "taskStatus": "string",
  "taskType": "string",
  "taskStartTime": "timestamp",
  "taskStatistics": {
    "totalChecks": "integer",
    "inProgressChecks": "integer",
    "waitingForDataCollectionChecks": "integer",
    "compliantChecks": "integer",
    "nonCompliantChecks": "integer",
    "failedChecks": "integer",
    "canceledChecks": "integer"
  },
  "scheduledAuditName": "string",
  "auditDetails": {
    "string": {
      "checkRunStatus": "string",
      "checkCompliant": "boolean",
      "totalResourcesCount": "long",
      "nonCompliantResourcesCount": "long",
      "errorCode": "string",
      "message": "string"
    }
  }
}
```

| CLI output fields              | Name                                                            | Type                                                                                                                                                                                | Description                 |
| ------------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------- | ----------------------- | ----------------------- | ------ |
| taskStatus                     | string                                                          | The status of the audit: one of IN_PROGRESS, COMPLETED, FAILED, or<br>CANCELED.<br>enum: IN_PROGRESS                                                                                | COMPLETED                   | FAILED   | CANCELED                |
| taskType                       | string                                                          | The type of audit: ON_DEMAND_AUDIT_TASK or SCHEDULED_AUDIT_TASK.<br>enum: ON_DEMAND_AUDIT_TASK                                                                                      | SCHEDULED_AUDIT_TASK        |
| taskStartTime                  | timestamp                                                       | The time the audit started.                                                                                                                                                         |
| taskStatistics                 | TaskStatistics                                                  | Statistical information about the audit.                                                                                                                                            |
| totalChecks                    | integer                                                         | The number of checks in this audit.                                                                                                                                                 |
| inProgressChecks               | integer                                                         | The number of checks in progress.                                                                                                                                                   |
| waitingForDataCollectionChecks | integer                                                         | The number of checks waiting for data collection.                                                                                                                                   |
| compliantChecks                | integer                                                         | The number of checks that found compliant resources.                                                                                                                                |
| nonCompliantChecks             | integer                                                         | The number of checks that found noncompliant resources.                                                                                                                             |
| failedChecks                   | integer                                                         | The number of checks.                                                                                                                                                               |
| canceledChecks                 | integer                                                         | The number of checks that did not run because the audit was<br>canceled.                                                                                                            |
| scheduledAuditName             | string<br>length<br>• max:128 min:1<br>pattern: [a-zA-Z0-9\_-]+ | The name of the scheduled audit (only if the audit was a scheduled<br>audit).                                                                                                       |
| auditDetails                   | map                                                             | Detailed information about each check performed during this<br>audit.                                                                                                               |
| checkRunStatus                 | string                                                          | The completion status of this check, one of IN_PROGRESS,<br>WAITING_FOR_DATA_COLLECTION, CANCELED, COMPLETED_COMPLIANT,<br>COMPLETED_NON_COMPLIANT, or FAILED.<br>enum: IN_PROGRESS | WAITING_FOR_DATA_COLLECTION | CANCELED | <br>COMPLETED_COMPLIANT | COMPLETED_NON_COMPLIANT | FAILED |
| checkCompliant                 | boolean                                                         | True if the check completed and found all resources compliant.                                                                                                                      |
| totalResourcesCount            | long                                                            | The number of resources on which the check was performed.                                                                                                                           |
| nonCompliantResourcesCount     | long                                                            | The number of resources that the check found noncompliant.                                                                                                                          |
| errorCode                      | string                                                          | The code of any error encountered when performing this check during this<br>audit. One of INSUFFICIENT_PERMISSIONS or AUDIT_CHECK_DISABLED.                                         |
| message                        | string<br>length<br>• max:2048                                  | The message associated with any error encountered when performing this check<br>during this audit.                                                                                  |

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ResourceNotFoundException`

The specified resource does not exist.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

### ListAuditTasks

Lists the Device Defender audits that have been performed during a given time
period.

**Synopsis**

```
aws iot  list-audit-tasks \
    --start-time <value> \
    --end-time <value> \
    [--task-type <value>] \
    [--task-status <value>] \
    [--next-token <value>] \
    [--max-results <value>]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "startTime": "timestamp",
  "endTime": "timestamp",
  "taskType": "string",
  "taskStatus": "string",
  "nextToken": "string",
  "maxResults": "integer"
}
```

| `cli-input-json` Fields | Name                                | Type                                                                                                                                                                                            | Description          |
| ----------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------ | -------- |
| startTime               | timestamp                           | The beginning of the time period. Audit information is retained for a limited<br>time (180 days). Requesting a start time prior to what is retained results in an<br>`InvalidRequestException`. |
| endTime                 | timestamp                           | The end of the time period.                                                                                                                                                                     |
| taskType                | string                              | A filter to limit the output to the specified type of audit: can be one of<br>ON_DEMAND_AUDIT_TASK or SCHEDULED\_\_AUDIT_TASK.<br>enum: ON_DEMAND_AUDIT_TASK                                    | SCHEDULED_AUDIT_TASK |
| taskStatus              | string                              | A filter to limit the output to audits with the specified completion status:<br>can be one of IN_PROGRESS, COMPLETED, FAILED, or CANCELED.<br>enum: IN_PROGRESS                                 | COMPLETED            | FAILED | CANCELED |
| nextToken               | string                              | The token for the next set of results.                                                                                                                                                          |
| maxResults              | integer<br>range<br>• max:250 min:1 | The maximum number of results to return at one time. The default is<br>25.                                                                                                                      |

Output

```
{
  "tasks": [
    {
      "taskId": "string",
      "taskStatus": "string",
      "taskType": "string"
    }
  ],
  "nextToken": "string"
}
```

| CLI output fields | Name                                                            | Type                                                                                                           | Description          |
| ----------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------- | ------ | -------- |
| tasks             | list<br>member: AuditTaskMetadata<br>java class: java.util.List | The audits that were performed during the specified time<br>period.                                            |
| taskId            | string<br>length<br>• max:40 min:1<br>pattern: [a-zA-Z0-9-]+    | The ID of this audit.                                                                                          |
| taskStatus        | string                                                          | The status of this audit: one of IN_PROGRESS, COMPLETED, FAILED, or<br>CANCELED.<br>enum: IN_PROGRESS          | COMPLETED            | FAILED | CANCELED |
| taskType          | string                                                          | The type of this audit: one of ON_DEMAND_AUDIT_TASK or<br>SCHEDULED_AUDIT_TASK.<br>enum: ON_DEMAND_AUDIT_TASK  | SCHEDULED_AUDIT_TASK |
| nextToken         | string                                                          | A token that can be used to retrieve the next set of results, or<br>`null` if there are no additional results. |

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

### CancelAuditTask

Cancels an audit that is in progress. The audit can be either scheduled or on-demand. If
the audit is not in progress, an `InvalidRequestException` occurs.

**Synopsis**

```
aws iot  cancel-audit-task \
    --task-id <value>  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "taskId": "string"
}
```

| `cli-input-json` Fields | Name                                                         | Type                                                                                         | Description |
| ----------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ----------- |
| taskId                  | string<br>length<br>• max:40 min:1<br>pattern: [a-zA-Z0-9-]+ | The ID of the audit you want to cancel. You can only cancel an audit that is<br>IN_PROGRESS. |

Output

None

**Errors**

`ResourceNotFoundException`

The specified resource does not exist.

`InvalidRequestException`

The contents of the request were invalid.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.

## Check audit results

Use `ListAuditFindings` to see the results of an audit. You can filter the
results by the type of check, a specific resource, or the time of the audit. You can use this
information to mitigate any problems that were found.

You can define mitigation actions and apply them to the findings from your audit. For more
information, see [Mitigation actions](dd-mitigation-actions.md "dd-mitigation-actions.md").

### ListAuditFindings

Lists the findings (results) of a Device Defender audit or of the audits performed
during a specified time period. (Findings are retained for 180 days.)

**Synopsis**

```
aws iot  list-audit-findings \
    [--task-id <value>] \
    [--check-name <value>] \
    [--resource-identifier <value>] \
    [--max-results <value>] \
    [--next-token <value>] \
    [--start-time <value>] \
    [--end-time <value>]  \
    [--cli-input-json <value>] \
    [--generate-cli-skeleton]
```

`cli-input-json` format

```
{
  "taskId": "string",
  "checkName": "string",
  "resourceIdentifier": {
    "deviceCertificateId": "string",
    "caCertificateId": "string",
    "cognitoIdentityPoolId": "string",
    "clientId": "string",
    "policyVersionIdentifier": {
      "policyName": "string",
      "policyVersionId": "string"
    },

    "roleAliasArn": "string",
    "account": "string"
  },
  "maxResults": "integer",
  "nextToken": "string",
  "startTime": "timestamp",
  "endTime": "timestamp"
}
```

| `cli-input-json` Fields | Name                                                              | Type                                                                                                                                                  | Description |
| ----------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| taskId                  | string<br>length<br>• max:40 min:1<br>pattern: [a-zA-Z0-9-]+      | A filter to limit results to the audit with the specified ID. You must specify<br>either the taskId or the startTime and endTime, but not both.       |
| checkName               | string                                                            | A filter to limit results to the findings for the specified audit<br>check.                                                                           |
| resourceIdentifier      | ResourceIdentifier                                                | Information that identifies the noncompliant resource.                                                                                                |
| deviceCertificateId     | string<br>length<br>• max:64 min:64<br>pattern: (0x)?[a-fA-F0-9]+ | The ID of the certificate attached to the resource.                                                                                                   |
| caCertificateId         | string<br>length<br>• max:64 min:64<br>pattern: (0x)?[a-fA-F0-9]+ | The ID of the CA certificate used to authorize the certificate.                                                                                       |
| cognitoIdentityPoolId   | string                                                            | The ID of the Amazon Cognito identity pool.                                                                                                           |
| clientId                | string                                                            | The client ID.                                                                                                                                        |
| policyVersionIdentifier | PolicyVersionIdentifier                                           | The version of the policy associated with the resource.                                                                                               |
| policyName              | string<br>length<br>• max:128 min:1<br>pattern: [w+=,.@-]+        | The name of the policy.                                                                                                                               |
| policyVersionId         | string<br>pattern: [0-9]+                                         | The ID of the version of the policy associated with the resource.                                                                                     |
| roleAliasArn            | string                                                            | The ARN of the role alias that has overly permissive actions.<br>length<br>• max:2048 min:1                                                           |
| account                 | string<br>length<br>• max:12 min:12<br>pattern: [0-9]+            | The account with which the resource is associated.                                                                                                    |
| maxResults              | integer<br>range<br>• max:250 min:1                               | The maximum number of results to return at one time. The default is 25.                                                                               |
| nextToken               | string                                                            | The token for the next set of results.                                                                                                                |
| startTime               | timestamp                                                         | A filter to limit results to those found after the specified time. You must<br>specify either the startTime and endTime or the taskId, but not both.  |
| endTime                 | timestamp                                                         | A filter to limit results to those found before the specified time. You must<br>specify either the startTime and endTime or the taskId, but not both. |

Output

```
{
  "findings": [
    {
      "taskId": "string",
      "checkName": "string",
      "taskStartTime": "timestamp",
      "findingTime": "timestamp",
      "severity": "string",
      "nonCompliantResource": {
        "resourceType": "string",
        "resourceIdentifier": {
          "deviceCertificateId": "string",
          "caCertificateId": "string",
          "cognitoIdentityPoolId": "string",
          "clientId": "string",
          "policyVersionIdentifier": {
            "policyName": "string",
            "policyVersionId": "string"
          },
          "account": "string"
        },
        "additionalInfo": {
          "string": "string"
        }
      },
      "relatedResources": [
        {
          "resourceType": "string",
          "resourceIdentifier": {
            "deviceCertificateId": "string",
            "caCertificateId": "string",
            "cognitoIdentityPoolId": "string",
            "clientId": "string",

            "iamRoleArn": "string",

            "policyVersionIdentifier": {
              "policyName": "string",
              "policyVersionId": "string"
            },
            "account": "string"
          },

          "roleAliasArn": "string",

          "additionalInfo": {
            "string": "string"
          }
        }
      ],
      "reasonForNonCompliance": "string",
      "reasonForNonComplianceCode": "string"
    }
  ],
  "nextToken": "string"
}
```

| CLI output fields          | Name                                                              | Type                                                                                                           | Description    |
| -------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------- | ---------- | ------------------------- | --------- | ---------------- |
| findings                   | list<br>member: AuditFinding                                      | The findings (results) of the audit.                                                                           |
| taskId                     | string<br>length<br>• max:40 min:1<br>pattern: [a-zA-Z0-9-]+      | The ID of the audit that generated this result (finding).                                                      |
| checkName                  | string                                                            | The audit check that generated this result.                                                                    |
| taskStartTime              | timestamp                                                         | The time the audit started.                                                                                    |
| findingTime                | timestamp                                                         | The time the result (finding) was discovered.                                                                  |
| severity                   | string                                                            | The severity of the result (finding).<br>enum: CRITICAL                                                        | HIGH           | MEDIUM     | LOW                       |
| nonCompliantResource       | NonCompliantResource                                              | The resource that was found to be noncompliant with the audit check.                                           |
| resourceType               | string                                                            | The type of the noncompliant resource.<br>enum: DEVICE_CERTIFICATE                                             | CA_CERTIFICATE | IOT_POLICY | <br>COGNITO_IDENTITY_POOL | CLIENT_ID | ACCOUNT_SETTINGS |
| resourceIdentifier         | ResourceIdentifier                                                | Information that identifies the noncompliant resource.                                                         |
| deviceCertificateId        | string<br>length<br>• max:64 min:64<br>pattern: (0x)?[a-fA-F0-9]+ | The ID of the certificate attached to the resource.                                                            |
| caCertificateId            | string<br>length<br>• max:64 min:64<br>pattern: (0x)?[a-fA-F0-9]+ | The ID of the CA certificate used to authorize the certificate.                                                |
| cognitoIdentityPoolId      | string                                                            | The ID of the Amazon Cognito identity pool.                                                                    |
| clientId                   | string                                                            | The client ID.                                                                                                 |
| policyVersionIdentifier    | PolicyVersionIdentifier                                           | The version of the policy associated with the resource.                                                        |
| policyName                 | string<br>length<br>• max:128 min:1<br>pattern: [w+=,.@-]+        | The name of the policy.                                                                                        |
| policyVersionId            | string<br>pattern: [0-9]+                                         | The ID of the version of the policy associated with the resource.                                              |
| account                    | string<br>length<br>• max:12 min:12<br>pattern: [0-9]+            | The account with which the resource is associated.                                                             |
| additionalInfo             | map                                                               | Other information about the noncompliant resource.                                                             |
| relatedResources           | list<br>member: RelatedResource                                   | The list of related resources.                                                                                 |
| resourceType               | string                                                            | The type of resource.<br>enum: DEVICE_CERTIFICATE                                                              | CA_CERTIFICATE | IOT_POLICY | <br>COGNITO_IDENTITY_POOL | CLIENT_ID | ACCOUNT_SETTINGS |
| resourceIdentifier         | ResourceIdentifier                                                | Information that identifies the resource.                                                                      |
| deviceCertificateId        | string<br>length<br>• max:64 min:64<br>pattern: (0x)?[a-fA-F0-9]+ | The ID of the certificate attached to the resource.                                                            |
| caCertificateId            | string<br>length<br>• max:64 min:64<br>pattern: (0x)?[a-fA-F0-9]+ | The ID of the CA certificate used to authorize the certificate.                                                |
| cognitoIdentityPoolId      | string                                                            | The ID of the Amazon Cognito identity pool.                                                                    |
| clientId                   | string                                                            | The client ID.                                                                                                 |
| policyVersionIdentifier    | PolicyVersionIdentifier                                           | The version of the policy associated with the resource.                                                        |
| iamRoleArn                 | string<br>length<br>• max:2048 min:20                             | The ARN of the IAM role that has overly permissive actions.                                                    |
| policyName                 | string<br>length<br>• max:128 min:1<br>pattern: [w+=,.@-]+        | The name of the policy.                                                                                        |
| policyVersionId            | string<br>pattern: [0-9]+                                         | The ID of the version of the policy associated with the resource.                                              |
| roleAliasArn               | string<br>length<br>• max:2048 min:1                              | The ARN of the role alias that has overly permissive actions.                                                  |
| account                    | string<br>length<br>• max:12 min:12<br>pattern: [0-9]+            | The account with which the resource is associated.                                                             |
| additionalInfo             | map                                                               | Other information about the resource.                                                                          |
| reasonForNonCompliance     | string                                                            | The reason the resource was noncompliant.                                                                      |
| reasonForNonComplianceCode | string                                                            | A code that indicates the reason that the resource was noncompliant.                                           |
| nextToken                  | string                                                            | A token that can be used to retrieve the next set of results, or<br>`null` if there are no additional results. |

**Errors**

`InvalidRequestException`

The contents of the request were invalid.

`ThrottlingException`

The rate exceeds the limit.

`InternalFailureException`

An unexpected error has occurred.
