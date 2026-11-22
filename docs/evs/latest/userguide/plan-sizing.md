

# Size your environment

The number of hosts in your Amazon Elastic VMware Service environment sets the capacity for the VMware Cloud Foundation (VCF) management appliances and your workloads. It also sets the quotas, the Amazon Elastic Compute Cloud (Amazon EC2) capacity, the IP addresses, and the VCF subscription cores that you need. Size the environment before you request any of them.

## Minimum and maximum hosts
<a name="plan-sizing-hosts"></a>

The minimum number of hosts depends on how VCF is deployed and on the VCF topology that you choose.


| VCF version | Minimum hosts | 
| --- | --- | 
| 9.x | The number that your VCF topology needs. Amazon EVS doesn’t set a minimum of its own. You add the hosts after you create the environment. For the minimum host counts, including the vSAN requirements, see the [Broadcom documentation for VCF 9.0](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0.html). | 
| 5.2.x | Four. Amazon EVS creates four hosts when it creates the environment, because VCF requires them for vSAN quorum. You can add hosts after deployment. | 

Broadcom recommends at least four hosts for production workloads. For hosts with local storage, four hosts keep vSAN quorum and keep the cluster available during maintenance and host failures. For more information, see [Plan for resilience and recovery](plan-resilience.md).

If your environment has fewer hosts than your VCF topology needs, the host count status check fails. For more information, see [Troubleshoot environment status checks](troubleshoot-status-checks.md).

The maximum number of hosts in an environment is limited by the **Host count per EVS environment** quota. For the default value and how to raise it, see [Service quotas for Amazon EVS](service-quotas-evs.md).

## Management appliance sizes
<a name="plan-sizing-appliances"></a>

The VCF management appliances run on the hosts of the management domain, so they use part of its compute and storage capacity. The appliances include vCenter, NSX Manager, NSX Edge nodes, and SDDC Manager or VCF Operations. Size the management domain for the appliances and for the workloads that share its hosts.

For the appliance sizes and the resources that each size needs, see the Broadcom documentation for your VCF version. For VCF 5.2.x, see the [Planning and Preparation Workbook](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/planning-and-preparation-workbook-5-2.html) in the Broadcom documentation.

For VCF 9.x, see the [Planning and Preparation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/planning-and-preparation.html) page in the Broadcom documentation.

If you use diskless hosts, which need VCF 9.x, the management appliances run on your external principal datastore. For datastore sizing, see [External storage options for diskless hosts](external-storage-diskless.md).

## Quotas to raise before you start
<a name="plan-sizing-quotas"></a>

Amazon EVS and Amazon EC2 quotas apply per AWS Region. Check these quotas before you create the environment and before you add hosts, because a request that exceeds a quota fails.


| Quota | What it must cover | 
| --- | --- | 
| Amazon EVS: **Host count per EVS environment**  | Every host that you plan to create in one environment, including temporary hosts that you add when you replace a host. Environment creation fails if this quota is lower than your VCF topology needs. | 
| Amazon EVS: **Environment count per AWS account**  | Every environment that you plan to create in the Region. | 
| Amazon EC2: **Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances**  | The vCPUs of all hosts, plus the vCPUs of every other Standard instance that runs in the Region. For the vCPUs of each instance type, see [Supported VCF versions by instance type](versions-provided.md#current-vcf-versions). | 
| Amazon EC2: **Dedicated Hosts** for your instance family | The number of Dedicated Hosts that you plan to use, if you use Dedicated Hosts. | 
| Amazon VPC IPAM: **Amazon-provided contiguous public IPv4 CIDR block netmask length**  | The default value of /28 is enough if you plan to use HCX internet connectivity. You don’t need to request an increase. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md). | 

For the default values and the steps to request an increase, see [Service quotas for Amazon EVS](service-quotas-evs.md). A quota increase can take time to approve, so request it early.

The number of hosts also decides other values that you plan next.

 **IP addresses**   
Each host uses addresses in the VLAN subnets. You can’t add VLAN subnets or change their CIDR blocks after you create the environment. For more information, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).

 **EC2 capacity**   
For more information, see [Reserve capacity for hosts](plan-capacity.md).

 **VCF subscription cores**   
For more information, see [VCF licensing](vcf-license-mgmt.md).

Next, reserve capacity for your hosts. See [Reserve capacity for hosts](plan-capacity.md).