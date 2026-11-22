

# Creating an approval chain

An approval chain is the ordered list of email approvers who review a purchase. You need at least one verified email approver before you can create an approval chain. You can also create a new chain while you create a rule.

**To create an approval chain**

1. Using your AWS management account or a delegated administrator account, open [Approvers and routing](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?tab=email-approvers) in the AWS Marketplace console. It's under **Buying policies** in the left navigation pane.

1. On the **Email approvers and chains** tab, in the **Email approval chains** table, choose **Create approval chain**.

1. Under **Chain details**, enter a **Chain name**, for example, **Manager → Finance**. Optionally, enter a **Description**.

1. Under **Approval level 1**, enter a **Level name**, and then choose up to 10 verified email approvers under **Approvers**.

1. (Optional) To add more levels, choose **Add another level**. You can add up to 6 levels. For each level after level 1, you can enter an amount in **Starts reviewing at**. Leave it blank and the level reviews after the previous level is complete. Enter a spend amount and the level reviews only purchases at or above it. Each amount must be greater than any earlier level's amount.

1. Choose **Create approval chain**.

To change an approval chain, select it in the **Email approval chains** table and choose **Edit**. A chain's levels and amounts are used by every rule that routes to it, so a change applies to all of those rules. To change the amounts for one rule only, create a separate chain for it. You can't delete an approval chain after you create it.