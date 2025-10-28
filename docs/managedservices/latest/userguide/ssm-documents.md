# AWS Systems Manager in AMS Advanced

An AWS Systems Manager document (SSM document) defines the actions that Systems Manager performs on your AWS resources. Systems Manager
includes more than a dozen pre-configured documents that you can use by specifying parameters at runtime. Documents
use JavaScript Object Notation (JSON) or YAML, and they include steps and parameters that you specify.

AWS Managed Services (AMS) is a trusted publisher for SSM documents. SSM documents owned by AMS are shared only with onboarded AMS accounts,
always begin with a reserved prefix (AWSManagedServices-\*), and show up in the Systems Manager console, as owned by AWS. The AMS process for
SSM document development and publishing follows AWS best practices and requires multiple peer reviews throughout the document life cycle.
For more information on AWS best practices for sharing SSM documents, see
[Best practices for shared SSM documents](../../../systems-manager/latest/userguide/ssm-before-you-share.md "../../../systems-manager/latest/userguide/ssm-before-you-share.md").
