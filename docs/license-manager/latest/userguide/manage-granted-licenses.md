

# Manage your granted licenses in License Manager
<a name="manage-granted-licenses"></a>

Licenses that have been granted to you will appear in the License Manager console. Recipients must accept and activate granted licenses before they can use the product. How you accept and activate a license depends on whether the license is from AWS Marketplace, if your account is member account in an organization for AWS Organizations, and whether all features is enabled for your organization.

Granted licenses require cross-Region replication of license metadata. License Manager automatically replicates each granted license and its associated information to other AWS Regions. This enables you to have a centralized view across all Regions where licenses are granted to you.

**Licenses from AWS Marketplace and AWS Data Exchange**
+ Licenses for subscriptions that you purchase are automatically accepted and activated.
+ If the management account for an organization with all features enabled purchases a subscription and distributes licenses to member accounts, the licenses are automatically accepted in the member accounts. Either the management account or the member accounts can later activate the license.
+ If the management account for an organization with only consolidated billing features enabled purchases a subscription and distributes licenses to member accounts, each member account must accept and activate the license.

**Licenses from a seller**
+ You must accept and activate licenses for products that use License Manager to distribute licenses.
+ If the management account for an organization with all features enabled purchases a product and distributes licenses to member accounts, the licenses are automatically accepted in the member accounts. Either the management account or the member accounts can later activate the license.
+ If the management account for an organization with only consolidated billing features enabled purchases a product and distributes licenses to member accounts, each member account must accept and activate the license.

------
#### [ Console (My licenses) ]

You can view and manage granted licenses for a single AWS account.

**To manage granted licenses in your account**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **Granted licenses**.

1. Choose the **My licenses** tab if it is not the current selection.

1. (Optional) Use the filter options, such as the following, to scope the list of licenses that are displayed.
   + Product SKU – The product identifier for this license, as defined by the license issuer when creating the license. The same product SKU might exist across multiple ISVs.
   + Recipient – The ARN of the license recipient.
   + Status – The status of the license. For example, **Available**.

1. To view additional information about the license, choose the license ID to open the **License overview** page.

1. If the license issuer is an entity other than AWS Marketplace, the initial grant status is **Pending acceptance**. Do one of the following:
   + Choose **Accept & activate license**. The resulting grant status is **Active**.
   + Choose **Accept license**. The resulting grant status is **Disabled**. When you are ready to use the license, choose **Activate license**.
   + Choose **Reject license**. The resulting grant status is **Rejected**. After you reject a license, you cannot activate it.

If you don't want to continue using a license that was activated, you can return to the **License overview** page and choose **Deactivate license**. If you want to continue using a license that was deactivated, return to the **License overview** page and choose **Activate license**.

------
#### [ Console (Aggregated licenses) ]

You can view your granted licenses that have been aggregated from all accounts in your organization.

**Important**  
In order to use the organization wide view for your granted licenses, you must first link AWS Organizations using the AWS License Manager console settings. For more information, see [Settings in License Manager](settings.md).

**To manage granted licenses across your accounts in AWS Organizations**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **Granted licenses**.

1. Choose the **Aggregated licenses** tab if it is not the current selection.

1. (Optional) Use the filter options, such as the following, to scope the list of licenses that are displayed.
   + Product SKU – The product identifier for this license, as defined by the license issuer when creating the license. The same product SKU might exist across multiple ISVs.
   + Beneficiary – The account in your organization that the license is granted to.

1. To view additional information about the license, choose the license ID to open the license detail page.

1. If the license issuer is an entity other than AWS Marketplace, do one of the following:
   + Choose **Activate license**. The resulting grant status is **Active**.
   + Choose **Deactivate license**. The resulting grant status is **Deactivated**.

If you don't want to continue using a license that was activated, you can return to the **License overview** page and choose **Deactivate license**. If you want to continue using a license that was deactivated, return to the **License overview** page and choose **Activate license**.

------
#### [ AWS CLI ]

You can use the AWS CLI to work with your granted licenses.

**To manage your granted licenses using the AWS CLI:**
+ [accept-grant](https://docs.aws.amazon.com/cli/latest/reference/license-manager/accept-grant.html)
+ [create-grant-version](https://docs.aws.amazon.com/cli/latest/reference/license-manager/create-grant-version.html)
+ [get-grant](https://docs.aws.amazon.com/cli/latest/reference/license-manager/get-grant.html)
+ [list-licenses](https://docs.aws.amazon.com/cli/latest/reference/license-manager/list-licenses.html)
+ [list-received-grants](https://docs.aws.amazon.com/cli/latest/reference/license-manager/list-received-grants.html)
+ [list-received-grants-for-organization](https://docs.aws.amazon.com/cli/latest/reference/license-manager/list-received-grants-for-organization.html)
+ [list-received-licenses](https://docs.aws.amazon.com/cli/latest/reference/license-manager/list-received-licenses.html)
+ [list-received-licenses-for-organization](https://docs.aws.amazon.com/cli/latest/reference/license-manager/list-received-licenses-for-organization.html)
+ [reject-grant](https://docs.aws.amazon.com/cli/latest/reference/license-manager/reject-grant.html)

------