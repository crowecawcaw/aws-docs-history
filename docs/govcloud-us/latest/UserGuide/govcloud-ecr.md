# Amazon Elastic Container Registry (Amazon ECR) in AWS GovCloud (US)

Amazon Elastic Container Registry (Amazon ECR) is a fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

## How Amazon Elastic Container Registry differs

The following differences apply to Amazon Elastic Container Registry:

- [Amazon ECR Dual-layer server-side encryption with AWS KMS (DSSE-KMS)](../../../AmazonECR/latest/userguide/encryption-at-rest.md "../../../AmazonECR/latest/userguide/encryption-at-rest.md") is available.
- [Amazon ECR to Amazon ECR pull through cache rules](../../../AmazonECR/latest/userguide/pull-through-cache.md "../../../AmazonECR/latest/userguide/pull-through-cache.md") are available only within the same partition.
- [Amazon ECR public registries](../../../AmazonECR/latest/public/public-registries.md "../../../AmazonECR/latest/public/public-registries.md") are not available.
- The [Amazon ECR Public Gallery](../../../AmazonECR/latest/public/public-gallery.md "../../../AmazonECR/latest/public/public-gallery.md") isn’t hosted in AWS GovCloud (US). However, if external internet access is available, you should be able to reach and pull container images from the gallery.

## Documentation

[Amazon Elastic Container Registry documentation](https://aws.amazon.com/documentation/ecr/ "https://aws.amazon.com/documentation/ecr/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Do not enter export-controlled data in the following fields:

  - Repository name
  - Image tag
  - Image manifest
  - Lifecycle policy
  - Repository policy
