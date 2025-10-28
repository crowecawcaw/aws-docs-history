# Manage your granted licenses in License Manager

Licenses that have been granted to you will appear in the License Manager console. Recipients must
accept and activate granted licenses before they can use the product. How you accept and
activate a license depends on whether the license is from AWS Marketplace, if your account is
member account in an organization for AWS Organizations, and whether all features is enabled for
your organization.

Granted licenses require cross-Region replication of license metadata. License Manager
automatically replicates each granted license and its associated information to other
AWS Regions. This enables you to have a centralized view across all Regions where
licenses are granted to you.

###### Licenses from AWS Marketplace and AWS Data Exchange

- Licenses for subscriptions that you purchase are automatically accepted and
  activated.
- If the management account for an organization with all features enabled purchases
  a subscription and distributes licenses to member accounts, the licenses are
  automatically accepted in the member accounts. Either the management account or the
  member accounts can later activate the license.
- If the management account for an organization with only consolidated billing
  features enabled purchases a subscription and distributes licenses to member
  accounts, each member account must accept and activate the license.

###### Licenses from a seller

- You must accept and activate licenses for products that use License Manager to distribute
  licenses.
- If the management account for an organization with all features enabled purchases
  a product and distributes licenses to member accounts, the licenses are automatically
  accepted in the member accounts. Either the management account or the member accounts
  can later activate the license.
- If the management account for an organization with only consolidated billing
  features enabled purchases a product and distributes licenses to member accounts,
  each member account must accept and activate the license.

Console (My licenses)
You can view and manage granted licenses for a single AWS account.

###### To manage granted licenses in your account

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Granted
   licenses**.
3. Choose the **My licenses** tab if it is not the current
   selection.
4. (Optional) Use the filter options, such as the following, to scope the
   list of licenses that are displayed.
   - Product SKU – The product identifier for this license, as
     defined by the license issuer when creating the license. The same
     product SKU might exist across multiple ISVs.
   - Recipient – The ARN of the license recipient.
   - Status – The status of the license. For example,
     **Available**.

5. To view additional information about the license, choose the license ID
   to open the **License overview** page.
6. If the license issuer is an entity other than AWS Marketplace, the initial grant
   status is **Pending acceptance**. Do one of the
   following:
   - Choose **Accept & activate license**. The
     resulting grant status is **Active**.
   - Choose **Accept license**. The resulting grant
     status is **Disabled**. When you are ready to use the
     license, choose **Activate license**.
   - Choose **Reject license**. The resulting grant
     status is **Rejected**. After you reject a license,
     you cannot activate it.

If you don't want to continue using a license that was activated, you can
return to the **License overview** page and choose
**Deactivate license**. If you want to continue using a
license that was deactivated, return to the **License overview**
page and choose **Activate license**.

Console (Aggregated licenses)
You can view your granted licenses that have been aggregated from all accounts
in your organization.

###### Important

In order to use the organization wide view for your granted licenses, you
must first link AWS Organizations using the AWS License Manager console settings. For more
information, see [Settings in License Manager](settings.md "settings.md").

###### To manage granted licenses across your accounts in AWS Organizations

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Granted
   licenses**.
3. Choose the **Aggregated licenses** tab if it is not
   the current selection.
4. (Optional) Use the filter options, such as the following, to scope the
   list of licenses that are displayed.
   - Product SKU – The product identifier for this license, as
     defined by the license issuer when creating the license. The same
     product SKU might exist across multiple ISVs.
   - Beneficiary – The account in your organization that the
     license is granted to.

5. To view additional information about the license, choose the license
   ID to open the license detail page.
6. If the license issuer is an entity other than AWS Marketplace, do one of the
   following:
   - Choose **Activate license**. The resulting grant
     status is **Active**.
   - Choose **Deactivate license**. The resulting grant
     status is **Deactivated**.

If you don't want to continue using a license that was activated, you can
return to the **License overview** page and choose
**Deactivate license**. If you want to continue using a
license that was deactivated, return to the **License overview**
page and choose **Activate license**.

AWS CLI
You can use the AWS CLI to work with your granted licenses.

###### To manage your granted licenses using the AWS CLI:

- [accept-grant](../../../cli/latest/reference/license-manager/accept-grant.md "../../../cli/latest/reference/license-manager/accept-grant.md")
- [create-grant-version](../../../cli/latest/reference/license-manager/create-grant-version.md "../../../cli/latest/reference/license-manager/create-grant-version.md")
- [get-grant](../../../cli/latest/reference/license-manager/get-grant.md "../../../cli/latest/reference/license-manager/get-grant.md")
- [list-licenses](../../../cli/latest/reference/license-manager/list-licenses.md "../../../cli/latest/reference/license-manager/list-licenses.md")
- [list-received-grants](../../../cli/latest/reference/license-manager/list-received-grants.md "../../../cli/latest/reference/license-manager/list-received-grants.md")
- [list-received-grants-for-organization](../../../cli/latest/reference/license-manager/list-received-grants-for-organization.md "../../../cli/latest/reference/license-manager/list-received-grants-for-organization.md")
- [list-received-licenses](../../../cli/latest/reference/license-manager/list-received-licenses.md "../../../cli/latest/reference/license-manager/list-received-licenses.md")
- [list-received-licenses-for-organization](../../../cli/latest/reference/license-manager/list-received-licenses-for-organization.md "../../../cli/latest/reference/license-manager/list-received-licenses-for-organization.md")
- [reject-grant](../../../cli/latest/reference/license-manager/reject-grant.md "../../../cli/latest/reference/license-manager/reject-grant.md")
