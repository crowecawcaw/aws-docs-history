# Delegating a control

set for review in AWS Audit Manager

When you need assistance from a subject matter expert, you can choose the AWS account
that you want to help you, and then delegate a control set to them for review.

## Delegate permissions

The below policy is attached to a delegate to whom the control set is delegated to.

Audit Manager replaces the `placeholder text` with your account and
resource identifiers before attaching the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Delegate",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`Principal for user/role who is delegated a Control Set of the Assessment`"
 },
 "Action": [
 "auditmanager:UpdateAssessmentControl",
 "auditmanager:UpdateAssessmentControlSetStatus",
 "auditmanager:GetEvidenceFoldersByAssessmentControl",
 "auditmanager:BatchImportEvidenceToAssessmentControl",
 "auditmanager:GetEvidenceFolder",
 "auditmanager:GetEvidence",
 "auditmanager:GetEvidenceByEvidenceFolder"
 ],
 "Resource": "arn:aws:auditmanager:`us-east-1`:`123456789012`:assessment/`assessment_ID`/controlSet/`control_set_ID`"
 }
 ]
}`

```

## Prerequisites

Make sure your IAM identity has appropriate permissions to create a delegation in
AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can use either of the following procedures to delegate a control set.

###### To delegate a control set from the assessment page

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Assessments**.
3. Select the name of the assessment that contains the control set that you want to delegate.
4. From the assessment page, choose the **Controls** tab. This displays the
   control status summary and the list of controls in the assessment.
5. Select a control set and choose **Delegate control set**.
6. Under **Delegate selection**, a list of users and roles is displayed.
   Choose a user or role, or use the search bar to look for one.
7. Under **Delegation details**, review the control set name and the
   assessment name.
8. (Optional) Under **Comments**, add a comment with instructions to help the
   delegate fulfill their review task. Don't include any sensitive information in your
   comment.
9. Choose **Delegate control set**.
10. A green success banner confirms the successful delegation of the control set. Choose
    **View delegation** to see the delegation request. You can also view your
    delegations at any time by choosing **Delegations** in the left navigation
    pane of the AWS Audit Manager console.

###### To delegate a control set from the delegations page

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Delegations**.
3. From the delegations page, choose **Create delegation**.
4. Under **Choose assessment and control set**, specify the assessment and the
   control set that you want to delegate.
5. Under **Delegate selection**, you will see a list of users and roles.
   Choose a user or role, or use the search bar to look for one.
6. (Optional) Under **Comments**, add a comment with instructions to help the
   delegate fulfill their review task. Don't include any sensitive information in your
   comment.
7. Choose **Create delegation**.
8. A green success banner confirms the successful delegation of the control set. Choose
   **View delegation** to see the delegation request. You can also view your
   delegations at any time by choosing **Delegations** in the left navigation
   pane of the AWS Audit Manager console.
   After you delegate a control set for review, the delegate receives a notification and
   can then begin to review the control set. This process that delegates follow is described
   in [Understanding the different delegation tasks for
   delegates](delegation-for-delegates.md "delegation-for-delegates.md").

## Next steps

To revisit your delegation at a later date, see [Finding and reviewing
the delegations that you've sent in AWS Audit Manager](delegation-for-audit-owners-reviewing-delegations.md "delegation-for-audit-owners-reviewing-delegations.md").
