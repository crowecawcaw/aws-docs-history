# Step 1: Terraform configuration file download

You can use a Terraform configuration file to create and provision HashiCorp Terraform products.
These configurations are plain text files and describe the resources
that you want to provision. You can use the text editor of your choice to create, update, and save
configurations. For product creation, you must upload Terraform configurations as a **tar.gz file**.
In this tutorial, AWS Service Catalog provides a simple configuration file
so you can get started. The configuration creates an Amazon S3 bucket.

## Configuration file download

AWS Service Catalog provides a sample [`simple-s3-bucket.tar.gz`](https://github.com/aws-samples/service-catalog-engine-for-terraform-os/blob/main/sample-provisioning-artifacts/s3bucket.tar.gz?raw=true "https://github.com/aws-samples/service-catalog-engine-for-terraform-os/blob/main/sample-provisioning-artifacts/s3bucket.tar.gz?raw=true") configuration file
for you to use in this tutorial.

## Configuration file overview

The text of the sample configuration file follows:

```

variable "bucket_name" {
  type = string
}
provider "aws" {
}
resource "aws_s3_bucket" "bucket" {
  bucket = var.bucket_name
}
output regional_domain_name {
  value = aws_s3_bucket.bucket.bucket_regional_domain_name
}

```

###### Configuration Resources

The configuration file declares the resources to be created when AWS Service Catalog provisions the product.
It consists of the following sections:

- **Variable** (optional)
  – The value definitions that an administrator user (hub account administrator) can assign to customize the configuration. Variables provide a
  consistent interface to change how a given configuration behaves. The label after the
  variable keyword is a name for the variable, which must be unique among all variables in the
  same module. This name is used to assign an outside value to the variable, and to reference the
  variable's value from within the module.
- **Provider** (optional) – The cloud service
  provider for resource provisioning, which is `AWS`. AWS Service Catalog only supports `AWS`
  as the provider. As a result, the Terraform provisioning engine overrides any other listed
  provider to `AWS`.
- **Resource** (required) – The AWS infrastructure resource for
  provisioning. For this tutorial, the Terraform configuration file specifies Amazon S3.
- **Output** (optional) – The returned information or value, similar to
  returned values in a programming language. You can use outputs data to configure infrastructure
  workflow with automation tools.
