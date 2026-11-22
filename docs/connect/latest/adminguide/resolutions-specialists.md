

# Work on Resolutions Cases in the agent workspace

 Specialists work on Resolutions Cases in the agent workspace. When a Step needs a person, Resolutions creates a Task for that Step and routes it to the queue configured on the Step. The specialist accepts the Task, sees the full Resolutions Case and its Work plan progress, records the outcome, and ends the Task. The Work plan then moves to the next Step. 

## Set up specialists
<a name="resolutions-specialists-set-up-specialists"></a>

1.  Add the queues that the Work plan uses to each specialist's routing profile. These are the queues you chose for the **UpdateContactTargetQueue** configurations when you created the Work plan. The routing profile must include the Task channel. For more information, see [The task channel in Connect Customer](tasks.md). 

1.  Give specialists Cases permissions. See [Grant Cases permissions to specialists](resolutions-grant-access.md#resolutions-grant-access-grant-cases-permissions-to-specialists). 

## Accept a Task
<a name="resolutions-specialists-accept-a-task"></a>

 When a Step reaches a specialist, the Task appears in the contact control panel as an incoming Task named after the Step, such as **Prequalify Applicant**. The Resolutions Case opens alongside it. 

Choose **Accept task**.

![The agent workspace with an incoming Prequalify Applicant Task and Accept task and Reject task buttons.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-incoming-task.png)


## Review the Resolutions Case and its Work plan progress
<a name="resolutions-specialists-review-the-resolutions-case-and-its-work-plan-progress"></a>

 The Resolutions Case opens on the **Work plan activity** tab. The tab shows the Work plan name and each Phase with its status, which is **Not started**, **In progress**, or **Complete**. 

![The Work plan activity tab for a Resolutions Case on the Personal auto first notice of loss Work plan. Phase 1 is Complete and Phase 2 is In progress. Two Tasks and an outbound email in Phase 2 show as Completed. The Work plan menu at the top is open and shows Start, which is unavailable, and Stop.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-workplan-activity.png)


 Expand a Phase to see its activities. Each activity shows its type and name, a description, its status, and the time it completed. Activities include the following. 
+  **Inbound email.** The customer message that started the Resolutions Case, with its sender, recipient, and attachments. 
+  **Inbound call.** The customer call that started the Resolutions Case. 
+  **Task.** A Step in the Work plan, shown as **Task:** followed by the Step name, such as **Task: Human Claim Approval Review**. The description states what the Step does and when it starts. Its status is **Queued**, **Ongoing**, or **Completed**. 
+  **Outbound email.** An email that the Work plan sent to the customer. 

 Steps in the same Phase can run at the same time. In the screenshot, **Send Receipt Confirmation** and **Human Claim Approval Review** both start as soon as Phase 1 completes. 

Use the controls on the tab to focus the view.


| Control | What it does | 
| --- | --- | 
| Activity type |  Filters the activities by type. The default is All activities.  | 
| Phase |  Filters the activities to one Phase. The default is All phases.  | 
| Show Work plan | Shows the Work plan's Phases on the tab. | 
|  Expand all and Collapse all  | Expands or collapses every Phase. | 

 The Resolutions Case also has **Comments**, **Attachments**, **SLAs**, **Related items**, **Linked Cases**, and **More Information** tabs. **More Information** shows the Case fields that the Work plan reads and writes. 

## Stop and restart the Work plan on a Resolutions Case
<a name="resolutions-specialists-stop-and-restart-the-work-plan-on-a-resolutions-case"></a>

 The **Work plan** menu at the top of the Resolutions Case shows the Work plan's status, such as **Work plan: Active** or **Work plan: Inactive**. 

**To stop the Work plan**

 Choose **Work plan: Active**, and then choose **Stop**. 

 Tasks close independently of the Work plan and the Resolutions Case. Stopping the Work plan doesn't close Tasks that are queued or in progress, and specialists end them as usual. 

**To restart the Work plan**

1.  Choose **Work plan: Inactive**, and then choose **Start**. **Start** is available only while the Work plan is inactive.   
![A Resolutions Case with Status Closed and the Work plan menu showing Inactive. The menu is open. Start is available and Stop is unavailable.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-work-plan-inactive-start.png)

1.  In the **Restart Work plan** dialog box, review the following. The example is for a Work plan named **Personal auto first notice of loss**. 
   + The name of the Work plan.
   +  The **Work plan overview**, which states the number of Phases and lists each Phase. In the example, the Work plan has 4 Phases: Phase 1: Intake Validation & Triage, Phase 2: Acknowledgement & Approval Routing, Phase 3: Approval Outcome Processing, and Phase 4: Customer Notification & Follow-up. 
   +  A note that case information from a previously active Work plan might exist on the Resolutions Case. You can erase the information by resetting the Work plan fields. 

1.  (Optional) For **Reset Work plan fields**, choose the Case fields to clear. 

1. Choose **Restart Work plan**.  
![The Restart work plan dialog box for a Resolutions Case.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-restart-work-plan.png)

 The restarted Work plan reuses the values already in the Case fields, and skips Steps whose results are already recorded. Clear the fields that hold data or decisions the rerun must redo, and keep the fields that are still correct. The rerun then updates only the fields that you cleared. 

 A restart runs the same Work plan version that the Resolutions Case ran before. For more information, see [Which Work plan version a Resolutions Case runs](resolutions-start-work-plan.md#resolutions-start-work-plan-which-work-plan-version-a-resolutions-case-runs). 

## Record the outcome and end the Task
<a name="resolutions-specialists-record-the-outcome-and-end-the-task"></a>

1.  In the **Task information** pane, review the Step description. It states what to check and what outcomes to record. 

1.  Enter the outcome in the Step's outcome field, such as **prequalificationOutcome**, and then choose **Save**. 

1. Choose **End task**, and then confirm.

 The Step shows as **Completed** on the **Work plan activity** tab, and the Work plan starts the next Step. To step away from a Task without ending it, choose **Pause**. Choose **Resume** to continue. 

![Phase 1 is Complete and expanded. Its Inbound call and its Task, Validate Intake And Triage, both show as Completed. Phase 2 is In progress, and Phases 3 and 4 are Not started.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-phase-progress.png)


**Note**  
Ending a Task closes it permanently. You can't resume work on it.

## When the Work plan finishes
<a name="resolutions-specialists-when-the-work-plan-finishes"></a>

 After the last Step completes, every Phase shows **Complete**. The Resolutions Case status changes to **Closed**, and the **Work plan** menu at the top of the Resolutions Case shows **Inactive**. 

![A closed Resolutions Case. Phases 1 to 4 are Complete and Phase 5 shows its final Task as Completed.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-case-complete.png)
