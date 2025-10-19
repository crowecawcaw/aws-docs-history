# IAM roles created by IAM Identity Center

When you assign a user to an AWS account IAM Identity Center creates IAM roles to give users permissions to resources.


 When you assign a
 permission set, IAM Identity Center creates corresponding IAM Identity Center-controlled IAM roles in each account, and
 attaches the policies speciﬁed in the permission set to those roles. IAM Identity Center manages the role, and
 allows the authorized users you’ve deﬁned to assume the role, by using the AWS access portal or AWS CLI.
 As you modify the permission set, IAM Identity Center ensures that the corresponding IAM policies and roles
 are updated accordingly. 

###### Note

Permissions sets are not used to grant permissions to applications.

If you've already configured IAM roles in your AWS account, we recommend that you check
 whether your account is approaching the quota for IAM roles. The default quota for IAM roles
 per account is 1000 roles. For more information, see [IAM object quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entities "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entities"). 

If you are nearing the quota, consider requesting a quota increase. Otherwise, you might
 experience problems with IAM Identity Center when you provision permission sets to accounts that have exceeded
 the IAM role quota. For information about how to request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html "https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html") in the
 *Service Quotas User Guide*.

###### Note

If you are reviewing IAM roles in an account that is already using IAM Identity Center, you might
 notice role names beginning with “AWSReservedSSO\_”. These are the roles which
 the IAM Identity Center service has created in the account, and they came from assigning a permission set to
 the account.
