

# Create and publish a Work plan

 In this procedure, you turn a standard operating procedure (SOP) into a published Work plan. You upload the SOP, answer the Resolutions AI assistant's questions, resolve open configuration items, generate flows, and publish. The screenshots show a sample mortgage approval SOP. 

## Before you begin
<a name="resolutions-create-work-plan-before-you-begin"></a>
+  Complete [Set up your instance for Resolutions](resolutions-prerequisites.md) and [Grant access to Resolutions](resolutions-grant-access.md). 
+  Have your SOP ready as a document, or be ready to describe the process in your own words. 
+  Know which queues should receive specialist work, which flow modules call your business applications, and which outbound email address the Work plan should send from. Resolutions asks for these values during configuration. For instructions on building a flow module, see [Connect business applications](resolutions-integrations.md). 

## Step 1: Create the Work plan
<a name="resolutions-create-work-plan-step-1-create-the-work-plan"></a>

1. Sign in to the Connect Customer admin website.

1. In the navigation pane, choose **Resolutions**.

    On an instance that has no Work plans, the **Resolutions** page shows a **Create a Work plan** button and an empty list of Work plans.   
![The Resolutions page, with a Create a Work plan button and an empty list of Work plans.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-landing.png)

1. Choose **Create a Work plan**.

1.  For **Work plan name**, enter a name for the process, such as `SampleMortgageProcess`. Optionally, enter a **Description**. 

    The **Create a Work plan** dialog box has two fields, **Work plan name** and **Description**.   
![The Create a Work plan dialog box, with Work plan name and Description fields.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-create-work-plan.png)
**Important**  
 Don't include sensitive or personal information in the Work plan name or description. 

1.  Choose **Next**. The **Describe your process** page opens. 

## Step 2: Describe your process
<a name="resolutions-create-work-plan-step-2-describe-your-process"></a>

 Resolutions needs your SOP, or a description of the process in your own words, to generate a Work plan. Do one of the following. 
+  To upload an SOP, choose the upload icon in the message box, choose your document, and then send it. 
+  To describe the process, type a description of how the request arrives, what the process checks, who approves what, and how the request ends. Then send it. 

 The assistant reads the process, summarizes what it found, and asks clarifying questions. 

## Step 3: Answer clarifying questions
<a name="resolutions-create-work-plan-step-3-answer-clarifying-questions"></a>

 The assistant asks about details that the SOP doesn't settle. Typical questions cover the following. 
+  What happens when a request fails a check, such as rejection, manual review by a specialist, or an alternative offer. 
+  The thresholds and limits that decide each outcome, and whether they differ by request type. 
+ Whether a Step needs a person, or can run automatically.
+  Whether to email the customer when information is missing, how many reminders to send, and how long to wait. 

![The Describe your process page. The assistant asks two questions about failed gates and loan limits, and the user answers both.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-describe-process.png)


 Answer each round of questions in plain language. You can also reply `just build it`, and the assistant fills in the remaining details with sensible defaults. The assistant labels each default it applies as `ASSUMED DEFAULT` in the Step description, so you can find and review them later. 

 When the assistant has what it needs, it generates the Work plan and opens the configuration page. 

## Step 4: Review Phases and Steps
<a name="resolutions-create-work-plan-step-4-review-phases-and-steps"></a>

 The configuration page has three areas. In the following example, version V1 has 24 open items and five Phases. 
+  **Phase list** on the left. Each Phase shows the number of open items it has. Expand a Phase to see its Steps. 
+  **Phase and Step details** in the center. Each Step shows a description of the work, including its decision rules and its branches for failures and exceptions. 
+  **Resolutions AI assistant** on the right. Ask the assistant to change the plan, for example to add an approval or change a threshold. 

 The Phase list and the details area work together. Choose a Phase or Step in the list to see its description in the details area. When you ask the assistant to change the plan, the list and the details update to show the change. 

![The configuration page for version V1, showing 24 open items, five Phases in the left pane, the details of Phase 1, and the Resolutions AI assistant.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-configuration-open-items.png)


 Read each Step description and confirm that it matches your process. Pay attention to any value labeled `ASSUMED DEFAULT`. To change a Step, choose **Edit** on the Step, or ask the assistant. Where your SOP is out of date with current practice, ask the assistant to reorder Steps or to remove Steps that are no longer needed. 

 The assistant also proposes a target duration for each Step, such as 2 days to appraise collateral. Review these targets in the assistant pane. 

**Note**  
 Phases are fixed for every Resolutions Case on a version. Each Resolutions Case moves through every Phase, and Resolutions uses the Phases to report progress. Design Phases around the stages that you want to track. 

## Step 5: Resolve open items
<a name="resolutions-create-work-plan-step-5-resolve-open-items"></a>

 Each open item is a value that a Step needs before Resolutions can generate its flow. Steps with open items show a warning icon. 

