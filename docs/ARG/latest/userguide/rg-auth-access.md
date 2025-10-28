# Learn more about AWS Resource Groups authorization and access

control

Resource Groups supports the following.

- **Action-based policies.** For example, you
  can create a policy that allows users to perform [**ListGroups**](../APIReference/API_ListGroups.md "../APIReference/API_ListGroups.md") operations, but no others.
- **Resource-level permissions.** Resource Groups
  supports using [ARNs](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") to
  specify individual resources in the policy.
- **Authorization based on tags.** Resource Groups
  supports using resource tags in the condition of a policy. For example, you
  can create a policy that allows Resource Groups users full access to a group that you
  have tagged.
- **Temporary credentials.** Users can assume a
  role with a policy that allows AWS Resource Groups operations.
  Resource Groups doesn't support resource-based policies.

For more information about how Resource Groups and Tag Editor integrate with AWS Identity and Access Management (IAM),
see the following topics in the _AWS Identity and Access Management User Guide_.

- [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md#management_svcs "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md#management_svcs")
- [Actions, resources,
  and condition keys for AWS Resource Groups](../../../IAM/latest/UserGuide/list_awsresourcegroups.md "../../../IAM/latest/UserGuide/list_awsresourcegroups.md")
- [Controlling access using policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md")
