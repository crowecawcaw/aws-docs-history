

# Accessing data feeds
<a name="data-feed-accessing"></a>

With AWS Marketplace, you can use data feeds as a mechanism to send structured, up-to-date product and customer information from AWS Marketplace systems an Amazon S3 buckets for ETL (extract, transform, and load) between seller-owned business intelligence tools. You need to configure your environment to receive data feeds to an encrypted Amazon S3 bucket. This topic shows you how to access and unsubscribe from data feeds.

**Topics**
+ [Access a data feed](#data-feed-accessing-procedure)
+ [Data feed policies](#data-feed-policies)
+ [Unsubscribe from data feeds](#data-feed-unsubscribing)

## Access a data feed
<a name="data-feed-accessing-procedure"></a>

1. Allocate a business intelligence or data engineer with SQL and ETL (extract, transform, load) experience. This person also needs experience setting up APIs.

1. Set up an Amazon Simple Storage Service bucket and a subscription to the data feeds. Use the AWS seller account ID associated with your Marketplace product listings. To do so, you can [watch this YouTube video](https://www.youtube.com/watch?v=heCsZdOT-hw) or follow the steps below.

   The video and the steps explain how to use a [CloudFormation template](https://s3.amazonaws.com/aws-marketplace-reports-resources/DataFeedsResources.yaml) that helps simplify configuration.

   1. Open a web browser and sign into the [AWS Marketplace Management Portal](https://us-east-1.console.aws.amazon.com/partnercentral/home), then go to [Set up customer data storage](https://aws.amazon.com/marketplace/management/reports/data-feed-configuration).

   1. Choose **Create resources with CloudFormation template** to open the template in the CloudFormation console in another window.

   1. In the template, specify the following and then choose **Next**:
      + Stack name – The collection of resources you're creating to enable access to data feeds.
      + Amazon S3 bucket name – The bucket for storing data feeds.
      + (Optional) Amazon SNS topic name – The topic for receiving notifications when Amazon Simple Storage Service bucket.

   1. On the **Review** page, confirm your entries and choose **Create stack**. This will open a new page with the CloudFormation status and details.

   1. From the **Resources** tab, copy Amazon Resource Names (ARNs) for the following resources from the CloudFormation page into the fields on the AWS Marketplace [Set up customer data storage](https://aws.amazon.com/marketplace/management/reports/data-feed-configuration) page:
      + Amazon S3 bucket for storing data feeds
      + AWS KMS key for encrypting the Amazon S3 bucket
      + (Optional) Amazon SNS topic for receiving notifications when AWS delivers new data to the Amazon S3 bucket

   1. On the **Set up customer data storage** page, choose **Submit**.

   1. (Optional) Edit the policies created by the CloudFormation template. See [Data feed policies](#data-feed-policies) for more details.

      You are now subscribed to data feeds. The next time data feeds are generated, you can access the data.

1. Use an ETL (extract, transform, load) operation to connect the data feeds to your data warehouse or relational database.
**Note**  
Data tools have different capabilities. You must involve a business intelligence engineer or data engineer to set up the integration to match your tool’s capabilities.

1. To run or create SQL queries, configure the data feeds to enforce primary and foreign keys in your data tool. Each data feed represents a unique table, and you must set up all data feeds in data schema with the entity relationships. For more information about the tables and entity relationships, see [Data feed tables overview](data-feed-joining.md) in this guide.

1. Setup Amazon Simple Notification Service to automatically refresh your data warehouse or relational database. You can configure Amazon SNS notifications to send alerts when data from each unique feed is delivered to an Amazon S3 bucket. These notifications can be leveraged to automatically refresh seller data warehouse when new data is received via data feeds, if seller data tool supports this capability. See [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the *Amazon Simple Notification Service Developer Guide*.

   Example notification:

   ```
   {
           "mainExecutionId": "{{1bc08b11-ab4b-47e1-866a-9c8f38423a98}}",
           "executionId": "{{52e862a9-42d2-41e0-8010-810af84d39b1}}",
           "subscriptionId": "{{27ae3961-b13a-44bc-a1a7-365b2dc181fd}}",
           "processedFiles": [],
           "executionStatus": "{{SKIPPED}}",
           "errors": [],
           "feedType": "[{{data feed name}}]"
           }
   ```

   Notifications can have the following `executionStatus` states:
   + `SKIPPED` – The seller has no new data for the day.
   + `COMPLETED` – We delivered the feed with new data.
   + `FAILED` – The feed delivery has an issue.

1. Validate the setup by running SQL queries. You can use the [sample queries in this guide](https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-full-examples.html), or the queries on GitHub, at [ https://github.com/aws-samples/aws-marketplace-api-samples/tree/main/seller-data-feeds/queries](https://github.com/aws-samples/aws-marketplace-api-samples/tree/main/seller-data-feeds/queries).
**Note**  
The sample queries in this guide were written for AWS Athena. You may need to modify the queries for use with your tools.

1. Determine where business users want to consume data. For example, you can:
   + Export .csv data from your data warehouse or SQL database.
   + Connect your data to a visualization tool such as PowerBI or Tableau.
   + Map data to your CRM, ERP, or financial tools, such as Salesforce, Infor, or Netsuite.

For more information about CloudFormation templates, see [Working with CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the *AWS CloudFormation User Guide*.

## Data feed policies
<a name="data-feed-policies"></a>

When your Amazon S3 bucket is created by the CloudFormation template, it will create policies for access attached to that bucket, the AWS KMS key, and the Amazon SNS topic. The policies allow the AWS Marketplace reports service to write to your bucket and SNS topic with the data feed information. Each policy will have a section like the following (this example is from the Amazon S3 bucket).

```
        {
            "Sid": "AwsMarketplaceDataFeedsAccess",
            "Effect": "Allow",
            "Principal": {
                "Service": "reports.marketplace.amazonaws.com"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:GetEncryptionConfiguration",
                "s3:GetBucketAcl",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ]
        },
```

In this policy, AWS Marketplace uses the `reports.marketplace.amazonaws.com` service principal to push data to the Amazon S3 bucket. You specified the {{amzn-s3-demo-bucket}} in the CloudFormation template.

When the AWS Marketplace reports service calls Amazon S3, AWS KMS, or Amazon SNS, it provides the ARN of the data it intends to write to the bucket. To ensure that the only data written to your bucket is data written on your behalf, you can specify the `aws:SourceArn` in the condition of the policy. In the following example, you must replace the {{account-id}} with the ID for your AWS account.

```
        {
           "Sid": "AwsMarketplaceDataFeedsAccess",
           "Effect": "Allow",
           "Principal": {
                "Service": "reports.marketplace.amazonaws.com"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:GetEncryptionConfiguration",
                "s3:GetBucketAcl",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ,
            "Condition": {
                "StringEquals": {
                        "aws:SourceAccount": "{{account-id}}",
                        "aws:SourceArn": ["arn:aws:marketplace::{{account-id}}:AWSMarketplace/SellerDataSubscription/DataFeeds_V1",
                        "arn:aws:marketplace::{{account-id}}:AWSMarketplace/SellerDataSubscription/{{Example-Report}}"]
                        }
                }
        },
```

## Unsubscribe from data feeds
<a name="data-feed-unsubscribing"></a>

Open a web browser and sign in to the [AWS Partner Central](http://aws.amazon.com/marketplace/management/). Then, go to the [Contact us page](https://aws.amazon.com/marketplace/management/contact-us/) to submit an unsubscribe request to the AWS Marketplace Seller Operations team. The unsubscribe request can take up to 10 business days to process.