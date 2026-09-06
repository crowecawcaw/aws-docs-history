

# Required AWS Config resources for control findings
<a name="controls-config-resources"></a>

**Note**  
 If you are using Security Hub CSPM and Security Hub the configuration of the resource recording is managed for you. Security Hub creates a service-linked configuration recorder with AWS Config and gets direct information on all resources that are related to controls supported in Security Hub CSPM. For more information, see [Using the service-linked configuration recorder](securityhub-setup-prereqs.md#service-linked-config-recorder). 

In AWS Security Hub CSPM, some controls use service-linked AWS Config rules that detect configuration changes in your AWS resources. For Security Hub CSPM to generate accurate findings for these controls, you must enable AWS Config and turn on resource recording in AWS Config. For information about how Security Hub CSPM uses AWS Config rules and how to enable and configure AWS Config, see [Enabling and configuring AWS Config for Security Hub CSPM](securityhub-setup-prereqs.md). For detailed information about resource recording, see [Working with the configuration recorder](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html) in the *AWS Config Developer Guide*.

To receive accurate control findings, you must turn on AWS Config resource recording for enabled controls with a *change triggered* schedule type. Some controls with a *periodic* schedule type also require resource recording. This page lists the required resources for these Security Hub CSPM controls.

Security Hub CSPM controls can rely on managed AWS Config rules or custom Security Hub CSPM rules. Make sure there aren't any AWS Identity and Access Management (IAM) policies or AWS Organizations managed policies that prevent AWS Config from having permission to record your resources. Security Hub CSPM controls evaluate resource configurations directly and don’t take AWS Organizations policies into account.

**Note**  
In AWS Regions where a control isn't available, the corresponding resource isn't available in AWS Config. For a list of these limits, see [Regional limits on Security Hub CSPM controls](regions-controls.md).

**Topics**
+ [Required resources for all Security Hub CSPM controls](#all-controls-config-resources)
+ [Required resources for the AWS Foundational Security Best Practices standard](#securityhub-standards-fsbp-config-resources)
+ [Required resources for the CIS AWS Foundations Benchmark](#securityhub-standards-cis-config-resources)
+ [Required resources for the NIST SP 800-53 Revision 5 standard](#nist-config-resources)
+ [Required resources for the NIST SP 800-171 Revision 2 standard](#nist-800-171-config-resources)
+ [Required resources for PCI DSS v3.2.1](#securityhub-standards-pci-config-resources)
+ [Required resources for the AWS Resource Tagging standard](#tagging-config-resources)

## Required resources for all Security Hub CSPM controls
<a name="all-controls-config-resources"></a>

For Security Hub CSPM to generate findings for change triggered controls that are enabled and use an AWS Config rule, you must record the following types of resources in AWS Config. This table also indicates which controls evaluate a particular type of resource. A single control might evaluate more than one type of resource.



- **AWS Amplify**
  - **Resource types:** AWS::Amplify::App / **Related controls:** Amplify.1
  - **Resource types:** AWS::Amplify::Branch / **Related controls:** Amplify.2

- **Amazon API Gateway**
  - **Resource types:** AWS::ApiGateway::Stage / **Related controls:** APIGateway.1<br />APIGateway.2<br />APIGateway.3<br />APIGateway.4<br />APIGateway.5
  - **Resource types:** AWS::ApiGatewayV2::Stage / **Related controls:** APIGateway.1<br />APIGateway.9
  - **Resource types:** AWS::ApiGateway::DomainName / **Related controls:** APIGateway.11

- **AWS AppConfig**
  - **Resource types:** AWS::AppConfig::Application  / **Related controls:** AppConfig.1
  - **Resource types:** AWS::AppConfig::ConfigurationProfile  / **Related controls:** AppConfig.2
  - **Resource types:** AWS::AppConfig::Environment  / **Related controls:** AppConfig.3
  - **Resource types:** AWS::AppConfig::ExtensionAssociation  / **Related controls:** AppConfig.4

- **Amazon AppFlow**
  - **Resource types:** AWS::AppFlow::Flow 
  - **Related controls:** AppFlow.1

- **AWS App Runner**
  - **Resource types:** AWS::AppRunner::Service  / **Related controls:** AppRunner.1
  - **Resource types:** AWS::AppRunner::VpcConnector  / **Related controls:** AppRunner.2

- **AWS AppSync**
  - **Resource types:** AWS::AppSync::GraphQLApi  / **Related controls:** AppSync.2<br />AppSync.4<br />AppSync.5
  - **Resource types:** AWS::AppSync::ApiCache  / **Related controls:** AppSync.1<br />AppSync.6

- **AWS Backup**
  - **Resource types:** AWS::Backup::BackupPlan  / **Related controls:** Backup.5
  - **Resource types:** AWS::Backup::BackupVault  / **Related controls:** Backup.3
  - **Resource types:** AWS::Backup::RecoveryPoint  / **Related controls:** Backup.1<br />Backup.2
  - **Resource types:** AWS::Backup::ReportPlan  / **Related controls:** Backup.4

- **AWS Batch**
  - **Resource types:** AWS::Batch::ComputeEnvironment  / **Related controls:** Batch.3<br />Batch.4
  - **Resource types:** AWS::Batch::JobQueue  / **Related controls:** Batch.1
  - **Resource types:** AWS::Batch::SchedulingPolicy  / **Related controls:** Batch.2

- **Amazon Bedrock**
  - **Resource types:** AWS::Bedrock::DataSource 
  - **Related controls:** Bedrock.1

- **Amazon Bedrock AgentCore**
  - **Resource types:** AWS::BedrockAgentCore::BrowserCustom  / **Related controls:** BedrockAgentCore.5<br />BedrockAgentCore.6
  - **Resource types:** AWS::BedrockAgentCore::CodeInterpreterCustom  / **Related controls:** BedrockAgentCore.7
  - **Resource types:** AWS::BedrockAgentCore::Gateway  / **Related controls:** BedrockAgentCore.2<br />BedrockAgentCore.4
  - **Resource types:** AWS::BedrockAgentCore::Memory  / **Related controls:** BedrockAgentCore.3
  - **Resource types:** AWS::BedrockAgentCore::Runtime  / **Related controls:** BedrockAgentCore.1

- **AWS Certificate Manager (ACM)**
  - **Resource types:** AWS::ACM::Certificate 
  - **Related controls:** ACM.1<br />ACM.2<br />ACM.3

- **Amazon Athena**
  - **Resource types:** AWS::Athena::DataCatalog / **Related controls:** Athena.2
  - **Resource types:** AWS::Athena::WorkGroup / **Related controls:** Athena.3<br />Athena.4

- **AWS CloudFormation**
  - **Resource types:** AWS::CloudFormation::Stack
  - **Related controls:** CloudFormation.2<br />CloudFormation.3<br />CloudFormation.4

- **Amazon CloudFront **
  - **Resource types:** AWS::CloudFront::Distribution 
  - **Related controls:** CloudFront.1<br />CloudFront.3<br />CloudFront.4<br />CloudFront.5<br />CloudFront.6<br />CloudFront.7<br />CloudFront.8<br />CloudFront.9<br />CloudFront.10<br />CloudFront.13<br />CloudFront.14<br />CloudFront.15<br />CloudFront.16<br />CloudFront.17

- **AWS CloudTrail**
  - **Resource types:** AWS::CloudTrail::Trail  / **Related controls:** CloudTrail.9
  - **Resource types:** AWS::CloudTrail::EventDataStore / **Related controls:** CloudTrail.11

- **Amazon CloudWatch**
  - **Resource types:** AWS::CloudWatch::Alarm 
  - **Related controls:** CloudWatch.15<br />CloudWatch.17

- **AWS CodeArtifact**
  - **Resource types:** AWS::CodeArtifact::Repository 
  - **Related controls:** CodeArtifact.1

- **AWS CodeBuild **
  - **Resource types:** AWS::CodeBuild::Project  / **Related controls:** CodeBuild.1<br />CodeBuild.2<br />CodeBuild.3<br />CodeBuild.4
  - **Resource types:** AWS::CodeBuild::ReportGroup  / **Related controls:** CodeBuild.7

- **Amazon CodeGuru Profiler**
  - **Resource types:** AWS::CodeGuruProfiler::ProfilingGroup
  - **Related controls:** CodeGuruProfiler.1

- **Amazon CodeGuru Reviewer**
  - **Resource types:** AWS::CodeGuruReviewer::RepositoryAssociation
  - **Related controls:** CodeGuruReviewer.1

- **Amazon Cognito**
  - **Resource types:** AWS::Cognito::IdentityPool / **Related controls:** Cognito.2
  - **Resource types:** AWS::Cognito::UserPool / **Related controls:** Cognito.1<br />Cognito.3<br />Cognito.4<br />Cognito.5<br />Cognito.6

- **Amazon Connect Customer**
  - **Resource types:** AWS::CustomerProfiles::ObjectType / **Related controls:** Connect.1
  - **Resource types:** AWS::Connect::Instance / **Related controls:** Connect.2

- **AWS DataSync**
  - **Resource types:** AWS::DataSync::Task
  - **Related controls:** DataSync.1<br />DataSync.2

- **Amazon Detective**
  - **Resource types:** AWS::Detective::Graph
  - **Related controls:** Detective.1

- **AWS Database Migration Service (AWS DMS)**
  - **Resource types:** AWS::DMS::Certificate / **Related controls:** DMS.2
  - **Resource types:** AWS::DMS::Endpoint  / **Related controls:** DMS.9<br />DMS.10<br />DMS.11<br />DMS.12
  - **Resource types:** AWS::DMS::EventSubscription  / **Related controls:** DMS.3
  - **Resource types:** AWS::DMS::ReplicationInstance  / **Related controls:** DMS.4<br />DMS.6<br />DMS.13
  - **Resource types:** AWS::DMS::ReplicationSubnetGroup  / **Related controls:** DMS.5
  - **Resource types:** AWS::DMS::ReplicationTask / **Related controls:** DMS.7<br />DMS.8

- **Amazon DynamoDB **
  - **Resource types:** AWS::DynamoDB::Table 
  - **Related controls:** DynamoDB.1<br />DynamoDB.2<br />DynamoDB.5<br />DynamoDB.6

- **Amazon Elastic Compute Cloud (EC2)**
  - **Resource types:** AWS::EC2::ClientVpnEndpoint / **Related controls:** EC2.51
  - **Resource types:** AWS::EC2::CustomerGateway / **Related controls:** EC2.36 
  - **Resource types:** AWS::EC2::DHCPOptions / **Related controls:** EC2.174
  - **Resource types:** AWS::EC2::EIP / **Related controls:** EC2.12<br />EC2.37
  - **Resource types:** AWS::EC2::FlowLog / **Related controls:** EC2.48 
  - **Resource types:** AWS::EC2::Instance / **Related controls:** EC2.4<br />EC2.8<br />EC2.9<br />EC2.17<br />EC2.24<br />EC2.38<br />EMR.1<br />SSM.1
  - **Resource types:** AWS::EC2::InternetGateway / **Related controls:** EC2.39
  - **Resource types:** AWS::EC2::LaunchTemplate / **Related controls:** EC2.25<br />EC2.170<br />EC2.175<br />EC2.181
  - **Resource types:** AWS::EC2::NatGateway / **Related controls:** EC2.40
  - **Resource types:** AWS::EC2::NetworkAcl / **Related controls:** EC2.16<br />EC2.21<br />EC2.41
  - **Resource types:** AWS::EC2::NetworkInterface / **Related controls:** EC2.22<br />EC2.35<br />EC2.180
  - **Resource types:** AWS::EC2::PrefixList / **Related controls:** EC2.176
  - **Resource types:** AWS::EC2::RouteTable / **Related controls:** EC2.42 
  - **Resource types:** AWS::EC2::SecurityGroup / **Related controls:** EC2.2<br />EC2.13<br />EC2.14<br />EC2.18<br />EC2.19<br />EC2.43
  - **Resource types:** AWS::EC2::SnapshotBlockPublicAccess / **Related controls:** EC2.182
  - **Resource types:** AWS::EC2::SpotFleet / **Related controls:** EC2.173
  - **Resource types:** AWS::EC2::Subnet / **Related controls:** EC2.15<br />EC2.44<br />ElastiCache.7
  - **Resource types:** AWS::EC2::TrafficMirrorFilter / **Related controls:** EC2.178
  - **Resource types:** AWS::EC2::TrafficMirrorSession / **Related controls:** EC2.177
  - **Resource types:** AWS::EC2::TrafficMirrorTarget / **Related controls:** EC2.179
  - **Resource types:** AWS::EC2::TransitGateway / **Related controls:** EC2.23<br />EC2.52
  - **Resource types:** AWS::EC2::TransitGatewayAttachment / **Related controls:** EC2.33 
  - **Resource types:** AWS::EC2::TransitGatewayRouteTable / **Related controls:** EC2.34 
  - **Resource types:** AWS::EC2::Volume / **Related controls:** EC2.3<br />EC2.45
  - **Resource types:** AWS::EC2::VPC / **Related controls:** EC2.6<br />EC2.46
  - **Resource types:** AWS::EC2::VPCBlockPublicAccessOptions / **Related controls:** EC2.172
  - **Resource types:** AWS::EC2::VPCEndpointService / **Related controls:** EC2.47 
  - **Resource types:** AWS::EC2::VPCPeeringConnection / **Related controls:** EC2.49 
  - **Resource types:** AWS::EC2::VPNConnection / **Related controls:** EC2.20 EC2.171<br />EC2.183
  - **Resource types:** AWS::EC2::VPNGateway / **Related controls:** EC2.50 

- **Amazon EC2 Auto Scaling**
  - **Resource types:** AWS::AutoScaling::AutoScalingGroup / **Related controls:** AutoScaling.1<br />AutoScaling.2<br />AutoScaling.6<br />AutoScaling.9<br />AutoScaling.10
  - **Resource types:** AWS::AutoScaling::LaunchConfiguration / **Related controls:** AutoScaling.3<br />Autoscaling.5

- **Amazon EC2 Systems Manager (SSM)**
  - **Resource types:** AWS::SSM::AssociationCompliance / **Related controls:** SSM.3
  - **Resource types:** AWS::SSM::ManagedInstanceInventory / **Related controls:** SSM.1
  - **Resource types:** AWS::SSM::PatchCompliance / **Related controls:** SSM.2

- **Amazon Elastic Container Registry (Amazon ECR)**
  - **Resource types:** AWS::ECR::PublicRepository / **Related controls:** ECR.4
  - **Resource types:** AWS::ECR::Repository / **Related controls:** ECR.2<br />ECR.3<br />ECR.5

- **Amazon Elastic Container Service (Amazon ECS)**
  - **Resource types:** AWS::ECS::Cluster / **Related controls:** ECS.12<br />ECS.14
  - **Resource types:** AWS::ECS::CapacityProvider / **Related controls:** ECS.19
  - **Resource types:** AWS::ECS::Service / **Related controls:** ECS.2<br />ECS.10<br />ECS.13
  - **Resource types:** AWS::ECS::TaskDefinition / **Related controls:** ECS.3<br />ECS.4<br />ECS.5<br />ECS.8<br />ECS.9<br />ECS.15<br />ECS.17<br />ECS.18<br />ECS.20<br />ECS.21
  - **Resource types:** AWS::ECS::TaskSet / **Related controls:** ECS.16

- **Amazon Elastic File System (Amazon EFS)**
  - **Resource types:** AWS::EFS::AccessPoint  / **Related controls:** EFS.3<br />EFS.4<br />EFS.5
  - **Resource types:** AWS::EFS::FileSystem  / **Related controls:** EFS.7<br />EFS.8

- **Amazon Elastic Kubernetes Service (Amazon EKS)**
  - **Resource types:** AWS::EKS::Cluster / **Related controls:** EKS.2<br />EKS.6<br />EKS.8
  - **Resource types:** AWS::EKS::IdentityProviderConfig / **Related controls:** EKS.7
  - **Resource types:** AWS::EKS::Nodegroup / **Related controls:** EKS.9

- **AWS Elastic Beanstalk**
  - **Resource types:** AWS::ElasticBeanstalk::Environment 
  - **Related controls:** ElasticBeanstalk.1<br />ElasticBeanstalk.2<br />ElasticBeanstalk.3

- **Elastic Load Balancing**
  - **Resource types:** AWS::ElasticLoadBalancing::LoadBalancer / **Related controls:** ELB.2<br />ELB.3<br />ELB.5<br />ELB.7<br />ELB.8<br />ELB.9<br />ELB.10<br />ELB.14
  - **Resource types:** AWS::ElasticLoadBalancingV2::Listener / **Related controls:** ELB.17<br />ELB.18
  - **Resource types:** AWS::ElasticLoadBalancingV2::LoadBalancer / **Related controls:** ELB.1<br />ELB.4<br />ELB.5<br />ELB.6<br />ELB.12<br />ELB.13<br />ELB.16

- **ElasticSearch**
  - **Resource types:** AWS::Elasticsearch::Domain
  - **Related controls:** ES.3<br />ES.4<br />ES.5<br />ES.6<br />ES.7<br />ES.8<br />ES.9

- **Amazon EMR**
  - **Resource types:** AWS::EMR::SecurityConfiguration
  - **Related controls:** EMR.3<br />EMR.4

- **Amazon EventBridge**
  - **Resource types:** AWS::Events::EventBus / **Related controls:** EventBridge.2<br />EventBridge.3
  - **Resource types:** AWS::Events::Endpoint / **Related controls:** EventBridge.4

- **Amazon Fraud Detector**
  - **Resource types:** AWS::FraudDetector::EntityType / **Related controls:** FraudDetector.1
  - **Resource types:** AWS::FraudDetector::Label / **Related controls:** FraudDetector.2
  - **Resource types:** AWS::FraudDetector::Outcome / **Related controls:** FraudDetector.3
  - **Resource types:** AWS::FraudDetector::Variable / **Related controls:** FraudDetector.4

- **AWS Global Accelerator**
  - **Resource types:** AWS::GlobalAccelerator::Accelerator
  - **Related controls:** GlobalAccelerator.1

- **AWS Glue**
  - **Resource types:** AWS::Glue::Job / **Related controls:** Glue.1<br />Glue.4
  - **Resource types:** AWS::Glue::MLTransform / **Related controls:** Glue.3

- **Amazon GuardDuty**
  - **Resource types:** AWS::GuardDuty::Detector / **Related controls:** GuardDuty.4
  - **Resource types:** AWS::GuardDuty::Filter / **Related controls:** GuardDuty.2
  - **Resource types:** AWS::GuardDuty::IPSet / **Related controls:** GuardDuty.3

- **AWS Identity and Access Management (IAM)**
  - **Resource types:** AWS::IAM::Group / **Related controls:** IAM.27<br />KMS.2
  - **Resource types:** AWS::IAM::Policy / **Related controls:** IAM.1<br />IAM.21<br />KMS.1
  - **Resource types:** AWS::IAM::Role / **Related controls:** IAM.24<br />IAM.27<br />KMS.2
  - **Resource types:** AWS::IAM::User / **Related controls:** IAM.2<br />IAM.3<br />IAM.5<br />IAM.8<br />IAM.19<br />IAM.22<br />IAM.25<br />IAM.27<br />KMS.2

- **AWS Identity and Access Management Access Analyzer**
  - **Resource types:** AWS::AccessAnalyzer::Analyzer
  - **Related controls:** IAM.23

- **Amazon Interactive Video Service (Amazon IVS)**
  - **Resource types:** AWS::IVS::PlaybackKeyPair / **Related controls:** IVS.1
  - **Resource types:** AWS::IVS::RecordingConfiguration / **Related controls:** IVS.2
  - **Resource types:** AWS::IVS::Channel / **Related controls:** IVS.3

- **AWS IoT**
  - **Resource types:** AWS::IoT::Authorizer / **Related controls:** IoT.4
  - **Resource types:** AWS::IoT::Dimension / **Related controls:** IoT.3
  - **Resource types:** AWS::IoT::MitigationAction / **Related controls:** IoT.2
  - **Resource types:** AWS::IoT::Policy / **Related controls:** IoT.6
  - **Resource types:** AWS::IoT::RoleAlias / **Related controls:** IoT.5
  - **Resource types:** AWS::IoT::SecurityProfile / **Related controls:** IoT.1

- **AWS IoT Events**
  - **Resource types:** AWS::IoTEvents::AlarmModel / **Related controls:** IoTEvents.3
  - **Resource types:** AWS::IoTEvents::DetectorModel / **Related controls:** IoTEvents.2
  - **Resource types:** AWS::IoTEvents::Input / **Related controls:** IoTEvents.1

- **AWS IoT SiteWise**
  - **Resource types:** AWS::IoTSiteWise::AssetModel / **Related controls:** IoTSiteWise.1
  - **Resource types:** AWS::IoTSiteWise::Dashboard / **Related controls:** IoTSiteWise.2
  - **Resource types:** AWS::IoTSiteWise::Gateway / **Related controls:** IoTSiteWise.3
  - **Resource types:** AWS::IoTSiteWise::Portal / **Related controls:** IoTSiteWise.4
  - **Resource types:** AWS::IoTSiteWise::Project / **Related controls:** IoTSiteWise.5

- **AWS IoT TwinMaker**
  - **Resource types:** AWS::IoTTwinMaker::Entity / **Related controls:** IoTTwinMaker.4
  - **Resource types:** AWS::IoTTwinMaker::Scene / **Related controls:** IoTTwinMaker.3
  - **Resource types:** AWS::IoTTwinMaker::SyncJob / **Related controls:** IoTTwinMaker.1
  - **Resource types:** AWS::IoTTwinMaker::Workspace / **Related controls:** IoTTwinMaker.2

- **AWS IoT Wireless**
  - **Resource types:** AWS::IoTWireless::MulticastGroup / **Related controls:** IoTWireless.1
  - **Resource types:** AWS::IoTWireless::ServiceProfile / **Related controls:** IoTWireless.2
  - **Resource types:** AWS::IoTWireless::FuotaTask / **Related controls:** IoTWireless.3

- **Amazon Keyspaces (for Apache Cassandra)**
  - **Resource types:** AWS::Cassandra::Keyspace
  - **Related controls:** Keyspaces.1

- **Amazon Kinesis**
  - **Resource types:** AWS::Kinesis::Stream
  - **Related controls:** Kinesis.1<br />Kinesis.2<br />Kinesis.3

- **AWS Key Management Service (AWS KMS)**
  - **Resource types:** AWS::KMS::Alias / **Related controls:** S3.17
  - **Resource types:** AWS::KMS::Key / **Related controls:** KMS.3<br />KMS.5<br />S3.17

- **AWS Lambda**
  - **Resource types:** AWS::Lambda::Function
  - **Related controls:** Lambda.1<br />Lambda.2<br />Lambda.3<br />Lambda.5<br />Lambda.6<br />Lambda.7

- **Amazon MSK**
  - **Resource types:** AWS::MSK::Cluster / **Related controls:** MSK.1<br />MSK.2<br />MSK.4<br />MSK.6
  - **Resource types:** AWS::KafkaConnect::Connector / **Related controls:** MSK.3<br />MSK.5

- **Amazon MQ**
  - **Resource types:** AWS::AmazonMQ::Broker
  - **Related controls:** MQ.2<br />MQ.4<br />MQ.5<br />MQ.6

- **AWS Network Firewall**
  - **Resource types:** AWS::NetworkFirewall::Firewall / **Related controls:** NetworkFirewall.1<br />NetworkFirewall.7<br />NetworkFirewall.9<br />NetworkFirewall.10
  - **Resource types:** AWS::NetworkFirewall::FirewallPolicy / **Related controls:** NetworkFirewall.3<br />NetworkFirewall.4<br />NetworkFirewall.5<br />NetworkFirewall.8
  - **Resource types:** AWS::NetworkFirewall::RuleGroup / **Related controls:** NetworkFirewall.6

- **Amazon OpenSearch Service**
  - **Resource types:** AWS::OpenSearch::Domain
  - **Related controls:** Opensearch.1<br />Opensearch.2<br />Opensearch.3<br />Opensearch.4<br />Opensearch.5<br />Opensearch.6<br />Opensearch.7<br />Opensearch.8<br />Opensearch.9<br />Opensearch.10<br />Opensearch.11

- **AWS Private CA**
  - **Resource types:** AWS::ACMPCA::CertificateAuthority
  - **Related controls:** PCA.2

- **Amazon Relational Database Service (Amazon RDS)**
  - **Resource types:** AWS::RDS::DBCluster / **Related controls:** DocumentDB.1<br />DocumentDB.2<br />DocumentDB.4<br />DocumentDB.5<br />Neptune.1<br />Neptune.2<br />Neptune.4<br />Neptune.5<br />Neptune.7<br />Neptune.8<br />Neptune.9<br />RDS.7<br />RDS.12<br />RDS.14<br />RDS.15<br />RDS.16<br />RDS.24<br />RDS.27<br />RDS.28<br />RDS.34<br />RDS.35<br />RDS.37<br />RDS.47<br />RDS.48
  - **Resource types:** AWS::RDS::DBClusterSnapshot / **Related controls:** DocumentDB.3<br />Neptune.3<br />Neptune.6<br />RDS.1<br />RDS.4<br />RDS.29
  - **Resource types:** AWS::RDS::DBInstance / **Related controls:** RDS.2<br />RDS.3<br />RDS.5<br />RDS.6<br />RDS.8<br />RDS.9<br />RDS.10<br />RDS.11<br />RDS.13<br />RDS.17<br />RDS.23<br />RDS.25<br />RDS.30<br />RDS.36<br />RDS.40
  - **Resource types:** AWS::RDS::DBSecurityGroup / **Related controls:** RDS.31
  - **Resource types:** AWS::RDS::DBSnapshot / **Related controls:** RDS.1<br />RDS.4<br />RDS.32
  - **Resource types:** AWS::RDS::DBSubnetGroup / **Related controls:** RDS.33
  - **Resource types:** AWS::RDS::EventSubscription / **Related controls:** RDS.19<br />RDS.20<br />RDS.21<br />RDS.22
  - **Resource types:** AWS::RDS::GlobalCluster / **Related controls:** RDS.51

- **Amazon Redshift**
  - **Resource types:** AWS::Redshift::Cluster / **Related controls:** Redshift.1<br />Redshift.2<br />Redshift.3<br />Redshift.4<br />Redshift.6<br />Redshift.7<br />Redshift.8<br />Redshift.10<br />Redshift.11<br />Redshift.18
  - **Resource types:** AWS::Redshift::ClusterParameterGroup / **Related controls:** Redshift.2<br />Redshift.17
  - **Resource types:** AWS::Redshift::ClusterSnapshot / **Related controls:** Redshift.13
  - **Resource types:** AWS::Redshift::ClusterSubnetGroup / **Related controls:** Redshift.14<br />Redshift.16
  - **Resource types:** AWS::Redshift::EventSubscription / **Related controls:** Redshift.12

- **Amazon Route 53**
  - **Resource types:** AWS::Route53::HostedZone / **Related controls:** Route53.2
  - **Resource types:** AWS::Route53::HealthCheck / **Related controls:** Route53.1

- **Amazon Simple Storage Service (Amazon S3)**
  - **Resource types:** AWS::S3::AccessPoint / **Related controls:** S3.19
  - **Resource types:** AWS::S3::AccountPublicAccessBlock / **Related controls:** S3.2<br />S3.3
  - **Resource types:** AWS::S3::Bucket / **Related controls:** CloudTrail.6<br />CloudTrail.7<br />S3.2<br />S3.3<br />S3.5<br />S3.6<br />S3.7<br />S3.8<br />S3.9<br />S3.10<br />S3.11<br />S3.12<br />S3.13<br />S3.14<br />S3.15<br />S3.17<br />S3.20
  - **Resource types:** AWS::S3::MultiRegionAccessPoint / **Related controls:** S3.24
  - **Resource types:** AWS::S3Express::DirectoryBucket / **Related controls:** S3.25

- **Amazon SageMaker AI **
  - **Resource types:** AWS::SageMaker::AppImageConfig  / **Related controls:** SageMaker.6
  - **Resource types:** AWS::SageMaker::Image  / **Related controls:** SageMaker.7
  - **Resource types:** AWS::SageMaker::InferenceExperiment  / **Related controls:** SageMaker.23<br />SageMaker.24
  - **Resource types:** AWS::SageMaker::Model  / **Related controls:** SageMaker.5<br />SageMaker.16<br />SageMaker.19
  - **Resource types:** AWS::SageMaker::ModelExplainabilityJobDefinition  / **Related controls:** SageMaker.20
  - **Resource types:** AWS::SageMaker::ModelQualityJobDefinition  / **Related controls:** SageMaker.25
  - **Resource types:** AWS::SageMaker::MonitoringSchedule  / **Related controls:** SageMaker.22
  - **Resource types:** AWS::SageMaker::NotebookInstance  / **Related controls:** SageMaker.2<br />SageMaker.3<br />SageMaker.21
  - **Resource types:** AWS::SageMaker::FeatureGroup  / **Related controls:** SageMaker.17<br />SageMaker.18

- **AWS Secrets Manager **
  - **Resource types:** AWS::SecretsManager::Secret 
  - **Related controls:** SecretsManager.1<br />SecretsManager.2<br />SecretsManager.5

- **AWS Service Catalog **
  - **Resource types:** AWS::ServiceCatalog::Portfolio 
  - **Related controls:** ServiceCatalog.1

- **Amazon Simple Email Service (Amazon SES) **
  - **Resource types:** AWS::SES::ConfigurationSet  / **Related controls:** SES.2<br />SES.3
  - **Resource types:** AWS::SES::ContactList  / **Related controls:** SES.1

- **Amazon Simple Notification Service (Amazon SNS) **
  - **Resource types:** AWS::SNS::Topic 
  - **Related controls:** SNS.1<br />SNS.3<br />SNS.4

- **Amazon Simple Queue Service (Amazon SQS) **
  - **Resource types:** AWS::SQS::Queue 
  - **Related controls:** SQS.1<br />SQS.2<br />SQS.3

- **AWS Step Functions**
  - **Resource types:** AWS::StepFunctions::StateMachine / **Related controls:** StepFunctions.1
  - **Resource types:** AWS::StepFunctions::Activity / **Related controls:** StepFunctions.2

- **AWS Systems Manager (SSM) **
  - **Resource types:** AWS::SSM::Document 
  - **Related controls:** SSM.5

- **AWS Transfer Family**
  - **Resource types:** AWS::Transfer::Agreement / **Related controls:** Transfer.4
  - **Resource types:** AWS::Transfer::Certificate / **Related controls:** Transfer.5
  - **Resource types:** AWS::Transfer::Connector / **Related controls:** Transfer.3<br />Transfer.6
  - **Resource types:** AWS::Transfer::Profile / **Related controls:** Transfer.7
  - **Resource types:** AWS::Transfer::Workflow / **Related controls:** Transfer.1

- **AWS WAF**
  - **Resource types:** AWS::WAF::Rule / **Related controls:** WAF.6
  - **Resource types:** AWS::WAF::RuleGroup / **Related controls:** WAF.7
  - **Resource types:** AWS::WAF::WebACL / **Related controls:** WAF.1<br />WAF.8
  - **Resource types:** AWS::WAFRegional::Rule / **Related controls:** WAF.2
  - **Resource types:** AWS::WAFRegional::RuleGroup / **Related controls:** WAF.3
  - **Resource types:** AWS::WAFRegional::WebACL / **Related controls:** WAF.4
  - **Resource types:** AWS::WAFv2::RuleGroup / **Related controls:** WAF.12
  - **Resource types:** AWS::WAFv2::WebACL / **Related controls:** WAF.10<br />WAF.11

- **Amazon WorkSpaces**
  - **Resource types:** AWS::WorkSpaces::WorkSpace
  - **Related controls:** WorkSpaces.1<br />WorkSpaces.2



## Required resources for the AWS Foundational Security Best Practices standard
<a name="securityhub-standards-fsbp-config-resources"></a>

For Security Hub CSPM to accurately report findings for change triggered controls that apply to the AWS Foundational Security Best Practices standard (v.1.0.0), are enabled, and use an AWS Config rule, you must record the following types of resources in AWS Config. For information about this standard, see [AWS Foundational Security Best Practices standard in Security Hub CSPM](fsbp-standard.md).


| AWS service | Resource types | 
| --- | --- | 
| Amazon API Gateway | `AWS::ApiGateway::DomainName`, `AWS::ApiGateway::Stage`, `AWS::ApiGatewayV2::Stage` | 
| AWS AppSync | `AWS::AppSync::ApiCache`, `AWS::AppSync::GraphQLApi` | 
| AWS Backup | `AWS::Backup::RecoveryPoint` | 
| Amazon Bedrock | `AWS::Bedrock::DataSource` | 
| Amazon Bedrock AgentCore | `AWS::BedrockAgentCore::BrowserCustom`, `AWS::BedrockAgentCore::CodeInterpreterCustom`, `AWS::BedrockAgentCore::Gateway`, `AWS::BedrockAgentCore::Runtime` | 
| AWS Certificate Manager (ACM) | `AWS::ACM::Certificate` | 
| AWS CloudFormation | `AWS::CloudFormation::Stack` | 
| Amazon CloudFront | `AWS::CloudFront::Distribution` | 
| AWS CodeBuild | `AWS::CodeBuild::Project`, `AWS::CodeBuild::ReportGroup` | 
| Amazon Cognito | `AWS::Cognito::IdentityPool`, `AWS::Cognito::UserPool` | 
| AWS CloudTrail | `AWS::CloudTrail::EventDataStore` | 
| Amazon Connect Customer | `AWS::Connect::Instance` | 
| AWS DataSync | `AWS::DataSync::Task` | 
| AWS Database Migration Service (AWS DMS) | `AWS::DMS::Endpoint`, `AWS::DMS::ReplicationInstance`, `AWS::DMS::ReplicationTask` | 
| Amazon DynamoDB | `AWS::DynamoDB::Table` | 
| Amazon EC2 Systems Manager (SSM)  | `AWS::SSM::AssociationCompliance`, `AWS::SSM::ManagedInstanceInventory`, `AWS::SSM::PatchCompliance` | 
| Amazon Elastic Compute Cloud (Amazon EC2) | `AWS::EC2::ClientVpnEndpoint`, `AWS::EC2::Instance`, `AWS::EC2::LaunchTemplate`, `AWS::EC2::NetworkAcl`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`, `AWS::EC2::SnapshotBlockPublicAccess`, `AWS::EC2::SpotFleet`, `AWS::EC2::Subnet`, `AWS::EC2::TransitGateway`, `AWS::EC2::VPCBlockPublicAccessOptions`, `AWS::EC2::VPNConnection`, `AWS::EC2::Volume` | 
| Amazon EC2 Auto Scaling | `AWS::AutoScaling::AutoScalingGroup`, `AWS::AutoScaling::LaunchConfiguration` | 
| Amazon Elastic Container Registry (Amazon ECR) | `AWS::ECR::Repository` | 
| Amazon Elastic Container Service (Amazon ECS) | `AWS::ECS::CapacityProvider`, `AWS::ECS::Cluster`, `AWS::ECS::Service`, `AWS::ECS::TaskDefinition`, `AWS::ECS::TaskSet` | 
| Amazon Elastic File System (Amazon EFS) | `AWS::EFS::AccessPoint`, `AWS::EFS::FileSystem` | 
| Amazon Elastic Kubernetes Service (Amazon EKS) | `AWS::EKS::Cluster`, `AWS::EKS::Nodegroup` | 
| AWS Elastic Beanstalk | `AWS::ElasticBeanstalk::Environment` | 
| Elastic Load Balancing | `AWS::ElasticLoadBalancing::LoadBalancer`, `AWS::ElasticLoadBalancingV2::Listener`, `AWS::ElasticLoadBalancingV2::LoadBalancer` | 
| ElasticSearch | `AWS::Elasticsearch::Domain` | 
| Amazon EMR | `AWS::EMR::SecurityConfiguration` | 
| AWS Glue | `AWS::Glue::Job`, `AWS::Glue::MLTransform` | 
| AWS Identity and Access Management (IAM) | `AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`, `AWS::IAM::User` | 
| Amazon Kinesis | `AWS::Kinesis::Stream` | 
| AWS Key Management Service (AWS KMS) | `AWS::KMS::Key` | 
| AWS Lambda | `AWS::Lambda::Function` | 
| Amazon Managed Streaming for Apache Kafka (Amazon MSK) | `AWS::MSK::Cluster`, `AWS::KafkaConnect::Connector` | 
| AWS Network Firewall | `AWS::NetworkFirewall::Firewall`, `AWS::NetworkFirewall::FirewallPolicy`, `AWS::NetworkFirewall::RuleGroup` | 
| Amazon OpenSearch Service | `AWS::OpenSearch::Domain` | 
| Amazon Relational Database Service (Amazon RDS) | `AWS::RDS::DBCluster`, `AWS::RDS::DBClusterSnapshot`, `AWS::RDS::DBInstance`, `AWS::RDS::DBProxy`, `AWS::RDS::DBSnapshot`, `AWS::RDS::EventSubscription`, `AWS::RDS::GlobalCluster` | 
| Amazon Redshift | `AWS::Redshift::Cluster`, `AWS::Redshift::ClusterSubnetGroup` | 
| Amazon Redshift Serverless | `AWS::RedshiftServerless::Workgroup` | 
| Amazon Route 53 | `AWS::Route53::HostedZone` | 
| Amazon Simple Storage Service (Amazon S3) | `AWS::S3::AccessPoint`, `AWS::S3::AccountPublicAccessBlock`, `AWS::S3::Bucket`, `AWS::S3::MultiRegionAccessPoint`, `AWS::S3Express::DirectoryBucket` | 
| Amazon SageMaker AI | `AWS::SageMaker::FeatureGroup`, `AWS::SageMaker::InferenceExperiment`, `AWS::SageMaker::Model`, `AWS::SageMaker::ModelExplainabilityJobDefinition`, `AWS::SageMaker::ModelQualityJobDefinition`, `AWS::SageMaker::MonitoringSchedule`, `AWS::SageMaker::NotebookInstance` | 
| Amazon Simple Notification Service (Amazon SNS) | `AWS::SNS::Topic` | 
| Amazon Simple Queue Service (Amazon SQS) | `AWS::SQS::Queue` | 
| AWS Secrets Manager | `AWS::SecretsManager::Secret` | 
| AWS Step Functions | `AWS::StepFunctions::StateMachine` | 
| AWS Transfer Family | `AWS::Transfer::Connector` | 
| AWS WAF | `AWS::WAF::Rule`, `AWS::WAF::RuleGroup`, `AWS::WAF::WebACL`, `AWS::WAFRegional::Rule`, `AWS::WAFRegional::RuleGroup`, `AWS::WAFRegional::WebACL`, `AWS::WAFv2::RuleGroup`, `AWS::WAFv2::WebACL` | 
| Amazon WorkSpaces | `AWS::WorkSpaces::WorkSpace` | 

## Required resources for the CIS AWS Foundations Benchmark
<a name="securityhub-standards-cis-config-resources"></a>

To run security checks for enabled controls that apply to the Center for Internet Security (CIS) AWS Foundations Benchmark, Security Hub CSPM either runs through the exact audit steps prescribed for the checks or uses specific AWS Config managed rules. For information about this standard in Security Hub CSPM, see [CIS AWS Foundations Benchmark in Security Hub CSPM](cis-aws-foundations-benchmark.md).

### Required resources for CIS v5.0.0
<a name="cis-5.0-config-resources"></a>

For Security Hub CSPM to accurately report findings for enabled CIS v5.0.0 change triggered controls that use an AWS Config rule, you must record the following types of resources in AWS Config.


| AWS service | Resource types | 
| --- | --- | 
| Amazon Elastic Compute Cloud (Amazon EC2) | `AWS::EC2::Instance`, `AWS::EC2::NetworkAcl`, `AWS::EC2::SecurityGroup`, `AWS::EC2::VPC` | 
| Amazon Elastic File System (Amazon EFS) | `AWS::EFS::FileSystem` | 
| AWS Identity and Access Management (IAM) | `AWS::IAM::Group`, `AWS::IAM::User`, `AWS::IAM::Role` | 
| Amazon Relational Database Service (Amazon RDS) | `AWS::RDS::DBInstance`, `AWS::RDS::DBCluster` | 
| Amazon Simple Storage Service (Amazon S3) | `AWS::S3::Bucket` | 

### Required resources for CIS v3.0.0
<a name="cis-3.0-config-resources"></a>

For Security Hub CSPM to accurately report findings for enabled CIS v3.0.0 change triggered controls that use an AWS Config rule, you must record the following types of resources in AWS Config.


| AWS service | Resource types | 
| --- | --- | 
| Amazon Elastic Compute Cloud (Amazon EC2) | `AWS::EC2::Instance`, `AWS::EC2::NetworkAcl`, `AWS::EC2::SecurityGroup`, `AWS::EC2::VPC` | 
| AWS Identity and Access Management (IAM) | `AWS::IAM::Group`, `AWS::IAM::User`, `AWS::IAM::Role` | 
| Amazon Relational Database Service (Amazon RDS) | `AWS::RDS::DBInstance` | 
| Amazon Simple Storage Service (Amazon S3) | `AWS::S3::Bucket` | 

### Required resources for CIS v1.4.0
<a name="cis-1.4-config-resources"></a>

For Security Hub CSPM to accurately report findings for enabled CIS v1.4.0 change triggered controls that use an AWS Config rule, you must record the following types of resources in AWS Config.


| AWS service | Resource types | 
| --- | --- | 
| Amazon Elastic Compute Cloud (Amazon EC2) | `AWS::EC2::NetworkAcl`, `AWS::EC2::SecurityGroup` | 
| AWS Identity and Access Management (IAM) | `AWS::IAM::Policy`, `AWS::IAM::User` | 
| Amazon Relational Database Service (Amazon RDS) | `AWS::RDS::DBInstance` | 
| Amazon Simple Storage Service (Amazon S3) | `AWS::S3::Bucket` | 

### Required resources for CIS v1.2.0
<a name="cis-1.2-config-resources"></a>

For Security Hub CSPM to accurately report findings for enabled CIS v1.2.0 change triggered controls that use an AWS Config rule, you must record the following types of resources in AWS Config.


| AWS service | Resource types | 
| --- | --- | 
| Amazon Elastic Compute Cloud (Amazon EC2) | `AWS::EC2::SecurityGroup` | 
| AWS Identity and Access Management (IAM) | `AWS::IAM::Policy`, `AWS::IAM::User` | 

## Required resources for the NIST SP 800-53 Revision 5 standard
<a name="nist-config-resources"></a>

For Security Hub CSPM to accurately report findings for change triggered controls that apply to the NIST SP 800-53 Revision 5 standard, are enabled, and use an AWS Config rule, you must record the following types of resources in AWS Config. For information about this standard, see [NIST SP 800-53 Revision 5 in Security Hub CSPM](standards-reference-nist-800-53.md).


| AWS service | Resource types | 
| --- | --- | 
| Amazon API Gateway | `AWS::ApiGateway::Stage`, `AWS::ApiGatewayV2::Stage` | 
| AWS AppSync | `AWS::AppSync::GraphQLApi` | 
| AWS Backup | `AWS::Backup::RecoveryPoint` | 
| Amazon Bedrock AgentCore | `AWS::BedrockAgentCore::Gateway`, `AWS::BedrockAgentCore::Memory` | 
| AWS Certificate Manager (ACM) | `AWS::ACM::Certificate` | 
| AWS CloudFormation | `AWS::CloudFormation::Stack` | 
| Amazon CloudFront | `AWS::CloudFront::Distribution` | 
| Amazon CloudWatch | `AWS::CloudWatch::Alarm` | 
| AWS CodeBuild | `AWS::CodeBuild::Project` | 
| AWS Database Migration Service (AWS DMS) | `AWS::DMS::Endpoint`, `AWS::DMS::ReplicationInstance`, `AWS::DMS::ReplicationTask` | 
| Amazon DynamoDB | `AWS::DynamoDB::Table` | 
| Amazon Elastic Compute Cloud (Amazon EC2) | `AWS::EC2::ClientVpnEndpoint`, `AWS::EC2::EIP`, `AWS::EC2::Instance`, `AWS::EC2::LaunchTemplate`, `AWS::EC2::NetworkAcl`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`, `AWS::EC2::Subnet`, `AWS::EC2::TransitGateway`, `AWS::EC2::VPNConnection`, `AWS::EC2::Volume` | 
| Amazon EC2 Auto Scaling | `AWS::AutoScaling::AutoScalingGroup`, `AWS::AutoScaling::LaunchConfiguration` | 
| Amazon Elastic Container Registry (Amazon ECR) | `AWS::ECR::Repository` | 
| Amazon Elastic Container Service (Amazon ECS) | `AWS::ECS::Cluster`, `AWS::ECS::Service`, `AWS::ECS::TaskDefinition` | 
| Amazon Elastic File System (Amazon EFS) | `AWS::EFS::AccessPoint` | 
| Amazon Elastic Kubernetes Service (Amazon EKS) | `AWS::EKS::Cluster` | 
| AWS Elastic Beanstalk | `AWS::ElasticBeanstalk::Environment` | 
| Elastic Load Balancing | `AWS::ElasticLoadBalancing::LoadBalancer`, `AWS::ElasticLoadBalancingV2::Listener`, `AWS::ElasticLoadBalancingV2::LoadBalancer` | 
| Amazon ElasticSearch | `AWS::Elasticsearch::Domain` | 
| Amazon EMR | `AWS::EMR::SecurityConfiguration` | 
| Amazon EventBridge | `AWS::Events::Endpoint`, `AWS::Events::EventBus` | 
| AWS Glue | `AWS::Glue::Job` | 
| AWS Identity and Access Management (IAM) | `AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`, `AWS::IAM::User` | 
| AWS Key Management Service (AWS KMS) | `AWS::KMS::Alias`, `AWS::KMS::Key` | 
| Amazon Kinesis | `AWS::Kinesis::Stream` | 
| AWS Lambda | `AWS::Lambda::Function` | 
| Amazon Managed Streaming for Apache Kafka (Amazon MSK) | `AWS::MSK::Cluster` | 
| Amazon MQ | `AWS::AmazonMQ::Broker` | 
| AWS Network Firewall | `AWS::NetworkFirewall::Firewall`, `AWS::NetworkFirewall::FirewallPolicy`, `AWS::NetworkFirewall::RuleGroup` | 
| Amazon OpenSearch Service | `AWS::OpenSearch::Domain` | 
| Amazon Relational Database Service (Amazon RDS) | `AWS::RDS::DBCluster`, `AWS::RDS::DBClusterSnapshot`, `AWS::RDS::DBInstance`, `AWS::RDS::DBSnapshot`, `AWS::RDS::EventSubscription` | 
| Amazon Redshift | `AWS::Redshift::Cluster`, `AWS::Redshift::ClusterSubnetGroup` | 
| Amazon Route 53 | `AWS::Route53::HostedZone` | 
| Amazon Simple Storage Service (Amazon S3) | `AWS::S3::AccessPoint`, `AWS::S3::AccountPublicAccessBlock`, `AWS::S3::Bucket` | 
| AWS Service Catalog | `AWS::ServiceCatalog::Portfolio` | 
| Amazon Simple Notification Service (Amazon SNS) | `AWS::SNS::Topic` | 
| Amazon Simple Queue Service (Amazon SQS) | `AWS::SQS::Queue` | 
| Amazon EC2 Systems Manager (SSM)  | `AWS::SSM::AssociationCompliance`, `AWS::SSM::ManagedInstanceInventory`, `AWS::SSM::PatchCompliance` | 
| Amazon SageMaker AI | `AWS::SageMaker::FeatureGroup`, `AWS::SageMaker::NotebookInstance` | 
| AWS Secrets Manager | `AWS::SecretsManager::Secret` | 
| AWS Transfer Family | `AWS::Transfer::Connector` | 
| AWS WAF | `AWS::WAF::Rule`, `AWS::WAF::RuleGroup`, `AWS::WAF::WebACL`, `AWS::WAFRegional::Rule`, `AWS::WAFRegional::RuleGroup`, `AWS::WAFRegional::WebACL`, `AWS::WAFv2::RuleGroup`, `AWS::WAFv2::WebACL` | 

## Required resources for the NIST SP 800-171 Revision 2 standard
<a name="nist-800-171-config-resources"></a>

For Security Hub CSPM to accurately report findings for change triggered controls that apply to the NIST SP 800-171 Revision 2 standard, are enabled, and use an AWS Config rule, you must record the following types of resources in AWS Config. For information about this standard, see [NIST SP 800-171 Revision 2 in Security Hub CSPM](standards-reference-nist-800-171.md).


| AWS service | Resource types | 
| --- | --- | 
| AWS Certificate Manager (ACM) | `AWS::ACM::Certificate` | 
| Amazon API Gateway | `AWS::ApiGateway::Stage` | 
| Amazon CloudFront | `AWS::CloudFront::Distribution` | 
| Amazon CloudWatch | `AWS::CloudWatch::Alarm` | 
| Amazon Elastic Compute Cloud (Amazon EC2) | `AWS::EC2::ClientVpnEndpoint`, `AWS::EC2::NetworkAcl`, `AWS::EC2::SecurityGroup`, `AWS::EC2::VPC`, `AWS::EC2::VPNConnection` | 
| Elastic Load Balancing | `AWS::ElasticLoadBalancing::LoadBalancer` | 
| AWS Identity and Access Management (IAM) | `AWS::IAM::Policy`, `AWS::IAM::User` | 
| AWS Key Management Service (AWS KMS) | `AWS::KMS::Alias`, `AWS::KMS::Key` | 
| AWS Network Firewall | `AWS::NetworkFirewall::FirewallPolicy`, `AWS::NetworkFirewall::RuleGroup` | 
| Amazon Simple Storage Service (Amazon S3) | `AWS::S3::Bucket` | 
| Amazon Simple Notification Service (Amazon SNS) | `AWS::SNS::Topic` | 
| AWS Systems Manager (SSM) | `AWS::SSM::PatchCompliance` | 
| AWS WAF | `AWS::WAFv2::RuleGroup` | 

## Required resources for PCI DSS v3.2.1
<a name="securityhub-standards-pci-config-resources"></a>

For Security Hub CSPM to accurately report findings for controls that apply to v3.2.1 of the Payment Card Industry Data Security Standard (PCI DSS), are enabled, and use an AWS Config rule, you must record the following types of resources in AWS Config. For information about this standard, see [PCI DSS in Security Hub CSPM](pci-standard.md).


| AWS service | Resource types | 
| --- | --- | 
| AWS CodeBuild | `AWS::CodeBuild::Project` | 
| Amazon Elastic Compute Cloud (Amazon EC2) | `AWS::EC2::EIP`, `AWS::EC2::Instance`, `AWS::EC2::SecurityGroup` | 
| Amazon EC2 Auto Scaling | `AWS::AutoScaling::AutoScalingGroup` | 
| AWS Identity and Access Management (IAM) | `AWS::IAM::Policy`, `AWS::IAM::User` | 
| AWS Lambda | `AWS::Lambda::Function` | 
| Amazon OpenSearch Service | `AWS::OpenSearch::Domain` | 
| Amazon Relational Database Service (Amazon RDS) | `AWS::RDS::DBClusterSnapshot`, `AWS::RDS::DBInstance`, `AWS::RDS::DBSnapshot` | 
| Amazon Redshift | `AWS::Redshift::Cluster` | 
| Amazon Simple Storage Service (Amazon S3) | `AWS::S3::AccountPublicAccessBlock`, `AWS::S3::Bucket` | 
| Amazon EC2 Systems Manager (SSM)  | `AWS::SSM::AssociationCompliance`, `AWS::SSM::ManagedInstanceInventory`, `AWS::SSM::PatchCompliance` | 

## Required resources for the AWS Resource Tagging standard
<a name="tagging-config-resources"></a>

All the controls that apply to the AWS Resource Tagging standard are change triggered and use an AWS Config rule. For Security Hub CSPM to accurately report findings for these controls, you must record the following types of resources in AWS Config. For information about this standard, see [AWS Resource Tagging standard in Security Hub CSPM](standards-tagging.md).


| AWS service | Resource types | 
| --- | --- | 
| AWS Amplify | `AWS::Amplify::App`, `AWS::Amplify::Branch` | 
| Amazon AppFlow  | `AWS::AppFlow::Flow` | 
| AWS App Runner  | `AWS::AppRunner::Service`, `AWS::AppRunner::VpcConnector` | 
| AWS AppConfig  | `AWS::AppConfig::Application`, `AWS::AppConfig::ConfigurationProfile`, `AWS::AppConfig::Environment`, `AWS::AppConfig::ExtensionAssociation` | 
| AWS AppSync  | `AWS::AppSync::GraphQLApi` | 
| Amazon Athena  | `AWS::Athena::DataCatalog`, `AWS::Athena::WorkGroup` | 
| AWS Backup | `AWS::Backup::BackupPlan`, `AWS::Backup::BackupVault`, `AWS::Backup::RecoveryPlan`, `AWS::Backup::ReportPlan` | 
| AWS Batch  | `AWS::Batch::ComputeEnvironment`, `AWS::Batch::JobQueue`, `AWS::Batch::SchedulingPolicy` | 
| AWS Certificate Manager (ACM)  | `AWS::ACM::Certificate` | 
| AWS CloudFormation  | `AWS::CloudFormation::Stack` | 
| Amazon CloudFront  | `AWS::CloudFront::Distribution` | 
| AWS CloudTrail  | `AWS::CloudTrail::Trail` | 
| AWS CodeArtifact  | `AWS::CodeArtifact::Repository` | 
| Amazon CodeGuru  | `AWS::CodeGuruProfiler::ProfilingGroup`, `AWS::CodeGuruReviewer::RepositoryAssociation` | 
| Amazon Connect Customer  | `AWS::CustomerProfiles::ObjectType` | 
| AWS Database Migration Service (AWS DMS)  | `AWS::DMS::Certificate`, `AWS::DMS::EventSubscription`<br />`AWS::DMS::ReplicationInstance`, `AWS::DMS::ReplicationSubnetGroup` | 
| AWS DataSync | `AWS::DataSync::Task` | 
| Amazon Detective  | `AWS::Detective::Graph` | 
| Amazon DynamoDB  | `AWS::DynamoDB::Trail` | 
| Amazon Elastic Compute Cloud (EC2)  | `AWS::EC2::CustomerGateway`, `AWS::EC2::DHCPOptions`, `AWS::EC2::EIP`, `AWS::EC2::FlowLog`, `AWS::EC2::Instance`, `AWS::EC2::InternetGateway`, `AWS::EC2::LaunchTemplate`, `AWS::EC2::NatGateway`, `AWS::EC2::NetworkAcl`, `AWS::EC2::NetworkInterface`, `AWS::EC2::PrefixList`, `AWS::EC2::RouteTable`, `AWS::EC2::SecurityGroup`, `AWS::EC2::Subnet`, `AWS::EC2::TrafficMirrorFilter`, `AWS::EC2::TrafficMirrorSession`, `AWS::EC2::TrafficMirrorTarget`, `AWS::EC2::TransitGateway`, `AWS::EC2::TransitGatewayAttachment`, `AWS::EC2::TransitGatewayRouteTable`, `AWS::EC2::Volume`, `AWS::EC2::VPC`, `AWS::EC2::VPCEndpointService`, `AWS::EC2::VPCPeeringConnection`, `AWS::EC2::VPNGateway` | 
| Amazon EC2 Auto Scaling  | `AWS::AutoScaling::AutoScalingGroup` | 
| Amazon Elastic Container Registry (Amazon ECR)  | `AWS::ECR::PublicRepository` | 
| Amazon Elastic Container Service (Amazon ECS)  | `AWS::ECS::Cluster`, `AWS::ECS::Service`, `AWS::ECS::TaskDefinition` | 
| Amazon Elastic File System (Amazon EFS)  | `AWS::EFS::AccessPoint` | 
| Amazon Elastic Kubernetes Service (Amazon EKS)  | `AWS::EKS::Cluster`, `AWS::EKS::IdentityProviderConfig` | 
| AWS Elastic Beanstalk | `AWS::ElasticBeanstalk::Environment` | 
| ElasticSearch  | `AWS::Elasticsearch::Domain` | 
| Amazon EventBridge  | `AWS::Events::EventBus` | 
| Amazon Fraud Detector  | `AWS::FraudDetector::EntityType`, `AWS::FraudDetector::Label`<br />`AWS::FraudDetector::Outcome`, `AWS::FraudDetector::Variable` | 
| AWS Global Accelerator  | `AWS::GlobalAccelerator::Accelerator` | 
| AWS Glue  | `AWS::Glue::Job` | 
| Amazon GuardDuty  | `AWS::GuardDuty::Detector`, `AWS::GuardDuty::Filter`, `AWS::GuardDuty::IPSet` | 
| AWS Identity and Access Management (IAM)  | `AWS::IAM::Role`, `AWS::IAM::User` | 
| AWS Identity and Access Management Access Analyzer (IAM Access Analyzer)  | `AWS::AccessAnalyzer::Analyzer` | 
| AWS IoT  | `AWS::IoT::Authorizer`, `AWS::IoT::Dimension`, `AWS::IoT::MitigationAction`, `AWS::IoT::Policy`, `AWS::IoT::RoleAlias`, `AWS::IoT::SecurityProfile` | 
| AWS IoT Events  | `AWS::IoTEvents::AlarmModel`, `AWS::IoTEvents::DetectorModel`, `AWS::IoTEvents::Input` | 
| AWS IoT SiteWise  | `AWS::IoTSiteWise::Dashboard`, `AWS::IoTSiteWise::Gateway`, `AWS::IoTSiteWise::Portal`, `AWS::IoTSiteWise::Project` | 
| AWS IoT TwinMaker  | `AWS::IoTTwinMaker::Entity`, `AWS::IoTTwinMaker::Scene`, `AWS::IoTTwinMaker::SyncJob`, `AWS::IoTTwinMaker::Workspace` | 
| AWS IoT Wireless  | `AWS::IoTWireless::FuotaTask`, `AWS::IoTWireless::MulticastGroup`, `AWS::IoTWireless::ServiceProfile` | 
| Amazon Interactive Video Service (Amazon IVS)  | `AWS::IVS::Channel`, `AWS::IVS::PlaybackKeyPair`, `AWS::IVS::RecordingConfiguration` | 
| Amazon Keyspaces (for Apache Cassandra)  | `AWS::Cassandra::Keyspace` | 
| Amazon Kinesis  | `AWS::Kinesis::Stream` | 
| AWS Lambda  | `AWS::Lambda::Function` | 
| Amazon MQ  | `AWS::AmazonMQ::Broker` | 
| AWS Network Firewall  | `AWS::NetworkFirewall::Firewall`, `AWS::NetworkFirewall::FirewallPolicy` | 
| Amazon OpenSearch Service | `AWS::OpenSearch::Domain` | 
| AWS Private Certificate Authority | `AWS::ACMPCA::CertificateAuthority` | 
| Amazon Relational Database Service  | `AWS::RDS::DBCluster`, `AWS::RDS::DBClusterSnapshot`, `AWS::RDS::DBInstance`, `AWS::RDS::DBSecurityGroup`, `AWS::RDS::DBSnapshot`, `AWS::RDS::DBSubnetGroup` | 
| Amazon Redshift  | `AWS::Redshift::Cluster`, `AWS::Redshift::ClusterParameterGroup`, `AWS::Redshift::ClusterSnapshot`, `AWS::Redshift::ClusterSubnetGroup`, `AWS::Redshift::EventSubscription` | 
| Amazon Route 53  | `AWS::Route53::HealthCheck` | 
| Amazon SageMaker AI | `AWS::SageMaker::AppImageConfig`, `AWS::SageMaker::Image` | 
| AWS Secrets Manager  | `AWS::SecretsManager::Secret` | 
| Amazon Simple Email Service (Amazon SES)  | `AWS::SES::ConfigurationSet`, `AWS::SES::ContactList` | 
| Amazon Simple Notification Service (Amazon SNS)  | `AWS::SNS::Topic` | 
| Amazon Simple Queue Service (Amazon SQS)  | `AWS::SQS::Queue` | 
| AWS Step Functions  | `AWS::StepFunctions::Activity` | 
| AWS Systems Manager (SSM) | `AWS::SSM::Document` | 
| AWS Transfer Family | `AWS::Transfer::Agreement`, `AWS::Transfer::Certificate`, `AWS::Transfer::Connector`, `AWS::Transfer::Profile`, `AWS::Transfer::Workflow` | 