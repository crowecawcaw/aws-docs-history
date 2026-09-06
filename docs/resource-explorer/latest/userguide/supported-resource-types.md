

# Resource types you can search for with Resource Explorer
<a name="supported-resource-types"></a>

Resource Explorer supports resource types across numerous AWS services. Resource discovery happens automatically when you access Resource Explorer with appropriate permissions. If you have, at minimum, the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy, you can immediately search all tagged resources and supported untagged resources created after the [immediate resource discovery](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-immediate-resource-discovery-experience.html) release. For complete resource discovery with automatic updates, you'll also need the `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.html) managed policy). After the service-linked role is created in your account by any user, subsequent users need only the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy to get complete results. 

**Topics**
+ [Supported services and resource types](#types-list)
+ [Programmatically accessing the list of supported resource types](#programmatic-access)
+ [Resource types that appear as other types](#resource-type-exceptions)

Some resource types are identified by [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) strings that share a common format with another resource type. When this happens, Resource Explorer can report such resources as that other resource type. For list of resource types affected by this issue, see [Resource types that appear as other types](#resource-type-exceptions).

At this time, tags attached to AWS Identity and Access Management (IAM) resources, such as roles or users, can't be used for searching.

If you have encrypted access to some of your resources, Resource Explorer is unable to discover them. You will not see these resources in your search results.

The following tables list the resource types that are supported for searching in AWS Resource Explorer.

**Note**  
As of May 20, 2026, Resource Explorer no longer supports the following resource types:  
**Amazon Inspector**— `inspector:target/template`
**AWS Panorama**— `panorama:device`
**AWS Panorama**— `panorama:package`
As of May 15, 2026, Resource Explorer no longer supports the following resource types:  
**AWS IoT Events**— `iotevents:alarmModel`
**AWS IoT Events**— `iotevents:detectorModel`
**AWS IoT Events**— `iotevents:input`
As of February 10, 2026, Resource Explorer no longer supports the following resource types:  
**Amazon Chime**— `chime:media-pipeline`
As of February 10, 2026, Resource Explorer no longer supports the following resource types:  
**Amazon Location Service**— `geo:map`
**Amazon Location Service**— `geo:place-index`
**Amazon Location Service**— `geo:tracker`
As of December 5, 2025, Resource Explorer no longer supports the following resource types:  
**AWS IoT Analytics**— `iotanalytics:channel`
**AWS IoT Analytics**— `iotanalytics:dataset`
**AWS IoT Analytics**— `iotanalytics:datastore`
**AWS IoT Analytics**— `iotanalytics:pipeline`
As of November 21, 2025, Resource Explorer no longer supports the following resource types:  
**AWS IoT FleetWise**— `iotfleethub:application`
As of November 3, 2025, Resource Explorer no longer supports the following resource types:  
**Amazon Lookout for Metrics**— `lookoutmetrics:Alert`
**Amazon Lookout for Metrics**— `lookoutmetrics:AnomalyDetector`
**Amazon Lookout for Vision**— `lookoutvision:project`
As of October 13, 2025, Resource Explorer no longer supports the following resource types:  
**Amazon CloudWatch Evidently**— `evidently:project`
**Amazon CloudWatch Evidently**— `evidently:project/experiment`
**Amazon CloudWatch Evidently**— `evidently:project/feature`
**Amazon CloudWatch Evidently**— `evidently:project/launch`
As of October 1, 2025, Resource Explorer no longer supports the following resource types:  
**Amazon Quantum Ledger Database (Amazon QLDB)** — `qldb:ledger`
**Amazon Quantum Ledger Database (Amazon QLDB)** — `qldb:stream`
As of July 9, 2024, Resource Explorer no longer supports the following resource types:  
**Amazon Elastic Container Service** — `ecs:task`
**AWS Systems Manager** — `ssm:automation-execution`
**AWS Systems Manager** — `ssm:patchbaseline`

## Supported services and resource types
<a name="types-list"></a>

**Topics**
+ [Amazon API Gateway](#services-apigateway)
+ [Direct Connect](#services-directconnect)
+ [AWS Partner Network](#services-partnercentral)
+ [AWS Shield](#services-shield)
+ [AWS Systems Manager Incident Manager](#services-ssm-incidents)
+ [AWS WAFV2](#services-wafv2)
+ [Amazon Macie](#services-macie2)
+ [OpenSearch Service Serverless Service](#services-aoss)
+ [Amazon S3 Express](#services-s3express)
+ [Amazon VPC Lattice](#services-vpc-lattice)
+ [Amazon Verified Permissions](#services-verifiedpermissions)
+ [Amazon WorkSpaces Web](#services-workspaces-web)
+ [AWS Amplify](#services-amplify)
+ [AWS App Runner](#services-apprunner)
+ [AWS AppConfig](#services-appconfig)
+ [Amazon AppFlow](#services-appflow)
+ [AppIntegrations](#services-app-integrations)
+ [AWS App Mesh](#services-appmesh)
+ [Amazon AppStream](#services-appstream)
+ [AWS AppSync](#services-appsync)
+ [AWS Application Discovery Service](#services-ds)
+ [Amazon Application Recovery Controller (ARC)](#services-route53-recovery-control)
+ [Amazon Athena](#services-athena)
+ [AWS Audit Manager](#services-auditmanager)
+ [AWS Backup](#services-backup)
+ [AWS Backup gateway](#services-backup-gateway)
+ [AWS Batch](#services-batch)
+ [Amazon Bedrock](#services-bedrock)
+ [AWS Certificate Manager](#services-acm)
+ [Amazon Chime](#services-chime)
+ [AWS Cloud Map](#services-servicediscovery)
+ [AWS Cloud9](#services-cloud9)
+ [CloudFormation](#services-cloudformation)
+ [Amazon CloudFront](#services-cloudfront)
+ [AWS CloudTrail](#services-cloudtrail)
+ [Amazon CloudWatch](#services-cloudwatch)
+ [Amazon CloudWatch Logs](#services-logs)
+ [Amazon CloudWatch Observability Access Manager](#services-oam)
+ [Amazon CloudWatch RUM](#services-rum)
+ [Amazon CloudWatch Synthetics](#services-synthetics)
+ [AWS CodeArtifact](#services-codeartifact)
+ [AWS CodeBuild](#services-codebuild)
+ [AWS CodeCommit](#services-codecommit)
+ [AWS CodeConnections](#services-codeconnections)
+ [AWS CodeDeploy](#services-codedeploy)
+ [Amazon CodeGuru Profiler](#services-codeguru-profiler)
+ [Amazon CodeGuru Reviewer](#services-codeguru-reviewer)
+ [AWS CodePipeline](#services-codepipeline)
+ [AWS CodeStar Connections](#services-codestar-connections)
+ [Amazon Cognito Identity](#services-cognito-identity)
+ [Amazon Cognito IdentityPool](#services-cognito-idp)
+ [Amazon Comprehend](#services-comprehend)
+ [AWS Config](#services-config)
+ [Amazon Connect Customer](#services-connect)
+ [Amazon Connect Customer Customer Profiles](#services-profile)
+ [Connect Customer Wisdom](#services-wisdom)
+ [AWS Cost Explorer](#services-ce)
+ [AWS Data Exchange](#services-dataexchange)
+ [AWS Data Pipeline](#services-datapipeline)
+ [AWS DataSync](#services-datasync)
+ [AWS Database Migration Service](#services-dms)
+ [Amazon Detective](#services-detective)
+ [AWS Device Farm](#services-devicefarm)
+ [Amazon DynamoDB](#services-dynamodb)
+ [DynamoDB Accelerator](#services-dax)
+ [Amazon EC2 Auto Scaling](#services-autoscaling)
+ [EC2 Image Builder](#services-imagebuilder)
+ [Amazon EMR](#services-elasticmapreduce)
+ [Amazon EMR Serverless](#services-emr-serverless)
+ [Amazon EMR on EKS](#services-emr-containers)
+ [Amazon ElastiCache](#services-elasticache)
+ [AWS Elastic Beanstalk](#services-elasticbeanstalk)
+ [Amazon Elastic Compute Cloud (Amazon EC2)](#services-ec2)
+ [Amazon Elastic Container Registry](#services-ecr)
+ [Amazon Elastic Container Registry Public](#services-ecr-public)
+ [Amazon Elastic Container Service](#services-ecs)
+ [Amazon Elastic File System](#services-elasticfilesystem)
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](#services-eks)
+ [Elastic Load Balancing](#services-elasticloadbalancing)
+ [AWS Elemental MediaPackage](#services-mediapackage)
+ [AWS Elemental MediaPackage VoD](#services-mediapackage-vod)
+ [AWS Elemental MediaStore](#services-mediastore)
+ [AWS Elemental MediaTailor](#services-mediatailor)
+ [Amazon CloudWatch Events](#services-events)
+ [Amazon EventBridge Pipes](#services-pipes)
+ [Amazon EventBridge Scheduler](#services-scheduler)
+ [Amazon EventBridge Schemas](#services-schemas)
+ [Amazon FSx](#services-fsx)
+ [AWS Fault Injection Service](#services-fis)
+ [Amazon FinSpace](#services-finspace)
+ [Firehose](#services-firehose)
+ [Amazon Forecast](#services-forecast)
+ [Amazon Fraud Detector](#services-frauddetector)
+ [Amazon GameLift Servers](#services-gamelift)
+ [AWS Global Accelerator](#services-globalaccelerator)
+ [AWS Glue](#services-glue)
+ [AWS Glue DataBrew](#services-databrew)
+ [AWS Ground Station](#services-groundstation)
+ [Amazon GuardDuty](#services-guardduty)
+ [AWS HealthLake](#services-healthlake)
+ [AWS HealthOmics](#services-omics)
+ [IAM Access Analyzer](#services-access-analyzer)
+ [Amazon IVS](#services-ivschat)
+ [AWS Identity and Access Management](#services-iam)
+ [Amazon Inspector](#services-inspector)
+ [Amazon Interactive Video Service](#services-ivs)
+ [AWS IoT](#services-iot)
+ [AWS IoT Core Device Advisor](#services-iotdeviceadvisor)
+ [AWS IoT FleetWise](#services-iotfleetwise)
+ [AWS IoT Greengrass](#services-greengrass)
+ [AWS IoT SiteWise](#services-iotsitewise)
+ [AWS IoT TwinMaker](#services-iottwinmaker)
+ [AWS IoT Wireless](#services-iotwireless)
+ [Amazon Kendra](#services-kendra)
+ [AWS Key Management Service](#services-kms)
+ [Amazon Kinesis](#services-kinesis)
+ [Amazon Managed Service for Apache Flink](#services-kinesisanalytics)
+ [Amazon Kinesis Video Streams](#services-kinesisvideo)
+ [AWS Lambda](#services-lambda)
+ [Amazon Lex](#services-lex)
+ [AWS License Manager](#services-license-manager)
+ [Amazon MQ](#services-mq)
+ [AWS Mainframe Modernization](#services-m2)
+ [Amazon Managed Blockchain](#services-managedblockchain)
+ [Amazon Managed Grafana](#services-grafana)
+ [Amazon Managed Service for Prometheus](#services-aps)
+ [Amazon Managed Streaming for Apache Kafka](#services-kafka)
+ [Amazon Managed Workflows for Apache Airflow](#services-airflow)
+ [Amazon MemoryDB](#services-memorydb)
+ [AWS Migration Hub Refactor Spaces](#services-refactor-spaces)
+ [AWS Mobile Targeting](#services-mobiletargeting)
+ [AWS Network Firewall](#services-network-firewall)
+ [AWS Network Manager](#services-networkmanager)
+ [Amazon OpenSearch Service](#services-es)
+ [AWS Outposts](#services-outposts)
+ [Amazon Personalize](#services-personalize)
+ [AWS Private Certificate Authority](#services-acm-pca)
+ [AWS Proton](#services-proton)
+ [Amazon Quick](#services-quicksight)
+ [Amazon Redshift](#services-redshift)
+ [Amazon Rekognition](#services-rekognition)
+ [Amazon Relational Database Service (Amazon RDS)](#services-rds)
+ [AWS Resilience Hub](#services-resiliencehub)
+ [AWS Resource Access Manager](#services-ram)
+ [AWS Resource Groups](#services-resource-groups)
+ [AWS Resource Explorer](#services-resource-explorer-2)
+ [Amazon Route 53](#services-route53)
+ [Amazon Route 53 Recovery Readiness](#services-route53-recovery-readiness)
+ [Amazon Route 53 Resolver](#services-route53resolver)
+ [Amazon Glacier](#services-glacier)
+ [Amazon SageMaker AI](#services-sagemaker)
+ [AWS Secrets Manager](#services-secretsmanager)
+ [AWS Service Catalog](#services-servicecatalog)
+ [AWS Signer](#services-signer)
+ [Amazon Simple Email Service](#services-ses)
+ [Amazon Simple Notification Service](#services-sns)
+ [Amazon Simple Queue Service](#services-sqs)
+ [Amazon Simple Storage Service (Amazon S3)](#services-s3)
+ [AWS Step Functions States Language](#services-states)
+ [Storage Gateway](#services-storagegateway)
+ [AWS Systems Manager](#services-ssm)
+ [AWS Transfer Family](#services-transfer)
+ [Amazon WorkSpaces](#services-workspaces)
+ [Amazon Bedrock AgentCore](#services-bedrock-agentcore)
+ [AWS Budgets](#services-budgets)
+ [AWS Clean Rooms](#services-cleanrooms)
+ [Amazon Data Lifecycle Manager](#services-dlm)
+ [Amazon Kendra Intelligent Ranking](#services-kendra-ranking)
+ [AWS Elemental MediaConnect](#services-mediaconnect)
+ [AWS Well-Architected Tool](#services-wellarchitected)
+ [AWS X-Ray](#services-xray)

### Amazon API Gateway
<a name="services-apigateway"></a>
+ `apigateway:apis`
+ `apigateway:apis/integrations`
+ `apigateway:apis/routes`
+ `apigateway:apis/stages`
+ `apigateway:restapis`
+ `apigateway:restapis/deployments`
+ `apigateway:restapis/resources`
+ `apigateway:restapis/resources/methods`
+ `apigateway:restapis/stages`
+ `apigateway:vpclinks`

### Direct Connect
<a name="services-directconnect"></a>
+ `directconnect:dx-gateway`

### AWS Partner Network
<a name="services-partnercentral"></a>
+ `partnercentral:catalog/engagement`
+ `partnercentral:catalog/engagement-invitation`
+ `partnercentral:catalog/opportunity`
+ `partnercentral:catalog/resource-snapshot-job`
+ `partnercentral:resourcesnapshot`

### AWS Shield
<a name="services-shield"></a>
+ `shield:protection`
+ `shield:protection-group`

### AWS Systems Manager Incident Manager
<a name="services-ssm-incidents"></a>
+ `ssm-incidents:response-plan`

### AWS WAFV2
<a name="services-wafv2"></a>
+ `wafv2:ipset`
+ `wafv2:regexpatternset`
+ `wafv2:rulegroup`
+ `wafv2:webacl`

### Amazon Macie
<a name="services-macie2"></a>
+ `macie2:allow-list`
+ `macie2:custom-data-identifier`
+ `macie2:findings-filter`
+ `macie2:member`

### OpenSearch Service Serverless Service
<a name="services-aoss"></a>
+ `aoss:collection`

### Amazon S3 Express
<a name="services-s3express"></a>
+ `s3express:bucket`

### Amazon VPC Lattice
<a name="services-vpc-lattice"></a>
+ `vpc-lattice:service`
+ `vpc-lattice:service/listener`
+ `vpc-lattice:servicenetwork`
+ `vpc-lattice:servicenetworkserviceassociation`
+ `vpc-lattice:targetgroup`

### Amazon Verified Permissions
<a name="services-verifiedpermissions"></a>
+ `verifiedpermissions:policy-store`

### Amazon WorkSpaces Web
<a name="services-workspaces-web"></a>
+ `workspaces-web:portal`

### AWS Amplify
<a name="services-amplify"></a>
+ `amplify:apps`
+ `amplify:apps/branches`
+ `amplify:apps/domains`

### AWS App Runner
<a name="services-apprunner"></a>
+ `apprunner:autoscalingconfiguration`
+ `apprunner:connection`
+ `apprunner:service`
+ `apprunner:vpcconnector`

### AWS AppConfig
<a name="services-appconfig"></a>
+ `appconfig:application`
+ `appconfig:application/environment`
+ `appconfig:deploymentstrategy`
+ `appconfig:extensionassociation`

### Amazon AppFlow
<a name="services-appflow"></a>
+ `appflow:flow`

### AppIntegrations
<a name="services-app-integrations"></a>
+ `app-integrations:application`
+ `app-integrations:event-integration`

### AWS App Mesh
<a name="services-appmesh"></a>
+ `appmesh:mesh`
+ `appmesh:mesh/virtualGateway`
+ `appmesh:mesh/virtualGateway/gatewayRoute`
+ `appmesh:mesh/virtualNode`
+ `appmesh:mesh/virtualRouter`
+ `appmesh:mesh/virtualRouter/route`
+ `appmesh:mesh/virtualService`

### Amazon AppStream
<a name="services-appstream"></a>
+ `appstream:app-block`
+ `appstream:application`
+ `appstream:fleet`
+ `appstream:image-builder`
+ `appstream:stack`

### AWS AppSync
<a name="services-appsync"></a>
+ `appsync:apis`

### AWS Application Discovery Service
<a name="services-ds"></a>
+ `ds:directory`

### Amazon Application Recovery Controller (ARC)
<a name="services-route53-recovery-control"></a>
+ `route53-recovery-control:cluster`
+ `route53-recovery-control:controlpanel/routingcontrol`
+ `route53-recovery-control:controlpanel/safetyrule`

### Amazon Athena
<a name="services-athena"></a>
+ `athena:datacatalog`
+ `athena:workgroup`

### AWS Audit Manager
<a name="services-auditmanager"></a>
+ `auditmanager:assessment`

### AWS Backup
<a name="services-backup"></a>
+ `backup:backup-plan`
+ `backup:backup-vault`
+ `backup:report-plan`

### AWS Backup gateway
<a name="services-backup-gateway"></a>
+ `backup-gateway:hypervisor`

### AWS Batch
<a name="services-batch"></a>
+ `batch:compute-environment`
+ `batch:job-definition`
+ `batch:job-queue`
+ `batch:scheduling-policy`

### Amazon Bedrock
<a name="services-bedrock"></a>
+ `bedrock:agent`
+ `bedrock:agent-alias`
+ `bedrock:application-inference-profile`
+ `bedrock:data-automation-project`
+ `bedrock:flow`
+ `bedrock:flow/alias`
+ `bedrock:guardrail`
+ `bedrock:knowledge-base`
+ `bedrock:prompt`
+ `bedrock:prompt-router`

### AWS Certificate Manager
<a name="services-acm"></a>
+ `acm:certificate`

### Amazon Chime
<a name="services-chime"></a>
+ `chime:app-instance`
+ `chime:app-instance/bot`
+ `chime:app-instance/user`
+ `chime:media-insights-pipeline-configuration`
+ `chime:media-pipeline-kinesis-video-stream-pool`
+ `chime:sma`
+ `chime:vc`

### AWS Cloud Map
<a name="services-servicediscovery"></a>
+ `servicediscovery:service`

### AWS Cloud9
<a name="services-cloud9"></a>
+ `cloud9:environment`

### CloudFormation
<a name="services-cloudformation"></a>
+ `cloudformation:stack`
+ `cloudformation:stackset`

### Amazon CloudFront
<a name="services-cloudfront"></a>
+ `cloudfront:cache-policy`
+ `cloudfront:continuous-deployment-policy`
+ `cloudfront:distribution`
+ `cloudfront:field-level-encryption-config`
+ `cloudfront:field-level-encryption-profile`
+ `cloudfront:function`
+ `cloudfront:origin-access-control`
+ `cloudfront:origin-access-identity`
+ `cloudfront:origin-request-policy`
+ `cloudfront:realtime-log-config`
+ `cloudfront:response-headers-policy`

### AWS CloudTrail
<a name="services-cloudtrail"></a>
+ `cloudtrail:channel`
+ `cloudtrail:dashboard`
+ `cloudtrail:eventdatastore`
+ `cloudtrail:trail`

### Amazon CloudWatch
<a name="services-cloudwatch"></a>
+ `cloudwatch:alarm`
+ `cloudwatch:dashboard`
+ `cloudwatch:insight-rule`
+ `cloudwatch:metric-stream`

### Amazon CloudWatch Logs
<a name="services-logs"></a>
+ `logs:destination`
+ `logs:log-group`

### Amazon CloudWatch Observability Access Manager
<a name="services-oam"></a>
+ `oam:sink`

### Amazon CloudWatch RUM
<a name="services-rum"></a>
+ `rum:appmonitor`

### Amazon CloudWatch Synthetics
<a name="services-synthetics"></a>
+ `synthetics:canary`
+ `synthetics:group`

### AWS CodeArtifact
<a name="services-codeartifact"></a>
+ `codeartifact:domain`
+ `codeartifact:repository`

### AWS CodeBuild
<a name="services-codebuild"></a>
+ `codebuild:project`

### AWS CodeCommit
<a name="services-codecommit"></a>
+ `codecommit:repository`

### AWS CodeConnections
<a name="services-codeconnections"></a>
+ `codeconnections:connection`

### AWS CodeDeploy
<a name="services-codedeploy"></a>
+ `codedeploy:application`
+ `codedeploy:deploymentconfig`

### Amazon CodeGuru Profiler
<a name="services-codeguru-profiler"></a>
+ `codeguru-profiler:profilingGroup`

### Amazon CodeGuru Reviewer
<a name="services-codeguru-reviewer"></a>
+ `codeguru-reviewer:association`

### AWS CodePipeline
<a name="services-codepipeline"></a>
+ `codepipeline:pipeline`
+ `codepipeline:webhook`

### AWS CodeStar Connections
<a name="services-codestar-connections"></a>
+ `codestar-connections:connection`
+ `codestar-connections:host`

### Amazon Cognito Identity
<a name="services-cognito-identity"></a>
+ `cognito-identity:identitypool`

### Amazon Cognito IdentityPool
<a name="services-cognito-idp"></a>
+ `cognito-idp:userpool`

### Amazon Comprehend
<a name="services-comprehend"></a>
+ `comprehend:document-classifier`
+ `comprehend:entity-recognizer`
+ `comprehend:flywheel`

### AWS Config
<a name="services-config"></a>
+ `config:config-rule`

### Amazon Connect Customer
<a name="services-connect"></a>
+ `connect:instance`
+ `connect:instance/agent`
+ `connect:instance/operating-hours`
+ `connect:instance/queue`
+ `connect:instance/rule`
+ `connect:instance/task-template`
+ `connect:instance/transfer-destination`
+ `connect:phone-number`

### Amazon Connect Customer Customer Profiles
<a name="services-profile"></a>
+ `profile:domains`
+ `profile:domains/integrations`
+ `profile:domains/object-types`

### Connect Customer Wisdom
<a name="services-wisdom"></a>
+ `wisdom:assistant`
+ `wisdom:association`
+ `wisdom:content`
+ `wisdom:knowledge-base`

### AWS Cost Explorer
<a name="services-ce"></a>
+ `ce:anomalymonitor`
+ `ce:anomalysubscription`

### AWS Data Exchange
<a name="services-dataexchange"></a>
+ `dataexchange:data-sets`
+ `dataexchange:data-sets/revisions`

### AWS Data Pipeline
<a name="services-datapipeline"></a>
+ `datapipeline:pipeline`

### AWS DataSync
<a name="services-datasync"></a>
+ `datasync:location`
+ `datasync:task`

### AWS Database Migration Service
<a name="services-dms"></a>
+ `dms:cert`
+ `dms:endpoint`
+ `dms:es`
+ `dms:rep`
+ `dms:subgrp`
+ `dms:task`

### Amazon Detective
<a name="services-detective"></a>
+ `detective:graph`

### AWS Device Farm
<a name="services-devicefarm"></a>
+ `devicefarm:instanceprofile`
+ `devicefarm:project`
+ `devicefarm:testgrid-project`

### Amazon DynamoDB
<a name="services-dynamodb"></a>
+ `dynamodb:table`

### DynamoDB Accelerator
<a name="services-dax"></a>
+ `dax:cache`

### Amazon EC2 Auto Scaling
<a name="services-autoscaling"></a>
+ `autoscaling:autoScalingGroup`

### EC2 Image Builder
<a name="services-imagebuilder"></a>
+ `imagebuilder:component`
+ `imagebuilder:container-recipe`
+ `imagebuilder:distribution-configuration`
+ `imagebuilder:image`
+ `imagebuilder:image-pipeline`
+ `imagebuilder:image-recipe`
+ `imagebuilder:infrastructure-configuration`

### Amazon EMR
<a name="services-elasticmapreduce"></a>
+ `elasticmapreduce:cluster`

### Amazon EMR Serverless
<a name="services-emr-serverless"></a>
+ `emr-serverless:applications`

### Amazon EMR on EKS
<a name="services-emr-containers"></a>
+ `emr-containers:jobtemplates`
+ `emr-containers:securityconfigurations`
+ `emr-containers:virtualclusters`
+ `emr-containers:virtualclusters/endpoints`

### Amazon ElastiCache
<a name="services-elasticache"></a>
+ `elasticache:cluster`
+ `elasticache:globalreplicationgroup`
+ `elasticache:parametergroup`
+ `elasticache:replicationgroup`
+ `elasticache:reserved-instance`
+ `elasticache:snapshot`
+ `elasticache:subnetgroup`
+ `elasticache:user`
+ `elasticache:usergroup`

### AWS Elastic Beanstalk
<a name="services-elasticbeanstalk"></a>
+ `elasticbeanstalk:application`
+ `elasticbeanstalk:applicationversion`
+ `elasticbeanstalk:configurationtemplate`
+ `elasticbeanstalk:environment`

### Amazon Elastic Compute Cloud (Amazon EC2)
<a name="services-ec2"></a>
+ `ec2:capacity-reservation`
+ `ec2:capacity-reservation-fleet`
+ `ec2:carrier-gateway`
+ `ec2:client-vpn-endpoint`
+ `ec2:customer-gateway`
+ `ec2:dedicated-host`
+ `ec2:dhcp-options`
+ `ec2:egress-only-internet-gateway`
+ `ec2:elastic-ip`
+ `ec2:fleet`
+ `ec2:fpga-image`
+ `ec2:host-reservation`
+ `ec2:image`
+ `ec2:instance`
+ `ec2:instance-event-window`
+ `ec2:internet-gateway`
+ `ec2:ipam`
+ `ec2:ipam-pool`
+ `ec2:ipam-resource-discovery`
+ `ec2:ipam-resource-discovery-association`
+ `ec2:ipam-scope`
+ `ec2:ipv4pool-ec2`
+ `ec2:key-pair`
+ `ec2:launch-template`
+ `ec2:natgateway`
+ `ec2:network-acl`
+ `ec2:network-insights-access-scope`
+ `ec2:network-insights-access-scope-analysis`
+ `ec2:network-insights-analysis`
+ `ec2:network-insights-path`
+ `ec2:network-interface`
+ `ec2:placement-group`
+ `ec2:prefix-list`
+ `ec2:reserved-instances`
+ `ec2:route-table`
+ `ec2:security-group`
+ `ec2:security-group-rule`
+ `ec2:snapshot`
+ `ec2:spot-fleet-request`
+ `ec2:spot-instances-request`
+ `ec2:subnet`
+ `ec2:subnet-cidr-reservation`
+ `ec2:traffic-mirror-filter`
+ `ec2:traffic-mirror-filter-rule`
+ `ec2:traffic-mirror-session`
+ `ec2:traffic-mirror-target`
+ `ec2:transit-gateway`
+ `ec2:transit-gateway-attachment`
+ `ec2:transit-gateway-connect-peer`
+ `ec2:transit-gateway-multicast-domain`
+ `ec2:transit-gateway-policy-table`
+ `ec2:transit-gateway-route-table`
+ `ec2:transit-gateway-route-table-announcement`
+ `ec2:verified-access-endpoint`
+ `ec2:verified-access-group`
+ `ec2:verified-access-instance`
+ `ec2:verified-access-trust-provider`
+ `ec2:volume`
+ `ec2:vpc`
+ `ec2:vpc-endpoint`
+ `ec2:vpc-flow-log`
+ `ec2:vpc-peering-connection`
+ `ec2:vpn-connection`
+ `ec2:vpn-gateway`

### Amazon Elastic Container Registry
<a name="services-ecr"></a>
+ `ecr:repository`

### Amazon Elastic Container Registry Public
<a name="services-ecr-public"></a>
+ `ecr-public:repository`

### Amazon Elastic Container Service
<a name="services-ecs"></a>
+ `ecs:capacity-provider`
+ `ecs:cluster`
+ `ecs:container-instance`
+ `ecs:service`
+ `ecs:task-definition`
+ `ecs:task-set`

### Amazon Elastic File System
<a name="services-elasticfilesystem"></a>
+ `elasticfilesystem:access-point`
+ `elasticfilesystem:file-system`

### Amazon Elastic Kubernetes Service (Amazon EKS)
<a name="services-eks"></a>
+ `eks:cluster`
+ `eks:daemonset`
+ `eks:deployment`
+ `eks:eks-anywhere-subscription`
+ `eks:endpointslice`
+ `eks:ingress`
+ `eks:namespace`
+ `eks:persistentvolume`
+ `eks:podidentityassociation`
+ `eks:replicaset`
+ `eks:service`
+ `eks:statefulset`

### Elastic Load Balancing
<a name="services-elasticloadbalancing"></a>
+ `elasticloadbalancing:listener-rule/app`
+ `elasticloadbalancing:listener/app`
+ `elasticloadbalancing:listener/gwy`
+ `elasticloadbalancing:listener/net`
+ `elasticloadbalancing:loadbalancer`
+ `elasticloadbalancing:loadbalancer/app`
+ `elasticloadbalancing:loadbalancer/gwy`
+ `elasticloadbalancing:loadbalancer/net`
+ `elasticloadbalancing:targetgroup`

### AWS Elemental MediaPackage
<a name="services-mediapackage"></a>
+ `mediapackage:channels`
+ `mediapackage:origin_endpoints`

### AWS Elemental MediaPackage VoD
<a name="services-mediapackage-vod"></a>
+ `mediapackage-vod:assets`
+ `mediapackage-vod:packaging-configurations`
+ `mediapackage-vod:packaging-groups`

### AWS Elemental MediaStore
<a name="services-mediastore"></a>
+ `mediastore:container`

### AWS Elemental MediaTailor
<a name="services-mediatailor"></a>
+ `mediatailor:channel`
+ `mediatailor:liveSource`
+ `mediatailor:playbackConfiguration`
+ `mediatailor:vodSource`

### Amazon CloudWatch Events
<a name="services-events"></a>
+ `events:api-destination`
+ `events:archive`
+ `events:connection`
+ `events:endpoint`
+ `events:event-bus`
+ `events:rule`

### Amazon EventBridge Pipes
<a name="services-pipes"></a>
+ `pipes:pipe`

### Amazon EventBridge Scheduler
<a name="services-scheduler"></a>
+ `scheduler:schedule-group`

### Amazon EventBridge Schemas
<a name="services-schemas"></a>
+ `schemas:discoverer`

### Amazon FSx
<a name="services-fsx"></a>
+ `fsx:backup`
+ `fsx:file-system`

### AWS Fault Injection Service
<a name="services-fis"></a>
+ `fis:experiment`
+ `fis:experiment-template`

### Amazon FinSpace
<a name="services-finspace"></a>
+ `finspace:environment`

### Firehose
<a name="services-firehose"></a>
+ `firehose:deliverystream`

### Amazon Forecast
<a name="services-forecast"></a>
+ `forecast:dataset`
+ `forecast:dataset-group`
+ `forecast:dataset-import-job`
+ `forecast:forecast`
+ `forecast:forecast-export-job`
+ `forecast:predictor`
+ `forecast:predictor-backtest-export-job`

### Amazon Fraud Detector
<a name="services-frauddetector"></a>
+ `frauddetector:detector`
+ `frauddetector:entity-type`
+ `frauddetector:event-type`
+ `frauddetector:external-model`
+ `frauddetector:label`
+ `frauddetector:model`
+ `frauddetector:outcome`
+ `frauddetector:variable`

### Amazon GameLift Servers
<a name="services-gamelift"></a>
+ `gamelift:alias`
+ `gamelift:build`
+ `gamelift:gamesessionqueue`
+ `gamelift:location`
+ `gamelift:matchmakingconfiguration`
+ `gamelift:matchmakingruleset`
+ `gamelift:script`

### AWS Global Accelerator
<a name="services-globalaccelerator"></a>
+ `globalaccelerator:accelerator`
+ `globalaccelerator:accelerator/listener`
+ `globalaccelerator:accelerator/listener/endpoint-group`

### AWS Glue
<a name="services-glue"></a>
+ `glue:crawler`
+ `glue:dataQualityRuleset`
+ `glue:database`
+ `glue:job`
+ `glue:mlTransform`
+ `glue:registry`
+ `glue:table`
+ `glue:trigger`

### AWS Glue DataBrew
<a name="services-databrew"></a>
+ `databrew:dataset`
+ `databrew:job`
+ `databrew:project`
+ `databrew:recipe`
+ `databrew:ruleset`
+ `databrew:schedule`

### AWS Ground Station
<a name="services-groundstation"></a>
+ `groundstation:config`
+ `groundstation:dataflow-endpoint-group`
+ `groundstation:mission-profile`

### Amazon GuardDuty
<a name="services-guardduty"></a>
+ `guardduty:detector`
+ `guardduty:detector/filter`
+ `guardduty:detector/ipset`
+ `guardduty:detector/publishingDestination`
+ `guardduty:detector/threatintelset`
+ `guardduty:malware-protection-plan`

### AWS HealthLake
<a name="services-healthlake"></a>
+ `healthlake:datastore/fhir`

### AWS HealthOmics
<a name="services-omics"></a>
+ `omics:referenceStore`
+ `omics:runGroup`
+ `omics:workflow`

### IAM Access Analyzer
<a name="services-access-analyzer"></a>
+ `access-analyzer:analyzer`

### Amazon IVS
<a name="services-ivschat"></a>
+ `ivschat:logging-configuration`
+ `ivschat:room`

### AWS Identity and Access Management
<a name="services-iam"></a>
+ `iam:group`
+ `iam:instance-profile`
+ `iam:mfa`
+ `iam:oidc-provider`
+ `iam:policy`
+ `iam:role`
+ `iam:saml-provider`
+ `iam:server-certificate`
+ `iam:user`

### Amazon Inspector
<a name="services-inspector"></a>
+ `inspector2:filter`

### Amazon Interactive Video Service
<a name="services-ivs"></a>
+ `ivs:channel`
+ `ivs:encoder-configuration`
+ `ivs:ingest-configuration`
+ `ivs:playback-key`
+ `ivs:playback-restriction-policy`
+ `ivs:recording-configuration`
+ `ivs:storage-configuration`
+ `ivs:stream-key`

### AWS IoT
<a name="services-iot"></a>
+ `iot:authorizer`
+ `iot:billinggroup`
+ `iot:cacert`
+ `iot:cert`
+ `iot:fleetmetric`
+ `iot:job`
+ `iot:jobtemplate`
+ `iot:mitigationaction`
+ `iot:policy`
+ `iot:provisioningtemplate`
+ `iot:rolealias`
+ `iot:rule`
+ `iot:ruledestination`
+ `iot:scheduledaudit`
+ `iot:securityprofile`
+ `iot:thing`
+ `iot:thinggroup`
+ `iot:thingtype`

### AWS IoT Core Device Advisor
<a name="services-iotdeviceadvisor"></a>
+ `iotdeviceadvisor:suitedefinition`

### AWS IoT FleetWise
<a name="services-iotfleetwise"></a>
+ `iotfleetwise:decoder-manifest`
+ `iotfleetwise:model-manifest`
+ `iotfleetwise:signal-catalog`
+ `iotfleetwise:vehicle`

### AWS IoT Greengrass
<a name="services-greengrass"></a>
+ `greengrass:components:versions`
+ `greengrass:connectorsDefinition`
+ `greengrass:coresDefinition`
+ `greengrass:devicesDefinition`
+ `greengrass:functionsDefinition`
+ `greengrass:groups`
+ `greengrass:loggersDefinition`
+ `greengrass:resourcesDefinition`
+ `greengrass:subscriptionsDefinition`

### AWS IoT SiteWise
<a name="services-iotsitewise"></a>
+ `iotsitewise:access-policy`
+ `iotsitewise:asset`
+ `iotsitewise:asset-model`
+ `iotsitewise:dashboard`
+ `iotsitewise:gateway`
+ `iotsitewise:portal`
+ `iotsitewise:project`

### AWS IoT TwinMaker
<a name="services-iottwinmaker"></a>
+ `iottwinmaker:workspace`
+ `iottwinmaker:workspace/component-type`
+ `iottwinmaker:workspace/entity`
+ `iottwinmaker:workspace/sync-job`

### AWS IoT Wireless
<a name="services-iotwireless"></a>
+ `iotwireless:Destination`
+ `iotwireless:DeviceProfile`
+ `iotwireless:FuotaTask`
+ `iotwireless:MulticastGroup`
+ `iotwireless:ServiceProfile`
+ `iotwireless:SidewalkAccount`
+ `iotwireless:WirelessDevice`
+ `iotwireless:WirelessGateway`
+ `iotwireless:WirelessGatewayTaskDefinition`

### Amazon Kendra
<a name="services-kendra"></a>
+ `kendra:index`
+ `kendra:index/access-control-configuration`
+ `kendra:index/data-source`
+ `kendra:index/experience`
+ `kendra:index/faq`
+ `kendra:index/featured-results-set`
+ `kendra:index/query-suggestions-block-list`
+ `kendra:index/thesaurus`

### AWS Key Management Service
<a name="services-kms"></a>
+ `kms:key`

### Amazon Kinesis
<a name="services-kinesis"></a>
+ `kinesis:stream`

### Amazon Managed Service for Apache Flink
<a name="services-kinesisanalytics"></a>
+ `kinesisanalytics:application`

### Amazon Kinesis Video Streams
<a name="services-kinesisvideo"></a>
+ `kinesisvideo:channel`
+ `kinesisvideo:stream`

### AWS Lambda
<a name="services-lambda"></a>
+ `lambda:code-signing-config`
+ `lambda:event-source-mapping`
+ `lambda:function`
+ `lambda:function/version`
+ `lambda:layer/version`

### Amazon Lex
<a name="services-lex"></a>
+ `lex:bot`
+ `lex:bot-alias`

### AWS License Manager
<a name="services-license-manager"></a>
+ `license-manager:grant`

### Amazon MQ
<a name="services-mq"></a>
+ `mq:broker`
+ `mq:configuration`

### AWS Mainframe Modernization
<a name="services-m2"></a>
+ `m2:env`

### Amazon Managed Blockchain
<a name="services-managedblockchain"></a>
+ `managedblockchain:accessors`

### Amazon Managed Grafana
<a name="services-grafana"></a>
+ `grafana:workspaces`

### Amazon Managed Service for Prometheus
<a name="services-aps"></a>
+ `aps:rulegroupsnamespace`
+ `aps:workspace`

### Amazon Managed Streaming for Apache Kafka
<a name="services-kafka"></a>
+ `kafka:cluster`
+ `kafka:configuration`

### Amazon Managed Workflows for Apache Airflow
<a name="services-airflow"></a>
+ `airflow:environment`

### Amazon MemoryDB
<a name="services-memorydb"></a>
+ `memorydb:acl`
+ `memorydb:cluster`
+ `memorydb:parametergroup`
+ `memorydb:snapshot`
+ `memorydb:subnetgroup`
+ `memorydb:user`

### AWS Migration Hub Refactor Spaces
<a name="services-refactor-spaces"></a>
+ `refactor-spaces:environment`
+ `refactor-spaces:environment/application`
+ `refactor-spaces:environment/application/route`
+ `refactor-spaces:environment/application/service`

### AWS Mobile Targeting
<a name="services-mobiletargeting"></a>
+ `mobiletargeting:apps/campaigns`
+ `mobiletargeting:apps/segments`
+ `mobiletargeting:templates/EMAIL`
+ `mobiletargeting:templates/PUSH`
+ `mobiletargeting:templates/SMS`

### AWS Network Firewall
<a name="services-network-firewall"></a>
+ `network-firewall:firewall`
+ `network-firewall:firewall-policy`
+ `network-firewall:stateful-rulegroup`
+ `network-firewall:stateless-rulegroup`

### AWS Network Manager
<a name="services-networkmanager"></a>
+ `networkmanager:attachment`
+ `networkmanager:core-network`
+ `networkmanager:device`
+ `networkmanager:global-network`
+ `networkmanager:link`

### Amazon OpenSearch Service
<a name="services-es"></a>
+ `es:domain`

### AWS Outposts
<a name="services-outposts"></a>
+ `outposts:site`

### Amazon Personalize
<a name="services-personalize"></a>
+ `personalize:dataset`
+ `personalize:dataset-group`
+ `personalize:schema`
+ `personalize:solution`

### AWS Private Certificate Authority
<a name="services-acm-pca"></a>
+ `acm-pca:certificate-authority`

### AWS Proton
<a name="services-proton"></a>
+ `proton:environment-account-connection`
+ `proton:environment-template`
+ `proton:service-template`

### Amazon Quick
<a name="services-quicksight"></a>
+ `quicksight:dataset`
+ `quicksight:datasource`
+ `quicksight:template`
+ `quicksight:theme`

### Amazon Redshift
<a name="services-redshift"></a>
+ `redshift:cluster`
+ `redshift:eventsubscription`
+ `redshift:hsmclientcertificate`
+ `redshift:parametergroup`
+ `redshift:snapshot`
+ `redshift:snapshotcopygrant`
+ `redshift:snapshotschedule`
+ `redshift:subnetgroup`
+ `redshift:usagelimit`

### Amazon Rekognition
<a name="services-rekognition"></a>
+ `rekognition:project`

### Amazon Relational Database Service (Amazon RDS)
<a name="services-rds"></a>
+ `rds:auto-backup`
+ `rds:cev`
+ `rds:cluster`
+ `rds:cluster-endpoint`
+ `rds:cluster-pg`
+ `rds:cluster-snapshot`
+ `rds:db`
+ `rds:db-proxy`
+ `rds:db-proxy-endpoint`
+ `rds:deployment`
+ `rds:es`
+ `rds:global-cluster`
+ `rds:og`
+ `rds:pg`
+ `rds:ri`
+ `rds:secgrp`
+ `rds:snapshot`
+ `rds:subgrp`

### AWS Resilience Hub
<a name="services-resiliencehub"></a>
+ `resiliencehub:app`
+ `resiliencehub:resiliency-policy`

### AWS Resource Access Manager
<a name="services-ram"></a>
+ `ram:permission`
+ `ram:resource-share`

### AWS Resource Groups
<a name="services-resource-groups"></a>
+ `resource-groups:group`

### AWS Resource Explorer
<a name="services-resource-explorer-2"></a>
+ `resource-explorer-2:index`
+ `resource-explorer-2:view`

### Amazon Route 53
<a name="services-route53"></a>
+ `route53:domain`
+ `route53:healthcheck`
+ `route53:hostedzone`

### Amazon Route 53 Recovery Readiness
<a name="services-route53-recovery-readiness"></a>
+ `route53-recovery-readiness:cell`
+ `route53-recovery-readiness:readiness-check`
+ `route53-recovery-readiness:recovery-group`
+ `route53-recovery-readiness:resource-set`

### Amazon Route 53 Resolver
<a name="services-route53resolver"></a>
+ `route53resolver:firewall-domain-list`
+ `route53resolver:firewall-rule-group`
+ `route53resolver:firewall-rule-group-association`
+ `route53resolver:resolver-endpoint`
+ `route53resolver:resolver-query-log-config`
+ `route53resolver:resolver-rule`

### Amazon Glacier
<a name="services-glacier"></a>
+ `glacier:vaults`

### Amazon SageMaker AI
<a name="services-sagemaker"></a>
+ `sagemaker:action`
+ `sagemaker:algorithm`
+ `sagemaker:app`
+ `sagemaker:app-image-config`
+ `sagemaker:artifact`
+ `sagemaker:cluster`
+ `sagemaker:code-repository`
+ `sagemaker:context`
+ `sagemaker:domain`
+ `sagemaker:endpoint`
+ `sagemaker:endpoint-config`
+ `sagemaker:experiment`
+ `sagemaker:experiment-trial`
+ `sagemaker:experiment-trial-component`
+ `sagemaker:feature-group`
+ `sagemaker:flow-definition`
+ `sagemaker:hub`
+ `sagemaker:hub-content`
+ `sagemaker:human-loop`
+ `sagemaker:human-task-ui`
+ `sagemaker:image`
+ `sagemaker:image-version`
+ `sagemaker:inference-component`
+ `sagemaker:inference-experiment`
+ `sagemaker:mlflow-tracking-server`
+ `sagemaker:model`
+ `sagemaker:model-card`
+ `sagemaker:model-package`
+ `sagemaker:model-package-group`
+ `sagemaker:monitoring-schedule`
+ `sagemaker:notebook-instance`
+ `sagemaker:notebook-instance-lifecycle-config`
+ `sagemaker:partner-app`
+ `sagemaker:pipeline`
+ `sagemaker:project`
+ `sagemaker:space`
+ `sagemaker:studio-lifecycle-config`
+ `sagemaker:user-profile`
+ `sagemaker:workforce`
+ `sagemaker:workteam`

### AWS Secrets Manager
<a name="services-secretsmanager"></a>
+ `secretsmanager:secret`

### AWS Service Catalog
<a name="services-servicecatalog"></a>
+ `servicecatalog:applications`
+ `servicecatalog:attribute-groups`

### AWS Signer
<a name="services-signer"></a>
+ `signer:signing-profiles`

### Amazon Simple Email Service
<a name="services-ses"></a>
+ `ses:configuration-set`
+ `ses:contact-list`
+ `ses:dedicated-ip-pool`
+ `ses:identity`

### Amazon Simple Notification Service
<a name="services-sns"></a>
+ `sns:topic`

### Amazon Simple Queue Service
<a name="services-sqs"></a>
+ `sqs:queue`

### Amazon Simple Storage Service (Amazon S3)
<a name="services-s3"></a>
+ `s3:accesspoint`
+ `s3:bucket`
+ `s3:multiregionaccesspoint`
+ `s3:storage-lens`
+ `s3:storage-lens-group`

### AWS Step Functions States Language
<a name="services-states"></a>
+ `states:activity`
+ `states:stateMachine`

### Storage Gateway
<a name="services-storagegateway"></a>
+ `storagegateway:gateway`
+ `storagegateway:share`

### AWS Systems Manager
<a name="services-ssm"></a>
+ `ssm:association`
+ `ssm:document`
+ `ssm:maintenancewindow`
+ `ssm:managed-instance`
+ `ssm:parameter`
+ `ssm:resource-data-sync`
+ `ssm:session`
+ `ssm:windowtarget`
+ `ssm:windowtask`

### AWS Transfer Family
<a name="services-transfer"></a>
+ `transfer:agreement`
+ `transfer:certificate`
+ `transfer:connector`
+ `transfer:profile`
+ `transfer:server`
+ `transfer:user`
+ `transfer:workflow`

### Amazon WorkSpaces
<a name="services-workspaces"></a>
+ `workspaces:connectionalias`
+ `workspaces:workspace`

### Amazon Bedrock AgentCore
<a name="services-bedrock-agentcore"></a>
+ `bedrock-agentcore:runtime`

### AWS Budgets
<a name="services-budgets"></a>
+ `budgets:budget`
+ `budgets:budget/action`

### AWS Clean Rooms
<a name="services-cleanrooms"></a>
+ `cleanrooms:collaboration`

### Amazon Data Lifecycle Manager
<a name="services-dlm"></a>
+ `dlm:policy`

### Amazon Kendra Intelligent Ranking
<a name="services-kendra-ranking"></a>
+ `kendra-ranking:rescore-execution-plan`

### AWS Elemental MediaConnect
<a name="services-mediaconnect"></a>
+ `mediaconnect:flow`
+ `mediaconnect:gateway`

### AWS Well-Architected Tool
<a name="services-wellarchitected"></a>
+ `wellarchitected:workload`

### AWS X-Ray
<a name="services-xray"></a>
+ `xray:sampling-rule`

## Programmatically accessing the list of supported resource types
<a name="programmatic-access"></a>

To access the list of supported resource types from code, you can invoke the [ListSupportedResourceTypes](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListSupportedResourceTypes.html) operation from any AWS SDK.

For example, you can run the [list-supported-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-supported-resource-types.html) AWS Command Line Interface (AWS CLI) command, as shown in the following example.

```
$ aws resource-explorer-2 list-supported-resource-types
{
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
... truncated for brevity ...
```

## Resource types that appear as other types
<a name="resource-type-exceptions"></a>

Some resource types are identified by [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) strings that share a common format with another resource type. When this happens, Resource Explorer can report such resources as that other resource type. This affects the resource types in the following table.


| Actual resource type | Reported as resource type | 
| --- | --- | 
| `ec2:securitygroupegress`<br />`ec2:securitygroupingress` | `ec2:security-group-rule` | 
| `elasticloadbalancingv2:loadbalancer` | `elasticloadbalancing:loadbalancer` | 
| `docdb:dbcluster`<br />`neptune:dbcluster`<br />`rds:dbcluster` | `rds:cluster` | 
| `docdb:dbclusterparametergroup`<br />`neptune:dbclusterparametergroup`<br />`rds:dbclusterparametergroup` | `rds:cluster-pg` | 
| `docdb:clustersnapshot`<br />`neptune:dbclustersnapshot`<br />`rds:clustersnapshot` | `rds:cluster-snapshot` | 
| `docdb:dbinstance`<br />`neptune:dbinstance`<br />`rds:dbinstance` | `rds:db` | 
| `docdb:eventsubscription`<br />`neptune:eventsubscription`<br />`rds:eventsubscription` | `rds:es` | 
| `docdb:globalcluster`<br />`rds:globalcluster` | `rds:global-cluster` | 
| `neptune:dbparametergroup`<br />`rds:dbparametergroup` | `rds:pg` | 
| `docdb:dbsubnetgroup`<br />`neptune:dbsubnetgroup`<br />`rds:dbsubnetgroup` | `rds:subgrp` | 