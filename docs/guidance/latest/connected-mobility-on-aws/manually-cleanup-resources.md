

# Manually clean up resources
<a name="manually-cleanup-resources"></a>

You must manually clean up the following resources:
+ S3 buckets
+ DynamoDB tables
+ Cognito user pool
+ KMS keys

Locate leftover resources using the following command, which first requires you to export the `DEPLOYMENT_UUID` variable using each of the values previously acquired from AWS Systems Manager.

If you tore down the stack without capturing the UUID, you can run the following command by removing the `Solutions:DeploymentUUID` Key filter, however the results will include other CMS on AWS stacks if they exist, so use this method with caution.

```
export DEPLOYMENT_UUID=<DEPLOYMENT_UUID_VALUE_FROM_SSM>

aws resourcegroupstaggingapi get-resources --tag-filters \
Key=Solutions:SolutionID,Values=SO0241 \
Key=Solutions:DeploymentUUID,Values=$DEPLOYMENT_UUID \
--query "ResourceTagMappingList[*].ResourceARN"
```

This query results in a list of ARNs to assist you with locating the resources in the AWS Management Console. Resources can then be manually deleted, or deleted with a script, utilizing the resource ARNs where appropriate.

**Important**  
Some resources may take some time to clean up after CloudFormation finishes tearing down, and could show in the output even if they no longer exist. For example, Amazon VPC, Fargate, and Amazon ECS resources can remain queryable for up to 30 minutes after deletion.

## Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

The guidance is configured to retain the Amazon S3 buckets if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the guidance, you can manually delete these Amazon S3 buckets if you don’t need to retain the data. Follow these steps to delete an Amazon S3 bucket.

**Note**  
 **Bucket RETAIN behavior:** Globally-named S3 buckets (those with explicit names that include the deployment stage, AWS Region, and account ID) are retained by design when their CloudFormation stack is deleted. This behavior is intentional — it prevents accidental data loss when the same stage is deployed to multiple AWS Regions and bucket names would otherwise collide in the global S3 namespace. After confirming you no longer need the data, you must delete these buckets manually using the steps below. Use the deployment UUID tag query above to locate all retained buckets associated with a specific deployment.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the S3 buckets created by the guidance.

1. Select an S3 bucket.

1. Choose **Delete**.

To delete the Amazon S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```

## Deleting the Amazon DynamoDB tables
<a name="deleting-the-amazon-dynamodb-tables"></a>

The guidance is configured to retain the DynamoDB tables if you decide to delete the CloudFormation stack to prevent accidental data loss. After uninstalling the guidance, you can manually delete the DynamoDB tables if you do not need to retain the data. Follow these steps:

1. Sign in to the [Amazon DynamoDB console](https://console.aws.amazon.com/dynamodb/home?).

1. Choose **Tables** from the left navigation pane.

1. Locate the tables created by the guidance.

1. Select a CMS on AWS table.

1. Choose **Delete**.

1. Repeat the steps until you have deleted all of the guidance’s tables.

To delete the DynamoDB tables using AWS CLI, run the following command:

```
$ aws dynamodb delete-table <table-name>
```

## Deleting the Amazon CloudWatch logs
<a name="deleting-the-amazon-cloudwatch-logs"></a>

The guidance retains the CloudWatch Logs if you decide to delete the CloudFormation stack to prevent against accidental data loss. After uninstalling the guidance, you can manually delete the logs if you do not need to retain the data. Follow these steps to delete the CloudWatch Logs.

1. Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home?).

1. Choose **Log Groups** from the left navigation pane.

1. Locate the log groups created by the guidance.

1. Select one of the log groups.

1. Choose **Actions - Delete**.

Repeat the steps until you have deleted all the guidance’s log groups.

To delete the CloudWatch log groups using AWS CLI, run the following command:

```
$ aws logs delete-log-group --log-group-name <log-group-name>
```

## Deleting the AWS KMS customer managed keys
<a name="deleting-the-aws-kms-customer-managed-keys"></a>

The guidance retains the AWS KMS customer managed keys if you decide to delete the CloudFormation stack to prevent against accidental encrypted data loss. After uninstalling the guidance, you can manually delete the keys if you do not need to use them again. Follow these steps to delete the AWS KMS keys.

1. Sign in to the [AWS KMS console](https://console.aws.amazon.com/kms/home?).

1. Choose **Customer managed keys** from the left navigation pane.

1. Locate the keys created by the guidance.

1. Select one of the keys.

1. Choose **Key actions - Schedule key deletion**.

1. Optionally edit the **Waiting period (in days)** value.

1. Select **Confirmation**.

1. Choose **Schedule deletion**.

Repeat the steps until you have deleted all the guidance’s customer managed keys.

To delete the AWS KMS customer managed keys using AWS CLI, run the following command:

```
$ aws kms schedule-key-deletion –-key-id <key-id-or-arn>
```

## Deleting the Amazon Cognito user pools
<a name="deleting-the-amazon-cognito-user-pools"></a>

The guidance retains the Amazon Cognito user pools if you decide to delete the CloudFormation stack to prevent against accidental user data loss. After uninstalling the guidance, you can manually delete the user pools if you do not need to retain the users. Follow these steps to delete the user pools.

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home?).

1. Choose **User pools** from the left navigation pane.

1. Locate the user pools created by the guidance.

1. Select one of the user pools.

1. Choose **Delete**.

1. Select **Deactivate deletion protection**.

1. Enter the user pool name in the second field.

1. Choose **Delete**.

Repeat the steps until you have deleted all the guidance’s user pools.

To delete the Amazon Cognito user pool using AWS CLI, run the following command:

```
$ aws cognito-idp delete-user-pool –-user-pool-id <user-pool-id>
```

## Deleting the Amazon Relational Database Service snapshots
<a name="deleting-the-amazon-relational-database-service-snapshots"></a>

The guidance retains the [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) snapshots if you decide to delete the AWS CloudFormation stack to prevent against accidental data loss. After uninstalling the guidance, you can manually delete the snapshots if you do not need to retain the data. Follow these steps to delete the snapshots.

1. Sign in to the [Amazon RDS console](https://console.aws.amazon.com/rds/home?).

1. Choose **Snapshots** from the left navigation pane.

1. Locate the snapshots created by the guidance.

1. Select one of the snapshots.

1. Choose **Actions – Delete snapshot**.

1. Choose **Delete**.

Repeat the steps until you have deleted all the guidance’s snapshots.

To delete the Amazon RDS snapshot using AWS CLI, run the following command:

```
$ aws rds delete-db-snapshot –-db-snapshot-identifier <db-snapshot-identifier>
```