

# Manage hosts

Because Amazon Elastic VMware Service is a self-managed service, you’re responsible for monitoring host health and for replacing a host when it fails. You add, replace, and delete hosts with the Amazon EVS console or the AWS CLI, and you bring them into or out of the cluster with VMware Cloud Foundation (VCF) tools. The VCF steps differ by VCF version, so each version has its own pages.

For the steps that apply to every version, see [Add a host](host-add-overview.md) and [Delete a host](host-delete-overview.md).

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API.

The following table shows the page for each host task by deployment mode.


<table>
<thead>
  <tr><th>Task</th><th>VCF 9.x (Self-deployed)</th><th>VCF 5.2.x (EVS-deployed)</th></tr>
</thead>
<tbody>
  <tr><td>Prepare for EC2 maintenance and retirement events</td><td colspan="2"> <a href="evs-host-maintenance.md">Host maintenance and retirement events</a> </td></tr>
  <tr><td>Add a host</td><td> <a href="host-add.md">Add a host (VCF 9.x)</a> </td><td> <a href="evs-env-create-host.md">Add a host (VCF 5.x)</a> </td></tr>
  <tr><td>Replace a failed or retiring host</td><td> <a href="host-replace.md">Replace a failed host (Self-deployed)</a> </td><td> <a href="host-replace-evs-deployed.md">Replace a host (EVS-deployed)</a> </td></tr>
  <tr><td>Delete a host</td><td> <a href="host-delete.md">Delete a host (VCF 9.x)</a> </td><td> <a href="evs-env-delete-host.md">Delete a host (VCF 5.x)</a> </td></tr>
  <tr><td>Add or replace a diskless host</td><td> <a href="host-add.md">Add a host (VCF 9.x)</a> and <a href="host-replace.md">Replace a failed host (Self-deployed)</a> </td><td>Not available</td></tr>
</tbody>
</table>


For the VCF versions and instance types that each mode supports, see [Supported VCF versions and instance types](versions-provided.md).

Before you add or replace hosts, check your **Host count per EVS environment** quota. Host creation fails if this quota is lower than the number of hosts that you want in the environment. For more information, see [Service quotas for Amazon EVS](service-quotas-evs.md). If a host task fails, see [Troubleshoot hosts](troubleshoot-hosts.md).

**Topics**
+ [Host maintenance and retirement events](evs-host-maintenance.md)
+ [Add a host](host-add-overview.md)
+ [Add a host (VCF 9.x)](host-add.md)
+ [Replace a failed host (Self-deployed)](host-replace.md)
+ [Delete a host](host-delete-overview.md)
+ [Delete a host (VCF 9.x)](host-delete.md)
+ [Add a host (VCF 5.x)](evs-env-create-host.md)
+ [Replace a host (EVS-deployed)](host-replace-evs-deployed.md)
+ [Delete a host (VCF 5.x)](evs-env-delete-host.md)