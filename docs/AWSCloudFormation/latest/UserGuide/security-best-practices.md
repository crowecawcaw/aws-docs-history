# Security best practices for CloudFormation

CloudFormation provides a number of security features to consider as you develop and implement your
own security policies. The following best practices are general guidelines and don’t
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

###### Topics

- [Use IAM to control access](#use-iam-to-control-access "#use-iam-to-control-access")
- [Do not embed credentials in your templates](#creds "#creds")
- [Use AWS CloudTrail to log CloudFormation calls](#cloudtrail "#cloudtrail")

## Use IAM to control access

IAM is an AWS service that you can use to manage users and their permissions in
AWS. You can use IAM with CloudFormation to specify what CloudFormation actions users can
perform, such as viewing stack templates, creating stacks, or deleting stacks.
Furthermore, anyone managing CloudFormation stacks will require permissions to resources
within those stacks. For example, if users want to use CloudFormation to launch, update, or
terminate Amazon EC2 instances, they must have permission to call the relevant Amazon EC2
actions.

In most cases, users require full access to manage all of the resources in a template.
CloudFormation makes calls to create, modify, and delete those resources on their behalf. To
separate permissions between a user and the CloudFormation service, use a service role.
CloudFormation uses the service role's policy to make calls instead of the user's policy.
For more information, see [CloudFormation service role](using-iam-servicerole.md "using-iam-servicerole.md").

## Do not embed credentials in your templates

Rather than embedding sensitive information in your CloudFormation templates, we recommend
you use _dynamic references_ in your stack template.

Dynamic references provide a compact, powerful way for you to reference external
values that are stored and managed in other services, such as the AWS Systems Manager
Parameter Store or AWS Secrets Manager. When you use a dynamic reference, CloudFormation
retrieves the value of the specified reference when necessary during stack and change
set operations, and passes the value to the appropriate resource. However, CloudFormation
never stores the actual reference value. For more information, see [Get values stored in other services using dynamic
references](dynamic-references.md "dynamic-references.md").

[AWS
Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") helps you to securely encrypt, store, and retrieve
credentials for your databases and other services. The [AWS
Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") provides secure, hierarchical storage for
configuration data management.

For more information on defining template parameters, see [CloudFormation template Parameters
syntax](parameters-section-structure.md "parameters-section-structure.md").

## Use AWS CloudTrail to log CloudFormation calls

AWS CloudTrail tracks anyone making CloudFormation API calls in your AWS account. API calls
are logged whenever anyone uses the CloudFormation API, the CloudFormation console, a back-end
console, or CloudFormation AWS CLI commands. Enable logging and specify an Amazon S3 bucket to
store the logs. That way, if you ever need to, you can audit who made what CloudFormation
call in your account. For more information, see [Logging CloudFormation API calls with AWS CloudTrail](cfn-api-logging-cloudtrail.md "cfn-api-logging-cloudtrail.md").
