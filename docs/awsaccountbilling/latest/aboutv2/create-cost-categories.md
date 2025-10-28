# Creating cost categories

Cost allocation helps you map and assign your AWS Cloud costs to the correct groups
within your organization. To allocate these costs, create cost categories. Cost
categories are composed of rules.

There are two types of rules:

1. Rules to group costs
2. Rules to split costs

**Rules to group costs**

Define rules to group costs by using one or more of the following
dimensions:

- Accounts
- Cost allocation tags
- Charge Type, such as credits and refunds
- Service
- Region
- Usage Type, such as BoxUsage:t2.micro
- Billing Entity, such as AWS and AWS Marketplace

Rules are evaluated in the order in which they're defined.

###### Example: Rules to group costs

Your engineering department has projects
`Alpha` and
`Beta`, and the marketing department has
project `Gamma`.

All resources are tagged with the project name that they're used for,
such as `Project:Alpha`,
`Project:Beta`, or
`Project:Gamma`.

You create a cost category named `Department`
to allocate costs to the `Marketing` and
`Engineering` departments. For the
`Department` cost category, you define your
rules as:

- Rule 1: If a cost has a cost allocation tag of
  `Project:Alpha` or
  `Project:Beta`, then assign the
  cost to
  `Department:Engineering`.
- Rule 2: If a cost has a cost allocation tag of
  `Project:Gamma`, then assign the
  cost to `Department:Marketing`.
  You can also provide a default name for uncategorized costs. In this
  example, costs associated with untagged resources should be allocated to
  the `IT` department

- Rule 1: If a cost has a cost allocation tag of
  `Project:Alpha` or
  `Project:Beta`, then assign the
  cost to
  `Department:Engineering`.
- Rule 2: If a cost has a cost allocation tag of
  `Project:Gamma`, then assign the
  cost to `Department:Marketing`.
- For all other costs, assign it to
  `Department:IT`.
  In this example, the cost category name is
  `Department`. The cost category values are
  `Engineering`,
  `Marketing`, and
  `IT`.

**Rules to split costs**

Costs that are allocated to one cost category value can be split among
others. In this example, if `IT` costs should be
split between `Engineering` and
`Marketing` departments in a 70:30 ratio, you
can define a split charge rule to perform that allocation.

When you create your cost category, you can provide additional details
such as:

- **Effective Date** – Set the start date
  for your cost category. By default, this date will be set to the
  current month. If you choose a prior month, your cost category rules
  are then applied retroactively from that date.
- **Tags** – To control access to who can
  edit this cost category, add a tag to the cost category. You then
  update your IAM policy to allow or deny access to that cost
  category. For example, you can add a tag
  `Role:Administrator` to your cost
  categories and then update an IAM policy to explicitly allow
  specific roles access to cost categories that have that tag.

Dy default, regular accounts and the management account in AWS Organizations have access to
create cost categories.

###### Tip

To request a backfill of your cost data in your AWS Cost and Usage Report, create a support case. In your support case, specify the report name and the billing period that you want backfilled. For more information, see [Contacting Support](billing-get-answers.md#billing-support "billing-get-answers.md#billing-support").

Use the following procedure to create a cost category. After you create a cost
category, wait up to 24 hours for your usage records to be updated with the cost
category values.

###### To create a cost category

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose
   **Cost Categories**.
3. Choose **Create cost category**. You can use the cost preview panel
   as reference as you update your rules.
4. Next to **Group your costs**, enter the name of your
   cost category. Your cost category name must be unique within your
   account.
5. Use either the **Rule Builder** or **JSON
   editor** to define your cost categories.

For more information about the JSON request syntax, see the [Cost category](../../../aws-cost-management/latest/APIReference/API_CostCategory.md "../../../aws-cost-management/latest/APIReference/API_CostCategory.md") section in the
_AWS Billing and Cost Management API Reference_ 6. For **Rule builder**, choose **Add
rule**. 7. Choose **Rule type**, either **Manually define how to
group costs (Regular rule)** or **Automatically group costs
by account or tag (Inherit rule)**. 8. For regular rule, choose if your costs meets **all** or
**any** of the conditions. 9. Choose a billing **Dimension** from the list.

    1. For a regular rule type, you can choose **Accounts**,
     **Service**, **Charge Type** (for
     example, `recurring reservation fee`), **Tag key**,
     **Region**, **Usage Type**, **Cost Category**, or **Billing Entity**. (You can choose **Cost
     Category** to create hierarchical relationships among your
     cost categories.)
    2. For an inherited value rule type, you can choose
     **Account** or **Tag key**
     (Cost allocation tags key).

10. For a regular rule type, choose **Operator** from the
    dropdown list. Your options are **Is**,
    **Contains**, **Starts with**, and
    **Ends with**.

###### Note

**Contains**, **Starts with**, and
**Ends with** are only supported with Accounts and Tag
dimensions. If you use these operators with Accounts, the engine evaluates
against account name, and not account ID. 11. Choose a filtered value or enter your own value for your
**Dimension** in the attribute selector.

###### Note

The **Account** dimension uses account names, not account
IDs for the inherited cost category value. 12. Choose **Add a condition** as needed and repeat steps 9 - 11. 13. For **Group costs together as**, enter a cost category
value. 14. Choose **Create rule**. 15. (Optional) Add a default value. It categorizes all unmatched costs to this
value. 16. (Optional) To rearrange the rule order, use the arrows or change the number on the top
right of each rule.

Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that cost category value. 17. (Optional) To remove a rule, select the rule and choose
**Delete**. 18. Choose **Next**. 19. (Optional) To split your cost, choose **Add a split
charges**. For more information about split charge rules, see [Splitting charges within
cost categories](splitcharge-cost-categories.md "splitcharge-cost-categories.md").

    1. Choose **Add a split charge**.
    2. Under **Source value**, choose your cost category
     value.
    3. Under **Target values**, choose one or more
     cost category values you wish to allocate split charges to.
    4. Under **Charge allocation method**, choose how you
     want to allocate your costs. Your choices are
     **proportional**, **fixed**, and
     **even split**.
    5. For **fixed** charge allocation, enter the percentage
     amount to allocate each target cost category value.
    6. Repeat step 19 as needed.

20. Choose **Next**.
21. (Optional) To add a lookback period for your cost category rules, choose
    the month from when you want to retroactively apply the rules.
22. (Optional) To add a tag, choose **Add new resource tag** and
    enter a key and value.
23. Choose **Create cost category**.

## Understanding the cost preview panel

The cost preview panel shows you in real time how your costs group together or split apart
as you create or update your cost categories rules. The results you see in the
cost preview panel is an estimate based on your month-to-date net amortized
cost.

Here are some things to keep in mind as you use the cost preview panel:

- The cost preview results might not be accurate if your rules have complex conditions. For example, containing too many matched values with `Contains`, `Starts With`, `Ends With` operators.

For a more precise results, save your rules and check the cost categories details page.

- If your rules are too complex or takes too long to calculate in real time, the preview will not show a cost breakdown.
