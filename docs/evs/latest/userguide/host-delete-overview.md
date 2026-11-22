

# Delete a host

1. In Amazon EVS, you delete the host with the Amazon EVS console or the AWS CLI. WARNING: Remove the host in VCF before you delete it in Amazon EVS. If you delete a host without removing it first, stale data stays in vCenter Server and SDDC Manager. Before you delete a host, make sure that the cluster keeps enough hosts for your VCF topology.

   <a name="host-delete-overview-choose"></a>== Choose the procedure Each procedure covers both parts, including the console and AWS CLI steps for deleting the host.


|  |  | 
| --- |--- |
| VCF version of the cluster | Procedure | 
| VCF 9.x |  [Delete a host (VCF 9.x)](host-delete.md)  | 
| VCF 5.x |  [Delete a host (VCF 5.x)](evs-env-delete-host.md)  | 

To delete every host and the environment, see [Clean up a Self-deployed environment](self-deployed-cleanup.md) for Self-deployed environments, or [Delete an EVS-deployed environment](getting-started-cleanup-env-hosts.md) for EVS-deployed environments.