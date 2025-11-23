# Viewing Billing and Cost Management data as a Bill Transfer account

When the transfer begins, the bill transfer account:

- Receives distinct AWS invoices (for example, distinct consolidated bills) for charges from bill source accounts after the transfer becomes effective. These appear only in the bill transfer account. For more information, see [What is AWS Billing and Cost Management?](billing-what-is.md "billing-what-is.md").
- Controls the cost data visible to the bill source account in the Billing and Cost Management console, using Billing Conductor.
- Gains access to two billing transfer views for each bill source account:

* My view: Shows the billing data that the bill transfer account is financially responsible for.

* Showback/chargeback view: Shows billing data configured through Billing Conductor for showback or chargeback purposes using Billing Conductor.
  The bill transfer account can access these billing views in Cost Explorer, AWS Cost and Usage Report, Budgets, and Bills page.

###### To view transferred invoices reflecting the usage of the bill source accounts

1. Log into the bill transfer account and navigate to **Billing and Cost Management**
2. Select **Bill** Page from the side navigation menu
3. Scroll down to and choose the **Invoice** tab
4. Identify the transferred invoices by bill source account ID column in the invoice tab

###### Note

this is the same way you view your invoices today. Your invoices will continue to be the deposited in the invoice tab. You can identify your invoices by looking at bill source account id column in the invoice tab and searching for your own management account ID.

###### To view the payments for the bill transfer accounts

1. Log into the bill transfer account and navigate to **Billing and Cost Management**
2. Select the **Payments** Page from the side navigation menu
3. In each tab, you will find the payments for the bill source accounts invoices

###### Note

For both Invoices and Payments, you don’t need to enable the Billing View mode. Payments and invoices are billing view agnostic resources, which means that they are associated with your account, not with a billing view (either your primary view, Billing Transfer - My view, or Billing Transfer Showback/chargeback view.

###### To view the Cost Management data for the bill transfer accounts

1. From the home page of the **Billing and Cost Management** Console, enable Billing Views, using the toggle at the top of the side navigation menu
2. When enabling billing view mode, you have the ability to select your desired billing view from a drop down menu. If you have more than 10 billing views, you will see the ‘Click all views’ option at the bottom of the drop down. This will open a modal to navigate across all your billing views.
3. By enabling billing views mode, you will view tools that exclusively support billing views:

Bill Page

Cost Explorer

Cost Explorer Forecasting

Cost Explorer Saved Reports

Data Exports

Budgets 4. Select the desired ‘Billing Transfer view’ reflecting the costs of the bill source accounts. You can choose between ‘My view’ and the ‘Showback/Chargeback view’ 5. To configure resources (e.g., Cost Explorer Saved Reports, Cost and Usage Reports, Budgets) you need to select the specific billing view in scope for the resource you want to create. For more information, see [What is AWS Billing and Cost Management?](billing-what-is.md "billing-what-is.md").
