

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Supported Resources
<a name="cfn-ingest-supp-services"></a>

The following AWS resources are supported in the AMS CloudFormation ingest process.

## CloudFormation Ingest Stack: Supported resources
<a name="ex-cfn-ingest-supp-resources"></a>

The instance operating system must be supported by AMS workload ingestion. Only those AWS resources listed here are supported.
+  [Amazon API Gateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApiGateway.html)
  + AWS::ApiGateway::Account
  + AWS::ApiGateway::ApiKey
  + AWS::ApiGateway::Authorizer
  + AWS::ApiGateway::BasePathMapping
  + AWS::ApiGateway::ClientCertificate
  + AWS::ApiGateway::Deployment
  + AWS::ApiGateway::DocumentationPart
  + AWS::ApiGateway::DocumentationVersion
  + AWS::ApiGateway::DomainName
  + AWS::ApiGateway::GatewayResponse
  + AWS::ApiGateway::Method
  + AWS::ApiGateway::Model
  + AWS::ApiGateway::RequestValidator
  + AWS::ApiGateway::Resource
  + AWS::ApiGateway::RestApi
  + AWS::ApiGateway::Stage
  + AWS::ApiGateway::UsagePlan
  + AWS::ApiGateway::UsagePlanKey
  + AWS::ApiGateway::VpcLink
+  [Amazon API Gateway V2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApiGatewayV2.html)
  + AWS::ApiGatewayV2::Api
  + AWS::ApiGatewayV2::ApiGatewayManagedOverrides
  + AWS::ApiGatewayV2::ApiMapping
  + AWS::ApiGatewayV2::Authorizer
  + AWS::ApiGatewayV2::Deployment
  + AWS::ApiGatewayV2::DomainName
  + AWS::ApiGatewayV2::Integration
  + AWS::ApiGatewayV2::IntegrationResponse
  + AWS::ApiGatewayV2::Model
  + AWS::ApiGatewayV2::Route
  + AWS::ApiGatewayV2::RouteResponse
  + AWS::ApiGatewayV2::Stage
  + AWS::ApiGatewayV2::VpcLink
+  [AWS AppSync](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppSync.html)
  + AWS::AppSync::ApiCache
  + AWS::AppSync::ApiKey
  + AWS::AppSync::DataSource
  + AWS::AppSync::FunctionConfiguration
  + AWS::AppSync::GraphQLApi
  + AWS::AppSync::GraphQLSchema
  + AWS::AppSync::Resolver
+  [Amazon Athena](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Athena.html)
  + AWS::Athena::NamedQuery
  + AWS::Athena::WorkGroup
+  [AWS Backup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Backup.html)
  + AWS::Backup::BackupVault
+ [Amazon CloudFront](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-reference-cloudfront.html)
  + AWS::CloudFront::Distribution
  + AWS::CloudFront::CloudFrontOriginAccessIdentity
  + AWS::CloudFront::StreamingDistribution
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-reference-cloudwatch.html)
  + AWS::CloudWatch::Alarm
  + AWS::CloudWatch::AnomalyDetector
  + AWS::CloudWatch::CompositeAlarm
  + AWS::CloudWatch::Dashboard
  + AWS::CloudWatch::InsightRule
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Logs.html)
  + AWS::Logs::LogGroup
  + AWS::Logs::LogStream
  + AWS::Logs::MetricFilter
  + AWS::Logs::SubscriptionFilter
+  [Amazon Cognito](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cognito.html)
  + AWS::Cognito::IdentityPool
  + AWS::Cognito::IdentityPoolRoleAttachment
  + AWS::Cognito::UserPool
  + AWS::Cognito::UserPoolClient
  + AWS::Cognito::UserPoolDomain
  + AWS::Cognito::UserPoolGroup
  + AWS::Cognito::UserPoolIdentityProvider
  + AWS::Cognito::UserPoolResourceServer
  + AWS::Cognito::UserPoolRiskConfigurationAttachment
  + AWS::Cognito::UserPoolUICustomizationAttachment
  + AWS::Cognito::UserPoolUser
  + AWS::Cognito::UserPoolUserToGroupAttachment
