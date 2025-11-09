# Contract pricing

Using the contract pricing model, you can offer upfront pricing to customers that enables
them to buy a license for 1 month, 12 months, 24 months, or 36 months.

Contract pricing is available for the following products:

- Single AMI-based products and AMI with AWS CloudFormation template-based products. For more
  information, see [Contract pricing for AMI products on AWS Marketplace](ami-contracts.md "ami-contracts.md")
- Container-based products. For more information, see [Contract pricing for container products](container-license-manager-integration.md#container-contracts "container-license-manager-integration.md#container-contracts").
- Software as a service (SaaS)-based products. For more information, see [Pricing for SaaS contracts](saas-contracts.md "saas-contracts.md").

###### Note

Contract pricing for AMI and container-based products is only for new products.

If you have an existing AMI or container-based product and want to use contract
pricing, create a new listing and then apply the contract pricing model by using the
Product Load Form (PLF) to add different dimensions, integrate the AMI or container-based
product with AWS License Manager, and then publish the AMI or container-based product.

When a customer purchases a product with contract pricing, a license is created by
AWS Marketplace in the customer AWS account that your software can check using the License Manager API.
Customers will need an IAM role to launch an instance of the AMI or container-based
product.
