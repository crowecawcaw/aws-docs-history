# Amazon ECR in AWS GovCloud (US)

Amazon Elastic Container Registry (Amazon ECR) is a fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images.

## How Amazon Elastic Container Registry differs for AWS GovCloud (US)

- [Amazon ECR Dual-layer server-side encryption with AWS KMS (DSSE-KMS)](../../../AmazonECR/latest/userguide/encryption-at-rest.md "../../../AmazonECR/latest/userguide/encryption-at-rest.md") is available.
- [Amazon ECR pull through cache rules](../../../AmazonECR/latest/userguide/pull-through-cache.md "../../../AmazonECR/latest/userguide/pull-through-cache.md") aren’t supported.
- [Amazon ECR public registries](../../../AmazonECR/latest/public/public-registries.md "../../../AmazonECR/latest/public/public-registries.md") aren’t supported.
- The [Amazon ECR Public Gallery](../../../AmazonECR/latest/public/public-gallery.md "../../../AmazonECR/latest/public/public-gallery.md") isn’t hosted in AWS GovCloud (US). However, if external internet access is available, you should be able to reach and pull container images from the gallery.
- [Repository creation templates](../../../AmazonECR/latest/userguide/repository-creation-templates.md "../../../AmazonECR/latest/userguide/repository-creation-templates.md") aren’t supported.

## Documentation for Amazon Elastic Container Registry

[Amazon Elastic Container Registry documentation](https://aws.amazon.com/documentation/ecr/ "https://aws.amazon.com/documentation/ecr/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Do not enter export-controlled data in the following fields:
  - Repository name
  - Image tag
  - Image manifest
  - Lifecycle policy
  - Repository policy
