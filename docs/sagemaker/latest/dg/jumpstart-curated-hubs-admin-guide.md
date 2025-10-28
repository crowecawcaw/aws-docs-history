# Admin guide for private model hubs

in Amazon SageMaker JumpStart

There are actions that administrators can take related to curated model hubs that
users within your organization can access. This includes creating, adding, deleting, and
managing access of private hubs. This page also includes information about the supported
AWS Regions for curated private hubs, as well as the prerequisites needed to use
curated private model hubs.

## Supported AWS Regions

Curated private hubs are currently generally available in the following AWS commercial
Regions:

- us-east-1
- us-east-2
- us-west-2
- eu-west-1
- eu-central-1
- ap-northeast-1
- ap-northeast-2
- ap-south-1
- ap-southeast-1
- ap-southeast-2
- il-central-1 (SDK only)

The default maximum number of hubs allowed in a single Region is 50.

## Prerequisites

To use a curated private hub in Studio, you must have the following
prerequisites:

- An AWS account with administrator access
- An AWS Identity and Access Management (IAM) role with access to Amazon SageMaker Studio
- An Amazon SageMaker AI domain with JumpStart enabled
- If your users try to use proprietary models, they must have subscriptions to those models in AWS Marketplace.
- AWS accounts that are deploying proprietary models must have subscriptions to those models in AWS Marketplace.

For more information on getting started with Studio, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").
