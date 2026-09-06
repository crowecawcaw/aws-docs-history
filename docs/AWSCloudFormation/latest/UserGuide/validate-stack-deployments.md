

# Validate stack deployments
<a name="validate-stack-deployments"></a>

With pre-deployment validation, you can identify and resolve potential deployment issues before CloudFormation provisions resources. Pre-deployment validation runs automatically on Create Stack, Update Stack, and Create Change Set operations, catching common errors in seconds.

**Topics**
+ [How pre-deployment validation works](#validate-stack-deployments-how-it-works)
+ [Considerations](#validate-stack-deployments-considerations)
+ [Prerequisites](#validate-stack-deployments-prerequisites)
+ [Disable pre-deployment validation](#validate-stack-deployments-disable)
+ [Validate a stack deployment (console)](#validate-stack-deployments-console)
+ [Validate a stack deployment (AWS CLI)](#validate-stack-deployments-cli)
+ [Validation types](#validate-stack-deployments-validation-types)
+ [Resource limitations](#validate-stack-deployments-resource-limitations)

## How pre-deployment validation works
<a name="validate-stack-deployments-how-it-works"></a>

Pre-deployment validation involves these phases:

1. **Initiate a stack operation** – Create a stack, update a stack, or create a change set as you normally would. Pre-deployment validation is enabled by default on all three operations.

1. **Validation execution** – CloudFormation runs multiple validation checks against your template and target environment. CloudFormation supports six types of pre-deployment validation. Property syntax validation and resource name conflict detection run on all supported operations. Four additional validations run during change set creation only: S3 bucket emptiness validation, service quota checks, Recorder conflict detection, and ECR repository delete readiness.

1. **Review validation results** – CloudFormation provides detailed feedback on any issues found, including precise path pinpointing the issue location in template, eliminating manual template debugging.

1. **Resolve issues** – Address identified problems by updating your templates or resolving conflicts before proceeding with deployment.

1. **Execute with confidence** – Proceed with your deployment knowing that common failure scenarios have been validated upfront.

**Note**  
For Create Stack and Update Stack operations, validation runs as part of the operation itself. If validation fails in FAIL mode, the operation stops before any resources are provisioned and the stack status reflects the validation failure. For change sets, the change set status shows `FAILED`.

## Considerations
<a name="validate-stack-deployments-considerations"></a>

As you use pre-deployment validation, keep the following in mind:
+ Pre-deployment validation focuses on common deployment failure scenarios. It doesn't guarantee that your deployment will succeed, but reduces the likelihood of common failures.
+ Validation modes behave differently:
  + **FAIL mode** stops the operation before any resources are provisioned when validation detects errors. For CreateStack and UpdateStack, the operation fails and the stack status reflects the validation failure. For CreateChangeSet, the change set status shows FAILED. This applies to property syntax errors and resource naming conflicts.
  + **WARN mode** allows change set creation to succeed despite validation failures, providing warnings that developers can review and address before execution. This applies to constraint violations like S3 bucket emptiness that may be resolvable through manual intervention.
+ For change set operations, validation results are tied to the specific change set. If you modify your template, create a new change set to get updated validation results. For CreateStack and UpdateStack operations, use the `describe-events` command with the operation ID to access validation results.
+ S3 bucket validation only checks for object presence, not for bucket policies or other constraints that might prevent deletion.
+ Pre-deployment validation adds a small amount of latency to Create Stack and Update Stack operations while validations run. This is typically a few seconds. If you need to skip validation for a specific operation, use the `DisableValidation` parameter.

## Prerequisites
<a name="validate-stack-deployments-prerequisites"></a>

To use pre-deployment validation, you must have:
+ The necessary IAM permissions to create stacks, update stacks, or create change sets, and read resources in your account. The validation checks that run during change set creation require the following additional permissions:
  + **Service quota check** – `cloudwatch:GetMetricData`, `lambda:GetAccountSettings`, `servicequotas:GetServiceQuota`, `ec2:DescribeSecurityGroups`, and `iam:GetAccountSummary`
  + ** Recorder conflict check** – `config:ListConfigurationRecorders`
  + **S3 bucket emptiness and ECR repository checks** – `s3:ListBucketV2` and `ecr:ListImages`
+ Access to the AWS Regions where your stacks are deployed.
+ CloudFormation templates that you want to validate before deployment.

## Disable pre-deployment validation
<a name="validate-stack-deployments-disable"></a>

Pre-deployment validation runs by default. To skip validation for a specific operation, use the `DisableValidation` parameter.

Disable validation in the following situations:
+ When you have already validated your template through other means (such as `cfn-lint`, `cdk validate`, or CI checks)
+ When you need to minimize operation latency for time-sensitive deployments
+ When a known false positive is blocking your deployment and you need to proceed

AWS CLI examples:

```
aws cloudformation create-stack --stack-name {{MyStack}} --template-body file://template.yaml --disable-validation
```

```
aws cloudformation update-stack --stack-name {{MyStack}} --template-body file://template.yaml --disable-validation
```

API: Set the `DisableValidation` parameter to `true` on the `CreateStack` or `UpdateStack` API call.

**Note**  
Disabling validation means CloudFormation does not catch common errors until it attempts to provision resources.

## Validate a stack deployment (console)
<a name="validate-stack-deployments-console"></a>

Pre-deployment validation runs automatically on CreateStack and UpdateStack operations. No additional steps are required.

**To validate during stack creation or update**

1. Create or update your stack as you normally would.

1. If validation detects errors, the operation stops before provisioning begins. The stack status reflects the validation failure.

1. To review validation results, open the stack's **Events** tab and choose the operation ID—or choose the link in the banner or the **Status reason** column. The Operation view page opens directly on the **Deployment validations** tab, which shows validation details, including Logical ID, Resource type, Validation type, Mode, and Status reason.

1. Fix the identified issues in your template and retry the operation.

### Validate using a change set (console)
<a name="validate-stack-deployments-console-changeset"></a>

You can also use change sets to validate your template before deployment. Change sets support all six validation types, including WARN-mode validations (S3 bucket emptiness, service quota, Config Recorder conflict, and ECR repository delete readiness) that are only available during change set creation. You can use a change set to validate a new stack before you create it, or to validate an update to an existing stack.

**To validate using a change set**

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose the AWS Region where your stack is located.

1. On the **Stacks** page, choose the running stack you want to create a change set for.

1. In the stack details pane, choose **Update Stack**, and then choose **Create a change set**.

1. On the **Create change set for {{stack-name}}** page, upload your updated template or specify the template source.

1. Choose **Next** to proceed through the remaining change set configuration steps.

1. If the template includes IAM resources, for **Capabilities**, choose **I acknowledge that CloudFormation might create IAM resources**. IAM resources can modify permissions in your AWS account; review these resources to ensure that you're permitting only the actions that you intend. For more information, see [Acknowledging IAM resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities).

1. On the **Review** page, choose **Create change set**.

1. CloudFormation creates the change set and runs validation checks. Review the validation results in the **Deployment validation** tab.

1. If validation passes or you're satisfied with the warnings, choose **Execute Change set** to deploy your changes.

1. If validation fails, fix the issues and create a new change set to re-validate your deployment.

## Validate a stack deployment (AWS CLI)
<a name="validate-stack-deployments-cli"></a>

Pre-deployment validation runs automatically on `create-stack` and `update-stack` commands.

**Create a stack with validation**  
Use the following command to create a stack. Pre-deployment validation runs automatically.

```
aws cloudformation create-stack \
  --stack-name {{MyStack}} \
  --template-body {{file://template.yaml}}
```

**Update a stack with validation**  
Use the following command to update a stack. Pre-deployment validation runs automatically.

```
aws cloudformation update-stack \
  --stack-name {{MyStack}} \
  --template-body {{file://updated-template.yaml}}
```

**View validation results**  
Use the following command to view validation results for a stack operation.

```
aws cloudformation describe-events \
  --stack-name {{MyStack}}
```

Example output of validation errors:

```
{
   "OperationEvents":[
      {
         "EventId":"9b5c9a29-4704-4ad0-8082-afb49418d55b",
         "StackId":"arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/c3908380-b357-11f0-a97f-0ad08f35df65",
         "OperationId":"f558b823-e1e3-4de3-a222-e6b930ddcad4",
         "OperationType":"CREATE_STACK",
         "OperationStatus":"FAILED",
         "EventType":"STACK_EVENT",
         "Timestamp":"2025-10-27T17:10:02.923Z",
         "StartTime":"2025-10-27T17:09:57.537Z",
         "EndTime":"2025-10-27T17:10:02.923Z"
      },
      {
         "EventId":"2d8c3262-3468-4283-82fb-6e780e9e4f1d",
         "StackId":"arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/c3908380-b357-11f0-a97f-0ad08f35df65",
         "OperationId":"f558b823-e1e3-4de3-a222-e6b930ddcad4",
         "OperationType":"CREATE_STACK",
         "EventType":"VALIDATION_ERROR",
         "LogicalResourceId":"NotificationBucket",
         "PhysicalResourceId":"",
         "ResourceType":"AWS::S3::Bucket",
         "Timestamp":"2025-10-27T17:10:02.461Z",
         "ValidationFailureMode":"FAIL",
         "ValidationName":"PROPERTY_VALIDATION",
         "ValidationStatus":"FAILED",
         "ValidationStatusReason":"#/NotificationConfiguration/QueueConfigurations/0: required key [Event] not found",
         "ValidationPath":"/Resources/NotificationBucket/Properties/NotificationConfiguration/QueueConfigurations/0"
      }
   ]
}
```

### Validate using a change set (AWS CLI)
<a name="validate-stack-deployments-cli-changeset"></a>

Change sets also surface WARN-mode validations that are not available on direct stack operations.

**To validate using a change set**

1. Use the [create-change-set](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-change-set.html) command:

   ```
   aws cloudformation create-change-set \
     --stack-name {{MyStack}} \
     --change-set-name {{MyChangeSet}} \
     --change-set-type "CREATE" \
     --template-body {{file://updated-template.yaml}}
   ```

   The command returns both the change set ARN and the stack ARN.

1. Use the [describe-events](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-events.html) command with the change set ARN to review validation status and results.

   ```
   aws cloudformation describe-events \
     --change-set-name "{{arn:aws:cloudformation:us-east-1:123456789012:changeSet/MyChangeSet/94498df5-1afb-43b1-9869-9f82b2d877ac}}"
   ```

1. Address any validation errors by updating your template, then create a new change set.

1. After validation passes, execute the change set:

   ```
   aws cloudformation execute-change-set \
     --change-set-name {{MyChangeSet}} \
     --stack-name {{MyStack}}
   ```

## Validation types
<a name="validate-stack-deployments-validation-types"></a>

Pre-deployment validation includes the following types of checks:
+ **Property Syntax Validation** – Validates resource properties against AWS resource schemas. It checks for required properties and valid property values and identifies deprecated or unsupported property combinations.
+ **Resource Name Conflict Detection** – Checks for naming conflicts with existing AWS resources. It validates that resource names meet AWS naming requirements and identifies potential conflicts before deployment attempts.
+ **S3 Bucket Emptiness Validation** – Warns when attempting to delete S3 buckets that contain objects. It provides object counts to help assess deletion impact and helps prevent common S3 deletion failures.
+ **Service Quota Validation** – Checks whether creating resources would exceed your AWS service quotas. This validation currently runs during change set creation only and operates in WARN mode. The operation proceeds, and you receive alerts about potential quota issues.
+ ** Recorder Conflict Detection** – Warns when your template adds rules to an account that doesn't have recording enabled, or defines an Recorder in an account where one is already active. This validation currently runs during change set creation only and operates in WARN mode.
+ **ECR Repository Delete Readiness** – Validates that ECR repositories targeted for deletion are empty or have appropriate force-delete settings. This validation currently runs during change set creation only and operates in WARN mode.

The following table summarizes each validation type, its mode, and the operations on which it runs.


| Validation type | Mode | Available on | 
| --- | --- | --- | 
| Property syntax validation | FAIL | CreateStack, UpdateStack, CreateChangeSet | 
| Resource name conflict (RAE) | FAIL | CreateStack, UpdateStack, CreateChangeSet | 
| S3 bucket emptiness | WARN | CreateChangeSet | 
| Service Quota | WARN | CreateChangeSet | 
|  Recorder conflict | WARN | CreateChangeSet | 
| ECR Repository delete readiness | WARN | CreateChangeSet | 

Each validation type provides specific error messages and with error location in the template to help you resolve issues quickly.

## Resource limitations
<a name="validate-stack-deployments-resource-limitations"></a>

The following resource types are not supported for pre-deployment validation:
+ `AWS::ApiGatewayV2::ApiGatewayManagedOverrides`
+ `AWS::ApiGatewayV2::Stage`
+ `AWS::AppMesh::GatewayRoute`
+ `AWS::AppMesh::Mesh`
+ `AWS::AppMesh::Route`
+ `AWS::AppMesh::VirtualGateway`
+ `AWS::AppMesh::VirtualNode`
+ `AWS::AppMesh::VirtualRouter`
+ `AWS::AppMesh::VirtualService`
+ `AWS::AppStream::Fleet`
+ `AWS::AppStream::Stack`
+ `AWS::AppStream::StackFleetAssociation`
+ `AWS::AppStream::StackUserAssociation`
+ `AWS::AppStream::User`
+ `AWS::AppSync::ApiCache`
+ `AWS::AppSync::ApiKey`
+ `AWS::AppSync::GraphQLSchema`
+ `AWS::AutoScalingPlans::ScalingPlan`
+ `AWS::Budgets::Budget`
+ `AWS::CertificateManager::Certificate`
+ `AWS::Cloud9::EnvironmentEC2`
+ `AWS::CloudFormation::CustomResource`
+ `AWS::CloudFormation::Macro`
+ `AWS::CloudFormation::WaitCondition`
+ `AWS::CloudFormation::WaitConditionHandle`
+ `AWS::CloudFront::StreamingDistribution`
+ `AWS::CloudWatch::AnomalyDetector`
+ `AWS::CloudWatch::InsightRule`
+ `AWS::CodeBuild::Project`
+ `AWS::CodeBuild::ReportGroup`
+ `AWS::CodeBuild::SourceCredential`
+ `AWS::CodeCommit::Repository`
+ `AWS::CodeDeploy::DeploymentGroup`
+ `AWS::CodeStar::GitHubRepository`
+ `AWS::Config::ConfigurationRecorder`
+ `AWS::Config::DeliveryChannel`
+ `AWS::Config::OrganizationConfigRule`
+ `AWS::Config::RemediationConfiguration`
+ `AWS::DAX::Cluster`
+ `AWS::DAX::ParameterGroup`
+ `AWS::DAX::SubnetGroup`
+ `AWS::DirectoryService::MicrosoftAD`
+ `AWS::DLM::LifecyclePolicy`
+ `AWS::DMS::Certificate`
+ `AWS::DMS::Endpoint`
+ `AWS::DMS::EventSubscription`
+ `AWS::DMS::ReplicationInstance`
+ `AWS::DMS::ReplicationSubnetGroup`
+ `AWS::DMS::ReplicationTask`
+ `AWS::DocDB::DBCluster`
+ `AWS::DocDB::DBClusterParameterGroup`
+ `AWS::DocDB::DBInstance`
+ `AWS::DocDB::DBSubnetGroup`
+ `AWS::DocDB::EventSubscription`
+ `AWS::EC2::ClientVpnAuthorizationRule`
+ `AWS::EC2::ClientVpnEndpoint`
+ `AWS::EC2::ClientVpnRoute`
+ `AWS::EC2::ClientVpnTargetNetworkAssociation`
+ `AWS::EC2::NetworkInterfacePermission`
+ `AWS::ElastiCache::CacheCluster`
+ `AWS::ElastiCache::ReplicationGroup`
+ `AWS::ElastiCache::SecurityGroup`
+ `AWS::ElastiCache::SecurityGroupIngress`
+ `AWS::ElasticLoadBalancing::LoadBalancer`
+ `AWS::ElasticLoadBalancingV2::ListenerCertificate`
+ `AWS::Elasticsearch::Domain`
+ `AWS::EMR::Cluster`
+ `AWS::EMR::InstanceFleetConfig`
+ `AWS::EMR::InstanceGroupConfig`
+ `AWS::FSx::FileSystem`
+ `AWS::FSx::Snapshot`
+ `AWS::FSx::StorageVirtualMachine`
+ `AWS::FSx::Volume`
+ `AWS::Glue::Classifier`
+ `AWS::Glue::Connection`
+ `AWS::Glue::CustomEntityType`
+ `AWS::Glue::DataCatalogEncryptionSettings`
+ `AWS::Glue::DataQualityRuleset`
+ `AWS::Glue::DevEndpoint`
+ `AWS::Glue::MLTransform`
+ `AWS::Glue::Partition`
+ `AWS::Glue::SecurityConfiguration`
+ `AWS::Glue::Table`
+ `AWS::Glue::TableOptimizer`
+ `AWS::Glue::Workflow`
+ `AWS::Greengrass::ConnectorDefinition`
+ `AWS::Greengrass::ConnectorDefinitionVersion`
+ `AWS::Greengrass::CoreDefinition`
+ `AWS::Greengrass::CoreDefinitionVersion`
+ `AWS::Greengrass::DeviceDefinition`
+ `AWS::Greengrass::DeviceDefinitionVersion`
+ `AWS::Greengrass::FunctionDefinition`
+ `AWS::Greengrass::FunctionDefinitionVersion`
+ `AWS::Greengrass::Group`
+ `AWS::Greengrass::GroupVersion`
+ `AWS::Greengrass::LoggerDefinition`
+ `AWS::Greengrass::LoggerDefinitionVersion`
+ `AWS::Greengrass::ResourceDefinition`
+ `AWS::Greengrass::ResourceDefinitionVersion`
+ `AWS::Greengrass::SubscriptionDefinition`
+ `AWS::Greengrass::SubscriptionDefinitionVersion`
+ `AWS::IAM::AccessKey`
+ `AWS::IAM::UserToGroupAddition`
+ `AWS::IoT::PolicyPrincipalAttachment`
+ `AWS::IoT::ThingPrincipalAttachment`
+ `AWS::IoTThingsGraph::FlowTemplate`
+ `AWS::KinesisAnalytics::Application`
+ `AWS::KinesisAnalytics::ApplicationOutput`
+ `AWS::KinesisAnalytics::ApplicationReferenceDataSource`
+ `AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption`
+ `AWS::KinesisAnalyticsV2::ApplicationOutput`
+ `AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource`
+ `AWS::LakeFormation::DataLakeSettings`
+ `AWS::LakeFormation::Permissions`
+ `AWS::LakeFormation::Resource`
+ `AWS::ManagedBlockchain::Member`
+ `AWS::ManagedBlockchain::Node`
+ `AWS::MediaConvert::JobTemplate`
+ `AWS::MediaConvert::Preset`
+ `AWS::MediaConvert::Queue`
+ `AWS::MediaLive::Channel`
+ `AWS::MediaLive::Input`
+ `AWS::MediaLive::InputSecurityGroup`
+ `AWS::MediaStore::Container`
+ `AWS::OpsWorks::App`
+ `AWS::OpsWorks::ElasticLoadBalancerAttachment`
+ `AWS::OpsWorks::Instance`
+ `AWS::OpsWorks::Layer`
+ `AWS::OpsWorks::Stack`
+ `AWS::OpsWorks::UserProfile`
+ `AWS::OpsWorks::Volume`
+ `AWS::Pinpoint::ADMChannel`
+ `AWS::Pinpoint::APNSChannel`
+ `AWS::Pinpoint::APNSSandboxChannel`
+ `AWS::Pinpoint::APNSVoipChannel`
+ `AWS::Pinpoint::APNSVoipSandboxChannel`
+ `AWS::Pinpoint::App`
+ `AWS::Pinpoint::ApplicationSettings`
+ `AWS::Pinpoint::BaiduChannel`
+ `AWS::Pinpoint::Campaign`
+ `AWS::Pinpoint::EmailChannel`
+ `AWS::Pinpoint::EmailTemplate`
+ `AWS::Pinpoint::EventStream`
+ `AWS::Pinpoint::GCMChannel`
+ `AWS::Pinpoint::PushTemplate`
+ `AWS::Pinpoint::Segment`
+ `AWS::Pinpoint::SMSChannel`
+ `AWS::Pinpoint::SmsTemplate`
+ `AWS::Pinpoint::VoiceChannel`
+ `AWS::PinpointEmail::ConfigurationSet`
+ `AWS::PinpointEmail::ConfigurationSetEventDestination`
+ `AWS::PinpointEmail::DedicatedIpPool`
+ `AWS::PinpointEmail::Identity`
+ `AWS::QLDB::Ledger`
+ `AWS::RDS::DBSecurityGroup`
+ `AWS::RDS::DBSecurityGroupIngress`
+ `AWS::Redshift::ClusterSecurityGroup`
+ `AWS::Redshift::ClusterSecurityGroupIngress`
+ `AWS::Route53::RecordSet`
+ `AWS::Route53::RecordSetGroup`
+ `AWS::SageMaker::CodeRepository`
+ `AWS::SageMaker::EndpointConfig`
+ `AWS::SageMaker::Model`
+ `AWS::SageMaker::NotebookInstance`
+ `AWS::SageMaker::NotebookInstanceLifecycleConfig`
+ `AWS::SageMaker::Workteam`
+ `AWS::SDB::Domain`
+ `AWS::ServiceCatalog::AcceptedPortfolioShare`
+ `AWS::ServiceCatalog::LaunchRoleConstraint`
+ `AWS::ServiceCatalog::Portfolio`
+ `AWS::ServiceCatalog::StackSetConstraint`
+ `AWS::ServiceDiscovery::HttpNamespace`
+ `AWS::ServiceDiscovery::Instance`
+ `AWS::ServiceDiscovery::PrivateDnsNamespace`
+ `AWS::ServiceDiscovery::PublicDnsNamespace`
+ `AWS::ServiceDiscovery::Service`
+ `AWS::SES::ReceiptFilter`
+ `AWS::SES::ReceiptRule`
+ `AWS::SES::ReceiptRuleSet`
+ `AWS::SSM::MaintenanceWindow`
+ `AWS::SSM::MaintenanceWindowTarget`
+ `AWS::SSM::MaintenanceWindowTask`
+ `AWS::WAF::ByteMatchSet`
+ `AWS::WAF::IPSet`
+ `AWS::WAF::Rule`
+ `AWS::WAF::SizeConstraintSet`
+ `AWS::WAF::SqlInjectionMatchSet`
+ `AWS::WAF::WebACL`
+ `AWS::WAF::XssMatchSet`
+ `AWS::WAFRegional::ByteMatchSet`
+ `AWS::WAFRegional::GeoMatchSet`
+ `AWS::WAFRegional::IPSet`
+ `AWS::WAFRegional::RateBasedRule`
+ `AWS::WAFRegional::RegexPatternSet`
+ `AWS::WAFRegional::Rule`
+ `AWS::WAFRegional::SizeConstraintSet`
+ `AWS::WAFRegional::SqlInjectionMatchSet`
+ `AWS::WAFRegional::WebACL`
+ `AWS::WAFRegional::WebACLAssociation`
+ `AWS::WAFRegional::XssMatchSet`
+ `AWS::WorkSpaces::Workspace`
+ `AWS::AmazonMQ::ConfigurationAssociation`
+ `AWS::ApiGateway::DomainNameAccessAssociation`
+ `AWS::AppConfig::ExtensionAssociation`
+ `AWS::AppStream::ApplicationEntitlementAssociation`
+ `AWS::AppStream::ApplicationFleetAssociation`
+ `AWS::AppSync::DomainNameApiAssociation`
+ `AWS::AppSync::SourceApiAssociation`
+ `AWS::CleanRooms::ConfiguredTableAssociation`
+ `AWS::CleanRooms::IdNamespaceAssociation`
+ `AWS::CodeGuruReviewer::RepositoryAssociation`
+ `AWS::Cognito::IdentityPoolRoleAttachment`
+ `AWS::Cognito::UserPoolRiskConfigurationAttachment`
+ `AWS::Cognito::UserPoolUICustomizationAttachment`
+ `AWS::Cognito::UserPoolUserToGroupAttachment`
+ `AWS::Connect::IntegrationAssociation`
+ `AWS::Deadline::QueueFleetAssociation`
+ `AWS::Deadline::QueueLimitAssociation`
+ `AWS::EC2::EIPAssociation`
+ `AWS::EC2::EnclaveCertificateIamRoleAssociation`
+ `AWS::EC2::GatewayRouteTableAssociation`
+ `AWS::EC2::IPAMResourceDiscoveryAssociation`
+ `AWS::EC2::IpPoolRouteTableAssociation`
+ `AWS::EC2::LocalGatewayRouteTableVPCAssociation`
+ `AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation`
+ `AWS::EC2::NetworkInterfaceAttachment`
+ `AWS::EC2::RouteServerAssociation`
+ `AWS::EC2::SecurityGroupVpcAssociation`
+ `AWS::EC2::SubnetNetworkAclAssociation`
+ `AWS::EC2::SubnetRouteTableAssociation`
+ `AWS::EC2::TransitGatewayAttachment`
+ `AWS::EC2::TransitGatewayMulticastDomainAssociation`
+ `AWS::EC2::TransitGatewayPeeringAttachment`
+ `AWS::EC2::TransitGatewayRouteTableAssociation`
+ `AWS::EC2::TransitGatewayVpcAttachment`
+ `AWS::EC2::VPCDHCPOptionsAssociation`
+ `AWS::EC2::VPCGatewayAttachment`
+ `AWS::EC2::VolumeAttachment`
+ `AWS::ECS::ClusterCapacityProviderAssociations`
+ `AWS::EKS::PodIdentityAssociation`
+ `AWS::FSx::DataRepositoryAssociation`
+ `AWS::FSx::S3AccessPointAttachment`
+ `AWS::GlobalAccelerator::CrossAccountAttachment`
+ `AWS::LakeFormation::TagAssociation`
+ `AWS::NetworkFirewall::VpcEndpointAssociation`
+ `AWS::NetworkManager::ConnectAttachment`
+ `AWS::NetworkManager::CustomerGatewayAssociation`
+ `AWS::NetworkManager::DirectConnectGatewayAttachment`
+ `AWS::NetworkManager::LinkAssociation`
+ `AWS::NetworkManager::SiteToSiteVpnAttachment`
+ `AWS::NetworkManager::TransitGatewayRouteTableAttachment`
+ `AWS::NetworkManager::VpcAttachment`
+ `AWS::Notifications::ChannelAssociation`
+ `AWS::Notifications::ManagedNotificationAccountContactAssociation`
+ `AWS::Notifications::ManagedNotificationAdditionalChannelAssociation`
+ `AWS::Notifications::OrganizationalUnitAssociation`
+ `AWS::ResourceExplorer2::DefaultViewAssociation`
+ `AWS::Route53Profiles::ProfileAssociation`
+ `AWS::Route53Profiles::ProfileResourceAssociation`
+ `AWS::Route53Resolver::FirewallRuleGroupAssociation`
+ `AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation`
+ `AWS::Route53Resolver::ResolverRuleAssociation`
+ `AWS::SSM::Association`
+ `AWS::SecretsManager::SecretTargetAttachment`
+ `AWS::SecurityHub::PolicyAssociation`
+ `AWS::ServiceCatalog::PortfolioPrincipalAssociation`
+ `AWS::ServiceCatalog::PortfolioProductAssociation`
+ `AWS::ServiceCatalog::ServiceActionAssociation`
+ `AWS::ServiceCatalog::TagOptionAssociation`
+ `AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation`
+ `AWS::ServiceCatalogAppRegistry::ResourceAssociation`
+ `AWS::VpcLattice::ServiceNetworkResourceAssociation`
+ `AWS::VpcLattice::ServiceNetworkServiceAssociation`
+ `AWS::VpcLattice::ServiceNetworkVpcAssociation`
+ `AWS::WAFv2::WebACLAssociation`
+ `AWS::Wisdom::AssistantAssociation`
+ `AWS::WorkspacesInstances::VolumeAssociation`
+ `AWS::IAM::Policy`
+ `AWS::SNS::TopicPolicy`
+ `AWS::SQS::QueuePolicy`
+ `AWS::EC2::NetworkAclEntry`
+ `AWS::EC2::VPNGatewayRoutePropagation`
+ `AWS::CloudFormation::Stack`
+ `AWS::CloudWatch::MetricStream`
+ `AWS::WorkSpaces::ConnectionAlias`
+ `AWS::IoT::ProvisioningTemplate`
+ `AWS::MediaPackage::Channel`
+ `AWS::CloudFront::OriginRequestPolicy`
+ `AWS::Route53Resolver::ResolverQueryLoggingConfig`
+ `AWS::NetworkManager::TransitGatewayRegistration`
+ `AWS::ImageBuilder::Image`
+ `AWS::Config::ConformancePack`
+ `AWS::S3::AccessPoint`
+ `AWS::CodeStarConnections::Connection`
+ `AWS::CloudFront::CachePolicy`
+ `AWS::FMS::NotificationChannel`
+ `AWS::ImageBuilder::InfrastructureConfiguration`
+ `AWS::Detective::Graph`
+ `AWS::EC2::CarrierGateway`
+ `AWS::CloudWatch::CompositeAlarm`
+ `AWS::CodeArtifact::Repository`
+ `AWS::GroundStation::DataflowEndpointGroup`
+ `AWS::ElasticLoadBalancingV2::Listener`
+ `AWS::ImageBuilder::ImageRecipe`
+ `AWS::NetworkManager::Device`
+ `AWS::Kendra::DataSource`
+ `AWS::Timestream::Database`
+ `AWS::CodeGuruProfiler::ProfilingGroup`
+ `AWS::Lambda::EventSourceMapping`
+ `AWS::ECR::Repository`
+ `AWS::WAFv2::IPSet`
+ `AWS::GameLift::Alias`
+ `AWS::IoTSiteWise::Asset`
+ `AWS::OpsWorksCM::Server`
+ `AWS::IoT::Authorizer`
+ `AWS::WAFv2::RuleGroup`
+ `AWS::NetworkManager::Site`
+ `AWS::ResourceGroups::Group`
+ `AWS::MediaPackage::PackagingConfiguration`
+ `AWS::ImageBuilder::ImagePipeline`
+ `AWS::ECS::TaskDefinition`
+ `AWS::Macie::CustomDataIdentifier`
+ `AWS::MediaPackage::OriginEndpoint`
+ `AWS::Logs::LogGroup`
+ `AWS::CodeArtifact::Domain`
+ `AWS::Kendra::Faq`
+ `AWS::ECS::TaskSet`
+ `AWS::WAFv2::RegexPatternSet`
+ `AWS::ECS::Cluster`
+ `AWS::SSO::Assignment`
+ `AWS::GlobalAccelerator::Listener`
+ `AWS::ServiceCatalog::CloudFormationProvisionedProduct`
+ `AWS::RDS::DBProxy`
+ `AWS::EC2::FlowLog`
+ `AWS::ImageBuilder::Component`
+ `AWS::CloudFront::RealtimeLogConfig`
+ `AWS::NetworkManager::GlobalNetwork`
+ `AWS::RDS::DBProxyTargetGroup`
+ `AWS::WAFv2::WebACL`
+ `AWS::IVS::StreamKey`
+ `AWS::IVS::PlaybackKeyPair`
+ `AWS::Macie::Session`
+ `AWS::Route53::HealthCheck`
+ `AWS::Synthetics::Canary`
+ `AWS::Lambda::CodeSigningConfig`
+ `AWS::EFS::AccessPoint`
+ `AWS::Timestream::Table`
+ `AWS::MediaPackage::PackagingGroup`
+ `AWS::ECS::PrimaryTaskSet`
+ `AWS::Config::ConfigurationAggregator`
+ `AWS::GroundStation::Config`
+ `AWS::IoTSiteWise::AssetModel`
+ `AWS::SES::ConfigurationSet`
+ `AWS::ImageBuilder::DistributionConfiguration`
+ `AWS::Config::OrganizationConformancePack`
+ `AWS::EC2::LocalGatewayRoute`
+ `AWS::KMS::Key`
+ `AWS::Detective::MemberInvitation`
+ `AWS::EKS::FargateProfile`
+ `AWS::MediaPackage::Asset`
+ `AWS::GlobalAccelerator::EndpointGroup`
+ `AWS::Macie::FindingsFilter`
+ `AWS::IoT::Certificate`
+ `AWS::SageMaker::MonitoringSchedule`
+ `AWS::IVS::Channel`
+ `AWS::Kendra::Index`
+ `AWS::EventSchemas::RegistryPolicy`
+ `AWS::KinesisFirehose::DeliveryStream`
+ `AWS::GlobalAccelerator::Accelerator`
+ `AWS::EC2::PrefixList`
+ `AWS::GameLift::GameServerGroup`
+ `AWS::NetworkManager::Link`
+ `AWS::EFS::FileSystem`
+ `AWS::Route53::HostedZone`
+ `AWS::GroundStation::MissionProfile`
+ `AWS::KMS::Alias`
+ `AWS::FMS::Policy`
+ `AWS::SSO::PermissionSet`
+ `AWS::StepFunctions::StateMachine`
+ `AWS::QLDB::Stream`
+ `AWS::IoTSiteWise::Gateway`
+ `AWS::ECS::Service`
+ `AWS::ECS::CapacityProvider`
+ `AWS::EC2::SecurityGroup`
+ `AWS::EC2::SecurityGroupIngress`
+ `AWS::EC2::SecurityGroupEgress`
+ `AWS::EC2::EC2Fleet`
+ `AWS::IAM::Group`
+ `AWS::IAM::Role`
+ `AWS::IAM::User`
+ `AWS::ApiGateway::GatewayResponse`
+ `AWS::S3::BucketPolicy`
+ `AWS::SNS::Topic`
+ `AWS::SNS::Subscription`
+ `AWS::RDS::DBInstance`
+ `AWS::RDS::DBParameterGroup`
+ `AWS::RDS::DBCluster`
+ `AWS::RDS::DBClusterParameterGroup`
+ `AWS::RDS::DBSubnetGroup`
+ `AWS::RDS::EventSubscription`
+ `AWS::RDS::GlobalCluster`
+ `AWS::RDS::OptionGroup`
+ `AWS::Neptune::DBInstance`
+ `AWS::Neptune::DBParameterGroup`
+ `AWS::Neptune::DBCluster`
+ `AWS::Neptune::DBClusterParameterGroup`
+ `AWS::Neptune::DBSubnetGroup`
+ `AWS::Redshift::Cluster`
+ `AWS::Redshift::ClusterParameterGroup`
+ `AWS::Redshift::ClusterSubnetGroup`
+ `AWS::Redshift::EndpointAccess`
+ `AWS::Redshift::EndpointAuthorization`
+ `AWS::Redshift::EventSubscription`
+ `AWS::Redshift::ScheduledAction`
+ `AWS::ElastiCache::SubnetGroup`
+ `AWS::ApiGateway::BasePathMapping`
+ `AWS::ApiGatewayV2::DomainName`
+ `AWS::ApplicationAutoScaling::ScalableTarget`
+ `AWS::Connect::ApprovedOrigin`
+ `AWS::EKS::Cluster`
+ `AWS::IAM::InstanceProfile`
+ `AWS::Lambda::EventInvokeConfig`