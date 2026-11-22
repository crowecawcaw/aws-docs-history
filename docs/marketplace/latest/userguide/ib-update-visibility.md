

# Updating EC2 Image Builder product visibility

As an AWS Marketplace seller, you can update your product visibility to change which buyers can view your product in AWS Marketplace. If the visibility status is set to **Public**, your product is visible to all AWS Marketplace buyers. If your product visibility is set to **Limited**, your product is visible only to the AWS account IDs that you allowlist. You can also manage and update this allowlist of AWS account IDs that can see your product. The following sections show you how to update your product visibility and **Limited** visibility allowlist.

**Topics**
+ [Update product visibility](#ib-update-self-service-visibility)
+ [Update the allowlist (preview accounts)](#single-ib-updating-allowlist)

## Update product visibility
<a name="ib-update-self-service-visibility"></a>

To change which buyers can view your product in AWS Marketplace, you can use **Update visibility**. 

**To update visibility**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose **Edit visibility**.

   This button appears when the product is **Limited**, **Public**, or **Restricted**.

1. In the **Update listing visibility** dialog box, under **Change to**, choose the new visibility. The choices depend on the current visibility:
   + **Limited** – **Restricted**, or **Public** after you complete the required steps in **Complete your listing**.
   + **Public** – **Restricted**.
   + **Restricted** – **Public**.

1. (Optional) If you choose **Restricted**, enter a **Replacement product ID**.

   Existing subscribers keep access until their contract ends, and then move to the replacement product. If you leave this field blank, existing subscribers keep access to this product, but they can't renew their contracts.

1. Choose **Update visibility**.

   When you request **Public** visibility, AWS Marketplace reviews your listing before it goes live. This usually takes 3 to 5 business days.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

To publish a **Limited** product from **Complete your listing**, choose **Publish**, and then choose **Submit for review**.

## Update the allowlist (preview accounts)
<a name="single-ib-updating-allowlist"></a>

To change the list of AWS account IDs that can see your product in a **Limited** state, use **Update allowlist**.

**To update the allowlist**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Settings** tab.

1. In the **Allowlisted AWS accounts** section, choose **Edit**.

   If no accounts are allowlisted yet, choose **Add AWS accounts** instead. You can't update the allowlist of a **Restricted** product.

1. In the **Allowlisted AWS accounts** field, add or remove AWS account IDs, separated by commas.

   You can enter up to 5,000 account IDs, each with 12 digits. If you remove the accounts that AWS Marketplace adds automatically to test and preview your product, releasing your product can take longer.

1. Choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.