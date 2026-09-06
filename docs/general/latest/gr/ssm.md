

# AWS Systems Manager endpoints and quotas
<a name="ssm"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

**Related services**  
For information about endpoints and quotas for related services, see the following topics:
+ [AWS AppConfig endpoints and quotas](appconfig.md)
+ [AWS Systems Manager Incident Manager endpoints and quotas](incident-manager.md)
+ [Systems Manager Quick Setup endpoints and quotas](quick-setup.md)
+ [AWS Systems Manager for SAP endpoints and quotas](ssm-sap.md)

## Service endpoints for Systems Manager
<a name="ssm_region"></a>

**Note**  
In addition to the `ssm.*` endpoints documented in the following table, your managed nodes must also allow HTTPS (port 443) outbound traffic to the following endpoints.  
`ec2messages.*`
`ssmmessages.*`
For more information, see [Reference: ec2messages, ssmmessages, and other API operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html) in the *AWS Systems Manager User Guide*.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  ssm.us-east-2.amazonaws.com <br /> ssm-fips.us-east-2.amazonaws.com <br /> ssm-fips.us-east-2.api.aws <br /> ssm.us-east-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  ssm.us-east-1.amazonaws.com <br /> ssm-fips.us-east-1.amazonaws.com <br /> ssm-fips.us-east-1.api.aws <br /> ssm.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  ssm.us-west-1.amazonaws.com <br /> ssm-fips.us-west-1.amazonaws.com <br /> ssm-fips.us-west-1.api.aws <br /> ssm.us-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  ssm.us-west-2.amazonaws.com <br /> ssm-fips.us-west-2.amazonaws.com <br /> ssm-fips.us-west-2.api.aws <br /> ssm.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  ssm.af-south-1.amazonaws.com <br /> ssm.af-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  ssm.ap-east-1.amazonaws.com <br /> ssm.ap-east-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  ssm.ap-south-2.amazonaws.com <br /> ssm.ap-south-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  ssm.ap-southeast-3.amazonaws.com <br /> ssm.ap-southeast-3.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  ssm.ap-southeast-5.amazonaws.com <br /> ssm.ap-southeast-5.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  ssm.ap-southeast-4.amazonaws.com <br /> ssm.ap-southeast-4.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  ssm.ap-south-1.amazonaws.com <br /> ssm.ap-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (New Zealand) | ap-southeast-6 |  ssm.ap-southeast-6.amazonaws.com <br /> ssm.ap-southeast-6.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  ssm.ap-northeast-3.amazonaws.com <br /> ssm.ap-northeast-3.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  ssm.ap-northeast-2.amazonaws.com <br /> ssm.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  ssm.ap-southeast-1.amazonaws.com <br /> ssm.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  ssm.ap-southeast-2.amazonaws.com <br /> ssm.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  ssm.ap-east-2.amazonaws.com <br /> ssm.ap-east-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  ssm.ap-southeast-7.amazonaws.com <br /> ssm.ap-southeast-7.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  ssm.ap-northeast-1.amazonaws.com <br /> ssm.ap-northeast-1.api.aws  | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  ssm.ca-central-1.amazonaws.com <br /> ssm-fips.ca-central-1.amazonaws.com <br /> ssm-fips.ca-central-1.api.aws <br /> ssm.ca-central-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Canada West (Calgary) | ca-west-1 |  ssm.ca-west-1.amazonaws.com <br /> ssm-fips.ca-west-1.amazonaws.com <br /> ssm-fips.ca-west-1.api.aws <br /> ssm.ca-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  ssm.eu-central-1.amazonaws.com <br /> ssm.eu-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  ssm.eu-west-1.amazonaws.com <br /> ssm.eu-west-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  ssm.eu-west-2.amazonaws.com <br /> ssm.eu-west-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Milan) | eu-south-1 |  ssm.eu-south-1.amazonaws.com <br /> ssm.eu-south-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Paris) | eu-west-3 |  ssm.eu-west-3.amazonaws.com <br /> ssm.eu-west-3.api.aws  | HTTPS<br />HTTPS | 
| Europe (Spain) | eu-south-2 |  ssm.eu-south-2.amazonaws.com <br /> ssm.eu-south-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Stockholm) | eu-north-1 |  ssm.eu-north-1.amazonaws.com <br /> ssm.eu-north-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Zurich) | eu-central-2 |  ssm.eu-central-2.amazonaws.com <br /> ssm.eu-central-2.api.aws  | HTTPS<br />HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  ssm.il-central-1.amazonaws.com <br /> ssm.il-central-1.api.aws  | HTTPS<br />HTTPS | 
| Mexico (Central) | mx-central-1 |  ssm.mx-central-1.amazonaws.com <br /> ssm.mx-central-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (Bahrain) | me-south-1 |  ssm.me-south-1.amazonaws.com <br /> ssm.me-south-1.api.aws  | HTTPS<br />HTTPS | 
| Middle East (UAE) | me-central-1 |  ssm.me-central-1.amazonaws.com <br /> ssm.me-central-1.api.aws  | HTTPS<br />HTTPS | 
| South America (São Paulo) | sa-east-1 |  ssm.sa-east-1.amazonaws.com <br /> ssm.sa-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-East) | us-gov-east-1 |  ssm.us-gov-east-1.amazonaws.com <br /> ssm.us-gov-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  ssm.us-gov-west-1.amazonaws.com <br /> ssm.us-gov-west-1.api.aws  | HTTPS<br />HTTPS | 

