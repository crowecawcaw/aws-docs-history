# Viewing and creating budgets using billing views

AWS Budgets supports primary and custom billing views, allowing you to create and manage
budgets based on filtered cost and usage data across multiple accounts within your
organization. This feature enables decentralized cloud cost management across your
organization without requiring access to the management account.

When creating a new budget, you can select a billing view to define the scope of cost and
usage data the budget will track. The selected billing view is saved as part of the budget
definition.

When you create a budget using a billing view, the budget only tracks cost and usage data
within the scope of that billing view. For instance, you could create a budget that tracks
costs only for a specific department or project. This allows for more granular budget
management aligned with your organizational structure or cost allocation strategies.

###### To view or create a budget using a billing view

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, select the **Choose billing view** menu. The
   default selection is the **Primary view**, which represents cost
   management data for the account you're currently logged in to.
3. From the dropdown list, choose the billing view you want to use:
   - **Primary view**: Shows cost management data for your current
     account.
   - **Custom views**: Shows filtered cost management data based on
     defined criteria.

4. In the navigation pane, choose **Budgets**.
5. For existing budgets, the budgets list displays only the budgets created using the
   selected billing view.
6. For a new budget, choose **Create budget**, and then
   follow the budget creation workflow. The selected billing view is automatically applied to
   the new budget. For more details, see [Creating
   a budget](budgets-create.md "budgets-create.md").

###### Note

Budgets created with billing views can only be viewed and managed when the corresponding
billing view is selected. When you switch to a different billing view, these budgets will
not be visible in the budgets list.
