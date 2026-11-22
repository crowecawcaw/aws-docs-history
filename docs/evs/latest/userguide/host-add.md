

# Add a host (VCF 9.x)

After you deploy VMware Cloud Foundation (VCF) in a Self-deployed environment, you can add hosts to increase capacity and workload resiliency. You create the host with the Amazon Elastic VMware Service console or the AWS CLI, and then you add it to a cluster with VCF 9.x tools. You can add hosts with local storage or diskless hosts.

To add the first hosts of a new environment, see [Step 3: Add hosts](self-deployed-add-hosts.md) instead. For EVS-deployed environments (VCF 5.2.x), see [Add a host (VCF 5.x)](evs-env-create-host.md).

**Important**  
All hosts in a cluster must use the same instance type and the same ESX version. After you add a host, you can change its ESX version only with vSphere Lifecycle Manager.

## Before you begin
<a name="host-add-prereqs"></a>

Before you begin, make sure that the following are true.
+ You created the forward (A) and reverse (PTR) DNS records for the new host, and they resolve. For more information, see [Step 2: Create DNS records](self-deployed-host-dns-records.md).
+ Your **Host count per EVS environment** quota is at least the number of hosts that the environment will have after you add hosts. Host creation fails if the quota is lower. For more information, see [Service quotas for Amazon EVS](service-quotas-evs.md).
+ You have the name of an Amazon EC2 key pair. Amazon EVS requires the key pair name when you add a host.
+ You know the instance type and ESX version of the hosts in the target cluster. For the versions available to your account, run `aws evs get-versions` or see [Supported VCF versions and instance types](versions-provided.md).
+ For a diskless host, the new host can reach the external storage of the cluster. For more information, see [Step 2: Connect a diskless host to external storage](#diskless-host-add-storage).

## Step 1: Create the host
<a name="host-add-create"></a>

To create the host in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**, and then choose your environment.

1. Choose the **Hosts** tab, and then choose **Create host**.

1. Enter the short host name from your DNS records (such as `esx05`), the instance type and ESX version of the target cluster, and your Amazon EC2 key pair.

1. Choose **Create host**.

1. To verify completion, check that the **Host state** has changed to **Created**.

1. Run the `aws evs create-environment-host` command. The following example adds a host that runs ESX 9.0.2. Replace the example environment ID, host name, and key pair name with your own values. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs create-environment-host \
       --environment-id env-abcde12345 \
       --esx-version ESXi-9.0.2.0.25148076 \
       --host '{
           "hostName": "esx05",
           "keyName": "my-ec2-key-pair",
           "instanceType": "i4i.metal"
       }' \
       --region <region-code>
   ```

1. Check the host state. The create command doesn’t return a host ID, so use the host name to find the host. Replace the example environment ID with your own value. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs list-environment-hosts \
       --environment-id env-abcde12345 \
       --query 'environmentHosts[].[hostName,hostState,ipAddress]' \
       --output table \
       --region <region-code>
   ```

Don’t run the create command again for a host that is in the `CREATING` state. A host usually reaches `CREATED` in about 9 minutes. When the host is `CREATED`, confirm that its IP address equals the address in its A record. If the host stays in `CREATING` or moves to `CREATE_FAILED`, check its DNS records first. For more information, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

Amazon EVS stores the ESX root password of each host in AWS Secrets Manager. Each host has its own secret. You need the root password to add the host to VCF.

## Step 2: Connect a diskless host to external storage
<a name="diskless-host-add-storage"></a>

Skip this step for hosts with local storage.

Diskless hosts have no local storage for VCF, so the datastores of the cluster are on external storage. Before you add a diskless host to a cluster, make sure that the host can reach the external storage of the cluster, and mount the datastores on the host.
+ For Amazon FSx for OpenZFS, the NFS export list of each volume and the security group of the file system must allow the host management VLAN subnet. For more information, see [Configure FSx for OpenZFS as principal storage for diskless hosts](config-fsx-openzfs-datastore.md).
+ For other external storage, see [External storage options for diskless hosts](external-storage-diskless.md).

## Step 3: Add the host to a cluster in VCF
<a name="host-add-vcf"></a>

 **In VCF** 

1. Add the host to the VCF inventory with the ESX root password from Secrets Manager.

1. Add the host to the target cluster.

For the procedures, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html).

You have added the host when it is connected in the cluster and shows no configuration errors. To check the environment after the change, see [Monitor environment status](evs-env-status-check.md). If adding the host to the cluster fails, see [Troubleshoot hosts](troubleshoot-hosts.md).