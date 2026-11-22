

# Getting started with products integrated with AWS services

RTB Fabric module products are published on AWS Marketplace and used through AWS RTB Fabric. This topic describes the product type, the prerequisites, and how buyers discover and subscribe to these products on AWS Marketplace.

RTB Fabric module products let advertising technology vendors sell bid-traffic modules. Buyers can subscribe to these products on AWS Marketplace or directly from the RTB Fabric console, and then deploy your module through the AWS RTB Fabric service.

**Note**  
At launch, RTB Fabric module products are available to a limited set of sellers on an allow-list basis. For more information or to request access, contact AWS Marketplace Seller Operations on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).

## Prerequisites
<a name="additional-product-types-prerequisites"></a>

Before you create an RTB Fabric module product, make sure that you meet the following prerequisites:
+ You are a registered AWS Marketplace seller with a complete public profile. For paid products, you also provide your tax and banking information and a disbursement method.
+ Your seller account is enabled for RTB Fabric module products. Publishing these products is available on an allow-list basis only, so make sure that your seller account is on the allow list. For more information, contact AWS Marketplace Seller Operations on the AWS Partner Central and Marketplace Support page.
+ You have IAM permissions to call the AWS Marketplace Catalog API.
+ You have your module ready in the AWS RTB Fabric service. After you publish the product on AWS Marketplace, which creates the product ID, you associate that product ID with your module in the AWS RTB Fabric console.

## How buyers find and buy your product
<a name="additional-product-types-finding"></a>

You find RTB Fabric module products on the AWS Marketplace website, on the AWS Marketplace console, the AWS Marketplace Model Context Protocol (MCP) server, or the AWS RTB Fabric console. On the AWS Marketplace search, to narrow your search to these products, use the **Delivery method** filter and select **RTB Fabric Module**. The product detail page shows the AWS service that the product is delivered through under **Delivery method**, and the **Usage information** section describes what to do in that service after you subscribe.

While you test your product, you keep it in the `Limited` state and add the AWS accounts that are allowed to view it to an allowlist. Products in the `Limited` state don't appear in AWS Marketplace search for public customers not allowlisted to view the listing.

You can also reach these products from the AWS RTB Fabric console, which links to the AWS Marketplace listing.

## Next steps
<a name="additional-product-types-next-steps"></a>

After you complete the required prerequisites, you can create and configure your product.