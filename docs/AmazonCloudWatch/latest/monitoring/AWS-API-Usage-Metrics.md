# AWS API usage metrics

Most APIs that support AWS CloudTrail logging also report usage metrics to CloudWatch. API usage
metrics in CloudWatch allow you to proactively manage API usage by visualizing
metrics in the CloudWatch console, creating custom dashboards, detecting changes in activity with
CloudWatch outlier detection, and configuring alarms that alert when usage approaches a threshold.

You can use the he following table to learn about services that report API usage metrics to CloudWatch.
The table lists the values to use for the `Service` dimension, so you can see the usage metrics from that service.
You can use the procedure in this section to view the list of a service's APIs that report usage metrics to CloudWatch.

| Service                                            | Value for the `Service` dimension   |
| -------------------------------------------------- | ----------------------------------- |
| AWS Identity and Access Management Access Analyzer | `Access Analyzer`                   |
| AWS Account Management                             | `Account Management`                |
| Alexa for Business                                 | `A4B`                               |
| Amazon API Gateway                                 | `API Gateway`                       |
| AWS App Mesh                                       | `App Mesh`                          |
| AWS AppConfig                                      | `AWS AppConfig`                     |
| Amazon AppFlow                                     | `AppFlow`                           |
| Application Auto Scaling                           | `Application Auto Scaling`          |
| Application Discovery Service                      | `Application Discovery Service`     |
| Amazon AppStream                                   | `AppStream`                         |
| WorkSpaces Applications Image Builder              | `Image Builder`                     |
| Amazon Athena                                      | `Athena`                            |
| AWS Audit Manager                                  | `Audit Manager`                     |
| AWS Backup                                         | `Backup`                            |
| AWS Batch                                          | `Batch`                             |
| Amazon Braket                                      | `Braket`                            |
| AWS Budgets                                        | `Budgets`                           |
| AWS Certificate Manager                            | `Certificate Manager`               |
| Amazon Chime SDK                                   | `ChimeSDK`                          |
| Amazon Cloud Directory                             | `Cloud Directory`                   |
| AWS Cloud Map                                      | `Cloud Map`                         |
| AWS CloudFormation                                 | `CloudFormation`                    |
| AWS CloudHSM                                       | `CloudHSM`                          |
| Amazon CloudSearch                                 | `CloudSearch`                       |
| AWS CloudShell                                     | `CloudShell`                        |
| AWS CloudTrail                                     | `CloudTrail`                        |
| Amazon CloudWatch                                  | `CloudWatch`                        |
| Amazon CloudWatch Application Signals              | `CloudWatch Application Signals`    |
| Amazon CloudWatch Logs                             | `Logs`                              |
| Amazon CloudWatch Application Insights             | `CloudWatch Application Insights`   |
| AWS CodeBuild                                      | `CodeBuild`                         |
| AWS CodeCommit                                     | `CodeCommit`                        |
| Amazon CodeGuru Profiler                           | `CodeGuru Profiler`                 |
| AWS CodePipeline                                   | `CodePipeline`                      |
| AWS CodeStar                                       | `CodeStar`                          |
| AWS CodeStar Notifications                         | `CodeStar Notifications`            |
| AWS CodeStar Connections                           | `CodeStar Connections`              |
| Amazon Cognito Identity pools                      | `Cognito Identity Pools`            |
| Amazon Cognito Sync                                | `Cognito Sync`                      |
| Amazon Comprehend                                  | `Comprehend`                        |
| Amazon Comprehend Medical                          | `Comprehend Medical`                |
| AWS Compute Optimizer                              | `ComputeOptimzier`                  |
| Amazon Connect                                     | `Connect`                           |
| Amazon Connect Customer Profiles                   | `Customer Profiles`                 |
| AWS Cost and Usage Reports                         | `Cost and Usage Report`             |
| AWS Cost Explorer                                  | `Cost Explorer`                     |
| AWS Data Exchange                                  | `Data Exchange`                     |
| AWS Data Lifecycle Manager                         | `Data Lifecycle Manager`            |
| AWS Database Migration Service                     | `Database Migration Service`        |
| AWS DataSync                                       | `DataSync`                          |
| AWS DeepLens                                       | `AWS DeepLens`                      |
| Amazon Detective                                   | `Detective`                         |
| Device Advisor                                     | `Device Advisor`                    |
| AWS Direct Connect                                 | `Direct Connect`                    |
| AWS Directory Service                              | `Directory Service`                 |
| DynamoDB Accelerator                               | `DynamoDBAccelerator`               |
| Amazon EC2                                         | `EC2`                               |
| EC2 Auto Scaling                                   | `EC2 Auto Scaling`                  |
| Amazon Elastic Container Registry                  | `ECR Public`                        |
| Amazon Elastic Container Service                   | `ECS`                               |
| Amazon Elastic File System                         | `EFS`                               |
| Amazon Elastic Kubernetes Service                  | `EKS`                               |
| AWS Elastic Beanstalk                              | `Elastic Beanstalk`                 |
| Amazon Elastic Inference                           | `Elastic Inference`                 |
| Elastic Load Balancing                             | `Elastic Load Balancing`            |
| Amazon EMR                                         | `EMR Containers`                    |
| AWS Firewall Manager                               | `Firewall Manager`                  |
| Amazon FSx                                         | `FSx`                               |
| Amazon GameLift Servers                            | `GameLift`                          |
| AWS Glue DataBrew                                  | `DataBrew`                          |
| Amazon Managed Grafana                             | `Grafana`                           |
| AWS IoT Greengrass                                 | `Greengrass`                        |
| AWS Ground Station                                 | `Ground Station`                    |
| AWS Health APIs And Notifications                  | `AWS Health APIs And Notifications` |
| Amazon Interactive Video Service                   | `IVS`                               |
| AWS IoT Core                                       | `IoT`                               |
| AWS IoT Events                                     | `IoT Events`                        |
| AWS IoT RoboRunner                                 | `IoT RoboRunner`                    |
| AWS IoT SiteWise                                   | `IoT Sitewise`                      |
| AWS IoT Wireless                                   | `IoT Wireless`                      |
| Amazon Kendra                                      | `Kendra`                            |
| Amazon Keyspaces (for Apache Cassandra)            | `Keyspaces`                         |
| Amazon Managed Service for Apache Flink            | `Kinesis Analytics`                 |
| Amazon Data Firehose                               | `Firehose`                          |
| Kinesis Video Streams                              | `Kinesis Video Streams`             |
| AWS Key Management Service                         | `KMS`                               |
| AWS Lambda                                         | `Lambda`                            |
| AWS Launch Wizard                                  | `Launch Wizard`                     |
| Amazon Lex                                         | `Amazon Lex`                        |
| Amazon Lightsail                                   | `Lightsail`                         |
| Amazon Location Service                            | `Location`                          |
| Amazon Lookout for Vision                          | `Lookout for Vision`                |
| Amazon Machine Learning                            | `Amazon Machine Learning`           |
| Amazon Macie                                       | `Macie`                             |
| Amazon Managed Blockchain (AMB) Query              | `Amazon Managed Blockchain Query`   |
| AWS Managed Services                               | `AWS Managed Services`              |
| AWS Marketplace Commerce Analytics                 | `Marketplace Analytics Service`     |
| AWS Elemental MediaConnect                         | `MediaConnect`                      |
| AWS Elemental MediaConvert                         | `MediaConvert`                      |
| AWS Elemental MediaLive                            | `MediaLive`                         |
| AWS Elemental MediaStore                           | `Mediastore`                        |
| AWS Elemental MediaTailor                          | `MediaTailor`                       |
| AWS Mobile Hub                                     | `Mobile Hub`                        |
| AWS Network Firewall                               | `Network Firewall`                  |
| OpsWorks                                           | `OpsWorks`                          |
| OpsWorks for Configuration Management              | `OPsWorks CM`                       |
| AWS Outposts                                       | `Outposts`                          |
| AWS Organizations                                  | `Organizations`                     |
| Amazon RDS Performance Insights                    | `Performance Insights`              |
| Amazon Pinpoint                                    | `Pinpoint`                          |
| AWS Private Certificate Authority                  | `Private Certificate Authority`     |
| Amazon Managed Service for Prometheus              | `Prometheus`                        |
| AWS Proton                                         | `Proton`                            |
| Amazon Quantum Ledger Database (Amazon QLDB)       | `QLDB`                              |
| Amazon RDS                                         | `RDS`                               |
| Amazon Redshift                                    | `Redshift Data API`                 |
| Amazon Rekognition                                 | `Rekognition`                       |
| AWS Resource Access Manager                        | `Resource Access Manager`           |
| AWS Resource Groups                                | `Resource Groups`                   |
| AWS Resource Groups Tagging API                    | `Resource Groups Tagging API`       |
| Amazon Route 53 Domains                            | `Route 53 Domains`                  |
| Amazon Route 53 Resolver                           | `Route 53 Resolver`                 |
| Amazon S3                                          | `S3`                                |
| Amazon Glacier                                     | `Amazon S3 Glacier`                 |
| Amazon SageMaker Runtime                           | `Sagemaker`                         |
| Savings Plans                                      | `Savings Plans`                     |
| AWS Secrets Manager                                | `Secrets Manager`                   |
| AWS Security Hub                                   | `Security Hub`                      |
| AWS Server Migration Service                       | `AWS Server Migration Service`      |
| AWS Service Catalog AppRegistry                    | `Service Catalog AppRegistry`       |
| Service Quotas                                     | `Service Quotas`                    |
| AWS Shield                                         | `Shield`                            |
| AWS Signer                                         | `Signer`                            |
| Amazon Simple Notification Service                 | `SNS`                               |
| Amazon Simple Email Service                        | `SES`                               |
| Amazon Simple Queue Service                        | `SQS`                               |
| Identity Store                                     | `Identity Store`                    |
| Storage Gateway                                    | `Storage Gateway`                   |
| AWS Support                                        | `Support`                           |
| Amazon Simple Workflow Service                     | `SWF`                               |
| Amazon Textract                                    | `Textract`                          |
| AWS IoT Things Graph                               | `ThingsGraph`                       |
| Amazon Timestream                                  | `Timestream`                        |
| Amazon Transcribe                                  | `Transcribe`                        |
| Amazon Translate                                   | `Translate`                         |
| Amazon Transcribe streaming transcription          | `Transcribe Streaming`              |
| AWS Transfer Family                                | `Transfer`                          |
| AWS WAF                                            | `WAF`                               |
| Amazon WorkLink                                    | `WorkLink`                          |
| Amazon WorkMail                                    | `Amazon WorkMail`                   |
| Amazon WorkSpaces                                  | `Workspaces`                        |
| AWS X-Ray                                          | `X-Ray`                             |

Some services report usage metrics for additional APIs as well. To see whether an API
reports usage metrics to CloudWatch, use the CloudWatch console to see the metrics reported by that
service in the `AWS/Usage` namespace.

###### To see the list of a service's APIs that report usage metrics to CloudWatch

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. On the **All metrics** tab, choose **Usage**, and
   then choose **By AWS Resource**.
4. In the search box near the list of metrics, enter the name of the service. The metrics are
   filtered by the service you entered.
