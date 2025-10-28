# Manage IAM policies

IAM gives you the tools to create and manage all types of IAM policies (managed policies
and inline policies). To add permissions to an IAM identity (IAM user, group, or role), you
create a policy, validate
the policy, and then attach the policy to the identity. You can attach
multiple policies to an identity, and each policy can contain multiple permissions.

###### Topics

- [Additional resources](#access_policies_manage-additional-resources "#access_policies_manage-additional-resources")
- [Define custom IAM permissions with customer managed
  policies](access_policies_create.md "access_policies_create.md")
- [IAM policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md")
- [IAM policy testing with the IAM policy
  simulator](access_policies_testing-policies.md "access_policies_testing-policies.md")
- [Adding and removing IAM identity
  permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md")
- [Versioning IAM policies](access_policies_managed-versioning.md "access_policies_managed-versioning.md")
- [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md")
- [Delete IAM policies](access_policies_manage-delete.md "access_policies_manage-delete.md")
- [Refine permissions in AWS using last
  accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md")

## Additional resources

The following resources can help you learn more about AWS policies.

- For more information about the different types of IAM policies, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md").
- For general information about using policies within IAM, see [Access management for AWS resources](access.md "access.md").
- For information about how to use IAM Access Analyzer to generate an IAM policy that is
  based on access activity for an entity, see [IAM Access Analyzer policy
  generation](access-analyzer-policy-generation.md "access-analyzer-policy-generation.md").
- For information about how permissions are evaluated when multiple policies are in
  effect for a given IAM identity, see [Policy evaluation logic](reference_policies_evaluation-logic.md "reference_policies_evaluation-logic.md").
- The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").
