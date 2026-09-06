

End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October 7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure will remain intact. For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# AWS managed policies for AWS Proton
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

AWS Proton provides managed IAM policies and trust relationships that you can attach to users, groups, or roles that allow differing levels of control over resources and API operations. You can apply these policies directly, or you can use them as starting points for creating your own policies.

The following trust relationship is used for each of the AWS Proton managed policies.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": {
    "Sid": "ExampleTrustRelationshipWithProtonConfusedDeputyPrevention",
    "Effect": "Allow",
    "Principal": {
      "Service": "proton.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
      "StringEquals": {
        "aws:SourceAccount": "{{123456789012}}"
      },
      "ArnLike": {
        "aws:SourceArn": "arn:aws:proton:*:{{123456789012}}:environment/*"
      }
    }
  }
}
```

------

## AWS managed policy: AWSProtonFullAccess
<a name="security-iam-awsmanpol-AWSProtonFullAccess"></a>

You can attach `AWSProtonFullAccess` to your IAM entities. AWS Proton also attaches this policy to a service role that allows AWS Proton to perform actions on your behalf. 

This policy grants administrative permissions that allow full access to AWS Proton actions and limited access to other AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:
+ `proton` – Allows administrators full access to AWS Proton APIs.
+ `iam` – Allows administrators to pass roles to AWS Proton. This is required so that AWS Proton can make API calls to other services on the administrator's behalf.
+ `kms` – Allows administrators to add a grant to a customer managed key.
+ `codeconnections` – Allows administrators to list and pass codeconnections so they can be used by AWS Proton.

For more information, see [AWSProtonFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSProtonFullAccess.html).

## AWS managed policy: AWSProtonDeveloperAccess
<a name="security-iam-awsmanpol-AWSProtonDeveloperAccess"></a>

You can attach `AWSProtonDeveloperAccess` to your IAM entities. AWS Proton also attaches this policy to a service role that allows AWS Proton to perform actions on your behalf.

This policy grants permissions that allow limited access to AWS Proton actions and to other AWS actions that AWS Proton depends on. The scope of these permissions is designed to support the role of a developer who creates and deploys AWS Proton services.

This policy doesn't provide access to AWS Proton template and environment *create, delete and update* APIs. If developers need even more limited permissions than what this policy provides, we recommend creating a custom policy that is scoped down to grant the [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).

The policy includes the following key action namespaces:
+ `proton` – Allows contributors access to a limited set of AWS Proton APIs.
+ `codeconnections` – Allows contributors to list and pass codeconnections so they can be used by AWS Proton.

For more information, see [AWSProtonDeveloperAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSProtonDeveloperAccess.html).

## AWS managed policy: AWSProtonReadOnlyAccess
<a name="security-iam-awsmanpol-AWSProtonReadOnlyAccess"></a>

You can attach `AWSProtonReadOnlyAccess` to your IAM entities. AWS Proton also attaches this policy to a service role that allows AWS Proton to perform actions on your behalf. 

This policy grants permissions that allow read-only access to AWS Proton actions and limited read-only access to other AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:
+ `proton` – Allows contributors read-only access to AWS Proton APIs.

For more information, see [AWSProtonReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSProtonReadOnlyAccess.html).

## AWS managed policy: AWSProtonSyncServiceRolePolicy
<a name="security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy"></a>

AWS Proton attaches this policy to the [AWSServiceRoleForProtonSync](using-service-linked-roles-sync.md) service-linked role that allows AWS Proton to perform template sync.

This policy grants permissions that allow limited access to AWS Proton actions and to other AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:
+ `proton` – Allows AWS Proton sync limited access to AWS Proton APIs.
+ `codeconnections` – Allows AWS Proton sync limited access to CodeConnections APIs.

For more information, see [AWSProtonSyncServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSProtonSyncServiceRolePolicy.html).

## AWS managed policy: AWSProtonCodeBuildProvisioningBasicAccess
<a name="security-iam-awsmanpol-AWSProtonCodeBuildProvisioningBasicAccess"></a>

Permissions CodeBuild needs to run a build for AWS Proton CodeBuild Provisioning. You can attach `AWSProtonCodeBuildProvisioningBasicAccess` to your CodeBuild Provisioning Role. 

This policy grants the minimum permissions for AWS Proton CodeBuild Provisioning to function. It grants permissions that allow CodeBuild to generate build logs. It also grants permission for Proton to make Infrastructure as Code (IaC) outputs available to AWS Proton users. It does not provide permissions needed by IaC tools to manage infrastructure.

The policy includes the following key action namespaces:
+ `logs` ‐ Allows CodeBuild to generate build logs. Without this permission, CodeBuild will fail to start.
+ `proton` ‐ Allows a CodeBuild Provisioning command to call `aws proton notify-resource-deployment-status-change` for updating the IaaC outputs for a given AWS Proton resource.

For more information, see [AWSProtonCodeBuildProvisioningBasicAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSProtonCodeBuildProvisioningBasicAccess.html).

## AWS managed policy: AWSProtonCodeBuildProvisioningServiceRolePolicy
<a name="security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy"></a>

AWS Proton attaches this policy to the [AWSServiceRoleForProtonCodeBuildProvisioning](using-service-linked-roles-codebuild.md) service-linked role that allows AWS Proton to perform CodeBuild-based provisioning.

This policy grants permissions that allow limited access to AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:
+ `cloudformation` – Allows AWS Proton CodeBuild-based provisioning limited access to CloudFormation APIs.
+ `codebuild` – Allows AWS Proton CodeBuild-based provisioning limited access to CodeBuild APIs.
+ `iam` – Allows administrators to pass roles to AWS Proton. This is required so that AWS Proton can make API calls to other services on the administrator's behalf.
+ `servicequotas` – Allows AWS Proton to check the CodeBuild concurrent build limit, which ensures proper build queuing.

For more information, see [AWSProtonCodeBuildProvisioningServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSProtonCodeBuildProvisioningServiceRolePolicy.html).

## AWS managed policy: AWSProtonServiceGitSyncServiceRolePolicy
<a name="security-iam-awsmanpol-AwsProtonServiceGitSyncServiceRolePolicy"></a>

AWS Proton attaches this policy to the [AWSServiceRoleForProtonServiceSync](using-service-linked-roles-sync.md) service-linked role that allows AWS Proton to perform service sync.

This policy grants permissions that allow limited access to AWS Proton actions and to other AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:
+ `proton` – Allows AWS Proton sync limited access to AWS Proton APIs.

For more information, see [AWSProtonServiceGitSyncServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSProtonServiceGitSyncServiceRolePolicy.html).

## AWS Proton updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Proton since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Proton Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
|  [AWSProtonCodeBuildProvisioningServiceRolePolicy](#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy) – Update to an existing policy | The managed policy for the service-linked role that allows AWS Proton to perform CodeBuild-based provisioning now grants permissions to call the CloudFormation `TagResource` and `UntagResource` API actions. These permissions are required to perform tagging operations on resources. | June 15, 2024 | 
| [AWSProtonFullAccess](#security-iam-awsmanpol-AWSProtonFullAccess) – Update to an existing policy | The managed policy for the service-linked role to use Git sync with Git repositories has been updated for resources with both service prefixes. For more information, see [Using service-linked roles for AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/what-is-dtconsole.html) and [Managed policies](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam-awsmanpol.html). | April 25, 2024 | 
| [AWSProtonDeveloperAccess](#security-iam-awsmanpol-AWSProtonDeveloperAccess) – Update to an existing policy | The managed policy for the service-linked role to use Git sync with Git repositories has been updated for resources with both service prefixes. For more information, see [Using service-linked roles for AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/what-is-dtconsole.html) and [Managed policies](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam-awsmanpol.html). | April 25, 2024 | 
| [AWSProtonSyncServiceRolePolicy](#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy) – Update to an existing policy | The managed policy for the service-linked role to use Git sync with Git repositories has been updated for resources with both service prefixes. For more information, see [Using service-linked roles for AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/what-is-dtconsole.html) and [Managed policies](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam-awsmanpol.html). | April 25, 2024 | 
| [AWSProtonCodeBuildProvisioningServiceRolePolicy](#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy) – Update to an existing policy | AWS Proton updated this policy to add permissions to ensure accounts have the necessary CodeBuild concurrent build limit in order to use CodeBuild Provisioning. | May 12, 2023 | 
| [AWSProtonServiceGitSyncServiceRolePolicy](#security-iam-awsmanpol-AwsProtonServiceGitSyncServiceRolePolicy) – New policy | AWS Proton added a new policy to allow AWS Proton to perform service syncing. The policy is used in the [AWSServiceRoleForProtonServiceSync](https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles-sync.html#service-linked-role-permissions-sync) service-linked role. | March 31, 2023 | 
| [AWSProtonDeveloperAccess](#security-iam-awsmanpol-AWSProtonDeveloperAccess) – Update to an existing policy | AWS Proton added a new `GetResourcesSummary` action that allows you to view a summary of your templates, deployed template resources, and out of date resources. | November 18, 2022 | 
| [AWSProtonReadOnlyAccess](#security-iam-awsmanpol-AWSProtonReadOnlyAccess) – Update to an existing policy | AWS Proton added a new `GetResourcesSummary` action that allows you to view a summary of your templates, deployed template resources, and out of date resources. | November 18, 2022 | 
| [AWSProtonCodeBuildProvisioningBasicAccess](#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningBasicAccess) – New policy | AWS Proton added a new policy that gives CodeBuild the permissions it needs to run a build for AWS Proton CodeBuild Provisioning. | November 16, 2022 | 
| [AWSProtonSyncServiceRolePolicy](#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy) – New policy | AWS Proton added a new policy to allow AWS Proton to perform operations related to CodeBuild-based provisioning. The policy is used in the [AWSServiceRoleForProtonCodeBuildProvisioning](using-service-linked-roles-codebuild.md) service-linked role. | September 02, 2022 | 
| [AWSProtonFullAccess](#security-iam-awsmanpol-AWSProtonFullAccess) – Update to an existing policy | AWS Proton updated this policy to provide access to new AWS Proton API operations and to fix permission issues for some AWS Proton console operations. | March 30, 2022 | 
|  [AWSProtonDeveloperAccess](#security-iam-awsmanpol-AWSProtonDeveloperAccess) – Update to an existing policy | AWS Proton update this policy to provide access to new AWS Proton API operations and to fix permission issues for some AWS Proton console operations. | March 30, 2022 | 
| [AWSProtonReadOnlyAccess](#security-iam-awsmanpol-AWSProtonReadOnlyAccess) – Update to an existing policy | AWS Proton update this policy to provide access to new AWS Proton API operations and to fix permission issues for some AWS Proton console operations. | March 30, 2022 | 
| [AWSProtonSyncServiceRolePolicy](#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy) – New policy | AWS Proton added a new policy to allow AWS Proton to perform operations related to template sync. The policy is used in the [AWSServiceRoleForProtonSync](using-service-linked-roles.md) service-linked role. | November 23, 2021 | 
| [AWSProtonFullAccess](#security-iam-awsmanpol-AWSProtonFullAccess) – New policy | AWS Proton added a new policy to provide administrative role access to AWS Proton API operations and to the AWS Proton console. | June 09, 2021 | 
| [AWSProtonDeveloperAccess](#security-iam-awsmanpol-AWSProtonDeveloperAccess) – New policy | AWS Proton added a new policy to provide developer role access to AWS Proton API operations and to the AWS Proton console. | June 09, 2021 | 
| [AWSProtonReadOnlyAccess](#security-iam-awsmanpol-AWSProtonReadOnlyAccess) – New policy | AWS Proton added a new policy to provide read-only access to AWS Proton API operations and to the AWS Proton console. | June 09, 2021 | 
| AWS Proton started tracking changes. | AWS Proton started tracking changes for its AWS managed policies. | June 09, 2021 | 