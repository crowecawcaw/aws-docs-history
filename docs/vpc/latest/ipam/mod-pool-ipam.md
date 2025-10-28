# Edit an IPAM pool

You may want to edit a pool to do one of the following:

- Change the allocation rules for the pool. For more information about allocation rules, see
  [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md").
- Modify the pool's name, description, or other metadata to improve organization and visibility
  within IPAM.
- Change pool options like auto-import discovered resources to optimize IPAM's automated IP address management.
  Follow the steps in this section to edit an IPAM pool.

AWS Management Console

###### To edit a pool

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, the default private scope is selected. If you don’t want to use the default
   private scope, from the dropdown menu at the top of the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md")
4. In the content pane, choose the pool whose CIDR you want to
   edit.
5. Choose **Actions** > **Edit**.
6. Make any changes you need to the pools. For information about pool
   configuration options, see [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md").
7. Choose **Update**.

Command line
Use the following AWS CLI commands to edit a pool:

1. Get an IPAM pool ID: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")
2. Modify the pool: [modify-ipam-pool](../../../cli/latest/reference/ec2/modify-ipam-pool.md "../../../cli/latest/reference/ec2/modify-ipam-pool.md")
