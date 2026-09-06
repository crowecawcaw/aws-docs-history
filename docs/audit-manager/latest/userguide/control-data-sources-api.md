

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# AWS API calls supported by AWS Audit Manager
<a name="control-data-sources-api"></a>



You can use Audit Manager to capture snapshots of your AWS environment as evidence for audits. When you create or edit a custom control, you can specify one or more AWS API calls as a data source mapping for evidence collection. Audit Manager then makes API calls to the relevant AWS services, and collects a snapshot of the configuration details for your AWS resources. 

For every resource that's in the scope of an API call, Audit Manager captures a configuration snapshot and converts it into evidence. This results in one piece of evidence per resource, as opposed to one piece of evidence per API call.

For example, if the `ec2_DescribeRouteTables` API call captures configuration snapshots from five route tables, then you'll get five pieces of evidence in total for the single API call. Each piece of evidence is a snapshot of the configuration of an individual route table.

**Topics**
+ [Key points](#control-data-sources-api-key-points)
+ [Supported API calls for custom control data sources](#apis-for-custom-control-data-sources)
+ [API calls used in the AWS License Manager standard framework](#apis-in-license-manager-framework)
+ [Additional resources](#using-api-calls-additional-resources)

## Key points
<a name="control-data-sources-api-key-points"></a>

### Paginated API calls
<a name="paginated-api-calls"></a>

Many AWS services collect and store a large amount of data. As a result, when a `list`, `describe`, or `get` API call attempts to return your data, there can be a lot of results. If the amount of data is too large to return in a single response, the results can be broken into more manageable pieces through the use of *pagination*. This divides the results into "pages" of data, making the responses easier to handle. 

Some of the [Supported API calls for custom control data sources](#apis-for-custom-control-data-sources) are paginated. This means that they return partial results at first, and require subsequent requests to return the entire result set. For example, the Amazon RDS [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) operation returns up to 100 instances at a time, and subsequent requests are needed to return the next page of results.

As of March 08, 2023, Audit Manager supports paginated API calls as a data source for evidence collection. Previously, if a paginated API call was used as a data source, only a subset of your resources was returned in the API response (up to 100 results). Now, Audit Manager calls the paginated API operation multiple times, and gets each page of results until all resources are returned. For each resource, Audit Manager then captures a configuration snapshot and saves it as evidence. Because your complete set of resources is now captured in the API response, it’s likely that you’ll notice an increase in the amount of evidence that’s collected after March 08, 2023. 

Audit Manager handles API call pagination for you automatically. If you create a custom control that uses a paginated API call as a data source, you don’t need to specify any pagination parameters. 

## Supported API calls for custom control data sources
<a name="apis-for-custom-control-data-sources"></a>

In your custom controls, you can use any of the following API calls as a data source. Audit Manager can then use these API calls to collect evidence about your AWS usage.


| Supported API call | How Audit Manager uses this API to collect evidence | 
| --- | --- | 
| [acm\_GetAccountConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_GetAccountConfiguration.html) | Collect a snapshot of the account configuration options associated with your AWS account. | 
| [acm\_ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html) | Retrieve a list of certificate ARNs and domain names.  | 
| [autoscaling\_DescribeAutoScalingGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html) | Collect a snapshot about the Auto Scaling groups in your AWS account. | 
| [backup\_ListBackupPlans](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupPlans.html) | Retrieve a list of all active backup plans in your AWS account.  | 
| [bedrock\_GetModelInvocationLoggingConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetModelInvocationLoggingConfiguration.html) | Collect a snapshot of the current configuration values for model invocation logging for models in your AWS account. | 
| [cloudfront\_ListDistributions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributions.html) | Retrieve a list of all distributions in your AWS account. | 
| [cloudtrail\_DescribeTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DescribeTrails.html) | Collect a snapshot of the settings for one or more trails associated with the current Region for your AWS account. | 
| [cloudtrail\_ListTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListTrails.html) | Retrieve a list of the trails that are in your AWS account.  | 
| [cloudwatch\_DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) | Collect a configuration snapshot of the alarms that are used for your AWS account. | 
| [config\_DescribeConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRules.html) | Retrieve details about your AWS Config rules. | 
| [config\_DescribeDeliveryChannels](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeDeliveryChannels.html) | Collect a configuration snapshot for the delivery channels in your in your AWS account. | 
| [directconnect\_DescribeDirectConnectGateways](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGateways.html) | Retrieve a list of all your Direct Connect gateways . | 
| [directconnect\_DescribeVirtualGateways](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualGateways.html) | Retrieve a list of the virtual private gateways owned by your AWS account. | 
| [docdb\_DescribeCertificates](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeCertificates.html) | Collect a list of certificates for your AWS account. | 
| [docdb\_DescribeDBClusterParameterGroups](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusterParameterGroups.html) | Collect a list of DBCLusterParameterGroup descriptions for your AWS account. | 
| [docdb\_DescribeDBInstances](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBInstances.html) | Collect information about provisioned Amazon DynamoDB instances for your AWS account. | 
| [cloudwatch\_DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) | Collect information about the alarms in your AWS account. | 
| [cloudtrail\_DescribeTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DescribeTrails.html) | Collect a snapshot of the settings for one or more trails associated with your AWS account. | 
| [dynamodb\_DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html) | Collect configuration snapshots for the DynamoDB tables in your AWS account.<br />When you use this API as a data source, you don't need to provide the name of a specific DynamoDB table. Instead, Audit Manager uses the `ListTables` operation to list all of your tables. For every table that's listed, Audit Manager then performs the `DescribeTable` operation to generate evidence for that resource. | 
| [dynamodb\_ListBackups](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBackups.html) | Retrieve a list of the DynamoDB backups that are associated with your AWS account. | 
| [dynamodb\_ListTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html) | Retrieve a list of all of the table names that are associated with your AWS account and your current endpoint. | 
| [ec2\_DescribeAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html) | Collect a snapshot of your Elastic IP addresses. | 
| [ec2\_DescribeCustomerGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCustomerGateways.html) | Collect a snapshot of your VPN customer gateways. | 
| [ec2\_DescribeEgressOnlyInternetGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeEgressOnlyInternetGateways.html) | Collect a snapshot of your egress-only internet gateways. | 
| [ec2\_DescribeFlowLogs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFlowLogs.html) | Collect a snapshot of your flow logs. | 
| [ec2\_DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) | Collect a snapshot of your instances. | 
| [ec2\_DescribeInternetGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInternetGateways.html) | Collect a snapshot of your internet gateways. | 
| [ec2\_DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.html) | Collect a description of the associations between the virtual interface groups and the local gateway route tables in your AWS account. | 
| [ec2\_DescribeLocalGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGateways.html) | Collect a snapshot of your local gateways. | 
| [ec2\_DescribeLocalGatewayVirtualInterfaces](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayVirtualInterfaces.html) | Collect a snapshot of your local gateway virtual interfaces. | 
| [ec2\_DescribeNatGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNatGateways.html) | Collect a snapshot of your NAT gateways. | 
| [ec2\_DescribeNetworkAcls](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkAcls.html) | Collect a snapshot of your network ACLs. | 
| [ec2\_DescribeRouteTables](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html) | Collect a snapshot of your route tables. | 
| [ec2\_DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html) | Collect a snapshot of your security groups. | 
| [ec2\_DescribeSecurityGroupRules](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroupRules.html) | Collect a snapshot of one or more of your security group rules. | 
| [ec2\_DescribeTransitGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html) | Collect a snapshot of your transit gateways. | 
| [ec2\_DescribeVolumes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html) | Collect a snapshot of your VPC endpoints. | 
| [ec2\_DescribeVpcs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html) | Collect a snapshot of your VPCs. | 
| [ec2\_DescribeVpcEndpoints](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.html) | Collect a snapshot of your VPC endpoints. | 
| [ec2\_DescribeVpcEndpointConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointConnections.html) | Collect a snapshot of the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance. | 
| [ec2\_DescribeVpcEndpointServiceConfigurations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServiceConfigurations.html) | Collect a snapshot of the VPC endpoint service configurations in your AWS account. | 
| [ec2\_DescribeVpcPeeringConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcPeeringConnections.html) | Collect a snapshot of your VPN connections. | 
| [ec2\_DescribeVpnConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html) | Collect a snapshot of your VPN connections. | 
| [ec2\_DescribeVpnGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html) | Collect a snapshot of your virtual private gateways. | 
| [ec2\_GetEbsDefaultKmsKeyId](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsDefaultKmsKeyId.html) | Collect a snapshot of the default AWS KMS key for EBS encryption for your AWS account in the current Region. | 
| [ec2\_GetEbsEncryptionByDefault](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsEncryptionByDefault.html) | Describe whether EBS encryption by default is enabled for your AWS account in the current Region. | 
| [ecs\_DescribeClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeClusters.html) | Collect a snapshot of your ECS clusters. | 
| [eks\_DescribeAddonVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html) | Collect a snapshot of your add-on versions. | 
| [elasticache\_DescribeCacheClusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheClusters.html) | Collect a snapshot of your provisioned clusters. | 
| [elasticache\_DescribeServiceUpdates](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeServiceUpdates.html) | Collect a snapshot of service updates for Amazon ElastiCache. | 
| [elasticfilesystem\_DescribeAccessPoints](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeAccessPoints.html) | Collect a snapshot of the Amazon EFS access points in your AWS account. | 
| [elasticfilesystem\_DescribeFileSystems](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeFileSystems.html) | Collect a snapshot of your Amazon EFS file systems. | 
| [elasticloadbalancingv2\_DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) | Collect a snapshot of the load balancers in your AWS account. | 
| [elasticloadbalancingv2\_DescribeSSLPolicies](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeSSLPolicies.html) | Collect a snapshot of the policies that you use for SSL negotiation. | 
| [elasticloadbalancingv2\_DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) | Collect a snapshot of your ELB target groups. | 
| [elasticmapreduce\_ListSecurityConfigurations](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSecurityConfigurations.html) | Retrieve a list of the security configurations that are visible to your AWS account, along with their creation dates and times, and their names. | 
| [events\_ListConnections](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListConnections.html) | Retrieve a list of the Amazon EventBridge connections in your AWS account. | 
| [events\_ListEventBuses](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEventBuses.html) | Retrieve a list of the Amazon EventBridge event buses in your AWS account, including the default event bus, custom event buses, and partner event buses. | 
| [events\_ListEventSources](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEventSources.html) | Retrieve a list of the partner event sources that have been shared with your AWS account.  | 
| [events\_ListRules](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListRules.html) | Retrieve a list of your Amazon EventBridge rules.  | 
| [firehose\_ListDeliveryStreams](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ListDeliveryStreams.html) | Retrieve a list of your delivery streams. | 
| [fsx\_DescribeFileSystems](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeFileSystems.html) | Collect a snapshot of the file systems that are owned by your AWS account. | 
| [guardduty\_ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) | Retrieve a list of the `detectorIds` for your Amazon GuardDuty detector resources. | 
| [iam\_GenerateCredentialReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateCredentialReport.html) | Generate a credential report for your AWS account. | 
| [iam\_GetAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html) | Collect a snapshot of the password policy for your AWS account. | 
| [iam\_GetAccountSummary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountSummary.html) | Collect a snapshot of the IAM entity usage and IAM quotas in your AWS account. | 
| [iam\_ListGroups](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroups.html) | Retrieve a list of the IAM groups that are associated with a path prefix that's available in your AWS account. | 
| [iam\_ListOpenIDConnectProviders](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html) | Retrieve a list of the IAM OpenID Connect (OIDC) provider resource objects that are defined in your AWS account. | 
| [iam\_ListPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html) | Retrieve a list of all the managed policies that are available in your AWS account, including your own customer-defined managed policies and all AWS managed policies. | 
| [iam\_ListRoles](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoles.html) | Retrieve a list of the IAM roles that are associated with a path prefix that's available in your AWS account. | 
| [iam\_ListSAMLProviders](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSAMLProviders.html) | Retrieve a list of the SAML provider resource objects defined in IAM in your AWS account.  | 
| [iam\_ListUsers](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html) | Retrieve a list of the IAM users in your AWS account. | 
| [iam\_ListVirtualMFADevices](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListVirtualMFADevices.html) | Retrieve a list of the virtual MFA devices that are defined in your AWS account. | 
| [kafka\_ListClusters](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clustersget) | Retrieve a list of the Amazon MSK clusters in your AWS account. | 
| [kafka\_ListKafkaVersions](https://docs.aws.amazon.com/msk/1.0/apireference/kafka-versions.html#kafka-versionsget) | Retrieve a list of the Apache Kafka version objects in your AWS account. | 
| [kinesis\_ListStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html) | Retrieve a list of your Kinesis data streams. | 
| [ kms\_GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html) | Audit Manager uses this API to collect a snapshot of the key policies for the AWS KMS keys in your AWS account.<br />When you use this API as a data source, you don't need to provide the name of a specific AWS KMS key. Instead, Audit Manager uses the `ListKeys` operation to list all of your KMS keys. For every KMS key that's listed, Audit Manager then performs the `GetKeyPolicy` operation to generate evidence for that resource. | 
| [ kms\_GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyRotationStatus.html) | Audit Manager uses this API to collect a snapshot of whether automatic rotation is enabled for the AWS KMS keys in your AWS account.<br />When you use this API as a data source, you don't need to provide the name of a specific AWS KMS key. Instead, Audit Manager uses the `ListKeys` operation to list all of your KMS keys. For every KMS key that's listed, Audit Manager then performs the `GetKeyRotationStatus` operation to generate evidence for that resource. | 
| [kms\_ListKeys](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) | Retrieve a list of the AWS KMS keys in your AWS account. | 
| [lambda\_ListFunctions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctions.html) | Retrieve a list of Lambda functions in your AWS account, with the version-specific configuration of each.  | 
| [rds\_DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) | Collect a snapshot of the existing Amazon Aurora DB clusters and Multi-AZ DB clusters in your AWS account. | 
| [rds\_DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) | Collect a snapshot of the provisioned RDS instances in your AWS account. | 
| [rds\_DescribeDbInstanceAutomatedBackups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstanceAutomatedBackups.html) | Collect a snapshot of the backups for both current and deleted instances in your AWS account. | 
| [rds\_DescribeDbSecurityGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSecurityGroups.html) | Collect a snapshot of the DBSecurityGroups in your AWS account. | 
| [redshift\_DescribeClusters](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusters.html) | Collect a snapshot of the provisioned Amazon Redshift clusters in your AWS account. | 
| [s3\_GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html) | Collect a snapshot that shows the default encryption configuration for your S3 buckets.<br />When you use this API as a data source, you don't need to provide the name of a specific S3 bucket. Instead, Audit Manager uses the `ListBuckets` operation to list the buckets that were created in the same AWS Region as your assessment. For every bucket that's listed, Audit Manager then performs the `GetBucketEncryption` operation to generate evidence for that resource.<br />Audit Manager can only provide the encryption status for buckets that were created in the same AWS Region as your assessment. If you need to see the encryption status of all your S3 buckets across multiple AWS Regions, we recommend that you create an assessment in each AWS Region where you have an S3 bucket. | 
| [s3\_ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html) | Retrieve a list of the S3 buckets in your AWS account. Audit Manager can only list buckets that were created in the same AWS Region as your assessment. If you need to see all your S3 buckets across multiple AWS Regions, we recommend that you create an assessment in each AWS Region where you have an S3 bucket. | 
| [sagemaker\_ListAlgorithms](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAlgorithms.html) | Retrieve a list of the machine learning algorithms in your AWS account. | 
| [sagemaker\_ListDomains](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListDomains.html) | Retrieve a list of the domains in your AWS account. | 
| [sagemaker\_ListEndpoints](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEndpoints.html) | Retrieve a list of the endpoints in your AWS account. | 
| [sagemaker\_ListEndpointConfigs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEndpointConfigs.html) | Retrieve a list of the endpoint configurations in your AWS account. | 
| [sagemaker\_ListFlowDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListFlowDefinitions.html) | Retrieve a list of the flow definitions in your AWS account. | 
| [sagemaker\_ListHumanTaskUis](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHumanTaskUis.html) | Retrieve a list of the human task interfaces in your AWS account. | 
| [sagemaker\_ListLabelingJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListLabelingJobs.html) | Retrieve a list of the labeling jobs in your AWS account. | 
| [sagemaker\_ListModels](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModels.html) | Retrieve a list of the models in your AWS account. | 
| [sagemaker\_ListModelBiasJobDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelBiasJobDefinitions.html) | Retrieve a list of the model bias job definitions in your AWS account. | 
| [sagemaker\_ListModelCards](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelCards.html) | Retrieve a list of the model cards in your AWS account. | 
| [sagemaker\_ListModelQualityJobDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelQualityJobDefinitions.html) | Retrieve a list of the model quality monitoring job definitions in your AWS account. | 
| [sagemaker\_ListMonitoringAlerts](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringAlerts.html) | Retrieve a list of the alerts for a given monitoring schedule. | 
| [sagemaker\_ListMonitoringSchedules](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringSchedules.html) | Retrieve a list of all monitoring schedules in your AWS account. | 
| [sagemaker\_ListTrainingJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrainingJobs.html) | Retrieve a list of training jobs in your AWS account. | 
| [sagemaker\_ListUserProfiles](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListUserProfiles.html) | Retrieve a list of user profiles in your AWS account. | 
| [secretsmanager\_ListSecrets](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html) | Retrieve a list of the secrets that are stored in your AWS account, not including secrets that are marked for deletion.  | 
| [sns\_ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) | Retrieve a list of the SNS topics in your AWS account. | 
| [sqs\_ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html) | Retrieve a list of the SQS queues in your AWS account. | 
| [waf-regional\_ListWebAcls](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListWebACLs.html) | Retrieve a list of the [WebACLSummary](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_WebACLSummary.html) objects for your AWS account. | 
| [waf-regional\_ListRules](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_ListRules.html) | Retrieve a list of the [RuleSummary](https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RuleSummary.html) objects for your AWS account. | 
| [waf\_ListRuleGroups](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListWebACLs.html) | Retrieve a list of the [RuleGroupSummary](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroupSummary.html) objects for the rule groups in your AWS account. | 
| [waf\_ListRules](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRules.html) | Retrieve a list of the [RuleSummary](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RuleSummary.html) objects for your AWS account. | 
| [waf\_ListWebAcls](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListWebACLs.html) | Retrieve a list of the [WebACLSummary](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_WebACLSummary.html) objects for your AWS account. | 

## API calls used in the AWS License Manager standard framework
<a name="apis-in-license-manager-framework"></a>

In the [AWS License Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/Licensemanager.html) standard framework, Audit Manager uses a custom activity called `GetLicenseManagerSummary` to collect evidence. This activity calls the following three License Manager APIs: 
+ [ListLicenseConfigurations](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseConfigurations.html)
+ [ListAssociationsForLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListAssociationsForLicenseConfiguration.html)
+ [ListUsageForLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListUsageForLicenseConfiguration.html) 

The data that’s returned is then converted into evidence and attached to the relevant controls in your assessment.

**Example**  
Let's say that you use two licensed products (*SQL Service 2017* and *Oracle Database Enterprise Edition*). First, the `GetLicenseManagerSummary` activity calls the [ListLicenseConfigurations](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseConfigurations.html) API, which provides details of license configurations in your account. Next, it adds additional contextual data for each license configuration by calling [ListUsageForLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListUsageForLicenseConfiguration.html) and [ListAssociationsForLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListAssociationsForLicenseConfiguration.html). Finally, it converts the license configuration data into evidence and attaches it to the respective controls in the framework (*4.5 - Customer managed license for SQL Server 2017* and *3.0.4 - Customer managed license for Oracle Database Enterprise Edition*). 

If you’re using a licensed product that isn’t covered by any of the controls in the framework, that license configuration data is attached as evidence to the following control: *5.0 - Customer managed license for other licenses*.

## Additional resources
<a name="using-api-calls-additional-resources"></a>
+ To find help with evidence collection issues for this data source type, see [My assessment isn’t collecting configuration data evidence for an AWS API call](evidence-collection-issues.md#no-evidence-from-aws-api-calls).
+ To create a custom control using this data source type, see [Creating a custom control in AWS Audit Manager](create-controls.md).
+ To create a custom framework that uses your custom control, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md). 
+ To add your custom control to an existing custom framework, see [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md).