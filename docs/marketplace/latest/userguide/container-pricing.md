

# Managing container product pricing on AWS Marketplace

As an AWS Marketplace seller, you can manage and update container product pricing. For container products, you can list free products, Bring Your Own License model (BYOL) products, and paid products for Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), and AWS Fargate. You can add or update pricing dimensions. Depending on your pricing model, you can add contract and usage dimensions. You can also update your pricing terms or your refund policy. For more information, see the following sections.

 For more information about the container product pricing models for AWS Marketplace, see [Container products pricing for AWS Marketplace](pricing-container-products.md).

**Topics**
+ [Adding a pricing dimension](#container-add-pricing-dimensions)
+ [Updating dimension information](#container-update-dimensions-information)
+ [Updating pricing terms](#container-update-pricing-terms)
+ [Updating the refund policy of a product](#container-update-refund-policy)

## Adding a pricing dimension
<a name="container-add-pricing-dimensions"></a>

You can add a pricing dimension to the pricing model that you use for your product billing. For more information about pricing models, see [Container pricing models](pricing-container-products.md#pricing-models-for-server-products).

**Note**  
Container products don't support contract with consumption pricing. For the pricing models that container products support, see [Container pricing models](pricing-container-products.md#pricing-models-for-server-products).  
You can't change your pricing model between contract and usage pricing. Contact the AWS Marketplace support team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console for assistance.

**To add pricing dimensions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Pricing dimensions** section, choose **Update**, and then choose **Add dimensions**.

   The **Pricing dimensions** section appears when your product has pricing dimensions that you define. If **Add dimensions** is unavailable, the menu shows the reason, such as a missing public offer or another change in progress.

1. On the **Add dimensions** step, choose **Add contract dimension** or **Add usage dimension**.

   The button that appears depends on your pricing model.

1. In the panel that opens on the right side of the page, enter the **API identifier**, **Display name**, and **Description**, and then choose **Add dimensions**.

   The API identifier can contain only letters, numbers, and underscores, and can't start with a number. You can't change it after the dimension is created. To add more than one dimension, choose **Add new dimension** before you choose **Add dimensions**.

1. Choose **Next**, and then choose **Submit** on the **Review and submit** step.

   If your product has a public offer, the **Configure prices** step comes first. Enter the prices for the new dimensions, and then choose **Next**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, **Add dimensions** and **Update dimensions** in the **Pricing dimensions** section are unavailable.

## Updating dimension information
<a name="container-update-dimensions-information"></a>

You can change the dimensions information for your product. For more information about pricing models, see [Container pricing models](pricing-container-products.md#pricing-models-for-server-products).

**To update dimension information**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Pricing dimensions** section, choose **Update**, and then choose **Update dimensions**.

1. On the **Update dimension information** page, select the dimension in the **Pricing dimensions** table, and then choose **Update**.

1. In the **Update pricing dimension** panel, change the **Display name** or **Description**, and then choose **Update dimension**.

   The display name can have 1 to 80 characters and can't start with a space. You can't change the API identifier, and the change doesn't affect prices.

1. At the bottom of the page, choose **Update**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, **Add dimensions** and **Update dimensions** in the **Pricing dimensions** section are unavailable.

## Updating pricing terms
<a name="container-update-pricing-terms"></a>

You can change the pricing terms for your product. Pricing terms might need updating if you change the countries in which your product is offered.

**To update pricing terms**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. On the **Public offer** card, choose **Update**, and then choose **Update pricing terms**.

   The **Update** menu appears after your public offer is released.

1. On the **Update pricing terms** page, under **Configure pricing details and duration**, enter your new prices.

1. Choose **Submit**.

Your change request appears on the offer's **Requests log** tab. To open the offer, choose the link under **Offer ID** on the **Public offer** card of the **Procurement** tab. Its status moves from **Under review** to **Update in progress**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the **Update** menu on the **Public offer** card is unavailable.

**Note**  
If you increase the price of a dimension using **Update pricing terms**, you won't be able to update pricing for 90 days. A price increase locks the price for 90 days from the day you initiate the change. This price lock is only in effect for a price increase not a price decrease.

## Updating the refund policy of a product
<a name="container-update-refund-policy"></a>

You can update the refund policy for your product. Updates to the refund policy take effect for all users. For more information, see [Refunds and cancellations in AWS Marketplace](refunds.md). 

**To update the refund policy**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. On the **Public offer** card, choose **Update**, and then choose **Update refund policy**.

   The **Update** menu appears after your public offer is released.

1. On the **Update refund policy** page, under **Refund policy**, enter your refund policy.

   The box shows your current refund policy, and your new text replaces it. Include the terms of your policy and your contact information for buyers to request a refund. You can enter up to 500 characters.

1. Choose **Submit**.

Your change request appears on the offer's **Requests log** tab. To open the offer, choose the link under **Offer ID** on the **Public offer** card of the **Procurement** tab. Its status moves from **Under review** to **Update in progress**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the **Update** menu on the **Public offer** card is unavailable.