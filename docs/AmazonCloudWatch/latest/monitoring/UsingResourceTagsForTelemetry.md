# Using resource tags for telemetry

Once you have enabled resource tags for telemetry, you can use this enriched data to create powerful monitoring solutions that scale with your infrastructure. Use tag-based queries to group and filter metrics across multiple resources, create dynamic alarms that
automatically adapt to resource changes, and gain insights into your AWS environment organized by meaningful business or operational categories. This approach enables you to monitor resources by team, environment, application, or any other tagging strategy you use in your
organization.

- **Creating tag-based Metrics Insights queries** – After you enable resource tags for telemetry in your account, you can create tag-based Metrics Insights queries to discover and visualize your AWS infrastructure metrics by tag. Example queries using tags can be seen in the
  [CloudWatch Metrics Insights query builder documentation](cloudwatch-metrics-insights-buildquery.md "cloudwatch-metrics-insights-buildquery.md"). _Monitoring accounts_ can also make tag-based queries for
  metrics in _source accounts_ which have enabled resource tags on their telemetry.
- **Creating tag-based CloudWatch alarms** – After you enable resource tags for telemetry in your account, you can create CloudWatch alarms on tag-based Metrics Insights queries to alert on your AWS infrastructure metrics by tag.
  Example alarms using tag-based queries can be seen in the [CloudWatch Metric Insights alarms documentation](cloudwatch-metrics-insights-alarms.md "cloudwatch-metrics-insights-alarms.md").
- **Querying AWS metrics with PromQL using resource tags** – After you enable resource tags for telemetry in your account, you can enable OTel enrichment to query your AWS infrastructure metrics using PromQL with resource tags as labels. This lets you filter, aggregate, and alert on metrics by any tag you've applied to your AWS resources. For more information, see
  [Enabling vended metrics in PromQL](CloudWatch-OTelEnrichment.md "CloudWatch-OTelEnrichment.md"). For example queries using tags, see
  [Querying vended AWS metrics with PromQL](CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Vended "CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Vended").
- **Creating tag-based CloudWatch Logs Insights queries** – After you enable resource tags for telemetry in your account, log events from supported resources are enriched with the associated resource tags. You can create tag-based Logs Insights queries to discover your log events by tag using facets such as `@aws.tag.env` or `@aws.tag.team`. For example: `filter @aws.tag.env = 'production'`. For more information, see the [CloudWatch Logs Insights query syntax documentation](../logs/CWL_QuerySyntax.md "../logs/CWL_QuerySyntax.md").

## Supported AWS resources

The following table lists the AWS resources that support resource tags for telemetry enrichment. When you enable resource tags for telemetry, CloudWatch can enrich metrics and log events from these resources with their associated resource tags.

For the specific metrics that CloudWatch enriches for each resource type, see [Supported metrics for resource tags for telemetry](SupportedMetricsForResourceTagsForTelemetry.md "SupportedMetricsForResourceTagsForTelemetry.md").

