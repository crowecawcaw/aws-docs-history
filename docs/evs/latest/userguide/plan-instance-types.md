

# Choose instance types

Each Amazon Elastic VMware Service host is an Amazon Elastic Compute Cloud (Amazon EC2) bare metal instance. The instance type sets the storage, vCPUs, and memory of the host. Choose the storage model first, and then the size. The storage model decides your deployment path and which VMware Cloud Foundation (VCF) versions you can use.

For the instance types, their storage model, vCPUs and memory, and the VCF versions and ESX builds that each supports, see [Supported VCF versions by instance type](versions-provided.md#current-vcf-versions).

## Step 1. Choose a storage model
<a name="plan-instance-types-storage"></a>

Amazon EVS offers two storage models for hosts. The model that you choose decides where your VCF management appliances and workload virtual machines are stored.


| Storage model | Principal storage | VCF version | Choose it when | 
| --- | --- | --- | --- | 
| Local NVMe | vSAN ESA on the NVMe instance store volumes of the hosts. You can add external storage as supplemental storage. | All | You want storage that grows with the number of hosts, and that VCF configures during bringup. | 
| Diskless | External storage that you provide, such as an NFS datastore. The hosts have no local disks for data. | 9.x | You want to keep all datastores on external storage that you manage, and size storage separately from compute. | 

Diskless hosts are available only in Self-deployed mode. For the VCF versions and instance types that each mode supports, see [Supported VCF versions and instance types](versions-provided.md).

For the full comparison of storage options, see [Choose storage](plan-storage.md).

## Step 2. Choose a size
<a name="plan-instance-types-size"></a>

Within a storage model, the instance types differ in vCPUs, memory and, for local NVMe, instance store capacity. Choose the size from the resources that your workloads need, and from the number of hosts that this size gives you.
+ For the vCPUs and memory of each instance type, see [Supported VCF versions by instance type](versions-provided.md#current-vcf-versions).
+ For network bandwidth and other hardware details, see [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types).
+ For the number of hosts and the quotas to raise, see [Size your environment](plan-sizing.md).
+ For how instance size affects the physical cores that your VCF subscription must cover, see [VCF licensing](vcf-license-mgmt.md).

The `get-versions` command returns the instance types for one AWS Region. Run it for the Region where you plan to deploy before you decide. For more information, see [Check which versions are available to you](plan-versions.md#plan-versions-check).

## Step 3. Plan for one instance type per cluster
<a name="plan-instance-types-mixing"></a>

All hosts in a VCF cluster must use the same instance type. Plan the instance type for each cluster before you add hosts.

When you install VCF, you set the Enhanced vMotion Compatibility (EVC) mode of the cluster to match the instance type of its hosts. For the EVC values, see [Management cluster settings](vcf-installer-settings.md#installer-settings-cluster). Diskless hosts need VCF 9.x, and you set their EVC mode after deployment. For more information, see [Verify the result](deploy-diskless-spec.md#getting-started-diskless-verify).

Next, decide how many hosts you need. See [Size your environment](plan-sizing.md).