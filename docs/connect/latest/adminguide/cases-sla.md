

# How SLAs work in Connect Customer Cases
<a name="cases-sla"></a>

 Service Level Agreements (SLAs) in Amazon Connect Cases are a type of related item that can be associated with a case. With SLAs, you can track service goals for your contact center, specifying that particular types of cases should reach certain milestones within set timeframes. 

## Understanding SLAs in Cases
<a name="cases-sla-understand"></a>

 Case SLAs in Amazon Connect consist of the following components: 
+  **SLA name**: The identifier for the SLA in the UI and API responses. 
+  **Target date and time**: The deadline by which the case needs to progress to the target status. This can be configured up to 90 days. 
+  **Target value**: The field value that the case needs to be updated to for the SLA to be considered fulfilled. 
+  **SLA status**: The current fulfillment status of the SLA. Possible statuses include: 
  +  Active: SLA not yet fulfilled, but target time not reached 
  +  Met: SLA fulfilled before target time 
  +  Not met: SLA fulfilled after target time exceeded 
  +  Due soon: SLA not fulfilled, target time less than 24 hours away 
  +  Overdue: SLA not fulfilled, target time already exceeded 
+  **Time to breach**: For unfulfilled SLAs, the time remaining until the target date and time is exceeded. For overdue cases, this continues to run negative until the target value is achieved. 

## Adding SLAs to Cases
<a name="cases-sla-adding"></a>

 You can associate SLAs with cases in two ways: 
+  **Automatically**: Use conversational analytics rules to add SLAs to cases that meet specified conditions (case template and field values) for Case Creation and Update rules. For more information, see [Automatically monitor and update cases in Connect Customer Cases](create-alerts-on-cases.md).
+  **Manually**: Use the CreateRelatedItem API to add an SLA related item to a case. 

## Viewing SLAs on Cases
<a name="cases-sla-viewing"></a>

 Managers and agents can view case SLAs in the agent application to prioritize cases and identify those at risk of missing service goals. 

**Case summary page**

**To add SLA information to the case list view:**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. Open the **Agent Workspace**.  
![Open the Agent Workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-sla-viewing-1.png)

1.  Choose the gear icon in the top right of the table.   
![The gear icon in the top right of the table.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-sla-viewing-2.png)

1.  Add the **Next SLA Breach** field to the active list.   
![Add the Next SLA Breach field to the active list.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-sla-viewing-3.png)

1.  Toggle the field from inactive to active.   
![You then toggle this new field to make it appear in the SLA dashboard.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-sla-viewing-4.png)

**Note**  
 These settings persist unless you clear your cookies. 

**Case detail page**

**For cases with active SLAs:**
+  A badge notification appears next to the case title, showing the time until the next active SLA will breach. 
+  An SLAs section below the case details lists all active and completed SLAs associated with the case, including: 
  +  SLA name 
  +  Status 
  +  Target date and time 
  +  Completion date and time (if applicable) 
  +  Time to breach (if applicable) 

## Automating Actions for Breached SLAs
<a name="cases-sla-automating-breached"></a>

 You can use conversational analytics rules to trigger automated actions when SLAs reach their target completion time without being met: 

1.  In the conversational analytics rules interface, add a new rule with the trigger based on **Case SLA Breach**. 

1.  Specify which SLA names the **Breach rule** should apply to. 

 For more information, see [Automatically monitor and update cases in Connect Customer Cases](create-alerts-on-cases.md) in the Amazon Connect documentation. 