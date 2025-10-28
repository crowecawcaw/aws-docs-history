# Getting started with container

products

As an AWS Marketplace seller, you can create container-based software products. Container products
consist of delivery options that are a set of container images and deployment templates that go
together.The following topic shows you how to get started with container products.

- [Product lifecycle](#container-product-lifecycle "#container-product-lifecycle")
- [Prerequisites](#container-prereq "#container-prereq")
- [Step 1: Create the product ID and product
  code for your container product](#create-initial-container-product "#create-initial-container-product")
- [Step 2: Create an initial listing](#container-initial-listing "#container-initial-listing")
- [Step 3: Add an initial version of your
  product](#container-add-version-gs "#container-add-version-gs")
- [Step 4: (For paid products only)
  Integrate metering or contract pricing](#getting-started-integrate-metering "#getting-started-integrate-metering")
- [Next steps](#getting-started-integrate-metering "#getting-started-integrate-metering")
- [Container product scans for security issues](#container-security "#container-security")

## Product lifecycle

When you create a product in AWS Marketplace, it's initially published with limited visibility so
that accounts on the allow list can see it, including the account that created the product.
When you're ready, you can publish it to the AWS Marketplace catalog to allow buyers to subscribe and
purchase your product.

On the [Server
product](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, you can view the list of your products. Depending on what stage it is
at, the product will have one of the following statuses.

- **Staging** – An incomplete product for which
  you're still adding information. At the first **Save and
  exit** from the self-service experience, the successful change request creates
  an unpublished product with information from the completed steps that you submitted. From
  this status, you can continue adding information to the product or change already
  submitted details through change requests.
- **Limited** – A product is complete after it is
  submitted to the system and passes all validation in the system. Then the product is
  released to a **Limited** status. At this point, the product
  has a detail page that's only accessible to your account and whoever you have allowlisted.
  You can test your product through the detail page. For more information or help, contact
  the [AWS Marketplace
  Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.
- **Public** – When you're ready to publish the
  product so that buyers can view and subscribe to the product, you use the **Update visibility** change request. This request initiates a
  workflow for the AWS Marketplace Seller Operations team to review and audit your product against
  AWS policies. After the product is approved and the change request is processed, the
  product is moved from a status of **Limited** to **Public**. For information about AWS guidelines, see [Container-based product requirements for AWS Marketplace](container-product-policies.md "container-product-policies.md").
- **Restricted** – If you want to stop new users
  from subscribing to your product, you can restrict the product by using the **Update visibility** change request. A **Restricted** status means that existing allowlisted users can continue to use
  the product. However, the product will no longer be visible to the public or be available
  to new users.

## Prerequisites

Before you get started, you must complete the following prerequisites:

1. Access and use the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/"). This is the tool that you use to register as a seller and manage the
   products that you sell on AWS Marketplace. For more information, see [AWS Marketplace Management Portal](user-guide-for-sellers.md#management-portal "user-guide-for-sellers.md#management-portal").
2. Register as a seller, and submit your tax and banking information. For more
   information, see [Registration process](registration-process.md "registration-process.md").
3. Create at least one container in Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), or
   AWS Fargate. Make sure that you have links for the associated images.
4. Plan how you'll create and integrate your container product in AWS Marketplace.

We recommend that you plan your pricing, entitlement, and metering strategy well in
advance of publicly publishing your product.

    * For information about the requirements for container-based products, see [Container-based product requirements for AWS Marketplace](container-product-policies.md "container-product-policies.md").
    * For information about setting the pricing for your product, see [Container products pricing for AWS Marketplace](pricing-container-products.md "pricing-container-products.md").
    * For information about custom metering for your paid container-based product, see
     [Hourly and custom metering with
     AWS Marketplace Metering Service](container-products-billing-integration.md#entitlement-and-metering-for-paid-products "container-products-billing-integration.md#entitlement-and-metering-for-paid-products").

## Overview: Create a container product

Creating a container product involves the following steps:

1. [Step 1: Create the product ID and product
   code for your container product](#create-initial-container-product "#create-initial-container-product")
2. [Step 2: Create an initial listing](#container-initial-listing "#container-initial-listing")
3. [Step 3: Add an initial version of your
   product](#container-add-version-gs "#container-add-version-gs")
4. [Step 4: (For paid products only)
   Integrate metering or contract pricing](#getting-started-integrate-metering "#getting-started-integrate-metering")
5. [Update product visibility](#container-product-visibility "#container-product-visibility")

For information on the product lifecycle, see [Product lifecycle](#container-product-lifecycle "#container-product-lifecycle").

## Step 1: Create the product ID and product

code for your container product

To get started with a container product, you must create a product ID and product code
record in AWS Marketplace. The product ID is used to track your product throughout its lifecycle.

Use the following procedure to create a new container product in the AWS Marketplace Management Portal, and
generate the product ID.

###### Note

This process also creates a public key for your container that pairs with your
product.

###### To create the container product ID

1. Open a web browser and sign into the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/").
2. From the menu bar, select **Product**, and choose
   **Server**.
3. Choose **Create server product** and then choose
   **Container**.
4. Generate a container product ID and code.

###### Note

(Optional) You can tag your product for tag-based authorization. For more
information, see [Tagging your AWS
resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md"). 5. Choose **Continue** to continue creating your product.

## Step 2: Create an initial listing

After generating the product ID, product code, and public key, you'll use a wizard to
create an initial listing.

1. Provide product information for your product listing.
2. Determine the pricing model for your product.

###### Note

For more information, see [Container products
pricing](pricing-container-products.md "pricing-container-products.md").

###### Note

For paid products, your product will start with $0.01 pricing to allow you and
AWS Marketplace Seller Operations team to test the product without incurring a high cost.
You'll provide the actual price when you go public. 3. Provide additional offer information, including a refund policy, EULA, and offer
availability. 4. Add an initial repository for your container product. 5. Choose **Submit** on the last step to move the product to Limited
visibility.

###### Note

Your container product is initially created with a placeholder version. You'll add
the final version when the product has a Limited visibility.

## Step 3: Add an initial version of your

product

Your product might have several versions over its lifetime. Each version has a set of
container images that are specific to that version. To add an initial version of your product,
see [Adding a new version of your container product on AWS Marketplace](container-add-version.md "container-add-version.md").

## Step 4: (For paid products only)

Integrate metering or contract pricing

For container-based products with usage pricing, you use the [AWS Marketplace Metering Service](../../../marketplacemetering/latest/APIReference/Welcome.md "../../../marketplacemetering/latest/APIReference/Welcome.md") for both checking
entitlement to use your product and metering usage for billing. You must meter for the pricing
model that you created when setting your pricing information. For more information, see [Hourly and custom metering with
AWS Marketplace Metering Service](container-products-billing-integration.md#entitlement-and-metering-for-paid-products "container-products-billing-integration.md#entitlement-and-metering-for-paid-products").

### Contract pricing

For container-based products with contract pricing, you use the
AWS License Manager to associate licenses with your product.

For more information about integrating with AWS License Manager, see [Contract pricing for container products
with AWS License Manager](container-license-manager-integration.md "container-license-manager-integration.md").

## Step 5: Update product visibility

When you create a product in AWS Marketplace, it's initially published with limited visibility
so that accounts on the allow list can see it, including the account that created the product.
You can update the product visibility to allow buyers to subscribe and purchase your product.
Alternately you can update the product allow list to add AWS accounts. This topic shows you
how to manage which buyers can view your product in AWS Marketplace.

For more information about product visibility and lifecycle, see [Product lifecycle](#container-product-lifecycle "#container-product-lifecycle").

###### Topics

- [Update product visibility](#container-product-visibility "#container-product-visibility")
- [Updating the allowlist of AWS account
  IDs](#container-update-allowlist "#container-update-allowlist")

### Update product visibility

###### To update visibility

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign in to your
   seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, on the **Current server
   product** tab, select the container-based product that you want to
   modify.
3. From the **Request changes** dropdown, choose **Update
   visibility**.

###### Note

You can request that the product be moved from a **Limited**
status to a **Public** status by using this change request. However,
the change request must go through an AWS Marketplace Seller Operations team approval process to be moved to
**Public**. 4. Choose **Submit** to submit your request for review. 5. Verify that the **Requests** tab shows the **Request
status** as **Under review**. When the request completes,
the status becomes **Succeeded**.

### Updating the allowlist of AWS account

IDs

You can change the list of AWS account IDs that can view your product in a limited
state. Allow-listed accounts display a Limited badge alongside the product version on the
product detail page.

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/") and sign in to your
   seller account.
2. From the [**Server Products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, select the container product
   that you want to modify.
3. From the **Request changes** dropdown list, select **Update
   allowlist**. The current list of accounts that are allowlisted is
   shown.
4. In the **Allowlisted AWS accounts** field, enter the
   AWS account IDs and separate them using a comma.
5. Choose **Submit** to submit your request for review.
6. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request completes,
   the status will update to **Succeeded** or
   **Failed**.

## Next steps

After you create a container product, you can use the information in the following topics
to configure and manage it:

- [Updating product information for
  your container product on AWS Marketplace](update-container-product-info.md "update-container-product-info.md")
- [Adding a new version of your container product on AWS Marketplace](container-add-version.md "container-add-version.md")
- [Managing container product pricing on AWS Marketplace](container-pricing.md "container-pricing.md")
- [Updating container product availability by
  country in AWS Marketplace](container-update-offer-avail-country.md "container-update-offer-avail-country.md")
- [Updating your end-user license agreement (EULA) for container products on AWS Marketplace](container-update-eula.md "container-update-eula.md")
- [Testing and releasing your container product on AWS Marketplace](test-release-product.md "test-release-product.md")

## Container product scans for security issues

When you create a change request to add a new version to your container product, we scan
the container images included in that new version and check for security vulnerabilities. To
do this, we perform a layer-by-layer static scan on the image. If we find critical
vulnerabilities with remotely exploitable risk vectors, we provide you with a list of found
issues. We strongly recommend that you perform your own security analysis using a container
image scanner such as Clair, Twistlock, Aqua
Security, or Trend Micro to avoid delays in the ingestion and
publishing process.

Your choice of base image for building your container images can have a significant
influence on the security profile of the final image. If you choose a base image that already
has known critical vulnerabilities, they will be flagged because of the base layer, even if
your application software layers are clean. We recommend that you verify that you're starting
with a base container that is free of vulnerabilities before you build your images and submit
them to AWS Marketplace.