+  [Amazon DocumentDB](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DocDB.html)
  + AWS::DocDB::DBCluster
  + AWS::DocDB::DBClusterParameterGroup
  + AWS::DocDB::DBInstance
  + AWS::DocDB::DBSubnetGroup
+  [Amazon DynamoDB](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DynamoDB.html)
  + AWS::DynamoDB::Table
+ [Amazon EC2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EC2.html)
  + AWS::EC2::Volume
  + AWS::EC2::VolumeAttachment
  + AWS::EC2::Instance
  + AWS::EC2::EIP
  + AWS::EC2::EIPAssociation
  + AWS::EC2::NetworkInterface
  + AWS::EC2::NetworkInterfaceAttachment
  + AWS::EC2::SecurityGroup
  + AWS::EC2::SecurityGroupIngress
  + AWS::EC2::SecurityGroupEgress
  + AWS::EC2::LaunchTemplate
+  [AWS Batch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Batch.html)
  + AWS::Batch::ComputeEnvironment
  + AWS::Batch::JobDefinition
  + AWS::Batch::JobQueue
+ [Amazon Elastic Container Registry (ECR)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ECR.html)
  + AWS::ECR::Repository
+ [Amazon Elastic Container Service (ECS) (Fargate)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EFS.html)
  + AWS::ECS::CapacityProvider
  + AWS::ECS::Cluster
  + AWS::ECS::PrimaryTaskSet
  + AWS::ECS::Service
  + AWS::ECS::TaskDefinition
  + AWS::ECS::TaskSet
+ [Amazon Elastic File System (EFS)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EFS.html)
  + AWS::EFS::FileSystem
  + AWS::EFS::MountTarget
+ [Amazon ElastiCache](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElastiCache.html)
  + AWS::ElastiCache::CacheCluster
  + AWS::ElastiCache::ParameterGroup
  + AWS::ElastiCache::ReplicationGroup
  + AWS::ElastiCache::SecurityGroup
  + AWS::ElastiCache::SecurityGroupIngress
  + AWS::ElastiCache::SubnetGroup
+ [Amazon EventBridge](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Events.html)
  + AWS::Events::EventBus
  + AWS::Events::EventBusPolicy
  + AWS::Events::Rule
+ [Amazon FSx](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FSx.html)
  + AWS::FSx::FileSystem
+ [Amazon Inspector](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Inspector.html)
  + AWS::Inspector::AssessmentTarget
  + AWS::Inspector::AssessmentTemplate
  + AWS::Inspector::ResourceGroup
+ [Amazon Kinesis Data Analytics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalytics.html)
  + AWS::KinesisAnalytics::Application
  + AWS::KinesisAnalytics::ApplicationOutput
  + AWS::KinesisAnalytics::ApplicationReferenceDataSource
+  [Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisFirehose.html)
  + AWS::KinesisFirehose::DeliveryStream
+ [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Kinesis.html)
  + AWS::Kinesis::Stream
  + AWS::Kinesis::StreamConsumer
+ [Amazon MQ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AmazonMQ.html)
  + AWS::AmazonMQ::Broker
  + AWS::AmazonMQ::Configuration
  + AWS::AmazonMQ::ConfigurationAssociation
+ [Amazon OpenSearch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpenSearchService.html)
  + AWS::OpenSearchService::Domain
+ [Amazon Relational Database Service (RDS)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RDS.html)
  + AWS::RDS::DBCluster
  + AWS::RDS::DBClusterParameterGroup
  + AWS::RDS::DBInstance
  + AWS::RDS::DBParameterGroup
  + AWS::RDS::DBSubnetGroup
  + AWS::RDS::EventSubscription
  + AWS::RDS::OptionGroup
+ [Amazon Route 53](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53.html)
  + AWS::Route53::HealthCheck
  + AWS::Route53::HostedZone
  + AWS::Route53::RecordSet
  + AWS::Route53::RecordSetGroup
  + AWS::Route53Resolver::ResolverRule
  + AWS::Route53Resolver::ResolverRuleAssociation
