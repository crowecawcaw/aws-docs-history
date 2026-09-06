

# Troubleshooting
<a name="S3-buckets-troubleshooting"></a>

**How to check if a bucket fails to mount on a VDI** 

If a bucket fails to mount on a VDI, there are a few locations where you can check for errors. Follow the steps below.

1. Check the VDI Logs:

   1. Sign in to the AWS Management Console. 

   1. Open the EC2 Console and navigate to **Instances**.

   1. Select the VDI instance you launched.

   1. Connect to the VDI via the Session Manager.

   1. Run the following commands:

      ```
      sudo su
      cd ~/bootstrap/logs
      ```

      Here, you'll find the bootstrap logs. The details of any failure will be located in the `configure.log.{time}` file.

      Additionally, check the `/etc/message` log for more details.

1. Check Custom Credential Broker Lambda CloudWatch Logs:

   1. Sign in to the AWS Management Console.

   1. Open the CloudWatch Console and navigate to **Log groups**.

   1. Search for the log group `/aws/lambda/{{<stack-name>}}-vdc-custom-credential-broker-lambda`. 

   1. Examine the first available log group and locate any errors within the logs. These logs will contain details regarding potential issues providing temporary custom credentials for mounting S3 buckets. 

1. Check Custom Credential Broker API Gateway CloudWatch Logs:

   1. Sign in to the AWS Management Console.

   1. Open the CloudWatch Console and navigate to **Log groups**.

   1. Search for the log group `{{<stack-name>}}-vdc-custom-credential-broker-lambdavdccustomcredentialbrokerapigatewayaccesslogs<nonce>`. 

   1. Examine the first available log group and locate any errors within the logs. These logs will contain details regarding any requests and responses to the API Gateway for custom credentials needed to mount the S3 buckets.

**How to edit a bucket's IAM role configuration after onboarding** 

1. Sign in to the [AWS DynamoDB Console](https://console.aws.amazon.com/dynamodbv2/home).

1. Select the Table: 

   1. In the left navigation pane, choose **Tables**.

   1. Find and select `{{<stack-name>}}.cluster-settings`. 

1. Scan the Table: 

   1. Choose **Explore table items**.

   1. Ensure **Scan** is selected.

1. Add a Filter:

   1. Choose **Filters** to open the filter entry section.

   1. Set the filter to match your key-
      + **Attribute**: Enter the key.
      + **Condition**: Select **Begins with**.
      + **Value**: Enter `shared-storage.{{<filesystem_id>}}.s3_bucket.iam_role_arn` replacing {{<filesystem\_id>}} with the value of the filesystem that needs to be modified.

1. Execute the Scan:

   Choose **Run** to run the scan with the filter.

1. Check the value: 

   If the entry exists, ensure the value is correctly set with the right IAM role ARN.

   If the entry does not exist:

   1. Choose **Create item**.

   1. Enter the item details:
      + For the key attribute, enter `shared-storage.{{<filesystem_id>}}.s3_bucket.iam_role_arn`. 
      + Add the correct IAM role ARN.

   1. Choose **Save** to add the item.

1. Restart the VDI instances: 

   Reboot the instance to ensure the VDIs that are affected by the incorrect IAM role ARN are mounted again.