# Finding container products in AWS Marketplace

Container products are products in AWS Marketplace that can be launched on container images.
Container products include any product in AWS Marketplace in which the seller has provided a fulfillment
option with a **Container image**, **Helm chart**, or
**Add-on for Amazon EKS** delivery method. For more information about container
product delivery methods, see [Container product delivery methods](buyer-container-product-delivery-methods.md "buyer-container-product-delivery-methods.md").

Many launch environments, also known as supported services, are available for fulfillment
options in container products. Launch environments include services such as Amazon Elastic Container Service (Amazon ECS),
Amazon Elastic Kubernetes Service (Amazon EKS), and even your own self-managed infrastructure. For a complete list of
available container product launch environments, see [Supported services for container
products](buyer-what-is-aws-marketplace-for-containers.md#buyer-container-product-launch-environments "buyer-what-is-aws-marketplace-for-containers.md#buyer-container-product-launch-environments").

## Find container products using the AWS Marketplace

website

The product details page in AWS Marketplace includes details about the product, such as the following information:

- **Product Overview** – The overview includes a product
  description and the following information:
  - The product version that you're viewing.
  - A link to the seller's profile.
  - The product categories that this product belongs to.
  - The supported operating systems to run this software.
  - The delivery methods that are available for launching the software.
  - The supported services that this product can be launched on.

- **Pricing Information** – Products have free tiers, Bring
  Your Own License (BYOL), pay-up-front with contract pricing, or pay-as-you-go with
  either a fixed monthly or annual price, or an hourly price. For more information about
  pricing models, see [Container product pricing](../userguide/pricing-container-products.md "../userguide/pricing-container-products.md").
- **Usage Information** – Included here are seller-provided
  fulfillment options with instructions to launch and run the software. Each product must
  have at least one fulfillment option and can have up to five. Each fulfillment option
  includes a delivery method and instructions to follow to launch and run the
  software.
- **Support Information** – This section includes details
  about how to get support for the product and its refund policy.
- **Customer Reviews** – Find reviews for the product from
  other customers or write your own.

###### To find container products using the AWS Marketplace website

1. Navigate to the [AWS Marketplace search
   page](https://aws.amazon.com/marketplace/search/? "https://aws.amazon.com/marketplace/search/?").
2. Filter **Delivery method** by **Container image** or
   **Helm chart**.
3. (Optional) Filter **Supported services** to narrow the search results
   by the services that the product can be launched with.

After you find a product that you're interested in, choose the title to navigate to the
product details page.

## Find container products using the Amazon ECS

console

You can also find container products in the Amazon ECS console. The navigation pane has links
to discover new products from AWS Marketplace and to see existing subscriptions.
