

# Product lifecycle for products integrated with AWS services

RTB Fabric module products use the generic `Product@1.0` entity and move through the same product states as other AWS Marketplace Catalog API products. You manage these states with the AWS Marketplace Catalog API or in AWS Partner Central.
+ **Draft** – An incomplete product for which you're still adding information. The first successful change request creates an unpublished product with the information that you submitted. From this status, you can continue adding information to the product or change already submitted details through change requests.
+ **Limited** – A product is complete after it is submitted to the system and passes all validation in the system. Then the product is released to a `Limited` status. At this point, the product has a detail page that is only accessible to your account and whoever you have allowlisted. In this state, you also associate your asset with the product. You can test your product through the detail page.
+ **Public** – When you're ready to publish the product so that buyers can view and subscribe to the product, you use the Update visibility change request. This request initiates a workflow for the AWS Marketplace Seller Operations team to review and audit your product against AWS policies. After the product is approved and the change request is processed, the product is moved from a status of `Limited` to `Public`.
+ **Restricted** – If you want to stop new users from subscribing to your product, you can restrict the product by using the Update visibility change request. A `Restricted` status means that existing users can continue to use the product. However, the product will no longer be visible to the public or be available to new users.

For how you create a product and move it to the `Limited` and `Public` states, see [Creating your product](additional-product-types-creating.md).