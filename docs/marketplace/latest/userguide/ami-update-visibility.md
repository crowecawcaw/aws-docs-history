

# Updating AMI-based product visibility

As an AWS Marketplace seller, you can update your product visibility to change which buyers can view your single AMI product in AWS Marketplace. If the visibility status is set to **Public**, your product is visible to all AWS Marketplace buyers. If your product visibility is set to **Limited**, your product is visible only to the AWS account IDs that you allowlist. You can also manage and update this allowlist of AWS account IDs that can see your product. The following sections show you how to update your product visibility and **Limited** visibility allowlist.

**Topics**
+ [Update product visibility](#ami-update-self-service-visibility)
+ [Update the allowlist (preview accounts)](#single-ami-updating-allowlist)

## Update product visibility
<a name="ami-update-self-service-visibility"></a>

To change which buyers can view your product in AWS Marketplace, you can use **Update visibility**. 

**To update visibility**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose **Edit visibility**.

   This button appears when the product is **Limited**, **Public**, or **Restricted**.

1. In the **Update listing visibility** dialog box, under **Change to**, choose the new visibility.

   The choices depend on the current visibility:
   + **Limited** – You can choose **Restricted**. After you complete the required steps in **Complete your listing**, you can also choose **Public**.
   + **Public** – You can choose **Restricted**.
   + **Restricted** – You can choose **Public**.

   If only one choice applies, the dialog box shows it without options to select.

1. (Optional) If you choose **Restricted**, enter a **Replacement product ID**.

   Use `prod-` followed by 13 or 25 letters and numbers, or a UUID. Existing subscribers keep access until their contracts end, and then move to the replacement product. If you leave this field blank, existing subscribers keep access to this product, but they can't renew their contracts.

1. Choose **Update visibility**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

When you move a **Limited** product to **Public**, AWS Marketplace reviews your listing against its policies before it goes live. Reviews typically take 3 to 5 business days. To start the same review from **Complete your listing**, choose **Publish**, and then choose **Submit for review**.

## Update the allowlist (preview accounts)
<a name="single-ami-updating-allowlist"></a>

To change the list of AWS account IDs that can see your product in a **Limited** state, use **Update allowlist**.

**To update the allowlist**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Settings** tab.

1. In the **Allowlisted AWS accounts** section, choose **Edit**.

   If no accounts are allowlisted yet, choose **Add AWS accounts** instead.

1. On the **Update allowlist** page, in the **Allowlisted AWS accounts** field, add or remove AWS account IDs.

   The field shows the accounts that are allowlisted now. Enter 12-digit IDs separated by commas, up to 5,000 IDs.

   The page also lists the AWS accounts that AWS Marketplace adds automatically to test and preview your product. If you remove these accounts, releasing your product can take longer.

1. Choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

**Note**  
You can't update the allowlist of a **Restricted** product.