

# Amazon Elastic Container Registry (Amazon ECR) in AWS GovCloud (US)
<a name="govcloud-ecr"></a>

Amazon Elastic Container Registry (Amazon ECR) is a fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Elastic Container Registry differs
<a name="govcloud-ecr-diffs"></a>

The following differences apply to Amazon Elastic Container Registry:
+  [Amazon ECR Dual-layer server-side encryption with AWS KMS (DSSE-KMS)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html) is available.
+  [Amazon ECR to Amazon ECR pull through cache rules](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html) are available only within the same partition.
+  [Amazon ECR public registries](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html) are not available.
+ The [Amazon ECR Public Gallery](https://docs.aws.amazon.com/AmazonECR/latest/public/public-gallery.html) isn’t hosted in AWS GovCloud (US). However, if external internet access is available, you should be able to reach and pull container images from the gallery.

## Documentation
<a name="govcloud-ecr-docs"></a>

 [Amazon Elastic Container Registry documentation](https://aws.amazon.com/documentation/ecr/).

## Export-controlled content
<a name="ecr-itar-boundary"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Do not enter export-controlled data in the following fields:
  + Repository name
  + Image tag
  + Image manifest
  + Lifecycle policy
  + Repository policy