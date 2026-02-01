Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Redshift resources in a VPC

You can launch an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup in a VPC on the EC2-VPC
platform based on the Amazon VPC service. For more information, see [Use EC2 to create your cluster](working-with-clusters.md#cluster-platforms "working-with-clusters.md#cluster-platforms").

###### Note

Launching clusters and Serverless workgroups into dedicated tenancy VPCs isn't
supported. For more information, see [Dedicated instances](../../../vpc/latest/userguide/dedicated-instance.md "../../../vpc/latest/userguide/dedicated-instance.md") in the _Amazon VPC User Guide_.

When provisioning resources in a VPC, you must do the following:

- **Provide VPC information.**

When you create a provisioned cluster in your VPC, you must provide your VPC
information by creating a cluster subnet group. This information includes the VPC ID
and a list of subnets in your VPC. When you launch a cluster, you provide the subnet
group so that Redshift can provision it in one of the subnets in the VPC. With
Amazon Redshift Serverless, the process is similar. You assign subnets directly to your
Serverless workgroup. But in the case of Serverless you don't create a subnet group.
For more information about creating subnet groups in Amazon Redshift, see [Subnets for Redshift resources](working-with-cluster-subnet-groups.md "working-with-cluster-subnet-groups.md"). For more information about
setting up the VPC, see [Getting started with Amazon VPC](../../../AmazonVPC/latest/GettingStartedGuide/GetStarted.md "../../../AmazonVPC/latest/GettingStartedGuide/GetStarted.md") in the
_Amazon VPC Getting Started Guide_.

- **Optionally, configure the accessibility
  options.**

Provisioned clusters and serverless workgroups in Amazon Redshift
are private by default.
If you configure your provisioned cluster or serverless workgroup to be publicly
accessible, Amazon Redshift uses an elastic IP address for the external IP address. An elastic
IP address is a static IP address. With it, you can change your underlying
configuration without affecting the IP address that clients use to connect. This
approach can be helpful for situations such as recovery after a failure. Whether you
create an elastic IP address depends on your availability zone relocation setting.
There are two options:

    1. If you have availability zone relocation turned on and you want to enable
     public access, you don’t specify an elastic IP address. An elastic IP
     address managed by Amazon Redshift is assigned. It's associated with your AWS
     account.
    2. If you have availability zone relocation turned off and you want to enable
     public access, you can opt to create an elastic IP address for the VPC in
     Amazon EC2, prior to launching your Amazon Redshift cluster or workgroup. If you don't
     create an IP address, Amazon Redshift provides a configured elastic IP address to
     use for the VPC. This elastic IP address is managed by Amazon Redshift and
     isn't associated with your AWS account.

For more information, see [Elastic IP addresses](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md") in the
_Amazon EC2 User Guide_.

In some cases, you might have a publicly accessible cluster in a VPC and you want
to connect to it by using the private IP address from within the VPC. If so, set the
following VPC parameters to `true`:

    + `DNS resolution`
    + `DNS hostnames`

Note that with Amazon Redshift Serverless, you can't connect in this manner.

Suppose that you have a publicly accessible provisioned cluster in a VPC but
don't set those parameters to `true` in the VPC. In these cases,
connections made from within the VPC resolve to the elastic IP address of the
resource instead of the private IP address. We recommend that you set these
parameters to `true` and use the private IP address for a publicly
accessible cluster when connecting from within the VPC. For more information, see
[Using DNS with your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the
_Amazon VPC User Guide._

###### Note

If you have an existing publicly accessible cluster in a VPC, connections from
within the VPC continue to use the elastic IP address to connect to it, until
you resize it, if it's a provisioned cluster. This occurs even with the
preceding parameters set. Any new clusters created follow the new behavior of
using the private IP address when connecting to a publicly accessible cluster
from within the same VPC.

The elastic IP address is an external IP address for accessing a resource outside
of a VPC. For a provisioned cluster, it isn't related to the **Public IP
addresses** and **Private IP addresses** that are
displayed in the Amazon Redshift console under **Node IP addresses**. The
public and private cluster node IP addresses appear regardless of whether a cluster
is publicly accessible or not. They're used only in certain circumstances to
configure ingress rules on the remote host. These circumstances occur when you load
data from an Amazon EC2 instance or other remote host using a Secure Shell (SSH)
connection. For more information, see [Step 1:
Retrieve the cluster public key and cluster node IP addresses](../dg/loading-data-from-remote-hosts.md#load-from-host-steps-retrieve-key-and-ips "../dg/loading-data-from-remote-hosts.md#load-from-host-steps-retrieve-key-and-ips") in the
_Amazon Redshift Database Developer Guide._

###### Note

Node IP addresses don't apply for a Redshift Serverless workgroup.

The option to associate a provisioned cluster with an elastic IP address is
available when you create the cluster or restore the cluster from a snapshot. In
some cases, you might want to associate the cluster with an elastic IP address or
change an elastic IP address that is associated with the cluster. To attach an
elastic IP address after the cluster is created, first update the cluster so that it
is not publicly accessible, then make it both publicly accessible and add an Elastic
IP address in the same operation.

For more information about how to make a provisioned cluster or Amazon Redshift Serverless
workgroup publicly accessible, and have an Elastic IP address assigned, see [Public accessibility with default or custom security group
configuration](rs-security-group-public-private.md#rs-security-group-public-default "rs-security-group-public-private.md#rs-security-group-public-default").

- **Associate a VPC security group.**

You grant inbound access using a VPC security group. For more information, see
[Configuring
security group communication settings for Amazon Redshift clusters](rs-security-group-public-private.md "rs-security-group-public-private.md"), which provides
guidance on configuring inbound and outbound rules between a client and a
provisioned cluster or an Amazon Redshift Serverless workgroup. Another resource that helps
you understand security groups is [Security in your VPC](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md") in the
_Amazon VPC User Guide_

###### Restoring a snapshot of a provisioned cluster or Serverless workgroup in a

VPC

A snapshot of a cluster or Serverless workgroup in a VPC can only be restored in a
VPC, not outside the VPC. You can restore it in the same VPC or another VPC in your
account. For more information about snapshots, see [Amazon Redshift snapshots and backups](working-with-snapshots.md "working-with-snapshots.md").
