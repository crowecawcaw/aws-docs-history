

# Creating backups of DynamoDB tables with AWS Backup
<a name="CreateBackupAWS"></a>

This section describes how to turn on AWS Backup to create on-demand and scheduled backups from your DynamoDB tables. 

** [Turning on AWS Backup features](#CreateBackupAWS_enabling) [On-demand backups](#CreateBackupAWS_on-demand) [Scheduled backups](#CreateBackupAWS_scheduled)**
+ [Turning on AWS Backup features](#CreateBackupAWS_enabling)
+ [On-demand backups](#CreateBackupAWS_on-demand)
+ [Scheduled backups](#CreateBackupAWS_scheduled)

## Turning on AWS Backup features
<a name="CreateBackupAWS_enabling"></a>

You must turn on AWS Backup to use it with DynamoDB.

To turn on AWS Backup, go through the following steps:

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. In the navigation pane on the left side of the console, choose **Backups**.

1. In the Backup Settings window, choose **Turn on**.

1. A confirmation screen will appear. Choose **Turn on features**.

 AWS Backup features are now available for your DynamoDB tables. 

If you choose to turn off AWS Backup features after they’ve been turned on, follow these steps:

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. In the navigation pane on the left side of the console, choose **Backups**.

1. In the Backup Settings window, choose **Turn off**.

1. A confirmation screen will appear. Choose **Turn off features**.

 If you can’t turn the AWS Backup features on or off, your AWS admin might need to perform those actions.

## On-demand backups
<a name="CreateBackupAWS_on-demand"></a>

To create an on-demand backup of a DynamoDB table, follow these steps: 

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. In the navigation pane on the left side of the console, choose **Backups**.

1. Choose **Create backup**.

1. From the dropdown menu that appears, choose **Create an on-demand backup**.

1. To create a backup managed by AWS Backup with warm storage and other basic features, choose **Default Settings.** To create a backup that can be transitioned to cold storage, or to create a backup with DynamoDB features instead of AWS Backup, choose **Customize settings**.

   If you want to create this backup with previous DynamoDB features instead, choose **Customize settings** and then choose **Backup with DynamoDB**.

1. When you have completed the settings, choose **Create backup.**

## Scheduled backups
<a name="CreateBackupAWS_scheduled"></a>

To schedule a backup, follow these steps. 

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. In the navigation pane on the left side of the console, choose **Backups**.

1. From the dropdown menu that appears, choose **Schedule backups with AWS Backup**.

1. You will be taken to AWS Backup to create a backup plan.