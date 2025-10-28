# Policy best

practices for Amazon EMR

Identity-based policies are very powerful. They determine whether someone can
create, access, or delete Amazon EMR resources in your account. These actions can incur
costs for your AWS account. When you create or edit identity-based policies,
follow these guidelines and recommendations:

- **Get Started Using AWS Managed Policies**
  – To start using Amazon EMR quickly, use AWS managed policies to give
  your employees the permissions they need. These policies are already
  available in your account and are maintained and updated by AWS. For more
  information, see [Get
  started using permissions with AWS managed policies](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies") in the
  _IAM User Guide_ and [Amazon EMR managed
  policies](emr-managed-iam-policies.md "emr-managed-iam-policies.md").
- **Grant Least Privilege** – When you
  create custom policies, grant only the permissions required to perform a
  task. Start with a minimum set of permissions and grant additional
  permissions as necessary. Doing so is more secure than starting with
  permissions that are too lenient and then trying to tighten them later. For
  more information, see [Grant
  least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the
  _IAM User Guide_.
- **Enable MFA for Sensitive Operations**
  – For extra security, require a users to use multi-factor
  authentication (MFA) to access sensitive resources or API operations. For
  more information, see [Using multi-factor authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the
  _IAM User Guide_.
- **Use Policy Conditions for Extra Security**
  – To the extent that it's practical, define the conditions under
  which your identity-based policies allow access to a resource. For example,
  you can write conditions to specify a range of allowable IP addresses that a
  request must come from. You can also write conditions to allow requests only
  within a specified date or time range, or to require the use of SSL or MFA.
  For more information, see [IAM
  JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the
  _IAM User Guide_.