+ [Amazon S3](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3.html)
  + AWS::S3::Bucket
+ [Amazon Sagemaker](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SageMaker.html)
  + AWS::SageMaker::CodeRepository
  + AWS::SageMaker::Endpoint
  + AWS::SageMaker::EndpointConfig
  + AWS::SageMaker::Model
  + AWS::SageMaker::NotebookInstance
  + AWS::SageMaker::NotebookInstanceLifecycleConfig
  + AWS::SageMaker::Workteam
+  [Amazon Simple Email Service (SES)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SES.html)
  + AWS::SES::ConfigurationSet
  + AWS::SES::ConfigurationSetEventDestination
  + AWS::SES::ReceiptFilter
  + AWS::SES::ReceiptRule
  + AWS::SES::ReceiptRuleSet
  + AWS::SES::Template
+  [Amazon SimpleDB](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SDB.html)
  + AWS::SDB::Domain
+ [Amazon SNS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SNS.html)
  + AWS::SNS::Subscription
  + AWS::SNS::Topic
+ [Amazon SQS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SQS.html)
  + AWS::SQS::Queue
+  [Amazon WorkSpaces](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpaces.html)
  + AWS::WorkSpaces::Workspace
+ [Application AutoScaling](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationAutoScaling.html)
  + AWS::ApplicationAutoScaling::ScalableTarget
  + AWS::ApplicationAutoScaling::ScalingPolicy
+ [Amazon EC2 AutoScaling](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AutoScaling.html)
  + AWS::AutoScaling::AutoScalingGroup
  + AWS::AutoScaling::LaunchConfiguration
  + AWS::AutoScaling::LifecycleHook
  + AWS::AutoScaling::ScalingPolicy
  + AWS::AutoScaling::ScheduledAction
+ [AWS Certificate Manager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html)
  + AWS::CertificateManager::Certificate
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CloudFormation.html)
  + AWS::CloudFormation::CustomResource
  + AWS::CloudFormation::Designer
  + AWS::CloudFormation::WaitCondition
  + AWS::CloudFormation::WaitConditionHandle
+ [AWS CodeBuild](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeBuild.html)
  + AWS::CodeBuild::Project
  + AWS::CodeBuild::ReportGroup
  + AWS::CodeBuild::SourceCredential
+  [AWS CodeCommit](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeCommit.html)
  + AWS::CodeCommit::Repository
+ [AWS CodeDeploy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeDeploy.html)
  + AWS::CodeDeploy::Application
  + AWS::CodeDeploy::DeploymentConfig
  + AWS::CodeDeploy::DeploymentGroup
+ [AWS CodePipeline](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodePipeline.html)
  + AWS::CodePipeline::CustomActionType
  + AWS::CodePipeline::Pipeline
  + AWS::CodePipeline::Webhook
+  [AWS Database Migration Service (DMS)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DMS.html)
  + AWS::DMS::Certificate
  + AWS::DMS::Endpoint
  + AWS::DMS::EventSubscription
  + AWS::DMS::ReplicationInstance
  + AWS::DMS::ReplicationSubnetGroup
  + AWS::DMS::ReplicationTask

  The MongoDbSettings property in AWS::DMS::Endpoint resource is not allowed.

  The following properties are only allowed if they are resolved by AWS Secrets Manager: CertificatePem and CertificateWallet properties in the AWS::DMS::Certificate resource, and the Password property in the AWS::DMS::Endpoint resource.
+ [AWS Elastic Load Balancing - Application Load Balancer / Network Load Balancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElasticLoadBalancingV2.html)
  + AWS::ElasticLoadBalancingV2::Listener
  + AWS::ElasticLoadBalancingV2::ListenerCertificate
  + AWS::ElasticLoadBalancingV2::ListenerRule
  + AWS::ElasticLoadBalancingV2::LoadBalancer
  + AWS::ElasticLoadBalancingV2::TargetGroup
+ [AWS Elastic Load Balancing - Classic Load Balancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElasticLoadBalancing.html)
  + AWS::ElasticLoadBalancing::LoadBalancer
