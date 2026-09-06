

# Tracking your AWS Free Tier usage
<a name="tracking-free-tier-usage"></a>

You can track your AWS Free Tier usage in the following ways:

**Monitoring free account plan information**: You can monitor your free account plan expiration date, credit balance, and days remaining through the AWS Cost and Usage Report widget, AWS Management Console home, or [programmatically](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.html) through the AWS SDK and CLI at no cost. You also receive periodic email alerts regarding your credit balance and when you are approaching the end of your free account plan period.

**Monitoring paid account plan information**: You can monitor your credit balance and expiration date on the credits page in the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing). You can also track your actual usage against short-term trial and always free usage limits using the [free tier API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.html) or on the **Free Tier** page on the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing). This shows when you exceed the free usage limits and will switch to pay-as-you-go pricing each month.

**Note**  
When using billing transfer and signed in as either the management account or a linked account of AWS Organizations transferring its bills (bill source account), you can't track your Free Tier credit applications in your pro forma , AWS Management Console home, or through the AWS SDK and CLI.  
The bill transfer account that manages your billing can track your Free Tier applications through the chargeable , AWS Management Console home, and AWS SDK and CLI.

**Topics**
+ [Using AWS Free Tier usage alerts](#free-budget)
+ [Recommended actions for Free Tier](#free-tier-table)
+ [Trackable AWS Free Tier services](#free-tier-services)

## Using AWS Free Tier usage alerts
<a name="free-budget"></a>

You can use AWS Free Tier usage alerts to track and take action on your cost and usage. For more information about this feature, see [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

AWS Free Tier usage alerts automatically notifies you over email when you exceed 85 percent of your Free Tier limit for each service. For additional tracking, you can configure AWS Budgets to track your usage to 100% of the Free Tier limit by setting a `zero spend budget` using the template. You can also filter your budget to track individual services. 

For example, you can set up a budget to send you an alert when you’re forecasted to exceed 100 percent of the Free Tier limit for Amazon Elastic Block Store. To set up a usage budget, see [Creating a usage budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html#create-usage-budget).

AWS Free Tier usage alerts cover AWS services with an active Free Tier offering in the current month, such as the first 25 GB of Amazon DynamoDB storage or the first 10 custom Amazon CloudWatch metrics.

Your AWS Free Tier offerings depend on your plan type. **Paid plan** accounts might have `Short-term trial` and `Always Free` offerings active. If you go beyond the Free Tier free limit for a service or access paid features, your AWS Free Tier credits automatically apply to cover the eligible cost. After your AWS Free Tier credits expire or are fully used, you're charged at the standard AWS billing rates for usage beyond the free limits. **Free account plan** accounts only have `Always Free` offerings active.

When you exceed the Free Tier limit for a service, AWS sends an email to the email address that you used to create your account (the AWS account root user). To change the email address for AWS Free Tier usage alerts, see the following procedure:<a name="customize-email"></a>

**To change the email address for AWS Free Tier usage alerts**

1. Sign in to the AWS Management Console and open the Billing console at [https://console.aws.amazon.com/billing/](https://console.aws.amazon.com/billing/).

1. Under **Preferences** in the navigation pane, choose ** Billing preferences**.

1. For **Alert preferences**, choose **Edit**.

1. Enter the email address to receive the usage alerts.

1. Choose **Update**.

AWS Budgets usage alerts for 85 percent of the Free Tier limit are automatically activated for all individual AWS accounts, but not for a management account in an AWS Organizations. If you own a management account, you must opt in to get AWS Free Tier usage alerts. Use the following procedure to opt in or out of Free Tier usage alerts.<a name="opt-in-out"></a>

**To opt in or out of AWS Free Tier usage alerts**

1. Sign in to the AWS Management Console and open the Billing console at [https://console.aws.amazon.com/billing/](https://console.aws.amazon.com/billing/).

1. Under **Preferences** in the navigation pane, choose ** Billing preferences**.

1. For **Alert preferences**, choose **Edit**.

1. Select **Receive AWS Free Tier alerts** to opt in to Free Tier usage alerts. To opt out, clear **Receive AWS Free Tier alerts**.

1. Choose **Update**.

## Recommended actions for Free Tier
<a name="free-tier-table"></a>

If you're eligible for AWS Free Tier and you use a free tier offering, you can track your usage with the **Recommended actions** widget on the Billing and Cost Management home page. This widget shows recommendations if your usage exceeded 85% of any service's free tier usage limits. 

The following conditions might limit whether you see AWS Free Tier data:
+ You use an AWS service that doesn't offer Free Tier
+ Your Free Tier has expired
+ You access AWS through an AWS Organizations member account
+ You use an AWS service in the AWS GovCloud (US-West) or AWS GovCloud (US-East) Regions

For more information, see [Recommended actions](view-billing-dashboard.md#recommended-actions-widget).

## Trackable AWS Free Tier services
<a name="free-tier-services"></a>

With AWS, you can track how much you used AWS Free Tier services and what service usage types you used. Usage types are the specific type of usage that AWS tracks. For example, the usage type `BoxUsage:freetier.micro` means that you used an Amazon EC2 micro instance.

The AWS Free Tier usage alerts and the **Top AWS Free Tier Services by Usage** table cover both expiring and non-expiring AWS Free Tier offerings. You can track the following services and usage types.


| Service | Usage type | Free Tier type | 
| --- | --- | --- | 
| AWS Audit Manager | Resource-Assessment-Collected | Short-term trial | 
| AWS Budgets | ActionEnabledBudgetsUsage | Always Free | 
| CloudFormation | Resource-Invocation-Count-FreeTier | Always Free | 
| AWS CodeArtifact | Requests<br />TimedStorage-ByteHrs | Always Free | 
| AWS CodeCommit | User-Month | Always Free | 
| AWS CodePipeline | actionExecutionMinute<br />activePipeline | Always Free | 
| AWS Data Transfer | DataTransfer-Out-Bytes<br />DataTransfer-Regional-Bytes | Always Free | 
| AWS Database Migration Service | InstanceUsg:dms.t2.micro<br />InstanceUsg:dms.t3.micro | Always Free | 
| AWS DeepRacer | ServiceUse-Train-Evaluate-Job<br />TimedStorage-GigabyteHrs | Short-term trial | 
| AWS Directory Service | MicrosoftAD-DC-Usage<br />Small-Directory-Usage | Short-term trial | 
| AWS Elemental MediaConnect | DataTransfer-Out-Bytes | Always Free | 
| AWS Glue | Catalog-Request<br />Catalog-Storage | Always Free | 
| AWS Key Management Service | KMS-Requests | Always Free | 
| AWS Lambda | Lambda-GB-Second<br />Lambda-Streaming-Response-Processed-Bytes<br />Request | Always Free | 
| AWS Migration Hub Refactor Spaces | API-Request<br />EnvironmentHours | Always Free | 
| AWS RoboMaker | SimulationUnitHour | Short-term trial | 
| AWS Security Hub CSPM | OtherProduct:PaidFindingsIngestion<br />RuleEvaluation | Always Free | 
| AWS Service Catalog | SC-API-Calls | Always Free | 
| AWS Step Functions | StateTransition | Always Free | 
| AWS Storage Gateway | Uploaded-Bytes | Always Free | 
| Supply Chain | ADPSiteProductCount<br />SiteProductCount<br />StorageSize | Short-term trial | 
| AWS Systems Manager | AWS-Auto-ScriptDuration-Tier3<br />AWS-Auto-Steps-Tier1<br />IM-Notifications-Tier1 | Always Free | 
| AWS WAF | AMR-BotControl-Request<br />AMR-BotControl-Targeted-Request<br />AMR-FraudControl-Request<br />ShieldProtected-AMR-BotControl-Request<br />ShieldProtected-AMR-BotControl-Targeted-Request<br />ShieldProtected-AMR-FraudControl-Request | Always Free | 
| AWS X-Ray | XRay-TracesAccessed<br />XRay-TracesStored | Always Free | 
| Amazon AppStream | stream-hrs:720p:g2<br />stream.standard.large-ib | Short-term trial | 
| Amazon Braket | Simulators-Task | Short-term trial | 
| Amazon CloudFront | DataTransfer-Out-Bytes<br />Executions-CloudFrontFunctions<br />Invalidations<br />Requests-Tier1 | Always Free | 
| Amazon CloudSearch | (all SearchInstance types) | Short-term trial | 
| Amazon Cognito | CognitoEnterpriseMAU<br />CognitoUserPoolMAU | Always Free | 
| Amazon Cognito Sync | CognitoSyncOperation<br />TimedStorage-ByteHrs | Always Free | 
| Amazon DataZone | DataZoneCompute<br />DataZoneRequests<br />DataZoneStorage<br />DataZoneUsers | Short-term trial | 
| Amazon DevOps Guru | DevOpsGuru-APICalls<br />ResourceGroup-A-usagehours<br />ResourceGroup-B-usagehours | Short-term trial | 
| Amazon DocumentDB (with MongoDB compatibility) | BackupUsage<br />InstanceUsage:db.t3.medium<br />StorageIOUsage<br />StorageUsage | Short-term trial | 
| Amazon DynamoDB | ReadCapacityUnit-Hrs<br />ReplWriteCapacityUnit-Hrs<br />Streams-Requests<br />TimedStorage-ByteHrs<br />WriteCapacityUnit-Hrs | Always Free | 
| Amazon Elastic Container Service | ECS-Anywhere-Instance-hours-WithFree | Short-term trial | 
| Amazon Forecast | DataInjection<br />ForecastDataPoints<br />TrainingHours | Short-term trial | 
| Amazon Fraud Detector | (all FraudPrediction types) | Short-term trial | 
| AWS HealthLake | FHIRDataStorage<br />FHIRQueries | Always Free | 
| Amazon Kendra | KendraDeveloperEdition<br />KendraIntelligentRanking-BaseCapacity | Short-term trial | 
| Amazon Keyspaces (for Apache Cassandra) | ReadRequestUnits<br />TimedStorage-ByteHrs<br />WriteRequestUnits | Short-term trial | 
| Amazon Lightsail | (all BundleUsage types) | Short-term trial | 
| Amazon Location Service | (all types) | Short-term trial | 
| Amazon Lookout for Equipment | Inference-Hours-L4E<br />Ingestion-GB-L4E<br />Training-Hours-L4E | Short-term trial | 
| Amazon Lookout for Metrics | ANOMALY\_DETECTION | Short-term trial | 
| Amazon Lookout for Vision | (all types) | Short-term trial | 
| Amazon Macie | EventsProcessing<br />S3ContentClassification<br />SensitiveDataDiscovery | Short-term trial | 
| Amazon Managed Service for Prometheus | AMP:MetricSampleCount<br />AMP:MetricStorageByteHrs<br />AMP:QuerySamplesProcessed | Always Free | 
| Amazon MemoryDB | DataWritten<br />NodeUsage:db.t4g.small | Short-term trial | 
| Amazon Neptune | BackupUsage<br />DataTransfer-Out-Bytes<br />InstanceUsage:db.t3.medium<br />StorageIOUsage<br />StorageUsage | Short-term trial | 
| AWS HealthOmics | (all types) | Short-term trial | 
| Amazon Personalize | DataIngestion<br />TPS-hours<br />TrainingHour | Short-term trial | 
| Quick | QS-ENT-Alerts-FreeTrial | Short-term trial | 
| Amazon Redshift | Node:dc2.large<br />Node:dw2.large | Short-term trial | 
| Amazon Route 53 | Cidr-Blocks<br />Health-Check-AWS | Always Free | 
| Amazon SageMaker Runtime | (all types) | Short-term trial | 
| Amazon Simple Email Service | Message<br />MessageUnits<br />Recipients-EC2<br />Recipients-MailboxSim-EC2<br />VirtDelivMgr | Always Free | 
| Amazon Simple Notification Service | (all types) | Always Free | 
| Amazon Simple Queue Service | Requests | Always Free | 
| Amazon Simple Workflow Service | AggregateInitiatedActions<br />AggregateInitiatedWorkflows<br />AggregateWorkflowDays | Always Free | 
| Amazon SimpleDB | BoxUsage<br />TimedStorage-ByteHrs | Always Free | 
| Amazon Textract | (all types) | Short-term trial | 
| Amazon Timestream | (all types) | Short-term trial | 
| Amazon WorkSpaces | (all types) | Short-term trial | 
| Amazon CloudWatch | (all types) | Always Free | 
| CloudWatch Events | Event-8K-Chunks<br />ScheduledInvocation | Always Free | 
| CodeBuild | Build-Min:Linux:g1.small<br />Build-Sec:Lambda.1GB | Always Free | 
| CodeCatalyst | (all types) | Always Free | 
| CodeGuru | Profiler-Lambda-Sampling-Hour | Short-term trial | 
| Amazon Comprehend Medical | (all types) | Short-term trial | 