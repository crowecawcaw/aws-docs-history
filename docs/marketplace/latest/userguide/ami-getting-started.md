# Understanding AMI-based products in AWS Marketplace

As an AWS Marketplace seller, you can deliver your products to buyers with [Amazon Machine Images (AMIs)](../../../glossary/latest/reference/glos-chap.md#AmazonMachineImage "../../../glossary/latest/reference/glos-chap.md#AmazonMachineImage"). An AMI
provides the information required to launch an Amazon Elastic Compute Cloud (Amazon EC2) instance.
The following section explains the key concepts for working with AMI-based products.

###### Note

You can only use one AMI in an AMI product, but you can add versions of that AMI to the product.

###### Topics

- [Product lifecycle](#ami-product-lifecycle "#ami-product-lifecycle")
- [AMI product codes](#ami-product-codes "#ami-product-codes")
- [Change requests](#ami-change-requests "#ami-change-requests")
- [Product Load Forms](#ami-product-load-forms "#ami-product-load-forms")
- [Annual agreement amendments](#annual-agreement-amendments "#annual-agreement-amendments")
- [FPGA Products](#ami-fpga-products "#ami-fpga-products")

## Product lifecycle

AMI-based products include one or more versions of the software, plus metadata
about the product as a whole. When you create the product, you configure its properties
in AWS Marketplace including the product name, description, and pricing. You also determine the
appropriate categories for your product and add keywords so your product appears in
relevant searches.

You also create the first version of the software. This can be just the AMI, or you can include
AWS CloudFormation templates or software packages that buyers can use to create their own AMIs. For
more information, see [AMI-based product delivery methods](ami-products.md#ami-product-delivery-methods "ami-products.md#ami-product-delivery-methods").

For paid products, buyers are billed for the number of installed instances. To meter
on a different dimension that your software tracks, such as the number of product users,
integrate your product with the AWS Marketplace Metering Service. For more information, see [Configuring custom metering for AMI products with
AWS Marketplace Metering Service](custom-metering-with-mp-metering-service.md "custom-metering-with-mp-metering-service.md").

When you create your product and the first version of your software, it's initially
published in a limited scope so that only your account can access it. When you're ready,
you can publish it to the AWS Marketplace catalog to allow buyers to subscribe and purchase your
product.

You use the [Server product](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page to view the list of your products. Products will have
one of the following statuses:

- **Staging** – An incomplete product for which you are
  still adding information. At the first **Save and exit** from
  the create self-service experience, the successful change request creates an
  unpublished product with information from the full steps you submitted. From
  this state, you can continue adding information to the product or change already
  submitted details through change requests.
- **Limited** – A product is complete after it is
  submitted to the system and passes all validation in the system. Then the
  product is released to a **Limited** state. At this point, the
  product has a detail page that is only accessible to your account and whoever
  you have allowlisted. You can test your product through the detail page. If
  necessary, for more information and help, contact the [**AWS Marketplace Seller Operations team**](https://aws.amazon.com/marketplace/management/contact-us/?# "https://aws.amazon.com/marketplace/management/contact-us/?#").
- **Public** – When you're ready to publish the product
  so that buyers can view and subscribe to the product, you use the
  **Update visibility** change request. This initiates a
  workflow for the AWS Marketplace Seller Operations team to review and audit your product against our [policies](product-and-ami-policies.md "product-and-ami-policies.md"). Once the product is approved and the change request is
  processed, the product is moved from a status of **Limited** to
  **Public**.
- **Restricted** – If you want to stop new users from
  subscribing to your product, you can restrict the product by using the
  **Update visibility** change request. A
  **Restricted** status means that existing users can
  continue to use the product. However, the product will no longer be visible to
  the public or be available to new users.

The lifecycle of an AMI-based product for AWS Marketplace does not end after you publish the
first version. You should keep your product up to date with new versions of your
software, and with security patches for the base operating system.

As an example of a complete AMI-based product lifecycle, imagine a seller wants to
sell their AMI-based product on AWS Marketplace. Following is how the seller creates and maintains
the product over time:

1. Create a product – The seller creates
   the product, and publishes version 1.0.0 to AWS Marketplace. Buyers can create instances
   of version 1.0.0 and use it.
2. Add a new version – Later, the seller
   adds a new feature to the product, and adds a new version, 1.1.0, that includes
   the feature. Buyers can still use the original version, 1.0.0, or they can
   choose the new version, 1.1.0.

###### Note

Unlike new products, new versions are published to full public
availability. You can only test them in AWS Marketplace without customers seeing them
if the product as a whole is in limited release. 3. Update product information – With
version 1.1.0 available, the seller lets buyers know about the new feature by
updating the product information with new highlight text describing the
feature. 4. Add a minor version – When the seller
fixes a bug in version 1.1.0, they release it by adding a new version 1.1.1.
Buyers now have the choice of using version 1.0.0, 1.1.0, or 1.1.1. 5. Restrict a version – The seller decides
that the bug is serious enough that they don’t want buyers to be able to use
version 1.1.0, so they restrict that version. No new customers can then buy
1.1.0 (they can only choose 1.0.0 or 1.1.1), although existing buyers still have
access to it. 6. Update version information – To help
those existing buyers, the seller updates the version information for 1.1.0 with
a suggestion to upgrade to version 1.1.1. 7. Monitor usage – As buyers purchase and
use the product, the seller monitors sales, usage, and other metrics using the
AWS Marketplace [Seller reports, data feeds, and dashboards in AWS Marketplace](reports-and-data-feed.md "reports-and-data-feed.md"). 8. Remove the product – When the product is
no longer needed, the seller removes it from AWS Marketplace.

In this example, the seller created three different versions of the AMI in the
product, but only two were available to new buyers (prior to removing the
product).

To make modifications to versions or the product information, you create [change requests](single-ami-create-change-request.md "single-ami-create-change-request.md") in the
AWS Marketplace Management Portal.

For detailed instructions on the steps to create and manage your AMI-based product,
see [Creating AMI-based products](ami-single-ami-products.md "ami-single-ami-products.md").

## AMI product codes

A unique product code is assigned to your product when you create it in AWS Marketplace. That
product code is associated with the AMI for your product and is used to track usage of
your product. Product codes are propagated automatically as buyers work with the
software. For example, a customer subscribes and launches an AMI, configures it, and
produces a new AMI. The new AMI still contains the original product code, so correct
usage tracking and permissions remain in place.

###### Note

The product _code_ is different than the product
_ID_ for your product. Each product in AWS Marketplace is
assigned a unique product ID. The product ID is used to identify your product in the
AWS Marketplace catalog, in customer billing, and in seller reports. The product code is
attached to instances created from your AMI as instance metadata. When an AMI with
that product code is used to create an instance, the customer will get a bill that
shows the associated product ID. After you create your product, find the product
code and the product ID in the AWS Marketplace Management Portal page for your product.

As a seller, your software can get the product code for the running Amazon Elastic Compute Cloud (Amazon EC2)
instance at runtime from the instance metadata. You can use the product code for extra
security, such as validating the product code at product start. You can't make API calls
to an AMI's product code until the product has been published into a limited state for
testing. For more information about verifying the product code, see [Verifying your software is running on your AWS Marketplace
AMI](best-practices-for-building-your-amis.md#verifying-ami-runtime "best-practices-for-building-your-amis.md#verifying-ami-runtime") .

## Change requests

To make changes to a product or version in AWS Marketplace, you submit a **change request** through the AWS Marketplace Management Portal. Change requests are added to a
queue and can take from minutes to days to resolve, depending on the type of request.
You can see the status of requests in the AWS Marketplace Management Portal.

###### Note

In addition to the AWS Marketplace Management Portal, you can also create change requests by using the
[AWS Marketplace
Catalog API](../../../marketplace-catalog/latest/api-reference/seller-products.md "../../../marketplace-catalog/latest/api-reference/seller-products.md").

The types of changes you can request for AMI-based products include:

- Update product information displayed to buyers.
- Update version information displayed to buyers.
- Add a new version of your product.
- Restrict a version so that new buyers can no longer access that
  version.
- Update the AWS Regions that a product is available in.
- Update the pricing and instance types for a product.
- Remove a product from AWS Marketplace.

###### Note

Some change requests require you to use product load forms to create the request.
For more information, see [Product Load Forms](#ami-product-load-forms "#ami-product-load-forms").

### Update change request

Change requests that start with an update will load the current details. You then make
updates, which overwrite the existing details.

### Add or restrict change request

Add and restrict request pairs are specifically for steps and updates that are
provisioned after each request succeeds. A request succeeds after you choose
**Save and exit** and **Submit** actions in the
self-service experience.

For example, if the AMI asset is provisioned to the instances and Regions once added,
then they can only be restricted rather than completely removed. This means existing
subscribers and users can continue to use the product until their subscription or
contract runs out. However, no new subscribers can be added to a product that is in a
**Restricted** status.

## Product Load Forms

Typically, you use [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management") to create or edit your product. However, a few operations require you to use
a _Product Load Form_ (PLF).

A PLF is a spreadsheet that contains all the information about a product. To obtain a PLF, you can:

- Download the PLF for an existing product from the product's details
  page in the AWS Marketplace Management Portal.
- Select a menu item for an action
  that requires a PLF. For example, if you create a new monthly billed
  server product, the system prompts you to download the appropriate PLF.

If the action is an edit to an existing product, the PLF is pre-populated with
the information for that product, so you only need to change the details that
you want to update.

- If you need a new, blank PLF, navigate to the AWS Marketplace Management Portal [File
  upload](https://aws.amazon.com/marketplace/management/product-load "https://aws.amazon.com/marketplace/management/product-load") page. The page contains links to PLFs for the product type you want to create.

After you have completed your PLF, upload it to the AWS Marketplace Management Portal [File
upload](https://aws.amazon.com/marketplace/management/product-load "https://aws.amazon.com/marketplace/management/product-load") page. The PLF itself has more detailed instructions in the
**Instructions** tab.

## Annual agreement amendments

Hourly annual (annual) plan amendments allow you and your buyers to make the following
changes to existing plans:

- Switch between Amazon EC2 instance type families
- Switch between Amazon EC2 instance type sizes
- Add a new instance type
- Increase the quantity of an existing instance type in the agreement

Buyers can make a change as long as the prorated cost of the change is greater than
zero (they can't lower the value of the subscription). The prorated cost of the newly
added Amazon EC2 instances is based on the annual cost of the instance type adjusted for
the remaining term of the agreement. When switching instance types, the prorated cost of
the removed Amazon EC2 instance type is deducted from the prorated cost of the newly added
Amazon EC2 instance type.

No additional action is required to enable amendments on AMI annual products.
Amendments are supported on all agreements made from public offers and agreements from
private offers that don't use installment plans.

You can see the amendments made by your buyers on the following dashboards:

- [Agreements and renewals dasboard](agreements-renewals-dashboard.md "agreements-renewals-dashboard.md") – The list of amended
  agreements.
- [Billed
  revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md") – Charges to the customer.
- [Collections and disbursement dashboard](collections-disbursement-dashboard.md "collections-disbursement-dashboard.md") – The
  disbursement.

## FPGA Products

FPGA (Field Programmable Gate Array) products are specialized AMI products that support
F2 instance types with Amazon FPGA Image (AFI) configurations. Unlike standard AMIs,
FPGA products include AFI IDs that are dynamically loaded by the AMI for hardware acceleration
on supported instance types.

**Key characteristics:**

- FPGA products support F2 instance types exclusively for FPGA acceleration.
- Each product version can include one or more AFI IDs, with a maximum of 15 AFI IDs per version.
- AFIs are loaded on-the-fly rather than launched like AMIs, providing dynamic hardware
  acceleration capabilities.
- When you add new regions to your FPGA product, automated regional AFI cloning is performed by AWS Marketplace to ensure
  your product is available across supported AWS Regions.
- While FPGA products can be offered on other instance types, the AFIs will only be loaded and provide hardware acceleration on
  F2 instance types. On other instance types, the AMI functions without the FPGA
  acceleration capabilities.

FPGA products are ideal for compute-intensive workloads requiring specialized hardware
acceleration such as genomics research, financial analytics, real-time video processing,
big data analytics, and machine learning inference. The dynamic loading of AFIs enables
buyers to leverage FPGA acceleration without managing the underlying FPGA infrastructure.
