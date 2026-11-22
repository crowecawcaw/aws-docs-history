

# Contract pricing

Using the contract pricing model, you can offer upfront pricing to customers that enables them to buy a license for 1 month, 12 months, 24 months, or 36 months.

Contract pricing is available for the following products:
+ Single AMI-based products and AMI with AWS CloudFormation template-based products. For more information, see [Contract pricing for AMI products on AWS Marketplace](ami-contracts.md)
+ Container-based products. For more information, see [Contract pricing for container products](container-license-manager-integration.md#container-contracts).
+ Software as a service (SaaS)-based products. For more information, see [Pricing for SaaS contracts](saas-contracts.md).
+ RTB Fabric module products. For more information, see [Pricing](additional-product-types-pricing.md).
+ Data as a Service (DaaS) products. For more information, see [DaaS product pricing in AWS Marketplace](daas-pricing-models.md).

**Note**  
Contract pricing for AMI and container-based products is only for new products.   
If you have an existing AMI or container-based product and want to use contract pricing, create a new product. When you create its public offer, choose **Contract pricing** on the **Set pricing model and dimensions** step, and add your contract dimensions. Integrate the product with AWS License Manager before you publish it. For more information, see [Contract pricing for AMI products on AWS Marketplace](ami-contracts.md) or [Contract pricing for container products](container-license-manager-integration.md#container-contracts).  
When a customer purchases a product with contract pricing, a license is created by AWS Marketplace in the customer AWS account that your software can check using the License Manager API. Customers will need an IAM role to launch an instance of the AMI or container-based product.