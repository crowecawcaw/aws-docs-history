

# Using AWS Config for resource discovery
<a name="omni-using-aws-config-for-resource-discovery"></a>

CloudWatch Omni uses AWS Config to find the AWS resources in your account. Omni then adds those resources to the context graph. This page lists the resource types that AWS Config records for Omni, and describes how the recorder works.

To learn how discovered resources appear in the graph, see [Using Context Graph](omni-using-context-graph.md).

**How the recorder works**

Omni creates a *service-linked configuration recorder* when you create a space. The recorder is named `AWSConfigurationRecorderForCloudWatch`. You do not create it. You do not configure it.

A service-linked recorder belongs to the service that it is linked to. That service sets the resource types to record. To learn more, see [Working with the configuration recorder](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html) in the *AWS Config Developer Guide*.

The recorder works as follows:
+ **You pay no AWS Config fee.** Omni uses an internal recording scope. AWS Config does not send these records to your delivery channel, and you cannot read them in AWS Config. You can still see the recorder itself in the AWS Config console.
+ **The recorder's settings are fixed.** You cannot change them in AWS Config. You cannot rename the recorder, and you cannot start it or stop it. Omni sets which resource types the recorder records, and it records the same types in every account.
+ **You can delete the recorder, but not while a space uses it.** When you call `DeleteServiceLinkedConfigurationRecorder`, AWS Config asks Omni whether it still uses the recorder. While your space has an active AWS Config integration, Omni answers yes and your call fails. To remove the recorder, delete the space first.
+ **Deleting the recorder stops resource discovery.** Omni keeps the resources that it already found, and it adds no new ones. AWS Config keeps the records that it already made.
+ **Your own recorder is separate.** Omni does not change or use your customer managed recorder.

**Note**  
Other CloudWatch features also create service-linked recorders. Your account can hold more than one recorder that is linked to CloudWatch.

**Which resources become graph nodes**

AWS Config records every type in the resource-type table on this page. Omni adds a graph node for only some of those types. Omni uses the other records to add detail to nodes that exist. For example, Omni reads subnet and security group records. It uses them to find the network address of a service.

A resource can appear in the graph before Omni gets telemetry from it. To learn more, see [Using Context Graph](omni-using-context-graph.md).

**Regions**

Omni creates the recorder in the same Region as your space. The recorder records the resources in that Region.

To add the resources from another Region, centralize that Region's telemetry into the space's account. For more information, see [Set up Omni for your organization](omni-set-up-omni-for-your-organization.md).

AWS Config makes a record only for a type that AWS Config supports in the Region. If AWS Config does not support a type in a Region, no resource of that type appears in the graph for that Region.

**Describe calls in CloudTrail**

AWS Config takes an inventory of the resources in your account at regular times. It does this for all resources, not only for the types that this page lists. You can therefore see `ConfigResourceCompositionSession` and `AWSConfig-Describe` calls in CloudTrail, including calls for types that Omni does not record. This behavior keeps the AWS Config inventory consistent.

**Recorded resource types**

AWS Config records the following resource types for Omni.


