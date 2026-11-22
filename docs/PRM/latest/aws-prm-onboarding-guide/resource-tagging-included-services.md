

# Included AWS Services

The following AWS services are supported for resource tagging implementation. Resources must be tagged with key `aws-apn-id-{{partner-central-aws-account-id}}` and value `pc:{{product-code}}` format. For how to construct your tag key, see [Constructing Your Tag Key and Value](manual-tagging.md#tag-key-construction). Account Tagging for SaaS products supports this same list of AWS services.

For a downloadable version of this list, download the [Resource Tagging and Account Tagging for SaaS products Included Services (CSV)](samples/resource-tagging-account-tagging-included-services.zip).


**Resource Tagging and Account Tagging for SaaS products included services**  

| Service Name | Product Service Code | Notes | 
| --- | --- | --- | 
| Amazon API Gateway | AmazonApiGateway | None | 
| Amazon AppStream | AmazonAppStream | Excludes User Fees | 
| AWS AppSync | AWSAppSync | None | 
| Amazon Athena | AmazonAthena | None | 
| Aurora DSQL | AuroraDSQL | None | 
| AWS Backup | AWSBackup | None | 
| Amazon Bedrock | AmazonBedrock | + Partner must use [tagging guide](bedrock-best-practices.md) for instructions on any supported model usage<br />+ Partners must gain access to [supported foundation models](#bedrock-supported-fms-rt) only by using the Amazon Bedrock Console or API<br />+ If using volume-based discounts (such as Provisioned Throughput for [supported foundation models](#bedrock-supported-fms-rt)), these must be purchased only using the Amazon Bedrock Console or API.<br />+ Eligible for inclusion and can be tagged after November 18, 2026<br />+ Excludes spend from AWS Marketplace Private Offers.<br />+ For bedrock-mantle, refer to the [bedrock documentation for tagging](https://docs.aws.amazon.com/bedrock/latest/userguide/cost-management.html). For bedrock-runtime, refer to the [Amazon Bedrock AWS Revenue Measurement best practices](bedrock-best-practices.md)<br />+ For Amazon Bedrock, attributed revenue reflects the total Amazon Bedrock charges as billed by AWS, including usage of closed-source models. | 
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
| Amazon Connect Decisions | AWSSupplyChain | Includes Demand Teammate and Supply Teammate. Revenue attribution available from September 1, 2026 | 
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
| Amazon GameLift Streams | AmazonGameLiftStreams | Excludes Game Data Storage Hours operation. Revenue attribution available from September 1, 2026 | 
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
| AWS RTB Fabric | AWSRTBFabric | Revenue attribution available from September 1, 2026 | 
| Amazon Route 53 | AmazonRoute53 | Excludes Amazon Route 53 Resolver, Traffic Flow, and CIDR block storage | 
| Amazon S3 | AmazonS3 | Includes storage cost only and all storage tiers; excludes Requests | 
| Amazon S3 Glacier | AmazonGlacier | Excludes Glacier Deep Archive | 
| Amazon SageMaker AI | AmazonSageMaker | Excludes Amazon SageMaker AI training plans for training jobs or HyperPod clusters | 
| AWS Secrets Manager | AWSSecretsManager | None | 
| AWS Security Hub | AWSSecurityHub | None | 
| Amazon Simple Email Service (SES) | AmazonSES | Excludes Dedicated IPs (managed) subscription, Insight Count for Recipients-Validation, Queries for Virtual Deliverability Manager, Incoming mail chunk and message received, Virtual Deliverability Manager (IP, Domain, InboxTest and Subscription). Revenue attribution available from September 1, 2026 | 
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
AWS Revenue Measurement intends to support all AWS services. We recommend that you instrument AWS Revenue Measurement on all AWS services and resources that your partner solution interacts with to avoid on-going operational changes as service coverage expands. At this time, revenue attribution data is surfaced for the services listed above. Any partial spend captured on services not listed above is aggregated as "Other".

## Amazon Bedrock supported foundation models
<a name="bedrock-supported-fms-rt"></a>

Model Provider: Amazon is supported. This includes Titan, and Amazon Nova models. Refer to the below table for supported foundation models (FMs) from other providers. For additional information on Amazon provided FMs, and other providers FMs, please refer to the [documentation page](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html).


| Model Name | Product Service Code | 
| --- | --- | 
| Claude - 100K tokens | 6g6ab1sru7eirvh6e7oq9d0qm | 
| Claude 12k | 5jm1opkmaj61url2p3po87d3b2 | 
| Claude 3 Sonnet | 7cloiv1lqe76eogr33nhp9r5k8 | 
| Claude 3.5 Haiku (Amazon Bedrock Edition) | mrranvtjv73frdrt492b07oio | 
| Claude 3.5 Sonnet | 4a524th30q694o538qndh9ucht | 
| Claude 3.5 Sonnet v2 (Amazon Bedrock Edition) | 5jl6d7hjcj7sd8pjt4cag3ttm0 | 
| Claude 3.7 Sonnet (Amazon Bedrock Edition) | 78rs41v08o682aebuab075t6n3 | 
| Claude Fable 5 | 3w8nci3qjojn50a04q9rrj2v1 | 
| Claude Fable 5.1 | 8x9un3wsd4o66772c4uio7m7l | 
| Claude Instant - 100K tokens | 2h6g04a0oc66maqka32cj9d049 | 
| Claude Instant - 12K tokens | 3ghtt72ra669kqboojpglmmh9g | 
| Claude 3 Haiku | 4s10koflct6dqpec6l9i37drsi | 
| Claude Haiku 4.5 | 7g37zhparap7eesm9k78jrzqc | 
| Claude Haiku 5.5 | es2xizaw5qhz61wmmxpomghdr | 
| Claude 3 Opus | 7t92q43968640bcrgt21cr6gbd | 
| Claude Opus 4 | 23otb4rdau62rpd0j3jiod095n | 
| Claude Opus 4.1 | bijmvsacydcvlmkfn4aoais9l | 
| Claude Opus 4.5 | 16kx7bv84avo7kphvohp3qiqt | 
| Claude Opus 4.6 | 3jkxki7g66gt6v02m7pqlqyyx | 
| Claude Opus 4.7 | 5gx3s48zyaequjfyy22fed1k0 | 
| Claude Opus 4.8 | 79jgs622sa6y5xas7zz923iaa | 
| Claude Opus 5 | 4ztzvfpgbx6ibqbfqh4pje7rd | 
| Claude Opus 5.5 | 6aej7ikcc3vxof4z1r46vw5a5 | 
| Claude Sonnet 4 | 17khu2002f6qgpo5v4c48l86p7 | 
| Claude Sonnet 4.1 | 9svps415mdwhhoxlp2tx3hald | 
| Claude Sonnet 4.5 | 9svps415mdwhhoxlp2tx3hald | 
| Claude Sonnet 4.6 | 7zgyu5r4uonlsrnaq20qq63eo | 
| Claude Sonnet 5 | 35bl0uzthq3u3dp0hocpb4n84 | 
| Claude Sonnet 5.5 | 4o3pwao2mchrff65jsl6s5oek | 
| Cohere - Command | 5tea8etmii7n8psresm4sphmmd | 
| Cohere - Command Light | 2klpp849cp7hu80e2id56dv3fm | 
| Cohere - Command R | 5s4alasn2363hanqn0bnj1cebd | 
| Cohere - Command R\+ | 3e74mlahrt6sbanvu7b5lt7f2f | 
| Cohere - Embed (english) | 2mln3pdg1n6ve9f3enhr6sk6b7 | 
| Cohere - Embed (multi-lingual) | 1bdfsn34iq7cpomvps1ds1s5ka | 
| DeepSeek (all models) | AmazonBedrock | 
| Embed v4 | 5tcg3vnqgmtc9v94qeud503qm | 
| Google (all oss models incl. Gemma) | AmazonBedrock | 
| Jamba 1.5 Large | 4q7vjg00b86khqbnmohodshjvh | 
| Jamba 1.5 Mini | v6cb8lh156aca7tmbeaqqoanl | 
| Jamba-Instruct | 713ahoolel7riqnkg3obffgubl | 
| Jurassic-2 Mid | 24bngp5r3b64lqgd8j5t6h1bd4 | 
| Jurassic-2 Ultra | 3ati5r8njj7nhrav2m9vcp4f0a | 
| Marengo Embed 2.7 | 3u017gmzbyn77kcc2bifhcs9u | 
| Marengo Embed 3.0 | emw7xgkdbf5zgzmulswgnc0mh | 
| Meta - Llama 2 13B chat | 4hh74csn487di98lf2n14hk256 | 
| Meta - Llama 2 70B chat | 1rba0m3nhm62aoaht9sequkg30 | 
| Meta - Llama 3 70B | AmazonBedrock | 
| Meta - Llama 3 8B | AmazonBedrock | 
| Meta - Llama 3.1 405B | AmazonBedrock | 
| Meta - Llama 3.1 70B | AmazonBedrock | 
| Meta - Llama 3.1 8B | AmazonBedrock | 
| Meta - Llama 3.2 11B Instruct | AmazonBedrock | 
| Meta - Llama 3.2 1B Instruct | AmazonBedrock | 
| Meta - Llama 3.2 3B Instruct | AmazonBedrock | 
| Meta - Llama 3.2 90B Instruct | AmazonBedrock | 
| Mistral (all models) | AmazonBedrock | 
| Mistral Large | AmazonBedrock | 
| Mistral Small | AmazonBedrock | 
| MiniMax (all models) | AmazonBedrock | 
| Moonshot AI (all models) | AmazonBedrock | 
| OpenAI (GPT-oss models only) | AmazonBedrock | 
| OpenAI GPT-5.4 | ceu1zqh289h0ctix7gbuul1o8 | 
| OpenAI GPT-5.5 | clbsr9o5hndkxz31zhdt808pe | 
| OpenAI GPT-5.6 Luna | chdqhsysykikm0lktr3is86jp | 
| OpenAI GPT-5.6 Sol | a9v3r8uw6qlknisvjgirvg2vw | 
| OpenAI GPT-5.6 Terra | 3r4g9jolgvqrs4xhjcazm3x0c | 
| OpenAI GPT-6 Astra | 6v7nofkna9y2bu4jf7m1u6jf6 | 
| OpenAI GPT-6 Luna | cbiwnvepyat1c5r4ebi61fb5a | 
| OpenAI GPT-6 Sol | 7hio9qiydiuhvan7f0z9qbghq | 
| OpenAI GPT-6.1 Sol | rmyu792p9dmjyg3l0f5xgx5a | 
| OpenAI GPT-6.1 Terra | 3szp4gw1qfswtqxmuxpx5nhux | 
| Pegasus 1.2 | 1loi2q7onlg7ghwkrcbd3gqp | 
| Palmyra X4 | 5rta26t9sd7h6rggf5d4gqjvbl | 
| Palmyra X5 | 7581bo10ok740bqmal1uhamp25 | 
| Qwen (all models) | AmazonBedrock | 
| Stability | 2vsi6e3d2j6tjqo73msdslnuus | 
| Stability - SDXL 1.0 (PT Only) | 374tv6kr397rkbt173gl2buu8p | 
| Stable Image Core (Amazon Bedrock Edition) | 65tbrqi5786lkon1p4cuo8esqu | 
| Stable Image Ultra (Amazon Bedrock Edition) | 9c1qlsn4v6s2arj6d3b6dhvd5 | 
| xAI - Grok 4.3 | AmazonBedrock | 
| xAI - Grok 4.6 | AmazonBedrock | 
| xAI - Grok 4.7 | AmazonBedrock | 
| Z.AI (all models) | AmazonBedrock | 