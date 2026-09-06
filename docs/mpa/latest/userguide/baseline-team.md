

# Baseline an approval team
<a name="baseline-team"></a>

Baselining an approval team is a method to ensure that approvers can and are responding to Multi-party approval sessions they are prompted for. The baseline feature allows the Multi-party approval administrator to select specific approvers or an entire team to baseline, based on the last activity of each approver.

Approval teams can decline in health for several reasons:
+ Natural attrition where approvers leave the organization.
+ Incorrect approvers selected by mistake.
+ Improper configuration of approval threshold and approver count.
+ Approvers becoming less engaged over time, missing approval windows or not responding.

Without regular review, approval thresholds and approval team compositions can become stale. Regular monitoring and adjustment of approval teams is necessary to maintain their effectiveness.

## Start an approval team baseline
<a name="baseline-team-steps"></a>

To baseline a team, complete the following steps.

 **Minimum permissions** 

To baseline a team, you need permission to run the following action:
+ `mpa:StartApprovalTeamBaseline`

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

**To baseline a team**

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/).

1. On the left navigation, choose **Multi-party approval**.

1. On the **Team** column, select a team to view its details.

1. On the team page, choose **Baseline approvers**.

1. On the **Baseline approvers** page, select one or more approvers you want to baseline. This will start a Multi-party approval session against the selected approvers.

1. After you have selected the approvers you want to baseline, choose **Baseline approvers**.

------
#### [ AWS CLI & AWS SDKs ]

**To baseline a team**  
You can use one of the following operations:
+ AWS CLI: [list-approval-teams](https://docs.aws.amazon.com/cli/latest/reference/mpa/list-approval-teams.html) and [start-approval-team-baseline](https://docs.aws.amazon.com/cli/latest/reference/mpa/start-approval-team-baseline.html)

  1. Run the following command to return a list of Amazon Resource Names (ARNs) for teams:

     ```
     $ C:\> aws mpa list-approval-teams
     ```

     This returns the `Arn` you need for `--arn` (Step 2).

  1. Run one of the following commands to start a baseline:

     **To baseline all approvers in a team:**

     ```
     $ C:\> aws mpa start-approval-team-baseline \
       --arn arn:aws:mpa:{{region}}:{{123456789012}}:approval-team/{{TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
     ```

     **To baseline specific approvers:**

     ```
     $ C:\> aws mpa start-approval-team-baseline \
       --arn arn:aws:mpa:{{region}}:{{123456789012}}:approval-team/{{TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
       --approver-ids {{approver-id-1}} {{approver-id-2}}
     ```
     + **`--arn`**: Amazon Resource Name (ARN) for the approval team.
     + **`--approver-ids`** (Optional): One or more approver IDs to baseline. If not specified, all approvers in the team are baselined.

  1. (Optional) Run the following command to view the last activity information for each approver in the team:

     ```
     $ C:\> aws mpa get-approval-team \
       --arn arn:aws:mpa:{{region}}:{{123456789012}}:approval-team/{{TeamName-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
     ```

     The response includes last activity information for each approver in the team.
+ AWS SDKs: [ListApprovalTeams](https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListApprovalTeams.html) and [StartApprovalTeamBaseline](https://docs.aws.amazon.com/mpa/latest/APIReference/API_StartApprovalTeamBaseline.html)

------

**What to do next**  
After you start a baseline, approvers can accept the baseline by accessing the approver portal. You can monitor the baseline status and last activity information for each approver using the AWS CLI & AWS SDKs with the [get-approval-team](https://docs.aws.amazon.com/cli/latest/reference/mpa/get-approval-team.html) command, or by viewing the team details in the Multi-party approval console. For more information, see [View team](admin-view-team.md).

## Considerations
<a name="baseline-team-considerations"></a>

**Baselining starts a Multi-party approval session**

When you baseline approvers, a Multi-party approval session is created for the selected approvers. Approvers must respond to the baseline through the approver portal.

**Regular baselining is recommended**

Regular baselining helps maintain the health of your approval teams by identifying approvers who are no longer responsive. Use the last activity information returned by `GetApprovalTeam` to determine which approvers may need to be baselined or replaced.