

# Choose storage

Principal storage is the first shared storage that VMware Cloud Foundation (VCF) uses when it creates a domain or cluster. It holds the VCF management appliances. Supplemental storage is storage that you add after VCF is deployed. The storage model of your hosts decides which principal storage you can use, so choose storage together with the instance type.

## Storage options
<a name="plan-storage-options"></a>

The following table compares the storage options for Amazon Elastic VMware Service hosts.


| Option | Principal storage | Instance types | VCF version | Next step | 
| --- | --- | --- | --- | --- | 
| vSAN Express Storage Architecture (ESA) on local NVMe | vSAN ESA on the NVMe instance store volumes of the hosts. You configure vSAN ESA when you install VCF. | Hosts with local NVMe | All | For the support conditions, see [vSAN ESA](vcf-feature-support.md#feat-vsan-esa). For the vSAN settings, see [Step 4b (local storage): Run VCF bringup](sd-install-bringup.md). | 
| vSAN ESA with supplemental external storage | vSAN ESA, as in the first row. You add Amazon FSx for NetApp ONTAP datastores (NFS, iSCSI, or NVMe/TCP) after VCF is deployed. | Hosts with local NVMe | All |  [Connect external storage](external-storage-connect.md)  | 
| External principal storage | An NFS v3 datastore on external storage that you create before you install VCF, such as Amazon FSx for OpenZFS or Amazon FSx for NetApp ONTAP. You can add supplemental storage after VCF is deployed. | Diskless hosts | 9.x |  [External storage options for diskless hosts](external-storage-diskless.md)  | 

For the vSAN storage architectures that Amazon EVS supports, see the [vSAN ESA](vcf-feature-support.md#feat-vsan-esa) and [vSAN OSA](vcf-feature-support.md#feat-vsan-osa) rows in [VCF feature support on Amazon EVS](vcf-feature-support.md).

## Hosts with local NVMe
<a name="plan-storage-local"></a>

vSAN ESA uses the NVMe instance store volumes of the hosts. Instance store volumes are ephemeral. Data on them doesn’t persist if the underlying EC2 instance is stopped or terminated.

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API.

For more information, see [Host maintenance and retirement events](evs-host-maintenance.md).

vSAN capacity grows when you add hosts. To add capacity without adding hosts, add supplemental datastores on Amazon FSx for NetApp ONTAP. For more information, see [Connect external storage](external-storage-connect.md).

## Diskless hosts
<a name="plan-storage-diskless"></a>

This section applies to Self-deployed environments that run VCF 9.x.

Diskless hosts have no local disks for data, so vSAN isn’t available on them. Every datastore, including the one that holds the VCF management appliances, must be on external storage that all hosts in the cluster can reach. You create and manage that storage, and Amazon EVS doesn’t create, configure, or monitor it.

For a comparison of Amazon FSx for NetApp ONTAP, Amazon FSx for OpenZFS, and Everpure Cloud Dedicated, and the requirements that apply to all of them, see [External storage options for diskless hosts](external-storage-diskless.md). For the deployment steps, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

**Topics**