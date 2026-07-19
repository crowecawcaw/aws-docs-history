# Prerequisites

Before you use the AWS Sustainability service for the first time, complete the following tasks.

###### Topics

- [Have an AWS account with usage](#setting-up-aws-account "#setting-up-aws-account")
- [Set up IAM access](#setting-up-iam-access "#setting-up-iam-access")

## Have an AWS account with usage

In order to see data in the AWS Sustainability console, you need to have usage of AWS services, otherwise your environmental impact will be zero.
The console shows data at the 0.000001 metric tons of carbon dioxide equivalent (MTCO2e), or 1 gram, resolution for carbon, and 0.000001 m³, or 1 milliliter, for water withdrawals.

## Set up IAM access

You must have the following IAM permissions in order to access your carbon emission data from AWS Sustainability.

- `sustainability:GetEstimatedCarbonEmissions`
- `sustainability:GetEstimatedCarbonEmissionsDimensionValues`

You must have the following IAM permissions in order to access water withdrawals data from AWS Sustainability.

- `sustainability:GetEstimatedWaterAllocation`
- `sustainability:GetEstimatedWaterAllocationDimensionValues`

For more information regarding IAM permissions, see [Identity and access management for AWS Sustainability](security-iam.md "security-iam.md")
