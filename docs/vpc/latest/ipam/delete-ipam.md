

# Delete an IPAM
<a name="delete-ipam"></a>

You may want to delete an IPAM if it is no longer needed, if you need to restructure your IP address management, or if you want to start fresh with a new IPAM configuration. Deleting an IPAM can help simplify your IP address management and align with changing business or operational requirements.

Follow the steps in this section to delete an IPAM. For information on increasing the default number of IPAMs you can have rather than deleting an existing IPAM, see [Quotas for your IPAM](quotas-ipam.md).

**Note**  
Deleting an IPAM removes all monitored data associated with the IPAM including the historical data for CIDRs.

------
#### [ AWS Management Console ]

**To delete an IPAM**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **IPAMs**.

1. In the content pane, select your IPAM.

1. Choose **Actions** > **Delete IPAM**.

1. Do one of the following:
   + Choose **Cascade delete** to delete the IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes. You cannot delete the IPAM with this option if there is a pool in your public scope. If you use this option, IPAM does the following:
     + Deallocates any CIDRs allocated to VPC resources (such as VPCs) in pools in private scopes.
**Note**  
No VPC resources are deleted as a result of enabling this option. The CIDR associated with the resource will no longer be allocated from an IPAM pool, but the CIDR itself will remain unchanged.
     + Deprovisions all IPv4 CIDRs provisioned to IPAM pools in private scopes.
     + Deletes all IPAM pools in private scopes.
     + Deletes all non-default private scopes in the IPAM.
     + Deletes the default public and private scopes and the IPAM.
   + If you don't choose the **Cascade delete** checkbox, before you can delete an IPAM, you must do the following:
     + Release allocations within the IPAM pools. For more information, see [Release an allocation](release-alloc-ipam.md).
     + Deprovision CIDRs provisioned to pools within the IPAM. For more information, see [Deprovision CIDRs from a pool](depro-pool-cidr-ipam.md).
     + Delete any additional non-default scopes. For more information, see [Delete a scope](delete-scope-ipam.md).
     + Delete your IPAM pools. For more information, see [Delete a pool](delete-pool-ipam.md).

1. Enter **delete** and then choose **Delete**.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

Use the following AWS CLI commands to delete an IPAM:

1. View current IPAMs: [describe-ipams](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipams.html)

1. Delete an IPAM: [delete-ipam](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-ipam.html)

1. View your updated IPAMs: [describe-ipams](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipams.html)

------

To create a new IPAM, see [Create an IPAM](create-ipam.md).