| Category | AWS service | Resource types | 
| --- | --- | --- | 
| Compute | AWS App Runner | AWS::AppRunner::Service | 
| Compute | AWS Elastic Beanstalk | AWS::ElasticBeanstalk::Environment | 
| Compute | AWS Lambda | AWS::Lambda::Function | 
| Compute | Amazon EC2 | AWS::EC2::Instance AWS::EC2::LaunchTemplate | 
| Compute | Amazon EC2 Auto Scaling | AWS::AutoScaling::AutoScalingGroup AWS::AutoScaling::LaunchConfiguration | 
| Compute | Amazon ECS | AWS::ECS::CapacityProvider AWS::ECS::Cluster AWS::ECS::Service AWS::ECS::TaskDefinition AWS::ECS::TaskSet | 
| Compute | Amazon EKS | AWS::EKS::Cluster AWS::EKS::FargateProfile AWS::EKS::Nodegroup | 
| Compute | Amazon WorkSpaces | AWS::WorkSpaces::Workspace | 
| Networking and content delivery | AWS Global Accelerator | AWS::GlobalAccelerator::Accelerator | 
| Networking and content delivery | Amazon CloudFront | AWS::CloudFront::Distribution | 
| Networking and content delivery | Amazon Route 53 | AWS::Route53::HostedZone | 
| Networking and content delivery | Amazon VPC | AWS::EC2::ClientVpnEndpoint AWS::EC2::EIP AWS::EC2::FlowLog AWS::EC2::InternetGateway AWS::EC2::NatGateway AWS::EC2::NetworkInterface AWS::EC2::RouteTable AWS::EC2::SecurityGroup AWS::EC2::Subnet AWS::EC2::TransitGateway AWS::EC2::TransitGatewayAttachment AWS::EC2::VPC AWS::EC2::VPCEndpoint AWS::EC2::VPCPeeringConnection AWS::EC2::VPNConnection AWS::EC2::VPNGateway | 
| Networking and content delivery | Elastic Load Balancing | AWS::ElasticLoadBalancing::LoadBalancer AWS::ElasticLoadBalancingV2::Listener AWS::ElasticLoadBalancingV2::LoadBalancer AWS::ElasticLoadBalancingV2::TargetGroup | 
| APIs | AWS AppSync | AWS::AppSync::GraphQLApi | 
| APIs | Amazon API Gateway | AWS::ApiGateway::Method AWS::ApiGateway::RestApi AWS::ApiGateway::Stage AWS::ApiGatewayV2::Api AWS::ApiGatewayV2::Integration AWS::ApiGatewayV2::Stage | 
| Databases and storage | Amazon DynamoDB | AWS::DynamoDB::Table | 
| Databases and storage | Amazon EFS | AWS::EFS::FileSystem | 
| Databases and storage | Amazon Keyspaces | AWS::Cassandra::Keyspace | 
| Databases and storage | Amazon OpenSearch Service | AWS::Elasticsearch::Domain AWS::OpenSearch::Domain | 
| Databases and storage | Amazon QLDB | AWS::QLDB::Ledger | 
| Databases and storage | Amazon RDS | AWS::RDS::DBCluster AWS::RDS::DBInstance | 
| Databases and storage | Amazon Redshift | AWS::Redshift::Cluster | 
| Databases and storage | Amazon S3 | AWS::S3::AccessPoint AWS::S3::Bucket | 
| Application integration | AWS IoT Core | AWS::IoT::TopicRule | 
| Application integration | AWS Step Functions | AWS::StepFunctions::Activity AWS::StepFunctions::StateMachine | 
| Application integration | Amazon Data Firehose | AWS::KinesisFirehose::DeliveryStream | 
| Application integration | Amazon EventBridge | AWS::Events::ApiDestination AWS::Events::Connection AWS::Events::EventBus AWS::Events::Rule | 
| Application integration | Amazon EventBridge Scheduler | AWS::Scheduler::ScheduleGroup | 
| Application integration | Amazon Kinesis Data Streams | AWS::Kinesis::Stream | 
| Application integration | Amazon MQ | AWS::AmazonMQ::Broker | 
| Application integration | Amazon MSK | AWS::MSK::Cluster AWS::MSK::ServerlessCluster | 
| Application integration | Amazon SNS | AWS::SNS::Topic | 
| Application integration | Amazon SQS | AWS::SQS::Queue | 
| Containers and service discovery | AWS Cloud Map | AWS::ServiceDiscovery::HttpNamespace AWS::ServiceDiscovery::PublicDnsNamespace AWS::ServiceDiscovery::Service | 
| Containers and service discovery | Amazon ECR | AWS::ECR::PublicRepository AWS::ECR::Repository | 
| Security and identity | AWS Certificate Manager | AWS::ACM::Certificate | 
| Security and identity | AWS IAM | AWS::IAM::Policy AWS::IAM::Role | 
| Security and identity | AWS KMS | AWS::KMS::Key | 
| Security and identity | AWS Network Firewall | AWS::NetworkFirewall::Firewall | 
| Security and identity | AWS Secrets Manager | AWS::SecretsManager::Secret | 
| Security and identity | AWS WAF | AWS::WAFv2::WebACL | 
| Security and identity | Amazon Cognito | AWS::Cognito::IdentityPool AWS::Cognito::UserPool | 
| Management and governance | AWS CloudFormation | AWS::CloudFormation::Stack | 
| Management and governance | AWS CloudTrail | AWS::CloudTrail::Trail | 
| Management and governance | Amazon CloudWatch | AWS::CloudWatch::Alarm AWS::CloudWatch::MetricStream | 
| Management and governance | Amazon CloudWatch Logs | AWS::Logs::Destination | 
| Machine learning | Amazon Bedrock | AWS::Bedrock::DataSource AWS::Bedrock::Guardrail AWS::Bedrock::KnowledgeBase AWS::Bedrock::Prompt | 
| Machine learning | Amazon Kendra | AWS::Kendra::Index | 
| Machine learning | Amazon Lex | AWS::Lex::Bot AWS::Lex::BotAlias | 
| Machine learning | Amazon SageMaker AI | AWS::SageMaker::Domain AWS::SageMaker::EndpointConfig AWS::SageMaker::Model AWS::SageMaker::NotebookInstance | 
| Analytics | AWS Glue | AWS::Glue::Crawler AWS::Glue::Database AWS::Glue::Job | 
| Analytics | Amazon Athena | AWS::Athena::WorkGroup | 
| Analytics | Amazon QuickSight | AWS::QuickSight::DataSource | 
| Developer tools and migration | AWS CodeBuild | AWS::CodeBuild::Project | 
| Developer tools and migration | AWS CodeDeploy | AWS::CodeDeploy::Application AWS::CodeDeploy::DeploymentGroup | 
| Developer tools and migration | AWS CodePipeline | AWS::CodePipeline::Pipeline | 
| Developer tools and migration | AWS DMS | AWS::DMS::ReplicationInstance | 
| Developer tools and migration | AWS Transfer Family | AWS::Transfer::Server | 
| Developer tools and migration | Amazon AppFlow | AWS::AppFlow::Flow | 

**Related information**
+ [Using Context Graph](omni-using-context-graph.md)
+ [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md)
+ [Working with the configuration recorder](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html) in the *AWS Config Developer Guide*