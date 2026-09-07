

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Resource-based policies
<a name="security_iam_access-manage-resource-based-policies"></a>

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.