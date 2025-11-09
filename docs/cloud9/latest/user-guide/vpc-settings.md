AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# VPC settings for AWS Cloud9 Development Environments

Every AWS Cloud9 development environment associated with an Amazon Virtual Private Cloud (Amazon VPC) must meet specific VPC
requirements. These environments include EC2 environments, and SSH environments that are associated
with AWS Cloud compute instances that run within a VPC. Examples include Amazon EC2 and
Amazon Lightsail instances.

## Amazon VPC requirements for AWS Cloud9

The Amazon VPC that AWS Cloud9 uses requires the following settings. If you're already familiar
with these requirements and just want to create a compatible VPC, skip ahead to [Create a VPC plus other VPC resources](#vpc-settings-create-vpc "#vpc-settings-create-vpc").

Use the following checklist to confirm that the VPC meets **all** of the following requirements:

- The VPC can be in the same AWS account and AWS Region as the AWS Cloud9 development environment or
  The VPC can be a shared VPC in a different AWS account than the environment. However, the
  VPC must be in the same AWS Region as the environment. For more information on Amazon VPCs for
  an AWS Region, see [View a list of VPCs for an
  AWS Region](#vpc-settings-requirements-list-vpcs "#vpc-settings-requirements-list-vpcs"). For more instructions on
  creating an Amazon VPC for AWS Cloud9, see [Create a VPC plus other VPC resources](#vpc-settings-create-vpc "#vpc-settings-create-vpc"). For information about working with
  shared Amazon VPCs, see [Working with shared
  VPCs](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the _Amazon VPC User Guide._
- A VPC must have a public subnet. A subnet is public if its traffic is routed to an
  internet gateway. For a list of subnets for an Amazon VPC, see [View a list of subnets for a
  VPC](#vpc-settings-requirements-subnets-view "#vpc-settings-requirements-subnets-view").
- If your environment is accessing its EC2 instance directly though SSH, the
  instance can be launched into a public subnet only. For information about confirming
  whether a subnet is public, see [Confirm whether a subnet is
  public](#vpc-settings-requirements-subnet-public "#vpc-settings-requirements-subnet-public").
- If you're accessing a [no-ingress Amazon EC2 instance](ec2-ssm.md "ec2-ssm.md")
  using Systems Manager, the instance can be launched into either a public or a private
  subnet.
- If you're using a public subnet, attach an internet gateway to the VPC. This is so
  the AWS Systems Manager Agent (SSM Agent) for the instance can
  connect to Systems Manager.
- If you're using a private subnet, allow the instance for the subnet to communicate
  with the internet by hosting a NAT gateway in a public subnet. For more information
  about viewing or changing settings for an internet gateway, see [View or change
  settings for an internet gateway](#vpc-settings-requirements-internet-gateway-view "#vpc-settings-requirements-internet-gateway-view")
- The public subnet must have a route table with a minimum set of routes. To learn
  how to confirm whether a subnet has a route table, see[Confirm whether a subnet
  has a route table](#vpc-settings-requirements-subnet-route-table "#vpc-settings-requirements-subnet-route-table"). For information
  about how to create a route table, see [Create a route
  table](#vpc-settings-requirements-route-table-create "#vpc-settings-requirements-route-table-create").
- The associated security groups for the VPC (or for the AWS Cloud compute
  instance, depending on your architecture) must allow a minimum set of inbound and
  outbound traffic. For a list of security groups for an Amazon VPC, see [View a list of
  security groups for a VPC](#vpc-settings-requirements-security-groups-vpc-view "#vpc-settings-requirements-security-groups-vpc-view"). For more
  information about creating a security group in an Amazon VPC, see [Create a security
  group in a VPC](#vpc-settings-requirements-security-group-vpc-create "#vpc-settings-requirements-security-group-vpc-create").
- For an additional layer of security, if the VPC has a network ACL, the network ACL
  must allow a minimum set of inbound and outbound traffic. To confirm whether an Amazon VPC
  has at least one network ACL, see [Confirm whether a VPC
  has at least one network ACL](#vpc-settings-requirements-network-acl-confirm "#vpc-settings-requirements-network-acl-confirm"). For information
  about creating a network ACL, see [Create a network
  ACL](#vpc-settings-requirements-network-acl-create "#vpc-settings-requirements-network-acl-create").
- If your development environment is [using SSM to access
  an EC2 instance](ec2-ssm.md "ec2-ssm.md"), ensure that the instance is assigned a public IP address
  by the public subnet it's launched into. To do so, you must enable the automatic
  assignment of a public IP address option for the public subnet, and set it to
  `Yes`. You can enable this on the public subnet before creating an
  AWS Cloud9 environment within the subnet settings page. For the steps involved in
  modifying auto-assign IP settings in a public subnet, see [Modify the public IPv4 addressing attribute for your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md") in the
  _Amazon VPC User Guide_. For more information about configuring a
  public and private subnet, see [Configuring a subnet as public or private](#public-private-subnet "#public-private-subnet")

###### Note

For the following procedures, sign in to the AWS Management Console and use administrator
credentials to open either the Amazon VPC console ([https://console.aws.amazon.com/vpc](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc")) or Amazon EC2 console ([https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2")) .

If you use the AWS CLI or the AWS CloudShell, we recommend that you configure the AWS CLI or
the AWS CloudShell with the credentials for an administrator in your AWS account. If you
can't do this, check with your AWS account administrator.

### View a list of VPCs for an

AWS Region

To use the Amazon VPC console, in the AWS navigation bar, choose the AWS Region that
AWS Cloud9 creates the environment in. Then, choose **Your VPCs** in the
navigation pane.

To use the AWS CLI or the AWS CloudShell, run the Amazon EC2**`describe-vpcs`** command, for example, as follows.

```
aws ec2 describe-vpcs --output table --query 'Vpcs[*].VpcId' --region us-east-2
```

In the preceding command, replace `us-east-2` with the AWS Region that
AWS Cloud9 creates the environment in. To run the preceding command in Windows, replace the single
quotation marks (' ') with double quotation marks (" "). To run the preceding command
with the `aws-shell`, omit `aws`.

The output contains the list of VPC IDs.

### View a list of subnets for a

VPC

To use the Amazon VPC console, choose **Your VPCs** in the navigation
pane. Note the ID of the VPC in the **VPC ID** column. Then choose
**Subnets** in the navigation pane, and look for subnets that
contain that ID in the **VPC** column.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`describe-subnets`** command, for example, as follows.

```
aws ec2 describe-subnets --output table --query 'Subnets[*].[SubnetId,VpcId]' --region us-east-2
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the subnets. To run the preceding command in Windows, replace the single
quotation marks (' ') with double quotation marks (" "). To run the preceding command
with the `aws-shell`, omit `aws`.

In the output, look for subnets that match the VPC ID.

### Confirm whether a subnet is

public

###### Important

Suppose that you're launching your environment's EC2 instance into a private
subnet. Make sure that outbound traffic is allowed for that instance so that it can
connect to the SSM service. For private subnets, outbound traffic is usually
configured through a network address translation (NAT) gateway or VPC endpoints. (A
NAT gateway requires a public subnet.)

Suppose that you choose VPC endpoints instead of a NAT gateway for accessing
SSM. Automatic updates and security patches for your instance might not work if
they depend on internet access. You can use other applications, such as [AWS Systems
Manager Patch Manager](../../../systems-manager/latest/userguide/patch-manager.md "../../../systems-manager/latest/userguide/patch-manager.md"), to manage any software updates that your
environment might require. AWS Cloud9 software will be updated as normal.

To use the Amazon VPC console, choose **Subnets** in the navigation pane.
Select the box next to the subnet that you want AWS Cloud9 to use. On the **Route
Table** tab, if there's an entry in the **Target** column
that starts with **igw-**, the subnet is public.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`describe-route-tables`** command.

```
aws ec2 describe-route-tables --output table --query 'RouteTables[*].Routes[*].{GatewayIds:GatewayId}' --region us-east-2 --filters Name=association.subnet-id,Values=subnet-12a3456b
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the subnet, and replace `subnet-12a3456b` with the subnet ID. To run
the preceding command in Windows, replace the single quotation marks (' ') with double
quotation marks (" "). To run the preceding command with the `aws-shell`,
omit `aws`.

In the output, if there's at least one result that starts with `igw-`, the
subnet is public.

In the output, if there are no results, the route table might be associated with the
VPC instead of the subnet. To confirm this, run the Amazon EC2**`describe-route-tables`** command for the VPC related to the subnet instead of the subnet itself, for
example, as follows.

```
aws ec2 describe-route-tables --output table --query 'RouteTables[*].Routes[*].{GatewayIds:GatewayId}' --region us-east-1 --filters Name=vpc-id,Values=vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the VPC, and replace `vpc-1234ab56` with the VPC ID. To run the
preceding command in Windows, replace the single quotation marks (' ') with double
quotation marks (" "). To run the preceding command with the `aws-shell`,
omit `aws`.

In the output, if there's at least one result that starts with `igw-`, the
VPC contains an internet gateway.

### View or change

settings for an internet gateway

To use the Amazon VPC console, choose **Internet Gateways** in the
navigation pane. Select the box next to the internet gateway. To see the settings, look
at each of the tabs. To change a setting on a tab, choose **Edit** if
applicable, and then follow the on-screen directions.

To use the AWS CLI or the `aws-shell` to see the settings, run the
Amazon EC2**`describe-internet-gateways`** command.

```
aws ec2 describe-internet-gateways --output table --region us-east-2 --internet-gateway-id igw-1234ab5c
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the internet gateway, and replace `igw-1234ab5c` with the internet
gateway ID. To run the preceding command with the `aws-shell`, omit
`aws`.

### Create an internet

gateway

To use the Amazon VPC console, choose **Internet Gateways** in the
navigation pane. Choose **Create internet gateway**, and then follow
the on-screen directions.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`create-internet-gateway`** command.

```
aws ec2 create-internet-gateway --output text --query 'InternetGateway.InternetGatewayId' --region us-east-2
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the new internet gateway. To run the preceding command in Windows, replace the
single quotation marks (' ') with double quotation marks (" "). To run the preceding
command with the `aws-shell`, omit `aws`.

The output contains the ID of the new internet gateway.

### Attach an internet

gateway to a VPC

To use the Amazon VPC console, choose **Internet Gateways** in the
navigation pane. Select the box next to the internet gateway. Choose **Actions,
Attach to VPC** if available, and then follow the on-screen
directions.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`attach-internet-gateway`** command, for example, as follows.

```
aws ec2 attach-internet-gateway --region us-east-2 --internet-gateway-id igw-a1b2cdef --vpc-id vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the internet gateway. Replace `igw-a1b2cdef` with the internet
gateway ID. And replace `vpc-1234ab56` with the VPC ID. To run the preceding
command with the `aws-shell`, omit `aws`.

### Confirm whether a subnet

has a route table

To use the Amazon VPC console, choose **Subnets** in the navigation pane.
Select the box next to the public subnet for the VPC that you want AWS Cloud9 to use. On the
**Route table** tab, if there's a value for **Route
Table**, the public subnet has a route table.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`describe-route-tables`** command.

```
aws ec2 describe-route-tables --output table --query 'RouteTables[*].Associations[*].{RouteTableIds:RouteTableId}' --region us-east-2 --filters Name=association.subnet-id,Values=subnet-12a3456b
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the public subnet, and replace `subnet-12a3456b` with the public
subnet ID. To run the preceding command in Windows, replace the single quotation marks
(' ') with double quotation marks (" "). To run the preceding command with the
`aws-shell`, omit `aws`.

If there are values in the output, the public subnet has at least one route
table.

In the output, if there are no results, the route table might be associated with the
VPC instead of the subnet. To confirm this, run the Amazon EC2**`describe-route-tables`** command for the subnet's related VPC instead of the subnet itself, for
example, as follows.

```
aws ec2 describe-route-tables --output table --query 'RouteTables[*].Associations[*].{RouteTableIds:RouteTableId}' --region us-east-2 --filters Name=vpc-id,Values=vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the VPC, and replace `vpc-1234ab56` with the VPC ID. To run the
preceding command in Windows, replace the single quotation marks (' ') with double
quotation marks (" "). To run the preceding command with the `aws-shell`,
omit `aws`.

In the output, if there's at least one result, the VPC has at least one route
table.

### Attach a route table to a

subnet

To use the Amazon VPC console, choose **Route Tables** in the navigation
pane. Select the box next to the route table that you want to attach. On the
**Subnet Associations** tab, choose **Edit**,
select the box next to the subnet you want to attach it to, and then choose
**Save**.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`associate-route-table`** command, for example, as follows.

```
aws ec2 associate-route-table --region us-east-2 --subnet-id subnet-12a3456b --route-table-id rtb-ab12cde3
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the route table. Replace `subnet-12a3456b` with the subnet ID. And
replace `rtb-ab12cde3` with the route table ID. To run the preceding command
with the `aws-shell`, omit `aws`.

### Create a route

table

To use the Amazon VPC console, choose **Route Tables** in the navigation
pane. Choose **Create Route Table**, and then follow the on-screen
directions.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`create-route-table`** command, for example, as follows.

```
aws ec2 create-route-table --output text --query 'RouteTable.RouteTableId' --region us-east-2 --vpc-id vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the new route table, and replace `vpc-1234ab56` with the VPC ID. To
run the preceding command in Windows, replace the single quotation marks (' ') with
double quotation marks (" "). To run the preceding command with the
`aws-shell`, omit `aws`.

The output contains the ID of the new route table.

### View or change settings for

a route table

To use the Amazon VPC console, choose **Route Tables** in the navigation
pane. Select the box next to the route table. To see the settings, look at each of the
tabs. To change a setting on a tab, choose **Edit**, and then follow
the on-screen directions.

To use the AWS CLI or the `aws-shell` to see the settings, run the
Amazon EC2**`describe-route-tables`** command, for example, as follows.

```
aws ec2 describe-route-tables --output table --region us-east-2 --route-table-ids rtb-ab12cde3
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the route table, and replace `rtb-ab12cde3` with the route table ID.
To run the preceding command with the `aws-shell`, omit
`aws`.

### Minimum suggested route

table settings for AWS Cloud9

| **Destination** | **Target**                | **Status** | **Propagated** |
| --------------- | ------------------------- | ---------- | -------------- |
| CIDR-BLOCK      | local                     | Active     | No             |
| 0.0.0.0/0       | `igw-INTERNET-GATEWAY-ID` | Active     | No             |

In these settings, `*CIDR-BLOCK*` is the CIDR block for
the subnet, and `igw-*INTERNET-GATEWAY-ID*` is the ID of a compatible internet gateway.

### View a list of

security groups for a VPC

To use the Amazon VPC console, choose **Security Groups** in the
navigation pane. In the **Search Security Groups** box, enter the VPC
ID or name, and then press `Enter`. Security groups for that VPC appear in
the list of search results.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`describe-security-groups`** command.

```
aws ec2 describe-security-groups --output table --query 'SecurityGroups[*].GroupId' --region us-east-2 --filters Name=vpc-id,Values=vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the VPC, and replace `vpc-1234ab56` with the VPC ID. To run the
preceding command in Windows, replace the single quotation marks (' ') with double
quotation marks (" "). To run the preceding command with the `aws-shell`,
omit `aws`.

The output contains the list of security group IDs for that VPC.

### View a list of

security groups for an AWS Cloud compute instance

To use the Amazon EC2 console, expand **Instances** in the navigation
pane, and then choose **Instances**. In the list of instances, choose
the box next to the instance. Security groups for that instance appear in the
**Description** tab next to **Security
groups**.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`describe-security-groups`** command, for example, as follows.

```
aws ec2 describe-instances --output table --query 'Reservations[*].Instances[*].NetworkInterfaces[*].Groups[*].GroupId' --region us-east-2 --instance-ids i-12a3c456d789e0123
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the instance, and replace `i-12a3c456d789e0123` with the instance
ID. To run the preceding command in Windows, replace the single quotation marks (' ')
with double quotation marks (" "). To run the preceding command with the
`aws-shell`, omit `aws`.

The output contains the list of security group IDs for that instance.

### View or change

settings for a security group in a VPC

To use the Amazon VPC console, choose **Security Groups** in the
navigation pane. Select the box next to the security group. To see the settings, look at
each of the tabs. To change a setting on a tab, choose **Edit** if
applicable, and then follow the on-screen directions.

To use the AWS CLI or the `aws-shell` to see the settings, run the
Amazon EC2**`describe-security-groups`** command, for example, as follows.

```
aws ec2 describe-security-groups --output table --region us-east-2 --group-ids sg-12a3b456
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the instance, and replace `sg-12a3b456` with the security group ID.
To run the preceding command with the `aws-shell`, omit
`aws`.

### View or change

settings for an AWS Cloud compute instance security group

To use the Amazon EC2 console, expand **Instances** in the navigation
pane, and then choose **Instances**. In the list of instances, select
the box next to the instance. In the **Description** tab, for
**Security groups**, choose the security group. Look at each of the
tabs. To change a setting on a tab, choose **Edit** if applicable, and
then follow the on-screen directions.

To use the AWS CLI or the `aws-shell` to see the settings, run the
Amazon EC2**`describe-security-groups`** command, for example, as follows.

```
aws ec2 describe-security-groups --output table --region us-east-2 --group-ids sg-12a3b456
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the instance, and replace `sg-12a3b456` with the security group ID.
To run the preceding command with the `aws-shell`, omit
`aws`.

### Minimum inbound and

outbound traffic settings for AWS Cloud9

###### Important

IA security group for an instance might not have an inbound rule. If this happens,
this means no incoming traffic originating from another host to the instance is
allowed. For information about using no-ingress EC2 instances, see [Accessing no-ingress EC2 instances with AWS Systems Manager](ec2-ssm.md "ec2-ssm.md").

- **Inbound**: All IP addresses using SSH over port 22.
  However, you can restrict these IP addresses to only those that AWS Cloud9 uses. For
  more information, see [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md "ip-ranges.md").

###### Note

For EC2 environments that are created on or after July 31 2018, AWS Cloud9 uses
security groups to restrict inbound IP addresses using SSH over port 22. These
inbound IP addresses are specifically only the addresses that AWS Cloud9 uses. For
more information, see [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md "ip-ranges.md").

- **Inbound (network ACLs only)**: For the
  EC2 environments and the SSH environments that are associated with Amazon EC2 instances
  that run Amazon Linux or Ubuntu Server, all IP addresses use TCP over ports 32768-61000.
  For more information, and for port ranges for other Amazon EC2 instance types, see
  [Ephemeral
  ports](../../../vpc/latest/userguide/VPC_ACLs.md#VPC_ACLs_Ephemeral_Ports "../../../vpc/latest/userguide/VPC_ACLs.md#VPC_ACLs_Ephemeral_Ports") in the _Amazon VPC User Guide_.
- **Outbound**: All traffic sources using any protocol
  and port.

You can set this behavior at the security group level. For an additional level of
security, you can also use a network ACL. For more information, see [Comparison of security
groups and network ACLs](../../../vpc/latest/userguide/VPC_Security.md#VPC_Security_Comparison "../../../vpc/latest/userguide/VPC_Security.md#VPC_Security_Comparison") in the _Amazon VPC User Guide_.

For example, to add inbound and outbound rules to a security group, you could set up
those rules as follows.

| Inbound rules | **Type** | **Protocol** | **Port range**                                                                                                        | **Source** |
| ------------- | -------- | ------------ | --------------------------------------------------------------------------------------------------------------------- | ---------- |
| SSH (22)      | TCP (6)  | 22           | 0.0.0.0 (But see the following note and [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md "ip-ranges.md").) |

###### Note

For EC2 environments that are created on or after July 31 2018, AWS Cloud9 adds an
inbound rule to restrict inbound IP addresses using SSH over port 22. This restricts
to specifically only the addresses that AWS Cloud9 uses. For more information, see [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md "ip-ranges.md").

| Outbound rules | **Type** | **Protocol** | **Port range** | **Source** |
| -------------- | -------- | ------------ | -------------- | ---------- |
| All traffic    | ALL      | ALL          | 0.0.0.0/0      |

If you also choose to add inbound and outbound rules to a network ACL, you can set up
those rules as follows.

| Inbound rules | **Rule #**      | **Type** | **Protocol**                                                                                                                                                                                                                                                | **Port range**                                                                                 | **Source** | **Allow / Deny** |
| ------------- | --------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------- | ---------------- |
| 100           | SSH (22)        | TCP (6)  | 22                                                                                                                                                                                                                                                          | 0.0.0.0 (But see [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md "ip-ranges.md").) | ALLOW      |
| 200           | Custom TCP rule | TCP (6)  | 32768-61000 (For Amazon Linux and Ubuntu Server instances. For other instance<br>types, see [Ephemeral<br>Ports](../../../vpc/latest/userguide/VPC_ACLs.md#VPC_ACLs_Ephemeral_Ports "../../../vpc/latest/userguide/VPC_ACLs.md#VPC_ACLs_Ephemeral_Ports").) | 0.0.0.0/0                                                                                      | ALLOW      |
| `*`           | All traffic     | ALL      | ALL                                                                                                                                                                                                                                                         | 0.0.0.0/0                                                                                      | DENY       |

| Outbound rules | **Rule #**  | **Type** | **Protocol** | **Port range** | **Source** | **Allow / Deny** |
| -------------- | ----------- | -------- | ------------ | -------------- | ---------- | ---------------- |
| 100            | All traffic | ALL      | ALL          | 0.0.0.0/0      | ALLOW      |
| `*`            | All traffic | ALL      | ALL          | 0.0.0.0/0      | DENY       |

For more information about security groups and network ACLs, see the following in the
_Amazon VPC User Guide_.

- [Security](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md")
- [Security groups for your
  VPC](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md")
- [Network ACLs](../../../vpc/latest/userguide/VPC_ACLs.md "../../../vpc/latest/userguide/VPC_ACLs.md")

### Create a security

group in a VPC

To use the Amazon VPC or Amazon EC2 consoles, do one of the following actions:

- In the Amazon VPC console, choose **Security Groups** in the
  navigation pane. Choose **Create Security Group**, and then
  follow the on-screen directions.
- In the Amazon EC2 console, expand **Network & Security** in the
  navigation pane, and then choose **Security Groups**. Choose
  **Create Security Group**, and then follow the on-screen
  directions.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`create-security-group`** command, for example, as follows.

```
aws ec2 create-security-group --region us-east-2 --vpc-id vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the VPC, and replace `vpc-1234ab56` with the VPC ID. To run the
preceding command with the `aws-shell`, omit `aws`.

### Confirm whether a VPC

has at least one network ACL

To use the Amazon VPC console, choose **Your VPCs** in the navigation
pane. Choose the box next to the VPC that you want AWS Cloud9 to use. On the
**Summary** tab, if there's a value for **Network
ACL**, the VPC has at least one network ACL.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2 **`describe-network-acls`** command.

```
aws ec2 describe-network-acls --output table --query 'NetworkAcls[*].Associations[*].NetworkAclId' --region us-east-2 --filters Name=vpc-id,Values=vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the VPC, and replace `vpc-1234ab56` with the VPC ID. To run the
preceding command in Windows, replace the single quotation marks (' ') with double
quotation marks (" "). To run the preceding command with the `aws-shell`,
omit `aws`.

If the output contains at least one entry in the list, the VPC has at least one
network ACL.

### View a list of network

ACLs for a VPC

To use the Amazon VPC console, choose **Network ACLs** in the navigation
pane. In the **Search Network ACLs** box, enter the VPC ID or name, and
then press `Enter`. Network ACLs for that VPC appear in the list of search
results.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2**`describe-network-acls`** command.

```
aws ec2 describe-network-acls --output table --query 'NetworkAcls[*].Associations[*].NetworkAclId' --region us-east-2 --filters Name=vpc-id,Values=vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the VPC, and replace `vpc-1234ab56` with the VPC ID. To run the
preceding command in Windows, replace the single quotation marks (' ') with double
quotation marks (" "). To run the preceding command with the `aws-shell`,
omit `aws`.

The output contains a list of network ACLs for that VPC.

### View or change settings for

a network ACL

To use the Amazon VPC console, choose **Network ACLs** in the navigation
pane. Choose the box next to the network ACL. To see the settings, look at each of the
tabs. To change a setting on a tab, choose **Edit**, if applicable, and
then follow the on-screen directions.

To use the AWS CLI or the `aws-shell` to see the settings, run the
Amazon EC2**`describe-network-acls`** command.

```
aws ec2 describe-network-acls --output table --region us-east-2 --network-acl-ids acl-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the network ACL, and replace `acl-1234ab56` with the network ACL ID.
To run the preceding command with the `aws-shell`, omit
`aws`.

### Create a network

ACL

To use the Amazon VPC console, choose **Network ACLs** in the navigation
pane. Choose **Create Network ACL**, and then follow the on-screen
directions.

To use the AWS CLI or the `aws-shell`, run the Amazon EC2 **`create-network-acl`** command.

```
aws ec2 create-network-acl --region us-east-2 --vpc-id vpc-1234ab56
```

In the preceding command, replace `us-east-2` with the AWS Region that
contains the VPC that you want to attach the new network ACL to. Also, replace
`vpc-1234ab56` with the VPC ID. To run the preceding command with the
`aws-shell`, omit `aws`.

## Create a VPC plus other VPC resources

Use the following procedure to create a VPC and the additional VPC resources that you
need to run your application. VPC resources include subnets, route tables, internet
gateways, and NAT gateways.

###### To create a VPC, subnets, and other VPC resources using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the VPC dashboard, choose **Create VPC**.
3. For **Resources to create**, choose **VPC and more**.
4. To create name tags for the VPC resources, keep **Name tag
   auto-generation** selected. To provide your own name tags for the VPC
   resources, clear it.
5. For **IPv4 CIDR block**, you must enter an IPv4 address range for
   the VPC. The recommended IPv4 range for AWS Cloud9 is `10.0.0.0/16`.
6. (Optional) To support IPv6 traffic, choose **IPv6 CIDR block**,
   **Amazon-provided IPv6 CIDR block**.
7. Choose a **Tenancy** option. This option defines if EC2 instances
   that you launch into the VPC will run on hardware that's shared with other
   AWS accounts or on hardware that's dedicated for your use only. If you choose the
   tenancy of the VPC to be `Default`, EC2 instances launched into this VPC
   will use the tenancy attribute that's specified when you launch the instance. For
   more information, see [Launch an instance
   using defined parameters](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md") in the _Amazon EC2 User Guide_.

If you choose the tenancy of the VPC to be `Dedicated`, the instances
will always run as [Dedicated
Instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md") on hardware that's dedicated for your use. If you're using
AWS Outposts, your Outpost requires private connectivity, and you must
use `Default` tenancy. 8. For **Number of Availability Zones (AZs)**, we recommend that you
provision subnets in at least two Availability Zones for a production
environment. To choose the AZs for your subnets, expand **Customize
AZs**. Otherwise, you can let AWS choose the AZs for you. 9. To configure your subnets, choose values for **Number of public
subnets** and **Number of private subnets**. To choose
the IP address ranges for your subnets, expand **Customize subnets CIDR
blocks**. Otherwise, let AWS choose them for you. 10. (Optional) If resources in a private subnet need access to the public internet
over IPv4: For **NAT gateways**, choose the number of AZs in which
to create NAT gateways. In production, we recommend that you deploy a NAT gateway in
each AZ with resources that need access to the public internet. 11. (Optional) If resources in a private subnet need access to the public internet
over IPv6: For **Egress only internet gateway**, choose
**Yes**. 12. (Optional) To access Amazon S3 directly from your VPC, choose **VPC
endpoints**, **S3 Gateway**. This creates a gateway VPC
endpoint for Amazon S3. For more information, see [Gateway VPC endpoints](../../../vpc/latest/privatelink/gateway-endpoints.md "../../../vpc/latest/privatelink/gateway-endpoints.md") in
the _AWS PrivateLink Guide_. 13. (Optional) For **DNS options**, both options for domain name
resolution are enabled by default. If the default doesn't meet your needs, you can
deactivate these options. 14. (Optional) To add a tag to your VPC, expand **Additional tags**,
choose **Add new tag**, and enter a tag key and a tag value. 15. In the **Preview** pane, you can visualize the relationships
between the VPC resources that you configured. Solid lines represent relationships
between resources. Dotted lines represent network traffic to NAT gateways, internet
gateways, and gateway endpoints. After you create the VPC, you can visualize the
resources in your VPC in this format at any time using the **Resource
map** tab. 16. After you finish configuring your VPC, choose **Create
VPC**.

## Create a VPC only

Use the following procedure to create a VPC with no additional VPC resources by using
the Amazon VPC console.

###### To create a VPC with no additional VPC resources using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the VPC dashboard, choose **Create VPC**.
3. For **Resources to create**, choose **VPC only**.
4. (Optional) For **Name tag**, enter a name for your
   VPC. Doing so creates a tag with a key of `Name` and the
   value that you specify.
5. For **IPv4 CIDR block**, do one of the following:
   - Choose **IPv4 CIDR manual input** and enter an IPv4 address
     range for your VPC. The recommended IPv4 range for AWS Cloud9 is
     `10.0.0.0/16`.
   - Choose **IPAM-allocated IPv4 CIDR block**, select an
     Amazon VPC IP Address Manager (IPAM) IPv4 address pool and a netmask. The size of the CIDR block
     is limited by the allocation rules on the IPAM pool. IPAM is a VPC feature that
     helps you plan, track, and monitor IP addresses for your AWS workloads. For
     more information, see [What is IPAM?](../../../vpc/latest/ipam/what-it-is-ipam.md "../../../vpc/latest/ipam/what-it-is-ipam.md") in the
     _Amazon Virtual Private Cloud Administrator's Guide_.

   If you use IPAM to manage your IP addresses, we recommend that you choose
   this option. Otherwise, the CIDR block that you specify for your VPC might
   overlap with an IPAM CIDR allocation.

6. (Optional) To create a dual stack VPC, specify an IPv6 address range
   for your VPC. For **IPv6 CIDR block**, do one of the
   following:
   - Choose **IPAM-allocated IPv6 CIDR block** and
     select your IPAM IPv6 address pool. The size of the CIDR block
     is limited by the allocation rules on the IPAM pool.
   - To request an IPv6 CIDR block from an Amazon pool of IPv6 addresses, choose
     **Amazon-provided IPv6 CIDR block**. For **Network
     Border Group**, select the group from which AWS advertises IP
     addresses. Amazon provides a fixed IPv6 CIDR block size of /56.
   - Choose **IPv6 CIDR owned by me** to use an IPv6 CIDR block that you
     brought to AWS using [bring your own IP
     addresses (BYOIP)](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md"). For **Pool**, choose the
     IPv6 address pool from which to allocate the IPv6 CIDR block.

7. (Optional) Choose a **Tenancy** option. This option defines if
   EC2 instances that you launch into the VPC will run on hardware that's shared with
   other AWS accounts or on hardware that's dedicated for your use only. If you choose
   the tenancy of the VPC to be `Default`, EC2 instances that are launched
   into this VPC will use the tenancy attribute that's specified when you launch the
   instance. For more information, see [Launch an instance
   using defined parameters](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md") in the _Amazon EC2 User Guide_.

If you choose the tenancy of the VPC to be `Dedicated`, the instances
will always run as [Dedicated
Instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md") on hardware that's dedicated for your use. If you're using
AWS Outposts, your Outpost requires private connectivity, and you must
use `Default` tenancy. 8. (Optional) To add a tag to your VPC, choose **Add new tag**
and enter a tag key and a tag value. 9. Choose **Create VPC**. 10. After you create a VPC, you can add subnets.

## Create a subnet for AWS Cloud9

You can use the Amazon VPC console to create a subnet for a VPC that's compatible with AWS Cloud9.
Whether you can create a private or public subnet for your EC2 instance depends on how your
environment connects to it:

- **Direct access through SSH:** public subnet
  only
- **Access through Systems Manager**: public or private
  subnet

The option to launch your environment's EC2 into a private subnet is available only if
you create a "no-ingress" EC2 environment using [the console, command line,
or AWS CloudFormation](ec2-ssm.md "ec2-ssm.md").

You follow the [same steps to create a subnet](#create-subnet-proc "#create-subnet-proc")
that can be made public or private. If the subnet is then associated with a route table
that has a route to an internet gateway, it becomes a public subnet. But if the subnet is
associated with a route table that does not have a route to an internet gateway, it becomes
a private subnet. For more information, see [Configuring a subnet as public or private](#public-private-subnet "#public-private-subnet")

If you followed the previous procedure to create a VPC for AWS Cloud9, you don't also need to
follow this procedure. This is because the **Create new VPC** wizard
creates a subnet for you automatically.

###### Important

- The AWS account must already have a compatible VPC in the same AWS Region
  for the environment. For more information, see the VPC requirements in [Amazon VPC requirements for AWS Cloud9](#vpc-settings-requirements "#vpc-settings-requirements").
- For this procedure, we recommend that you sign in to the AWS Management Console and open the
  Amazon VPC console using credentials for an IAM administrator in your AWS account.
  If you can't do this, check with your AWS account administrator.
- Some organizations might not allow you to create subnets on your own. If you
  cannot create a subnet, check with your AWS account administrator or network
  administrator.

###### To create a subnet

1. If the Amazon VPC console isn't already open, sign in to the AWS Management Console and open the
   Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. In the navigation bar, if the AWS Region isn't the same as the Region for the
   environment, choose the correct Region.
3. Choose **Subnets** in the navigation pane, if the
   **Subnets** page isn't already displayed.
4. Choose **Create Subnet**.
5. In the **Create Subnet** dialog box, for **Name
   tag**, enter a name for the subnet.
6. For **VPC**, choose the VPC to associate the subnet with.
7. For **Availability Zone**, choose the Availability Zone within
   the AWS Region for the subnet to use, or choose **No Preference**
   to let AWS choose an Availability Zone for you.
8. For **IPv4 CIDR block**, enter the range of IP addresses for the
   subnet to use, in CIDR format. This range of IP addresses must be a subset of IP
   addresses in the VPC.

For information about CIDR blocks, see [VPC and subnet sizing](../../../vpc/latest/userguide/subnet-sizing.md "../../../vpc/latest/userguide/subnet-sizing.md") in
the _Amazon VPC User Guide_. See also [3.1. Basic Concept and Prefix
Notation](http://tools.ietf.org/html/rfc4632#section-3.1 "http://tools.ietf.org/html/rfc4632#section-3.1") in RFC 4632 or [IPv4 CIDR blocks](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#IPv4_CIDR_blocks "http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#IPv4_CIDR_blocks") in Wikipedia.

After you create the subnet, [configure it as
either a public or private subnet](#public-private-subnet "#public-private-subnet").

## Configuring a subnet as public or private

After you create a subnet, you can make it public or private by specifying how it
communicates with the internet.

A public subnet has a public IP address and an internet gateway (IGW) is attached to it
that allows communication between the instance for the subnet and the internet and other
AWS services.

An instance in a private subnet has a private IP address and a network address
translation (NAT) gateway is used to send traffic back and forth between the instance for
the subnet and the internet and other AWS services. The NAT gateway must be hosted in a
public subnet.

Public subnets

###### Note

Even if the instance for your environment is launched in a private subnet,
your VPC must feature at least one public subnet. This is because the NAT
gateway that forwards traffic to and from the instance must be hosted in a
public subnet.

Configuring a subnet as public involves attaching an internet gateway (IGW) to
it, configuring a route table to specify a route to that IGW, and defining
settings in a security group to control inbound and outbound traffic.

Guidance on carrying out these tasks is provided in [Create a VPC plus other VPC resources](#vpc-settings-create-vpc "#vpc-settings-create-vpc").

###### Important

If your development environment is [using SSM to
access an EC2 instance](ec2-ssm.md "ec2-ssm.md"), ensure that the instance is assigned a public
IP address by the public subnet it's launched into. To do so, you must enable
the automatic assignment of a public IP address option for the public subnet,
and set it to `Yes`. You can enable this on the public subnet before
creating an AWS Cloud9 environment within the subnet settings page. For the steps
involved in modifying auto-assign IP settings in a public subnet, see [Modify the public IPv4 addressing attribute for your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md") in the
_Amazon VPC User Guide_. For more information about
configuring a public and private subnet, see Configuring a subnet as public or private.

Private subnets
If you're creating a no-ingress instance that's accessed through Systems Manager, you can
launch it into a private subnet. A private subnet doesn't have a public IP
address. So you need a NAT gateway to map the private IP address to a public
address for requests, and you also need to map the public IP address back to the
private address for the response.

###### Warning

You're charged for creating and using a NAT gateway in your account. NAT
gateway hourly usage and data processing rates apply. Amazon EC2 charges for data
transfer also apply. For more information, see [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

Before creating and configuring the NAT gateway, you must do the
following:

- Create a public VPC subnet to host the NAT gateway.
- Provision an [Elastic IP address](../../../vpc/latest/userguide/vpc-eips.md#WorkWithEIPs "../../../vpc/latest/userguide/vpc-eips.md#WorkWithEIPs") that can be assigned to the NAT gateway.
- For the private subnet, clear the **Enable auto-assign public
  IPv4 address** check box so that the instance launched into it
  is assigned a private IP address. For more information, see [IP Addressing in your
  VPC](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in the _Amazon VPC User Guide_.

For the steps in this task, see [Working with
NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-working-with "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-working-with") in the _Amazon VPC User Guide_.

###### Important

Currently, if your environment’s EC2 instance is launched into a private
subnet, you can't use [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials") to allow the EC2 environment to access an
AWS service on behalf of an AWS entity such as an IAM user.
