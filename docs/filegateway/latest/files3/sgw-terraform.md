# AWS Storage Gateway Terraform module

[HashiCorp](https://www.hashicorp.com/ "https://www.hashicorp.com/")[Terraform](https://www.terraform.io/ "https://www.terraform.io/") is an open-source Infrastructure as
Code (IaC) engine developed using the HashiCorp Configuration Language (HCL). Terraform
provides a consistent command line interface (CLI) workflow that, in conjunction with
Amazon S3 File Gateway for the back-end infrastructure, can manage hundreds of cloud services and
codify cloud APIs into declarative configuration files.

You can use Terraform to safely deploy an Amazon S3 File Gateway as a virtual machine (VM) in your
on-premises virtual infrastructure. Terraform provides automation for on-premises virtual
infrastructure. See [Automate Amazon S3 File Gateway deployments in VMware with Terraform
by HashiCorp](https://aws.amazon.com/blogs/storage/automate-amazon-s3-file-gateway-deployments-in-vmware-with-terraform-by-hashicorp/ "https://aws.amazon.com/blogs/storage/automate-amazon-s3-file-gateway-deployments-in-vmware-with-terraform-by-hashicorp/") for information about quickly deploying an Amazon S3 File Gateway using
Terraform within an on-premises VMware virtual environment.

###### Note

You might need to configure Terraform to obtain the latest version of the AWS Storage Gateway
machine image for your preferred hypervisor platform. Storage Gateway machine images use the
following naming convention. The version number appended to the image name changes with
each version release.

`aws-storage-gateway-FILE_S3-1.25.0`

This automation provides you with a customizable Terraform module that you can use to
provision an Amazon S3 File Gateway with all of the resources and dependencies needed to fully deploy
the gateway and file shares in your VM environment. The Terraform module provisions the
gateway VM, activates the gateway, configures the cache disk, joins the gateway to a domain,
creates the Amazon S3 buckets, creates the file shares, and maps them to buckets. For a complete
example of a repository that contains Terraform code to create the resources required to run
Amazon S3 File Gateway on premises, see the [Terraform Storage Gateway
module](https://github.com/aws-ia/terraform-aws-storagegateway "https://github.com/aws-ia/terraform-aws-storagegateway") source code on GitHub.

###### Note

The Amazon S3 File Gateway module for Terraform is a community supported effort. It is not part
of an AWS service. Best-effort support is provided by the AWS Storage
community.
