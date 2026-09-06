

# AWS managed policies for AWS Elemental MediaTailor
<a name="security-iam-awsmanpol"></a>







To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSElementalMediaTailorFullAccess
<a name="security-iam-awsmanpol-AWSElementalMediaTailorFullAccess"></a>

You can attach the `AWSElementalMediaTailorFullAccess` policy to your IAM identities. It's useful for users who need to create and manage playback configurations and channel assembly resources, such as programs and channels. This policy grants permissions that allow full access to AWS Elemental MediaTailor. These users can create, update, and delete MediaTailor resources.

To view the permissions for this policy, see [AWSElementalMediaTailorFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElementalMediaTailorFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSElementalMediaTailorReadOnly
<a name="security-iam-awsmanpol-AWSElementalMediaTailorReadOnly"></a>

You can attach the `AWSElementalMediaTailorReadOnly` policy to your IAM identities. It's useful for users who need to view playback configurations and channel assembly resources, such as programs and channels. This policy grants permissions that allow read-only access to AWS Elemental MediaTailor. These users can't create, update, or delete MediaTailor resources.

To view the permissions for this policy, see [AWSElementalMediaTailorReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElementalMediaTailorReadOnly.html) in the *AWS Managed Policy Reference*.

## MediaTailor updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for MediaTailor since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the MediaTailor [Document history for AWS Elemental MediaTailor](document-history.md).




| Change | Description | Date | 
| --- | --- | --- | 
|  MediaTailor added new managed policies | MediaTailor added the following managed policies:+  [AWSElementalMediaTailorReadOnly](#security-iam-awsmanpol-AWSElementalMediaTailorReadOnly)  <br />+  [AWSElementalMediaTailorFullAccess](#security-iam-awsmanpol-AWSElementalMediaTailorFullAccess)   | November 24, 2021 | 
| MediaTailor started tracking changes | MediaTailor started tracking changes for its AWS managed policies. | November 24, 2021 | 