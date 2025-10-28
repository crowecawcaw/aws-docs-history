# Launching container software from

AWS Marketplace

After you have an active subscription to a container product in AWS Marketplace, you launch the
software. To do so, follow the instructions included in one of the fulfillment options provided
by the seller. In AWS Marketplace, a _fulfillment option_ is an optional
seller-provided procedure for launching their product in your environment. For container
products, the seller can provide up to four fulfillment options, which can use different
delivery methods and represent different configurations for the software. For example, a seller
might create one fulfillment option that's used for testing the product, and another for
deploying the product at scale within an enterprise.

You can see the fulfillment options that are available in the **Usage Information** section of a product's detail page. Alongside the fulfillment options provided by the seller,
AWS Marketplace includes instructions for pulling the Docker images directly from Amazon Elastic Container Registry (Amazon ECR).

Because the sellers provide the fulfillment options, their names and content will differ for each product in AWS Marketplace. Although the methods are unique to each product and seller,
each fulfillment option must have a delivery method. You can think of a delivery method as a fulfillment option type. You can use the following delivery methods for container products:

- Container image
- Helm chart
- Add on for Amazon EKS

###### To launch container software from AWS Marketplace

1. Sign in to [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").
2. Browse AWS Marketplace, and find the product that contains the software that you want to launch.
   You must have a subscription to the product to launch its software. For information about
   finding and subscribing to container products in AWS Marketplace, see [Finding container products in AWS Marketplace](buyer-finding-and-subscribing-to-container-products.md "buyer-finding-and-subscribing-to-container-products.md").
3. Choose **Continue to Subscribe** on the product details page.
4. Choose **Continue to Configuration**. If you don't see the button,
   you might have to accept terms first, or you might not have a subscription to the
   product.
5. Choose the service to deploy on and the delivery methods provided by the seller.
6. Follow the instructions provided by the seller to launch the product. The instructions
   are different for each fulfillment option. For more information, see [Launching with a Container image fulfillment option](buyer-launch-container-image.md "buyer-launch-container-image.md") or
   [Launching with a Helm fulfillment
   option](buyer-launch-container-helm.md "buyer-launch-container-helm.md").
7. _Optional -_ Choose **Usage instructions** for
   documentation from the seller about how to configure and use the product after
   launching.

###### Note

For a walkthrough on how to subscribe to and deploy a container-based product, you can
also refer to the following videos:

- [Deploying AWS Marketplace Containers
  on Amazon ECS Clusters](https://www.youtube.com/watch?v=XaiUAiQQJtk "https://www.youtube.com/watch?v=XaiUAiQQJtk") (3:34)
- [Deploying AWS Marketplace
  Container-based Products using Amazon ECS Anywhere](https://www.youtube.com/watch?v=9SFjG2UaxXs "https://www.youtube.com/watch?v=9SFjG2UaxXs") (5:07)
