# AWS managed policies for AWS Elemental MediaTailor

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

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
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed

policy: AWSElementalMediaTailorFullAccess

You can attach the `AWSElementalMediaTailorFullAccess` policy to your IAM
identities. It's useful for users who need to create and manage playback configurations and
channel assembly resources, such as programs and channels. This policy grants permissions
that allow full access to AWS Elemental MediaTailor. These users can create, update, and delete
MediaTailor resources.

To view the permissions for this policy, see [AWSElementalMediaTailorFullAccess](../../../aws-managed-policy/latest/reference/AWSElementalMediaTailorFullAccess.md "../../../aws-managed-policy/latest/reference/AWSElementalMediaTailorFullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed

policy: AWSElementalMediaTailorReadOnly

You can attach the `AWSElementalMediaTailorReadOnly` policy to your IAM
identities. It's useful for users who need to view playback configurations and channel
assembly resources, such as programs and channels. This policy grants permissions that
allow read-only access to AWS Elemental MediaTailor. These users can't create, update, or delete
MediaTailor resources.

To view the permissions for this policy, see [AWSElementalMediaTailorReadOnly](../../../aws-managed-policy/latest/reference/AWSElementalMediaTailorReadOnly.md "../../../aws-managed-policy/latest/reference/AWSElementalMediaTailorReadOnly.md") in the _AWS Managed Policy Reference_.

## MediaTailor updates to AWS managed

policies

View details about updates to AWS managed policies for MediaTailor since this
service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the MediaTailor [Document history for AWS Elemental MediaTailor](document-history.md "document-history.md").

| Change                                 | Description                                                                                                                                                                                                                                                                                                                                                                   | Date              |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| MediaTailor added new managed policies | MediaTailor added the following managed policies: <br>• [AWSElementalMediaTailorReadOnly](#security-iam-awsmanpol-AWSElementalMediaTailorReadOnly "#security-iam-awsmanpol-AWSElementalMediaTailorReadOnly") <br>• [AWSElementalMediaTailorFullAccess](#security-iam-awsmanpol-AWSElementalMediaTailorFullAccess "#security-iam-awsmanpol-AWSElementalMediaTailorFullAccess") | November 24, 2021 |
| MediaTailor started tracking changes   | MediaTailor started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                            | November 24, 2021 |
