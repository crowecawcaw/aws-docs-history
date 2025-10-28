# Delete an approval team

When you sign in to your organization's management account, you can request to delete your approval
teams by navigating to the Multi-party approval console. This creates an approval session for the request if the team is active.

## Delete an approval team

To delete a team, complete the following steps.

**Minimum permissions**

To delete a team, you need permission to run the following actions:

- `mpa:DeleteInactiveApprovalTeamVersion` (If deleting an inactive team)
- `mpa:StartActiveApprovalTeamDeletion` (If deleting an active team)

If you are using the AWS Management Console, you also need permission to run the following actions:

- `kms:Decrypt`
- `organizations:DescribeOrganization`
- `organizations:ListDelegatedAdministrators`
- `sso:DescribeInstance`
- `sso:GetSharedSsoConfiguration`
- `sso:ListInstances`
- `sso-directory:DescribeUsers`
- `sso-directory:SearchUsers`

AWS Management Console

###### To delete a team

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/").
2. On the left navigation, choose **Multi-party approval**.
3. On the **Team** column, select a team to view its details.
4. On the team page, choose **Delete**.
5. On the **Delete team** dialog box, confirm the deletion and choose **Delete approval team**.

AWS CLI & AWS SDKs

###### To delete a team

You can use one of the following operations:

- AWS CLI: [list-approval-teams](../../../cli/latest/reference/mpa/list-approval-teams.md "../../../cli/latest/reference/mpa/list-approval-teams.md"), [start-active-approval-team-deletion](../../../cli/latest/reference/mpa/start-active-approval-team-deletion.md "../../../cli/latest/reference/mpa/start-active-approval-team-deletion.md"), and [delete-inactive-approval-team-version](../../../cli/latest/reference/mpa/start-active-approval-team-deletion.md "../../../cli/latest/reference/mpa/start-active-approval-team-deletion.md")
  1.  Run the following command to return a list of Amazon Resource Names (ARNs) for your teams:

  ```
  `$` `C:\>` **aws mpa list-approval-teams**
  ```

  2.  **For active teams**

  Run the following command to request to delete an active team:

  ```
  `$` `C:\>` **aws mpa start-active-approval-team-deletion \
   --arn arn:aws:mpa:`region`:`123456789012`:approval-team/`TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`**
  ```

  **For inactive teams**

  Run the following command to get the version ID:

  ```
  `$` `C:\>` **aws mpa get-approval-team --arn arn:aws:mpa:`region`:`123456789012`:approval-team/`TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`**
  ```

  Run the following command to delete an inactive team:

  ```
  `$` `C:\>` **aws mpa delete-inactive-approval-team-version \
   --arn arn:aws:mpa:`region`:`123456789012`:approval-team/`TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
   --version-id `string`**
  ```

- AWS SDKs: [ListApprovalTeams](../APIReference/API_ListApprovalTeams.md "../APIReference/API_ListApprovalTeams.md"), [StartActiveApprovalTeamDeletion](../APIReference/API_StartActiveApprovalTeamDeletion.md "../APIReference/API_StartActiveApprovalTeamDeletion.md"), and [DeleteInactiveApprovalTeamVersion](../APIReference/API_DeleteInactiveApprovalTeamVersion.md "../APIReference/API_DeleteInactiveApprovalTeamVersion.md")

###### What to do next

After you request to delete an active team, you can monitor the team status in the Multi-party approval console or using the AWS CLI & AWS SDKs.
For more information, see [View team](admin-view-team.md "admin-view-team.md"). To cancel a request, see [Cancel session](cancel-session.md "cancel-session.md").

## Considerations

**Deletions of active teams require team approval**

The request to delete an active team must be approved by the team. If the team is inactive, you do not need team approval.

**Teams can be deleted even when protecting resources**

A team can still be deleted even when it is protecting resources. The service integration provides workflows for reassigning protected resources to available teams.

For information, see the **Learn More** column in [What operations are currently supported with Multi-party approval](what-is.md#mpa-integrations-supported "what-is.md#mpa-integrations-supported").
