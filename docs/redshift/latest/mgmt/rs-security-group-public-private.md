Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring security group

communication settings for an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup

This topic helps you configure your security groups to route and receive network
traffic appropriately. The following are a couple common use cases:

- You turn on public accessibility for an Amazon Redshift cluster or an Amazon Redshift Serverless
  workgroup, but it isn't receiving traffic. For this you must configure an
  inbound rule to allow traffic to reach it from the internet.
- Your cluster or workgroup isn't publicly accessible, and you use Redshift's
  pre-configured default VPC security group to allow inbound traffic. But you have
  a requirement to use a security group other than the default, and this custom
  security group doesn't allow inbound traffic. You must configure it to allow
  communication.
  The following sections help you choose the correct response for each use case and
  show you how to configure network traffic per your requirements. You can optionally use
  the steps to set up communication from other private security groups.

###### Note

Network traffic settings in most cases aren't configured automatically in Amazon Redshift.
This is because they can vary at a granular level, depending on whether the source
of traffic is the internet or a private security group, and because security
requirements vary.

## Public accessibility with default

or custom security group configuration

If you are creating or you already have a cluster or workgroup, perform the
following configuration steps to make it publicly accessible. This applies both to
when you choose the default security group or a custom security group:

1. Find the network settings:
   - For a provisioned Amazon Redshift cluster, choose the
     **Properties** tab, and then under
     **Network and security settings**, select the
     VPC for your cluster.
   - For an Amazon Redshift Serverless workgroup, choose **Workgroup
     configuration**. Choose the workgroup from the list.
     Then, under **Data access**, in the
     **Network and security** panel, choose
     **edit**.

2. Configure the Internet gateway and route table for your VPC. You start the
   configuration by choosing the VPC by name. It opens the VPC dashboard. To
   connect to a publicly accessible cluster or workgroup from the internet, an
   internet gateway must be attached to the route table. You can configure this
   by choosing **Route tables** in the VPC dashboard.
   Confirm that the internet gateway's target is set with source 0.0.0.0/0 or a
   public IP CIDR. The route table must be associated with the VPC where your
   cluster resides. For more information regarding setting up internet access
   for a VPC, like what is described here, see [Enable internet access](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#vpc-igw-internet-access "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#vpc-igw-internet-access") in the Amazon VPC documentation. For more
   information about configuring a route table, see [Configure route
   tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md").
3. After you configure the internet gateway and route table, return to the
   network settings for Redshift. Open inbound access by choosing the security
   group and then choosing the **Inbound rules**. Choose
   **Edit inbound rules**.
4. Choose the **Protocol** and **Port** for
   the inbound rule, or rules, per your requirements, to allow traffic from
   clients. For an RA3 cluster, select a port within the ranges 5431-5455 or
   8191-8215. When you are finished, save each rule.
5. Edit the **Publicly accessible** setting to enable it.
   You can do this from your cluster or workgroup's **Actions**
   menu.

When you turn on the publicly accessible setting, Redshift creates an Elastic IP
address. It's a static IP address that's associated with your AWS account. Clients
outside the VPC can use it to connect.

For more information about configuring your security group, see [Amazon Redshift security groups](security-network-isolation.md#working-with-security-groups "security-network-isolation.md#working-with-security-groups").

You can test your rules by connecting with a client, perform the following if
you're connecting to Amazon Redshift Serverless. After you finish network configuration,
connect with your client tool, such as [Amazon Redshift RSQL](rsql-query-tool.md "rsql-query-tool.md"). Using your
Amazon Redshift Serverless domain as the host, enter the following:

```
rsql -h `workgroup-name`.`account-id`.`region`.amazonaws.com -U `admin` -d dev -p 5439
```

## Private accessibility with default or

custom security group configuration

When you don't communicate through the internet to your cluster or workgroup,
it's referred to as _privately_ accessible. If you chose the
default security group when you created it, the security group includes the
following default communication rules:

- An inbound rule that allows traffic from all resources assigned to the
  security group.
- An outbound rule that allows all outbound traffic. The destination for
  this rule is 0.0.0.0/0. In classless inter-domain routing (CIDR) notation,
  it represents all possible IP addresses.

You can view the rules in the console by selecting the security group for your
cluster or workgroup.

If your cluster or workgroup and client both use the default security group, there
isn't any additional configuration necessary to allow network traffic. But if you
delete or change any rules in the default security group for Redshift or the
client, this no longer applies. In this case, you must configure rules to allow
inbound and outbound communication. A common security-group configuration is the
following:

- For a client Amazon EC2 instance:
  - An inbound rule that allows the IP address of the client.
  - An outbound rule that allows the IP address range (CIDR block) of
    all subnets provided for Redshift usage. Or your can specify
    0.0.0.0/0, which is all IP address ranges.

- For your Redshift cluster or workgroup:
  - An inbound rule that allows the client security group.
  - An outbound rule that allows traffic to 0.0.0.0/0. Typically, the
    outbound rule allows all outbound traffic. Optionally, you can add
    an outbound rule to allow traffic to the client security group. In
    this optional case, an outbound rule isn't always required, because
    response traffic for each request is allowed to reach the instance.
    For more details regarding request and response behavior, see [Security groups](../../../vpc/latest/userguide/security-groups.md "../../../vpc/latest/userguide/security-groups.md")
    in the _Amazon VPC user guide_.

If you change configuration for any subnets or security groups specified for
Redshift usage, you might need to change traffic rules accordingly to keep
communication open. For more information about creating inbound and outbound rules,
see [VPC CIDR blocks](../../../vpc/latest/userguide/vpc-cidr-blocks.md "../../../vpc/latest/userguide/vpc-cidr-blocks.md") in the
_Amazon VPC user guide_. For more information about connecting to
Amazon Redshift from a client, see [Configuring connections in Amazon Redshift](configuring-connections.md "configuring-connections.md").
