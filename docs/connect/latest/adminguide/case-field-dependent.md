# Dependent field options

You can create cascading dropdown fields where the options in a single-select field (target) depend on the selection made in another field (source), providing a more intuitive and organized experience for agents.

To set up dependent field relationships, you first create a field options condition that defines the relationship between a source field and a target field. Then, on a case template, apply this condition to control the available options.

For example, you may want the **State/Province** field options to change based on the selected **Country**. To achieve this you would:

1. Create a field options condition that maps country selections to their respective states/provinces.
2. Apply the field options condition to the **State/Province** field on the case template.
   This feature provides a lot of flexibility. Here are a few other examples you can set up:

- If Product Category = Electronics, show subcategories: Computers, Phones, Tablets, Accessories.
- If Department = IT, show relevant issue types: Hardware, Software, Network, Security.
- If Service Type = Premium, show premium-specific options in the Service Level field.
  You can apply field options conditions to multiple dependent field pairs on a template.

## Step 1: Create field options conditions

1. Log in to the Amazon Connect admin website with an **Admin** account, or an account assigned to a security profile that has the following permission in it's security profile: **Cases** - **Case Templates** - **Create**.
2. On the left navigation menu, choose **Agent applications**, **Case field conditions**.
3. Choose **New Field Condition**.
4. On the **Create new field condition** page, select **Field Options** as the condition type.
5. Configure the relationship:
   - **Source field**: Choose the field that will control the options
   - **Target field**: Choose the field whose options will be controlled

6. Set up the option mappings by defining which source field values correspond to which target field options.

For example, the following configuration shows when **Country** equals **United States**, the state field will show US states:

    * **Source field** = **Country**
    * **Target field** = **State/Province**
    * Mapping: "United States" → ["California", "New York", "Texas", "Florida"]

7. Add additional mappings for other source field values as needed.
8. Choose **Save**, and then proceed to the next step to add the condition to your template.

## Step 2: Add field options conditions to a template

In this step, you specify which target field the options condition will apply to.

1. Log in to the Amazon Connect admin website with an **Admin** account, or an account assigned to a security profile that has the following permission in it's security profile: **Cases** - **Case Templates** - **Create** or **Edit**.
2. On the left navigation menu, choose **Agent applications**, **Case templates**.
3. Choose the case template you want to apply the condition to.
4. In the **Fields** section, choose the settings icon next to the target field you want to apply the condition to.
5. In the **Modify field conditions for** [field] use the dropdown box to choose the field options condition you want to apply to the field.
6. Choose **Apply**, and then choose **Save** to save the change to the template.

## Example field options conditions

### Example 1: Show states/provinces based on country selection

1. Create the following condition:
   - **Source field**: **Country**
   - **Target field**: **State/Province**
   - Mappings:
     - "United States" → ["California", "New York", "Texas", "Florida"]
     - "Canada" → ["Ontario", "Quebec", "British Columbia"]

2. Assign this condition to the **State/Province** field on the cases template.
3. Result: When agents select a **Country**, only the relevant states or provinces will be shown.

### Example 2: Show product subcategories based on main category

1. Create the following condition:
   - **Source field**: **Product Category**
   - **Target field**: **Subcategory**
   - Mappings:
     - "Electronics" → ["Computers", "Phones", "Tablets", "Accessories"]
     - "Clothing" → ["Shirts", "Pants", "Shoes", "Accessories"]
     - "Books" → ["Fiction", "Non-Fiction", "Technical", "Children"]

2. Assign this condition to the **Subcategory** field on the cases template.
3. Result: When agents select a **Product Category**, only relevant subcategories will be shown.

### Example 3: Show department-specific issue types

1. Create the following condition:
   - **Source field**: **Department**
   - **Target field**: **Issue Type**
   - Mappings:
     - "IT" → ["Hardware", "Software", "Network", "Security"]
     - "HR" → ["Benefits", "Payroll", "Policy", "Training"]
     - "Finance" → ["Invoicing", "Expenses", "Budget", "Reporting"]

2. Assign this condition to the **Issue Type** field on the cases template.
3. Result: When agents select a **Department**, only issue types relevant to that department will be available.

## APIs for field options conditions

Use the following APIs to programmatically create field options conditions:

- [CreateCaseRule](../APIReference/API_connect-cases_CreateCaseRule.md "../APIReference/API_connect-cases_CreateCaseRule.md"): Creates the field options condition using the "fieldOptions" rule type.
- [CreateTemplate](../APIReference/API_connect-cases_UpdateTemplate.md "../APIReference/API_connect-cases_UpdateTemplate.md") or [UpdateTemplate](../APIReference/API_connect-cases_UpdateTemplate.md "../APIReference/API_connect-cases_UpdateTemplate.md"): Associate the field options condition with the case template.
