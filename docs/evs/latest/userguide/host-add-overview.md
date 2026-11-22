

# Add a host

1. In VMware Cloud Foundation (VCF), you add the host to a cluster with VCF tools. The steps depend on the VCF version that the cluster runs. == Before you begin Before you create the host, make sure that the following are true.
   + A DNS forward lookup zone contains an A record for the host, and a reverse lookup zone contains a PTR record for the host. For more information, see [DNS records for hosts and appliances](evs-deployment-prereq-checklist.md#evs-prereq-dns-records).
   + Your **Host count per EVS environment** quota is at least the number of hosts that the environment will have after you add hosts. Host creation fails if the quota is lower. For more information, see [Service quotas for Amazon EVS](service-quotas-evs.md).
   + You have an Amazon EC2 key pair. Amazon EVS requires the key pair name when you create a host.
   + You know the instance type and the ESX version that the target cluster uses. For the versions that are available to your account, run `aws evs get-versions` or see [Supported VCF versions and instance types](versions-provided.md). == Choose the procedure Each procedure covers both parts, including the console and AWS CLI steps for creating the host.


|  |  | 
| --- |--- |
| VCF version of the cluster | Procedure | 
| VCF 9.x |  [Add a host (VCF 9.x)](host-add.md). Use this procedure also to add a diskless host. | 
| VCF 5.x |  [Add a host (VCF 5.x)](evs-env-create-host.md)  | 

If a host stays in the `CREATING` state or moves to `CREATE_FAILED`, check its DNS records first. For more information, see [Troubleshoot hosts](troubleshoot-hosts.md).