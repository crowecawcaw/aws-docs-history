# Cross-account cross-Region log

centralization

Amazon CloudWatch Logs data centralization works with AWS Organizations to collect log data from multiple member
accounts into one data repository using cross-account and cross-region centralization rules.
You define the rules that automatically replicate log data from multiple accounts and
AWS Regions into a centralized account within your organization. This capability
streamlines log consolidation for improved centralized monitoring, analysis, and compliance
across your entire AWS infrastructure.

CloudWatch Logs data centralization offers configuration flexibility to meet operational and
security requirements, such as the ability to configure a backup region during rule setup
within the destination account to ensure increased resiliency. Additionally, you have full
control over encryption behavior for log groups copied from source accounts to handle data
originally encrypted with customer-managed KMS keys.

###### Note

The CloudWatch Logs centralization feature only processes new log data that arrives in source accounts
after you create the centralization rule. Historical log data (logs that existed before
rule creation) is not centralized.

## Data centralization concepts

Before you begin using CloudWatch Logs data centralization, familiarize yourself with the
following concepts:

**Centralization rule**

A configuration that defines how log data from source accounts and regions
is replicated to a destination account and region. Rules specify source
criteria and destination settings.

**Source account**

The AWS account where log data originates. Log events from source
accounts are replicated to the destination account based on the
centralization rules you define.

**Destination account**

The destination AWS account where replicated log data is stored. This
account serves as the centralized location for log analysis and
monitoring.

**Backup region**

An optional secondary region within the destination account where log data
can be replicated for increased resiliency and disaster recovery
purposes.

**Encryption in CloudWatch Logs**

