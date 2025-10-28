# Delegate permission set

administration

IAM Identity Center enables you to delegate management of permission sets and assignments in
accounts by creating [IAM policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") that reference the [Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") of IAM Identity Center resources. For example, you
can create policies that enable different administrators to manage assignments
in specified accounts for permission sets with specific tags.

###### Note

To use permission sets, you'll need to use an Organization instance of
IAM Identity Center. For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").

You can use either of the following methods to create these types of
policies.

- (Recommended) Create [permission
  sets](permissionsets.md "permissionsets.md") in IAM Identity Center, each with a different policy, and assign the
  permission sets to different users or groups. This enables you to manage
  administrative permissions for users who sign in using your chosen [IAM Identity Center identity source](manage-your-identity-source.md "manage-your-identity-source.md").
- Create custom policies in IAM, and then attach them to IAM roles
  that your administrators assume. For information about roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") to get their assigned IAM Identity Center administrative
  permissions.

###### Important

IAM Identity Center resource ARNs are case sensitive.

The following shows the proper case for referencing the IAM Identity Center permission set
and account resource types.

| Resource Types | ARN                                                                     | Context Keys                |
| -------------- | ----------------------------------------------------------------------- | --------------------------- |
| PermissionSet  | `arn:${Partition}:sso:::permissionSet/${InstanceId}/${PermissionSetId}` | `aws:ResourceTag/${TagKey}` |
| Account        | `arn:${Partition}:sso:::account/${AccountId}`                           | Not Applicable              |
