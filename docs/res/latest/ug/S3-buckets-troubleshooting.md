# Troubleshooting

**How to check if a bucket fails to mount on a VDI**

If a bucket fails to mount on a VDI, there are a few locations where you can check for
errors. Follow the steps below.

1.  Check the VDI Logs:
    1. Log into the AWS Management Console.
    2. Open the EC2 Console and navigate to **Instances**.
    3. Select the VDI instance you launched.
    4. Connect to the VDI via the Session Manager.
    5. Run the following commands:

    ```
    sudo su
    cd ~/bootstrap/logs
    ```

    Here, you'll find the bootstrap logs. The details of any failure will be
    located in the `configure.log.{time}` file.

    Additionally, check the `/etc/message` log for more details.

2.  Check Custom Credential Broker Lambda CloudWatch Logs:
    1. Log into the AWS Management Console.
    2. Open the CloudWatch Console and navigate to **Log groups**.
    3. Search for the log group
       `/aws/lambda/`<stack-name>`-vdc-custom-credential-broker-lambda`.
    4. Examine the first available log group and locate any errors within the logs.
       These logs will contain details regarding potential issues providing temporary
       custom credentials for mounting S3 buckets.

3.  Check Custom Credential Broker API Gateway CloudWatch Logs:

        1. Log into the AWS Management Console.
        2. Open the CloudWatch Console and navigate to **Log groups**.
        3. Search for the log group
         ``<stack-name>`-vdc-custom-credential-broker-lambdavdccustomcredentialbrokerapigatewayaccesslogs<nonce>`.
        4. Examine the first available log group and locate any errors within the logs.
         These logs will contain details regarding any requests and responses to the API
         Gateway for custom credentials needed to mount the S3 buckets.

    **How to edit a bucket's IAM role configuration after onboarding**

4.  Sign in to the [AWS DynamoDB
    Console](https://console.aws.amazon.com/dynamodbv2/home "https://console.aws.amazon.com/dynamodbv2/home").
5.  Select the Table:
    1. In the left navigation pane, choose **Tables**.
    2. Find and select ``<stack-name>`.cluster-settings`.

6.  Scan the Table:
    1. Choose **Explore table items**.
    2. Ensure **Scan** is selected.

7.  Add a Filter:
    1. Choose **Filters** to open the filter entry section.
    2. Set the filter to match your key-
       - **Attribute**: Enter the key.
       - **Condition**: Select **Begins with**.
       - **Value**: Enter
         `shared-storage.`<filesystem_id>`.s3_bucket.iam_role_arn`
         replacing `<filesystem_id>` with the
         value of the filesystem that needs to be modified.

8.  Execute the Scan:

Choose **Run** to run the scan with the filter. 6. Check the value:

If the entry exists, ensure the value is correctly set with the right IAM
role ARN.

If the entry does not exist:

    1. Choose **Create item**.
    2. Enter the item details:




    	* For the key attribute, enter
    	 `shared-storage.`<filesystem_id>`.s3_bucket.iam_role_arn`.
    	* Add the correct IAM role ARN.
    3. Choose **Save** to add the item.

7. Restart the VDI instances:

Reboot the instance to ensure the VDIs that are affected by the incorrect IAM
role ARN are mounted again.
