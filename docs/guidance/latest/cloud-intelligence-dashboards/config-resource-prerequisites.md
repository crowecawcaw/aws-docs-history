

# Prerequisites
<a name="config-resource-prerequisites"></a>

## Architecture
<a name="architecture"></a>

The AWS Config Resource Compliance Dashboard (CRCD) solution can be deployed in standalone AWS accounts or AWS accounts that are members of an AWS Organization.

You can deploy the dashboard in a standalone account with [AWS Config enabled](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html). This option may be useful for proof of concept or testing purposes. In this case, all dashboard resources are deployed within the same AWS account.

If you use AWS Organizations, AWS Config must be enabled with an [AWS Config delivery channel](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html) sending files to a centralized Amazon S3 bucket (which we will call the AWS Config Logs bucket) in a dedicated account (which we will call the AWS Config account). In this case, there are two possible ways to deploy the CRCD dashboard.

1.  **Deploy in the AWS Config account** You can deploy the dashboard resources in the same account where your AWS Config configuration files are delivered. The architecture in this case looks like this:

![AWS Config Dashboard: deployment on AWS Organization](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/crcd-architecture-log-archive-account.png)


1.  **Deploy in a separate Dashboard account** Alternatively, you can create a separate Dashboard account to deploy the dashboard resources. In this case, objects from the AWS Config Logs bucket in the AWS Config account are replicated to another bucket in the Dashboard account.

![AWS Config Dashboard: deployment on AWS Organization](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/crcd-architecture-dashboard-account.png)


An Amazon Athena table is used to extract data from the AWS Config configuration files delivered to Amazon S3. Whenever a new object is added to the bucket, the Lambda Partitioner function is triggered. This function checks if the object is an AWS Config configuration snapshot or configuration history file. If it is, the function adds a new partition to the corresponding Athena table with the new data. If the object is neither a configuration snapshot nor configuration history file, the function ignores it.

The solution provides Athena views, which are SQL queries that extract data from Amazon S3 using the schema defined in the Athena table. Finally, you can visualize the data in a Quick Sight dashboard that uses these views through Amazon Quick Sight datasets.

### AWS Config Logs bucket encrypted with an AWS Key Management Service (KMS) key
<a name="aws-config-logs-bucket-encrypted-with-an-aws-key-management-service-kms-key"></a>

The deployment process supports AWS Config Logs buckets encrypted using a customer-managed KMS key (SSE-KMS).

In case of AWS Config account deployment:
+ Amazon Quick Sight will be granted permissions to use the KMS key for decrypt operations. This is done with an IAM policy. If you prefer, you can manually grant this permission directly on the key policy. See below for instructions.

In case of Dashboard account deployment:
+ S3 replication must occur between buckets with the same type of encryption.
+ The Dashboard bucket will be encrypted with a KMS key which is created by the AWS CloudFormation template.
+ The S3 replication policy will have permissions to use the KMS keys of both buckets.

**Note**  
If your AWS Config Logs bucket is SSE-KMS encrypted, and you do not provide the ARN of the corresponding KMS key in the CloudFormation parameters, the dashboard resources will not have the necessary permissions to function correctly.

## Prerequisites
<a name="prerequisites"></a>

1. AWS Config enabled in the accounts and AWS Regions you want to track, with an AWS Config delivery channel sending files to a centralized Amazon S3 bucket (the AWS Config Logs bucket) in a dedicated account (the AWS Config account).
   + We recommend that your AWS Config delivery channel delivers AWS Config configuration snapshot files every 24 hours for all accounts and Regions where AWS Config is active (see below for more information).

1. An AWS account where you’ll deploy the dashboard.

1. An IAM Role or IAM User with permissions to deploy the infrastructure using CloudFormation.

