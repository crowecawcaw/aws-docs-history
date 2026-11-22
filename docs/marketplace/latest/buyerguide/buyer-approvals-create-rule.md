

# Creating a procurement approval rule

A rule defines which purchases need review and where each request is sent. Before you create a rule that routes to email approvers, add at least one verified email approver. Before you create a rule that routes to an external system, connect your procurement system. Your organization can have up to 10 rules in total, including rules created in Private Marketplace experiences.

**To create a procurement approval rule**

1. Using your AWS management account or a delegated administrator account, open [Procurement approval rules](https://console.aws.amazon.com/marketplace/buying-policies/procurement-approval-rules) in the AWS Marketplace console. It's under **Buying policies** in the left navigation pane.

1. Choose **Create rule**.

1. On the **Choose action and routing** page, under **Action on rule match**, choose **Require approval** or **Decline purchase**.

1. If you chose **Require approval**, under **Approval routing**, choose one of the following:
   + **AWS Marketplace console** – Your AWS management account or delegated administrator manages approval requests in the AWS Marketplace console.
   + **Email approval chain** – Under **Email approval chain**, choose a saved chain, or choose **Create a new chain** to build one without leaving the rule. A new chain is saved when you create the rule. A saved chain's spend amounts can only be changed on the chain's page.
   + **External system** – The rule routes to your connected procurement system, shown under **Connected system**.

   Choose **Next**.

1. On the **Define rule details and criteria** page, enter a **Rule name**, for example, **High spend requires approval**. Rule names must be unique in your organization.

1. Under **Approval criteria**, choose one or more criteria, and then set their values. The rule applies only to purchases that match all selected criteria.
   + **Purchase amount** – Choose a **Currency**, and then enter a **From** amount, an **Up to** amount, or both. The rule matches only purchases in the selected currency. To set amounts for another currency, create a separate rule. The purchase amount is the total contract value of the purchase's fixed charges. It doesn't include usage-based (pay-as-you-go) charges, because those amounts aren't known at the time of purchase. To require approval for usage-based purchases, use **Pricing type**.
   + **Pricing type** – For example, **Contract pricing with upfront payment**, **Usage-based (pay-as-you-go)**, or **Free**.
   + **Delivery method** – **SaaS**, **AMI**, **Professional Services**, or **Machine Learning**.
   + **Offer type** – **Private** or **Public**.
   + **Publisher** – Specific software publishers or service providers. This refers to the manufacturer of the software, not the selling entity.
   + **Excluded publisher** – Publishers that the rule doesn't apply to. Other matching rules still apply.

1. Choose **Next**. On the **Review and create** page, check the rule, and then choose **Create approval rule**.

## Editing and deleting rules
<a name="buyer-approvals-manage-rules"></a>

The **Procurement approval rules** page lists your rules on two tabs, **Require approval rules** and **Decline purchase rules**. The **Procurement policy summary** describes, in one paragraph, how your rules govern purchases.
+ To edit a rule, select it and choose **Edit**. Make your changes, and then choose **Save changes**.
+ To delete one or more rules, select them, choose **Delete**, and then confirm. Deleting a rule stops new purchase requests from being sent to it. Pending requests that already matched the rule aren't affected and continue through their current approvals.