1.  Choose a Step that has open items, and then choose **Fix open items**. 

1.  For each configuration, choose a value from the list. The description under each configuration explains what the value is for. 

1.  Choose **Save**. A confirmation message appears, and the open item count decreases. 

![Step 1.1 Prequalify Applicant, with lists to choose a flow module and a target queue.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-step-configuration.png)


The following table describes the configuration types that you might see.


| Configuration | What you choose | When it appears | 
| --- | --- | --- | 
| InvokeFlowModule (Flows) |  The flow module that performs the Step's work, such as pulling a credit report or generating a commitment letter  | Steps that call a business application | 
| UpdateContactTargetQueue (Queues) |  The queue that receives the Step's Task, such as a loan officer review queue  | Steps or branches that need a specialist | 
| CreateContact (Queues) |  The queue that sends the Step's email. Choose an existing queue, or ask Resolutions to create a dedicated outbound queue.  | Steps that email the customer | 
| StartOutboundEmailContact (Emails) | The from email address for the message | Steps that email the customer | 

![Step 4.2 Issue Decision and Terms, with lists for the flow module, the outbound email queue, and the from email address.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-email-step-configuration.png)


**Important**  
 The from email address must already be configured as an outbound address on your instance. For more information, see [Email setup for Resolutions](resolutions-prerequisites.md#resolutions-prereq-email). 

**Important**  
 If you choose an existing queue for **CreateContact**, set the queue's **Outbound email flow** to a flow that links each email to its Resolutions Case. If you ask Resolutions to create a dedicated outbound queue, Resolutions sets this up for you. For a sample flow, see [Outbound queue and whisper flow for Work plan email](resolutions-prerequisites.md#resolutions-prerequisites-outbound-queue-and-whisper-flow-for-work-plan-email). 

 Repeat for each Step until the **Configuration** badge shows **No open items**. 

## Step 6: Generate flows
<a name="resolutions-create-work-plan-step-6-generate-flows"></a>

 Generate the flows that power your Work plan after you resolve all open items. When no open items remain, the configuration page shows **No open items**. The assistant then summarizes the target duration of each Step and offers to generate the flows. 

1.  Choose **Generate Flows**, or enter `Generate Flows` in the assistant. 

    When no open items remain, the configuration page shows **No open items**. The assistant lists the Step durations and shows a **Generate Flows** button.   
![The configuration page shows No open items. The assistant lists Step durations and shows a Generate Flows button.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-generate-flows.png)

1.  Review the list of fields that the information extraction flow will extract from customer messages. 

   The list includes fields such as the following.
   + `applicantId`
   + `loanType`
   + `requestedLoanAmount`

    The assistant shows the list with **Continue** and **Adjust extraction fields** buttons.   
![The assistant lists fields such as applicantId, loanType, and requestedLoanAmount, with Continue and Adjust extraction fields buttons.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-confirm-extraction-fields.png)

1. Do one of the following.
   + If the list is correct, choose **Continue**.
   +  To change the list, choose **Adjust extraction fields** and tell the assistant what to extract. Resolutions revises the plan and generates the flows again after you approve. 

 When generation finishes, a message confirms that the Step flows were generated. Each Step shows a **View flow** link that opens its flow in the flow designer. 

## Step 7: Publish the version
<a name="resolutions-create-work-plan-step-7-publish-the-version"></a>

1. Choose **Publish**.

1.  In the **Publish Work plan version** dialog box, choose **Publish**. 

![The Publish Work plan version dialog box explains that the version can't be changed after publishing.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-publish-dialog.png)


 Resolutions publishes the version and its flows. It creates the Case template, Case fields, and Task templates, and associates the Case template with the Work plan. The Work plan page opens and shows the published version. 

![The Work plan page for SampleMortgageProcess_demo, showing version V1 as Default and Published, with links to the Work plan flow and the information extraction flow.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-published-work-plan.png)


## Clean up
<a name="resolutions-create-work-plan-clean-up"></a>

 If you created a Work plan only to try Resolutions, delete the Work plan when you no longer need it. Publishing a version creates resources in your instance, such as flows, a Case template, Case fields, and Task templates. For more information about these resources, see [Resources that Resolutions creates](resolutions-how-it-works.md#resolutions-how-it-works-resources-that-resolutions-creates). 

1. In the navigation pane, choose **Resolutions**.

1. Choose the Work plan to open it.

1.  Choose **Work plan actions**, and then choose the delete option. 

 For more information about deleting a Work plan, see [Delete a Work plan](resolutions-manage-work-plans.md#resolutions-manage-work-plans-delete-a-work-plan). 

## Next step
<a name="resolutions-create-work-plan-next-step"></a>

 The published Work plan doesn't run until your inbound contact flow transfers email to its information extraction flow. To add it, see [Start Work plans from inbound email](resolutions-start-work-plan.md). 