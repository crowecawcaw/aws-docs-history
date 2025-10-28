# Finding and reviewing

the delegations that you've sent in AWS Audit Manager

You can access a list of your delegations at any time by choosing
**Delegations** in the left navigation pane of Audit Manager. The delegations page
contains a list of your active and completed delegations.

When a delegation is completed, you receive a notification in Audit Manager. You might also
receive comments with remarks from the delegate. The following procedure explains how to
check your delegations in Audit Manager after they are completed, and how to view any comments that
the delegate might have left for you.

## Prerequisites

Make sure your IAM identity has appropriate permissions to view a delegation in
AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

Follow these steps to find and review the delegations that you previously
created.

###### To view a completed delegation and check for comments

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Delegations**.
3. Review the **Delegations** page, which includes a table with the following
   information:

| Name             | Description                                                           |
| ---------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Delegated to** | The AWS account that you delegated the control set to.                |
| **Date**         | The date when you delegated the control set.                          |
| **Status**       | The current status of the delegation.                                 |
| **Assessment**   | The name of the assessment with a link to the assessment detail page. |
| **Control set**  | The name of the control set that was delegated for review.            | 4. Find the assessment and control set that the delegate reviewed and submitted to you, and choose the name of the assessment to open it. 5. Under the **Controls** tab of the assessment detail page, scroll down to the **Control sets** table. 6. Under **Controls grouped by control set**, find the name of the control set that you delegated. 7. Expand the name of the control set to show its controls, and choose the name of a control to open the control detail page. 8. Choose the **Comments** tab to view any remarks added by the delegate for that particular control. 9. When you're satisfied that the review is complete for a control set, select the control set and choose **Complete control set review**. ###### Important Audit Manager collects evidence continuously. As a result, additional new evidence might be collected _after_ the delegate completes their review of a control. If you only want to use reviewed evidence in your assessment reports, you can refer to the _control reviewed_ timestamp to determine when evidence was reviewed. This timestamp can be found on the [Changelog tab](review-controls.md#review-changelog "review-controls.md#review-changelog") of the control detail page. You can then use this timestamp to identify which evidence you add to your assessment reports. ## Next steps To delete a delegation after it's complete and you no longer need it, see [Deleting your completed delegations in AWS Audit Manager](delegation-for-audit-owners-cancel-delegations.md "delegation-for-audit-owners-cancel-delegations.md"). |
