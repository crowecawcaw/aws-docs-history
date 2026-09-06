

# Included AWS Services
<a name="resource-tagging-included-services"></a>

The following AWS services are supported for resource tagging implementation. Resources must be tagged with key `aws-apn-id` and value `pc:product-code` format.

For a downloadable version of this list, download the [Resource Tagging Included Services (CSV)](samples/resource-tagging-included-services.zip).


**Resource Tagging Included Services**  

| Service Name | Product Service Code | Notes | 
| --- | --- | --- | 
| Amazon API Gateway | AmazonApiGateway | None | 
| Amazon AppStream | AmazonAppStream | Excludes User Fees | 
| AWS AppSync | AWSAppSync | None | 
| Amazon Athena | AmazonAthena | None | 
| Aurora DSQL | AuroraDSQL | None | 
| AWS Backup | AWSBackup | None | 
| Amazon Bedrock | AmazonBedrock | Includes only [Amazon models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-amazon.html) and [Open Source models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) available in Amazon Bedrock | 
| Amazon Bedrock AgentCore | AmazonBedrockAgentCore | Includes AgentCore RunTime, Browser Tool, Code Interpreter, Gateway, Identity, and Memory | 
| AWS Certificate Manager | AWSCertificateManager | Includes AWS Certificate Manager Private CA | 
| Amazon Cloud Directory | AmazonCloudDirectory | None | 
| AWS Cloud WAN | AWSCloudWAN | Excludes Core Network Edge Hours and data transfer | 
| Amazon CloudFront | AmazonCloudFront | Excludes data transfer costs and Lambda@Edge | 
| AWS CloudHSM | CloudHSM | None | 
| Amazon CloudWatch | AmazonCloudWatch | Logs only | 
| AWS CodeBuild | CodeBuild | None | 
| AWS CodePipeline | AWSCodePipeline | None | 
| AWS CodeStar | AWSCodeStar | None | 
| Amazon Cognito | AmazonCognito | Excludes Amazon Cognito add-ons | 
| Amazon Comprehend | comprehend | None | 
| Amazon Connect | AmazonConnect | Includes Full Connect Unlimited AI and A La Carte; excludes Cases, Entity Resolution, Legacy Pinpoint Engagement, Meetings SDK, ContactLens, Chat, Email, Lex, Q in Connect, Tasks, Voice, Customer Profiles, Outbound Campaigns Processing, Telephony | 
| AWS Data Pipeline | datapipeline | None | 
| AWS Database Migration Service | AWSDatabaseMigrationSvc | None | 
| AWS DataSync | AWSDataSync | None | 
| AWS Deadline Cloud | AWSDeadlineCloud | Excludes AWS data transfer charges and Bring-Your-Own-License third-party creative tool software license costs | 
| AWS Direct Connect | AWSDirectConnect | Excludes AWS Local Zones | 
| AWS Directory Service | AWSDirectoryService | None | 
| Amazon DocumentDB (with MongoDB compatibility) | AmazonDocDB | None | 
| Amazon DynamoDB | AmazonDynamoDB | None | 
| Amazon DynamoDB Accelerator (DAX) | AmazonDAX | None | 
| Amazon EC2 | AmazonEC2 | Includes Amazon EBS, EBS Snapshots, EC2 Mac, AWS Local Zones deployment, Savings Plan for ML instance types; excludes Capacity Block for ML | 
| Amazon ECR | AmazonECR | None | 
| Amazon ECS | AmazonECS | Includes Fargate and AWS App Mesh | 
| Amazon EKS | AmazonEKS | Excludes Fargate; includes AWS App Mesh | 
| Amazon Elastic VMware Service (Amazon EVS) | AmazonEC2 | Only includes underlying Amazon EC2 use; excludes VCF licenses, VPC Route Server Endpoints, EVS control plane | 
| AWS Elastic Beanstalk | AWSElasticBeanstalk | None | 
| AWS Elastic Disaster Recovery (DRS) | AWSElasticDisasterRecovery | None | 
| Amazon Elastic File System | AmazonEFS | None | 
| Amazon ElastiCache | AmazonElastiCache | None | 
| AWS Elemental MediaConvert | AWSElementalMediaConvert | None | 
| AWS Elemental MediaLive | AWSElementalMediaLive | None | 
| AWS Elemental MediaPackage | AWSElementalMediaPackage | None | 
| Amazon EMR | ElasticMapReduce | Includes AWS Local Zones deployment | 
| AWS End User Messaging | AmazonPinpoint | Excludes Carrier Fees, Carrier Fee Count, Number Information (Carrier Lookup), Numbers Validated, Phone numbers, SMS Inbound Price | 
| Amazon FinSpace | AmazonFinSpace | Excludes any kdb Insights software license amount | 
| Amazon FSx | AmazonFSx | None | 
| Amazon GameLift | AmazonGameLift | Excludes GameLift Anywhere, FleetIQ, and FlexMatch when using either EC2 for GameLift or On-premises for GameLift | 
| AWS Glue | AWSGlue | None | 
| AWS HealthImaging | AmazonMedicalImaging | None | 
| AWS HealthLake | AmazonHealthLake | Excludes FHIR data export and transformation | 
| AWS IoT Core | AWSIoT | Excludes Registry operations | 
| AWS IoT SiteWise | AWSIoTSiteWise | Excludes Alarm, Query, Data Storage - Warm Storage, Edge - Data collection pack, Assistant - Monthly Enablement Fee, Assistant - API bundle price, Messaging - Bulk Import, Data Export - Bulk Import | 
| Amazon Kendra | AmazonKendra | None | 
| AWS Key Management Service | awskms | Excludes cross-account request costs | 
| Amazon Keyspaces (for Apache Cassandra) | AmazonMCS | None | 
| Amazon Kinesis Data Analytics | AmazonKinesisAnalytics | None | 
| Amazon Kinesis Data Firehose | AmazonKinesisFirehose | None | 
| Amazon Kinesis Data Streams | AmazonKinesis | None | 
| Amazon Kinesis Video Streams | AmazonKinesisVideo | None | 
| AWS Lambda | AWSLambda | None | 
| Elastic Load Balancing | AWSELB | None | 
| AWS Mainframe Modernization | AWSM2 | Excludes 'M2 Custom' and Blu Age Transformation Center costs | 
| Amazon MemoryDB for Redis | AmazonMemoryDB | Excludes Snapshot Storage | 
| Amazon MQ | AmazonMQ | None | 
| Amazon MSK | AmazonMSK | None | 
| Amazon Neptune | AmazonNeptune | None | 
| AWS Network Firewall | AWSNetworkFirewall | None | 
| Amazon Omics | AmazonOmics | None | 
| Amazon OpenSearch Service | AmazonES | Includes Amazon Elasticsearch Service; excludes OpenSearch Serverless and OpenSearch Ingestion | 
| AWS Payment Cryptography | PaymentCryptography | Excludes following APIs under Requests usage: ListAliases, ListKeys, GetResourcePolicy, GetParametersForImport, GetParametersForExport, DeleteResourcePolicy, DeleteAlias, CreateKey, CreateAlias | 
| Amazon QuickSight | AmazonQuickSight | Excludes Region fee for Q, SPICE, unused charges on subscription packs, Pro user, Pro author, and administrator | 
| Amazon Redshift | AmazonRedshift | Amazon Redshift Provisioned and Amazon Redshift Serverless | 
| Amazon Relational Database Service (RDS) | AmazonRDS | Includes all RDS engines, Amazon RDS Custom, AWS Local Zones deployment; excludes Db2 licensing fees | 
| AWS Resilience Hub | AWSResilienceHub | None | 
| Amazon Route 53 | AmazonRoute53 | Excludes Amazon Route 53 Resolver, Traffic Flow, and CIDR block storage | 
| Amazon S3 | AmazonS3 | Includes storage cost only and all storage tiers; excludes Requests | 
| Amazon S3 Glacier | AmazonGlacier | Excludes Glacier Deep Archive | 
| Amazon SageMaker AI | AmazonSageMaker | Excludes Amazon SageMaker AI training plans for training jobs or HyperPod clusters | 
| AWS Secrets Manager | AWSSecretsManager | None | 
| AWS Security Hub | AWSSecurityHub | None | 
| Amazon Simple Notification Service (SNS) | AmazonSNS | None | 
| Amazon Simple Queue Service (SQS) | AWSQueueService | None | 
| AWS Step Functions | AmazonStates | None | 
| AWS Storage Gateway | AWSStorageGateway | None | 
| AWS Systems Manager | AWSSystemsManager | OpsCenter only | 
| Amazon Timestream | AmazonTimestream | None | 
| AWS Transfer Family | AWSTransfer | Excludes AWSDataTransfer | 
| AWS Transit Gateway | AmazonVPC | Includes Transit Gateway VPN, VPC, Peering, DirectConnect, DX; excludes data transfer costs | 
| Amazon VPC Lattice | AmazonVPC | None | 
| Amazon WorkSpaces | AmazonWorkSpaces | Includes WorkSpaces Core; excludes third-party VDI management software license and third-party OS or software license on virtual desktop | 
| Amazon WorkSpaces Core Managed Instances | AmazonWorkSpacesInstances | Excludes hourly metering, third-party VDI management software license, third-party OS or software license on virtual desktop | 

**Note**  
Revenue attribution continues until the tag is removed or the resource is terminated.

**Note**  
Partner Revenue Measurement intends to support all AWS services. We recommend that you instrument PRM on all AWS services and resources that your partner solution interacts with to avoid on-going operational changes as service coverage expands. At this time, revenue attribution data is surfaced for the services listed above. Any partial spend captured on services not listed above is aggregated as "Other".