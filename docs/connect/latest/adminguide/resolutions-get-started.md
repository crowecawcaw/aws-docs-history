

# Get started with Resolutions

 Use these steps to run your first process on Resolutions. You start from a standard operating procedure (SOP) for the process. The steps are in dependency order. The first procedure sets up your instance and publishes a Work plan. Steps 1 and 2 are one-time setup for your instance. The remaining steps repeat for each process that you bring onto Resolutions. 

## Before you begin
<a name="resolutions-get-started-before-you-begin"></a>

You need the following.
+  A Connect Customer instance. If you don't have one, see [Get started with Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-get-started.html). 
+ At least one queue for specialist work.
+ A routing profile that includes the Task channel.

## Steps
<a name="resolutions-get-started-steps"></a>

### Set up your instance and publish a Work plan
<a name="resolutions-get-started-set-up-your-instance-and-publish-a-work-plan"></a>

1.  **Set up your instance.** Enable Connect AI agents, Customer Profiles, Cases, the email channel, and attachments. Several of these steps need IAM permissions beyond a typical operations role. For instructions, see [Set up your instance for Resolutions](resolutions-prerequisites.md). 

1.  **Grant access.** Assign the ResolutionsUser security profile to the operations managers who will author Work plans. For instructions, see [Grant access to Resolutions](resolutions-grant-access.md). 

1.  **Prepare your SOP.** Choose one process with high volume and clear rules for your first Work plan. The SOP describes how a request arrives, what information the process needs, the decision rules and thresholds, who approves exceptions, and how the request ends. If the SOP leaves something out, the Resolutions AI assistant asks you about it. 

1.  **Create and publish a Work plan.** Upload the SOP, answer the assistant's questions, update Steps that don't match current practice, resolve open items, generate flows, and publish. For instructions, see [Create and publish a Work plan](resolutions-create-work-plan.md). 

### Put the Work plan into service and refine it
<a name="resolutions-get-started-put-the-work-plan-into-service-and-refine-it"></a>

1.  **Add the Work plan to your inbound contact flow.** Update the inbound contact flow that handles email for this process so that it transfers to the Work plan's information extraction flow. Resolutions doesn't change inbound contact flows for you. For instructions, see [Start Work plans from inbound email](resolutions-start-work-plan.md). 

1.  **Set up specialists.** Add the queues that the Work plan uses to your specialists' routing profiles, and give specialists Cases permissions. For instructions, see [Work on Resolutions Cases in the agent workspace](resolutions-specialists.md). 

1.  **Send a test request.** Email a sample request to the email address that uses the inbound contact flow you updated. Confirm that a Resolutions Case is created, that Case fields are populated, and that the first Phase starts. Follow the Resolutions Case through each Step in the agent workspace. 

1.  **Refine and republish.** Clone the published version to make changes, publish the new version, and update your inbound contact flow to use the new version's information extraction flow. For instructions, see [Manage Work plans and versions](resolutions-manage-work-plans.md). 

**Tip**  
 Test your email setup before you test a Work plan. Send a plain email to your Connect Customer address and confirm that a contact arrives. Email configuration problems and Work plan problems look the same from the outside, so ruling out email first saves diagnosis time. 

## Next steps
<a name="resolutions-get-started-next-steps"></a>
+  To call your own business applications from a Step, see [Connect business applications](resolutions-integrations.md). 
+  If a Work plan doesn't start or stalls, see [Troubleshoot Resolutions](resolutions-troubleshoot.md). 

## Additional resources
<a name="resolutions-get-started-additional-resources"></a>
+  [Connect Customer pricing on the AWS website](https://aws.amazon.com/connect/pricing/) 
+  [Connect Customer API Reference](https://docs.aws.amazon.com/connect/latest/APIReference/Welcome.html) 