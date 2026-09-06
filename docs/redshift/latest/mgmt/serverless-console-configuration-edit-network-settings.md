

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Editing security and encryption
<a name="serverless-console-configuration-edit-network-settings"></a>

Amazon Redshift Serverless is secured by means of KMS encryption. You can update encryption settings via the console:

1. Choose **Namespace configuration** from the main menu on the console, choose the namespace to edit, and choose **Edit** on the **Security and encryption** tab. A dialog appears.

1. You can select **Customize encryption settings** and then **Choose an AWS customer managed key** to change the key used to encrypt your resources.

1. For **Audit logging**, choose the logs to export. Each log type specifies different metadata.

1. To complete the configuration update, choose **Save changes**.