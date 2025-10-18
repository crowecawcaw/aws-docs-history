# AWS managed policies for AWS Cloud WAN

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
 than to write policies yourself. It takes time and expertise to [create IAM customer
 managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html") that provide your team with only the permissions they need. To get
 started quickly, you can use our AWS managed policies. These policies cover common use cases
 and are available in your AWS account. For more information about AWS managed policies,
 see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the
 permissions in AWS managed policies. Services occasionally add additional permissions to an
 AWS managed policy to support new features. This type of update affects all identities
 (users, groups, and roles) where the policy is attached. Services are most likely to update an
 AWS managed policy when a new feature is launched or when new operations become available.
 Services do not remove permissions from an AWS managed policy, so policy updates won't break
 your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
 services. For example, the `ReadOnlyAccess` AWS managed
 policy provides read-only access to all AWS services and resources. When a service launches
 a new feature, AWS adds read-only permissions for new operations and resources. For a list
 and descriptions of job function policies, see [AWS managed policies for
 job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html") in the *IAM User Guide*.


## AWS managed policy: AWSNetworkManagerCloudWANServiceRolePolicy


You can attach the `AWSNetworkManagerCloudWANServiceRolePolicy` policy to
 your IAM identities. This policy allows AWS Network Manager to access resources associated with
 Cloud WAN. For more information, see [AWS Cloud WAN service-linked roles](cwan-using-service-linked-roles.md "cwan-using-service-linked-roles.md").


To view the permissions for this policy, see [AWSNetworkManagerCloudWANServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerCloudWANServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerCloudWANServiceRolePolicy.html") 
 in the *AWS Managed Policy Reference*.


## AWS managed policy: AWSNetworkManagerServiceRolePolicy


This policy is attached to the service-linked role named
 `AWSServiceRoleForNetworkManager` to allow AWS Cloud WAN to call API actions on your
 behalf when you work with global networks. For more information, see [AWS Cloud WAN service-linked roles](cwan-using-service-linked-roles.md "cwan-using-service-linked-roles.md").


To view the permissions for this policy, see [AWSNetworkManagerServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSNetworkManagerServiceRolePolicy.html") 
 in the *AWS Managed Policy Reference*.


## Cloud WAN updates to AWS managed
 policies


View details about updates to AWS managed policies for AWS Cloud WAN since this service began
 tracking these changes in July 2022.




| Change | Description | Date |
| --- | --- | --- |
| [AWSNetworkManagerCloudWANServiceRolePolicy](#security-iam-AWSNetworkManagerCloudWANServiceRolePolicy "#security-iam-AWSNetworkManagerCloudWANServiceRolePolicy") - New policy.  | Added a policy to allow Network Manager to access resources associated with your core network. | July 12, 2022 |
| [AWSNetworkManagerServiceRolePolicy](#security-iam-AWSNetworkManagerServiceRolePolicy "#security-iam-AWSNetworkManagerServiceRolePolicy") - New policy. | Added a policy to allow Network Manager to access resources associated with your global networks. | December 3, 2019 |
