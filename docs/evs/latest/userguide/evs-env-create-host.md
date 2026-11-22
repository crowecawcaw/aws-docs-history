

# Add a host (VCF 5.x)

This page applies to EVS-deployed environments (VCF 5.2.x). For Self-deployed environments that run VCF 9.x, see [Manage hosts](host-management.md).

After your Amazon Elastic VMware Service environment is deployed, you can add hosts to increase capacity and workload resiliency. You create the host with the Amazon EVS console or the AWS CLI, and then you commission it and add it to the cluster in SDDC Manager.

For host count requirements for your VMware Cloud Foundation (VCF) deployment topology, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2.html).

**Important**  
If you create a host with an ESX version that’s newer than the ESX version of your vSphere cluster image, you can’t downgrade the host. You must delete the host and create it again with the correct ESX version.

## Before you begin
<a name="evs-env-create-host-prereqs"></a>

Before you begin, make sure that the following are true.
+ A DNS forward lookup zone contains an A record for the host, and a reverse lookup zone contains a PTR record for the host. For more information, see [DNS records for hosts and appliances](evs-deployment-prereq-checklist.md#evs-prereq-dns-records).
+ Your **Host count per EVS environment** quota is at least the number of hosts that the environment will have after you add hosts. Host creation fails if the quota is lower. To raise the quota, request a quota increase. For more information, see [Service quotas for Amazon EVS](service-quotas-evs.md).
+ You know the ESX version that your target vSphere cluster uses. Select this version when you create the host, or an older version if it’s unavailable. If you choose an older version, upgrade the host with vSphere Lifecycle Manager, which can require host reboots and increase the time it takes to commission the host. If you don’t specify an ESX version, Amazon EVS uses the default ESX version of your environment’s VCF version. For more information, see [Supported VCF versions and instance types](versions-provided.md).
+ If you plan to use an EC2 partition placement group for your hosts, see the placement group guidance in [Resilience for Amazon EVS](disaster-recovery-resiliency.md).

The following conditions can make the SDDC Manager steps fail. Check them before you add the host.
+ A new host has the latest available version of the Amazon EVS custom vendor add-on, which provides important host functionality. If the hosts in your cluster use an older add-on version, adding the new host to the vSphere cluster causes cluster image remediation to fail. For the fix, see [Troubleshoot hosts](troubleshoot-hosts.md).
+ If you updated your ESX version after the environment was deployed, SDDC Manager can fail during VCF host validation in the commission hosts step. For the fix, see [Troubleshoot hosts](troubleshoot-hosts.md).

## Create the host
<a name="evs-env-create-host-evs"></a>

To create the host in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment where you want to create the host.

1. Choose the **Hosts** tab.

1. Choose **Create host**.

1. Enter the host name, the instance type, the ESX version, and your Amazon EC2 key pair, and then choose **Create host**.

1. To verify completion, check that the **Host state** has changed to **Created**.

1. Run the `create-environment-host` command. The following example adds a host that runs ESX 8.0 U3g. Replace the example environment ID, host name, and key pair name with your own values.

   ```bash
   aws evs create-environment-host \
       --environment-id "env-abcde12345" \
       --esx-version "ESXi-8.0U3g-24859861" \
       --host '{
           "hostName": "esxi-host-05",
           "keyName": "my-ec2-key-pair",
           "instanceType": "i4i.metal"
       }'
   ```

1. To verify completion, check that the state of the host is `CREATED`. Replace the example environment ID with your own value.

   ```bash
   aws evs list-environment-hosts \
       --environment-id "env-abcde12345"
   ```

## Commission the host in SDDC Manager
<a name="evs-env-create-host-sddc"></a>

You must commission the host and assign it to a cluster in the SDDC Manager user interface.

 **In SDDC Manager** 

1. Commission the new host. For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html) in the Broadcom documentation.

1. Add the new host to the cluster. For more information, see [How to Add an ESX Host to Your vSphere Cluster by Using the Quickstart Workflow](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/organizing-your-inventory/creating-and-configuring-clusters/use-quickstart-to-add---host-to-a-cluster.html) in the Broadcom documentation.

You have added a host to your environment and to the cluster. To check the environment after the change, see [Monitor environment status](evs-env-status-check.md). If commissioning or cluster image remediation fails, see [Troubleshoot hosts](troubleshoot-hosts.md).