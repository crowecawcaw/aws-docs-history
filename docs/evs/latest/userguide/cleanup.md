

# Clean up network resources

After you delete your Amazon Elastic VMware Service environment, delete the network resources that you created for it, so that they don’t continue to incur costs. You delete them in reverse order of creation, using the Amazon VPC console or the AWS CLI as described in the linked Amazon VPC topics.

**Warning**  
You can’t recover these resources after you delete them. Make sure that no other workload uses the VPC, the route server, the network ACL, the gateways, or the subnets before you delete them.

## Before you begin
<a name="cleanup-prereqs"></a>

Make sure that you’ve deleted the Amazon EVS environment. For instructions, see the page for your deployment mode.
+ For a Self-deployed environment, see [Clean up a Self-deployed environment](self-deployed-cleanup.md).
+ For an EVS-deployed environment, see [Delete an EVS-deployed environment](getting-started-cleanup-env-hosts.md).

Environment deletion also deletes the Amazon EVS VLAN subnets and the AWS Secrets Manager secrets that Amazon EVS created. Amazon EVS VLAN subnets can be deleted only when the environment is deleted. AWS resources that you created yourself are not deleted.

## Delete the network resources
<a name="cleanup-steps"></a>

To delete the remaining resources, do the following.

1.  (HCX internet connectivity only) Delete the IPAM resources in this order.

   1. Release the Elastic IP address allocations from the public IPAM pool. For instructions, see [Release an allocation](https://docs.aws.amazon.com/vpc/latest/ipam/release-alloc-ipam.html).

   1. Disassociate the public CIDR block from your VPC. Use the [disassociate-vpc-cidr-block](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-vpc-cidr-block.html) command with the association ID of the public CIDR block.

   1. Deprovision the public IPv4 CIDR block from the IPAM pool. For instructions, see [Deprovision CIDRs from a pool](https://docs.aws.amazon.com/vpc/latest/ipam/depro-pool-cidr-ipam.html).

   1. Delete the public IPAM pool. For instructions, see [Delete a pool](https://docs.aws.amazon.com/vpc/latest/ipam/delete-pool-ipam.html).

   1. Delete the IPAM. For instructions, see [Delete an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/delete-ipam.html).

1. Terminate the instances and delete the file systems that you created in the VPC subnets, such as the instance from [Launch an instance to reach the VPC](network-dhcp-dns-ntp.md#network-access-instance) and your external storage. You can’t delete a subnet while network interfaces exist in it.

1. If you attached the VPC to a transit gateway, delete the VPC attachment. For instructions, see [Amazon VPC attachments in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html).

1.  Delete the Amazon VPC Route Server components. For instructions, see [Route server cleanup](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-cleanup.html) in the * Amazon VPC User Guide*.

1.  Delete the custom network ACL. For instructions, see [Delete a network ACL for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/delete-network-acl.html).

1. Delete the NAT gateway, wait until its state is `deleted`, and then release its Elastic IP address. A NAT gateway and an allocated Elastic IP address continue to incur costs until you delete or release them. For instructions, see [Work with NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html) and [Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html).

1.  Disassociate and delete the subnet route tables that you created. For instructions, see [Subnet route tables](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-route-tables.html).

1. If you use Route 53 for DNS, delete the inbound resolver endpoints in the service access subnet, and then delete the private hosted zones. You can’t delete the service access subnet while the endpoints exist.

1. Detach the internet gateway from the VPC, and then delete it. For instructions, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html).

1.  Delete the VPC subnets, including the service access subnet. For instructions, see [Delete a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-deleting.html).

1.  Delete the VPC, and then delete the DHCP option set that you created for it. For instructions, see [Delete your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/delete-vpc.html) and [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html).

1. If you have Amazon EC2 Capacity Reservations that you no longer need, cancel them. For instructions, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html) in the *Amazon EC2 User Guide*.

You have deleted the network resources for your Amazon EVS environment. To confirm, open the Amazon VPC console and check that the VPC no longer appears under **Your VPCs**.