Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating

a workgroup with a namespace

Complete the following steps to create a workgroup. For more information about
workgroup configuration, see [Workgroup properties](serverless-console-workgroups.md#serverless-workgroup-describe "serverless-console-workgroups.md#serverless-workgroup-describe").

1. Choose the **Serverless dashboard**. Then
   choose **Create workgroup**.
2. Enter the workgroup name.
3. Choose an **IP address type** for the workgroup.
   Choices include:
   - **IPv4** – With this option, your
     AWS resources only communicate over the IPv4 addressing
     protocol.
   - **Dual-stack mode** – With this
     option, your AWS resources can communicate over the IPv4,
     IPv6, or both addressing protocols. Also, you must associate an
     IPv6 CIDR block with the VPC and subnets used for your workgroup
     in the Amazon VPC. You can use the Amazon VPC console to create an Amazon VPC
     or update an existing Amazon VPC to use IPv6 addressing. For more
     information, see [IPv6
     support for your VPC;](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in the
     _Amazon VPC User Guide_.

4. Choose a **Virtual private cloud (VPC)** for
   Amazon Redshift Serverless. This assigns the workgroup to a specific virtual
   network in your AWS environment. When using **dual-stack
   mode**, the Amazon VPC you choose must support IPV6 addressing.
   For more information about an Amazon VPC, see [Overview of VPCs and
   subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md").
5. Choose one or more **VPC security groups**. For more
   information, see [Control traffic to resources using security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md").
6. Choose whether to enable extra compute resources for automatic
   optimizations. For more information, see [Allocating extra compute resources for automatic database optimization](../dg/t_extra-compute-autonomics.md "../dg/t_extra-compute-autonomics.md") in the _Amazon Redshift Database Developer Guide_.
7. Under **Subnet**, specify one or more subnets to
   associate with your database. These subnets are contained in the Amazon VPC
   you chose previously and must be in three distinct Availability
   Zones. For more
   information, see [Considerations when using Amazon Redshift Serverless](serverless-usage-considerations.md "serverless-usage-considerations.md").
8. Select the base RPU capacity that conforms with your
   requirements.

## Choose a

namespace

1. Choose either **Create a new namespace**, and
   enter the namespace name, or **Add to an existing
   namespace**, and select the namespace from the
   drop-down list.
2. For **Database name and password**, specify the
   name of the first database. You can also specify an admin other than
   your default console admin, by editing the **Admin user
   credentials**.
3. For **Permissions**, you choose
   **Associate IAM role** to associate
   specific IAM roles with your namespace and workgroup. For more
   information about associating IAM roles with Amazon Redshift, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").
4. You can customize your encryption settings by creating a new key
   or choosing a key other than the default. For **Audit
   logging**, choose the logs to export. Each log type
   specifies different metadata. Choose **Continue**
   to review your choices.

## Review

workgroup selections

1. Review your settings under **Review and create**.
   It shows the settings you chose in the previous steps.
2. Choose **Save**.

After you create the workgroup, it's added to the
**Workgroups** list.
