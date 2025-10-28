# Use IAM policies in permission sets

In [Create a permission set](howtocreatepermissionset.md "howtocreatepermissionset.md"), you learned how to add policies,
including customer managed policies and permissions boundaries, to a permission
set. When you add customer managed policies and permissions to a permission set,
IAM Identity Center doesn't create a policy in any AWS accounts. You must instead create
those policies in advance in each account where you want to assign your
permission set, and match them to the name and path specifications of your
permission set. When you assign a permission set to an AWS account in your
organization, IAM Identity Center creates an [AWS Identity and Access Management (IAM) role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") and
attaches your [IAM policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") to
that role.

###### Considerations

- To use permission sets, you'll need to use an Organization instance of
  IAM Identity Center. For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").
- Before you assign your permission set with IAM policies, you must
  prepare your member account. The name of an IAM policy in your member
  account must be a match to the name of the policy in your
  management account. IAM Identity Center fails to assign the permission set if the
  policy doesn't exist in your member account.

###### Note

When a customer managed policy is attached to a permission set,
the name of the policy is not case sensitive.

- The permissions that the policy grants do not have to be an exact match
  between accounts.

# Assign an IAM policy to a

permission set

1. Create an IAM policy in each of the AWS accounts where you want to
   assign the permission set.
2. Assign permissions to the IAM policy. You can assign different
   permissions in different accounts. For a consistent experience,
   configure and maintain identical permissions in each policy. You can use
   automation resources like AWS CloudFormation StackSets to create copies of an
   IAM policy with the same name and permissions in each member account.
   For more information about CloudFormation StackSets, see [Working with AWS CloudFormation StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md") in the
   _AWS CloudFormation User
   guide_.
3. Create a permission set in your management account and add your IAM
   policy under **Customer managed policies** or
   **Permissions boundary**. For more details about
   how to create a permission set, See [Create a permission set](howtocreatepermissionset.md "howtocreatepermissionset.md").
4. Add any inline policies, AWS managed policies, or additional IAM
   policies that you have prepared.
5. Create and assign your permission set.
