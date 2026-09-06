# Included AWS Services

The following AWS services are supported for User Agent string implementation. User Agent strings must be included in all management or control-plane AWS API/CLI calls (i.e., calls that create, describe, modify, or delete AWS resources) to ensure proper revenue attribution.

For detailed information including specific API actions and regions supported for each service, download the [User Agent Included Services and API Actions (CSV)](samples/user-agent-included-services.zip.md "samples/user-agent-included-services.zip.md").

###### Note

Monthly API operations on resources are required for attribution to occur.

###### Note

Only management or control plane operations are supported. Data plane operations using AWS API/CLI are NOT supported.

###### Note

Partner Revenue Measurement intends to support all AWS services. We recommend that you instrument PRM on all AWS services and resources that your partner solution interacts with to avoid ongoing operational changes as service coverage expands. At this time, revenue attribution data is surfaced for the services listed below. Any partial spend captured on services not listed below is aggregated as "Misc".

User Agent String Included Services| Service Name | Product Service Code | Notes |
| --- | --- | --- |
| Amazon API Gateway | AmazonApiGateway | None |
| Amazon AppStream | AmazonAppStream | Excludes User Fees |
| Amazon Athena | AmazonAthena | None |
| Amazon Bedrock | AmazonBedrock | Includes only Amazon models and Open Source models available in Amazon Bedrock |
| Amazon Bedrock AgentCore | AmazonBedrockAgentCore | Includes AgentCore RunTime, Browser Tool, Code Interpreter, Gateway, Identity, and Memory |
| Amazon Bedrock Service | AmazonBedrockService | None |
| Amazon Chime | AmazonChime | None |
| Amazon Chime | AmazonChimeFeatures | None |
| Amazon Chime | AmazonChimeServices | None |
| Amazon Chime | AmazonChimeVoiceConnector | None |
| Amazon CloudFront | AmazonCloudFront | Excludes data transfer costs and Lambda@Edge |
| Amazon CloudSearch | AmazonCloudSearch | None |
| Amazon CloudWatch | AmazonCloudWatch | Alarms and Logs |
| Amazon CodeWhisperer | AmazonCodeWhisperer | None |
| Amazon Cognito | AmazonCognito | Excludes Amazon Cognito add-ons |
| Amazon Connect | AmazonConnect | Includes Full Connect Unlimited AI and A La Carte; excludes Cases, Entity Resolution, Legacy Pinpoint Engagement, Meetings SDK, ContactLens, Chat, Email, Lex, Q in Connect, Tasks, Voice, Customer Profiles, Outbound Campaigns Processing, Telephony |
| Amazon Connect | ContactCenterTelecomm | None |
| Amazon Connect | ContactCenterTelecommKR | None |
| Amazon Connect | ContactCenterTelecommZA | None |
| Amazon Connect Customer Profiles | CustomerProfiles | None |
| Amazon Detective | AmazonDetective | None |
| Amazon DocumentDB (with MongoDB compatibility) | AmazonDocDB | None |
| Amazon DynamoDB | AmazonDynamoDB | None |
| Amazon DynamoDB Accelerator (DAX) | AmazonDAX | None |
| Amazon EC2 | AmazonEC2 | Includes Amazon EBS, EBS Snapshots, EC2 Mac, AWS Local Zones deployment, Savings Plan for ML instance types; excludes Capacity Block for ML |
| Amazon EC2 | AmazonEC2OCPULicenseFees | None |
| Amazon ECR | AmazonECR | None |
| Amazon ECR Public | AmazonECRPublic | None |
| Amazon ECS | AmazonECS | Includes Fargate and AWS App Mesh |
| Amazon EKS | AmazonEKS | Excludes Fargate; includes AWS App Mesh |
| Amazon Elastic File System | AmazonEFS | None |
| Amazon ElastiCache | AmazonElastiCache | None |
| Amazon EMR | ElasticMapReduce | Includes AWS Local Zones deployment |
| Amazon FSx | AmazonFSx | None |
| Amazon GameLift Streams | AmazonGameLiftStreams | None |
| Amazon Grafana | AmazonGrafana | None |
| Amazon Interactive Video Service | AmazonIVS | None |
| Amazon Kendra | AmazonKendra | None |
| Amazon Keyspaces (for Apache Cassandra) | AmazonMCS | None |
| Amazon Kinesis Data Analytics | AmazonKinesisAnalytics | None |
| Amazon Kinesis Data Firehose | AmazonKinesisFirehose | None |
| Amazon Kinesis Data Streams | AmazonKinesis | Data Streams and Data Firehose |
| Amazon Kinesis Video Streams | AmazonKinesisVideo | None |
| Amazon Lex | AmazonLex | None |
| Amazon Managed Service for Prometheus | AmazonPrometheus | None |
| Amazon Managed Workflows for Apache Airflow (MWAA) | AmazonMWAA | None |
| Amazon MemoryDB for Redis | AmazonMemoryDB | Excludes Snapshot Storage |
| Amazon MQ | AmazonMQ | None |
| Amazon MSK | AmazonMSK | None |
| Amazon Neptune | AmazonNeptune | None |
| Amazon Omics | AmazonOmics | Excludes storage charges |
| Amazon OpenSearch Service | AmazonES | Includes Amazon Elasticsearch Service; excludes OpenSearch Serverless and OpenSearch Ingestion |
| Amazon Personalize | AmazonPersonalize | None |
| Amazon Q | AmazonQ | None |
| Amazon RDS OCPU License Fees | AmazonRDSOCPULicenseFees | None |
| Amazon Redshift | AmazonRedshift | Amazon Redshift Provisioned and Amazon Redshift Serverless |
| Amazon Relational Database Service (RDS) | AmazonRDS | Includes all RDS engines, Amazon RDS Custom, AWS Local Zones deployment; excludes Db2 licensing fees |
| Amazon Route 53 | AmazonRoute53 | Excludes Amazon Route 53 Resolver, Traffic Flow, and CIDR block storage |
| Amazon S3 | AmazonS3 | Includes storage cost only and all storage tiers; excludes Requests |
| Amazon S3 Glacier | AmazonGlacier | Excludes Glacier Deep Archive |
| Amazon Security Lake | AmazonSecurityLake | None |
| Amazon SES | AmazonSES | Excludes managed infrastructure hours |
| Amazon Simple Notification Service (SNS) | AmazonSNS | Excludes API request charges |
| Amazon Simple Queue Service (SQS) | AWSQueueService | Excludes API request charges |
| Amazon Timestream | AmazonTimestream | Excludes monitoring and analysis charges |
| Amazon Verified Permissions | AmazonVerifiedPermissions | None |
| Amazon WorkSpaces | AmazonWorkSpaces | Includes WorkSpaces Core; excludes third-party VDI management software license and third-party OS or software license on virtual desktop |
| Amazon WorkSpaces Secure Browser | AmazonWorkSpacesWeb | None |
| AWS Amplify | AWSAmplify | None |
| AWS App Fabric | AWSAppFabric | None |
| AWS App Runner | AWSAppRunner | None |
| AWS Application Migration Service | AWSApplicationMigrationSvc | None |
| AWS AppSync | AWSAppSync | None |
| AWS B2B Data Interchange | AWSB2Bi | None |
| AWS Backup | AWSBackup | None |
| AWS Billing Conductor | AWSBillingConductor | None |
| AWS Certificate Manager | ACM | None |
| AWS Certificate Manager | AWSCertificateManager | Includes AWS Certificate Manager Private CA |
| AWS CloudFormation | AWSCloudFormation | None |
| AWS CodeArtifact | AWSCodeArtifact | Excludes API request charges |
| AWS CodeBuild | CodeBuild | None |
| AWS CodePipeline | AWSCodePipeline | None |
| AWS Compute Optimizer | AWSComputeOptimizer | None |
| AWS Database Migration Service | AWSDatabaseMigrationSvc | None |
| AWS DataSync | AWSDataSync | None |
| AWS DevOps Agent Service | DevOpsAgent | None |
| AWS Direct Connect | AWSDirectConnect | Excludes AWS Local Zones |
| AWS Directory Service | AWSDirectoryService | None |
| AWS Elastic Disaster Recovery (DRS) | AWSElasticDisasterRecovery | None |
| AWS Elemental Inference | AWSElementalInference | None |
| AWS Elemental MediaConvert | AWSElementalMediaConvert | None |
| AWS Elemental MediaPackage | AWSElementalMediaPackage | None |
| AWS Elemental MediaStore | AWSElementalMediaStore | None |
| AWS Elemental MediaTailor | AWSElementalMediaTailor | None |
| AWS End User Messaging | AmazonPinpoint | Excludes Carrier Fees, Carrier Fee Count, Number Information (Carrier Lookup), Numbers Validated, Phone numbers, SMS Inbound Price |
| AWS Firewall Manager | AWSFMS | None |
| AWS Global Accelerator | AWSGlobalAccelerator | None |
| AWS Glue | AWSGlue | None |
| AWS HealthLake | AmazonHealthLake | Excludes FHIR data export and transformation |
| AWS Interconnect | AWSInterconnect | None |
| AWS IoT Core | AWSIoT | Excludes Registry operations |
| AWS IoT Device Management | IoTDeviceManagement | None |
| AWS IoT Greengrass | AWSGreengrass | None |
| AWS Key Management Service | awskms | Excludes cross-account request costs |
| AWS Lambda | AWSLambda | None |
| AWS Network Firewall | AWSNetworkFirewall | None |
| AWS Outposts | AWSOutposts | None |
| AWS Payment Cryptography | PaymentCryptography | Excludes following APIs under Requests usage: ListAliases, ListKeys, GetResourcePolicy, GetParametersForImport, GetParametersForExport, DeleteResourcePolicy, DeleteAlias, CreateKey, CreateAlias |
| AWS R53 App Recovery Controller | AWSR53AppRecoveryController | None |
| AWS Resilience Hub | AWSResilienceHub | None |
| AWS Secrets Manager | AWSSecretsManager | Excludes API request charges |
| AWS Security Agent | SecAgent | None |
| AWS Step Functions | AmazonStates | None |
| AWS Storage Gateway | AWSStorageGateway | None |
| AWS Transfer Family | AWSTransfer | Excludes AWSDataTransfer |
| AWS Transit Gateway | AmazonVPC | Includes Transit Gateway VPN, VPC, Peering, DirectConnect, DX; excludes data transfer costs |
| AWS WAF | awswaf | None |
| AWS Wisdom | AWSWisdom | None |
| Elastic Load Balancing | AWSELB | None |
