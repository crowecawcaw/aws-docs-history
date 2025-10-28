# Step 4: Install AWS SCT on Your Local Computer

In this step, you install and configure the AWS Schema Conversion Tool. In this walkthrough, we run AWS SCT and the data extraction agent on Windows. However, you can use AWS SCT and data extraction agents on other supported operating systems. For more information, see [Installing the schema conversion tool](../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md#CHAP_Installing.Procedure "../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md#CHAP_Installing.Procedure") and [Installing extraction agents](../../../SchemaConversionTool/latest/userguide/agents.md#agents.Installing "../../../SchemaConversionTool/latest/userguide/agents.md#agents.Installing").

**To install AWS SCT**

1. Download the compressed file that contains AWS SCT installer for Microsoft Windows from [https://s3.amazonaws.com/publicsctdownload/Windows/aws-schema-conversion-tool-1.0.latest.zip](https://s3.amazonaws.com/publicsctdownload/Windows/aws-schema-conversion-tool-1.0.latest.zip "https://s3.amazonaws.com/publicsctdownload/Windows/aws-schema-conversion-tool-1.0.latest.zip").
2. Extract AWS SCT installer file.
3. Run AWS SCT installer file that you extracted in the previous step.
4. Choose **Next**, accept the terms of the License Agreement, and choose **Next** again.
5. Enter the path to the folder where you want to install AWS SCT, and choose **Next**.
6. Choose **Install**.
7. Choose **Finish** to close the installation wizard.
   Now you can run AWS SCT. Before you create a new project, make sure that you add the path to an Amazon Redshift JDBC driver in the application settings. You don’t need a JDBC driver to connect to your BigQuery project.

**To configure driver settings in AWS SCT**

1. Download an Amazon Redshift JDBC driver version 2.1.0.9 or later from [https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-download-driver.html](../../../redshift/latest/mgmt/jdbc20-download-driver.md "../../../redshift/latest/mgmt/jdbc20-download-driver.md").
2. Extract the JDBC driver from the compressed file that you downloaded.
3. Open AWS SCT, and choose **Global settings** from **Settings**.
4. Choose **Drivers**.
5. For **Amazon Redshift driver path**, choose Browse and choose the `redshift-jdbc42-2.1.0.9.jar` file that you extracted.
6. Choose **Apply**, and then choose **OK** to close the settings window.
   To access AWS services such as Amazon S3 from AWS SCT, you configure an AWS service profile. An AWS service profile is a set of AWS credentials that includes your AWS access key, AWS secret access key, AWS Region, and Amazon S3 bucket.

**To create an AWS service profile in AWS SCT**

1. Open AWS SCT, and choose **Global settings** from **Settings**.
2. Choose **AWS service profiles**.
3. Choose **Add a new AWS service profile**.
4. For **Profile name**, enter a descriptive name for your profile.
5. For **AWS access key**, enter your AWS access key.
6. For **AWS secret key**, enter your AWS secret access key. For more information about AWS access keys, see [Programmatic access](../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys "../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys").
7. For **Region**, choose the AWS Region where you created your Amazon S3 bucket in the previous step.
8. For **Amazon S3 bucket folder**, choose the Amazon S3 bucket that you created in the previous step.
9. Choose **Apply**, and then choose **OK** to close the settings window.
