# Before you set up Amazon EMR

Complete the preliminary tasks detailed in this section before you launch an Amazon EMR cluster for the first time. These include setting up your AWS account if you need one and
and taking steps to set up secure communication.

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Create an Amazon EC2 key pair for SSH

###### Note

With Amazon EMR release versions 5.10.0 or later, you can configure Kerberos to authenticate users
and SSH connections to a cluster. For more information, see [Use Kerberos for authentication with Amazon EMR](emr-kerberos.md "emr-kerberos.md").

To authenticate and connect to the nodes in a cluster over a
secure channel using the Secure Shell (SSH) protocol, create an Amazon Elastic Compute Cloud (Amazon EC2) key pair before you launch the cluster. You can also create a cluster without a key pair. This is usually done with transient clusters that start, run steps, and then terminate automatically.

| If...                                                                                                            | Then...                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You already have an Amazon EC2 key pair that you want to use, or you don't need to authenticate to your cluster. | Skip this step.                                                                                                                                                                                                       |
| You need to create a key pair.                                                                                   | See [Creating your key pair using Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#having-ec2-create-your-key-pair "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#having-ec2-create-your-key-pair"). |

## Next steps

- For guidance on creating a sample cluster, see [Tutorial: Getting started with Amazon EMR](emr-gs.md "emr-gs.md").
- For more information on how to configure a custom cluster and control access to it, see
  [Plan, configure and launch Amazon EMR clusters](emr-plan.md "emr-plan.md") and [Security in Amazon EMR](emr-security.md "emr-security.md").
