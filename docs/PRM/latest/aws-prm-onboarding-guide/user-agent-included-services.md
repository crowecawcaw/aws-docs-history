

# Included AWS Services

The following AWS services are supported for User Agent string implementation. User Agent strings must be included in all management or control-plane AWS API/CLI calls (i.e., calls that create, describe, modify, or delete AWS resources) to ensure proper revenue attribution. Identity Tagging supports this same list of AWS services.

For detailed information including specific API actions and regions supported for each service, download the [User Agent String and Identity Tagging Included Services and API Actions (CSV)](samples/user-agent-identity-tagging-included-services.zip).

**Note**  
Monthly API operations on resources are required for attribution to occur.

**Note**  
Only management or control plane operations are supported. Data plane operations using AWS API/CLI are NOT supported.


**User Agent String and Identity Tagging included services**  

| Service Name | Product Service Code | Notes | 
| --- | --- | --- | 
| Amazon API Gateway | AmazonApiGateway | None | 
| Amazon AppStream | AmazonAppStream | Excludes User Fees | 
| Amazon Athena | AmazonAthena | None | 
| Amazon Bedrock | AmazonBedrock | + Partner must use [tagging guide](bedrock-best-practices.md) for instructions on any supported model usage<br />+ Partners must gain access to [supported foundation models](#bedrock-supported-fms-ua) only by using the Amazon Bedrock Console or API<br />+ If using volume-based discounts (such as Provisioned Throughput for [supported foundation models](#bedrock-supported-fms-ua)), these must be purchased only using the Amazon Bedrock Console or API.<br />+ Eligible for inclusion and can be tagged after November 18, 2026<br />+ Excludes spend from AWS Marketplace Private Offers.<br />+ For bedrock-mantle, refer to the [bedrock documentation for tagging](https://docs.aws.amazon.com/bedrock/latest/userguide/cost-management.html). For bedrock-runtime, refer to the [Amazon Bedrock AWS Revenue Measurement best practices](bedrock-best-practices.md)<br />+ For Amazon Bedrock, attributed revenue reflects the total Amazon Bedrock charges as billed by AWS, including usage of closed-source models. | 
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

**Note**  
AWS Revenue Measurement intends to support all AWS services. We recommend that you instrument AWS Revenue Measurement on all AWS services and resources that your partner solution interacts with to avoid ongoing operational changes as service coverage expands. At this time, revenue attribution data is surfaced for the services listed below. Any partial spend captured on services not listed below is aggregated as "Misc".

## Amazon Bedrock supported foundation models
<a name="bedrock-supported-fms-ua"></a>

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