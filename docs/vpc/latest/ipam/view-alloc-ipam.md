

# View IPAM pool allocations
<a name="view-alloc-ipam"></a>

There are two ways to view IPAM pool allocations:
+ **By pool** – Use [get-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-allocations.html) to view all allocations in a specific pool that you own or that has been shared with you. This includes allocations that are not directly owned by you. 
+ **Across all pools** – Use [describe-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pool-allocations.html) to view only allocations that you directly own. This command works across all pools without requiring a pool ID. 

To find pools that you own or that are shared with you, use [describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html).

------
#### [ AWS Management Console ]

**To view IPAM pool allocations**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Pools**.

1. By default, the default private scope is selected. If you don't want to use the default private scope, from the scope dropdown menu in the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md).

1. In the content pane, choose the pool.

1. Choose the **Allocations** tab to view all allocations in the pool.

**Note**  
The console shows all allocations in the selected pool, including allocations owned by other accounts. To view only allocations that you directly own across all pools, use the command line.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

**View allocations in a specific pool**  
Use [get-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-allocations.html) to view all allocations in a specific pool. This includes allocations owned by other accounts if the pool is shared with you.

1. Get the ID of the IPAM pool: [describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html).

1. View allocations in the pool: [get-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-allocations.html).

   ```
   aws ec2 get-ipam-pool-allocations --ipam-pool-id {{ipam-pool-0533048da7eba92f6}}
   ```

1. (Optional) View a specific allocation in the pool:

   ```
   aws ec2 get-ipam-pool-allocations --ipam-pool-id {{ipam-pool-0533048da7eba92f6}} --ipam-pool-allocation-id {{ipam-pool-alloc-0e6186d73999e1f12}}
   ```

**Note**  
This command shows all allocations in the pool, including allocations owned by other accounts.

**View your allocations across all pools**  
Use [describe-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pool-allocations.html) to view only allocations that you directly own across all pools.

1. View all of your allocations:

   ```
   aws ec2 describe-ipam-pool-allocations
   ```

1. (Optional) View specific allocations by ID:

   ```
   aws ec2 describe-ipam-pool-allocations --ipam-pool-allocation-ids {{ipam-pool-alloc-0e6186d73999e1f12}}
   ```

1. (Optional) Filter by tag:

   ```
   aws ec2 describe-ipam-pool-allocations --filters Name=tag:{{Environment}},Values={{Production}}
   ```

**Note**  
This command returns only allocations that you directly own.

------

To allocate a new CIDR, see [Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md). To release an allocation, see [Release an allocation](release-alloc-ipam.md).