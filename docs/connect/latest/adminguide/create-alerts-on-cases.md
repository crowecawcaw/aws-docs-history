

# Automatically monitor and update cases in Connect Customer Cases
<a name="create-alerts-on-cases"></a>

You can easily set up case notifications and automation. You can create rules that automatically run whenever a case is created or updated. You can create rules that: 
+ Assign service level agreements to cases
+ Create tasks
+ End associated tasks
+ Update cases
+ Send email alerts to Connect Customer users

For example, you can set up an alert that automatically sends an email to a manager when a high-priority case is created or updated.

**Tip**  
A developer needs to enable this feature. For instructions, see [Allow Connect Customer Cases to send updates to conversational analytics rules](cases-rules-integration-onboarding.md). 

**Topics**
+ [Step 1: Define rule conditions](#conditions-alerts-on-cases)
+ [Step 2: Define rule actions](#rule-actions-alerts-on-cases)

## Step 1: Define rule conditions
<a name="conditions-alerts-on-cases"></a>

1. On the navigation menu, choose **Analytics and optimization**, **Rules**.

1. Select **Create a rule**, **Cases**.  
![The Create a rule dropdown menu on the Rules page, the Cases option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/conditions-alerts-on-cases-1.png)

1. Under **When**, use the dropdown list to choose from two event sources: **A new case is created**, **A case is updated**, or **A case service level agreement is breached**. These options are shown in the following image.  
![The option When a case rule is available.](http://docs.aws.amazon.com/connect/latest/adminguide/images/conditions-alerts-on-cases-2.png)

1. Choose **Add condition**. You can define conditions based on the case template value, such as when the case template equals **Billing**, or based on case field values, such as when Priority equals **high**.  
![The condition for when a real-time metric is updated.](http://docs.aws.amazon.com/connect/latest/adminguide/images/conditions-alerts-on-cases-3.png)

   You can combine multiple conditions to build very specific rules.

   The following image shows a sample rule with multiple conditions:  
![The condition for when a real-time metric is updated.](http://docs.aws.amazon.com/connect/latest/adminguide/images/conditions-alerts-on-cases-4.png)

1. Choose **Next**.

## Step 2: Define rule actions
<a name="rule-actions-alerts-on-cases"></a>

1. Choose **Add action**. You can choose the following actions:
   + [Assign service level agreement to case](cases-sla.md#cases-sla-adding)
   + [Create task](contact-lens-rules-create-task.md)
   + [End tasks](contact-lens-rules-ends-tasks.md)
   + [Update case](contact-lens-rules-update-case.md)
   + [Send email notification](contact-lens-rules-email.md)  
![The add action dropdown menu, a list of actions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/rule-actions-alerts-on-cases.png)

1. Choose **Next**.

1. Review and make any edits, then choose **Save**. 