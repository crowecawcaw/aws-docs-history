# Understand shared AMI usage in Amazon EC2

_A shared AMI_ is an AMI that a developer created and made available for
others to use. One of the easiest ways to get started with Amazon EC2 is to use a shared AMI that
has the components you need and then add custom content. You can also create your own AMIs
and share them with others.

You use a shared AMI at your own risk. Amazon can't vouch for the integrity or security of
AMIs shared by other Amazon EC2 users. Therefore, you should treat shared AMIs as you would any
foreign code that you might consider deploying in your own data center, and perform the
appropriate due diligence. We recommend that you get an AMI from a
trusted source, such as a verified provider.

## Verified provider

In the Amazon EC2 console, public AMIs that are owned by Amazon or a verified Amazon partner are
marked **Verified provider**.

You can also use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") AWS CLI
command to identify the public AMIs that come from a verified provider. Public images
that are owned by Amazon or a verified partner have an aliased owner, which is either
`amazon`, `aws-backup-vault`, or `aws-marketplace`.
In the CLI output, these values appear for `ImageOwnerAlias`. Other users
can't alias their AMIs. This enables you to easily find AMIs from Amazon or verified
partners.

To become a verified provider, you must register as a seller on the AWS Marketplace. Once registered,
you can list your AMI on the AWS Marketplace. For more information, see [Getting started as a seller](../../../marketplace/latest/userguide/user-guide-for-sellers.md "../../../marketplace/latest/userguide/user-guide-for-sellers.md") and [AMI-based products](../../../marketplace/latest/userguide/ami-products.md "../../../marketplace/latest/userguide/ami-products.md") in
the _AWS Marketplace Seller Guide_.

###### Shared AMI topics

- [Find shared AMIs to use for Amazon EC2 instances](usingsharedamis-finding.md "usingsharedamis-finding.md")
- [Prepare to use shared AMIs for Linux](usingsharedamis-confirm.md "usingsharedamis-confirm.md")
- [Control the discovery and use of AMIs in Amazon EC2 with
  Allowed AMIs](ec2-allowed-amis.md "ec2-allowed-amis.md")
- [Make your AMI publicly available for use in Amazon EC2](sharingamis-intro.md "sharingamis-intro.md")
- [Understand block public access for AMIs](block-public-access-to-amis.md "block-public-access-to-amis.md")
- [Share an AMI with organizations and
  organizational units](share-amis-with-organizations-and-OUs.md "share-amis-with-organizations-and-OUs.md")
- [Share an AMI with specific AWS
  accounts](sharingamis-explicit.md "sharingamis-explicit.md")
- [Cancel having an AMI shared with your AWS account](cancel-sharing-an-AMI.md "cancel-sharing-an-AMI.md")
- [Recommendations for creating shared Linux AMIs](building-shared-amis.md "building-shared-amis.md")

###### If you're looking for information about other topics

- For information about creating an AMI, see [Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md") or [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md").
- For information about building, delivering, and maintaining your applications on the
  AWS Marketplace, see the [AWS Marketplace
  Documentation](../../../marketplace.md "../../../marketplace.md").
