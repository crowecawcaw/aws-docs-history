# SaaS product lifecycle in AWS Marketplace

When you create a software as a service (SaaS) product in AWS Marketplace, it's initially
published with limited visibility so that only your account can access it. When you're
ready, you can publish it to the AWS Marketplace catalog to allow buyers to subscribe and purchase
your product. The following topic provides information about the SaaS product lifecycle. For
more information about creating a SaaS product, see [Creating a SaaS product in AWS Marketplace](saas-create-product.md "saas-create-product.md"),

On the SaaS product page, you can view the list of your products. Depending on its stage
in the product lifecycle, the product will have one of the following statuses:

- **Staging** – An incomplete product for which
  you're still adding information. At the first **Save and
  exit** from the self-service experience, the successful change request
  creates an unpublished product with information from the completed steps that you
  submitted. From this status, you can continue adding information to the product or
  change already submitted details through change requests.
- **Limited** – A product is complete after it
  is submitted to the system and passes all validation in the system. Then the product
  is released to a **Limited** status. At this point, the
  product has a detail page that is only accessible to your account and whoever you
  have allowlisted. You can test your product through the detail page. For more
  information or help, contact the [AWS Marketplace Seller
  Operations](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.
- **Public** – When you're ready to publish the
  product so that buyers can view and subscribe to the product, you use the **Update visibility** change request. This request initiates
  a workflow for the AWS Marketplace Seller Operations team to review and audit your product
  against AWS policies. After the product is approved and the change request is
  processed, the product is moved from a status of **Limited** to **Public**. For information
  about AWS guidelines, see [SaaS product
  guidelines](saas-guidelines.md "saas-guidelines.md").
- **Restricted** – If you want to stop new users
  from subscribing to your product, you can restrict the product by using the
  **Update visibility** change request. A **Restricted** status means that existing users can continue
  to use the product. However, the product will no longer be visible to the public or
  be available to new users.
  You can update your product at the **Staging**, **Limited**, and **Public** statuses.
  For more information, see [Updating product information](saas-product-settings.md#update-product-information "saas-product-settings.md#update-product-information").
