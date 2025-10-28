# Manage data perimeters for S3 bucket

download access in Image Builder

EC2 Image Builder maintains two classes of AWS service-owned S3 buckets that contain
downloadable resources needed to run Image Builder workloads in your account. If you use
data perimeters to control access to Amazon S3 in your environment, you might need to
explicitly allow access to these buckets. You can use the bucket ARN or bucket URL to
allowlist these buckets, depending on how you control access to Amazon S3.

**Component management bootstrapping scripts (Required)**

This S3 bucket contains bootstrapping scripts to set up the AWSTOE application
on the EC2 instances that are used to create images. Image Builder requires access
to download the scripts to support build and testing for new images.

- **S3 bucket ARN:**
  `arn:`<AWS partition>`:s3:::ec2imagebuilder-managed-resources-`<AWS Region>`-prod`
- **S3 bucket URL:**
  `https://ec2imagebuilder-managed-resources-`<AWS Region>`.s3.`<AWS Region>`.`<AWS partition-specific domain name>``

**Managed components**

This S3 bucket contains package payloads for Amazon managed components.
Image Builder requires access to download any managed components that are configured
in your recipes.

- **S3 bucket ARN:**
  `arn:`<AWS partition>`:s3:::ec2imagebuilder-toe-`<AWS Region>`-prod`
- **S3 bucket URL:**
  `https://ec2imagebuilder-toe-`<AWS Region>`.s3.`<AWS Region>`.`<AWS partition-specific domain name>``