+  [AWS Elemental MediaConvert](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaConvert.html)
  + AWS::MediaConvert::JobTemplate
  + AWS::MediaConvert::Preset
  + AWS::MediaConvert::Queue
+  [AWS Elemental MediaStore](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaStore.html)
  + AWS::MediaStore::Container
+  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)
  + AWS::IAM::Role
+  [AWS Managed Streaming for Apache Kafka (MSK)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MSK.html)
  + AWS::MSK::Cluster
+  [AWS Glue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Glue.html)
  + AWS::Glue::Classifier
  + AWS::Glue::Connection
  + AWS::Glue::Crawler
  + AWS::Glue::Database
  + AWS::Glue::DataCatalogEncryptionSettings
  + AWS::Glue::DevEndpoint
  + AWS::Glue::Job
  + AWS::Glue::MLTransform
  + AWS::Glue::Partition
  + AWS::Glue::SecurityConfiguration
  + AWS::Glue::Table
  + AWS::Glue::Trigger
  + AWS::Glue::Workflow
+ [AWS Key Management Service (KMS)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KMS.html)
  + AWS::KMS::Key
  + AWS::KMS::Alias
+  [AWS Lake Formation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.html)
  + AWS::LakeFormation::DataLakeSettings
  + AWS::LakeFormation::Permissions
  + AWS::LakeFormation::Resource
+  [AWS Lambda](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lambda.html)
  + AWS::Lambda::Alias
  + AWS::Lambda::EventInvokeConfig
  + AWS::Lambda::EventSourceMapping
  + AWS::Lambda::Function
  + AWS::Lambda::LayerVersion
  + AWS::Lambda::LayerVersionPermission
  + AWS::Lambda::Permission
  + AWS::Lambda::Version
+  [Amazon Redshift](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Redshift.html)
  + AWS::Redshift::Cluster
  + AWS::Redshift::ClusterParameterGroup
  + AWS::Redshift::ClusterSubnetGroup
+  [AWS Secrets Manager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecretsManager.html)
  + AWS::SecretsManager::ResourcePolicy
  + AWS::SecretsManager::RotationSchedule
  + AWS::SecretsManager::Secret
  + AWS::SecretsManager::SecretTargetAttachment
+  [AWS Security Hub](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.html)
  + AWS::SecurityHub::Hub
+  [AWS Step Functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_StepFunctions.html)
  + AWS::StepFunctions::Activity
  + AWS::StepFunctions::StateMachine
+  [AWS Systems Manager (SSM)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSM.html)
  + AWS::SSM::Parameter
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Synthetics.html)
  + AWS::Synthetics::Canary
+  [AWS Transfer Family](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Transfer.html)
  + AWS::Transfer::Server
  + AWS::Transfer::User
+ [AWS WAF](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WAF.html)
  + AWS::WAF::ByteMatchSet
  + AWS::WAF::IPSet
  + AWS::WAF::Rule
  + AWS::WAF::SizeConstraintSet
  + AWS::WAF::SqlInjectionMatchSet
  + AWS::WAF::WebACL
  + AWS::WAF::XssMatchSet
+ [AWS WAF Regional](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WAFRegional.html)
  + AWS::WAFRegional::ByteMatchSet
  + AWS::WAFRegional::GeoMatchSet
  + AWS::WAFRegional::IPSet
  + AWS::WAFRegional::RateBasedRule
  + AWS::WAFRegional::RegexPatternSet
  + AWS::WAFRegional::Rule
  + AWS::WAFRegional::SizeConstraintSet
  + AWS::WAFRegional::SqlInjectionMatchSet
  + AWS::WAFRegional::WebACL
  + AWS::WAFRegional::WebACLAssociation
  + AWS::WAFRegional::XssMatchSet
+ [AWS WAFv2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WAFv2.html)
  + AWS::WAFv2::IPSet
  + AWS::WAFv2::RegexPatternSet
  + AWS::WAFv2::RuleGroup
  + AWS::WAFv2::WebACL
  + AWS::WAFv2::WebACLAssociation