

# Getting started with professional services products in AWS Marketplace

As a seller, you can offer professional services to AWS Marketplace buyers. Professional services include services to assess, migrate, support, manage, and train others in how to use AWS services and products in AWS Marketplace. Your product definition tells buyers about the services that you offer and explains why they should select your company for those services. AWS Marketplace allows buyers to contact you. You agree on a contract, and then you create a private offer that allows the buyer to purchase your services for a fixed cost. The following sections show you how to get started with a professional services product, providing the steps that you need to create your first product and offer it to your customers. 

The following video explains more about listing professional services products in AWS Marketplace.

[![AWS Videos](https://img.youtube.com/vi/8inkD7mgrLk/0.jpg)](https://www.youtube.com/watch?v=8inkD7mgrLk)


**Topics**
+ [Prerequisites](#proserv-prereqs)
+ [Create a professional services product](#proserv-create)
+ [Create private offers](#proserv-create-offer)
+ [Edit product information](#proserv-edit-product)
+ [Editing product pricing](#proserv-edit-pricing)
+ [Edit product visibility](#proserv-edit-visibility)
+ [Remove a professional services product](#proserv-remove-product)

## Prerequisites
<a name="proserv-prereqs"></a>

To sell professional services on AWS Marketplace, you must complete the following prerequisites:
+ Have access to AWS Partner Central. This is the tool that you use to register as a seller and manage the products that you sell on AWS Marketplace. To learn more about getting access to AWS Partner Central, see [Policies and permissions for AWS Marketplace sellers](detailed-management-portal-permissions.md).
+ Register as an AWS Marketplace seller and submit your tax and banking information. You must provide a non-UK bank account to receive disbursements. To learn more about becoming an seller, see [Getting started as an AWS Marketplace seller](user-guide-for-sellers.md). 
+ You must have a professional services product to offer that is related to an AWS service or at least one public product in AWS Marketplace. Your product must either directly support those products, or offer services that drive subscriptions to those products.

**Note**  
Your product must be listed in at least one of these primary categories: Assessments, Implementation, Managed Services, Premium Support, or Training.   
For more information about professional services product guidelines, see [Requirements for professional services products on AWS Marketplace](proserv-product-guidelines.md).

## Create a professional services product
<a name="proserv-create"></a>

The following procedures describe how to create a new professional services product.

**To create a professional services product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose **Create product**.

1. For **Product name**, enter a unique name of 2 to 72 characters.

1. For **Product type**, choose **Professional service**.

1. (Optional) Under **Tags**, add tags for the product.

1. Choose **Create product**.

AWS Partner Central creates the product with **Draft** visibility and opens the product's page. Next, add your product details.

**To provide product details**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Under **Step 1: Product details**, choose **Start** on the **Provide product details** card.

   To link up to 10 AWS Marketplace products that your service supports, use the optional **Associated products** card in this step. This card is available after you complete **Provide product details**.

1. Enter your product details.

   For the details that you must provide, see [Providing details for a professional services product in AWS Marketplace](proserv-product-details.md).

1. Choose **Save**.

1. At the top of the page, choose **Advance to add-ons**.

   This button is available after you complete the required cards under **Step 1: Product details**.

1. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

Your product moves to **Limited** visibility. Each change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

When your product is initially created, it's only accessible to your AWS account (the one you used to create the product). When your product has **Limited** visibility, choose **View on AWS Marketplace** on the product's page to see the product details as buyers see them. This detail listing isn't available to other AWS Marketplace users, unless you extend a private offer to them.

To learn how to make the product available publicly, see [Edit product visibility](#proserv-edit-visibility).

## Create private offers
<a name="proserv-create-offer"></a>

When a potential buyer views your product on AWS Marketplace, they can't purchase it directly. When they attempt to subscribe, they are redirected to request a [private offer](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-overview.html) from you. AWS Marketplace sends an email message to your AWS Marketplace seller account root user email address, informing you that the customer has requested a private offer. The following procedure describes how to respond to this request. 

**Note**  
When you create a private offer higher than $250,000 through AWS Partner Central, additional approval may be required. For more information, contact the Private Offer Success Team (POST), Vendor Finance Success (VFS), or Seller Reporting teams on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1). 

Before you create the offer, contact the buyer to resolve any questions about the request, and agree on the offer terms. The buyer isn't obligated to purchase your product.

For a professional services product, the offer's pricing model can be **Variable payments**, **Installment plan**, or **Upfront payment**. For variable payments, see [Pricing professional service products in AWS Marketplace](proserv-variable-payments.md).

**To create a private offer for a professional services product**

1. Open the [**Offers**](https://console.aws.amazon.com/partnercentral/offers) page in AWS Partner Central, and sign in to your seller account.

1. On the **Private offers** tab, choose **Create private offer**.

1. For **Product type**, choose **Professional service product**, and then choose your product under **Product**.

   If the page shows **Offer type**, choose **Direct private offer** first.

1. Choose **Continue to offer details**.

   Generating the offer ID can take up to 30 seconds. Don't close or refresh the page.

1. Complete each step of the offer, and then choose **Next**.

   For the fields on each step, see [Drafting and publishing the private offer](creating-private-offer.md#drafting-and-publishing-private-offer).

1. On the **Review and create** step, choose **Create offer**.

Your offer can take some time to publish. After it's published, select it on the **Private offers** tab, choose **Actions**, and then choose **Copy offer URL**. Send the URL to the buyer in an email message. To change a published offer, select it, and then choose **Edit**.

## Edit product information
<a name="proserv-edit-product"></a>

The following procedure describes how to edit the product information for an existing professional services product.

**To edit product information**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Product details** tab.

1. In the **Product details** section, choose **Edit**.

1. On the **Provide product details** page, make your changes.

   For the fields that you can edit, see [Providing details for a professional services product in AWS Marketplace](proserv-product-details.md).

1. Choose **Save**.

Your change request appears on the product's **Change history** tab as **Provide product details**. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While any of these requests is in progress, you can't edit product details, images and videos, the trust center, or associated products.

To change the products associated with your service, choose **Edit** in the **Associated products** section of the **Product details** tab, or **Add** if there are none. You can choose up to 10 products. This change request is named **Update associated products**.

## Editing product pricing
<a name="proserv-edit-pricing"></a>

The following procedure describes how to edit the pricing information for an existing professional services product.

**To edit product pricing**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Pricing dimensions** section, choose **Update**, and then choose **Add dimensions**.

   The section appears after your product has at least one pricing dimension, and you can't edit dimensions while your product has **Restricted** visibility. To change the display name or description of an existing dimension, choose **Update dimensions** instead.

1. On the **Add dimensions** step, choose **Add contract dimension**.

1. For each new dimension, enter a **Display name** and a **Description**, and then choose **Add dimensions**.

   A display name can have up to 80 characters, and a description up to 1,000 characters. AWS Partner Central generates the API identifier from the display name.

1. Choose **Next**, and then on the **Review and submit** step, choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

## Edit product visibility
<a name="proserv-edit-visibility"></a>

A new product starts with **Draft** visibility and moves to **Limited** when you choose **Advance to add-ons**. A product with limited visibility is visible only from your account. You can make the product publicly visible in AWS Marketplace. The following procedure describes how to edit the visibility of an existing professional services product.

**Note**  
You don't need to add buyers to the allowlist. If you have at least one other product with **Public** visibility, you can create private offers on a professional services product with **Limited** visibility, and the buyers that you extend them to can accept them.

**To edit product visibility**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose **Edit visibility**.

   This button appears when your product has **Limited** visibility.

1. In the **Update listing visibility** dialog box, for **Change to**, choose **Public** or **Restricted**.

   For a product with **Limited** visibility, **Public** appears only when **Publish** is available under **Step 2: Add-ons** on the **Complete your listing** progress bar.

1. Choose **Update visibility**.

Your change request appears on the product's **Change history** tab as **Publish product** or **Restrict product**. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

Another way to publish a product with **Limited** visibility is the **Complete your listing** progress bar: choose **Step 2: Add-ons**, choose **Publish**, and then choose **Submit for review**.

**Note**  
To make a product visible in the public AWS Marketplace catalog requires a product review by the AWS Marketplace Seller Operations team to ensure that the product meets the product guidelines (see [Requirements for professional services products on AWS Marketplace](proserv-product-guidelines.md)). The request can take several days to complete.

## Remove a professional services product
<a name="proserv-remove-product"></a>

The following procedure describes how to remove an existing professional services product.

**Note**  
Removing a professional services product would not affect active private offers.

**To remove a product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose **Edit visibility**.

1. In the **Update listing visibility** dialog box, for **Change to**, choose **Restricted**.

1. (Optional) For **Replacement product ID**, enter the ID of the product that existing subscribers move to when their contract ends.

1. Choose **Update visibility**.

Your change request appears on the product's **Change history** tab as **Restrict product**. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

**Note**  
The request can take several days to complete. Products with active offers will be moved to restricted state until the last active subscription or contract is completed and then removed from AWS Marketplace. Restricted status means that existing users can continue to use the product. However, the product will no longer be visible to the public or be available to new users.