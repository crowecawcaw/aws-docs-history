

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Approving or rejecting a workflow run
<a name="workflows-approval-approve"></a>

Workflow runs that include the **Approval** gate will need to be approved or rejected. Users can provide their approval or rejection starting from:
+ the CodeCatalyst console
+ a link provided by a team member
+ an automated Slack notification

After a user provides their approval or rejection, this decision cannot be undone.

**Note**  
Only certain users can approve or reject a workflow run. For more information, see [Who can provide an approval?](workflows-approval.md#workflows-approval-who).

**Before you begin**  
Make sure you have added an **Approval** gate to your workflow. For more information, see [Adding an 'Approval' gate](workflows-approval-add.md).

**To approve or reject a workflow run starting from the CodeCatalyst console**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. In the workflow diagram, choose the box representing the **Approval** gate.

   A side panel appears.
**Note**  
At this point, you can send the URL of this page to other approvers if you want.

1. Under **Review decision**, choose **Approve** or **Reject**.

1. (Optional) In **Comment - optional**, enter a comment indicating why you approved or rejected the workflow run.

1. Choose **Submit**.

**To approve or reject a workflow run starting from a link provided by a team member**

1. Choose the link sent to you by your team member. (You can have your team member read the preceding procedure to obtain the link.)

1. Sign in to CodeCatalyst, if asked.

   You are redirected to the workflow run approval page.

1. Under **Review decision**, choose **Approve** or **Reject**.

1. (Optional) In **Comment - optional**, enter a comment indicating why you approved or rejected the workflow run.

1. Choose **Submit**.

**To approve or reject a workflow run starting from an automated Slack notification**

1. Make sure Slack notifications are set up. See [Configuring approval notifications](workflows-approval-notify.md).

1. In Slack, in the channel to which the approval notification was sent, choose the link in the approval notification.

1. Sign in to CodeCatalyst, if asked.

   You are redirected to the workflow run page.

1. In the workflow diagram, choose the approval gate.

1. Under **Review decision**, choose **Approve** or **Reject**.

1. (Optional) In **Comment - optional**, enter a comment indicating why you approved or rejected the workflow run.

1. Choose **Submit**.