| Resource type                               | Metrics | Logs |
| ------------------------------------------- | ------- | ---- |
| `AWS::APS::RuleGroupsNamespace`             | Yes     | No   |
| `AWS::APS::Workspace`                       | Yes     | Yes  |
| `AWS::ApiGatewayV2::Api`                    | Yes     | No   |
| `AWS::AppFlow::Flow`                        | Yes     | No   |
| `AWS::AppSync::GraphQLApi`                  | Yes     | Yes  |
| `AWS::Athena::CapacityReservation`          | Yes     | No   |
| `AWS::Athena::WorkGroup`                    | Yes     | No   |
| `AWS::Backup::BackupVault`                  | Yes     | No   |
| `AWS::CloudFront::Distribution`             | Yes     | Yes  |
| `AWS::CloudFront::Function`                 | No      | Yes  |
| `AWS::CloudWatch::MetricStream`             | Yes     | No   |
| `AWS::CodeGuruProfiler::ProfilingGroup`     | Yes     | No   |
| `AWS::Cognito::UserPool`                    | Yes     | Yes  |
| `AWS::Connect::Instance`                    | Yes     | Yes  |
| `AWS::DAX::Cluster`                         | Yes     | No   |
| `AWS::DataSync::Agent`                      | Yes     | No   |
| `AWS::DataSync::Task`                       | Yes     | No   |
| `AWS::DocDB::DBCluster`                     | Yes     | No   |
| `AWS::DocDB::DBInstance`                    | Yes     | No   |
| `AWS::DocDBElastic::Cluster`                | Yes     | No   |
| `AWS::DynamoDB::GlobalTable`                | Yes     | No   |
| `AWS::DynamoDB::Table`                      | Yes     | No   |
| `AWS::EC2::CapacityReservation`             | Yes     | No   |
| `AWS::EC2::ClientVpnEndpoint`               | Yes     | No   |
| `AWS::EC2::Host`                            | Yes     | No   |
| `AWS::EC2::Instance`                        | Yes     | Yes  |
| `AWS::EC2::NatGateway`                      | Yes     | No   |
| `AWS::EC2::TransitGateway`                  | Yes     | Yes  |
| `AWS::EC2::VPC`                             | Yes     | Yes  |
| `AWS::EC2::VPNConnection`                   | Yes     | Yes  |
| `AWS::EC2::Volume`                          | Yes     | No   |
| `AWS::ECS::Cluster`                         | Yes     | Yes  |
| `AWS::ECS::Service`                         | Yes     | No   |
| `AWS::EFS::FileSystem`                      | Yes     | No   |
| `AWS::EKS::Cluster`                         | Yes     | Yes  |
| `AWS::EMR::Cluster`                         | Yes     | No   |
| `AWS::EMRServerless::Application`           | Yes     | No   |
| `AWS::ElastiCache::CacheCluster`            | Yes     | Yes  |
| `AWS::ElastiCache::ReplicationGroup`        | Yes     | No   |
| `AWS::ElasticBeanstalk::Environment`        | Yes     | No   |
| `AWS::ElasticLoadBalancing::LoadBalancer`   | Yes     | No   |
| `AWS::ElasticLoadBalancingV2::LoadBalancer` | Yes     | Yes  |
| `AWS::ElasticLoadBalancingV2::TargetGroup`  | Yes     | No   |
| `AWS::Events::Rule`                         | Yes     | No   |
| `AWS::FSx::FileSystem`                      | Yes     | No   |
| `AWS::FraudDetector::Detector`              | Yes     | No   |
| `AWS::GameLift::GameSessionQueue`           | Yes     | No   |
| `AWS::GameLift::MatchmakingConfiguration`   | Yes     | No   |
| `AWS::Glue::Job`                            | Yes     | No   |
| `AWS::IVSChat::LoggingConfiguration`        | Yes     | No   |
| `AWS::IoT::CACertificate`                   | Yes     | No   |
| `AWS::IoT::ScheduledAudit`                  | Yes     | No   |
| `AWS::IoT::SecurityProfile`                 | Yes     | No   |
| `AWS::IoT::TopicRule`                       | Yes     | No   |
| `AWS::KMS::Key`                             | Yes     | No   |
| `AWS::Kendra::DataSource`                   | Yes     | No   |
| `AWS::Kendra::Index`                        | Yes     | No   |
| `AWS::Kinesis::Stream`                      | Yes     | No   |
| `AWS::KinesisAnalyticsV2::Application`      | Yes     | No   |
| `AWS::KinesisFirehose::DeliveryStream`      | Yes     | No   |
| `AWS::Lambda::Function`                     | Yes     | Yes  |
| `AWS::M2::Application`                      | Yes     | No   |
| `AWS::MediaTailor::Channel`                 | Yes     | No   |
| `AWS::MemoryDB::Cluster`                    | Yes     | No   |
| `AWS::Neptune::DBCluster`                   | Yes     | No   |
| `AWS::Neptune::DBInstance`                  | Yes     | No   |
| `AWS::NetworkFirewall::Firewall`            | Yes     | Yes  |
| `AWS::OpenSearchServerless::Collection`     | Yes     | No   |
| `AWS::OpenSearchService::Domain`            | Yes     | No   |
| `AWS::Pinpoint::App`                        | Yes     | No   |
| `AWS::Pipes::Pipe`                          | Yes     | Yes  |
| `AWS::RDS::DBCluster`                       | Yes     | Yes  |
| `AWS::RDS::DBInstance`                      | Yes     | No   |
| `AWS::RUM::AppMonitor`                      | Yes     | Yes  |
| `AWS::Redshift::Cluster`                    | Yes     | No   |
| `AWS::RedshiftServerless::Namespace`        | Yes     | No   |
| `AWS::RedshiftServerless::Workgroup`        | Yes     | No   |
| `AWS::Route53::HealthCheck`                 | Yes     | No   |
| `AWS::Route53Resolver::FirewallRuleGroup`   | Yes     | No   |
| `AWS::Route53Resolver::ResolverEndpoint`    | Yes     | No   |
| `AWS::S3::Bucket`                           | Yes     | No   |
| `AWS::SNS::Topic`                           | Yes     | No   |
| `AWS::SQS::Queue`                           | Yes     | No   |
| `AWS::SageMaker::Endpoint`                  | Yes     | No   |
| `AWS::SageMaker::InferenceComponent`        | Yes     | No   |
| `AWS::Scheduler::ScheduleGroup`             | Yes     | No   |
| `AWS::Synthetics::Canary`                   | Yes     | No   |
| `AWS::Transfer::Connector`                  | Yes     | Yes  |
| `AWS::Transfer::Server`                     | Yes     | Yes  |
| `AWS::VpcLattice::Service`                  | Yes     | Yes  |
| `AWS::WorkSpaces::Workspace`                | Yes     | No   |
| `AWS::WorkSpaces::WorkspacesPool`           | Yes     | No   |
