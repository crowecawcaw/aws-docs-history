# Delete a pool

An IPAM pool in AWS represents a defined range of IP addresses that can be allocated and managed within a specific AWS environment or organization. Pools are used to organize IP address space, enable automated IP address management, and enforce IP address governance policies across your cloud infrastructure.

You may want to delete an IPAM pool to remove unused or unnecessary IP address space and
reclaim it for other purposes. You cannot delete an IP address pool if there are allocations
in it. You must first release the allocations and [Deprovision CIDRs from a pool](depro-pool-cidr-ipam.md "depro-pool-cidr-ipam.md") before you can delete the pool.

Follow the steps in this section to delete an IPAM pool.

AWS Management Console

###### To delete a pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. From the dropdown menu at the top of the content pane, choose the
   scope that you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. In the content pane, choose the pool whose CIDR you want to delete.
5. Choose **Actions** > **Delete
   pool**.
6. Enter `delete` and then choose
   **Delete**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to delete a pool:

1. View pools and get an IPAM pool ID: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")
2. Delete a pool: [delete-ipam-pool](../../../cli/latest/reference/ec2/delete-ipam-pool.md "../../../cli/latest/reference/ec2/delete-ipam-pool.md")
3. View your pools: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")

To create a new pool, see [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md").
