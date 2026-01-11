# AWS services that support related

telemetry

The following table lists the AWS services that support related entity information
in their CloudWatch telemetry. Services or resources that are not listed in the table do not
have related entity information exposed in CloudWatch.

###### Note

For services that use the [CloudWatch
agent](Install-CloudWatch-Agent.md "Install-CloudWatch-Agent.md"), you may need to update the agent to the latest version to get
related telemetry. For information about sending related entity information
with your own custom metrics, see [How to add related information to
custom telemetry sent to CloudWatch](adding-your-own-related-telemetry.md "adding-your-own-related-telemetry.md").

| AWS Service                                      | Resource                                     | Metrics | Logs |
| ------------------------------------------------ | -------------------------------------------- | ------- | ---- |
| Amazon API Gateway                               | `AWS::ApiGateway::Method`                    | Yes     | No   |
| Amazon API Gateway                               | `AWS::ApiGateway::Resource`                  | Yes     | No   |
| Amazon API Gateway                               | `AWS::ApiGateway::RestApi`                   | Yes     | No   |
| Amazon API Gateway                               | `AWS::ApiGateway::Stage`                     | Yes     | Yes  |
| Amazon API Gateway                               | `AWS::ApiGateway::VpcLink`                   | Yes     | No   |
| Amazon API Gateway V2                            | `AWS::ApiGatewayV2::Integration`             | Yes     | No   |
| Amazon API Gateway V2                            | `AWS::ApiGatewayV2::Route`                   | Yes     | No   |
| Amazon API Gateway V2                            | `AWS::ApiGatewayV2::Stage`                   | No      | Yes  |
| Amazon API Gateway V2                            | `AWS::ApiGatewayV2::Api`                     | Yes     | No   |
| AWS App Runner                                   | `AWS::AppRunner::Service`                    | No      | Yes  |
| AWS Application Migration Service                | `AWS::MGN::SourceServer`                     | Yes     | No   |
| Amazon WorkSpaces Applications                   | `AWS::AppStream::Fleet`                      | Yes     | Yes  |
| AWS AppSync                                      | `AWS::AppSync::GraphQLApi`                   | Yes     | Yes  |
| AWS B2B Data Interchange                         | `AWS::B2BI::Transformer`                     | No      | Yes  |
| AWS Backup gateway                               | `AWS::BackupGateway::Hypervisor`             | No      | Yes  |
| Amazon Bedrock                                   | `AWS::Bedrock::KnowledgeBase`                | No      | Yes  |
| Amazon Bedrock                                   | `AWS::Bedrock::ModelId`                      | Yes     | No   |
| Amazon Chime                                     | `AWS::Chime::SipMediaApplication`            | No      | Yes  |
| Amazon Chime                                     | `AWS::Chime::VoiceConnector`                 | No      | Yes  |
| AWS Clean Rooms                                  | `AWS::CleanRooms::Membership`                | No      | Yes  |
| AWS CloudFormation                               |                                              | No      | Yes  |
| AWS CloudFormation Hooks                         |                                              | No      | Yes  |
| Amazon CloudFront                                | `AWS::CloudFront::Distribution`              | Yes     | Yes  |
| AWS CloudTrail                                   | `AWS::CloudTrail::EventDataStore`            | No      | Yes  |
| AWS CloudTrail                                   | `AWS::CloudTrail::Trail`                     | No      | Yes  |
| Amazon CloudWatch                                | `AWS::CloudWatch::MetricStream`              | Yes     | No   |
| Amazon CloudWatch Logs                           | `AWS::Logs::LogGroup`                        | Yes     | No   |
| Amazon CloudWatch RUM                            | `AWS::RUM::AppMonitor`                       | No      | Yes  |
| Amazon CloudWatch Synthetics                     | `AWS::Synthetics::Canary`                    | Yes     | No   |
| AWS CodeBuild                                    | `AWS::CodeBuild::Project`                    | Yes     | No   |
| Amazon CodeWhisperer                             | `AWS::CodeWhisperer::Customization`          | No      | Yes  |
| Amazon Cognito user pools                        | `AWS::Cognito::UserPool`                     | Yes     | Yes  |
| AWS Config                                       | `AWS::Config::ConfigRule`                    | No      | Yes  |
| Amazon Connect                                   | `AWS::Connect::Instance`                     | No      | Yes  |
| AWS Database Migration Service                   | `AWS::DMS::ReplicationInstance`              | Yes     | No   |
| AWS Database Migration Service                   | `AWS::DMS::ReplicationTask`                  | Yes     | No   |
| AWS DataSync                                     | `AWS::Datasync::Agent`                       | Yes     | No   |
| AWS DataSync                                     | `AWS::DataSync::Task`                        | Yes     | Yes  |
| AWS Directory Service                            | `AWS::DirectoryService::MicrosoftAD`         | No      | Yes  |
| Amazon DynamoDB                                  | `AWS::DynamoDB::Table`                       | Yes     | No   |
| DynamoDB Accelerator                             | `AWS::DAX::Cluster`                          | Yes     | No   |
| Amazon EC2                                       | `AWS::EC2::CapacityReservation`              | Yes     | No   |
| Amazon EC2                                       | `AWS::EC2::Instance`                         | Yes     | No   |
| Amazon EC2                                       | `AWS::EC2::FlowLog`                          | Yes     | No   |
| Amazon EC2                                       | `AWS::EC2::NATGateway`                       | Yes     | No   |
| Amazon EC2                                       | `AWS::EC2::NetworkInterface`                 | Yes     | Yes  |
| Amazon EC2                                       | `AWS::EC2::Subnet`                           | Yes     | Yes  |
| Amazon EC2                                       | `AWS::EC2::TransitGateway`                   | Yes     | No   |
| Amazon EC2                                       | `AWS::EC2::TransitGatewayAttachment`         | Yes     | Yes  |
| Amazon EC2                                       | `AWS::EC2::VerifiedAccessInstance`           | No      | Yes  |
| Amazon EC2                                       | `AWS::EC2::Volume`                           | Yes     | No   |
| Amazon EC2                                       | `AWS::EC2::VPC`                              | No      | Yes  |
| Amazon EC2                                       | `AWS::EC2::VPNConnection`                    | Yes     | Yes  |
| Amazon EC2 Auto Scaling                          | `AWS::AutoScaling::AutoScalingGroup`         | Yes     | No   |
| AWS Elastic Beanstalk                            | `AWS::ElasticBeanstalk::Environment`         | Yes     | No   |
| Amazon Elastic Container Service                 | `AWS::ECS::Cluster`                          | Yes     | Yes  |
| Amazon Elastic Container Service                 | `AWS::ECS::Service`                          | Yes     | Yes  |
| Amazon Elastic File System                       | `AWS::EFS::AccessPoint`                      | Yes     | No   |
| Amazon Elastic File System                       | `AWS::EFS::FileSystem`                       | Yes     | No   |
| Amazon Elastic File System                       | `AWS::EFS::MountTarget`                      | Yes     | No   |
| Amazon Elastic Kubernetes Service                | `AWS::EKS::Cluster`                          | Yes     | Yes  |
| Amazon Elastic Kubernetes Service on AWS Fargate |                                              | No      | Yes  |
| Elastic Load Balancing                           | `AWS::ElasticLoadBalancing::LoadBalancer`    | Yes     | No   |
| Elastic Load Balancing V2                        | `AWS::ElasticLoadBalancingV2::LoadBalancer`  | Yes     | No   |
| Elastic Load Balancing V2                        | `AWS::ElasticLoadBalancingV2::TargetGroup`   | Yes     | No   |
| Amazon ElastiCache                               | `AWS::ElastiCache::CacheCluster`             | Yes     | Yes  |
| AWS Elemental MediaConvert                       | `AWS::MediaConvert::Queue`                   | Yes     | No   |
| AWS Elemental MediaLive                          |                                              | No      | Yes  |
| AWS Elemental MediaLive                          | `AWS::MediaLive::Channel`                    | Yes     | No   |
| AWS Elemental MediaPackage                       | `AWS::MediaPackage::Channel`                 | Yes     | No   |
| AWS Elemental MediaStore                         | `AWS::MediaStore::Container`                 | Yes     | Yes  |
| AWS Elemental MediaTailor                        |                                              | No      | Yes  |
| Amazon EMR                                       | `AWS::EMR::Cluster`                          | Yes     | Yes  |
| Amazon EventBridge                               | `AWS::Events::Rule`                          | Yes     | Yes  |
| Amazon EventBridge Pipes                         | `AWS::Pipes::Pipe`                           | Yes     | Yes  |
| AWS Fault Injection Service                      | `AWS::FIS::ExperimentTemplate`               | No      | Yes  |
| Amazon FinSpace                                  | `AWS::FinSpace::Environment`                 | No      | Yes  |
| Amazon FSx                                       | `AWS::FSx::FileSystem`                       | Yes     | No   |
| Amazon GameLift Servers                          | `AWS::GameLift::Fleet`                       | Yes     | No   |
| AWS Glue                                         | `AWS::Glue::Job`                             | No      | Yes  |
| AWS Identity Sync                                | `AWS::IdentitySync::Profile`                 | No      | Yes  |
| Amazon Interactive Video Service                 | `AWS::IVSChat::LoggingConfiguration`         | Yes     | Yes  |
| AWS IoT                                          | `AWS::IoT::TopicRule`                        | Yes     | Yes  |
| AWS IoT 1-Click                                  | `AWS::IoT1Click::Device`                     | Yes     | No   |
| AWS IoT Events                                   |                                              | No      | Yes  |
| AWS IoT FleetWise                                | `AWS::IoTFleetWise::Vehicle`                 | No      | Yes  |
| AWS IoT SiteWise                                 |                                              | No      | Yes  |
| AWS Key Management Service                       | `AWS::KMS::Key`                              | Yes     | No   |
| Amazon Managed Service for Apache Flink          | `AWS::KinesisAnalytics::Application`         | Yes     | Yes  |
| Amazon Data Firehose                             | `AWS::KinesisFirehose::DeliveryStream`       | Yes     | Yes  |
| Amazon Kinesis Data Streams                      | `AWS::Kinesis::Stream`                       | Yes     | No   |
| Amazon Kinesis Video Streams                     | `AWS::KinesisVideo::Stream`                  | Yes     | No   |
| AWS Lambda                                       | `AWS::Lambda::Function`                      | Yes     | No   |
| Amazon Lex                                       |                                              | No      | Yes  |
| AWS Mainframe Modernization                      | `AWS::M2::Application`                       | No      | Yes  |
| Amazon Managed Streaming for Apache Kafka        | `AWS::Kafka::Cluster`                        | Yes     | No   |
| Amazon Managed Streaming for Apache Kafka        | `AWS::KafkaConnect::Connector`               | No      | Yes  |
| Amazon Managed Streaming for Apache Kafka        | `AWS::MSK::Cluster`                          | Yes     | Yes  |
| Amazon MemoryDB                                  | `AWS::Mmemorydb::Cluster`                    | Yes     | No   |
| Amazon MQ                                        | `AWS::AmazonMQ::Broker`                      | Yes     | Yes  |
| AWS Network Firewall                             | `AWS::NetworkFirewall::Firewall`             | Yes     | Yes  |
| Amazon OpenSearch Service                        | `AWS::OpenSearchService::Domain`             | Yes     | No   |
| Amazon OpenSearch Service                        |                                              | No      | Yes  |
| Amazon OpenSearch Service Ingestion              | `AWS::OSIS::Pipeline`                        | No      | Yes  |
| AWS Organizations                                | `AWS::Organizations::Organization`           | No      | Yes  |
| AWS Outposts                                     | `AWS::Outposts::Outpost`                     | Yes     | No   |
| Amazon Managed Service for Prometheus            | `AWS::Prometheus::Resource`                  | Yes     | No   |
| Amazon Q Business                                |                                              | No      | Yes  |
| Amazon QLDB                                      | `AWS::QLDB::Ledger`                          | Yes     | No   |
| Amazon Quick Suite                               | `AWS::Quicksight::Dashboard`                 | Yes     | No   |
| Amazon Quick Suite                               | `AWS::Quicksight::DataSet`                   | Yes     | No   |
| Amazon Redshift                                  | `AWS::Redshift::Cluster`                     | Yes     | Yes  |
| Amazon Redshift Serverless                       | `AWS::RedshiftServerless::Workgroup`         | Yes     | No   |
| Amazon Relational Database Service               | `AWS::RDS::DBCluster`                        | Yes     | Yes  |
| Amazon Relational Database Service               | `AWS::RDS::DBInstance`                       | Yes     | Yes  |
| Amazon Route 53                                  | `AWS::Route53::HealthCheck`                  | Yes     | Yes  |
| Amazon Route 53                                  | `AWS::Route53::HostedZone`                   | Yes     | No   |
| Amazon Route 53 Resolver                         | `AWS::Route53Resolver::ResolverEndpoint`     | Yes     | No   |
| Amazon S3                                        | `AWS::S3::Bucket`                            | Yes     | No   |
| Amazon SageMaker AI                              | `AWS::SageMaker::Endpoint`                   | Yes     | No   |
| Amazon SageMaker AI                              | `AWS::SageMaker::Workteam`                   | No      | Yes  |
| AWS Service Catalog                              | `AWS::ServiceCatalog::CloudFormationProduct` | Yes     | No   |
| Amazon Simple Email Service                      | `AWS::SES::ConfigurationSet`                 | Yes     | No   |
| Amazon Simple Notification Service               | `AWS::SNS::Topic`                            | Yes     | Yes  |
| Amazon Simple Notification Service               |                                              | No      | Yes  |
| Amazon Simple Queue Service                      | `AWS::SQS::Queue`                            | Yes     | No   |
| AWS Step Functions                               | `AWS::StepFunctions::Activity`               | Yes     | No   |
| AWS Step Functions                               | `AWS::StepFunctions::StateMachine`           | Yes     | Yes  |
| AWS Storage Gateway                              | `AWS::StorageGateway::Gateway`               | Yes     | No   |
| AWS Storage Gateway                              | `AWS::StorageGateway::Share`                 | No      | Yes  |
| AWS Transfer Family                              | `AWS::Transfer::Server`                      | Yes     | Yes  |
| Amazon VPC Lattice                               | `AWS::VpcLattice::Service`                   | No      | Yes  |
| AWS WAFV2                                        | `AWS::WAFv2::WebAcl`                         | No      | Yes  |
| Amazon WorkMail                                  | `AWS::WorkMail::Organization`                | Yes     | No   |
| Amazon WorkSpaces                                | `AWS::WorkSpaces::Workspace`                 | Yes     | Yes  |
