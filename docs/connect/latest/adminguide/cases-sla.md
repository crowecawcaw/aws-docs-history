

# How SLAs work in Connect Customer Cases

 Service Level Agreements (SLAs) in Amazon Connect Cases are a type of related item that can be associated with a case. With SLAs, you can track service goals for your contact center, specifying that particular types of cases should reach certain milestones within set timeframes. 

## Understanding SLAs in Cases
<a name="cases-sla-understand"></a>

 Case SLAs in Amazon Connect consist of the following components: 
+  **SLA name** – The identifier for the SLA in the UI and API responses. 
+  **Target field** – The case field that the SLA tracks. This can be the Status field or any other single-select field, including custom fields. 
+  **Target value** – The field value that the case must reach to fulfill the SLA. It must exactly match one of the field's option values. 
+  **Target date and time** – The deadline by which the case needs to reach a target value. You can set a deadline of up to 730 days (2 years). 
+  **SLA status** – The current fulfillment status of the SLA. Possible statuses include: 
  +  Active – SLA not yet fulfilled, but target time not reached 
  +  Met – SLA fulfilled before target time 
  +  Not met – SLA fulfilled after target time exceeded 
  +  Due soon – SLA not fulfilled, target time less than 24 hours away 
  +  Overdue – SLA not fulfilled, target time already exceeded 
+  **Time to breach** – For unfulfilled SLAs, the time remaining until the target date and time is exceeded. For overdue cases, this continues to run negative until the target value is achieved. 

