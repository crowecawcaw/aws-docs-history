

# Snowflake
<a name="snowflake"></a>

The following are the requirements and connection instructions for using Snowflake with Amazon AppFlow.

**Note**  
You can use Snowflake as a destination only.

**Topics**
+ [Requirements](#snowflake-requirements)
+ [Connection instructions](#snowflake-setup)
+ [Related resources](#snowflake-resources)

## Requirements
<a name="snowflake-requirements"></a>
+ Amazon AppFlow uses the Snowflake COPY command to move data using an S3 bucket. To configure the integration, see [Configuring Secure Access to Amazon S3](https://docs.snowflake.net/manuals/user-guide/data-load-s3-config.html) in the Snowflake documentation.
+ You must also add access to the `kms:Decrypt` action so that Snowflake can access the encrypted data that Amazon AppFlow stored in the Amazon S3 bucket.

  ```
  {
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "*"
  }
  ```
+ You must provide Amazon AppFlow with the following information:
  + the name of the stage and the S3 bucket for the stage
  + the user name and password for your Snowflake account
  + the S3 bucket prefix
  + the warehouse that you want to use to move the data

## Connection instructions
<a name="snowflake-setup"></a>

**To connect to Snowflake while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Snowflake** from the **Destination name** dropdown list.

1. Choose **Connect** or **Connect with PrivateLink** to open the **Connect to Snowflake** dialog box.

   1. Under **Warehouse**, enter the Snowflake warehouse that you want to use to move the data.

   1. Under **Stage name**, enter the Amazon S3 stage name in the following format: <Database> <Schema> <Stage name>

   1. Under **Bucket details**, select the S3 bucket where Amazon AppFlow will write data prior to copying it.

   1. Under **Account name**, enter your Snowflake account name. You can find your account name in the URL of your Snowflake instance. For example, if your Snowflake URL is https://vna33034.snowflakecomputing.com, your account name is vna33034.

   1. Under **User name**, enter the user name you use to log into Snowflake.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Connect**.  
![Snowflake connection form with fields for warehouse, stage, bucket, account, and other details.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-snowflake-console.png)

Now that you are connected to your Snowflake account, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#snowflake-requirements) section.

## Related resources
<a name="snowflake-resources"></a>
+ [Configuring Secure Access to Amazon S3](https://docs.snowflake.net/manuals/user-guide/data-load-s3-config.html) in the Snowflake documentation