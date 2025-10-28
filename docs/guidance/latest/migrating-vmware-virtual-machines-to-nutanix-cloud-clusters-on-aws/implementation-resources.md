# Implementation

resources

**Step 1 – Prerequisites**

1. Obtain on-premises connectivity using VPN or direct connectivity with AWS.
2. VMware ESXi hosts should be reachable from Nutanix Move on ports TCP 443 and TCP
3.
4. VMware vCenter should be reachable from Nutanix Move Appliance on ports TCP
5.
6. Allow ports (TCP and UDP) 2049 and 111 between the Nutanix Move network and the
   AHV CVM network.

**Step 2 - Setup Nutanix Cloud Clusters**

1. Use the [Nutanix Cloud Clusters on AWS Deployment and User Guide](https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Clusters-AWS:Nutanix-Clusters-AWS "https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Clusters-AWS:Nutanix-Clusters-AWS") to setup NC2 on
   AWS.

**Step 3 - Deploy Nutanix Move Tool**

1. Refer to the [Deploying Move on AHV (CLI)](https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Move-v5_2:top-deploy-vmms-t.html "https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Move-v5_2:top-deploy-vmms-t.html") to setup the appliance.
2. Become familiar with the Nutanix Move [migration considerations.](https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Move-v5_2:top-migration-considerations-c.html "https://portal.nutanix.com/page/documents/details?targetId=Nutanix-Move-v5_2:top-migration-considerations-c.html")

**Step 4 - Setup Move for Source and Target Environment**

Within the Nutanix Move tool, add the source environment (existing ESXi environment) and
the target environment (AOS on AHV).

**Step 5 - Move a Microsoft Windows virtual server from an ESXi
environment to AHV on Nutanix.**

1. Create a new Migration Plan
2. Select **VMware Vcenter** as the source
   environment
3. Select the target Nutanix Cluster and the Windows virtual machine to be migrated
4. Select the target network where the destination virtual machine network interfaces
   will connect
   Prepare the guest operating system for the migration:

5. Provide the administrative credentials for the source Windows virtual
   machine
6. Review the migration plan summary as shown below in Figure 3
7. Select **Save** and **Start** to initiate the migration process.

**Step 6 - Cutover to complete the migration**

Monitor the progress of the data being copied. Select **Cutover** to complete the migration.

Nutanix Move will power off the source virtual machine and perform a final data
synchronization to copy any changed data.

**Step 7 - Verify the cutover**

Verify the successful completion of the cutover by logging into the Windows server and
monitoring it on the Nutanix cluster console.
