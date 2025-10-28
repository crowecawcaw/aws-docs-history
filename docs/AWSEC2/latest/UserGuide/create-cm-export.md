# Creating a data export for your Capacity Manager data

To create a data export, you can use the Data Exports page in the Capacity Manager console or the AWS CLI.

## Prerequisites

You must create an Amazon Simple Storage Service (Amazon S3) bucket. You must make sure of the following:

- Your S3 bucket must be in the same AWS Region where you enabled Capacity Manager.
- Your S3 bucket has the required permissions policy for the Capacity Manager service to deliver files.

For more information, see [Setting up an Amazon S3 bucket for Capacity Manager data exports](cm-set-up-s3-export.md "cm-set-up-s3-export.md").

## Procedure

You can export your Capacity Manager data using the AWS Console or the AWS CLI.

Console

###### To create a data export

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Manager**.
3. Choose the **Data exports** tab.
4. Choose **Create data export**.
5. Configure you export properties, delivery location, and tags (optional).
6. Choose **Create**.

AWS CLI

###### To create a data export

Use the following command to create a data export with the specified configuration:

```

aws ec2 create-capacity-manager-data-export \
    --s3-bucket-name my-exports-bucket \
    --s3-bucket-prefix capacity-data-exports \
    --schedule hourly \
    --output-format `parquet/CSV` \
    --tag-specifications 'ResourceType=capacity-manager-data-export,Tags=[{Key=environment,Value=production}]'

```
