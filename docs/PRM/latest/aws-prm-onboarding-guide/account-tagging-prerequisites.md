

# Method-Specific Requirements

In addition to the general prerequisites of ARM, ensure you meet the following requirements for Account Tagging for SaaS products:
+ **SaaS product listing on AWS Marketplace.** Your product must be listed as a SaaS product type on AWS Marketplace. Account Tagging is not available for Amazon Machine Image (AMI), Machine Learning (ML), or Professional Services product types.
+ **Partner-owned AWS accounts.** You must own the AWS accounts that host your product. Account Tagging for SaaS products applies only to accounts under your control.
+ **AWS Organizations membership.** The accounts hosting your product must be member accounts within an AWS Organization that you manage. Account tags are applied from the management account (or a delegated administrator account) using AWS Organizations.
+ **Each account dedicated to a single product.** Each AWS account you tag must be dedicated to delivering a single product. Account Tagging for SaaS products is not available when multiple products share the same AWS account because AWS Revenue Measurement cannot distinguish which product drives consumption within that account.