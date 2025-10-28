# Getting started with custom billing views

Custom billing views in AWS Billing and Cost Management allow you to make cost management
data accessible to accounts both inside and outside your organization. These views can only be created by
the management account of an organization. By creating and sharing a custom billing view, you provide recipient accounts with access to specific cost management data.
End users of the recipient account can then select from a list of shared custom billing views in
the navigation pane. For example, you can define a custom billing view to contain all cost
management data for a business unit that spans multiple member accounts. When shared with a
relevant accounts, end users can monitor and analyze costs using Cost Explorer across all accounts and resources mapped to that business unit without requiring direct access to the management account. Additionally, you can consolidate cost management data across multiple organizations by creating a custom billing view that combines data from multiple shared billing views, enabling centralized cost monitoring.

## Prerequisites

To create custom billing views, you must use fine-grained AWS Cost Management actions.
For AWS Organizations users, you can use the bulk policy migrator scripts to update policies
from your payer account. You can also use the old to granular action mapping reference to
verify the IAM actions that need to be added. For more information, see the Changes to AWS
Billing, AWS Cost Management, and Account Console Permission blog. Fine-grained actions are
already in effect if you have a standalone AWS account, or you’re part of AWS
Organizations created on or after March 6, 2023, 11:00AM (PDT).

To share custom billing views, you must access
the management account of your organization using an IAM principal that has permissions to
create and share resources using AWS Resource Access Manager (AWS RAM). Permissions are
not required for member accounts who receive a shared custom billing view. When sharing a custom billing view outside of your organization, you must access the recipient account using an IAM principal that has permissions to accept resource invitation shares using AWS RAM. For details about
IAM actions for sharing custom billing views, see [How AWS RAM
works with IAM](../../../ram/latest/userguide/security-iam-policies.md "../../../ram/latest/userguide/security-iam-policies.md") in the _AWS Resource Access Manager User
Guide_.

###### Note

Appropriate IAM actions must be enabled to create, update, delete, and share custom
billing views. For more information about IAM actions for managing custom billing views, see
[Using identity-based policies (IAM policies) for AWS Cost
Management](billing-permissions-ref.md "billing-permissions-ref.md").

## Accessing the console to create custom billing

views

There are two ways to access Billing View in the console to create custom billing
views.

- From the console navigation pane: If you haven’t yet created or don’t have access to
  any custom billing views, you can access Billing View from the navigation pane.
- From Cost Management preferences: You can also access Billing View by navigating to
  Cost Management preferences.

To access Billing View

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. Choose either of the following methods to begin creating your custom billing
   view:
   - From the console navigation pane:
     1. In the navigation pane, select the **Choose billing view**
        menu.
     2. Choose **Create new view** from the dropdown list.

   - From Cost Management preferences:
     1. In the navigation pane, choose **Cost Management
        Preferences**.
     2. Choose the **Billing View** tab.
