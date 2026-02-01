# Included AWS services

Partner Revenue Measurement supports specific AWS services for revenue attribution tracking through resource tagging.

## Resource Tagging

The following AWS services are supported for resource tagging implementation:

- Amazon API Gateway
- Amazon AppStream (excludes User Fees)
- AWS AppSync
- Amazon Athena
- AWS Backup
- AWS Certificate Manager (includes AWS Certificate Manager Private CA)
- Amazon Cloud Directory
- AWS CloudHSM
- Amazon CloudWatch (Logs only)
- AWS CodeBuild
- AWS CodePipeline
- AWS CodeStar
- Amazon Cognito (excludes Amazon Cognito add-ons)
- Amazon Comprehend
- Amazon Connect (includes Full Connect Unlimited AI and A La Carte; excludes Cases, Entity Resolution, Legacy Pinpoint Engagement, Meetings SDK, ContactLens (Conversational Analytics, Screen Recording, Enterprise Analytics, External Voice: Integration-Connector Months), Chat (ACGR Chat/SMS, WhatsApp, Apple Messages), Email (ACGR Email), Lex (Automated chatbot designer, Streaming Chat-Connect-Standard, Streaming Conversations-Speech-GR), Q in Connect (Agents, Free Trial, Self Service Chat/Voice, Users, Wisdom Contacts), Tasks (ACGR Tasks), Voice (Outbound Campaigns), Customer Profiles (ConnectBaseProfiles, Profiles), Outbound Campaigns Processing (Custom Action, WBM Sent), Telephony (Phone Numbers, EVAT Voice Connectors, External Voice Transfer-ACGR Minutes, OCB))
- AWS Data Pipeline
- AWS Database Migration Service
- AWS DataSync
- AWS Direct Connect (excludes AWS Local Zones)
- AWS Directory Service
- Amazon DynamoDB (excludes DAX)
- Amazon EC2 (includes Amazon EBS, Amazon EBS Snapshots, Amazon EC2 Mac, AWS Local Zones deployment; excludes Capacity Block for ML)
- Amazon ECR
- Amazon EKS (excludes Fargate; includes AWS App Mesh)
- Amazon ECS (includes Fargate and AWS App Mesh)
- AWS Elastic Beanstalk
- Amazon Elastic File System
- Elastic Load Balancing
- Amazon ElastiCache
- Amazon EMR (includes AWS Local Zones deployment)
- Amazon FSx
- Amazon S3 Glacier (excludes Glacier Deep Archive)
- AWS Glue
- AWS Key Management Service (excludes cross-account request costs)
- Amazon Kinesis Data Streams
- Amazon Kinesis Data Analytics
- Amazon Kinesis Data Firehose
- Amazon Kinesis Video Streams
- AWS Lambda
- Amazon MQ
- Amazon MSK
- Amazon Neptune
- AWS Network Firewall
- Amazon OpenSearch Service (includes Amazon Elasticsearch Service; excludes OpenSearch Serverless and OpenSearch Ingestion)
- Amazon Redshift (Amazon Redshift Provisioned and Amazon Redshift Serverless)
- Amazon Relational Database Service (RDS) (includes all RDS engines, Amazon RDS Custom, AWS Local Zones deployment; excludes Db2 licensing fees)
- Amazon Route 53 (excludes Amazon Route 53 Resolver, Traffic Flow, and CIDR block storage)
- Amazon S3 (includes storage cost only and all storage tiers; excludes Requests)
- Amazon SageMaker (excludes Amazon SageMaker training plans for training jobs or HyperPod clusters)
- AWS Secrets Manager
- AWS Security Hub
- Amazon Simple Notification Service (SNS)
- Amazon Simple Queue Service (SQS)
- AWS Step Functions
- AWS Storage Gateway
- AWS Systems Manager (OpsCenter only)
- AWS Transfer Family (excludes AWSDataTransfer)
- AWS Transit Gateway (includes Transit Gateway VPN, VPC, Peering, DirectConnect, DX; excludes data transfer costs)
- Amazon WorkSpaces (includes WorkSpaces Core; excludes third-party VDI management software license and third-party OS or software license on virtual desktop)
- Amazon CloudFront (excludes data transfer costs and Lambda@Edge)
- Amazon Kendra
- Amazon Keyspaces (for Apache Cassandra)
- AWS Mainframe Modernization (excludes 'M2 Custom' and Blu Age Transformation Center costs)
- AWS Elastic Disaster Recovery (DRS)
- AWS Elemental MediaLive
- AWS Elemental MediaPackage
- AWS Elemental MediaConvert
- Amazon DocumentDB (with MongoDB compatibility)
- Amazon Omics
- Amazon Timestream
- Amazon QuickSight (excludes Region fee for Q, SPICE, unused charges on subscription packs, Pro user, Pro author, and administrator)
- AWS Resilience Hub
- Amazon FinSpace (excludes any kdb Insights software license amount)
- Amazon GameLift (excludes GameLift Anywhere, FleetIQ, and FlexMatch when using either EC2 for GameLift or On-premises for GameLift)
- Amazon MemoryDB for Redis (excludes Snapshot Storage)
- AWS HealthImaging
- Amazon VPC Lattice
- Amazon Bedrock (excludes spend from AWS Marketplace Private Offers)
- Amazon Bedrock AgentCore (includes AgentCore RunTime, Browser Tool, Code Interpreter, Gateway, Identity, and Memory)
- AWS Payment Cryptography (excludes following APIs under Requests usage: ListAliases, ListKeys, GetResourcePolicy, GetParametersForImport, GetParametersForExport, DeleteResourcePolicy, DeleteAlias, CreateKey, CreateAlias)
- AWS Cloud WAN (excludes Core Network Edge Hours and data transfer)
- Aurora DSQL
- AWS Deadline Cloud (excludes AWS data transfer charges and Bring-Your-Own-License third-party creative tool software license costs)
- AWS HealthLake (excludes FHIR data export and transformation)
- AWS IoT Core (excludes Registry operations)
- AWS IoT SiteWise (excludes Alarm, Query, Data Storage - Warm Storage, Edge - Data collection pack, Assistant - Monthly Enablement Fee, Assistant - API bundle price, Messaging - Bulk Import, Data Export - Bulk Import)

###### Note

Resources must be tagged with key `aws-apn-id` and value `pc:product-code` format. Revenue attribution continues until the tag is removed or the resource is terminated.
