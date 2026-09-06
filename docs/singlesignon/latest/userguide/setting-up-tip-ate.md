

# Setting up trusted identity propagation with Amazon Athena workgroups
<a name="setting-up-tip-ate"></a>

The following procedure walks you through setting up Amazon Athena workgroups for trusted identity propagation. 

## Prerequisites
<a name="setting-up-tip-ate-prereqs"></a>

Before you can get started with this tutorial, you'll need to set up the following:

1. [Enable IAM Identity Center](enable-identity-center.md). [Organization instance](organization-instances-identity-center.md) is recommended. For more information, see [Prerequisites and considerations](trustedidentitypropagation-overall-prerequisites.md).

1. [Provision the users and groups from your source of identities into IAM Identity Center](tutorials.md).

1. This configuration requires [Amazon EMR Studio](setting-up-tip-emr.md), [AWS Lake Formation](tip-tutorial-lf.md), and [Amazon S3 Access Grants](tip-tutorial-s3.md).

## Setting up trusted identity propagation with Athena
<a name="setting-up-tip-ate-step1"></a>

To set up trusted identity propagation with Athena, the Athena administrator must:

1. Review [Considerations and limitations in using IAM Identity Center enabled Athena workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-identity-center.html#workgroups-identity-center-considerations-and-limitations). 

1. [Create an IAM Identity Center enabled Athena workgroup](https://docs.aws.amazon.com/athena/latest/ug/workgroups-identity-center.html#workgroups-identity-center-creating-an-identity-center-enabled-athena-workgroup).