Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Approving or rejecting a workflow run

Workflow runs that include the **Approval** gate will need to be approved
or rejected. Users can provide their approval or rejection starting from:

- the CodeCatalyst console
- a link provided by a team member
- an automated Slack notification
  After a user provides their approval or rejection, this decision cannot be undone.

###### Note

Only certain users can approve or reject a workflow run. For more information, see
[Who can provide an approval?](workflows-approval.md#workflows-approval-who "workflows-approval.md#workflows-approval-who").

###### Before you begin

Make sure you have added an **Approval** gate to
your workflow. For more information, see [Adding an 'Approval' gate](workflows-approval-add.md "workflows-approval-add.md").

###### To approve or reject a workflow run starting from the CodeCatalyst console

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. In the workflow diagram, choose the box representing the
   **Approval** gate.

A side panel appears.

###### Note

At this point, you can send the URL of this page to other approvers if you
want. 6. Under **Review decision**, choose **Approve** or
**Reject**. 7. (Optional) In **Comment - optional**, enter a comment indicating
why you approved or rejected the workflow run. 8. Choose **Submit**.

###### To approve or reject a workflow run starting from a link provided by a team member

1. Choose the link sent to you by your team member. (You can have your team member
   read the preceding procedure to obtain the link.)
2. Sign in to CodeCatalyst, if asked.

You are redirected to the workflow run approval page. 3. Under **Review decision**, choose **Approve** or
**Reject**. 4. (Optional) In **Comment - optional**, enter a comment indicating
why you approved or rejected the workflow run. 5. Choose **Submit**.

###### To approve or reject a workflow run starting from an automated Slack

notification

1. Make sure Slack notifications are set up. See [Configuring approval notifications](workflows-approval-notify.md "workflows-approval-notify.md").
2. In Slack, in the channel to which the approval notification was sent, choose the
   link in the approval notification.
3. Sign in to CodeCatalyst, if asked.

You are redirected to the workflow run page. 4. In the workflow diagram, choose the approval gate. 5. Under **Review decision**, choose **Approve** or
**Reject**. 6. (Optional) In **Comment - optional**, enter a comment indicating
why you approved or rejected the workflow run. 7. Choose **Submit**.
