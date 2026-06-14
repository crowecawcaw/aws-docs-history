# View IPAM pool allocations

There are two ways to view IPAM pool allocations:

- **By pool** – Use [get-ipam-pool-allocations](../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md "../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md") to view all allocations in a specific pool
  that you own or that has been shared with you. This includes allocations that are not
  directly owned by you.
- **Across all pools** – Use [describe-ipam-pool-allocations](../../../cli/latest/reference/ec2/describe-ipam-pool-allocations.md "../../../cli/latest/reference/ec2/describe-ipam-pool-allocations.md") to view only allocations that you
  directly own. This command works across all pools without requiring a pool ID.
  To find pools that you own or that are shared with you, use [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md").

AWS Management Console

###### To view IPAM pool allocations

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, the default private scope is selected. If you don't want
   to use the default private scope, from the scope dropdown menu in
   the content pane, choose the scope you want to use. For more information
   about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. In the content pane, choose the pool.
5. Choose the **Allocations** tab to view all
   allocations in the pool.

###### Note

The console shows all allocations in the selected pool, including
allocations owned by other accounts. To view only allocations that you
directly own across all pools, use the command line.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

###### View allocations in a specific pool

Use [get-ipam-pool-allocations](../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md "../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md") to view all allocations in a specific
pool. This includes allocations owned by other accounts if the pool is shared
with you.

1. Get the ID of the IPAM pool: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md").
2. View allocations in the pool: [get-ipam-pool-allocations](../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md "../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md").

```
aws ec2 get-ipam-pool-allocations --ipam-pool-id `ipam-pool-0533048da7eba92f6`
```

3. (Optional) View a specific allocation in the pool:

```
aws ec2 get-ipam-pool-allocations --ipam-pool-id `ipam-pool-0533048da7eba92f6` --ipam-pool-allocation-id `ipam-pool-alloc-0e6186d73999e1f12`
```

###### Note

This command shows all allocations in the pool, including allocations
owned by other accounts.

###### View your allocations across all pools

Use [describe-ipam-pool-allocations](../../../cli/latest/reference/ec2/describe-ipam-pool-allocations.md "../../../cli/latest/reference/ec2/describe-ipam-pool-allocations.md") to view only allocations that
you directly own across all pools.

1. View all of your allocations:

```
aws ec2 describe-ipam-pool-allocations
```

2. (Optional) View specific allocations by ID:

```
aws ec2 describe-ipam-pool-allocations --ipam-pool-allocation-ids `ipam-pool-alloc-0e6186d73999e1f12`
```

3. (Optional) Filter by tag:

```
aws ec2 describe-ipam-pool-allocations --filters Name=tag:`Environment`,Values=`Production`
```

###### Note

This command returns only allocations that you directly own.

To allocate a new CIDR, see [Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md "allocate-cidrs-ipam.md"). To release an allocation, see [Release an allocation](release-alloc-ipam.md "release-alloc-ipam.md").
