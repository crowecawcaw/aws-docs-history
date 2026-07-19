# Tracking your AWS Free Tier usage

You can track your AWS Free Tier usage in the following ways:

**Monitoring free account plan information**: You
can monitor your free account plan expiration date, credit balance, and days
remaining through the AWS Cost and Usage Report widget, AWS Management Console home, or [programmatically](../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md") through the AWS SDK and CLI at no cost. You also
receive periodic email alerts regarding your credit balance and when you are
approaching the end of your free account plan period.

**Monitoring paid account plan information**: You
can monitor your credit balance and expiration date on the credits page in the
[AWS Billing and Cost Management console](https://console.aws.amazon.com/billing "https://console.aws.amazon.com/billing"). You can also
track your actual usage against short-term trial and always free usage limits
using the [free tier API](../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md") or on the **Free Tier** page on the
[AWS Billing and Cost Management console](https://console.aws.amazon.com/billing "https://console.aws.amazon.com/billing"). This shows
when you exceed the free usage limits and will switch to pay-as-you-go pricing
each month.

###### Note

When using billing transfer and signed in as either the management account or a linked account of AWS Organizations transferring its bills (bill source account), you can't track your Free Tier credit applications in your pro forma , AWS Management Console home, or through the AWS SDK and CLI.

The bill transfer account that manages your billing can track your Free Tier applications through the chargeable , AWS Management Console home, and AWS SDK and CLI.

###### Topics

- [Using AWS Free Tier usage alerts](#free-budget "#free-budget")
- [Recommended actions for Free Tier](#free-tier-table "#free-tier-table")
- [Trackable AWS Free Tier services](#free-tier-services "#free-tier-services")

## Using AWS Free Tier usage alerts

You can use AWS Free Tier usage alerts to track and take action on your cost and
usage. For more information about this feature, see [Managing your
costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md").

AWS Free Tier usage alerts automatically notifies you over email when you exceed 85
percent of your Free Tier limit for each service. For additional tracking, you can
configure AWS Budgets to track your usage to 100% of the Free Tier limit by
setting a `zero spend budget` using the template. You can also filter
your budget to track individual services.

For example, you can set up a budget to send you an alert when you’re forecasted
to exceed 100 percent of the Free Tier limit for Amazon Elastic Block Store. To set up a usage
budget, see [Creating a usage budget](../../../cost-management/latest/userguide/budgets-create.md#create-usage-budget "../../../cost-management/latest/userguide/budgets-create.md#create-usage-budget").

AWS Free Tier usage alerts cover AWS services with an active Free Tier offering in the current month,
such as the first 25 GB of Amazon DynamoDB storage or the first 10 custom Amazon CloudWatch metrics.

Your AWS Free Tier offerings depend on your plan type.
**Paid plan** accounts might have `Short-term
 trial` and `Always Free` offerings active. If you go
beyond the Free Tier free limit for a service or access paid features, your
AWS Free Tier credits automatically apply to cover the eligible cost. After
your AWS Free Tier credits expire or are fully used, you're charged at the
standard AWS billing rates for usage beyond the free limits.
**Free account plan** accounts only have `Always
 Free` offerings active.

When you exceed the Free Tier limit for a service, AWS sends an email to the
email address that you used to create your account (the AWS account root user). To change the
email address for AWS Free Tier usage alerts, see the following procedure:

###### To change the email address for AWS Free Tier usage alerts

1. Sign in to the AWS Management Console and open the Billing console at
   [https://console.aws.amazon.com/billing/](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/").
2. Under **Preferences** in the navigation pane, choose
   **Billing preferences**.
3. For **Alert preferences**, choose
   **Edit**.
4. Enter the email address to receive the usage alerts.
5. Choose **Update**.

AWS Budgets usage alerts for 85 percent of the Free Tier limit are automatically
activated for all individual AWS accounts, but not for a management account in an
AWS Organizations. If you own a management account, you must opt in to get AWS Free Tier usage
alerts. Use the following procedure to opt in or out of Free Tier usage
alerts.

###### To opt in or out of AWS Free Tier usage alerts

1. Sign in to the AWS Management Console and open the Billing console at
   [https://console.aws.amazon.com/billing/](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/").
2. Under **Preferences** in the navigation pane, choose
   **Billing preferences**.
3. For **Alert preferences**, choose
   **Edit**.
4. Select **Receive AWS Free Tier alerts** to opt in to Free
   Tier usage alerts. To opt out, clear **Receive AWS Free Tier
   alerts**.
5. Choose **Update**.

## Recommended actions for Free Tier

If you're eligible for AWS Free Tier and you use a free tier offering, you can track
your usage with the **Recommended actions** widget on the Billing and Cost Management home
page. This widget shows recommendations if your usage exceeded 85% of any
service's free tier usage limits.

The following conditions might limit whether you see AWS Free Tier data:

- You use an AWS service that doesn't offer Free Tier
- Your Free Tier has expired
- You access AWS through an AWS Organizations member account
- You use an AWS service in the AWS GovCloud (US-West) or AWS GovCloud (US-East)
  Regions

For more information, see [Recommended actions](view-billing-dashboard.md#recommended-actions-widget "view-billing-dashboard.md#recommended-actions-widget").

## Trackable AWS Free Tier services

With AWS, you can track how much you used AWS Free Tier services and what service
usage types you used. Usage types are the specific type of usage that AWS tracks.
For example, the usage type `BoxUsage:freetier.micro` means that you used
an Amazon EC2 micro instance.

The AWS Free Tier usage alerts and the **Top AWS Free Tier Services by
Usage** table cover both expiring and non-expiring AWS Free Tier
offerings. You can track the following services and usage types.

| Service                                        | Usage type                                                                                                                                                                                                 | Free Tier type   |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| AWS Audit Manager                              | Resource-Assessment-Collected                                                                                                                                                                              | Short-term trial |
| AWS Budgets                                    | ActionEnabledBudgetsUsage                                                                                                                                                                                  | Always Free      |
| CloudFormation                                 | Resource-Invocation-Count-FreeTier                                                                                                                                                                         | Always Free      |
| AWS CodeArtifact                               | RequestsTimedStorage-ByteHrs                                                                                                                                                                               | Always Free      |
| AWS CodeCommit                                 | User-Month                                                                                                                                                                                                 | Always Free      |
| AWS CodePipeline                               | actionExecutionMinuteactivePipeline                                                                                                                                                                        | Always Free      |
| AWS Data Transfer                              | DataTransfer-Out-BytesDataTransfer-Regional-Bytes                                                                                                                                                          | Always Free      |
| AWS Database Migration Service                 | InstanceUsg:dms.t2.microInstanceUsg:dms.t3.micro                                                                                                                                                           | Always Free      |
| AWS DeepRacer                                  | ServiceUse-Train-Evaluate-JobTimedStorage-GigabyteHrs                                                                                                                                                      | Short-term trial |
| AWS Directory Service                          | MicrosoftAD-DC-UsageSmall-Directory-Usage                                                                                                                                                                  | Short-term trial |
| AWS Elemental MediaConnect                     | DataTransfer-Out-Bytes                                                                                                                                                                                     | Always Free      |
| AWS Glue                                       | Catalog-RequestCatalog-Storage                                                                                                                                                                             | Always Free      |
| AWS Key Management Service                     | KMS-Requests                                                                                                                                                                                               | Always Free      |
| AWS Lambda                                     | Lambda-GB-SecondLambda-Streaming-Response-Processed-BytesRequest                                                                                                                                           | Always Free      |
| AWS Migration Hub Refactor Spaces              | API-RequestEnvironmentHours                                                                                                                                                                                | Always Free      |
| AWS RoboMaker                                  | SimulationUnitHour                                                                                                                                                                                         | Short-term trial |
| AWS Security Hub CSPM                          | OtherProduct:PaidFindingsIngestionRuleEvaluation                                                                                                                                                           | Always Free      |
| AWS Service Catalog                            | SC-API-Calls                                                                                                                                                                                               | Always Free      |
| AWS Step Functions                             | StateTransition                                                                                                                                                                                            | Always Free      |
| AWS Storage Gateway                            | Uploaded-Bytes                                                                                                                                                                                             | Always Free      |
| Supply Chain                                   | ADPSiteProductCountSiteProductCountStorageSize                                                                                                                                                             | Short-term trial |
| AWS Systems Manager                            | AWS-Auto-ScriptDuration-Tier3AWS-Auto-Steps-Tier1IM-Notifications-Tier1                                                                                                                                    | Always Free      |
| AWS WAF                                        | AMR-BotControl-RequestAMR-BotControl-Targeted-RequestAMR-FraudControl-RequestShieldProtected-AMR-BotControl-RequestShieldProtected-AMR-BotControl-Targeted-RequestShieldProtected-AMR-FraudControl-Request | Always Free      |
| AWS X-Ray                                      | XRay-TracesAccessedXRay-TracesStored                                                                                                                                                                       | Always Free      |
| Amazon AppStream                               | stream-hrs:720p:g2stream.standard.large-ib                                                                                                                                                                 | Short-term trial |
| Amazon Braket                                  | Simulators-Task                                                                                                                                                                                            | Short-term trial |
| Amazon CloudFront                              | DataTransfer-Out-BytesExecutions-CloudFrontFunctionsInvalidationsRequests-Tier1                                                                                                                            | Always Free      |
| Amazon CloudSearch                             | (all SearchInstance types)                                                                                                                                                                                 | Short-term trial |
| Amazon Cognito                                 | CognitoEnterpriseMAUCognitoUserPoolMAU                                                                                                                                                                     | Always Free      |
| Amazon Cognito Sync                            | CognitoSyncOperationTimedStorage-ByteHrs                                                                                                                                                                   | Always Free      |
| Amazon DataZone                                | DataZoneComputeDataZoneRequestsDataZoneStorageDataZoneUsers                                                                                                                                                | Short-term trial |
| Amazon DevOps Guru                             | DevOpsGuru-APICallsResourceGroup-A-usagehoursResourceGroup-B-usagehours                                                                                                                                    | Short-term trial |
| Amazon DocumentDB (with MongoDB compatibility) | BackupUsageInstanceUsage:db.t3.mediumStorageIOUsageStorageUsage                                                                                                                                            | Short-term trial |
| Amazon DynamoDB                                | ReadCapacityUnit-HrsReplWriteCapacityUnit-HrsStreams-RequestsTimedStorage-ByteHrsWriteCapacityUnit-Hrs                                                                                                     | Always Free      |
| Amazon Elastic Container Service               | ECS-Anywhere-Instance-hours-WithFree                                                                                                                                                                       | Short-term trial |
| Amazon Forecast                                | DataInjectionForecastDataPointsTrainingHours                                                                                                                                                               | Short-term trial |
| Amazon Fraud Detector                          | (all FraudPrediction types)                                                                                                                                                                                | Short-term trial |
| AWS HealthLake                                 | FHIRDataStorageFHIRQueries                                                                                                                                                                                 | Always Free      |
| Amazon Kendra                                  | KendraDeveloperEditionKendraIntelligentRanking-BaseCapacity                                                                                                                                                | Short-term trial |
| Amazon Keyspaces (for Apache Cassandra)        | ReadRequestUnitsTimedStorage-ByteHrsWriteRequestUnits                                                                                                                                                      | Short-term trial |
| Amazon Lightsail                               | (all BundleUsage types)                                                                                                                                                                                    | Short-term trial |
| Amazon Location Service                        | (all types)                                                                                                                                                                                                | Short-term trial |
| Amazon Lookout for Equipment                   | Inference-Hours-L4EIngestion-GB-L4ETraining-Hours-L4E                                                                                                                                                      | Short-term trial |
| Amazon Lookout for Metrics                     | ANOMALY\_DETECTION                                                                                                                                                                                         | Short-term trial |
| Amazon Lookout for Vision                      | (all types)                                                                                                                                                                                                | Short-term trial |
| Amazon Macie                                   | EventsProcessingS3ContentClassificationSensitiveDataDiscovery                                                                                                                                              | Short-term trial |
| Amazon Managed Service for Prometheus          | AMP:MetricSampleCountAMP:MetricStorageByteHrsAMP:QuerySamplesProcessed                                                                                                                                     | Always Free      |
| Amazon MemoryDB                                | DataWrittenNodeUsage:db.t4g.small                                                                                                                                                                          | Short-term trial |
| Amazon Neptune                                 | BackupUsageDataTransfer-Out-BytesInstanceUsage:db.t3.mediumStorageIOUsageStorageUsage                                                                                                                      | Short-term trial |
| AWS HealthOmics                                | (all types)                                                                                                                                                                                                | Short-term trial |
| Amazon Personalize                             | DataIngestionTPS-hoursTrainingHour                                                                                                                                                                         | Short-term trial |
| Quick                                          | QS-ENT-Alerts-FreeTrial                                                                                                                                                                                    | Short-term trial |
| Amazon Redshift                                | Node:dc2.largeNode:dw2.large                                                                                                                                                                               | Short-term trial |
| Amazon Route 53                                | Cidr-BlocksHealth-Check-AWS                                                                                                                                                                                | Always Free      |
| Amazon SageMaker Runtime                       | (all types)                                                                                                                                                                                                | Short-term trial |
| Amazon Simple Email Service                    | MessageMessageUnitsRecipients-EC2Recipients-MailboxSim-EC2VirtDelivMgr                                                                                                                                     | Always Free      |
| Amazon Simple Notification Service             | (all types)                                                                                                                                                                                                | Always Free      |
| Amazon Simple Queue Service                    | Requests                                                                                                                                                                                                   | Always Free      |
| Amazon Simple Workflow Service                 | AggregateInitiatedActionsAggregateInitiatedWorkflowsAggregateWorkflowDays                                                                                                                                  | Always Free      |
| Amazon SimpleDB                                | BoxUsageTimedStorage-ByteHrs                                                                                                                                                                               | Always Free      |
| Amazon Textract                                | (all types)                                                                                                                                                                                                | Short-term trial |
| Amazon Timestream                              | (all types)                                                                                                                                                                                                | Short-term trial |
| Amazon WorkSpaces                              | (all types)                                                                                                                                                                                                | Short-term trial |
| Amazon CloudWatch                              | (all types)                                                                                                                                                                                                | Always Free      |
| CloudWatch Events                              | Event-8K-ChunksScheduledInvocation                                                                                                                                                                         | Always Free      |
| CodeBuild                                      | Build-Min:Linux:g1.smallBuild-Sec:Lambda.1GB                                                                                                                                                               | Always Free      |
| CodeCatalyst                                   | (all types)                                                                                                                                                                                                | Always Free      |
| CodeGuru                                       | Profiler-Lambda-Sampling-Hour                                                                                                                                                                              | Short-term trial |
| Amazon Comprehend Medical                      | (all types)                                                                                                                                                                                                | Short-term trial |
