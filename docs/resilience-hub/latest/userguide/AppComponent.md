# Managing Application Components

An Application Component (AppComponent) is a group of related AWS resources that work
and fail as a single unit. For example, if you have a primary and replica database, both the
databases belong to the same AppComponent. AWS Resilience Hub has rules that govern which AWS
resources can belong to which AppComponent type. For example, a `DBInstance` can
belong to `AWS::ResilienceHub::DatabaseAppComponent` and not to
`AWS::ResilienceHub::ComputeAppComponent`.

The AWS Resilience Hub AppComponents support the following resources:

- `AWS::ResilienceHub::ComputeAppComponent`
  - `AWS::ApiGateway::RestApi`
  - `AWS::ApiGatewayV2::Api`
  - `AWS::AutoScaling::AutoScalingGroup`
  - `AWS::EC2::Instance`
  - `AWS::ECS::Service`
  - `AWS::EKS::Deployment`
  - `AWS::EKS::ReplicaSet`
  - `AWS::EKS::Pod`
  - `AWS::Lambda::Function`
  - `AWS::StepFunctions::StateMachine`

- `AWS::ResilienceHub::DatabaseAppComponent`
  - `AWS::DocDB::DBCluster`
  - `AWS::DynamoDB::Table`
  - `AWS::ElastiCache::CacheCluster`
  - `AWS::ElastiCache::GlobalReplicationGroup`
  - `AWS::ElastiCache::ReplicationGroup`
  - `AWS::ElastiCache::ServerlessCache`
  - `AWS::RDS::DBCluster`
  - `AWS::RDS::DBInstance`

- `AWS::ResilienceHub::NetworkingAppComponent`
  - `AWS::EC2::NatGateway`
  - `AWS::ElasticLoadBalancing::LoadBalancer`
  - `AWS::ElasticLoadBalancingV2::LoadBalancer`
  - `AWS::Route53::RecordSet`

- `AWS:ResilienceHub::NotificationAppComponent`
  - `AWS::SNS::Topic`

- `AWS::ResilienceHub::QueueAppComponent`
  - `AWS::SQS::Queue`

- `AWS::ResilienceHub::StorageAppComponent`
  - `AWS::Backup::BackupPlan`
  - `AWS::EC2::Volume`
  - `AWS::EFS::FileSystem`
  - `AWS::FSx::FileSystem`

  ###### Note

  Currently, AWS Resilience Hub supports Amazon FSx for Windows File Server only.
  - `AWS::S3::Bucket`

###### Topics

- [Grouping resources in an Application
  Component](AppComponent.md "AppComponent.md")
