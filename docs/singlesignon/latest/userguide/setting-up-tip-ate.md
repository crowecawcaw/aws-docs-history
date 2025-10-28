# Setting up trusted identity propagation

with Amazon Athena workgroups

The following procedure walks you through setting up Amazon Athena workgroups
for trusted identity propagation.

## Prerequisites

Before you can get started with this tutorial, you'll need to set up
the following:

1. [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md").
   [Organization instance](organization-instances-identity-center.md "organization-instances-identity-center.md") is recommended. For more
   information, see [Prerequisites and
   considerations](trustedidentitypropagation-overall-prerequisites.md "trustedidentitypropagation-overall-prerequisites.md").
2. [Provision the users and groups from
   your source of identities into IAM Identity Center](tutorials.md "tutorials.md").
3. This configuration requires [Amazon EMR Studio](setting-up-tip-emr.md "setting-up-tip-emr.md"), [AWS Lake Formation](tip-tutorial-lf.md "tip-tutorial-lf.md"), and [Amazon S3
   Access Grants](tip-tutorial-s3.md "tip-tutorial-s3.md").

## Setting up trusted identity

propagation with Athena

To set up trusted identity propagation with Athena, the Athena
administrator must:

1. Review [Considerations and limitations in using IAM Identity Center enabled Athena
   workgroups](../../../athena/latest/ug/workgroups-identity-center.md#workgroups-identity-center-considerations-and-limitations "../../../athena/latest/ug/workgroups-identity-center.md#workgroups-identity-center-considerations-and-limitations").
2. [Create an IAM Identity Center enabled Athena workgroup](../../../athena/latest/ug/workgroups-identity-center.md#workgroups-identity-center-creating-an-identity-center-enabled-athena-workgroup "../../../athena/latest/ug/workgroups-identity-center.md#workgroups-identity-center-creating-an-identity-center-enabled-athena-workgroup").
