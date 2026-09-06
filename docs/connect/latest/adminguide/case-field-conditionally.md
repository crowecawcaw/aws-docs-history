

# Conditionally required
<a name="case-field-conditionally"></a>

You can streamline how agents populate case fields, and reduce data entry errors, by conditionally requiring specific fields.

To make a field conditionally required, you first set up a field condition. Then, on a case template, choose which field the case field condition should apply to. 

For example, you might want to enforce that **Agent Handle Reason** is required if a case is updated after it was created. To achieve this you would:

1. Create a case field condition based on whether the [Date/Time Opened](case-fields.md) field is not blank.

1. Apply the case field condition to the **Agent Handle Reason** field on the case template.

The following image shows an example **Edit case** page where this requirement is being enforced.

![The Edit case page on the agent workspace, the Agent Handle Reason field as required.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-agentworkspace.png)


This feature provides a lot of flexibility. Following are few other examples you can set up:
+ If Status = Closed, then the Close Reason field must be populated.
+ If Case Reason = Refund, then the Amount field is required.
+ If Country = USA, the State field is required.

You can apply case field conditions to multiple fields on a template.

**Topics**
+ [Step 1: Create case field conditions](#step1-create-case-field-condition)
+ [Step 2: Add the case field conditions to a template](#step2-add-casefieldcondition-template)
+ [Example field case conditions](#example-case-conditions)
+ [APIs to create field case conditions](#case-conditions-apis)

## Step 1: Create case field conditions
<a name="step1-create-case-field-condition"></a>

1. Log in to the Connect Customer admin website with an **Admin** account, or an account assigned to a security profile that has the following permission in it's security profile: **Cases** - **Case Templates** - **Create**.

1. On the left navigation menu, choose **Agent applications**, **Case field conditions**.

1. Choose **New Field Condition**.

1. On the **Create new field condition** page, use the **Source field** dropdown list to choose the field you want to validate, as shown in the following image:   
![The Conditions section, the Source field dropdown list.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-choose-field-1.png)

1. Choose the operator and the value to check.

   For example, the following image shows when the **State** field equals **New York**, a case field will be required.   
![The Create new field condition page, example settings to make a field required.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-country-2.png)

   The condition is configured as follows:
   + **Source** = **State**
   + **Operator** = **equals**
   + **Value** = **New York**
   + **Required** is selected. A case field that you specify in [Step 2](#step2-add-casefieldcondition-template) will be required when this condition is met.

1. You can add up to 5 field conditions and choose whether they are fulfilled by AND or OR conditions, by choosing the Add Condition button.  
![A conditionally required field with 3 conditions configured.](http://docs.aws.amazon.com/connect/latest/adminguide/images/conditionally-required-with-3-conditions.png)

1. For **Fallback condition**, if the condition is not met, choose this field to set the default experience. 

   For example, if you leave **Fallback condition** unselected, when **Country** does not equal **USA**, then the field this condition is applied to won't be required. So, if you apply the condition to **State**, but the **Country = France**, the **State** field won't be required.

1. Choose **Save**, and then proceed to the next step to add the condition to your template.

## Step 2: Add case field conditions to a template
<a name="step2-add-casefieldcondition-template"></a>

In this step, you specify which case fields the condition will apply to.

1. Log in to the Connect Customer admin website with an **Admin** account, or an account assigned to a security profile that has the following permission in it's security profile: **Cases** - **Case Templates** - **Create** or **Edit**. 

1. On the left navigation menu, choose **Agent applications**, **Case templates**.

1. Choose the case template you want to apply the condition to. 

   You might want the condition to apply to one template but not others. For example, you might want a **Close reason** condition to apply to escalations, but not to general inquires. 

1. In the **Fields** section, choose the settings icon next to the field you want to apply the condition to. The following image shows the settings icon for the **State** field.   
![The case templates page, the settings icon for a field.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-gear-icon-2.png)

1. In the **Modify field conditions for** [{{field}}] use the dropdown box to choose the condition you want to apply to the field. 

   In the following image, the **USA requirements** condition is going to be applied to the **State** field.  
![The Modify field conditions dialog box.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-choose-condition-2.png)

1. Choose **Apply**, and then choose **Save** to save the change to the template.

   The status page indicates which conditions have been applied to a field. The following image shows the **USA requirements** condition is applied to the **State** field.  
![The Fields on a template, the Required column.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-condition-applied-2.png)

## Example case field conditions
<a name="example-case-conditions"></a>

### Example 1: Require agents to enter a reason for closing a case
<a name="example1-case-conditions"></a>

1. Create the following condition:
   + If **Status** is **Closed**, then a case field will be required. If **Status** is not **Closed**, then a case field will be optional. 

   The following image shows how to set up this condition.   
![The Create new field condition page, example settings to make a field optional.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-example1-2.png)

1. Assign this condition to the **Closed Reason** field on the cases template. 

1. Result: When agents save a case and the **Closed Reason** field is blank, they will be prompted to enter a value.

### Example 2: Require agents to provide a reason every time they update a case
<a name="example2-case-conditions"></a>

1. Create the following condition:

   If the **Date/Time Created** field does not equal blank, then a case field will be required. If the **Date/Time Created** field is empty, then that case field is optional. The following image shows how to set up this condition.  
![The Create new field condition page, example settings to make a field optional.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-example2-2.png)

1. Assign this condition to the **Agent Handle Reason** field on the cases template.

1. Result: When agents save a case and the **Agent Handle Reason** is blank, they will be prompted to enter a value.

### Example 3: Require agents to provide a reason when they assign a case to the Escalation queue
<a name="example3-case-conditions"></a>

1. Create the following condition:

   If the **Assigned Queue** field equals the **Escalation queue** Amazon Resource Name (ARN), then a case field will be required. If the **Assigned Queue** field does not equal the **Escalation queue** ARN, then that case field is optional. 
**Tip**  
You can copy the ARN of a queue from the **Queues** page.

   The following image shows how to set up this condition.  
![The Create new field condition page, example settings to make a field optional.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cfc-escalationqueue-2.png)

1. Assign this condition to the **Escalation reason** field on the cases template.

1. Result: When agents assign a case to the **Escalation queue**, and the **Escalation reason** field is blank, they will be prompted to enter a value.

## APIs to create case field conditions
<a name="case-conditions-apis"></a>

Use the following APIs to programmatically create case field conditions and associate them to a template:
+ [CreateCaseRule](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateCaseRule.html): Creates the case field condition.
+ [CreateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html) or [UpdateTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html): Associate the case field condition with the case template.