Log group data is always encrypted in CloudWatch Logs. By default,
CloudWatch Logs uses server-side encryption with 256-bit Advanced Encryption
Standard Galois/Counter Mode (AES-GCM) to encrypt log data at rest. As an
alternative, you can use AWS Key Management Service for this encryption.
If you do, the encryption is done using an either an AWS owned KMS key or
a customer managed KMS key. KMS key Encryption using AWS KMS is enabled at
the log group level, by associating a KMS key with a log group, either when
you create the log group or after it exists. After you associate a KMS key
with a log group, all newly ingested data for the log group is encrypted
using this key. This data is stored in encrypted format throughout its
retention period. CloudWatch Logs decrypts this data whenever it is
requested. CloudWatch Logs must have permissions for the KMS key whenever
encrypted data is requested, such as when a log centralization rule is run
against a source account. If you are using customer managed KMS keys, update
the KMS keys associated with the source and destination log groups with the
tag `LogsManaged = true`. For more information, see [AWS
KMS keys](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the _AWS Key Management Service Developer
Guide_

## Setting up log centralization

To set up CloudWatch Logs Centralization, you need to configure centralization rules that define
how log data flows from log groups in source accounts to log groups in your destination
account.

Once the centralization rule is enabled and log events are being replicated to the
destination account, you can create metric, subscription, and account filters on centralized log
groups with enhanced filtering capabilities. These filters can target log events from
specific source accounts and regions, and can emit source account and region information
as metric dimensions. For more information, see [Creating metrics from log events using filters](MonitoringLogData.md "MonitoringLogData.md").

### Prerequisites

- AWS Organizations must be set up and the source and destination accounts must both
  belong to the organization.
- Trusted access must be enabled for CloudWatch, the management account and the
  destination account so provide access to the log data.

### Creating a centralization rule

Use the following procedure to create a centralization rule that replicates log
data from source accounts to your destination account.

###### To create a centralization rule

1.  Navigate to the CloudWatch console in the Management or Delegated Administrator
    account of the organization.
2.  Choose **Settings**.
3.  Navigate to the **Organization** tab.
4.  Choose **Configure rule**.
5.  Specify source details by setting the following fields, then choose
    **Next**:
    1.  **Centralization rule name**: Enter a unique name
        for the centralization rule.
    2.  **Source accounts**: Define source selection
        criteria to pick accounts from which telemetry data will be
        centralized. The selection criteria can include:

            * A list of member accounts in the organization
            * A list of organization units in the organization
            * The entire organization

        You can provide the selection criteria in two modes:

            * **Builder**: A click-based experience to
             generate the source selection criteria
            * **Editor**: A free-form text box to
             provide the source selection criteria

        Supported syntax for source selection criteria:

            * *Supported Keys:* OrganizationId |
             OrganizationUnitId | AccountId | \*
            * *Supported Operators:* = | IN |
             OR

    3.  **Source Regions**: Select a list of regions to
        look for the telemetry data to centralize.

6.  Specify destination details by setting the following fields, then choose
    **Next**:
    1. **Destination account**: Select an account in the
       organization that acts as a central destination for telemetry
       data.
    2. **Destination Region**: Select a primary region
       that stores a copy of the centralized telemetry data.
    3. **Backup Region**: Optionally select a region
       that stores a second copy of the centralized telemetry data.

7.  Specify telemetry data by setting the following fields, then choose
    **Next**:

        1. **Log groups**: Choose one of the following
         options:




        	* **All log groups**: Centralize logs from
        	 all log groups in the source accounts.
        	* **Filter log group**: Centralize logs
        	 from a subset of log groups in the source accounts, matching
        	 a log group selection criteria. You can provide the
        	 selection criteria in two modes:




        		+ **Builder**: A click-based
        		 experience to generate the log group selection
        		 criteria
        		+ **Editor**: A free-form text box
        		 to provide the log group selection criteria
        	Supported syntax for log group selection criteria:




        		+ *Supported Keys:* LogGroupName

    | \* + _Supported Operators:_ = | != | IN | NOT IN | AND | OR | LIKE | NOT LIKE 2. **KMS Encrypted Log Group** ###### Important CloudWatch centralization rules will fail to deliver logs from the source account to the destination log groups if the KMS Key provided in the Centralization rule doesn't permit CloudWatch Logs to use it. For more information, see [Step 2: Set permissions on the KMS key](CloudWatchLogs-Insights-Query-Encrypt.md#cmk-permissions "CloudWatchLogs-Insights-Query-Encrypt.md#cmk-permissions"). Choose one of the following options: <br>• **Do not centralize log groups encrypted with Customer Managed KMS keys**: Skip centralization of log events from source log groups encrypted with Customer Managed KMS Keys. <br>• **Centralize log groups encrypted with Customer Managed KMS keys in destination account with an AWS Managed KMS key**: Centralize log events from source log groups encrypted with Customer Managed KMS Keys into destination log groups that are not associated with Customer Managed KMS Keys but instead use an AWS Managed KMS key. When this setting is selected, you must also set the following: + **Destination encryption key ARN**: ARN of the KMS Key belonging to the destination account and the primary destination region, to be associated with newly created destination log groups. + **Backup destination encryption key ARN** (optional): ARN of the KMS Key belonging to the destination account and the backup destination region, to be associated with newly created destination log groups. ###### Note Note that this setting only applies when the source log group is encrypted using Customer Managed KMS Keys and only applies to newly created log groups in the destination account. 8. Review the centralization rule, optionally make any last-minute edits, and choose **Create Centralization policy**. ### Modifying a centralization rule Use the following procedure to modify an existing centralization rule. ###### To modify a centralization rule 1. Navigate to the CloudWatch console in the Management or Delegated Administrator account of the organization. 2. Choose **Settings**. 3. Navigate to the **Organization** tab. 4. Choose **Manage rules**. 5. Select the rule to update and choose **Edit**. 6. Update the rule configuration as needed, choosing **Next** to proceed through each step. 7. In Step 4, Review and configure, choose **Update centralization policy**. ### Viewing a centralization rule Use the following procedure to view details of an existing centralization rule. ###### To view a centralization rule 1. Navigate to the CloudWatch console in the Management or Delegated Administrator account of the organization. 2. Choose **Settings**. 3. Navigate to the **Organization** tab. 4. Choose **Manage rules**. 5. View a list of all existing centralization rules and choose a specific rule name to view its details. ### Deleting a centralization rule Use the following procedure to delete an existing centralization rule. ###### To delete a centralization rule 1. Navigate to the CloudWatch console in the Management or Delegated Administrator account of the organization. 2. Choose **Settings**. 3. Navigate to the **Organization** tab. 4. Choose **Manage rules**. 5. Select the rule to delete and choose **Delete**. 6. Confirm deletion and choose **Delete**. ## Monitoring centralization You can monitor the status and performance of your centralization rules using CloudWatch metrics, the CloudWatch Logs console, and AWS CloudTrail logs. This helps you ensure that log data is being replicated successfully and identify any issues with your centralization configuration. ### Monitoring centralization in the console Use the CloudWatch Logs console to view the status and activity of your centralization rules. ###### To monitor centralization rules in the console 1. Navigate to the CloudWatch console in the Management or Delegated Administrator account of the organization. 2. Choose **Settings**. 3. Navigate to the **Organization** tab. 4. Choose **Manage rules**. 5. Review the centralization rules list, which displays: <br>• **Rule name**: The name of each centralization rule <br>• **Rule status**: Current operational status (Active, Inactive, Error) <br>• **Creation date**: When the rule was created <br>• **Destination account ID**: The account ID of the destination account <br>• **Destination Region**: The Region of the destination account 6. Choose a specific rule name to view the rule configuration details ### Centralization monitoring You can monitor centralization rules using the console interface and API operations. Current monitoring capabilities include: <br>• _Rule health status_: Monitor the overall health of centralization rules through the console or `GetCentralizationRuleForOrganization` API <br>• _Rule configuration_: Review rule settings and last update timestamps <br>• _Failure reasons_: View detailed failure information when rules are marked as UNHEALTHY <br>• _API activity_: Track centralization API calls through CloudTrail logs ### Monitoring rule health Each centralization rule has a health status that indicates whether it's operating correctly. You can check rule health through the console or programmatically using the API. Rule health statuses include: <br>• `HEALTHY`: The rule is operating normally and replicating log data as configured <br>• `UNHEALTHY`: The rule has encountered issues and may not be replicating data correctly <br>• `PROVISIONING`: Centralization for the organization is in the process of being set up. When a rule is marked as UNHEALTHY, the `FailureReason` field provides details about the specific issue that needs to be addressed. ### Monitoring centralization API calls with AWS CloudTrail AWS CloudTrail logs API calls made to the centralization service, allowing you to track configuration changes and troubleshoot issues for accounts that are members of your AWS Organizations. Key CloudTrail events for centralization include: <br>• `CreateCentralizationRuleForOrganization`: When a new centralization rule is created <br>• `UpdateCentralizationRuleForOrganization`: When an existing rule is modified <br>• `DeleteCentralizationRuleForOrganization`: When a rule is deleted <br>• `GetCentralizationRuleForOrganization`: When rule details are retrieved <br>• `ListCentralizationRulesForOrganization`: When rules are listed You can use CloudTrail logs to audit centralization configuration changes and correlate them with performance issues or replication failures.
