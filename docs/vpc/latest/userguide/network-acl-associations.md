

# Manage network ACL associations for your VPC
<a name="network-acl-associations"></a>

Each subnet is associated with one network ACL. When you first create a subnet, it is associated with the default network ACL for the VPC. You can create a custom network ACL and associate it with one or more subnets, replacing the previous network ACL association.

**Topics**
+ [Describe your network ACL associations](#describe-network-acl-association)
+ [Change the subnets associated with a network ACL](#DisassociateNetworkACL)
+ [Change the network ACL associated with a subnet](#ChangeNetworkACL)

## Describe your network ACL associations
<a name="describe-network-acl-association"></a>

You can describe the network ACL that's associated with a subnet and you can also describe which subnets are associated with a network ACL.

**To describe the network ACL associated with a subnet using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**.

1. Select the subnet.

1. Select the **Network ACL** tab.

**To describe the network ACL associated with a subnet using the AWS CLI**  
Use the following [describe-network-acls](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-network-acls.html) command to list the network ACL associated with the specified subnet.

```
aws ec2 describe-network-acls --filters Name=association.subnet-id,Values={{subnet-0d2d1b81e0bc9c6d4}} --query NetworkAcls[*].NetworkAclId
```

The following is example output.

```
[
    "acl-03701d1f82d8c3fd6"
]
```

**To describe the subnets associated with a network ACL using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Network ACLs**.

1. Select the network ACL.

1. Select the **Subnet associations** tab.

**To describe the subnets associated with a network ACL using the AWS CLI**  
Use the following [describe-network-acls](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-network-acls.html) command to list the subnets associated with the specified network ACL.

```
aws ec2 describe-network-acls --network-acl-ids {{acl-060415a18fcc9afde}} --query NetworkAcls[*].Associations[].SubnetId
```

The following is example output.

```
[
    "subnet-0d2d1b81e0bc9c6d4",
    "subnet-0e990c67809773b19",
    "subnet-0eb17d85f5dfd33b1",
    "subnet-0e01d500780bb7468"
]
```

## Change the subnets associated with a network ACL
<a name="DisassociateNetworkACL"></a>

You can disassociate a custom network ACL from a subnet. After you disassociate a subnet from a custom network ACL, we automatically associate it with the default network ACL for the VPC. The changes take effect after a short period of time.

**To change the subnets associated with a network ACL**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Network ACLs**.

1. Select the network ACL.

1. Choose **Actions**, **Edit subnet associations**.

1. Remove the subnet from **Selected subnets**.

1. Choose **Save changes**.

## Change the network ACL associated with a subnet
<a name="ChangeNetworkACL"></a>

You can change the network ACL that's associated with a subnet. For example, when you create a subnet, it is initially associated with the default network ACL for the VPC. If you create a custom network ACL, you apply the network ACL rules by associating the network ACL with one or more subnets.

After you change the network ACL for a subnet, the changes take effect after a short period of time.

**To change the network ACL associated with a subnet**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**.

1. Select the subnet.

1. Choose **Actions**, **Edit network ACL association**.

1. For **Network ACL ID**, select the network ACL to associate with the subnet, and review the inbound and outbound rules for the selected network ACL.

1. Choose **Save**.

**To replace a network ACL association using the command line**
+ [replace-network-acl-association](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-network-acl-association.html) (AWS CLI)
+ [Set-EC2NetworkAclAssociation](https://docs.aws.amazon.com/powershell/latest/reference/items/Set-EC2NetworkAclAssociation.html) (AWS Tools for Windows PowerShell)