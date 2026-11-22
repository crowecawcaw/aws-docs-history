

# Setting up level sharing for a Reserved Instance

Level sharing lets you choose which accounts can use the discount from a specific Reserved Instance. Use level sharing when a specific commitment was purchased for a particular team, project or business unit. You set up level sharing in the **Sharing preferences** section on the **Reserved Instance details** page.

Level sharing works within your account-level sharing preferences. It can narrow the set of accounts that receive a commitment's discount, but it can't extend the discount to an account whose sharing is deactivated.
+ The commitment applies first to eligible usage in the account that owns it.
+ The remaining discount applies to the accounts defined in the commitment's level sharing preference.
+ With prioritized mode, any remaining discount then applies to other sharing-activated accounts in the organization. With restricted mode, the discount doesn't apply outside the defined accounts.
+ A level sharing preference on a commitment overrides the organization's group sharing preference for that commitment. Commitments without a level sharing preference follow the organization's group or open sharing preference.

Level sharing uses a Cost Category with the Benefit level sharing association. Each Cost Category rule defines a set of accounts that can use a commitment. Only the **Accounts** dimension can be used in Cost Category rules for sharing. For all Cost Category requirements, see [Cost Category requirements for sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html#sharing-cost-category-requirements) in the *AWS Billing and Cost Management User Guide*.

**Note**  
Only the management account can set up level sharing. Retired Reserved Instances don't have a **Sharing preferences** section.<a name="manage-ri-sharing-preference-howto"></a>

**To configure level sharing for a Reserved Instance**

1. Sign in to the management account and open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Reservations**, choose **Inventory**.

1. Choose the Reserved Instance to open its detail page.

1. In the **Sharing preferences** section, choose **Manage sharing preference**.

1. For **Mode**, choose **Prioritized** or **Restricted**.

1. For **Cost category**, select a Cost Category with the Benefit level sharing association, or choose **Create cost category**. If you don't see a Cost Category that you just created, choose the refresh button.

1. For **Rule**, select the rule that defines the accounts that can use this commitment. The rule must include the account that owns the Reserved Instance.

1. Review **Selected rule details** to confirm the Cost Category, rule and accounts, and then choose **Save**.<a name="remove-ri-sharing-preference-howto"></a>

**To remove a level sharing preference**

1. Open the Reserved Instance detail page from **Inventory**.

1. In the **Sharing preferences** section, choose **Remove sharing preference**.

After you remove the preference, the commitment follows the organization's sharing preference.