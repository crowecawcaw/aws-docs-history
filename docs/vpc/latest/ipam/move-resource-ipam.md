

# Move VPC CIDRs between scopes
<a name="move-resource-ipam"></a>

Moving CIDRs between scopes allows you to optimize IP address allocation, organize by Region, separate concerns, enforce compliance, and adapt to infrastructure changes. This flexibility helps manage your IP address space efficiently as your workloads evolve.

Follow the steps in this section to move a VPC CIDR from one scope to another.

**Important**  
You can only move VPC CIDRs. When you move a VPC CIDR, the VPC's subnet CIDRs are moved automatically as well.
You can only move VPC CIDRs from one private scope to another. You cannot move VPC CIDRs out of a public scope to a private scope or from a private scope to a public scope.
The same AWS account must own both scopes.
If a VPC CIDR is currently allocated from a pool in a private scope, the move request succeeds, but the VPC CIDR will not be moved until you release the VPC CIDR allocation from the current pool. For information on releasing an allocation, see [Release an allocation](https://docs.aws.amazon.com/vpc/latest/ipam/release-alloc-ipam.html).

------
#### [ AWS Management Console ]

**To move a CIDR allocated to a VPC**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Resources**.

1. From the dropdown menu at the top of the content pane, choose the scope you want to use.

1. In the content pane, choose a VPC and view the details of the VPC.

1. Under **VPC CIDRs**, select one of the CIDRs allocated to the resource and choose **Actions** > **Move CIDR to different scope**.

1. Select the scope you want to move the VPC CIDR to.

1. Choose **Move CIDR to different scope**.

------
#### [ Command line ]

Use the following AWS CLI commands to move a VPC CIDR:

1. Get a VPC CIDR in current scope: [get-ipam-resource-cidrs](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-resource-cidrs.html)

1. Move a VPC CIDR: [modify-ipam-resource-cidr](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-ipam-resource-cidr.html)

1. Get a VPC CIDR in the other scope: [get-ipam-resource-cidrs](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-resource-cidrs.html)

------