**Note**  
You can attach up to 30 SLAs to a case. To request more, use Service Quotas. For more information, see [Cases quotas](amazon-connect-service-limits.md#cases-quotas).  
You can change the target date and time of an existing SLA only by using the `UpdateRelatedItem` API. Set `targetSlaMinutes` to a value from 1 to 1,051,200 minutes (730 days). The new target date and time is the SLA creation time plus `targetSlaMinutes`, regardless of when you make the update. Cases then recalculates the SLA status against the new target date and time. A fulfilled SLA can change from Met to Not met, or from Not met to Met.

## Adding SLAs to Cases
<a name="cases-sla-adding"></a>

 You can associate SLAs with cases in two ways: 
+  **Automatically** – Use conversational analytics rules to add SLAs to cases that meet specified conditions (case template and field values) for Case Creation and Update rules. For more information, see [Automatically monitor and update cases in Connect Customer Cases](create-alerts-on-cases.md).
+  **Manually** – Use the CreateRelatedItem API to add an SLA related item to a case. 

Create a rule for SLA assignment when you want SLAs applied automatically to cases that meet certain conditions. The following two procedures create the rule. In the first, you create the rule and define the cases that it applies to. In the second, you add the action that assigns the SLA.

**Before you begin**
+ Make sure that Cases sends updates to rules. For more information, see [Allow Connect Customer Cases to send updates to conversational analytics rules using the CLI](cases-rules-integration-onboarding.md).
+ Make sure that the case templates and fields that the rule uses exist, including the single-select field that you want the SLA to track.
+ Make sure that you have a user account with permissions to create rules.<a name="cases-sla-assign-rule"></a>

**To create a rule for SLA assignment**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use a user account that has permissions to create rules.

1. On the navigation menu, choose **Analytics and optimization**, **Rules**, and then choose **Create a rule**, **Cases**.

1. Under **When**, choose **A new case is created** or **A case is updated**. Choose **Add condition** and define the cases that the SLA applies to, for example, when the case template equals **Billing**. Choose **Next**.

After you choose **Next**, add the action that assigns the SLA.<a name="cases-sla-assign-rule-action"></a>

**To add the SLA action to the rule**

1. Choose **Add action**, **Assign service level agreement to case**.

1. For **SLA name**, enter a name for the SLA.

1. For **The SLA is met if**, choose **Select field**, and then select a single-select field. The list shows every single-select field in your Cases domain, including custom fields.

   An SLA can track only single-select fields. If you select a field of another type, you can't save the rule.

1. For **Value**, select the value that the field must reach for the SLA to be met.

   If you select a value that isn't one of the field's options, you can't save the rule.

1. For **Target** and **Time**, enter the target duration, which is the time from when the SLA is assigned within which the case must reach a target value.

1. Choose **Next**, review the rule, and then choose **Save**.

The rule takes its name from the SLA name. You can't change the rule name on the review page.

## Viewing SLAs on Cases
<a name="cases-sla-viewing"></a>

 Managers and agents can view case SLAs in the agent workspace to prioritize cases and identify those at risk of missing service goals. 

**Case summary page**

**To add SLA information to the case list view:**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. Open the **Agent Workspace**.  
![Open the agent workspace.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-sla-viewing-1.png)

1.  Choose the gear icon in the top right of the table.   
![The gear icon in the top right of the table.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-sla-viewing-2.png)

1.  Add the **Next SLA Breach** field to the active list.   
![Add the Next SLA Breach field to the active list.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-sla-viewing-3.png)

1.  Toggle the field from inactive to active.   
![You then toggle this new field to make it appear in the SLA dashboard.](https://docs.aws.amazon.com/connect/latest/adminguide/images/cases-sla-viewing-4.png)

**Note**  
 These settings persist unless you clear your cookies. 

**Case detail page**

**For cases with active SLAs:**
+  A badge notification appears next to the case title, showing the time until the next active SLA will breach. 
+  An SLAs section below the case details lists all active and completed SLAs associated with the case. This includes SLAs that track custom fields. For each SLA, the section shows: 
  +  SLA name 
  +  Status 
  +  Target date and time 
  +  Completion date and time (if applicable) 
  +  Time to breach (if applicable) 
**Note**  
The SLAs section doesn't show which field an SLA tracks or its target value. To get them, call the `SearchRelatedItems` API, which returns `fieldId` and `targetFieldValues` for each SLA.

## Automating Actions for Breached SLAs
<a name="cases-sla-automating-breached"></a>

 You can use conversational analytics rules to trigger automated actions when SLAs reach their target completion time without being met: 

1.  In the conversational analytics rules interface, add a new rule with the trigger based on **Case SLA Breach**. 

1.  Specify which SLA names the **Breach rule** should apply to. 

You can create a rule that emails the user who is assigned to a case when one of the case's SLAs is breached. You don't need to keep a list of recipients: The email goes to whoever is assigned to the case at the time of the breach.

**Before you begin**

Make sure that Cases sends updates to rules. If it doesn't, breach rules don't run, and no email is sent. For more information, see [Allow Connect Customer Cases to send updates to conversational analytics rules using the CLI](cases-rules-integration-onboarding.md).<a name="cases-sla-breach-email-assignee"></a>

**To create a rule for SLA breaches**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use a user account that has permissions to create rules.

1. On the navigation menu, choose **Analytics and optimization**, **Rules**, and then choose **Create a rule**, **Cases**.

1. Under **When**, choose **A case service level agreement is breached**.

1. Specify which SLA names the rule applies to, and then choose **Next**.

After you choose **Next**, add the email action.<a name="cases-sla-breach-email-assignee-action"></a>

**To add the email action to the rule**

1. Choose **Add action**, **Send email notification**.

1. Under **To**, choose **Select the agent who is assigned to the case**.

1. In **Subject** and **Body**, enter the email content. Use **@** to add dynamic variables. For case rules, you can insert the rule name, the instance URL, and the case ID.

1. Choose **Next**, review the rule, and then choose **Save**.

**Who receives the email**
+ With this rule, you can email the user who is assigned to the case when the SLA becomes Overdue. If the case was reassigned before then, the new assignee receives the email.
+ Your email goes to the user's secondary email address if the user has one, and otherwise to the user's email address. For SAML users, you must configure a secondary email address so that they can receive the email from Connect Customer.
+ Make sure that a user is assigned to the case before the SLA is breached. If the case has no assigned user, your rule doesn't send an email, and the rule action fails. If you receive rule failure events in Amazon EventBridge, the Amazon Connect Rules Action Execution Failed event has the reason code `InvalidRequestException`.
+ Make sure that the assigned user has an email address. If the user has no email address, your rule doesn't send an email.
+ Your existing breach rules that email specific users or users with specific tags keep working as before. A case can have both kinds of rule.

**Note**  
The same email limits apply as for other rule emails, including the default limit of 500 emails a day. For more information, see [Create rules that send email notifications](contact-lens-rules-email.md).

To create this rule with the API, call `CreateRule` with the event source `OnSlaBreach` and a `SEND_NOTIFICATION` action whose recipient `UserIds` is `["$.Case.Fields.AssignedUser"]`.

 For more information, see [Automatically monitor and update cases in Connect Customer Cases](create-alerts-on-cases.md) in the Amazon Connect documentation. 