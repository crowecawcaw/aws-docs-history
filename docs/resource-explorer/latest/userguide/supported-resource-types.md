# Resource types you can search for with

Resource Explorer

Resource Explorer supports resource types across numerous AWS services. Resource discovery happens
automatically when you access Resource Explorer with appropriate permissions. If you have, at minimum,
the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy, you can
immediately search all tagged resources and supported untagged resources created after the
[immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release. For complete resource discovery with automatic updates, you'll
also need the `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy). After the service-linked role is
created in your account by any user, subsequent users need only the permissions in the
`AWSResourceExplorerReadOnlyAccess` managed policy to get complete
results.

###### Topics

- [Supported services and resource types](#types-list "#types-list")
- [Programmatically accessing the list of supported
  resource types](#programmatic-access "#programmatic-access")
- [Resource types that appear as other
  types](#resource-type-exceptions "#resource-type-exceptions")
  Some resource types are identified by [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") strings that share a common format
  with another resource type. When this happens, Resource Explorer can report such resources as that
  other resource type. For list of resource types affected by this issue, see [Resource types that appear as other
  types](#resource-type-exceptions "#resource-type-exceptions").

At this time, tags attached to AWS Identity and Access Management (IAM) resources, such as roles or users, can't
be used for searching.

If you have encrypted access to some of your resources, Resource Explorer is unable to discover them.
You will not see these resources in your search results.

The following tables list the resource types that are supported for searching in
AWS Resource Explorer.

###### Note

As of February 10, 2026, Resource Explorer no longer supports the following resource types:

- **Amazon Chime**—
  `chime:media-pipeline`
  As of February 10, 2026, Resource Explorer no longer supports the following resource types:

- **Amazon Location Service**—
  `geo:map`
- **Amazon Location Service**—
  `geo:place-index`
- **Amazon Location Service**—
  `geo:tracker`
  As of December 5, 2025, Resource Explorer no longer supports the following resource types:

- **AWS IoT Analytics**—
  `iotanalytics:channel`
- **AWS IoT Analytics**—
  `iotanalytics:dataset`
- **AWS IoT Analytics**—
  `iotanalytics:datastore`
- **AWS IoT Analytics**—
  `iotanalytics:pipeline`
  As of November 21, 2025, Resource Explorer no longer supports the following resource types:

- **AWS IoT FleetWise**—
  `iotfleethub:application`
  As of November 3, 2025, Resource Explorer no longer supports the following resource types:

- **Amazon Lookout for Metrics**—
  `lookoutmetrics:Alert`
- **Amazon Lookout for Metrics**—
  `lookoutmetrics:AnomalyDetector`
- **Amazon Lookout for Vision**—
  `lookoutvision:project`
  As of October 13, 2025, Resource Explorer no longer supports the following resource types:

- **Amazon CloudWatch Evidently**—
  `evidently:project`
- **Amazon CloudWatch Evidently**—
  `evidently:project/experiment`
- **Amazon CloudWatch Evidently**—
  `evidently:project/feature`
- **Amazon CloudWatch Evidently**—
  `evidently:project/launch`
  As of October 1, 2025, Resource Explorer no longer supports the following resource types:

- **Amazon Quantum Ledger Database (Amazon QLDB)** —
  `qldb:ledger`
- **Amazon Quantum Ledger Database (Amazon QLDB)** —
  `qldb:stream`
  As of July 9, 2024, Resource Explorer no longer supports the following resource types:

- **Amazon Elastic Container Service** —
  `ecs:task`
- **AWS Systems Manager** —
  `ssm:automation-execution`
- **AWS Systems Manager** —
  `ssm:patchbaseline`

## Supported services and resource types

###### Supported AWS services

- [Amazon API Gateway](#services-apigateway "#services-apigateway")
- [Direct Connect](#services-directconnect "#services-directconnect")
- [AWS Partner Network](#services-partnercentral "#services-partnercentral")
- [AWS Shield](#services-shield "#services-shield")
- [AWS Systems Manager Incident Manager](#services-ssm-incidents "#services-ssm-incidents")
- [AWS WAFV2](#services-wafv2 "#services-wafv2")
- [Amazon Macie](#services-macie2 "#services-macie2")
- [OpenSearch Service Serverless Service](#services-aoss "#services-aoss")
- [Amazon S3 Express](#services-s3express "#services-s3express")
- [Amazon VPC Lattice](#services-vpc-lattice "#services-vpc-lattice")
- [Amazon Verified Permissions](#services-verifiedpermissions "#services-verifiedpermissions")
- [Amazon WorkSpaces Web](#services-workspaces-web "#services-workspaces-web")
- [AWS Amplify](#services-amplify "#services-amplify")
- [AWS App Runner](#services-apprunner "#services-apprunner")
- [AWS AppConfig](#services-appconfig "#services-appconfig")
- [Amazon AppFlow](#services-appflow "#services-appflow")
- [AppIntegrations](#services-app-integrations "#services-app-integrations")
- [AWS App Mesh](#services-appmesh "#services-appmesh")
- [Amazon AppStream](#services-appstream "#services-appstream")
- [AWS AppSync](#services-appsync "#services-appsync")
- [AWS Application Discovery Service](#services-ds "#services-ds")
- [Amazon Application Recovery Controller (ARC)](#services-route53-recovery-control "#services-route53-recovery-control")
- [Amazon Athena](#services-athena "#services-athena")
- [AWS Audit Manager](#services-auditmanager "#services-auditmanager")
- [AWS Backup](#services-backup "#services-backup")
- [AWS Backup gateway](#services-backup-gateway "#services-backup-gateway")
- [AWS Batch](#services-batch "#services-batch")
- [Amazon Bedrock](#services-bedrock "#services-bedrock")
- [AWS Certificate Manager](#services-acm "#services-acm")
- [Amazon Chime](#services-chime "#services-chime")
- [AWS Cloud Map](#services-servicediscovery "#services-servicediscovery")
- [AWS Cloud9](#services-cloud9 "#services-cloud9")
- [CloudFormation](#services-cloudformation "#services-cloudformation")
- [Amazon CloudFront](#services-cloudfront "#services-cloudfront")
- [AWS CloudTrail](#services-cloudtrail "#services-cloudtrail")
- [Amazon CloudWatch](#services-cloudwatch "#services-cloudwatch")
- [Amazon CloudWatch Logs](#services-logs "#services-logs")
- [Amazon CloudWatch Observability Access Manager](#services-oam "#services-oam")
- [Amazon CloudWatch RUM](#services-rum "#services-rum")
- [Amazon CloudWatch Synthetics](#services-synthetics "#services-synthetics")
- [AWS CodeArtifact](#services-codeartifact "#services-codeartifact")
- [AWS CodeBuild](#services-codebuild "#services-codebuild")
- [AWS CodeCommit](#services-codecommit "#services-codecommit")
- [AWS CodeConnections](#services-codeconnections "#services-codeconnections")
- [AWS CodeDeploy](#services-codedeploy "#services-codedeploy")
- [Amazon CodeGuru Profiler](#services-codeguru-profiler "#services-codeguru-profiler")
- [Amazon CodeGuru Reviewer](#services-codeguru-reviewer "#services-codeguru-reviewer")
- [AWS CodePipeline](#services-codepipeline "#services-codepipeline")
- [AWS CodeStar Connections](#services-codestar-connections "#services-codestar-connections")
- [Amazon Cognito Identity](#services-cognito-identity "#services-cognito-identity")
- [Amazon Cognito IdentityPool](#services-cognito-idp "#services-cognito-idp")
- [Amazon Comprehend](#services-comprehend "#services-comprehend")
- [AWS Config](#services-config "#services-config")
- [Amazon Connect](#services-connect "#services-connect")
- [Amazon Connect Customer Profiles](#services-profile "#services-profile")
- [Amazon Connect Wisdom](#services-wisdom "#services-wisdom")
- [AWS Cost Explorer](#services-ce "#services-ce")
- [AWS Data Exchange](#services-dataexchange "#services-dataexchange")
- [AWS Data Pipeline](#services-datapipeline "#services-datapipeline")
- [AWS DataSync](#services-datasync "#services-datasync")
- [AWS Database Migration Service](#services-dms "#services-dms")
- [Amazon Detective](#services-detective "#services-detective")
- [AWS Device Farm](#services-devicefarm "#services-devicefarm")
- [Amazon DynamoDB](#services-dynamodb "#services-dynamodb")
- [DynamoDB Accelerator](#services-dax "#services-dax")
- [Amazon EC2 Auto Scaling](#services-autoscaling "#services-autoscaling")
- [EC2 Image Builder](#services-imagebuilder "#services-imagebuilder")
- [Amazon EMR](#services-elasticmapreduce "#services-elasticmapreduce")
- [Amazon EMR Serverless](#services-emr-serverless "#services-emr-serverless")
- [Amazon EMR on EKS](#services-emr-containers "#services-emr-containers")
- [Amazon ElastiCache](#services-elasticache "#services-elasticache")
- [AWS Elastic Beanstalk](#services-elasticbeanstalk "#services-elasticbeanstalk")
- [Amazon Elastic Compute Cloud (Amazon EC2)](#services-ec2 "#services-ec2")
- [Amazon Elastic Container Registry](#services-ecr "#services-ecr")
- [Amazon Elastic Container Registry Public](#services-ecr-public "#services-ecr-public")
- [Amazon Elastic Container Service](#services-ecs "#services-ecs")
- [Amazon Elastic File System](#services-elasticfilesystem "#services-elasticfilesystem")
- [Amazon Elastic Kubernetes Service (Amazon EKS)](#services-eks "#services-eks")
- [Elastic Load Balancing](#services-elasticloadbalancing "#services-elasticloadbalancing")
- [AWS Elemental MediaPackage](#services-mediapackage "#services-mediapackage")
- [AWS Elemental MediaPackage VoD](#services-mediapackage-vod "#services-mediapackage-vod")
- [AWS Elemental MediaStore](#services-mediastore "#services-mediastore")
- [AWS Elemental MediaTailor](#services-mediatailor "#services-mediatailor")
- [Amazon CloudWatch Events](#services-events "#services-events")
- [Amazon EventBridge Pipes](#services-pipes "#services-pipes")
- [Amazon EventBridge Scheduler](#services-scheduler "#services-scheduler")
- [Amazon EventBridge Schemas](#services-schemas "#services-schemas")
- [Amazon FSx](#services-fsx "#services-fsx")
- [AWS Fault Injection Service](#services-fis "#services-fis")
- [Amazon FinSpace](#services-finspace "#services-finspace")
- [Firehose](#services-firehose "#services-firehose")
- [Amazon Forecast](#services-forecast "#services-forecast")
- [Amazon Fraud Detector](#services-frauddetector "#services-frauddetector")
- [Amazon GameLift Servers](#services-gamelift "#services-gamelift")
- [AWS Global Accelerator](#services-globalaccelerator "#services-globalaccelerator")
- [AWS Glue](#services-glue "#services-glue")
- [AWS Glue DataBrew](#services-databrew "#services-databrew")
- [AWS Ground Station](#services-groundstation "#services-groundstation")
- [Amazon GuardDuty](#services-guardduty "#services-guardduty")
- [AWS HealthLake](#services-healthlake "#services-healthlake")
- [AWS HealthOmics](#services-omics "#services-omics")
- [IAM Access Analyzer](#services-access-analyzer "#services-access-analyzer")
- [Amazon IVS](#services-ivschat "#services-ivschat")
- [AWS Identity and Access Management](#services-iam "#services-iam")
- [Amazon Inspector](#services-inspector "#services-inspector")
- [Amazon Inspector](#services-inspector "#services-inspector")
- [Amazon Interactive Video Service](#services-ivs "#services-ivs")
- [AWS IoT](#services-iot "#services-iot")
- [AWS IoT Core Device Advisor](#services-iotdeviceadvisor "#services-iotdeviceadvisor")
- [AWS IoT Events](#services-iotevents "#services-iotevents")
- [AWS IoT FleetWise](#services-iotfleetwise "#services-iotfleetwise")
- [AWS IoT Greengrass](#services-greengrass "#services-greengrass")
- [AWS IoT SiteWise](#services-iotsitewise "#services-iotsitewise")
- [AWS IoT TwinMaker](#services-iottwinmaker "#services-iottwinmaker")
- [AWS IoT Wireless](#services-iotwireless "#services-iotwireless")
- [Amazon Kendra](#services-kendra "#services-kendra")
- [AWS Key Management Service](#services-kms "#services-kms")
- [Amazon Kinesis](#services-kinesis "#services-kinesis")
- [Amazon Managed Service for Apache Flink](#services-kinesisanalytics "#services-kinesisanalytics")
- [Amazon Kinesis Video Streams](#services-kinesisvideo "#services-kinesisvideo")
- [AWS Lambda](#services-lambda "#services-lambda")
- [Amazon Lex](#services-lex "#services-lex")
- [AWS License Manager](#services-license-manager "#services-license-manager")
- [Amazon MQ](#services-mq "#services-mq")
- [AWS Mainframe Modernization](#services-m2 "#services-m2")
- [Amazon Managed Blockchain](#services-managedblockchain "#services-managedblockchain")
- [Amazon Managed Grafana](#services-grafana "#services-grafana")
- [Amazon Managed Service for Prometheus](#services-aps "#services-aps")
- [Amazon Managed Streaming for Apache Kafka](#services-kafka "#services-kafka")
- [Amazon Managed Workflows for Apache Airflow](#services-airflow "#services-airflow")
- [Amazon MemoryDB](#services-memorydb "#services-memorydb")
- [AWS Migration Hub Refactor Spaces](#services-refactor-spaces "#services-refactor-spaces")
- [AWS Mobile Targeting](#services-mobiletargeting "#services-mobiletargeting")
- [AWS Network Firewall](#services-network-firewall "#services-network-firewall")
- [AWS Network Manager](#services-networkmanager "#services-networkmanager")
- [Amazon OpenSearch Service](#services-es "#services-es")
- [AWS Outposts](#services-outposts "#services-outposts")
- [AWS Panorama](#services-panorama "#services-panorama")
- [Amazon Personalize](#services-personalize "#services-personalize")
- [AWS Private Certificate Authority](#services-acm-pca "#services-acm-pca")
- [AWS Proton](#services-proton "#services-proton")
- [Amazon Quick Suite](#services-quicksight "#services-quicksight")
- [Amazon Redshift](#services-redshift "#services-redshift")
- [Amazon Rekognition](#services-rekognition "#services-rekognition")
- [Amazon Relational Database Service (Amazon RDS)](#services-rds "#services-rds")
- [AWS Resilience Hub](#services-resiliencehub "#services-resiliencehub")
- [AWS Resource Access Manager](#services-ram "#services-ram")
- [AWS Resource Groups](#services-resource-groups "#services-resource-groups")
- [AWS Resource Explorer](#services-resource-explorer-2 "#services-resource-explorer-2")
- [Amazon Route 53](#services-route53 "#services-route53")
- [Amazon Route 53 Recovery Readiness](#services-route53-recovery-readiness "#services-route53-recovery-readiness")
- [Amazon Route 53 Resolver](#services-route53resolver "#services-route53resolver")
- [Amazon Glacier](#services-glacier "#services-glacier")
- [Amazon SageMaker AI](#services-sagemaker "#services-sagemaker")
- [AWS Secrets Manager](#services-secretsmanager "#services-secretsmanager")
- [AWS Service Catalog](#services-servicecatalog "#services-servicecatalog")
- [AWS Signer](#services-signer "#services-signer")
- [Amazon Simple Email Service](#services-ses "#services-ses")
- [Amazon Simple Notification Service](#services-sns "#services-sns")
- [Amazon Simple Queue Service](#services-sqs "#services-sqs")
- [Amazon Simple Storage Service (Amazon S3)](#services-s3 "#services-s3")
- [AWS Step Functions States Language](#services-states "#services-states")
- [Storage Gateway](#services-storagegateway "#services-storagegateway")
- [AWS Systems Manager](#services-ssm "#services-ssm")
- [AWS Transfer Family](#services-transfer "#services-transfer")
- [Amazon WorkSpaces](#services-workspaces "#services-workspaces")

### Amazon API Gateway

- `apigateway:apis`
- `apigateway:apis/integrations`
- `apigateway:apis/routes`
- `apigateway:apis/stages`
- `apigateway:restapis`
- `apigateway:restapis/deployments`
- `apigateway:restapis/resources`
- `apigateway:restapis/resources/methods`
- `apigateway:restapis/stages`
- `apigateway:vpclinks`

### Direct Connect

- `directconnect:dx-gateway`

### AWS Partner Network

- `partnercentral:catalog/engagement`
- `partnercentral:catalog/engagement-invitation`
- `partnercentral:catalog/opportunity`
- `partnercentral:catalog/resource-snapshot-job`
- `partnercentral:resourcesnapshot`

### AWS Shield

- `shield:protection`
- `shield:protection-group`

### AWS Systems Manager Incident Manager

- `ssm-incidents:response-plan`

### AWS WAFV2

- `wafv2:ipset`
- `wafv2:regexpatternset`
- `wafv2:rulegroup`
- `wafv2:webacl`

### Amazon Macie

- `macie2:allow-list`
- `macie2:custom-data-identifier`
- `macie2:findings-filter`

### OpenSearch Service Serverless Service

- `aoss:collection`

### Amazon S3 Express

- `s3express:bucket`

### Amazon VPC Lattice

- `vpc-lattice:service`
- `vpc-lattice:service/listener`
- `vpc-lattice:servicenetwork`
- `vpc-lattice:servicenetworkserviceassociation`
- `vpc-lattice:targetgroup`

### Amazon Verified Permissions

- `verifiedpermissions:policy-store`

### Amazon WorkSpaces Web

- `workspaces-web:portal`

### AWS Amplify

- `amplify:apps`
- `amplify:apps/branches`
- `amplify:apps/domains`

### AWS App Runner

- `apprunner:autoscalingconfiguration`
- `apprunner:connection`
- `apprunner:service`
- `apprunner:vpcconnector`

### AWS AppConfig

- `appconfig:application`
- `appconfig:application/environment`
- `appconfig:deploymentstrategy`
- `appconfig:extensionassociation`

### Amazon AppFlow

- `appflow:flow`

### AppIntegrations

- `app-integrations:application`
- `app-integrations:event-integration`

### AWS App Mesh

- `appmesh:mesh`
- `appmesh:mesh/virtualGateway`
- `appmesh:mesh/virtualGateway/gatewayRoute`
- `appmesh:mesh/virtualNode`
- `appmesh:mesh/virtualRouter`
- `appmesh:mesh/virtualRouter/route`
- `appmesh:mesh/virtualService`

### Amazon AppStream

- `appstream:app-block`
- `appstream:application`
- `appstream:fleet`
- `appstream:image-builder`
- `appstream:stack`

### AWS AppSync

- `appsync:apis`

### AWS Application Discovery Service

- `ds:directory`

### Amazon Application Recovery Controller (ARC)

- `route53-recovery-control:cluster`
- `route53-recovery-control:controlpanel/routingcontrol`
- `route53-recovery-control:controlpanel/safetyrule`

### Amazon Athena

- `athena:datacatalog`
- `athena:workgroup`

### AWS Audit Manager

- `auditmanager:assessment`

### AWS Backup

- `backup:backup-plan`
- `backup:backup-vault`
- `backup:report-plan`

### AWS Backup gateway

- `backup-gateway:hypervisor`

### AWS Batch

- `batch:compute-environment`
- `batch:job-definition`
- `batch:job-queue`
- `batch:scheduling-policy`

### Amazon Bedrock

- `bedrock:agent`
- `bedrock:agent-alias`
- `bedrock:application-inference-profile`
- `bedrock:data-automation-project`
- `bedrock:flow`
- `bedrock:guardrail`
- `bedrock:knowledge-base`
- `bedrock:prompt`
- `bedrock:prompt-router`

### AWS Certificate Manager

- `acm:certificate`

### Amazon Chime

- `chime:app-instance`
- `chime:app-instance/bot`
- `chime:app-instance/user`
- `chime:media-insights-pipeline-configuration`
- `chime:media-pipeline-kinesis-video-stream-pool`
- `chime:sma`
- `chime:vc`

### AWS Cloud Map

- `servicediscovery:service`

### AWS Cloud9

- `cloud9:environment`

### CloudFormation

- `cloudformation:stack`
- `cloudformation:stackset`

### Amazon CloudFront

- `cloudfront:cache-policy`
- `cloudfront:continuous-deployment-policy`
- `cloudfront:distribution`
- `cloudfront:field-level-encryption-config`
- `cloudfront:field-level-encryption-profile`
- `cloudfront:function`
- `cloudfront:origin-access-control`
- `cloudfront:origin-access-identity`
- `cloudfront:origin-request-policy`
- `cloudfront:realtime-log-config`
- `cloudfront:response-headers-policy`

### AWS CloudTrail

- `cloudtrail:channel`
- `cloudtrail:dashboard`
- `cloudtrail:eventdatastore`
- `cloudtrail:trail`

### Amazon CloudWatch

- `cloudwatch:alarm`
- `cloudwatch:dashboard`
- `cloudwatch:insight-rule`
- `cloudwatch:metric-stream`

### Amazon CloudWatch Logs

- `logs:destination`
- `logs:log-group`

### Amazon CloudWatch Observability Access Manager

- `oam:sink`

### Amazon CloudWatch RUM

- `rum:appmonitor`

### Amazon CloudWatch Synthetics

- `synthetics:canary`
- `synthetics:group`

### AWS CodeArtifact

- `codeartifact:domain`
- `codeartifact:repository`

### AWS CodeBuild

- `codebuild:project`

### AWS CodeCommit

- `codecommit:repository`

### AWS CodeConnections

- `codeconnections:connection`

### AWS CodeDeploy

- `codedeploy:application`
- `codedeploy:deploymentconfig`

### Amazon CodeGuru Profiler

- `codeguru-profiler:profilingGroup`

### Amazon CodeGuru Reviewer

- `codeguru-reviewer:association`

### AWS CodePipeline

- `codepipeline:pipeline`
- `codepipeline:webhook`

### AWS CodeStar Connections

- `codestar-connections:connection`

### Amazon Cognito Identity

- `cognito-identity:identitypool`

### Amazon Cognito IdentityPool

- `cognito-idp:userpool`

### Amazon Comprehend

- `comprehend:document-classifier`
- `comprehend:entity-recognizer`
- `comprehend:flywheel`

### AWS Config

- `config:config-rule`

### Amazon Connect

- `connect:instance`
- `connect:instance/agent`
- `connect:instance/operating-hours`
- `connect:instance/rule`
- `connect:instance/task-template`
- `connect:instance/transfer-destination`
- `connect:phone-number`

### Amazon Connect Customer Profiles

- `profile:domains`
- `profile:domains/integrations`
- `profile:domains/object-types`

### Amazon Connect Wisdom

- `wisdom:assistant`
- `wisdom:association`
- `wisdom:content`
- `wisdom:knowledge-base`

### AWS Cost Explorer

- `ce:anomalymonitor`
- `ce:anomalysubscription`

### AWS Data Exchange

- `dataexchange:data-sets`

### AWS Data Pipeline

- `datapipeline:pipeline`

### AWS DataSync

- `datasync:location`
- `datasync:task`

### AWS Database Migration Service

- `dms:cert`
- `dms:endpoint`
- `dms:es`
- `dms:rep`
- `dms:subgrp`
- `dms:task`

### Amazon Detective

- `detective:graph`

### AWS Device Farm

- `devicefarm:instanceprofile`
- `devicefarm:project`
- `devicefarm:testgrid-project`

### Amazon DynamoDB

- `dynamodb:table`

### DynamoDB Accelerator

- `dax:cache`

### Amazon EC2 Auto Scaling

- `autoscaling:autoScalingGroup`

### EC2 Image Builder

- `imagebuilder:component`
- `imagebuilder:container-recipe`
- `imagebuilder:distribution-configuration`
- `imagebuilder:image`
- `imagebuilder:image-pipeline`
- `imagebuilder:image-recipe`
- `imagebuilder:infrastructure-configuration`

### Amazon EMR

- `elasticmapreduce:cluster`

### Amazon EMR Serverless

- `emr-serverless:applications`

### Amazon EMR on EKS

- `emr-containers:jobtemplates`
- `emr-containers:securityconfigurations`
- `emr-containers:virtualclusters`
- `emr-containers:virtualclusters/endpoints`

### Amazon ElastiCache

- `elasticache:cluster`
- `elasticache:globalreplicationgroup`
- `elasticache:parametergroup`
- `elasticache:replicationgroup`
- `elasticache:reserved-instance`
- `elasticache:snapshot`
- `elasticache:subnetgroup`
- `elasticache:user`
- `elasticache:usergroup`

### AWS Elastic Beanstalk

- `elasticbeanstalk:application`
- `elasticbeanstalk:applicationversion`
- `elasticbeanstalk:configurationtemplate`
- `elasticbeanstalk:environment`

### Amazon Elastic Compute Cloud (Amazon EC2)

- `ec2:capacity-reservation`
- `ec2:capacity-reservation-fleet`
- `ec2:carrier-gateway`
- `ec2:client-vpn-endpoint`
- `ec2:customer-gateway`
- `ec2:dedicated-host`
- `ec2:dhcp-options`
- `ec2:egress-only-internet-gateway`
- `ec2:elastic-ip`
- `ec2:fleet`
- `ec2:fpga-image`
- `ec2:host-reservation`
- `ec2:image`
- `ec2:instance`
- `ec2:instance-event-window`
- `ec2:internet-gateway`
- `ec2:ipam`
- `ec2:ipam-pool`
- `ec2:ipam-resource-discovery`
- `ec2:ipam-resource-discovery-association`
- `ec2:ipam-scope`
- `ec2:ipv4pool-ec2`
- `ec2:key-pair`
- `ec2:launch-template`
- `ec2:natgateway`
- `ec2:network-acl`
- `ec2:network-insights-access-scope`
- `ec2:network-insights-access-scope-analysis`
- `ec2:network-insights-analysis`
- `ec2:network-insights-path`
- `ec2:network-interface`
- `ec2:placement-group`
- `ec2:prefix-list`
- `ec2:reserved-instances`
- `ec2:route-table`
- `ec2:security-group`
- `ec2:security-group-rule`
- `ec2:snapshot`
- `ec2:spot-fleet-request`
- `ec2:spot-instances-request`
- `ec2:subnet`
- `ec2:subnet-cidr-reservation`
- `ec2:traffic-mirror-filter`
- `ec2:traffic-mirror-filter-rule`
- `ec2:traffic-mirror-session`
- `ec2:traffic-mirror-target`
- `ec2:transit-gateway`
- `ec2:transit-gateway-attachment`
- `ec2:transit-gateway-connect-peer`
- `ec2:transit-gateway-multicast-domain`
- `ec2:transit-gateway-policy-table`
- `ec2:transit-gateway-route-table`
- `ec2:transit-gateway-route-table-announcement`
- `ec2:verified-access-endpoint`
- `ec2:verified-access-group`
- `ec2:verified-access-instance`
- `ec2:verified-access-trust-provider`
- `ec2:volume`
- `ec2:vpc`
- `ec2:vpc-endpoint`
- `ec2:vpc-flow-log`
- `ec2:vpc-peering-connection`
- `ec2:vpn-connection`
- `ec2:vpn-gateway`

### Amazon Elastic Container Registry

- `ecr:repository`

### Amazon Elastic Container Registry Public

- `ecr-public:repository`

### Amazon Elastic Container Service

- `ecs:capacity-provider`
- `ecs:cluster`
- `ecs:container-instance`
- `ecs:service`
- `ecs:task-definition`
- `ecs:task-set`

### Amazon Elastic File System

- `elasticfilesystem:access-point`
- `elasticfilesystem:file-system`

### Amazon Elastic Kubernetes Service (Amazon EKS)

- `eks:cluster`
- `eks:eks-anywhere-subscription`
- `eks:podidentityassociation`

### Elastic Load Balancing

- `elasticloadbalancing:listener-rule/app`
- `elasticloadbalancing:listener/app`
- `elasticloadbalancing:listener/gwy`
- `elasticloadbalancing:listener/net`
- `elasticloadbalancing:loadbalancer`
- `elasticloadbalancing:loadbalancer/app`
- `elasticloadbalancing:loadbalancer/gwy`
- `elasticloadbalancing:loadbalancer/net`
- `elasticloadbalancing:targetgroup`

### AWS Elemental MediaPackage

- `mediapackage:channels`
- `mediapackage:origin_endpoints`

### AWS Elemental MediaPackage VoD

- `mediapackage-vod:assets`
- `mediapackage-vod:packaging-configurations`
- `mediapackage-vod:packaging-groups`

### AWS Elemental MediaStore

- `mediastore:container`

### AWS Elemental MediaTailor

- `mediatailor:channel`
- `mediatailor:liveSource`
- `mediatailor:playbackConfiguration`
- `mediatailor:vodSource`

### Amazon CloudWatch Events

- `events:api-destination`
- `events:archive`
- `events:connection`
- `events:endpoint`
- `events:event-bus`
- `events:rule`

### Amazon EventBridge Pipes

- `pipes:pipe`

### Amazon EventBridge Scheduler

- `scheduler:schedule-group`

### Amazon EventBridge Schemas

- `schemas:discoverer`

### Amazon FSx

- `fsx:backup`
- `fsx:file-system`

### AWS Fault Injection Service

- `fis:experiment-template`

### Amazon FinSpace

- `finspace:environment`

### Firehose

- `firehose:deliverystream`

### Amazon Forecast

- `forecast:dataset`
- `forecast:dataset-group`
- `forecast:dataset-import-job`
- `forecast:forecast`
- `forecast:forecast-export-job`
- `forecast:predictor`
- `forecast:predictor-backtest-export-job`

### Amazon Fraud Detector

- `frauddetector:detector`
- `frauddetector:entity-type`
- `frauddetector:event-type`
- `frauddetector:external-model`
- `frauddetector:label`
- `frauddetector:model`
- `frauddetector:outcome`
- `frauddetector:variable`

### Amazon GameLift Servers

- `gamelift:alias`
- `gamelift:build`
- `gamelift:gamesessionqueue`
- `gamelift:location`
- `gamelift:matchmakingconfiguration`
- `gamelift:matchmakingruleset`
- `gamelift:script`

### AWS Global Accelerator

- `globalaccelerator:accelerator`
- `globalaccelerator:accelerator/listener`
- `globalaccelerator:accelerator/listener/endpoint-group`

### AWS Glue

- `glue:crawler`
- `glue:dataQualityRuleset`
- `glue:database`
- `glue:job`
- `glue:mlTransform`
- `glue:registry`
- `glue:table`
- `glue:trigger`

### AWS Glue DataBrew

- `databrew:dataset`
- `databrew:job`
- `databrew:project`
- `databrew:recipe`
- `databrew:ruleset`
- `databrew:schedule`

### AWS Ground Station

- `groundstation:config`
- `groundstation:dataflow-endpoint-group`
- `groundstation:mission-profile`

### Amazon GuardDuty

- `guardduty:detector`
- `guardduty:detector/filter`
- `guardduty:detector/ipset`
- `guardduty:detector/publishingDestination`
- `guardduty:detector/threatintelset`
- `guardduty:malware-protection-plan`

### AWS HealthLake

- `healthlake:datastore/fhir`

### AWS HealthOmics

- `omics:referenceStore`
- `omics:runGroup`
- `omics:workflow`

### IAM Access Analyzer

- `access-analyzer:analyzer`

### Amazon IVS

- `ivschat:logging-configuration`
- `ivschat:room`

### AWS Identity and Access Management

- `iam:group`
- `iam:instance-profile`
- `iam:mfa`
- `iam:oidc-provider`
- `iam:policy`
- `iam:role`
- `iam:saml-provider`
- `iam:server-certificate`
- `iam:user`

### Amazon Inspector

- `inspector:target/template`
- `inspector2:filter`

### Amazon Inspector

- `inspector:target/template`
- `inspector2:filter`

### Amazon Interactive Video Service

- `ivs:channel`
- `ivs:encoder-configuration`
- `ivs:ingest-configuration`
- `ivs:playback-key`
- `ivs:playback-restriction-policy`
- `ivs:recording-configuration`
- `ivs:storage-configuration`
- `ivs:stream-key`

### AWS IoT

- `iot:authorizer`
- `iot:billinggroup`
- `iot:cacert`
- `iot:cert`
- `iot:fleetmetric`
- `iot:jobtemplate`
- `iot:mitigationaction`
- `iot:policy`
- `iot:provisioningtemplate`
- `iot:rolealias`
- `iot:rule`
- `iot:ruledestination`
- `iot:scheduledaudit`
- `iot:securityprofile`
- `iot:thing`
- `iot:thinggroup`
- `iot:thingtype`

### AWS IoT Core Device Advisor

- `iotdeviceadvisor:suitedefinition`

### AWS IoT Events

- `iotevents:alarmModel`
- `iotevents:detectorModel`
- `iotevents:input`

### AWS IoT FleetWise

- `iotfleetwise:decoder-manifest`
- `iotfleetwise:model-manifest`
- `iotfleetwise:signal-catalog`
- `iotfleetwise:vehicle`

### AWS IoT Greengrass

- `greengrass:components:versions`
- `greengrass:connectorsDefinition`
- `greengrass:coresDefinition`
- `greengrass:devicesDefinition`
- `greengrass:functionsDefinition`
- `greengrass:groups`
- `greengrass:loggersDefinition`
- `greengrass:resourcesDefinition`
- `greengrass:subscriptionsDefinition`

### AWS IoT SiteWise

- `iotsitewise:access-policy`
- `iotsitewise:asset`
- `iotsitewise:asset-model`
- `iotsitewise:dashboard`
- `iotsitewise:gateway`
- `iotsitewise:portal`
- `iotsitewise:project`

### AWS IoT TwinMaker

- `iottwinmaker:workspace`
- `iottwinmaker:workspace/component-type`
- `iottwinmaker:workspace/entity`
- `iottwinmaker:workspace/sync-job`

### AWS IoT Wireless

- `iotwireless:Destination`
- `iotwireless:DeviceProfile`
- `iotwireless:FuotaTask`
- `iotwireless:MulticastGroup`
- `iotwireless:ServiceProfile`
- `iotwireless:SidewalkAccount`
- `iotwireless:WirelessDevice`
- `iotwireless:WirelessGateway`
- `iotwireless:WirelessGatewayTaskDefinition`

### Amazon Kendra

- `kendra:index`
- `kendra:index/access-control-configuration`
- `kendra:index/data-source`
- `kendra:index/experience`
- `kendra:index/faq`
- `kendra:index/featured-results-set`
- `kendra:index/query-suggestions-block-list`
- `kendra:index/thesaurus`

### AWS Key Management Service

- `kms:key`

### Amazon Kinesis

- `kinesis:stream`

### Amazon Managed Service for Apache Flink

- `kinesisanalytics:application`

### Amazon Kinesis Video Streams

- `kinesisvideo:channel`
- `kinesisvideo:stream`

### AWS Lambda

- `lambda:code-signing-config`
- `lambda:event-source-mapping`
- `lambda:function`

### Amazon Lex

- `lex:bot`
- `lex:bot-alias`

### AWS License Manager

- `license-manager:grant`

### Amazon MQ

- `mq:broker`
- `mq:configuration`

### AWS Mainframe Modernization

- `m2:env`

### Amazon Managed Blockchain

- `managedblockchain:accessors`

### Amazon Managed Grafana

- `grafana:workspaces`

### Amazon Managed Service for Prometheus

- `aps:rulegroupsnamespace`
- `aps:workspace`

### Amazon Managed Streaming for Apache Kafka

- `kafka:cluster`
- `kafka:configuration`

### Amazon Managed Workflows for Apache Airflow

- `airflow:environment`

### Amazon MemoryDB

- `memorydb:acl`
- `memorydb:cluster`
- `memorydb:parametergroup`
- `memorydb:snapshot`
- `memorydb:subnetgroup`
- `memorydb:user`

### AWS Migration Hub Refactor Spaces

- `refactor-spaces:environment`
- `refactor-spaces:environment/application`
- `refactor-spaces:environment/application/route`
- `refactor-spaces:environment/application/service`

### AWS Mobile Targeting

- `mobiletargeting:apps/campaigns`
- `mobiletargeting:apps/segments`
- `mobiletargeting:templates/EMAIL`
- `mobiletargeting:templates/PUSH`
- `mobiletargeting:templates/SMS`

### AWS Network Firewall

- `network-firewall:firewall`
- `network-firewall:firewall-policy`
- `network-firewall:stateful-rulegroup`
- `network-firewall:stateless-rulegroup`

### AWS Network Manager

- `networkmanager:attachment`
- `networkmanager:core-network`
- `networkmanager:device`
- `networkmanager:global-network`
- `networkmanager:link`

### Amazon OpenSearch Service

- `es:domain`

### AWS Outposts

- `outposts:site`

### AWS Panorama

- `panorama:package`

### Amazon Personalize

- `personalize:dataset`
- `personalize:dataset-group`
- `personalize:schema`
- `personalize:solution`

### AWS Private Certificate Authority

- `acm-pca:certificate-authority`

### AWS Proton

- `proton:environment-account-connection`
- `proton:environment-template`
- `proton:service-template`

### Amazon Quick Suite

- `quicksight:dataset`
- `quicksight:datasource`
- `quicksight:template`
- `quicksight:theme`

### Amazon Redshift

- `redshift:cluster`
- `redshift:eventsubscription`
- `redshift:hsmclientcertificate`
- `redshift:parametergroup`
- `redshift:snapshot`
- `redshift:snapshotcopygrant`
- `redshift:snapshotschedule`
- `redshift:subnetgroup`
- `redshift:usagelimit`

### Amazon Rekognition

- `rekognition:project`

### Amazon Relational Database Service (Amazon RDS)

- `rds:auto-backup`
- `rds:cev`
- `rds:cluster`
- `rds:cluster-endpoint`
- `rds:cluster-pg`
- `rds:cluster-snapshot`
- `rds:db`
- `rds:db-proxy`
- `rds:db-proxy-endpoint`
- `rds:deployment`
- `rds:es`
- `rds:global-cluster`
- `rds:og`
- `rds:pg`
- `rds:ri`
- `rds:secgrp`
- `rds:snapshot`
- `rds:subgrp`

### AWS Resilience Hub

- `resiliencehub:app`
- `resiliencehub:resiliency-policy`

### AWS Resource Access Manager

- `ram:resource-share`

### AWS Resource Groups

- `resource-groups:group`

### AWS Resource Explorer

- `resource-explorer-2:index`
- `resource-explorer-2:view`

### Amazon Route 53

- `route53:domain`
- `route53:healthcheck`
- `route53:hostedzone`

### Amazon Route 53 Recovery Readiness

- `route53-recovery-readiness:cell`
- `route53-recovery-readiness:readiness-check`
- `route53-recovery-readiness:recovery-group`
- `route53-recovery-readiness:resource-set`

### Amazon Route 53 Resolver

- `route53resolver:firewall-domain-list`
- `route53resolver:firewall-rule-group`
- `route53resolver:firewall-rule-group-association`
- `route53resolver:resolver-endpoint`
- `route53resolver:resolver-query-log-config`
- `route53resolver:resolver-rule`

### Amazon Glacier

- `glacier:vaults`

### Amazon SageMaker AI

- `sagemaker:action`
- `sagemaker:algorithm`
- `sagemaker:app`
- `sagemaker:app-image-config`
- `sagemaker:artifact`
- `sagemaker:cluster`
- `sagemaker:code-repository`
- `sagemaker:context`
- `sagemaker:domain`
- `sagemaker:endpoint`
- `sagemaker:endpoint-config`
- `sagemaker:experiment`
- `sagemaker:experiment-trial`
- `sagemaker:experiment-trial-component`
- `sagemaker:feature-group`
- `sagemaker:flow-definition`
- `sagemaker:hub`
- `sagemaker:human-task-ui`
- `sagemaker:image`
- `sagemaker:image-version`
- `sagemaker:inference-component`
- `sagemaker:inference-experiment`
- `sagemaker:mlflow-tracking-server`
- `sagemaker:model`
- `sagemaker:model-card`
- `sagemaker:model-package`
- `sagemaker:model-package-group`
- `sagemaker:monitoring-schedule`
- `sagemaker:notebook-instance`
- `sagemaker:notebook-instance-lifecycle-config`
- `sagemaker:pipeline`
- `sagemaker:project`
- `sagemaker:space`
- `sagemaker:studio-lifecycle-config`
- `sagemaker:user-profile`
- `sagemaker:workforce`
- `sagemaker:workteam`

### AWS Secrets Manager

- `secretsmanager:secret`

### AWS Service Catalog

- `servicecatalog:applications`
- `servicecatalog:attribute-groups`

### AWS Signer

- `signer:signing-profiles`

### Amazon Simple Email Service

- `ses:configuration-set`
- `ses:contact-list`
- `ses:dedicated-ip-pool`
- `ses:identity`

### Amazon Simple Notification Service

- `sns:topic`

### Amazon Simple Queue Service

- `sqs:queue`

### Amazon Simple Storage Service (Amazon S3)

- `s3:accesspoint`
- `s3:bucket`
- `s3:multiregionaccesspoint`
- `s3:storage-lens`
- `s3:storage-lens-group`

### AWS Step Functions States Language

- `states:activity`
- `states:stateMachine`

### Storage Gateway

- `storagegateway:gateway`

### AWS Systems Manager

- `ssm:association`
- `ssm:document`
- `ssm:maintenancewindow`
- `ssm:managed-instance`
- `ssm:parameter`
- `ssm:resource-data-sync`
- `ssm:session`
- `ssm:windowtarget`
- `ssm:windowtask`

### AWS Transfer Family

- `transfer:agreement`
- `transfer:certificate`
- `transfer:connector`
- `transfer:profile`
- `transfer:server`
- `transfer:user`
- `transfer:workflow`

### Amazon WorkSpaces

- `workspaces:connectionalias`
- `workspaces:workspace`

## Programmatically accessing the list of supported

resource types

To access the list of supported resource types from code, you can invoke the [ListSupportedResourceTypes](../apireference/API_ListSupportedResourceTypes.md "../apireference/API_ListSupportedResourceTypes.md") operation from any AWS SDK.

For example, you can run the [list-supported-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-supported-resource-types.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-supported-resource-types.html") AWS Command Line Interface (AWS CLI) command, as shown in the
following example.

```
`$` `aws resource-explorer-2 list-supported-resource-types``{
 "ResourceTypes": [
 {
 "ResourceType": "acm-pca:certificate-authority",
 "Service": "acm-pca"
 },
 {
 "ResourceType": "airflow:environment",
 "Service": "airflow"
 },
 {
 "ResourceType": "amplify:branches",
 "Service": "amplify"
 },
***... truncated for brevity ...***`
```

## Resource types that appear as other

types

Some resource types are identified by [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") strings that share a common
format with another resource type. When this happens, Resource Explorer can report such resources
as that other resource type. This affects the resource types in the following
table.

| Actual resource type                                                                                  | Reported as resource type           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `ec2:securitygroupegress`<br>`ec2:securitygroupingress`                                               | `ec2:security-group-rule`           |
| `elasticloadbalancingv2:loadbalancer`                                                                 | `elasticloadbalancing:loadbalancer` |
| `docdb:dbcluster`<br>`neptune:dbcluster`<br>`rds:dbcluster`                                           | `rds:cluster`                       |
| `docdb:dbclusterparametergroup`<br>`neptune:dbclusterparametergroup`<br>`rds:dbclusterparametergroup` | `rds:cluster-pg`                    |
| `docdb:clustersnapshot`<br>`neptune:dbclustersnapshot`<br>`rds:clustersnapshot`                       | `rds:cluster-snapshot`              |
| `docdb:dbinstance`<br>`neptune:dbinstance`<br>`rds:dbinstance`                                        | `rds:db`                            |
| `docdb:eventsubscription`<br>`neptune:eventsubscription`<br>`rds:eventsubscription`                   | `rds:es`                            |
| `docdb:globalcluster`<br>`rds:globalcluster`                                                          | `rds:global-cluster`                |
| `neptune:dbparametergroup`<br>`rds:dbparametergroup`                                                  | `rds:pg`                            |
| `docdb:dbsubnetgroup`<br>`neptune:dbsubnetgroup`<br>`rds:dbsubnetgroup`                               | `rds:subgrp`                        |
