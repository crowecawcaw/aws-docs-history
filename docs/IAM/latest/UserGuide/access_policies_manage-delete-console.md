# Delete IAM policies (console)

You can use the AWS Management Console to delete _customer managed
policies_ and _inline policies_ in IAM.
The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

###### Note

Deletion of IAM policies is permanent. After the policy is deleted it cannot be
recovered.

For more information about IAM policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md") and the [IAM JSON policy element reference](reference_policies_elements.md "reference_policies_elements.md").

For more information about the difference between managed and inline policies, see [Managed policies and inline policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md").

## Prerequisites

Before you delete a policy, you should review its recent service-level activity. This is
important because you don't want to remove access from a principal (person or application) who
is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Deleting IAM policies

(console)

You might need to delete a customer managed policy when it becomes obsolete or no longer
aligns with your organization's security requirements and access control needs. By deleting
unnecessary policies, you reduce potential security risks associated with outdated or unused
policies. You can delete a customer managed policy to remove it from your AWS account. You
cannot delete AWS managed policies.

Console

###### To delete a customer managed policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Select the radio button next to the customer managed policy to delete. You can
   use the search box to filter the list of policies.
4. Choose **Actions**, and then choose
   **Delete**.
5. Follow the instructions to confirm that you want to delete the policy, and then
   choose **Delete**.

## Deleting inline policies (console)

You might need to delete an inline policy when the specific permissions it grants are no
longer required for the IAM user, group, or role to which it's directly attached. Deleting
unnecessary inline policies helps reduce the risk of unintended access, especially since
inline policies can't be reused or shared across multiple identities like managed policies
can. You can delete an inline policy to remove it from your AWS account. You cannot delete
AWS managed policies.

Console

###### To delete an inline policy for a IAM user, group, or role

1. In the navigation pane, choose **User groups**,
   **Users**, or **Roles**.
2. Choose the name of the user group, user, or role with the policy that you want
   to delete. Then choose the **Permissions** tab.
3. Select the checkboxes next to the policies to delete and choose
   **Remove**. Then, in the confirmation dialog, confirm the removal
   and deletion of the policy.
   - To delete an inline policy in **Users** or
     **Roles**, choose **Remove** to confirm the
     deletion.
   - If you are deleting a single inline policy in **User
     groups**, type the name of the policy and choose
     **Delete**. If you are deleting multiple inline policies in
     **User groups**, type the number of policies you are deleting
     followed by `inline policies` and choose
     **Delete**. For example, if you are deleting three inline
     policies, type `3 inline policies`.
