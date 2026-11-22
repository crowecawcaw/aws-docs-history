

# Start Work plans from inbound email

 Customer email must reach the Work plan's information extraction flow. That flow uses the prebuilt agentic data extraction capability in Connect Customer to read the message and its attachments. It fills in the Case fields, creates a new Resolutions Case or updates an existing one, and starts the Work plan. 

 Resolutions doesn't update your inbound contact flows, because those flows might also handle contacts for use cases outside Resolutions. The operations manager or an authorized administrator adds the information extraction flow to the inbound contact flow, after the logic that determines which Work plan applies. Until then, email still arrives as a contact, but it never reaches the information extraction flow. No Resolutions Case is created and no Work plan runs. Resolutions tracks only Resolutions Cases, so it has nothing to report. 

## Before you begin
<a name="resolutions-start-work-plan-before-you-begin"></a>
+  A published Work plan version that's associated with a Case template. See [Create and publish a Work plan](resolutions-create-work-plan.md). 
+  A working email address on your instance. See [Email setup for Resolutions](resolutions-prerequisites.md#resolutions-prereq-email). 
+  Permission to edit and publish the inbound contact flow that handles email for this process. 

## To add a Work plan to your inbound contact flow
<a name="resolutions-start-work-plan-to-add-a-work-plan-to-your-inbound-contact-flow"></a>

1.  In Resolutions, open the Work plan and confirm that the version you want is **Published** and associated with your Case template. 

1.  On the **Version details** tab, note the name of the **Information extraction flow**. 

1.  In the Connect Customer admin website, open the inbound contact flow that handles email for this process. 

1.  After the logic that determines which Work plan applies to the contact, add a **Transfer to flow** block that transfers the contact to the information extraction flow from step 2. 

    In the block's properties, choose the information extraction flow, and then choose **Save**. For more information about the block, see [Transfer to flow](transfer-to-flow.md). 

1. Save and publish the inbound contact flow.

1.  If the email address that receives requests doesn't already use this inbound contact flow, set the address's inbound flow to it. 

## To verify
<a name="resolutions-start-work-plan-to-verify"></a>

 Send a test email to the address. Include the details that the Work plan extracts, such as the applicant's name and the requested amount, and attach any documents the process needs. 

Then confirm the following.
+ A Resolutions Case is created from the Work plan's Case template.
+ The Case fields contain values from the message.
+  On the Resolutions Case's **Work plan activity** tab, the inbound email shows as **Completed** and the first Phase shows as **In progress**. 

 Also send an email for a different use case that the same inbound contact flow handles. Confirm that it doesn't start a Resolutions Case. 

 To follow the Resolutions Case, see [Work on Resolutions Cases in the agent workspace](resolutions-specialists.md). 

## When you publish a new version
<a name="resolutions-start-work-plan-when-you-publish-a-new-version"></a>

 Each published version has its own set of flows, including its own information extraction flow. After you publish a new version, update your inbound contact flow to transfer to the new version's information extraction flow. 

**Important**  
 If you don't update the inbound contact flow, inbound email continues to start Resolutions Cases on the previous version. 

## Which Work plan version a Resolutions Case runs
<a name="resolutions-start-work-plan-which-work-plan-version-a-resolutions-case-runs"></a>

 The Case template determines which Work plan version a Resolutions Case can run. 
+  If the Case template has no Work plan version set, a Resolutions Case can start any published Work plan version on its first run. 
+  If the Case template has a Work plan version set, every Resolutions Case from that template runs that version. 

 After a Resolutions Case runs a Work plan version, it can rerun only that version. To run a different version, create a new Resolutions Case, and link it to the original Resolutions Case on the **Linked Cases** tab to keep the history together. 