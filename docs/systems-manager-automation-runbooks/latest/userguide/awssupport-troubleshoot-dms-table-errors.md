# `AWSSupport-TroubleshootDMSTableErrors`

**Description**

The AWS Systems Manager **AWSSuport-TroubleshootDMSTableErrors** automation runbook helps
you to automate the troubleshooting process for `Table errors` found in Database
migration task or Serverless replication from AWS Database Migration Service. These errors occur when tables fail
to migrate from the source endpoint (source database) to the target endpoint (target
database) by the Database migration task or Serverless replication created in AWS DMS service.
This runbook analyzes the signature error messages from CloudWatch logs, specifically focusing on
task logs for traditional Database migration task and serverless logs for Serverless
replication. It also provides targeted suggestions and remediation steps for common error
messages encountered with `Table error` during AWS DMS migrations.

**How does it work?**

The runbook performs the following steps:

- Fetches information about the provided AWS DMS ARN, which can be either a Database
  migration task or a Serverless replication.
- Verifies if the provided AWS DMS resource has been started at least once by checking
  the `FreshStartDate` value in the DescribeReplicationTasks API (for
  Database migration task) and DescribeReplications API (for Serverless replication)
  response. If the resource has not started, the automation raises an error.
- If the resource has started, the automation checks for the tables in the
  `TableError` states using `TableStatistics` information.
  If no errors are found, the automation ends the workflow after displaying a message
  confirming no table errors found in the specified Database migration task or
  Serverless replication.
- If tables with `TableError` state are found, the automation checks if
  CloudWatch logging is enabled for the specified AWS DMS resource. If logging is not enabled,
  the automation ends the workflow after displaying a message indicating that logging
  is not enabled.

**Note:** CloudWatch logging is expected to be enabled, as
the automation relies on these logs to analyze and identify the issues with the
tables in `TableError` state.

- If logging is enabled, the automation analyzes the CloudWatch logs and generates a
  report for each table which is in `TableError` state. The report includes
  suggestions for common error message and provides relevant error logs to help
  identify and resolve issues preventing successful table migration from the AWS DMS
  source endpoint to AWS DMS target endpoint.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootDMSTableErrors "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootDMSTableErrors")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- DMSArn

Type: String

Description: (Required) ARN of the Database migration task or Serverless
replication

Allowed Pattern:
`^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):dms:[a-z0-9-]+:\d{12}:(task|replication-config):[a-zA-Z0-9-]+$`

- StartTimeRange

Type: String

Description: (Optional) This parameter defines the beginning of the time range for
CloudWatch logs analysis of the given Database Migration task or Serverless replication.
When provided, only logs generated from this specific time onward will be collected
and analyzed. Please note, there is a possibility that the workflow could timeout if
the time range between the `startDate` and `endDate` is too
long. The value should be provided in ISO 6081 date time format.

Allowed Pattern:
`^$|^(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2}):(\\d{2}):(\\d{2})\\.(\\d{3})Z$`

- EndTimeRange

Type: String

Description: (Optional) This parameter sets the end of the time range for CloudWatch log
analysis of the given Database migration task or Serverless replication. When
provided, only logs generated till this specific time will be collected and
analyzed. Please note, there is a possibility that the workflow could timeout if the
time range between the `startDate` and `endDate` is too long.
The value should be provided in ISO 6081 date time format.

Allowed Pattern:
`^$|^(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2}):(\\d{2}):(\\d{2})\\.(\\d{3})Z$`
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `dms:DescribeReplicationTasks`
- `dms:DescribeReplications`
- `dms:DescribeEndpoints`
- `dms:DescribeReplicationConfigs`
- `dms:DescribeTableStatistics`
- `dms:DescribeReplicationTableStatistics`
- `logs:FilterLogEvents`

**Example IAM Policy for the Automation Assume Role**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "dms:DescribeReplicationConfigs",
 "dms:DescribeEndpoints",
 "dms:DescribeReplicationTableStatistics",
 "dms:DescribeTableStatistics",
 "logs:FilterLogEvents",
 "dms:DescribeReplicationTasks",
 "dms:DescribeReplications"
 ],
 "Resource": "*"
 }
 ]
 }`

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootDMSTableErrors`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootDMSTableErrors/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootDMSTableErrors/description") in Systems Manager under
   Documents.
2. Select Execute automation.
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**

   The Amazon Resource Name (ARN) of the AWS AWS Identity and Access Management (IAM) role that
   allows Systems Manager Automation to perform the actions on your behalf. If no role is
   specified, Systems Manager Automation uses the permissions of the user who starts this
   runbook.
   - **DMSArn**

   ARN of the Database migration task or Serverless replication which has
   Table errors.
   - **StartTimeRange**

   (Optional) ISO 6081 date time format defining the start of the time range
   for analyzing CloudWatch logs of the given Database migration task or Serverless
   replication.
   - **EndTimeRange**

   (Optional) ISO 6081 date time format defining the end of the time range
   for analyzing CloudWatch logs of the given Database migration task or Serverless
   replication.

4. Select **Execute** button from bottom of the
   page.
5. The automation initiates.
6. The document performs the following steps:
   - **validateDMSInputTypeAndGatherDetails**

   Validates the given AWS DMS ARN input and gather the basic details of the
   Database migration task or Serverless replication which are required in the
   next steps.
   - **branchOnTableErrors**

   Branches the workflow based on the number of Table errors found in the
   above step. If count is greater than 0, then proceed to -
   `branchOnCWLoggingStatus` step. Else, proceed to -
   `outputNoTableErrors` step.
   - **outputNoTableErrors**

   Output a message stating that the table errors are not found in the given
   Database migration task or Serverless replication.
   - **branchOnCWLoggingStatus**

   Branches the workflow based on the CloudWatch logging status found in the above
   step. If enabled, then proceed to - `gatherTableDetails` step.
   Else, proceed to - `outputNoCWLoggingEnabled` step.
   - **outputNoCWLoggingEnabled**

   Outputs a message stating that the CloudWatch logging is not enabled in the
   given Database migration task or Serverless replication.
   - **gatherTableDetails**

   Gathers the `FullLoadEndTime` timestamps of the failed tables
   and calculate the timerange values to analyze the CloudWatch logs.
   - **analyzeCloudWatchLogs**

   Analyzes the logs found in CloudWatch log group based on the signature error
   messages and returns the report to User.

7. After the execution completes, review the Outputs section for the detailed results
   of the execution.
   - **Output of No Table errors found**

   If there are no table errors found in the provided Database migration task
   or Serverless replication, the automation shows the output stating the same.
   - **Output of No CloudWatch loggin enabled**

   If CloudWatch logging is not enabled in the provided Database migration task or
   Serverless replication, the automation shows the output stating the same and
   provides the steps to enable logging.
   - **Log analyasis report**

   Outputs a report that identifies tables in `Table error` state
   from either provided Database migration task or Serverless replication,
   differentiating between error types, listing the error messages encountered,
   and providing targeted remediation steps and suggestions for each identified
   table.

**References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootDMSTableErrors/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootDMSTableErrors/description")
- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
