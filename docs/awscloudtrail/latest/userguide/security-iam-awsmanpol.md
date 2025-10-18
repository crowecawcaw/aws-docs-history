# AWS managed policies for AWS CloudTrail

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
 than to write policies yourself. It takes time and expertise to [create IAM customer
 managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html") that provide your team with only the permissions they need. To get
 started quickly, you can use AWS managed policies. These policies cover common use cases
 and are available in your AWS account. For more information about AWS managed policies,
 see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the
 permissions in AWS managed policies. Services occasionally add additional permissions to an
 AWS managed policy to support new features. This type of update affects all identities
 (users, groups, and roles) where the policy is attached. Services are most likely to update an
 AWS managed policy when a new feature is launched or when new operations become available.
 Services do not remove permissions from an AWS managed policy, so policy updates won't
 break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
 services. For example, the **ReadOnlyAccess** AWS managed
 policy provides read-only access to all AWS services and resources. When a service launches
 a new feature, AWS adds read-only permissions for new operations and resources. For a list
 and descriptions of job function policies, see [AWS managed policies for
 job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html") in the *IAM User Guide*.


## AWS managed policy: `AWSCloudTrail_FullAccess`


A user identity that has the [AWSCloudTrail\_FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html") 
 policy attached to its role has full administrative access in CloudTrail.


For a JSON listing of the policy details, see [AWSCloudTrail\_FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html") in the *AWS Managed Policy reference guide*.


## AWS managed policy: `AWSCloudTrail_ReadOnlyAccess`


A user identity that has the [AWSCloudTrail\_ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_ReadOnlyAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_ReadOnlyAccess.html") policy attached to its role can perform read-only actions in CloudTrail, 
 such as `Get*`, `List*`, and `Describe*` actions on trails, CloudTrail Lake event data stores, or Lake queries.


For a JSON listing of the policy details, see [AWSCloudTrail\_ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_ReadOnlyAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_ReadOnlyAccess.html") in the *AWS Managed Policy reference guide*.


## AWS managed policy: `AWSServiceRoleForCloudTrail`


The [CloudTrailServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudTrailServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudTrailServiceRolePolicy.html") policy 
 allows AWS CloudTrail to perform actions on organization trails and organization event data stores on your behalf. The policy includes required 
 AWS Organizations permissions for describing and listing the organization accounts and delegated administrators in an AWS Organizations organization.


This policy additionally includes the required AWS Glue and AWS Lake Formation permissions to 
 [disable Lake federation](query-disable-federation.md "query-disable-federation.md") on an organization event data store.


This policy is attached to the **AWSServiceRoleForCloudTrail** service-linked role 
 that allows CloudTrail to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.


For a JSON listing of the policy details, see [CloudTrailServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudTrailServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudTrailServiceRolePolicy.html") in the *AWS Managed Policy reference guide*.


## AWS managed policy: `CloudTrailEventContext`


The [CloudTrailEventContext](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudTrailEventContext.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudTrailEventContext.html") policy 
 allows AWS CloudTrail to manage CloudTrail Event Context and EventBridge rules on your behalf. The policy includes required 
 EventBridge permissions for creating, managing, and describing the rules it creates for you.


This policy is attached to the **AWSServiceRoleForCloudTrailEventContext** service-linked role 
 that allows CloudTrail to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.


For a JSON listing of the policy details, see 
 [CloudTrailEventContext](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudTrailEventContext.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudTrailEventContext.html") 
 in the *AWS Managed Policy reference guide*.


## CloudTrail updates to AWS managed
 policies


View details about updates to AWS managed policies for CloudTrail. For automatic alerts
 about changes to this page, subscribe to the RSS feed on the CloudTrail [Document history](cloudtrail-document-history.md "cloudtrail-document-history.md")
 page.




| Change | Description | Date |
| --- | --- | --- |
| [CloudTrailEventContext](using-service-linked-roles-create-slr-for-context-management.md "using-service-linked-roles-create-slr-for-context-management.md") – New policy used by the `AWSServiceRoleForCloudTrailEventContext` service linked role | Added a new policy and role used for the CloudTrail enriched events feature. | May 19, 2025 |
| [CloudTrailServiceRolePolicy](#security-iam-awsmanpol-CloudTrailServiceRolePolicy "#security-iam-awsmanpol-CloudTrailServiceRolePolicy") – Update to an existing policy | Updated policy to allow the following actions on an organization event data store when federation is disabled: <br>• `glue:DeleteTable` <br>• `lakeformation:DeregisterResource` | November 26, 2023 |
| [AWSCloudTrail\_ReadOnlyAccess](#security-iam-awsmanpol-AWSCloudTrail-ReadOnlyAccess "#security-iam-awsmanpol-AWSCloudTrail-ReadOnlyAccess") – Update to an existing policy | CloudTrail changed the name of the `AWSCloudTrailReadOnlyAccess` policy to `AWSCloudTrail_ReadOnlyAccess`. Also, the scope of permissions in the policy has been reduced to CloudTrail actions. It no longer includes Amazon S3, AWS KMS, or AWS Lambda action permissions. | June 6, 2022 |
| CloudTrail started tracking changes | CloudTrail started tracking changes for its AWS managed policies. | June 6, 2022 |
