# Supported Resources

The following AWS resources are supported in the AMS CloudFormation ingest process.

## CloudFormation Ingest Stack: Supported resources

The instance operating system must be supported by AMS workload ingestion.
Only those AWS resources listed here are supported.

- [Amazon API Gateway](../../../AWSCloudFormation/latest/UserGuide/AWS_ApiGateway.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ApiGateway.md")
  - AWS::ApiGateway::Account
  - AWS::ApiGateway::ApiKey
  - AWS::ApiGateway::Authorizer
  - AWS::ApiGateway::BasePathMapping
  - AWS::ApiGateway::ClientCertificate
  - AWS::ApiGateway::Deployment
  - AWS::ApiGateway::DocumentationPart
  - AWS::ApiGateway::DocumentationVersion
  - AWS::ApiGateway::DomainName
  - AWS::ApiGateway::GatewayResponse
  - AWS::ApiGateway::Method
  - AWS::ApiGateway::Model
  - AWS::ApiGateway::RequestValidator
  - AWS::ApiGateway::Resource
  - AWS::ApiGateway::RestApi
  - AWS::ApiGateway::Stage
  - AWS::ApiGateway::UsagePlan
  - AWS::ApiGateway::UsagePlanKey
  - AWS::ApiGateway::VpcLink

- [Amazon API Gateway V2](../../../AWSCloudFormation/latest/UserGuide/AWS_ApiGatewayV2.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ApiGatewayV2.md")
  - AWS::ApiGatewayV2::Api
  - AWS::ApiGatewayV2::ApiGatewayManagedOverrides
  - AWS::ApiGatewayV2::ApiMapping
  - AWS::ApiGatewayV2::Authorizer
  - AWS::ApiGatewayV2::Deployment
  - AWS::ApiGatewayV2::DomainName
  - AWS::ApiGatewayV2::Integration
  - AWS::ApiGatewayV2::IntegrationResponse
  - AWS::ApiGatewayV2::Model
  - AWS::ApiGatewayV2::Route
  - AWS::ApiGatewayV2::RouteResponse
  - AWS::ApiGatewayV2::Stage
  - AWS::ApiGatewayV2::VpcLink

- [AWS AppSync](../../../AWSCloudFormation/latest/UserGuide/AWS_AppSync.md "../../../AWSCloudFormation/latest/UserGuide/AWS_AppSync.md")
  - AWS::AppSync::ApiCache
  - AWS::AppSync::ApiKey
  - AWS::AppSync::DataSource
  - AWS::AppSync::FunctionConfiguration
  - AWS::AppSync::GraphQLApi
  - AWS::AppSync::GraphQLSchema
  - AWS::AppSync::Resolver

- [Amazon Athena](../../../AWSCloudFormation/latest/UserGuide/AWS_Athena.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Athena.md")
  - AWS::Athena::NamedQuery
  - AWS::Athena::WorkGroup

- [AWS Backup](../../../AWSCloudFormation/latest/UserGuide/AWS_Backup.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Backup.md")
  - AWS::Backup::BackupVault

- [Amazon CloudFront](../../../AWSCloudFormation/latest/UserGuide/cfn-reference-cloudfront.md "../../../AWSCloudFormation/latest/UserGuide/cfn-reference-cloudfront.md")
  - AWS::CloudFront::Distribution
  - AWS::CloudFront::CloudFrontOriginAccessIdentity
  - AWS::CloudFront::StreamingDistribution

- [Amazon CloudWatch](../../../AWSCloudFormation/latest/UserGuide/cfn-reference-cloudwatch.md "../../../AWSCloudFormation/latest/UserGuide/cfn-reference-cloudwatch.md")
  - AWS::CloudWatch::Alarm
  - AWS::CloudWatch::AnomalyDetector
  - AWS::CloudWatch::CompositeAlarm
  - AWS::CloudWatch::Dashboard
  - AWS::CloudWatch::InsightRule

- [Amazon CloudWatch Logs](../../../AWSCloudFormation/latest/UserGuide/AWS_Logs.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Logs.md")
  - AWS::Logs::LogGroup
  - AWS::Logs::LogStream
  - AWS::Logs::MetricFilter
  - AWS::Logs::SubscriptionFilter

- [Amazon Cognito](../../../AWSCloudFormation/latest/UserGuide/AWS_Cognito.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Cognito.md")
  - AWS::Cognito::IdentityPool
  - AWS::Cognito::IdentityPoolRoleAttachment
  - AWS::Cognito::UserPool
  - AWS::Cognito::UserPoolClient
  - AWS::Cognito::UserPoolDomain
  - AWS::Cognito::UserPoolGroup
  - AWS::Cognito::UserPoolIdentityProvider
  - AWS::Cognito::UserPoolResourceServer
  - AWS::Cognito::UserPoolRiskConfigurationAttachment
  - AWS::Cognito::UserPoolUICustomizationAttachment
  - AWS::Cognito::UserPoolUser
  - AWS::Cognito::UserPoolUserToGroupAttachment

- [Amazon DocumentDB](../../../AWSCloudFormation/latest/UserGuide/AWS_DocDB.md "../../../AWSCloudFormation/latest/UserGuide/AWS_DocDB.md")
  - AWS::DocDB::DBCluster
  - AWS::DocDB::DBClusterParameterGroup
  - AWS::DocDB::DBInstance
  - AWS::DocDB::DBSubnetGroup

- [Amazon DynamoDB](../../../AWSCloudFormation/latest/UserGuide/AWS_DynamoDB.md "../../../AWSCloudFormation/latest/UserGuide/AWS_DynamoDB.md")
  - AWS::DynamoDB::Table

- [Amazon EC2](../../../AWSCloudFormation/latest/UserGuide/AWS_EC2.md "../../../AWSCloudFormation/latest/UserGuide/AWS_EC2.md")
  - AWS::EC2::Volume
  - AWS::EC2::VolumeAttachment
  - AWS::EC2::Instance
  - AWS::EC2::EIP
  - AWS::EC2::EIPAssociation
  - AWS::EC2::NetworkInterface
  - AWS::EC2::NetworkInterfaceAttachment
  - AWS::EC2::SecurityGroup
  - AWS::EC2::SecurityGroupIngress
  - AWS::EC2::SecurityGroupEgress
  - AWS::EC2::LaunchTemplate

- [AWS Batch](../../../AWSCloudFormation/latest/UserGuide/AWS_Batch.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Batch.md")
  - AWS::Batch::ComputeEnvironment
  - AWS::Batch::JobDefinition
  - AWS::Batch::JobQueue

- [Amazon Elastic Container Registry (ECR)](../../../AWSCloudFormation/latest/UserGuide/AWS_ECR.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ECR.md")
  - AWS::ECR::Repository

- [Amazon Elastic Container Service (ECS) (Fargate)](../../../AWSCloudFormation/latest/UserGuide/AWS_EFS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_EFS.md")
  - AWS::ECS::CapacityProvider
  - AWS::ECS::Cluster
  - AWS::ECS::PrimaryTaskSet
  - AWS::ECS::Service
  - AWS::ECS::TaskDefinition
  - AWS::ECS::TaskSet

- [Amazon Elastic File System (EFS)](../../../AWSCloudFormation/latest/UserGuide/AWS_EFS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_EFS.md")
  - AWS::EFS::FileSystem
  - AWS::EFS::MountTarget

- [Amazon ElastiCache](../../../AWSCloudFormation/latest/UserGuide/AWS_ElastiCache.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ElastiCache.md")
  - AWS::ElastiCache::CacheCluster
  - AWS::ElastiCache::ParameterGroup
  - AWS::ElastiCache::ReplicationGroup
  - AWS::ElastiCache::SecurityGroup
  - AWS::ElastiCache::SecurityGroupIngress
  - AWS::ElastiCache::SubnetGroup

- [Amazon EventBridge](../../../AWSCloudFormation/latest/UserGuide/AWS_Events.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Events.md")
  - AWS::Events::EventBus
  - AWS::Events::EventBusPolicy
  - AWS::Events::Rule

- [Amazon FSx](../../../AWSCloudFormation/latest/UserGuide/AWS_FSx.md "../../../AWSCloudFormation/latest/UserGuide/AWS_FSx.md")
  - AWS::FSx::FileSystem

- [Amazon Inspector](../../../AWSCloudFormation/latest/UserGuide/AWS_Inspector.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Inspector.md")
  - AWS::Inspector::AssessmentTarget
  - AWS::Inspector::AssessmentTemplate
  - AWS::Inspector::ResourceGroup

- [Amazon Kinesis Data Analytics](../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalytics.md "../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalytics.md")
  - AWS::KinesisAnalytics::Application
  - AWS::KinesisAnalytics::ApplicationOutput
  - AWS::KinesisAnalytics::ApplicationReferenceDataSource

- [Amazon Kinesis Data Firehose](../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisFirehose.md "../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisFirehose.md")
  - AWS::KinesisFirehose::DeliveryStream

- [Amazon Kinesis Data Streams](../../../AWSCloudFormation/latest/UserGuide/AWS_Kinesis.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Kinesis.md")
  - AWS::Kinesis::Stream
  - AWS::Kinesis::StreamConsumer

- [Amazon MQ](../../../AWSCloudFormation/latest/UserGuide/AWS_AmazonMQ.md "../../../AWSCloudFormation/latest/UserGuide/AWS_AmazonMQ.md")
  - AWS::AmazonMQ::Broker
  - AWS::AmazonMQ::Configuration
  - AWS::AmazonMQ::ConfigurationAssociation

- [Amazon OpenSearch](../../../AWSCloudFormation/latest/UserGuide/AWS_OpenSearchService.md "../../../AWSCloudFormation/latest/UserGuide/AWS_OpenSearchService.md")
  - AWS::OpenSearchService::Domain

- [Amazon Relational Database Service (RDS)](../../../AWSCloudFormation/latest/UserGuide/AWS_RDS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_RDS.md")
  - AWS::RDS::DBCluster
  - AWS::RDS::DBClusterParameterGroup
  - AWS::RDS::DBInstance
  - AWS::RDS::DBParameterGroup
  - AWS::RDS::DBSubnetGroup
  - AWS::RDS::EventSubscription
  - AWS::RDS::OptionGroup

- [Amazon Route 53](../../../AWSCloudFormation/latest/UserGuide/AWS_Route53.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Route53.md")
  - AWS::Route53::HealthCheck
  - AWS::Route53::HostedZone
  - AWS::Route53::RecordSet
  - AWS::Route53::RecordSetGroup
  - AWS::Route53Resolver::ResolverRule
  - AWS::Route53Resolver::ResolverRuleAssociation

- [Amazon S3](../../../AWSCloudFormation/latest/UserGuide/AWS_S3.md "../../../AWSCloudFormation/latest/UserGuide/AWS_S3.md")
  - AWS::S3::Bucket

- [Amazon Sagemaker](../../../AWSCloudFormation/latest/UserGuide/AWS_SageMaker.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SageMaker.md")
  - AWS::SageMaker::CodeRepository
  - AWS::SageMaker::Endpoint
  - AWS::SageMaker::EndpointConfig
  - AWS::SageMaker::Model
  - AWS::SageMaker::NotebookInstance
  - AWS::SageMaker::NotebookInstanceLifecycleConfig
  - AWS::SageMaker::Workteam

- [Amazon Simple Email Service (SES)](../../../AWSCloudFormation/latest/UserGuide/AWS_SES.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SES.md")
  - AWS::SES::ConfigurationSet
  - AWS::SES::ConfigurationSetEventDestination
  - AWS::SES::ReceiptFilter
  - AWS::SES::ReceiptRule
  - AWS::SES::ReceiptRuleSet
  - AWS::SES::Template

- [Amazon SimpleDB](../../../AWSCloudFormation/latest/UserGuide/AWS_SDB.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SDB.md")
  - AWS::SDB::Domain

- [Amazon SNS](../../../AWSCloudFormation/latest/UserGuide/AWS_SNS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SNS.md")
  - AWS::SNS::Subscription
  - AWS::SNS::Topic

- [Amazon SQS](../../../AWSCloudFormation/latest/UserGuide/AWS_SQS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SQS.md")
  - AWS::SQS::Queue

- [Amazon WorkSpaces](../../../AWSCloudFormation/latest/UserGuide/AWS_WorkSpaces.md "../../../AWSCloudFormation/latest/UserGuide/AWS_WorkSpaces.md")
  - AWS::WorkSpaces::Workspace

- [Application AutoScaling](../../../AWSCloudFormation/latest/UserGuide/AWS_ApplicationAutoScaling.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ApplicationAutoScaling.md")
  - AWS::ApplicationAutoScaling::ScalableTarget
  - AWS::ApplicationAutoScaling::ScalingPolicy

- [Amazon EC2 AutoScaling](../../../AWSCloudFormation/latest/UserGuide/AWS_AutoScaling.md "../../../AWSCloudFormation/latest/UserGuide/AWS_AutoScaling.md")
  - AWS::AutoScaling::AutoScalingGroup
  - AWS::AutoScaling::LaunchConfiguration
  - AWS::AutoScaling::LifecycleHook
  - AWS::AutoScaling::ScalingPolicy
  - AWS::AutoScaling::ScheduledAction

- [AWS Certificate Manager](../../../AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.md")
  - AWS::CertificateManager::Certificate

- [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_CloudFormation.md "../../../AWSCloudFormation/latest/UserGuide/AWS_CloudFormation.md")
  - AWS::CloudFormation::CustomResource
  - AWS::CloudFormation::Designer
  - AWS::CloudFormation::WaitCondition
  - AWS::CloudFormation::WaitConditionHandle

- [AWS CodeBuild](../../../AWSCloudFormation/latest/UserGuide/AWS_CodeBuild.md "../../../AWSCloudFormation/latest/UserGuide/AWS_CodeBuild.md")
  - AWS::CodeBuild::Project
  - AWS::CodeBuild::ReportGroup
  - AWS::CodeBuild::SourceCredential

- [AWS CodeCommit](../../../AWSCloudFormation/latest/UserGuide/AWS_CodeCommit.md "../../../AWSCloudFormation/latest/UserGuide/AWS_CodeCommit.md")
  - AWS::CodeCommit::Repository

- [AWS CodeDeploy](../../../AWSCloudFormation/latest/UserGuide/AWS_CodeDeploy.md "../../../AWSCloudFormation/latest/UserGuide/AWS_CodeDeploy.md")
  - AWS::CodeDeploy::Application
  - AWS::CodeDeploy::DeploymentConfig
  - AWS::CodeDeploy::DeploymentGroup

- [AWS CodePipeline](../../../AWSCloudFormation/latest/UserGuide/AWS_CodePipeline.md "../../../AWSCloudFormation/latest/UserGuide/AWS_CodePipeline.md")
  - AWS::CodePipeline::CustomActionType
  - AWS::CodePipeline::Pipeline
  - AWS::CodePipeline::Webhook

- [AWS Database Migration Service (DMS)](../../../AWSCloudFormation/latest/UserGuide/AWS_DMS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_DMS.md")

      + AWS::DMS::Certificate
      + AWS::DMS::Endpoint
      + AWS::DMS::EventSubscription
      + AWS::DMS::ReplicationInstance
      + AWS::DMS::ReplicationSubnetGroup
      + AWS::DMS::ReplicationTask

  The MongoDbSettings property in AWS::DMS::Endpoint resource is not allowed.

The following properties are only allowed if they are resolved by
AWS Secrets Manager: CertificatePem and CertificateWallet properties
in the AWS::DMS::Certificate resource, and the Password property in
the AWS::DMS::Endpoint resource.

- [AWS Elastic Load Balancing - Application Load Balancer / Network Load Balancer](../../../AWSCloudFormation/latest/UserGuide/AWS_ElasticLoadBalancingV2.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ElasticLoadBalancingV2.md")
  - AWS::ElasticLoadBalancingV2::Listener
  - AWS::ElasticLoadBalancingV2::ListenerCertificate
  - AWS::ElasticLoadBalancingV2::ListenerRule
  - AWS::ElasticLoadBalancingV2::LoadBalancer
  - AWS::ElasticLoadBalancingV2::TargetGroup

- [AWS Elastic Load Balancing - Classic Load Balancer](../../../AWSCloudFormation/latest/UserGuide/AWS_ElasticLoadBalancing.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ElasticLoadBalancing.md")
  - AWS::ElasticLoadBalancing::LoadBalancer

- [AWS Elemental MediaConvert](../../../AWSCloudFormation/latest/UserGuide/AWS_MediaConvert.md "../../../AWSCloudFormation/latest/UserGuide/AWS_MediaConvert.md")
  - AWS::MediaConvert::JobTemplate
  - AWS::MediaConvert::Preset
  - AWS::MediaConvert::Queue

- [AWS Elemental MediaStore](../../../AWSCloudFormation/latest/UserGuide/AWS_MediaStore.md "../../../AWSCloudFormation/latest/UserGuide/AWS_MediaStore.md")
  - AWS::MediaStore::Container

- [AWS Identity and Access Management (IAM)](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md")
  - AWS::IAM::Role

- [AWS Managed Streaming for Apache Kafka (MSK)](../../../AWSCloudFormation/latest/UserGuide/AWS_MSK.md "../../../AWSCloudFormation/latest/UserGuide/AWS_MSK.md")
  - AWS::MSK::Cluster

- [AWS Glue](../../../AWSCloudFormation/latest/UserGuide/AWS_Glue.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Glue.md")
  - AWS::Glue::Classifier
  - AWS::Glue::Connection
  - AWS::Glue::Crawler
  - AWS::Glue::Database
  - AWS::Glue::DataCatalogEncryptionSettings
  - AWS::Glue::DevEndpoint
  - AWS::Glue::Job
  - AWS::Glue::MLTransform
  - AWS::Glue::Partition
  - AWS::Glue::SecurityConfiguration
  - AWS::Glue::Table
  - AWS::Glue::Trigger
  - AWS::Glue::Workflow

- [AWS Key Management Service (KMS)](../../../AWSCloudFormation/latest/UserGuide/AWS_KMS.md "../../../AWSCloudFormation/latest/UserGuide/AWS_KMS.md")
  - AWS::KMS::Key
  - AWS::KMS::Alias

- [AWS Lake Formation](../../../AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.md "../../../AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.md")
  - AWS::LakeFormation::DataLakeSettings
  - AWS::LakeFormation::Permissions
  - AWS::LakeFormation::Resource

- [AWS Lambda](../../../AWSCloudFormation/latest/UserGuide/AWS_Lambda.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Lambda.md")
  - AWS::Lambda::Alias
  - AWS::Lambda::EventInvokeConfig
  - AWS::Lambda::EventSourceMapping
  - AWS::Lambda::Function
  - AWS::Lambda::LayerVersion
  - AWS::Lambda::LayerVersionPermission
  - AWS::Lambda::Permission
  - AWS::Lambda::Version

- [Amazon Redshift](../../../AWSCloudFormation/latest/UserGuide/AWS_Redshift.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Redshift.md")
  - AWS::Redshift::Cluster
  - AWS::Redshift::ClusterParameterGroup
  - AWS::Redshift::ClusterSubnetGroup

- [AWS Secrets Manager](../../../AWSCloudFormation/latest/UserGuide/AWS_SecretsManager.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SecretsManager.md")
  - AWS::SecretsManager::ResourcePolicy
  - AWS::SecretsManager::RotationSchedule
  - AWS::SecretsManager::Secret
  - AWS::SecretsManager::SecretTargetAttachment

- [AWS Security Hub](../../../AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.md")
  - AWS::SecurityHub::Hub

- [AWS Step Functions](../../../AWSCloudFormation/latest/UserGuide/AWS_StepFunctions.md "../../../AWSCloudFormation/latest/UserGuide/AWS_StepFunctions.md")
  - AWS::StepFunctions::Activity
  - AWS::StepFunctions::StateMachine

- [AWS Systems Manager (SSM)](../../../AWSCloudFormation/latest/UserGuide/AWS_SSM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_SSM.md")
  - AWS::SSM::Parameter

- [Amazon CloudWatch Synthetics](../../../AWSCloudFormation/latest/UserGuide/AWS_Synthetics.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Synthetics.md")
  - AWS::Synthetics::Canary

- [AWS Transfer Family](../../../AWSCloudFormation/latest/UserGuide/AWS_Transfer.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Transfer.md")
  - AWS::Transfer::Server
  - AWS::Transfer::User

- [AWS WAF](../../../AWSCloudFormation/latest/UserGuide/AWS_WAF.md "../../../AWSCloudFormation/latest/UserGuide/AWS_WAF.md")
  - AWS::WAF::ByteMatchSet
  - AWS::WAF::IPSet
  - AWS::WAF::Rule
  - AWS::WAF::SizeConstraintSet
  - AWS::WAF::SqlInjectionMatchSet
  - AWS::WAF::WebACL
  - AWS::WAF::XssMatchSet

- [AWS WAF Regional](../../../AWSCloudFormation/latest/UserGuide/AWS_WAFRegional.md "../../../AWSCloudFormation/latest/UserGuide/AWS_WAFRegional.md")
  - AWS::WAFRegional::ByteMatchSet
  - AWS::WAFRegional::GeoMatchSet
  - AWS::WAFRegional::IPSet
  - AWS::WAFRegional::RateBasedRule
  - AWS::WAFRegional::RegexPatternSet
  - AWS::WAFRegional::Rule
  - AWS::WAFRegional::SizeConstraintSet
  - AWS::WAFRegional::SqlInjectionMatchSet
  - AWS::WAFRegional::WebACL
  - AWS::WAFRegional::WebACLAssociation
  - AWS::WAFRegional::XssMatchSet

- [AWS WAFv2](../../../AWSCloudFormation/latest/UserGuide/AWS_WAFv2.md "../../../AWSCloudFormation/latest/UserGuide/AWS_WAFv2.md")
  - AWS::WAFv2::IPSet
  - AWS::WAFv2::RegexPatternSet
  - AWS::WAFv2::RuleGroup
  - AWS::WAFv2::WebACL
  - AWS::WAFv2::WebACLAssociation
