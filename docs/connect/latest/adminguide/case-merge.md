

# Merge cases in Cases

Agents can merge cases in the agent workspace. You choose a *primary case*, which stays open, and a *secondary case*, which is merged into the primary case and then closed. The merge copies field values to the primary case, moves related items such as comments and contacts, links the two cases to each other, and records the merge in the audit history of both cases.

**Important**  
You can't undo a merge. After a case is merged into another case, it can't be merged again.

## Prerequisites
<a name="case-merge-prerequisites"></a>

To merge cases, the agent's security profile must include the **Cases** - **Merge** permission. Without this permission, the **Merge** button is not displayed on the case details page. Enabling **Merge** automatically grants the **View** permission for Cases if it is not already granted. Agents don't need the **Edit** permission to merge cases. For information about configuring security profiles, see [Security profile permissions for Cases](assign-security-profile-cases.md).

If you use tag-based access control for cases, the agent must have access to both the primary case and the secondary case. For more information, see [Set up tag-based access controls on cases](cases-tag-based-access-control.md).

## Which cases can be merged
<a name="case-merge-eligibility"></a>

You can merge two cases when all of the following are true:
+ Neither case is **Closed**.
+ Both cases have the same customer, or at least one of the cases has no customer.
+ Neither case is part of a merge that is still in progress.
+ Neither case was previously merged into another case. A case that was the primary case in an earlier merge can be merged again.
+ After the merge, the primary case doesn't have more than 500 field values and doesn't exceed the maximum case size.
+ After the merge, the related items on the primary case, including the related items moved from the secondary case and the new link to the secondary case, don't exceed the quota for related items that can be attached to a case. For more information, see [Connect Customer Cases service quotas](amazon-connect-service-limits.md#cases-quotas).

The cases can use different case templates. The primary case keeps its case template.

You merge one secondary case into a primary case at a time.

## How to merge cases
<a name="case-merge-how-to"></a>

1. In the agent workspace, open one of the cases that you want to merge.

1. On the case details page, choose **Merge**. If the button isn't displayed, choose **More**, and then choose **Merge**.  
![The Merge button on the case details page.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-merge-button.png)

   The **Merge cases** page opens in a new tab. The case that you started from is the **Primary case**.

1. For **Secondary case**, choose **Choose a case**, and then search for and select the case to merge. The list shows only cases that are not closed and that have the same customer as the case you started from, or no customer.  
![The Merge cases page, with the list of cases that can be chosen as the secondary case.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-merge-choose-case.png)

   To make the selected case the primary case instead, choose the swap icon (**Swap primary and secondary cases**).

1. For **Merge method**, choose one of the following:
   + **Quick merge** (default): Keeps all field values from the primary case. Empty fields on the primary case are filled with the values from the secondary case.
   + **Manual merge**: Under **Reconcile case differences**, for each field where the two cases have different values, choose whether to keep the value from the **Primary case** or the **Secondary case**. Each field defaults to the primary case's value. Empty fields on the primary case are filled with the values from the secondary case.  
![The Merge cases page with Manual merge selected, showing the Reconcile case differences section.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-merge-settings.png)

1. For **Merge related items**, choose one of the following:
   + **Keep all related items** (default): Moves supported related items from the secondary case to the primary case. For details, see [What is merged](#case-merge-what-is-merged).
   + **Keep related items from the primary case only**: No related items are moved. The related items of the secondary case stay on the secondary case after it's closed.

1. Review the warning that the secondary case will be closed and can't be merged again, and then choose **Merge cases**.

   The **Merge cases** tab closes and the merge runs in the background.

## What is merged into the primary case
<a name="case-merge-what-is-merged"></a>

**Fields**
+ The merge applies to custom fields and to the following system fields: assigned queue, assigned user, summary, and case reason. Other system fields, such as status, title, customer, and reference number, keep the primary case's values.
+ For each of these fields, the primary case keeps its value unless you chose the secondary case's value in a manual merge. If the field is empty on the primary case, it's filled with the value from the secondary case.
+ Field values are read from both cases when the merge runs, so changes made to the primary case after the merge starts are taken into account.

**Related items**

The following table describes what happens to the related items of the secondary case when you choose **Keep all related items**.


| Related item | What the merge does | 
| --- | --- | 
| Comments, contacts, custom related items, and linked cases | Moved from the secondary case to the primary case. Tags on these items are kept, except tags whose keys start with aws:. | 
| A contact that is on both cases | Kept once, on the primary case. Tags that exist only on the secondary case's copy are added to it. | 
| A linked case that the primary case is already linked to | Removed from the secondary case. The primary case keeps its existing link. | 
| Files, SLAs, and other related item types | Not moved. They stay on the secondary case. | 

**Case links and status**
+ The primary and secondary cases are linked to each other. Each case shows the other case on its **Linked Cases** tab.
+ The secondary case is closed.
+ The merge doesn't change the tags on either case.

## Primary and secondary cases during and after a merge
<a name="case-merge-during-after"></a>

A merge runs in the background. It can take a few moments, and longer for cases with many related items. While a merge is in progress:
+ The primary case shows the banner **A merge is in progress for this case**. Agents can continue to edit the primary case, but they can't delete it or include it in another merge.  
![The primary case during a merge, with the banner A merge is in progress for this case.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-merge-primary-in-progress.png)
+ The secondary case shows the banner **This case is currently being merged**. Agents can't edit, delete, or take any other action on the secondary case until the merge is complete.

After the merge completes:
+ The primary case can be edited, deleted, and merged like any other case.
+ The secondary case is closed and shows a banner that links to the case it was merged into. Agents can reopen, edit, or delete the secondary case like any other case, but they can't merge it again, either as a primary case or as a secondary case.  
![The closed secondary case after a merge, with a banner that links to the primary case.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-merge-secondary-closed.png)

## Merges in case audit history
<a name="case-merge-audit-history"></a>

Each case keeps its own audit history. The merge adds entries to the audit history of both cases for the changes it makes, such as the field updates on the primary case and the closed status on the secondary case. Both cases also get a summary entry for the merge.

In the [GetCaseAuditEvents](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCaseAuditEvents.html) API, the summary entry has the type `Case.Merged`. Audit events created by a merge include a `mergeMetadata` object with a `mergeEventId`, the `primaryCaseId`, and the `secondaryCaseId`. Use the `mergeEventId` to group all the audit events from the same merge.

## APIs to merge cases
<a name="case-merge-apis"></a>

You can also merge cases by using the Connect Customer Cases API:
+ [StartMergeCases](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_StartMergeCases.html): Starts merging a secondary case into a primary case. The merge runs asynchronously. The request is rejected with a `ConflictException` if either case is part of a merge that is in progress or was previously merged into another case.
+ [GetMergeCasesStatus](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetMergeCasesStatus.html): Returns `IN_PROGRESS` for both cases while a merge runs, and `COMPLETED` for the secondary case after the merge finishes. For any other case, including the primary case after the merge finishes, it returns a `ResourceNotFoundException`.