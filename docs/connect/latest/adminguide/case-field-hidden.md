# Hidden field conditions

You can create dynamic case templates that show or hide fields based on other field values, improving the user experience and reducing complexity for agents.

To make a field conditionally hidden, you first set up a hidden field condition. Then, on a case template, choose which field the hidden field condition should apply to.

For example, you may want to hide the **Advanced Configuration** field unless the user selects **Advanced** as the **User Level**. To achieve this you would:

1. Create a hidden field condition based on whether the **User Level** field equals **Advanced**.
2. Apply the hidden field condition to the **Advanced Configuration** field on the case template.
   This feature provides a lot of flexibility. Here are a few other examples you can set up:

- If Case Type = Basic, hide the Priority field.
- If Customer Type = Internal, hide the Billing Address fields.
- If Status = Draft, hide the Approval fields.
  You can apply hidden field conditions to multiple fields on a template.

## Step 1: Create hidden field conditions

1. Log in to the Amazon Connect admin website with an **Admin** account, or an account assigned to a security profile that has the following permission in it's security profile: **Cases** - **Case Templates** - **Create**.
2. On the left navigation menu, choose **Agent applications**, **Case field conditions**.
3. Choose **New Field Condition**.
4. On the **Create new field condition** page, select **Hidden** as the condition type.
5. Use the **Source field** dropdown list to choose the field you want to evaluate for the condition.
6. Configure the visibility settings:
   - **Default visibility**: Choose whether the field is hidden or shown when no conditions match
   - **Show field when**: Define the conditions that will show the field

7. Choose the operator and the value to check.
8. Choose **Save**, and then proceed to the next step to add the condition to your template.

## Step 2: Add hidden field conditions to a template

In this step, you specify which case fields the hidden condition will apply to.

1. Log in to the Amazon Connect admin website with an **Admin** account, or an account assigned to a security profile that has the following permission in it's security profile: **Cases** - **Case Templates** - **Create** or **Edit**.
2. On the left navigation menu, choose **Agent applications**, **Case templates**.
3. Choose the case template you want to apply the condition to.
4. In the **Fields** section, choose the settings icon next to the field you want to apply the condition to.
5. In the **Modify field conditions for** [field] use the dropdown box to choose the hidden condition you want to apply to the field.
6. Choose **Apply**, and then choose **Save** to save the change to the template.

## Example hidden field conditions

### Example 1: Hide advanced options unless user selects advanced mode

1. Create the following condition: If **User Level** equals **Advanced**, then show the field. Otherwise, hide the field by default.
2. Assign this condition to the **Advanced Configuration** field on the cases template.
3. Result: **Advanced Configuration** will only be visible when agents select **Advanced** in the **User Level**.

### Example 2: Hide billing fields for internal customers

1. Create the following condition: If **Customer Type** does not equal **Internal**, then show the field. If **Customer Type** equals **Internal**, hide the field.
2. Assign this condition to the **Billing Address** field on the cases template.
3. Result: **Billing Address** will be hidden when the **Customer Type** is set to **Internal**.

### Example 3: Hide approval fields for draft cases

1. Create the following condition: If **Status** does not equal **Draft**, then show the field. If **Status** equals **Draft**, hide the field.
2. Assign this condition to the **Approval** field on the cases template.
3. Result: **Approval** will be hidden until the case **Status** changes from **Draft**.

## APIs for hidden field conditions

Use the following APIs to programmatically create hidden field conditions:

- [CreateCaseRule](../APIReference/API_connect-cases_CreateCaseRule.md "../APIReference/API_connect-cases_CreateCaseRule.md"): Creates the hidden field condition using the "hidden" rule type.
- [CreateTemplate](../APIReference/API_connect-cases_CreateTemplate.md "../APIReference/API_connect-cases_CreateTemplate.md") or [UpdateTemplate](../APIReference/API_connect-cases_UpdateTemplate.md "../APIReference/API_connect-cases_UpdateTemplate.md"): Associate the hidden field condition with the case template.