## Service quotas
<a name="limits_ssm"></a>

The following sections list and describe the quotas for Systems Manager, grouped by tool or feature area.

Unless otherwise specified, each quota applies to an individual AWS Region in each AWS account. For example, the default quota for the number of State Manager associations is 2,000. This means that in the AWS account 123456789012, you can create 2,000 associations in the US East (N. Virginia) Region, 2,000 in the US East (Ohio) Region, and so on.

**Topics**
+ [Service quotas for Application Manager](#application-manager)
+ [Service quotas for Automation](#automation)
+ [Service quotas for Distributor](#distributor)
+ [Service quotas for Documents](#documents)
+ [Service quotas for Explorer](#explorer)
+ [Service quotas for Fleet Manager / AWS Systems Manager GUI Connect](#fleet-manager)
+ [Service quotas for Inventory](#inventory)
+ [Service quotas for Maintenance Windows](#maintenance-windows)
+ [Service quotas for Managed nodes](#managed-nodes)
+ [Service quotas for OpsCenter](#opscenter)
+ [Service quotas for Parameter Store](#parameter-store)
+ [Service quotas for Patch Manager](#patch-manager)
+ [Service quotas for Session Manager](#session-manager)
+ [Service quotas for State Manager](#state-manager)

### Service quotas for Application Manager
<a name="application-manager"></a>


| Resource | Default | 
| --- | --- | 
| Maximum number of applications in Application Manager | 100<br />When you add an application in Application Manager, Systems Manager automatically creates a resource group to organize all of the resources for that application. The maximum number of applications is based on the underlying quota for AWS Resource Groups. | 
| Maximum number of AWS resources assigned to an application | For applications based on AWS CloudFormation stacks: 200<br />For applications based on AWS Resource Groups: Unlimited | 

### Service quotas for Automation
<a name="automation"></a>


| Resource | Default | 
| --- | --- | 
| Concurrently running automations | 100<br />This quota can be increased up to 500 by enabling adaptive concurrency. <br />Additionally, you can run up to 400 concurrent automations with blocking actions. Blocking actions include `aws:approve`, `aws:pause`, and `aws:sleep`. If you attempt to run more automations than this, Systems Manager adds the additional automations to a queue and displays a status of `Pending`. <br />For more information about adaptive concurrency, see [Allowing Automation to adapt to your concurrency needs](https://docs.aws.amazon.com/systems-manager/latest/userguide/adaptive-concurrency.html) in the *AWS Systems Manager User Guide*. | 
| Automation queue | 5,000<br />If you attempt to run more automations than the concurrent automation limit, subsequent automations are added to the Automation queue. When an automation completes (or reaches a terminal state), the first automation in the queue is started. | 
| Concurrently running rate control automations | 25<br />If you attempt to run more rate control automations than the concurrent rate control automation limit, Systems Manager adds the subsequent rate control automations to the queue and displays a status of `Pending`. | 
| Rate control automation queue | 1,000<br />If you attempt to run more automations than the concurrent rate control automation limit, subsequent automations are added to the queue. When an automation completes (or reaches a terminal state), the first automation in the queue is started. | 
| Number of levels of nested automation | 5<br />A parent-level Automation runbook can start a child-level Automation runbook. This represents one level of nested automation. The child-level Automation runbook can start another Automation runbook, resulting in two levels of nested automation. This can continue up to a maximum of five levels below the top-level parent Automation runbook. | 
| Number of days an automation execution history is stored in the system | 30 | 
| Number of days an automation variable is stored in the system | 30 | 
| Additional automation executions that can be queued | 1,000 | 
| Maximum duration an automation execution can run in the context of a user | 12 hours<br />If you expect an automation to run longer than 12 hours, then you must run the automation by using a service role (or assume role). | 
| Maximum executeScript action run time | 10 minutes<br />Each `executeScript` action can run up to a maximum duration of 10 minutes. | 
| Maximum executeScript action maximum output | 100 KB | 
| Maximum invokeLambdaFunction action run time | 5 minutes<br />Each `invokeLambdaFunction` action can run up to a maximum duration of five (5) minutes. | 
| Maximum invokeLambdaFunction action output | 200 KB | 
| Number of Automation runbook attachments | 5 per runbook | 
| Size of an Automation runbook attachment | 256 MB per attachment, per runbook<br /> | 
| Transactions per second for the [StartAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAutomationExecution.html) API action | 1 | 
| Transactions per second for the [DescribeAutomationStepExecutions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAutomationStepExecutions.html) API action | 3 | 
| Transactions per second for the [GetAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetAutomationExecution.html) API action | 3 | 
| Transactions per second for the [DescribeAutomationExecutions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAutomationExecutions.html) API action | 3 | 
| Transactions per second for the [SendAutomationSignal](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendAutomationSignal.html) API action | 3 | 
| Transactions per second for the [StopAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StopAutomationExecution.html) API action | 1 | 
| Transactions per second for the [StartExecutionPreview](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartExecutionPreview.html) API action | 1 | 
| Transactions per second for the [GetExecutionPreview](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetExecutionPreview.html) API action | 1 | 

### Service quotas for Distributor
<a name="distributor"></a>


| Resource | Default | 
| --- | --- | 
| Maximum number of attachments in a Distributor package | 20 | 
| Maximum size per attachment in a Distributor package | 1 GB | 
| Maximum number of files in a Distributor package | 1,000 | 
| Maximum number of Distributor packages | 500 | 
| Maximum number of package versions per Distributor package | 25 | 
| Maximum package size in Distributor | 20 GB | 
| Maximum package manifest size in Distributor | 64 KB | 

### Service quotas for Documents
<a name="documents"></a>


| Resource | Default | 
| --- | --- | 
| Document size | 64 KB per document | 
| Total documents | 500 | 
| Document versions | 1,000 per document | 
| Privately shared Systems Manager document | A single SSM document can be shared with a maximum of 1,000 AWS accounts. | 
| Publicly shared Systems Manager document | 5<br />Each AWS account can publicly share a maximum of five documents. | 
| Maximum number of favorites per document type | 20 | 

### Service quotas for Explorer
<a name="explorer"></a>


| Resource | Default | 
| --- | --- | 
| Maximum number of resource data syncs | 5 | 

### Service quotas for Fleet Manager / AWS Systems Manager GUI Connect
<a name="fleet-manager"></a>


| Resource | Default | 
| --- | --- | 
| Maximum number of Systems Manager GUI Connect concurrent Remote Desktop sessions | 5 ¹<br />Service quota increase requests up to 50 are automatically approved. Service quota increases can take up to two and a half hours to take effect. | 
| Maximum duration of an Systems Manager GUI Connect Remote Desktop session | 60 minutes | 
| Maximum idle time for a Systems Manager GUI Connect Remote Desktop session before connection timeout | 10 minutes | 
| Maximum connection persistence for a Systems Manager GUI Connect Remote Desktop session | 60 minutes (maximum connection duration) or 10 minutes (idle timeout limit).<br />A connection persists until the maximum connection duration (60 minutes) or idle timeout limit (10 minutes) is met. The connection persists after IAM credentials expire if the connection duration limits are not met.  | 

¹ The standard license for Windows Server allows for two concurrent RDP connections. To support more connections, you must purchase additional Client Access Licenses (CALs) from Microsoft or Microsoft Remote Desktop Services licenses from AWS. For more information on supplemental licensing, see the following topics:
+ [Client Access Licenses and Management Licenses](https://www.microsoft.com/en-us/licensing/product-licensing/client-access-license) on the Microsoft website
+ [Use License Manager user-based subscriptions for supported software products](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscriptions.html) in the *License Manager User Guide*

### Service quotas for Inventory
<a name="inventory"></a>


| Resource | Default | 
| --- | --- | 
| Maximum size of an inventory data item that can be sent in a single PutInventory API request, per managed node | 1024 KB | 
| Maximum number of resource data syncs | 5 | 
| Maximum size of inventory data collected per managed node, per call | 1 MB<br />This maximum adequately supports most inventory collection scenarios. When this quota is reached, no new inventory data is collected for the node. Inventory data previously collected is stored until the expiration. | 
| Maximum size of inventory data collected per node, per day | 5,000 KB<br />When this quota is reached, no new inventory data is collected for the instance. Inventory data previously collected is stored until the expiration. | 
| Number of custom inventory types | 20 | 
| Maximum size of a custom inventory type | 200 KB<br />This is the maximum size of the type, not the inventory collected. | 
| Maximum number of attributes in a custom inventory type | 50 | 
| Length of inventory data retention | 30 days<br />AWS Systems Manager Inventory retains managed node data for 30 days after the most recent inventory update. This retention quota applies to all managed node states, including stopped instances. The retention rules work this way:+  If a node remains in a stopped state or loses connection for 30 consecutive days without any inventory updates, the inventory data is automatically deleted after the 30-day period. <br />+  If that node becomes active again before the 30-day period expires (for example, if a stopped node is started) and new inventory data is reported successfully, the 30-day retention period resets from that point. <br />If you need to store inventory data longer than 30 days, you can use AWS Config to record history or periodically query and upload the data to an Amazon S3 bucket. For more information, see [Recording Software Configuration for Managed Instances](https://docs.aws.amazon.com/config/latest/developerguide/recording-managed-instance-inventory.html) in the *AWS Config Developer Guide*. | 

### Service quotas for Maintenance Windows
<a name="maintenance-windows"></a>


| Resource | Default | 
| --- | --- | 
| Maintenance windows | 50 | 
| Tasks per maintenance window | 20 | 
| Targets per maintenance window | 100 | 
| Targets per task | 10 | 
| Concurrent executions of maintenance windows | 5 | 

### Service quotas for Managed nodes
<a name="managed-nodes"></a>


| Resource | Default | 
| --- | --- | 
| Maximum number of managed nodes (Amazon EC2 and hybrid) in a fleet | 2,400<br />Approximate maximum number of nodes managed by Systems Manager (per AWS account per Region). Utilization up to the applied account level quota is considered safe. Exceeding this quota may cause instances to stop communicating with Systems Manager, but actual capacity varies.<br />**AWS default quota value**: The default fleet size quota is set at 2,400 managed nodes in Systems Manager. This is the default maximum safe limit for an AWS account. We do not recommend scaling past this without a limit increase because instances could stop communicating with Systems Manager. If you pass this limit, instances might be able to connect to Systems Manager, especially if you stagger node launches, but it's not certain.<br />**Applied account-level quota value**: The applied quota is the current regional limit for this account. This may be the default quota or an increased limit that has been approved by Support upon customer request. Exceeding the limit may cause instances to stop communicating with Systems Manager because connection attempts could exceed approved throughput.<br />**Utilization**: The utilized quota represents the approximate number of managed nodes currently active and communicating with Systems Manager. It is calculated based on the number of [UpdateInstanceInformation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html) API calls made within a five minute period of time. This number changes when instances are launched, terminated, or experience connectivity issues. The number also changes when SSM Agent is restarted. Customers may see greater than 100% utilization if instances are configured to call `UpdateInstanceInformation` API more frequently than the default five-minute interval or if instances launched within a five-minute window are staggered, resulting in distributed calls to the [UpdateInstanceInformation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html) API. | 
| Maximum number of hybrid-activated machines in a hybrid and multicloud environment | Standard instances: 1,000<br />Advanced instances: Advanced instances are available on a pay-per-use basis. Advanced instances also enable you to connect to your non-EC2 machines by using AWS Systems Manager Session Manager.<br /> For more information about activating non-EC2 machines for use in your hybrid and multicloud environment, see [Setting up Systems Manager for hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html#sysman-managed-instance-activation) in the *[AWS Systems Manager User Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/)*. For more information about enabling advanced instances, see [Configuring instance tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managed-instances-tiers.html). | 

### Service quotas for OpsCenter
<a name="opscenter"></a>


| Resource | Default | 
| --- | --- | 
| Maximum number of OpsItems (including Open *and* Resolved OpsItems) | 500,000  OpsItems that are created by an integration with AWS Security Hub CSPM are *not* currently limited by this maximum quota. It is therefore possible for Security Hub CSPM alerts to create more than 500,000 chargeable OpsItems in an account. <br />For high-production environments, we therefore recommend limiting the scope of Security Hub CSPM findings to high severity issues only. <br />For more information about OpsCenter integration with Security Hub CSPM and OpsItems pricing in AWS Systems Manager, see [Understanding OpsCenter integration with AWS Security Hub CSPM](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-applications-that-integrate.html#OpsCenter-integrate-with-security-hub) in the *AWS Systems Manager User Guide*.  | 
| Maximum number of OpsItems per AWS account per month | 10,000 | 
| Maximum operational data value size | 20 KB | 
| Maximum number of associated Automation runbooks per OpsItem | 10 | 
| Maximum number of Automation runbook executions stored in operational data under a single associated runbook | 10 | 
| Maximum number of related resources you can specify per OpsItem | 100 | 
| Maximum number of related OpsItems you can specify per OpsItem | 10 | 
| Maximum length of a deduplication string | 512 characters | 

### Service quotas for Parameter Store
<a name="parameter-store"></a>


| Resource | Default | 
| --- | --- | 
| Maximum number of parameters | Standard parameters: 10,000<br />Advanced parameters: 100,000 ¹<br /> | 
| Maximum size for parameter value | Standard parameter: 4 KB<br />Advanced parameter: 8 KB ¹ | 
| Maximum number of parameter policies per advanced parameter | 10 ¹ | 
| Maximum number of parameter versions retained | 100 | 
| Transactions per second for the following API Actions:+  [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html) <br />+  [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html) <br />+  [GetParametersByPath](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html)  |  +  Default: 40 <br />This default maximum of 40 TPS is shared by all three API actions. <br />+  Higher throughput enabled: ², ³   `GetParameter`: 10,000   `GetParameters`: 1,000   `GetParametersByPath`: 100     | 
| Transactions per second for the following API actions:+  [DeleteParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameter.html) <br />+  [DeleteParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameters.html)  |  +  Default: 3 <br />+  Higher throughput enabled: 5 ²   | 
| Transactions per second for the following API actions:+  [DescribeParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html) <br />+  [GetParameterHistory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameterHistory.html) <br />+  [LabelParameterVersion](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_LabelParameterVersion.html) <br />+  [UnlabelParameterVersion](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UnlabelParameterVersion.html) <br />+  [PutParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html)  |  +  Default: 3 <br />+  Higher throughput enabled: 10 ²   | 

¹ Enabling the advanced parameter tier incurs a charge on your AWS account. For more information, see [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html) in the *AWS Systems Manager User Guide*.

² You can raise the maximum transactions per second (TPS) for this API action to support applications and workloads that need concurrent access to multiple parameters. Increasing the TPS quota incurs a charge on your AWS account. For more information, see [Increasing or resetting Parameter Store throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html) in the *AWS Systems Manager User Guide*. 

³ Throughput for `SecureString` parameters might be further limited by AWS Key Management Service (AWS KMS) throughput limits depending on the Region. For more information about AWS KMS limits, see [ Request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) in the *AWS Key Management Service Developer Guide*.

### Service quotas for Patch Manager
<a name="patch-manager"></a>


| Resource | Default | 
| --- | --- | 
| Patch baselines | 50 | 
| Patch groups per patch baseline | 25 | 
| Operation history retention | Most recent 150 operations | 

### Service quotas for Session Manager
<a name="session-manager"></a>


| Resource | Default | 
| --- | --- | 
| Transactions per second for the [DescribeSessions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeSessions.html) API action | 6 | 
| Transactions per second for the [GetConnectionStatus](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetConnectionStatus.html) API action | 50 | 
| Transactions per second for the [ResumeSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResumeSession.html) API action | 6 | 
| Transactions per second for the [StartSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartSession.html) API action | 3 | 
| Transactions per second for the [TerminateSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_TerminateSession.html) API action | 6 | 
| Idle time before session termination | Default: 20 minutes<br />Configurable to between 1 and 60 minutes. | 
| Execution history retention | 30 days<br />The history of each command is available for up to 30 days. In addition, you can store a copy of all log files in Amazon Simple Storage Service or have an audit trail of all API calls in AWS CloudTrail. | 

### Service quotas for State Manager
<a name="state-manager"></a>


| Resource | Default | 
| --- | --- | 
| Transactions per second (TPS) for the [CreateAssociation ](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html) API action | 3 | 
| Transactions per second (TPS) for the [CreateAssociationBatch](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociationBatch.html) API action | 1 | 
| Transactions per second (TPS) for the [DeleteAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteAssociation.html) API action | 2 | 
| Transactions per second (TPS) for the [DescribeAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociation.html) API action | 2 | 
| Transactions per second (TPS) for the [DescribeAssociationExecutions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociationExecutions.html) API action | 4 | 
| Transactions per second (TPS) for the [DescribeAssociationExecutionTargets](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociationExecutionTargets.html) API action | 4 | 
| Transactions per second (TPS) for the [DescribeEffectiveInstanceAssociations](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeEffectiveInstanceAssociations.html) API action | 1 | 
| Transactions per second (TPS) for the [DescribeInstanceAssociationsStatus](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstanceAssociationsStatus.html) API action | 2 | 
| Transactions per second (TPS) for the [ListAssociations](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListAssociations.html) API action | 4 | 
| Transactions per second (TPS) for the [ListAssociationVersions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListAssociationVersions.html) API action | 4 | 
| Transactions per second (TPS) for the [StartAssociationsOnce](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAssociationsOnce.html) API action | 2 | 
| Transactions per second (TPS) for the [UpdateAssociation ](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateAssociation.html) API action | 3 | 
| Transactions per second (TPS) for the [UpdateAssociationStatus](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateAssociationStatus.html) API action | 3 | 
| Maximum number of associations | 2,000 | 
| Maximum number of versions per association | 1,000 | 
| Maximum number of associations targeting a single managed node | 20 | 