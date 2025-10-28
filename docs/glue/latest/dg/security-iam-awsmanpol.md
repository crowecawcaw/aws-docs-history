# Granting AWS managed policies for AWS Glue

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed (predefined) policies for

AWS Glue

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. These AWS managed policies grant necessary permissions
for common use cases so that you can avoid having to investigate what permissions are
needed. For more information, see [AWS
managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to identities in your
account, are specific to AWS Glue and are grouped by use case scenario:

- [AWSGlueConsoleFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess") – Grants full access to
  AWS Glue resources when an identity that the policy is attached to
  uses the AWS Management Console. If you follow the naming convention for resources specified in
  this policy, users have full console capabilities. This policy is typically attached
  to users of the AWS Glue console.
- [AWSGlueServiceRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole") – Grants access to resources that various
  AWS Glue processes require to run on your behalf. These resources include
  AWS Glue, Amazon S3, IAM, CloudWatch Logs, and Amazon EC2. If you follow the naming
  convention for resources specified in this policy, AWS Glue processes have
  the required permissions. This policy is typically attached to roles specified when
  defining crawlers, jobs, and development endpoints.
- [AwsGlueSessionUserRestrictedServiceRole](https://console.aws.amazon.com/iam/home#policies/details/arn:aws:iam::aws:policy%2Fservice-role%2FAwsGlueSessionUserRestrictedServiceRole "https://console.aws.amazon.com/iam/home#policies/details/arn:aws:iam::aws:policy%2Fservice-role%2FAwsGlueSessionUserRestrictedServiceRole") – Provides full access to
  all AWS Glue resources except for sessions. It allows users to create and
  use only the interactive sessions that are associated with the user. This policy
  includes other permissions needed by AWS Glue to manage
  AWS Glue resources in other AWS services. The policy also allows
  adding tags to AWS Glue resources in other AWS services.

###### Note

To achieve the full security benefits, do not grant this policy to a user that was
assigned the `AWSGlueServiceRole`, `AWSGlueConsoleFullAccess`,
or `AWSGlueConsoleSageMakerNotebookFullAccess` policy.

- [AwsGlueSessionUserRestrictedPolicy](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AwsGlueSessionUserRestrictedPolicy "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AwsGlueSessionUserRestrictedPolicy") – Provides access to create
  AWS Glue interactive sessions using the `CreateSession` API
  operation only if a tag key “owner” and value that match the assignee's AWS user ID
  are provided. This identity policy is attached to the IAM user that invokes the
  `CreateSession` API operation. This policy also permits the assignee to
  interact with the AWS Glue interactive session resources that were
  created with an “owner” tag and value that match their AWS user ID. This policy
  denies permission to change or remove "owner" tags from an AWS Glue
  session resource after the session is created.

###### Note

To achieve the full security benefits, do not grant this policy to a user that was
assigned the `AWSGlueServiceRole`, `AWSGlueConsoleFullAccess`,
or `AWSGlueConsoleSageMakerNotebookFullAccess` policy.

- [AwsGlueSessionUserRestrictedNotebookServiceRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AwsGlueSessionUserRestrictedNotebookServiceRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AwsGlueSessionUserRestrictedNotebookServiceRole") – Provides
  sufficient access to the AWS Glue Studio notebook session to interact with
  specific AWS Glue interactive session resources. These are resources that
  are created with the “owner” tag value that matches the AWS user ID of the
  principal (IAM user or role) that creates the notebook. For more information about
  these tags, see the [Principal key values](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse") chart in the
  _IAM User Guide_.

This service-role policy is attached to the role that is specified with a magic
command within the notebook or is passed as a role to the `CreateSession`
API operation. This policy also permits the principal to create an
AWS Glue interactive session from the AWS Glue Studio notebook
interface only if a tag key “owner” and value match the AWS user ID of the
principal. This policy denies permission to change or remove "owner" tags from an
AWS Glue session resource after the session is created. This policy
also includes permissions for writing and reading from Amazon S3 buckets,
writing CloudWatch logs, and creating and deleting tags for Amazon EC2 resources used by
AWS Glue.

###### Note

To achieve the full security benefits, do not grant this policy to a role that was
assigned the `AWSGlueServiceRole`, `AWSGlueConsoleFullAccess`,
or `AWSGlueConsoleSageMakerNotebookFullAccess` policy.

- [AwsGlueSessionUserRestrictedNotebookPolicy](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AwsGlueSessionUserRestrictedNotebookPolicy "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AwsGlueSessionUserRestrictedNotebookPolicy") – Provides access to
  create an AWS Glue interactive session from the AWS Glue Studio
  notebook interface only if there is a tag key “owner” and value that match the AWS
  user IDof the principal (IAM user or role) that creates the notebook. For more
  information about these tags, see the [Principal key values](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse") chart in the
  _IAM User Guide_.

This policy is attached to the principal (IAM user or role) that creates
sessions from the AWS Glue Studio notebook interface. This policy also permits
sufficient access to the AWS Glue Studio notebook to interact with specific
AWS Glue interactive session resources. These are resources that are
created with the “owner” tag value that matches the AWS user ID of the principal.
This policy denies permission to change or remove "owner" tags from an
AWS Glue session resource after the session is created.

- [AWSGlueServiceNotebookRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceNotebookRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceNotebookRole") – Grants access to AWS Glue
  sessions started in an AWS Glue Studio notebook. This policy allows listing and
  getting session information for all sessions, but only permits users to create and
  use the sessions tagged with their AWS user ID. This policy denies permission to
  change or remove “owner” tags from AWS Glue session resources tagged with
  their AWS ID.

Assign this policy to the AWS user who creates jobs using the notebook interface
in AWS Glue Studio.

- [AWSGlueConsoleSageMakerNotebookFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleSageMakerNotebookFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleSageMakerNotebookFullAccess") – Grants full access to
  AWS Glue and SageMaker AI resources when the identity that the policy is attached to uses the
  AWS Management Console. If you follow the naming convention for resources specified in this
  policy, users have full console capabilities. This policy is typically attached to
  users of the AWS Glue console who manage SageMaker AI notebooks.
- [AWSGlueSchemaRegistryFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueSchemaRegistryFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueSchemaRegistryFullAccess") – Grants full access to
  AWS Glue Schema Registry resources when the identity that the policy
  is attached to uses the AWS Management Console or AWS CLI. If you follow the naming convention for
  resources specified in this policy, users have full console capabilities. This policy
  is typically attached to users of the AWS Glue console or AWS CLI who
  manage the AWS Glue Schema Registry.
- [AWSGlueSchemaRegistryReadonlyAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueSchemaRegistryReadonlyAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueSchemaRegistryReadonlyAccess") – Grants read-only access to
  AWS Glue Schema Registry resources when an identity that the policy is
  attached to uses the AWS Management Console or AWS CLI. If you follow the naming convention for
  resources specified in this policy, users have full console capabilities. This policy
  is typically attached to users of the AWS Glue console or AWS CLI who use
  the AWS Glue Schema Registry.

###### Note

You can review these permissions policies by signing in to the IAM console and
searching for specific policies there.

You can also create your own custom IAM policies to allow permissions for
AWS Glue actions and resources. You can attach these custom policies to the IAM users
or groups that require those permissions.

To create a connection with VPC configuration while using a custom IAM role, it must have the following VPC access actions:

- secretsmanager:GetSecretValue
- secretsmanager:PutSecretValue
- secretsmanager:DescribeSecret
- ec2:CreateNetworkInterface
- ec2:DeleteNetworkInterface
- ec2:DescribeNetworkInterfaces
- ec2:DescribeSubnets

## AWS Glue updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Glue since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS Glue Document history page.

| Change                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                         | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| AwsGlueSessionUserRestrictedNotebookPolicy – Minor update to an existing policy.                                                                                                                                                                               | Add allow for `glue:TagResource` action on the owner tag key. Required for supporting on tag-on-create for sessions with owner tag key.                                                                                                                                                                                                                                                             | August 30, 2024   |
| AwsGlueSessionUserRestrictedNotebookServiceRole – Minor update to an existing policy.                                                                                                                                                                          | Add allow for `glue:TagResource` action on the owner tag key. Required for supporting on tag-on-create for sessions with owner tag key.                                                                                                                                                                                                                                                             | August 30, 2024   |
| AwsGlueSessionUserRestrictedPolicy – Minor update to an existing policy.                                                                                                                                                                                       | Add allow for `glue:TagResource` action on the owner tag key. Required for supporting on tag-on-create for sessions with owner tag key.                                                                                                                                                                                                                                                             | August 5, 2024    |
| AwsGlueSessionUserRestrictedServiceRole – Minor update to an existing policy.                                                                                                                                                                                  | Add allow for `glue:TagResource` action on the owner tag key. Required for supporting on tag-on-create for sessions with owner tag key.                                                                                                                                                                                                                                                             | August 5, 2024    |
| AwsGlueSessionUserRestrictedPolicy – Minor update to an existing policy.                                                                                                                                                                                       | Add `glue:StartCompletion` and `glue:GetCompletion` to policy. Required for Amazon Q data integration in AWS Glue.                                                                                                                                                                                                                                                                                  | April 30, 2024    |
| AwsGlueSessionUserRestrictedNotebookServiceRole – Minor update to an existing policy.                                                                                                                                                                          | Add `glue:StartCompletion` and `glue:GetCompletion` to policy. Required for Amazon Q data integration in AWS Glue.                                                                                                                                                                                                                                                                                  | April 30, 2024    |
| AwsGlueSessionUserRestrictedServiceRole – Minor update to an existing policy.                                                                                                                                                                                  | Add `glue:StartCompletion` and `glue:GetCompletion` to policy. Required for Amazon Q data integration in AWS Glue.                                                                                                                                                                                                                                                                                  | April 30, 2024    |
| AWSGlueServiceNotebookRole – Minor update to an existing policy.                                                                                                                                                                                               | Add `glue:StartCompletion` and `glue:GetCompletion` to policy. Required for Amazon Q data integration in AWS Glue.                                                                                                                                                                                                                                                                                  | Jan 30, 2024      |
| AwsGlueSessionUserRestrictedNotebookPolicy – Minor update to an existing policy.                                                                                                                                                                               | Add `glue:StartCompletion` and `glue:GetCompletion` to policy. Required for Amazon Q data integration in AWS Glue.                                                                                                                                                                                                                                                                                  | Nov 29, 2023      |
| AWSGlueServiceNotebookRole – Minor update to an existing policy.                                                                                                                                                                                               | Add `codewhisperer:GenerateRecommendations` to policy. Required for a new feature where AWS Glue generates CodeWhisperer recommendations.                                                                                                                                                                                                                                                           | Oct 9, 2023       |
| AWSGlueServiceRole – Minor update to an existing policy.                                                                                                                                                                                                       | Tighten scope of CloudWatch permissions to better reflect AWS Glue logging.                                                                                                                                                                                                                                                                                                                         | Aug 4, 2023       |
| AWSGlueConsoleFullAccess – Minor update to an existing policy.                                                                                                                                                                                                 | Add `databrew` recipe List and Describe permissions to policy. Required to provide full administrative access for new features where AWS Glue can access recipes.                                                                                                                                                                                                                                   | May 9, 2023       |
| AWSGlueConsoleFullAccess – Minor update to an existing policy.                                                                                                                                                                                                 | Add `cloudformation:ListStacks` to policy. Preserves existing capabilities after changes to AWS CloudFormation authorization requirements.                                                                                                                                                                                                                                                          | March 28, 2023    |
| New managed policies added for the interactive sessions feature: <br>• AwsGlueSessionUserRestrictedServiceRole <br>• AwsGlueSessionUserRestrictedPolicy <br>• AwsGlueSessionUserRestrictedNotebookServiceRole <br>• AwsGlueSessionUserRestrictedNotebookPolicy | These policies were designed to provide additional security for interactive sessions and notebooks in AWS Glue Studio. The policies restrict access to the `CreateSession` API operation so that only the owner has access.                                                                                                                                                                         | November 30, 2021 |
| AWSGlueConsoleSageMakerNotebookFullAccess – Update to an existing policy.                                                                                                                                                                                      | Removed a redundant resource ARN (`arn:aws:s3:::aws-glue-*/*`) for the action that grants read/write permissions on Amazon S3 buckets that AWS Glue uses to store scripts and temporary files. Fixed a syntax issue by changing `"StringEquals"` to `"ForAnyValue:StringLike"`, and moved the `"Effect": "Allow"` lines to precede the `"Action":` line in each place where they were out of order. | July 15, 2021     |
| AWSGlueConsoleFullAccess – Update to an existing policy.                                                                                                                                                                                                       | Removed a redundant resource ARN (`arn:aws:s3:::aws-glue-*/*`) for the action that grants read/write permissions on Amazon S3 buckets that AWS Glue uses to store scripts and temporary files.                                                                                                                                                                                                      | July 15, 2021     |
| AWS Glue started tracking changes.                                                                                                                                                                                                                             | AWS Glue started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                     | June 10, 2021     |
