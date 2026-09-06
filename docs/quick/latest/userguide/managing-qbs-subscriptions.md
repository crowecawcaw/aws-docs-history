

# Configure Amazon Quick subscriptions
<a name="managing-qbs-subscriptions"></a>

You can purchase user subscriptions to get discounted pricing on Amazon Quick. When you invite additional users to Quick, you're charged for those accounts on a month-by-month basis.

To understand how Amazon Quick subscription names on the pricing page map to user roles in the admin console, see [Understanding Amazon Quick subscriptions and roles](https://docs.aws.amazon.com/quicksuite/latest/userguide/user-types.html).

When you purchase an annual subscription, you pay for a Quick user account on an annual rather than monthly basis. With an annual subscription, you receive a discounted price in return for the extended time commitment. You don't need to purchase an annual subscription to create or add users. 

When you purchase a set of standard user subscriptions, you choose the number of accounts you want to cover. You also choose when to start the subscriptions (any time from the month following the current month, to one year in the future) and whether to autorenew them. All subscriptions that you purchase together must use the same values for these settings.

You can edit an existing set of user subscriptions to change whether it autorenews. If the set is not yet active, you can also change the number of subscriptions it covers, or delete it entirely.

**Topics**
+ [Viewing current subscriptions](#view-subscriptions)
+ [Purchase subscriptions](#buy-subscriptions)
+ [Editing a subscription](#edit-subscriptions)
+ [Delete a subscription](#delete-subscriptions)
+ [Upgrading or downgrading user subscriptions](#upgrading-subscription)
+ [Understanding Amazon Quick user billing](understanding-quick-user-billing.md)

## Viewing current subscriptions
<a name="view-subscriptions"></a>

Use the following procedure to view your current user subscriptions.

**To view your current user subscriptions**

1. Choose your user name on the application bar and then choose **Manage Quick**.

1. Choose **Manage pricing**.

1. Use the subscription meter to see how many accounts you have and how they are billed. In the following example, the account has 21 users total:
   + Seven users with annual subscriptions. Only currently active subscriptions are shown here.
   + 13 month-to-month users.

   Pause over any section of the meter bar to display details about that user segment.

1. Use the information in the subscriptions table to see what current and future subscriptions you have.

## Purchase subscriptions
<a name="buy-subscriptions"></a>

Use the following procedure to purchase subscriptions.

**To purchase subscriptions**

1. Choose your user name on the application bar and then choose **Manage Quick**.

1. Choose **Manage pricing**.

1. Navigate to the **Authors and Admins** section, and then choose **Purchase plan**.

1. Choose or enter the number of subscriptions you want.

1. Choose the month and year when the subscriptions will start.

1. Choose whether the subscriptions autorenew.

1. Choose **Purchase**.

## Editing a subscription
<a name="edit-subscriptions"></a>

Use the following procedure to edit subscriptions.

**To edit subscriptions**

1. Choose your user name on the application bar and then choose **Manage Quick**.

1. Choose **Manage pricing**.

1. Next to the set of subscriptions you want to change, choose **Manage**.

1. (Optional) If the subscriptions haven't started yet, change the number of subscriptions.

1. Choose whether the subscriptions autorenew.

1. Choose **Save changes**.

## Delete a subscription
<a name="delete-subscriptions"></a>

**Warning**  
Deleting Amazon Quick subscriptions affects user access. When you delete subscriptions:  
Users covered by deleted subscriptions may lose access to Quick features and content
Subscription changes affect your entire organization's access to Quick capabilities
Deleted subscriptions cannot be recovered - you must purchase new subscriptions to restore access
**Before proceeding:** Verify that affected users have alternative access methods and understand the implications of subscription changes.

Use the following procedure to delete subscriptions. You can only delete subscriptions that haven't started yet.

**To delete subscriptions**

1. Choose your user name on the application bar and then choose **Manage Quick**.

1. Choose **Manage pricing**.

1. Next to the set of subscriptions that you want to delete, choose **Edit**.

1. Choose **Delete Subscription**.

**Note**  
If you use AWS Key Management Service or AWS Secrets Manager with Amazon Quick, you are billed for access and maintenance as described in the pricing pages for each AWS product. For more information on how these products are billed, see the following:  
[AWS Key Management Service Pricing page](https://aws.amazon.com/kms/pricing)
[AWS Secrets Manager Pricing page](https://aws.amazon.com/secrets-manager/pricing)
In your billing statement, the costs are itemized under the appropriate product and not under Amazon Quick.

## Upgrading or downgrading user subscriptions
<a name="upgrading-subscription"></a>

Amazon Quick Professional and Amazon Quick Enterprise are per-user subscriptions that you assign through group membership. To change a user's subscription, you move them between the groups that are mapped to Quick roles. The Reader Pro role corresponds to the Amazon Quick Professional subscription, and the Author Pro role corresponds to the Amazon Quick Enterprise subscription. For more information about how subscriptions map to roles, see [Understanding Amazon Quick subscriptions and roles](https://docs.aws.amazon.com/quicksuite/latest/userguide/user-types.html).

For a full comparison of the capabilities included with each subscription and current per-user pricing, see [Amazon Quick pricing](https://aws.amazon.com/quick/pricing/).

### Upgrading from Professional to Enterprise
<a name="upgrade-to-enterprise"></a>

To upgrade a user from the Amazon Quick Professional subscription to the Amazon Quick Enterprise subscription, move the user to a group that is mapped to the Author Pro role. If you use IAM Identity Center or Active Directory, you make this change by updating the user's group membership in your identity provider. For the procedure, see [Changing a user's role](https://docs.aws.amazon.com/quicksight/latest/user/updating-user-accounts-enterprise.html).

Users can also request an upgrade themselves when they encounter a feature or usage limit that requires the Enterprise subscription. Depending on your organization's settings, these requests can process automatically or require administrator approval. For more information, see [User-driven license upgrades](https://docs.aws.amazon.com/quicksuite/latest/userguide/user-driven-upgrades.html).

After the change takes effect, the user has immediate access to Enterprise capabilities. Changes to users or groups can take up to five minutes to propagate.

### Downgrading from Enterprise to Professional
<a name="downgrade-to-professional"></a>

To downgrade a user from the Amazon Quick Enterprise subscription to the Amazon Quick Professional subscription, move the user out of the group that is mapped to the Author Pro role and into a group that is mapped to the Reader Pro role. As with an upgrade, you make this change through your identity provider when you use IAM Identity Center or Active Directory. For the procedure, see [Changing a user's role](https://docs.aws.amazon.com/quicksight/latest/user/updating-user-accounts-enterprise.html).

**Important**  
If a user belongs to multiple groups that are mapped to different roles, they keep the subscription that grants the broadest level of access. To complete a downgrade, remove the user from every group that is mapped to the Author Pro role.

After you downgrade a user, they lose access to the capabilities included only with the Amazon Quick Enterprise subscription. Before you downgrade, make sure any assets the user owns that you want to keep are transferred to another user. Changes to users or groups can take up to five minutes to propagate.

**Note**  
For questions about billing adjustments or refunds related to a subscription change, contact [AWS Support](https://aws.amazon.com/contact-us/).