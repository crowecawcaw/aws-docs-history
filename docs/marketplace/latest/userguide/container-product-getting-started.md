

# Getting started with container products

As an AWS Marketplace seller, you can create container-based software products. Container products consist of delivery options that are a set of container images and deployment templates that go together. The following topic shows you how to get started with container products.
+ [Product lifecycle](#container-product-lifecycle)
+ [Prerequisites](#container-prereq)
+  [Step 1: Create your container product](#create-initial-container-product) 
+ [Step 2: Create an initial listing](#container-initial-listing)
+ [Step 3: Add an initial version of your product](#container-add-version-gs)
+ [Step 4: (For paid products only) Integrate metering or contract pricing](#getting-started-integrate-metering)
+ [Next steps](#getting-started-integrate-metering)
+ [Container product scans for security issues](#container-security)

## Product lifecycle
<a name="container-product-lifecycle"></a>

When you create a product in AWS Marketplace, it starts with a status of **Draft**. After you complete the product details and delivery configuration, you can move the product to **Limited**. Only your account and the accounts on the product's allowlist can access a **Limited** product. When you're ready, you can publish it to the AWS Marketplace catalog to allow buyers to subscribe and purchase your product.

You can view the list of your products on the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central. Depending on what stage it is at, the product has one of the following values in the **Visibility** column.
+ **Draft** – An incomplete product for which you're still adding information. To move the product to Limited, complete **Step 1: Product details** and **Step 2: Delivery configuration**, and then choose **Advance to procurement configuration**. For more information, see [Step 3: Add an initial version of your product](#container-add-version-gs).
+ **Limited** – The product has a detail page that only your account and the accounts on the product's allowlist can access. You can test your product through the detail page. For more information or help, contact the AWS Marketplace Seller Operations team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).
+ **Public** – Buyers can find and subscribe to the product. To publish a **Limited** product, choose **Publish**, and then choose **Submit for review**. AWS Marketplace reviews the product against its policies, which usually takes 3 to 5 business days, and then the product moves to **Public**. For the steps, see [Update product visibility](#container-product-visibility). For information about AWS guidelines, see [Container-based product requirements for AWS Marketplace](container-product-policies.md).
+ **Restricted** – New buyers can't find or subscribe to the product. Existing subscribers keep access, but they can't renew their contracts. To restrict a product, choose **Edit visibility**, and then choose **Restricted**. For the steps, see [Update product visibility](#container-product-visibility).

## Prerequisites
<a name="container-prereq"></a>

Before you get started, you must complete the following prerequisites:

1. Access and use [AWS Partner Central](https://console.aws.amazon.com/partnercentral/home). This is the tool that you use to register as a seller and manage the products that you sell on AWS Marketplace. For more information, see [AWS Partner Central](user-guide-for-sellers.md#aws-marketplace-management-portal).

1. Register as a seller, and submit your tax and banking information. For more information, see [Registration process](registration-process.md).

1. Create at least one container in Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), or AWS Fargate. You deliver your product only from repositories that AWS Marketplace creates for it, so you push your container images and Helm charts there before you add a version. To push them, install the latest version of the AWS CLI and the Docker or Helm 3 client.

1. Plan how you'll create and integrate your container product in AWS Marketplace.

   We recommend that you plan your pricing, entitlement, and metering strategy well in advance of publicly publishing your product.
   + For information about the requirements for container-based products, see [Container-based product requirements for AWS Marketplace](container-product-policies.md).
   + For information about setting the pricing for your product, see [Container products pricing for AWS Marketplace](pricing-container-products.md).
   + For information about custom metering for your paid container-based product, see [Hourly and custom metering with AWS Marketplace Metering Service](container-products-billing-integration.md#entitlement-and-metering-for-paid-products).

## Overview: Create a container product
<a name="create-container-product"></a>

Creating a container product involves the following steps:

1. [Step 1: Create your container product](#create-initial-container-product)

1. [Step 2: Create an initial listing](#container-initial-listing)

1. [Step 3: Add an initial version of your product](#container-add-version-gs)

1. [Step 4: (For paid products only) Integrate metering or contract pricing](#getting-started-integrate-metering)

1. [Update product visibility](#container-product-visibility)

For information on the product lifecycle, see [Product lifecycle](#container-product-lifecycle).

## Step 1: Create your container product
<a name="create-initial-container-product"></a>

To get started, create your container product in AWS Partner Central. AWS Marketplace generates a product ID and a product code for it. The product ID tracks your product throughout its lifecycle.

**To create a container product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose **Create product**.

1. For **Product name**, enter the name that buyers see on your listing and in AWS Marketplace search results.

   The name must be 2 to 72 characters and unique.

1. For **Product type**, choose **Software**.

1. For **Software type**, choose **Container**, and then for **Delivery option**, choose **AWS Marketplace Containers**.

1. (Optional) Under **Tags**, add tags to your product for tag-based authorization. For more information, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

1. Choose **Create product**.

AWS Partner Central creates the product as a draft and opens its page. The **Product summary** section shows the **Product ID**. To see the **Product code**, choose **Show more**.

## Step 2: Create an initial listing
<a name="container-initial-listing"></a>

After you create the product, its page shows **Complete your listing**. Work through its steps in order:

1. **Step 1: Product details** – Provide product information for your product listing. For more information, see [Updating product information for your container product on AWS Marketplace](update-container-product-info.md).

1. **Step 2: Delivery configuration** – Add repositories, upload your container images, and add the initial version of your product. Then move the product to Limited visibility. For more information, see [Step 3: Add an initial version of your product](#container-add-version-gs).

1. **Step 3: Procurement configuration** – Create the public offer for your product. The offer sets the pricing model and prices, the refund policy, the EULA, and the availability by country. For more information about pricing models, see [Container products pricing for AWS Marketplace](pricing-container-products.md).

1. **Step 4: Testing and integrations** and **Step 5: Add-ons** – Share the product with test accounts, set up integrations, and add optional add-ons. Then publish the product. For more information, see [Update product visibility](#container-product-visibility).

## Step 3: Add an initial version of your product
<a name="container-add-version-gs"></a>

Your product might have several versions over its lifetime. Each version has a set of container images that are specific to that version.

You add the initial version before your product moves to Limited visibility.

**To complete product details and delivery configuration**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 1: Product details**.

1. Under **Step 2: Delivery configuration**, complete the following cards in order:
   + **Add repositories** – See [Step 1: Add repositories](container-add-version.md#add-repositories).
   + **Upload container images to repository** – See [Step 2: Upload container images and artifacts to repositories](container-add-version.md#upload-resources).
   + **Configure version and delivery options** – See [Step 3: Add a new version to your container product](container-add-version.md#add-new-version).

   Each card is available after you complete the one before it. The upload card is complete when at least one of your repositories holds an image.

1. Choose **Advance to procurement configuration**.

1. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

   Your product is now in the **Limited** state, and you can test it with allowlisted accounts.

To add an initial version of your product, see [Adding a new version of your container product on AWS Marketplace](container-add-version.md).

## Step 4: (For paid products only) Integrate metering or contract pricing
<a name="getting-started-integrate-metering"></a>

For container-based products with usage pricing, you use the [AWS Marketplace Metering Service](https://docs.aws.amazon.com/marketplacemetering/latest/APIReference/Welcome.html) for both checking entitlement to use your product and metering usage for billing. You must meter for the pricing model that you created when setting your pricing information. For more information, see [Hourly and custom metering with AWS Marketplace Metering Service](container-products-billing-integration.md#entitlement-and-metering-for-paid-products).

### Contract pricing
<a name="container-integrate-LM"></a>

For container-based products with contract pricing, you use the AWS License Manager to associate licenses with your product. 

For more information about integrating with AWS License Manager, see [Contract pricing for container products with AWS License Manager](container-license-manager-integration.md).

## Step 5: Update product visibility
<a name="container-product-visibility-allowlist"></a>

When you create a product in AWS Marketplace, it starts with a status of **Draft**. After you move it to **Limited**, only your account and the accounts on the product's allowlist can see it. You can update the product visibility to allow buyers to subscribe and purchase your product. Alternately you can update the product allow list to add AWS accounts. This topic shows you how to manage which buyers can view your product in AWS Marketplace.

For more information about product visibility and lifecycle, see [Product lifecycle](#container-product-lifecycle).

**Topics**
+ [Update product visibility](#container-product-visibility)
+ [Updating the allowlist of AWS account IDs](#container-update-allowlist)

### Update product visibility
<a name="container-product-visibility"></a>

**Note**  
You can publish a container product only after it has a version with at least one delivery option that isn't restricted. Until then, **Publish** and the **Public** choice in **Edit visibility** are unavailable, and the console shows "This product isn't eligible to publish yet." To add a version, see [Adding a new version of your container product on AWS Marketplace](container-add-version.md).

**To publish a container product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 3: Procurement configuration** and **Step 4: Testing and integrations**.

   **Step 5: Add-ons** is optional.

1. Test your product, and make sure that it meets the requirements in [Container-based product requirements for AWS Marketplace](container-product-policies.md).

1. Choose **Publish**.

1. In the confirmation dialog box, choose **Submit for review**.

AWS Marketplace reviews your listing against its policies before it becomes **Public**. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days.

**To update visibility**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose **Edit visibility**.

1. In the **Update listing visibility** dialog box, for **Change to**, choose **Public** or **Restricted**.

   The choices depend on the product's current visibility.

1. (Optional) If you choose **Restricted**, enter a **Replacement product ID**.

   Existing subscribers keep access until their contract ends, and then move to the replacement product. If you leave it blank, existing subscribers keep access to this product, but they can't renew their contracts.

1. Choose **Update visibility**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

### Updating the allowlist of AWS account IDs
<a name="container-update-allowlist"></a>

You can change the list of AWS account IDs that can view your product in a limited state. Allow-listed accounts display a Limited badge alongside the product version on the product detail page.

**To update the allowlist**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Settings** tab.

1. In the **Allowlisted AWS accounts** section, choose **Edit**.

   If no accounts are allowlisted yet, choose **Add AWS accounts** instead. For a new product, you can also choose **Start** on the **Share with others for testing** card under **Step 4: Testing and integrations**.

1. On the **Update allowlist** page, in **Allowlisted AWS accounts**, enter the 12-digit AWS account IDs, separated by commas.

   The field shows the accounts that are allowlisted now. You can enter up to 5,000 IDs. AWS Marketplace adds your AWS account and the accounts listed on the page automatically, so that it can test and preview your product. If you remove these accounts, the release of your product might take longer.

1. Choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

**Note**  
You can't update the allowlist of a **Restricted** product.

## Next steps
<a name="container-next-steps"></a>

After you create a container product, you can use the information in the following topics to configure and manage it:
+ [Updating product information for your container product on AWS Marketplace](update-container-product-info.md)
+ [Adding a new version of your container product on AWS Marketplace](container-add-version.md)
+ [Managing container product pricing on AWS Marketplace](container-pricing.md)
+ [Updating container product availability by country in AWS Marketplace](container-update-offer-avail-country.md)
+ [Updating your end-user license agreement (EULA) for container products on AWS Marketplace](container-update-eula.md)
+ [Testing and releasing your container product on AWS Marketplace](test-release-product.md)
+ To list your container product without displaying public pricing, see [Leads-only listings](update-pricing-visibility.md).

## Container product scans for security issues
<a name="container-security"></a>

When you create a change request to add a new version to your container product, we scan the container images included in that new version and check for security vulnerabilities. To do this, we perform a layer-by-layer static scan on the image. If we find critical vulnerabilities with remotely exploitable risk vectors, we provide you with a list of found issues. We strongly recommend that you perform your own security analysis using a container image scanner such as Clair, Twistlock, Aqua Security, or Trend Micro to avoid delays in the ingestion and publishing process. 

Your choice of base image for building your container images can have a significant influence on the security profile of the final image. If you choose a base image that already has known critical vulnerabilities, they will be flagged because of the base layer, even if your application software layers are clean. We recommend that you verify that you're starting with a base container that is free of vulnerabilities before you build your images and submit them to AWS Marketplace. 

Scan results appear on your product's **Delivery** tab, in the **Scan result** column of the **Versions** table. The result is **Passed**, the number of issues found, or **Assessment expired**. **Missing permission** means that your IAM identity can't view scan results. The **Due date** column shows when you must resolve the issues.

To see the issues for a version, choose its version title. The details page shows the **Security issues found** section, with the artifact ID, description, recommended action, and due date of each issue. To get help, choose **Contact support**. To save the list, choose **Download as CSV**.

To resolve the issues, add a new version with fixed images, and then restrict the version that has the issues. If you don't resolve the issues by the due date, AWS Marketplace temporarily restricts the product. Active subscribers keep access, but new buyers can't find or subscribe to the product. For more information, see [Adding a new version of your container product on AWS Marketplace](container-add-version.md).