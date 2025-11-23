End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Security best practices for AWS Proton

AWS Proton provides security features to consider as you develop and implement your own security policies. The following best practices are
general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for
your environment, treat them as helpful considerations rather than prescriptions.

###### Topics

- [Use IAM to control access](#use-iam-to-control-access "#use-iam-to-control-access")
- [Do not embed credentials in your templates and template bundles](#creds "#creds")
- [Use encryption to protect sensitive data](#encryption "#encryption")
- [Use AWS CloudTrail to view and log API calls](#cloudtrail "#cloudtrail")

## Use IAM to control access

IAM is an AWS service that you can use to manage users and their permissions in AWS. You can use IAM with AWS Proton to specify which
AWS Proton actions administrators and developers can perform, such as managing templates, environments or services. You can use IAM service
roles to allow AWS Proton to make calls to other services on your behalf.

For more information on AWS Proton and IAM roles, see [Identity and Access Management for AWS Proton](security-iam.md "security-iam.md").

Implement least privilege access. For more information, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _AWS Identity and Access Management User Guide_.

## Do not embed credentials in your templates and template bundles

Rather than embedding sensitive information in your CloudFormation templates and template bundles, we recommend you use _dynamic
references_ in your stack template.

Dynamic references provide a compact, powerful way for you to reference external values that are stored and managed in other services,
such as the AWS Systems Manager Parameter Store or AWS Secrets Manager. When you use a dynamic reference, CloudFormation retrieves the value of the
specified reference when necessary during stack and change set operations, and passes the value to the appropriate resource. However,
CloudFormation never stores the actual reference value. For more information, see [Using Dynamic References to Specify Template Values](../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md "../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md") in the
_CloudFormation User Guide_.

[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") helps you to securely encrypt,
store, and retrieve credentials for your databases and other services. The [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") provides secure,
hierarchical storage for configuration data management.

For more information on defining template parameters, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html](../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md") in the _CloudFormation User Guide_.

## Use encryption to protect sensitive data

Within AWS Proton, all customer data is encrypted by default using an AWS Proton owned key.

As a member of the platform team, you can provide a customer managed key to AWS Proton to encrypt and secure your sensitive data. Encrypt
sensitive data at rest in your S3 bucket. For more information, see [Data protection in AWS Proton](data-protection.md "data-protection.md").

## Use AWS CloudTrail to view and log API calls

AWS CloudTrail tracks anyone making API calls in your AWS account. API calls are logged whenever anyone uses the AWS Proton API, the AWS Proton
console or AWS Proton AWS CLI commands. Enable logging and specify an Amazon S3 bucket to store the logs. That way, if you need to, you can audit
who made what AWS Proton call in your account. For more information, see [Logging and monitoring in AWS Proton](security-logging-and-monitoring.md "security-logging-and-monitoring.md").
