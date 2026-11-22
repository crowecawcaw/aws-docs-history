

# Replace a host (EVS-deployed)

This page applies to EVS-deployed environments (VCF 5.2.x). For Self-deployed environments that run VCF 9.x, see [Manage hosts](host-management.md).

Replace a host when it fails, or before an EC2 `system-maintenance` or `instance-retirement` event occurs. You create the new host with the Amazon Elastic VMware Service console or the AWS CLI, move it into the cluster in SDDC Manager, and then delete the old host. For when to replace a host, see [Host maintenance and retirement events](evs-host-maintenance.md).

**Warning**  
Replace a host with local storage before the scheduled event occurs. If EC2 reboots the instance during the event, you lose the vSAN data that’s stored on its instance store volumes.

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API.

**Important**  
Amazon EVS hosts use the Amazon EVS custom vendor add-on to provide important host functionality. A new host has the latest available version of the add-on. If your environment uses hosts with an older add-on version, adding the new host to your vSphere cluster causes cluster image remediation to fail. For the fix, see [Troubleshoot hosts](troubleshoot-hosts.md).

**Note**  
If you updated your ESX version after deployment, SDDC Manager can fail during VMware Cloud Foundation (VCF) host validation in the commission hosts step. For the fix, see [Troubleshoot hosts](troubleshoot-hosts.md).

## Before you begin
<a name="host-replace-evs-deployed-prereqs"></a>

Before you begin, make sure that the following are true.
+ Your **Host count per EVS environment** quota allows one more host than the environment has. Host creation fails if the quota is lower than the number of hosts in the environment. You might need to request a quota increase for maintenance that requires host replacement. For more information, see [Service quotas for Amazon EVS](service-quotas-evs.md).
+ The A and PTR DNS records for the new host exist. For more information, see [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md).
+ You know the ESX version that your vSphere cluster uses. For more information, see [Add a host (VCF 5.x)](evs-env-create-host.md).

## Step 1: Create the new host
<a name="host-replace-evs-deployed-create"></a>

To create the new host in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment that contains the host to be replaced.

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

1. To verify completion, check that the state of the new host is `CREATED`. Replace the example environment ID with your own value.

   ```bash
   aws evs list-environment-hosts \
       --environment-id "env-abcde12345"
   ```

## Step 2: Retrieve the ESX root password
<a name="host-replace-evs-deployed-creds"></a>

1. Retrieve the ESX root password of the new host from AWS Secrets Manager. For more information, see [Retrieve VCF credentials and access appliances](access-vcf.md) and [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the * AWS Secrets Manager User Guide*.

1. Sign in to the VMware Host Client of the new host as `root` with this password, to confirm that the password works before you commission the host.

## Step 3: Move the new host into the cluster
<a name="host-replace-evs-deployed-sddc"></a>

 **In SDDC Manager** 

1. Commission the new host, using the ESX root password that you retrieved in the previous step. For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html) in the Broadcom documentation.

1. Add the new host to the cluster that contains the host to be replaced. For more information, see [How to Add an ESX Host to Your vSphere Cluster by Using the Quickstart Workflow](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/organizing-your-inventory/creating-and-configuring-clusters/use-quickstart-to-add---host-to-a-cluster.html) in the Broadcom documentation.

1. Decommission the old host to remove it from SDDC Manager. For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html) in the Broadcom documentation.

## Step 4: Delete the old host
<a name="host-replace-evs-deployed-delete"></a>

To delete the old host in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Return to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. On the **Hosts** tab, select the old host and choose **Delete** > **Delete host**.

1. Run the `delete-environment-host` command. Replace the example environment ID and host name with your own values.

   ```bash
   aws evs delete-environment-host \
       --environment-id "env-abcde12345" \
       --host-name "esxi-host-01"
   ```

1. To verify completion, list the hosts and confirm that the old host is no longer listed or is in the `DELETED` state.

   ```bash
   aws evs list-environment-hosts \
       --environment-id "env-abcde12345"
   ```

You have replaced the host. To check the environment after the change, see [Monitor environment status](evs-env-status-check.md). If a step fails, see [Troubleshoot hosts](troubleshoot-hosts.md).