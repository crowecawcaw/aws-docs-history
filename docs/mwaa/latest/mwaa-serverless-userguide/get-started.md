# Get started with Amazon MWAA Serverless

To create a workflow in Amazon MWAA Serverless you need an Amazon S3 Bucket and an Execution role. You can choose to provide optional KMS key, Amazon VPC and VPC Security groups.

- The **Amazon S3 bucket** stores your workflow files. Your Amazon S3 bucket must block all public access and have versioning enabled. When you upload workflow files, Amazon MWAA Serverless parses these files before scheduling tasks. To learn more, refer to [Create an Amazon S3 bucket for Amazon MWAA Serverless](mwaas-s3-bucket.md "mwaas-s3-bucket.md").
- **Execution role** enables Amazon MWAA Serverless workflow tasks to access your AWS resources. To learn more, refer to [Execution roles](get-started-execution-role.md "get-started-execution-role.md").
- (Optional) **KMS key** is used to encrypt your workflow data. If you do not provide a KMS key, Amazon MWAA Serverless will use a default key for encryption. To learn more, refer to [Using customer-managed keys for encryption](data-protection.md#data-protection-keys-certs "data-protection.md#data-protection-keys-certs").
- (Optional) **Amazon VPC** to connect to your private resources. If you don't provide a VPC, Amazon MWAA Serverless uses a default VPC with internet connectivity. To learn more, refer to [Create your Amazon VPC network](networking-vpc.md#networking-create-vpc "networking-vpc.md#networking-create-vpc").
- (Optional) **VPC security group** lets Amazon MWAA Serverless access other AWS resources in your VPC network. You can provide your security group information while creating a workflow. To learn more, refer to [Security in your VPC on Amazon MWAA Serverless](networking-security.md "networking-security.md").
  After you complete these steps, you're ready to use Amazon MWAA Serverless. Choose one of two paths:

- Initialize a workflow using the AWS CLI (you must first upload your YAML workflow file to your S3 bucket). For more information, refer to [Manage workflows](workflows.md#workflows-manage "workflows.md#workflows-manage").
- Migrate a Python DAG to YAML using [dag-converter](https://pypi.org/project/python-to-yaml-dag-converter-mwaa-serverless/ "https://pypi.org/project/python-to-yaml-dag-converter-mwaa-serverless/"). For more information, refer to [Convert Python DAG to YAML definition](workflows-migrate.md "workflows-migrate.md").
