# Share an approval team

Multi-party approval works with [AWS Resource Access Manager (AWS RAM)](https://aws.amazon.com/ram "https://aws.amazon.com/ram") to enable resource sharing. Sharing allows other AWS accounts to use or access approval teams you have created. For example, if you want the requester to have access to details about an approval session, you must share the associated approval team.

The shareable resource is called a `Multi-party Approval Team`.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

###### Topics

- [Prerequisites for sharing teams](#sharing-prereqs "#sharing-prereqs")
- [Share a team](#sharing-share "#sharing-share")
- [Unshare a shared team](#sharing-unshare "#sharing-unshare")
- [Identify a shared team](#sharing-identify "#sharing-identify")

## Prerequisites for sharing teams

- To share a team, you must own it in your AWS account. This means that
  the resource must be allocated or provisioned in your account. You cannot share
  a team that has been shared with you.
- To share a team with your organization or an organizational unit in
  AWS Organizations, you must enable sharing with AWS Organizations. For more information, see
  [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
  _AWS RAM User Guide_.

## Share a team

To share a team, you must add it to a resource share. A resource share is an
AWS RAM resource that lets you share your resources across AWS accounts. A resource
share specifies the resources to share, and the consumers with whom they are shared.
To add the team to a new resource share, you must first create the
resource share using the [AWS RAM
console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").

If you are part of an organization in AWS Organizations and sharing within your organization is
enabled, consumers in your organization are automatically granted access to the shared
team. Otherwise, consumers receive an invitation to join the resource share and
are granted access to the shared team after accepting the invitation.

**Minimum permissions**

To share a team, you need permission to run the following actions:

- `ram:EnableSharingWithAwsOrganization` (If sharing within an organization)
- `ram:CreateResourceShare`

For step-by-step instructions, see [Creating a Resource Share](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the
_AWS RAM User Guide_.

## Unshare a shared team

**Minimum permissions**

To unshare a team, you need permission to run the following action:

- `ram:DisassociateResourceShare`

For step-by-step instructions, see [Deleting a Resource Share](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md") in the _AWS RAM User Guide_.

## Identify a shared team

**Minimum permissions**

To identify a shared team, you need permission to run the following action:

- `mpa:ListApprovalTeams`

AWS Management Console

###### To identify a shared team

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/").
2. On the left navigation, choose **Multi-party approval**.
3. On the **Multi-party approval** console, you can view the owner in the **Owner** column.

AWS CLI & AWS SDKs

###### To identify a shared team

You can use one of the following operations:

- AWS CLI: [list-approval-teams](../../../cli/latest/reference/mpa/list-approval-teams.md "../../../cli/latest/reference/mpa/list-approval-teams.md")

Run the following command to return a list of Amazon Resource Names (ARNs) for your teams:

```
`$` `C:\>` **aws mpa list-approval-teams**
```

The ARN includes the account ID which you can use to identify the owner. For example, `arn:aws:mpa:`region`:`123456789012`:approval-team/`TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``.

In this example, if `123456789012` is your account ID, you are the owner. If not, the team has been shared with you.

- AWS SDKs: [ListApprovalTeams](../APIReference/API_ListApprovalTeams.md "../APIReference/API_ListApprovalTeams.md")
