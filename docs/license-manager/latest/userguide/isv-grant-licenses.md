

# Grant License Manager seller issued licenses to ISV customers
<a name="isv-grant-licenses"></a>

After you add the new license, you can grant the license to a customer with an AWS account using the AWS Management Console. The recipient must accept the grant before using the license. For more information, see [Granted licenses in License Manager](granted-licenses.md).

Alternatively, if the customer does not have an AWS account, you can use the License Manager API to enable customers to [consume licenses](license-consumption.md).

**To grant a license to a customer using the console**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Choose **Seller Issued Licenses** from the left menu.

1. Choose the ID of the license to open its details page.

1. For **Grants**, choose **Create grant**.

1. For **Grant details**, provide the following information:
   + **Grant name** – The grant name. This is used to enable search capabilities.
   + **AWS account ID** – The AWS account number of the license recipient.
   + **License rights**
     + Select **Consumption** if the recipient can consume granted entitlements.
     + Select **Distribution** if the recipient can distribute granted entitlements to other AWS accounts.
     + Select **Allow on-premise token generation** to authenticate shared licenses without using AWS identities or credentials.
     + Select **Allow submission of usage records** to permit license recipients to emit usage records for usage types.
   + **Home Region** – The AWS Region for the license.

1. Choose **Create grant**.