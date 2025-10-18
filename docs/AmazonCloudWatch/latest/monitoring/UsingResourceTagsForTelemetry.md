# Using resource tags for telemetry

Once you have enabled resource tags for telemetry, you can leverage this enriched data to create powerful monitoring solutions that scale with your infrastructure. Use tag-based queries to group and filter metrics across multiple resources, create dynamic alarms that 
 automatically adapt to resource changes, and gain insights into your AWS environment organized by meaningful business or operational categories. This approach enables you to monitor resources by team, environment, application, or any other tagging strategy you use in your 
 organization.


* **Creating tag-based Metrics Insights queries** – After you enable resource tags for telemetry in your account, you can create tag-based Metrics Insights queries to discover and visualize your AWS infrastructure metrics by tag. Example queries using tags can be seen in the 
 [CloudWatch Metrics Insights query builder documentation](cloudwatch-metrics-insights-buildquery.md "cloudwatch-metrics-insights-buildquery.md"). *Monitoring accounts* can also make tag based queries for 
 metrics in *source accounts* which have enabled resource tags on their telemetry.
* **Creating tag based CloudWatch alarms** – After you enable resource tags for telemetry in your account, you can create CloudWatch alarms on tag-based Metrics Insights queries to alert on your AWS infrastructure metrics by tag. 
 Example alarms using tag based queries can be seen in the [CloudWatch Metric Insights alarms documentation](cloudwatch-metrics-insights-alarms.md "cloudwatch-metrics-insights-alarms.md").

## Supported AWS infrastructure metrics


The list below displays the AWS CloudFormation resource that support resource tags for telemetry enrichment in CloudWatch. When you enable resource tags for telemetry, CloudWatch can enrich metrics from these services with their associated resource tags.
 



* AWS::EC2::Instance
* AWS::EC2::Volume
* AWS::SQS::Queue
* AWS::ElasticLoadBalancingV2::LoadBalancer
* AWS::Elasticsearch::Domain
* AWS::Route53::HealthCheck
* AWS::Redshift::Cluster
* AWS::ElasticLoadBalancingV2::TargetGroup
* AWS::ElastiCache::CacheCluster
* AWS::RDS::DBInstance
* AWS::Lambda::Function
* AWS::RDS::DBCluster
* AWS::DynamoDB::Table
* AWS::EC2::NatGateway
* AWS::KinesisVideo::Stream
* AWS::Logs::LogGroup
* AWS::CloudFront::Distribution
* AWS::Events::Rule
* AWS::WorkSpaces::Workspace
* AWS::KinesisFirehose::DeliveryStream
* AWS::ElasticLoadBalancing::LoadBalancer
* AWS::Kinesis::Stream
* AWS::AmazonMQ::Broker
* AWS::Route53::HostedZone
* AWS::SNS::Topic
* AWS::EFS::FileSystem
* AWS::EC2::TransitGatewayAttachment
* AWS::DocDB::DBCluster
* AWS::ECS::Service
* AWS::ApiGateway::Stage
* AWS::KinesisAnalytics::Application
* AWS::DocDB::DBInstance
* AWS::DMS::ReplicationInstance
* AWS::Neptune::DBInstance
* AWS::Neptune::DBCluster
* AWS::EC2::TransitGateway
* AWS::KinesisVideo::SignalingChannel
* AWS::ElastiCache::ReplicationGroup
* AWS::S3::Bucket
* AWS::StepFunctions::StateMachine
* AWS::MemoryDB::Cluster
* AWS::FSx::Volume
* AWS::ECS::Cluster
* AWS::CertificateManager::Certificate
* AWS::DAX::Cluster
* AWS::EMRServerless::Application
* AWS::FSx::FileSystem
* AWS::MWAA::Environment
* AWS::ElasticBeanstalk::Environment
* AWS::OpsWorks::Instance
* AWS::Events::EventBus
* AWS::NetworkFirewall::Firewall
* AWS::CodeBuild::Project
* AWS::SageMaker::Endpoint
* AWS::ECR::Repository
* AWS::MediaLive::Channel
* AWS::OSIS::Pipeline
* AWS::GameLift::Fleet
* AWS::OpsWorks::Layer
* AWS::MediaPackage::Channel
* AWS::Backup::BackupVault
* AWS::AppRunner::Service
* AWS::CloudWatch::MetricStream
* AWS::StepFunctions::Activity
* AWS::OpsWorks::Stack
* AWS::Timestream::Database
* AWS::Cassandra::Keyspace
* AWS::DataSync::Task
* AWS::KafkaConnect::Connector
* AWS::Kendra::Index
* AWS::Athena::WorkGroup
* AWS::InternetMonitor::Monitor
* AWS::IoT::SecurityProfile
* AWS::AppStream::Fleet
* AWS::Timestream::Table
* AWS::AppFlow::Flow
* AWS::Connect::Instance
* AWS::Logs::LogAnomalyDetector
* AWS::Scheduler::ScheduleGroup
* AWS::MediaPackage::OriginEndpoint
* AWS::Cognito::UserPool
* AWS::CodeGuruProfiler::ProfilingGroup
* AWS::Transfer::Server
* AWS::GameLift::Location
* AWS::IVS::Channel
* AWS::DataSync::Agent
* AWS::EC2::Host
* AWS::QuickSight::Dashboard
* AWS::VpcLattice::TargetGroup
* AWS::MediaConvert::Queue
* AWS::SageMaker::FeatureGroup
* AWS::Route53Resolver::FirewallRuleGroup
* AWS::Config::ConformancePack
* AWS::VoiceID::Domain
* AWS::Lex::BotVersion
* AWS::Transfer::Connector
* AWS::MSK::Replicator
* AWS::DMS::ReplicationConfig
* AWS::Redshift::Integration
* AWS::Evidently::Project
* AWS::QLDB::Ledger
* AWS::Lex::Bot
* AWS::ManagedBlockchain::Member
* AWS::MediaTailor::Channel
* AWS::GameLift::ContainerGroupDefinition
* AWS::VpcLattice::Service
* AWS::QBusiness::Index
* AWS::Lex::BotAlias
* AWS::MediaStore::Container
* AWS::IoT::ScheduledAudit
* AWS::IoTSiteWise::Gateway
* AWS::LookoutEquipment::InferenceScheduler
* AWS::FraudDetector::Variable
* AWS::DMS::ReplicationTask
* AWS::MediaPackage::PackagingConfiguration
* AWS::CustomerProfiles::Domain
* AWS::Personalize::Dataset
* AWS::IoTAnalytics::Pipeline
* AWS::M2::Environment
* AWS::LookoutMetrics::AnomalyDetector
* AWS::IoTAnalytics::Dataset
* AWS::SageMaker::InferenceComponent
* AWS::ManagedBlockchain::Node
* AWS::IoTAnalytics::Channel
* AWS::Personalize::DatasetGroup
* AWS::SageMaker::Workteam
* AWS::FraudDetector::Outcome
* AWS::Rekognition::Project
* AWS::LookoutMetrics::Alert
* AWS::KMS::Key
* AWS::QLDB::Stream
* AWS::IoT::ProvisioningTemplate
* AWS::Personalize::Solution
* AWS::ApiGateway::UsagePlan
* AWS::IoTFleetWise::Campaign
* AWS::Forecast::Dataset
* AWS::IoTFleetWise::Vehicle
* AWS::SageMaker::Model
