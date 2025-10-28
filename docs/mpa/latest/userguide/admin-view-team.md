# View an approval team

When you sign in to your organization's management account, you can view your approval
teams and teams that have been shared with you by navigating to the Multi-party approval console.

For more information about statuses, see [Team health](team-health.md "team-health.md").

## View an approval team

To view a team, complete the following steps.

**Minimum permissions**

To view a team, you need permission to run the following action:

- `mpa:GetApprovalTeam`

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

###### To view a team

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/").
2. On the left navigation, choose **Multi-party approval**.
3. On the **Multi-party approval** console, you can view a list of your teams.
4. On the **Team** column, select a team to view its details.

AWS CLI & AWS SDKs

###### To view a team

You can use one of the following operations:

- AWS CLI: [list-approval-teams](../../../cli/latest/reference/mpa/list-approval-teams.md "../../../cli/latest/reference/mpa/list-approval-teams.md") and [get-approval-team](../../../cli/latest/reference/mpa/get-approval-team.md "../../../cli/latest/reference/mpa/get-approval-team.md")
  1.  Run the following command to return a list of Amazon Resource Names (ARNs) for your teams:

  ```
  `$` `C:\>` **aws mpa list-approval-teams**
  ```

  2.  Run the following command to view details for a team:

  ```
  `$` `C:\>` **aws mpa get-approval-team --arn arn:aws:mpa:`region`:`123456789012`:approval-team/`TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`**
  ```

- AWS SDKs: [ListApprovalTeams](../APIReference/API_ListApprovalTeams.md "../APIReference/API_ListApprovalTeams.md") and [GetApprovalTeam](../APIReference/API_GetApprovalTeam.md "../APIReference/API_GetApprovalTeam.md")
