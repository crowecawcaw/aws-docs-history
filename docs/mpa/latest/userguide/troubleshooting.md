# Troubleshooting

To help you understand Multi-party approval, this topic describes troubleshooting scenarios.

**Scenarios**

- Recover teams after IAM Identity Center instance deletion
- Recover team with too few active approvers
- Failed team update
- Failed team deletion

Recover teams after IAM Identity Center instance deletion

Problem

When you delete the IAM Identity Center instance that is connected to your Multi-party approval identity source, your approval teams will enter an error state. In this state, approvers can no longer access the Multi-party approval portal to vote on sessions, making the teams non-functional.

Solution

**Prerequisites**

Before starting the recovery process, check that:

- Your IAM Identity Center instance has been deleted
- You cannot update your approval team

**To recover teams after IAM Identity Center instance deletion:**

1. Delete your Multi-party approval identity source by following the instructions in [Disable Multi-party approval](delete-identity-source.md "delete-identity-source.md"). Because the IAM Identity Center instance is deleted, you can proceed with identity source deletion even with existing approval teams.
2. Create a new IAM Identity Center instance. Configure users in this new instance to replace the existing identities in the approval teams that you need to recover.
3. [Create a new Multi-party approval identity source](setting-up.md "setting-up.md").
4. Assign new approvers to the affected approval teams using the standard process. Do not include previous approvers.
5. Follow the troubleshooting steps for the scenario **Recover team with too few active approvers**.

After you create your support ticket, AWS will review the case. If the case is approved, AWS will provide you with information on how to recover the team.

Recover team with too few active approvers

Problem

Your approval team can't approve team updates or requested operations because the number of active approvers has fallen below the approver threshold.

Solution

**Prerequisites**

Before starting the recovery process, check that:

- Your team cannot meet the approval threshold
- Your team has experienced a failed approval session (including sessions for team updates)
- You cannot assign new approvers through standard processes

**To recover the team**:

1. Collect the following information:
   - Amazon Resource Name (ARN) for the affected approval team
   - Amazon Resource Name (ARN) for the failed approval session
   - Business impact statement
   - Updated list of approvers

2. Contact AWS Support to initiate the approval team recovery process.
   - Open a ticket using the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/")
   - In the ticket, include the team details you collected
   - Label the ticket "Approval Team Recovery" and then submit the ticket.

After you create your support ticket, AWS will review the case. If the case is approved, AWS will provide you with information on how to recover the team.

Failed team update

Problem

When you update a team, Multi-party approval changes the workflow status to _update pending activation_.
If the update fails, the workflow status changes to either _update failed approval_, _update failed validation_, or _update failed activation_.

This status will remain for the team unless you [delete the draft](update-team.md#update-team-draft-status "update-team.md#update-team-draft-status") or there are subsequent successful updates.

For more information on team and workflow statuses, see [Team health](team-health.md "team-health.md").

Solution

- You can try to update the team again, or [delete the draft](update-team.md#update-team-draft-status "update-team.md#update-team-draft-status"). For more information, see [Update team](update-team.md "update-team.md").

Failed team deletion

Problem

When you delete a team, Multi-party approval changes the workflow status to _delete pending approval_.
If the deletion is rejected, the workflow status changes to _delete failed approval_.

This status will remain for the team unless there are subsequent successful updates (including a successful team deletion).

For more information on team and workflow statuses, see [Team health](team-health.md "team-health.md").

Solution

You can try to delete the team again, or you can update the team. For more information, see [Delete team](delete-team.md "delete-team.md") and [Update team](update-team.md "update-team.md").
