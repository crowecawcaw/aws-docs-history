# Limitations

The following features and functionality currently aren't supported by the AMS CloudFormation
ingest process.

- **YAML** – Not supported. Only JSON-based CloudFormation
  templates are supported.
- **Nested stacks** – Instead, architect your application
  infrastructure to use a single template. Or, alternatively you can make use of cross-stack
  referencing to separate resources across multiple stacks where one resource has a dependency
  on another. For more information, see [Walkthrough:
  Refer to Resource Outputs in Another AWS CloudFormation Stack](../../../AWSCloudFormation/latest/UserGuide/walkthrough-crossstackref.md "../../../AWSCloudFormation/latest/UserGuide/walkthrough-crossstackref.md").
- **CloudFormation stack sets** – Not supported, due to
  security implications.
- **IAM resource creation using CloudFormation templates** –

Only IAM roles are supported, due to security implications.

- **Sensitive data** – Not supported. Do not include
  sensitive data in the template or in the parameter values. If you need to reference
  sensitive data, use Secrets Manager to store and retrieve these values. For information
  about using AWS Secrets Managers secrets in a resource property, see [How to create and retrieve secrets managed in AWS Secrets Manager using AWS
  CloudFormation templates](https://aws.amazon.com/blogs/security/how-to-create-and-retrieve-secrets-managed-in-aws-secrets-manager-using-aws-cloudformation-template/ "https://aws.amazon.com/blogs/security/how-to-create-and-retrieve-secrets-managed-in-aws-secrets-manager-using-aws-cloudformation-template/") and [Using Dynamic References
  to Specify Template Values](../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md "../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md").
