# Transfer Family Terraform modules

[HashiCorp](https://www.hashicorp.com/ "https://www.hashicorp.com/")
[Terraform](https://www.terraform.io/ "https://www.terraform.io/") is an open-source Infrastructure as
Code (IaC) engine developed using the HashiCorp Configuration Language (HCL). Terraform
provides a consistent command line interface (CLI) workflow that, in conjunction with
AWS Transfer Family for the back-end infrastructure, can manage hundreds of cloud services and codify
cloud APIs into declarative configuration files.

You can use Terraform to safely deploy AWS Transfer Family SFTP servers and SFTP connectors, along
with associated dependencies and customizations. For the repository that contains Terraform
code to create the resources required to run AWS Transfer Family, see the [Terraform Transfer Family
module](https://github.com/aws-ia/terraform-aws-transfer-family "https://github.com/aws-ia/terraform-aws-transfer-family") source code on GitHub.

###### Note

The AWS Transfer Family modules for Terraform are a community supported effort. They are not part
of an AWS service. Best-effort support is provided by the AWS Storage
community.

## SFTP servers

This automation provides you with a customizable Terraform module and end-to-end
examples to create an SFTP endpoint (`PUBLIC` or `VPC` endpoint
types), integrate with Amazon CloudWatch for logging and monitoring, manage user identities for
endpoint access, and configure IAM roles for access to Amazon S3 buckets where files are
stored. The module supports multiple SSH public keys per user (up to 50 keys) for
enhanced security and key rotation capabilities.

## SFTP connectors

AWS Transfer Family Terraform module now supports deployment of SFTP connectors to transfer files
between Amazon S3 and remote SFTP servers. SFTP connectors provide a fully managed and
low-code capability to copy files between Amazon S3 and remote SFTP servers.

You can now use Terraform to programmatically provision your SFTP connectors,
associated dependencies and customizations in a single deployment. The module also
provides end-to-end examples to automate file transfer workflows based on a schedule or
event triggers. Using Terraform for deployment eliminates the need for time-consuming
and error-prone manual configurations, and provides you a fast, repeatable and secure
deployment option that can scale.

## AS2

To show support for AS2 Terraform templates, add a thumbs up reaction (👍) to the
[Transfer Family
Terraform templates feature request](https://github.com/aws-ia/terraform-aws-transfer-family/issues/62#issue-3364703944 "https://github.com/aws-ia/terraform-aws-transfer-family/issues/62#issue-3364703944"). You can also add a comment describing your use case.

## B2B Data Interchange

AWS B2B Data Interchange automates the transformation, validation, and generation of Electronic Data
Interchange (EDI) documents to and from JSON and XML data formats.
To show support for Terraform templates for B2B Data Interchange, add a thumbs up reaction (👍)
to the [feature request](https://github.com/aws-ia/terraform-aws-transfer-family/issues/63#issue-3364717955 "https://github.com/aws-ia/terraform-aws-transfer-family/issues/63#issue-3364717955").
You can also add a comment describing your use case.
