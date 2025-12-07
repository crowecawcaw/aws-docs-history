# Using resource tags for telemetry

Once you have enabled resource tags for telemetry, you can leverage this enriched data to create powerful monitoring solutions that scale with your infrastructure. Use tag-based queries to group and filter metrics across multiple resources, create dynamic alarms that
automatically adapt to resource changes, and gain insights into your AWS environment organized by meaningful business or operational categories. This approach enables you to monitor resources by team, environment, application, or any other tagging strategy you use in your
organization.

- **Creating tag-based Metrics Insights queries** – After you enable resource tags for telemetry in your account, you can create tag-based Metrics Insights queries to discover and visualize your AWS infrastructure metrics by tag. Example queries using tags can be seen in the
  [CloudWatch Metrics Insights query builder documentation](cloudwatch-metrics-insights-buildquery.md "cloudwatch-metrics-insights-buildquery.md"). _Monitoring accounts_ can also make tag-based queries for
  metrics in _source accounts_ which have enabled resource tags on their telemetry.
- **Creating tag-based CloudWatch alarms** – After you enable resource tags for telemetry in your account, you can create CloudWatch alarms on tag-based Metrics Insights queries to alert on your AWS infrastructure metrics by tag.
  Example alarms using tag-based queries can be seen in the [CloudWatch Metric Insights alarms documentation](cloudwatch-metrics-insights-alarms.md "cloudwatch-metrics-insights-alarms.md").

## Supported AWS infrastructure metrics

The list below displays the CloudFormation resource that support resource tags for telemetry enrichment in CloudWatch. When you enable resource tags for telemetry, CloudWatch can enrich metrics from these services with their associated resource tags.

- AWS::ApiGatewayV2::Api
- AWS::AppSync::GraphQLApi
- AWS::Athena::CapacityReservation
- AWS::Athena::WorkGroup
- AWS::AutoScaling::AutoScalingGroup
- AWS::Backup::BackupVault
- AWS::CloudFront::Distribution
- AWS::CloudWatch::MetricStream
- AWS::Cognito::UserPool
- AWS::Connect::Instance
- AWS::DataSync::Agent
- AWS::DataSync::Task
- AWS::DocDB::DBCluster
- AWS::DocDB::DBInstance
- AWS::DocDBElastic::Cluster
- AWS::DynamoDB::GlobalTable
- AWS::DynamoDB::Table
- AWS::EC2::CapacityReservation
- AWS::EC2::Host
- AWS::EC2::Instance
- AWS::EC2::NatGateway
- AWS::EC2::TransitGateway
- AWS::EC2::VPC
- AWS::EC2::VPNConnection
- AWS::EC2::Volume
- AWS::ECS::Cluster
- AWS::ECS::Service
- AWS::EFS::FileSystem
- AWS::EKS::Cluster
- AWS::EMR::Cluster
- AWS::ElastiCache::CacheCluster
- AWS::ElastiCache::ReplicationGroup
- AWS::ElasticLoadBalancing::LoadBalancer
- AWS::ElasticLoadBalancingV2::LoadBalancer
- AWS::ElasticLoadBalancingV2::TargetGroup
- AWS::Events::Rule
- AWS::FSx::FileSystem
- AWS::Glue::Job
- AWS::IVSChat::LoggingConfiguration
- AWS::IoT::CACertificate
- AWS::IoT::ScheduledAudit
- AWS::IoT::SecurityProfile
- AWS::IoT::TopicRule
- AWS::KMS::Key
- AWS::Kinesis::Stream
- AWS::KinesisAnalyticsV2::Application
- AWS::KinesisFirehose::DeliveryStream
- AWS::Lambda::Function
- AWS::M2::Application
- AWS::MediaTailor::Channel
- AWS::Neptune::DBCluster
- AWS::Neptune::DBInstance
- AWS::NetworkFirewall::Firewall
- AWS::Pinpoint::App
- AWS::Pipes::Pipe
- AWS::RDS::DBCluster
- AWS::RDS::DBInstance
- AWS::RUM::AppMonitor
- AWS::Redshift::Cluster
- AWS::RedshiftServerless::Namespace
- AWS::RedshiftServerless::Workgroup
- AWS::Route53::HealthCheck
- AWS::S3::Bucket
- AWS::SNS::Topic
- AWS::SQS::Queue
- AWS::SageMaker::Endpoint
- AWS::SageMaker::InferenceComponent
- AWS::Synthetics::Canary
- AWS::Transfer::Connector
- AWS::Transfer::Server
- AWS::VpcLattice::Service
