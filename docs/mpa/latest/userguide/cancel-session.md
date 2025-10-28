# Cancel an approval session

When you sign in to your organization's management account, you can cancel an approval session by navigating to the Multi-party approval console.

As the Multi-party approval administrator, you can cancel unnecessary sessions, including those created by mistake or for team updates and deletions that are no longer needed.

## Cancel a session

To cancel an approval session, complete the following steps.

**Minimum permissions**

To cancel a session, you need permission to run the following action:

- `mpa:CancelSession`

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

###### To cancel a team update or deletion

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/").
2. On the left navigation, choose **Multi-party approval**.
3. On the **Multi-party approval** console, select a team and choose **Edit** in the **Actions** dropdown menu.
4. On the **Team** column, select a team to view its details.
5. On the team page, choose **Cancel edits** or **Cancel delete**.
6. (For cancel edits) On the **Cancel team edits** dialog box, confirm the cancellation and choose **Cancel edits**.

AWS CLI & AWS SDKs

###### To cancel a session

You can use one of the following operations:

- AWS CLI: [list-approval-teams](../../../cli/latest/reference/mpa/list-approval-teams.md "../../../cli/latest/reference/mpa/list-approval-teams.md"), [get-approval-team](../../../cli/latest/reference/mpa/get-approval-team.md "../../../cli/latest/reference/mpa/get-approval-team.md"), and [cancel-session](../../../cli/latest/reference/mpa/cancel-session.md "../../../cli/latest/reference/mpa/cancel-session.md")
  1.  Run the following command to return a list of Amazon Resource Names (ARNs) for your teams:

  ```
  `$` `C:\>` **aws mpa list-approval-teams**
  ```

  2.  Run the following command to get the Amazon Resource Name (ARN) for the session with the pending update from the relevant team:

  ```
  `$` `C:\>` **aws mpa get-approval-team --arn arn:aws:mpa:`region`:`123456789012`:approval-team/`TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`**
  ```

  3.  Run the following command to cancel a session:

  ```
  `$` `C:\>` **aws mpa cancel-session \
   --arn arn:aws:mpa:`region`:`123456789012`:session/`TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`**
  ```

- AWS SDKs: [ListApprovalTeams](../APIReference/API_ListApprovalTeams.md "../APIReference/API_ListApprovalTeams.md"), [GetApprovalTeam](../APIReference/API_GetApprovalTeam.md "../APIReference/API_GetApprovalTeam.md"), and [CancelSession](../APIReference/API_CancelSession.md "../APIReference/API_CancelSession.md")

###### What to do next

After you cancel a team update or deletion, the team continues to function with its existing details. The version ID for the team does not change.

## Considerations

**Only sessions pending approval can be canceled**

You can only cancel sessions in the _update pending approval_ or _delete pending approval_ state.

For more information about statuses, see [Team health](team-health.md "team-health.md").
