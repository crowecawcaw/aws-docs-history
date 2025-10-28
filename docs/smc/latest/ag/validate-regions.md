# Validating ServiceNow connectivity to AWS Regions

You can now validate connectivity to AWS accounts between the ServiceNow
**Connector_Demo** account and the AWS IAM
`SMSyncUser` and `SMEndUser`.

###### To validate connectivity to AWS account

1. In the AWS Service Management scoped app, choose **Setup**, then **AWS Accounts**.
2. Choose **Connector_Demo** and select **Validate
   Account**.

A successful connection results in the message, _Successfully validating AWS account in each referenced
Region_.
If the AWS IAM access key or secret access key are incorrect, you receive an
error message.