1. Sign up for [Amazon QuickSight](https://docs.aws.amazon.com/quick/latest/userguide/signing-up.html) and create a user:

   1. Select **Enterprise** edition.

   1. For the **Get Paginated Reports add-on**, choose the option you prefer (this is not required for deploying the dashboard).

   1.  **Use IAM federated identities and Quick Sight-managed users**.

   1. Select the Region where to deploy the dashboard. We recommend using the same Region of your Amazon S3 bucket.

   1. Add a username and an e-mail where you’ll receive notifications about failed Quick Sight datasets updates.

   1. Use the **Quick Sight-managed role (default)**.

   1. Don’t modify the **Allow access and autodiscovery for these resources** section and click **Finish**.

1. Ensure you have SPICE capacity available in the Region where you’re deploying the dashboard.

### Account Names
<a name="account-names"></a>

If you deployed other CUDOS dashboards, the dashboard will display account names. If you deploy the AWS Organization Data Collection Module of [CID Data Collection](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection.html), the dashboard supports your organizational taxonomy (account names, OUs and OU tags). The latter is the recommended way to extend the dashboard with account names and organization metadata, make sure the setup of CID Data Collection is complete prior to deploy the dashboard, and that you install the dashboard and the CID Data collection module in the same account and Region.

## Before you start
<a name="before-you-start"></a>

### AWS Config considerations
<a name="aws-config-considerations"></a>

 *Skip this paragraph if you have AWS Config enabled.* 

The solution leverages AWS Config data to build the visualizations on the dashboard. If you **do not** have AWS Config enabled, we strongly recommend building your strategy first:
+ Decide which accounts, Regions, and resources to monitor.
+ Define what "compliance" means to your organization, i.e. which [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) or [conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) to activate.
+ Identify the account that will be delegated admin for AWS Config.
+ Keep in mind the paragraphs below when enabling AWS Config.

**Note**  
Only when the AWS Config setup matches your needs should you consider deploying this dashboard.

### AWS Config delivery channel considerations
<a name="aws-config-delivery-channel-considerations"></a>

The AWS Config delivery channel is a crucial component for managing and controlling where configuration updates are sent. It consists of an Amazon S3 bucket and an optional Amazon SNS topic, which is not needed by the AWS Config dashboard. The S3 bucket is used to store AWS Config configuration history and configuration snapshots files, while the SNS topic can be used for streaming configuration changes. A delivery channel is required to use AWS Config and is limited to one per Region per AWS account. When setting up a delivery channel, you can specify the name, the S3 bucket for file delivery, and the frequency of configuration snapshot delivery.

A configuration **snapshot** provides a comprehensive view of all currently active recorded configuration items within a customer’s AWS account. In contrast, AWS Config delivers automatically a configuration **history** file to the S3 bucket every 6 hours. This file contains changes detected for each resource type since the last history file was delivered. Check this [blog post](https://aws.amazon.com/blogs/mt/configuration-history-configuration-snapshot-files-aws-config/) for more information on the difference between AWS Config configuration history and configuration snapshot files.

The dashboard does not support [oversized configuration item change notifications](https://docs.aws.amazon.com/config/latest/developerguide/oversized-notification-example.html).

To check your AWS Config delivery channel setup, you can use the AWS CLI command:

```
aws configservice describe-delivery-channels
```

This command will provide information about the delivery channel configuration on the account and Region where it is launched, including the S3 bucket where configuration updates are sent and the configuration snapshot delivery properties. Ensure the configuration is consistent across all accounts and Regions you want to record. The output of the CLI command should look like this:

```
{
    "DeliveryChannels": [
        {
            "name": "[YOUR-DELIVERY-CHANNEL-NAME]",
            "s3BucketName": "[YOUR-LOG-ARCHIVE-BUCKET-NAME]",
            "s3KeyPrefix": "[OPTIONAL-S3-PREFIX-FOR-AWS-CONFIG-FILES]",
            "configSnapshotDeliveryProperties": {
                "deliveryFrequency": "TwentyFour_Hours"
            }
        }
    ]
}
```

We recommend to have `configSnapshotDeliveryProperties` configured on your delivery channel with a delivery frequency of 24 hours, run the CLI command above to verify your setup.

**Note**  
AWS Control Tower configures the AWS Config delivery channel with a 24-hour delivery frequency for configuration snapshot files.

#### Click here to read what to do if your delivery channel is not configured to deliver configuration snapshots
<a name="collapsible-section-id-config-resource-prerequisites-1"></a>

 **How to add daily delivery of configuration snapshot files to your delivery channel** 

You have to configure this on every account and Region where you have AWS Config active. We’ll give an example below of how this can be achieved with the AWS CLI, but if your environment consists of several AWS accounts and Regions, we recommend using CloudFormation StackSets to ensure a consistent configuration.

Here’s how you can use the AWS CLI to modify the existing settings and schedule the delivery of configuration snapshot files to your delivery channel configuration.

1. Log into the AWS Console in any account and Region, open AWS CloudShell.

1. Run the AWS CLI command `aws configservice describe-delivery-channels` and save the resulting JSON to a local file. Name it `deliveryChannel.json`. For example, your file may look like the one below.

```
{
  "name": "default",
  "s3BucketName": "config-bucket-123456789012",
  "snsTopicARN": "arn:aws:sns:us-east-1:123456789012:config-topic",
  "s3KeyPrefix": "my-prefix"
}
```

1. Verify the S3 bucket in `s3BucketName` is the name of your AWS Config Logs bucket.

1. Edit the file to add the `configSnapshotDeliveryProperties` section:

```
{
  "name": "default",
  "s3BucketName": "config-bucket-123456789012",
  "snsTopicARN": "arn:aws:sns:us-east-1:123456789012:config-topic",
  "s3KeyPrefix": "my-prefix",
  "configSnapshotDeliveryProperties": {
    "deliveryFrequency": "TwentyFour_Hours"
  }
}
```

You have to follow these steps consistently in every account and Region:

1. Log into the AWS Console of one account and Region, open AWS CloudShell.

1. Upload the `deliveryChannel.json` file containing the delivery channel configuration.

1. Use the `put-delivery-channel` AWS CLI [command](https://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html) to update your delivery channel configuration according to the content of the JSON file. This command allows you to update or modify your current delivery channel settings.

```
aws configservice put-delivery-channel --delivery-channel file://deliveryChannel.json
```

Ensure this is done consistently in every account and Region.

### Regional considerations
<a name="regional-considerations"></a>

**Note**  
You will incur data transfer costs when Amazon Athena queries an Amazon S3 bucket across Regions.

To avoid cross-region data transfer, Amazon Quick Sight and the Amazon S3 bucket containing AWS Config files must be deployed in the same Region.
+ If you have already deployed either resource, the other must use the same Region. If you haven’t deployed anything yet, you can choose a Region of your preference.
+ If you have deployed both resources in different Regions, we strongly recommend making changes so that both are in the same Region.
+ Once you have decided on the Region, deploy AWS resources supporting the dashboard (via CloudFormation) in the same Region.

The dashboards support organizational taxonomy and will allow you to add filters based on the Organizational Unit or on tags that you apply on the AWS Organizations Console from the payer account. In order to leverage this data, you must install the AWS Organization Data Collection Module of [CID Data Collection](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection.html). The data collection account and Region must be the same account and Region where you deploy the dashboard resources.

### Tag Compliance: naming convention on the AWS Config rule
<a name="tag-compliance-naming-convention-on-the-aws-config-rule"></a>

This part of the dashboard visualizes the evaluation results of AWS Config Managed Rule [required-tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html), or one of the several [rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) ending with `-tagged`. You can deploy these rules to find resources in your accounts that were not launched with your desired tag configurations. The rules can be deployed multiple times in AWS Config. To display data on the dashboard, make sure your tag rules' name contains either `required-tags`, `required-tag`, `requiredtags`, `requiredtag` or `tagged` (this is case insensitive).

### Deployment architecture
<a name="deployment-architecture"></a>

The most important decision is whether to deploy the dashboard on a dedicated Dashboard account or directly into the AWS Config account. These are the implications of each architecture.

#### AWS Config account architecture
<a name="aws-config-account-architecture"></a>


| Pros | Cons | 
| --- | --- | 
| Keep your logs secure in the AWS Config account. | Your security team must deploy and maintain the AWS Config Dashboard resources, including user access to Quick Sight. Alternatively, you have to share access to the account with other teams that will manage these resources. | 
| Avoid cost for data transfer and storing data on the Dashboard account. | If you already have S3 object notification configured on your AWS Config Logs bucket, a part of the deployment process must be done manually. | 

#### Dashboard account architecture
<a name="dashboard-account-architecture"></a>


| Pros | Cons | 
| --- | --- | 
| Allow your DevOps or Platform teams independence in installing and maintaining the dashboard, as well as regulating user access. | Your security data will be copied to another AWS account. | 
| A limited number of resources must be deployed on AWS Config account. | Until v3.3 (included), AWS Control Tower collects AWS Config and AWS CloudTrail on the same bucket. This means that all your security logs will be replicated to another account. | 
|  | You will incur costs for the replication and storing a copy of your data on another Amazon S3 bucket. CloudTrail logs will increase those costs needlessly, as they are not used by the dashboard. | 
|  | If you already have S3 replication configured on your AWS Config Logs bucket, a part of the deployment process must be done manually. | 

### Deployment instructions
<a name="deployment-instructions"></a>
+ Follow [these instructions](config-resource-log-archive.md) to deploy the dashboard in the **AWS Config** account, or in a standalone AWS account.
+ Follow [these instructions](config-resource-dashboard-account.md) to deploy the dashboard in the **Dashboard** account.