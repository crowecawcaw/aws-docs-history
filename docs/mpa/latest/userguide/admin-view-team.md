

# View an approval team
<a name="admin-view-team"></a>

When you sign in to your organization's management account, you can view your approval teams and teams that have been shared with you by navigating to the Multi-party approval console.

For more information about statuses, see [Team health](team-health.md).

## View an approval team
<a name="admin-view-team-steps"></a>

To view a team, complete the following steps.

 **Minimum permissions** 

To view a team, you need permission to run the following action:
+ `mpa:GetApprovalTeam`

If you are using the AWS Management Console, you also need permission to run the following actions:
+ `kms:Decrypt`
+ `organizations:DescribeOrganization`
+ `organizations:ListDelegatedAdministrators`
+ `sso:DescribeInstance`
+ `sso:GetSharedSsoConfiguration`
+ `sso:ListInstances`
+ `sso-directory:DescribeUsers`
+ `sso-directory:SearchUsers`

------
#### [ AWS Management Console ]

**To view a team**

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/).

1. On the left navigation, choose **Multi-party approval**.

1. On the **Multi-party approval** console, you can view a list of your teams.

1. On the **Team** column, select a team to view its details.

------
#### [ AWS CLI & AWS SDKs ]

**To view a team**  
You can use one of the following operations:
+ AWS CLI: [list-approval-teams](https://docs.aws.amazon.com/cli/latest/reference/mpa/list-approval-teams.html) and [get-approval-team](https://docs.aws.amazon.com/cli/latest/reference/mpa/get-approval-team.html)

  1. Run the following command to return a list of Amazon Resource Names (ARNs) for your teams:

     ```
     $ C:\> aws mpa list-approval-teams
     ```

  1. Run the following command to view details for a team:

     ```
     $ C:\> aws mpa get-approval-team --arn arn:aws:mpa:{{region}}:{{123456789012}}:approval-team/{{TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
     ```
+ AWS SDKs: [ListApprovalTeams](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListApprovalTeams.html) and [GetApprovalTeam](https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetApprovalTeam.html)

------