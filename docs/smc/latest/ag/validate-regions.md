End of support notice: On March 31, 2027, AWS
will end support for AWS Service Management Connector. After March 31, 2027, you will
no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources.
For more information, see [AWS Service Management Connector end of support](smc-end-of-support.md "smc-end-of-support.md").

# Validating ServiceNow connectivity to AWS Regions

You can now validate connectivity to AWS accounts between the ServiceNow
**Connector\_Demo** account and the AWS IAM
`SMSyncUser` and `SMEndUser`.

###### To validate connectivity to AWS account

1. In the AWS Service Management scoped app, choose **Setup**, then **AWS Accounts**.
2. Choose **Connector\_Demo** and select **Validate
   Account**.

A successful connection results in the message, _Successfully validating AWS account in each referenced
Region_.
If the AWS IAM access key or secret access key are incorrect, you receive an
error message.
