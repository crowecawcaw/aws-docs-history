

# How Windows Server entitlements work
<a name="entitlements-concepts"></a>

With Windows Server entitlements, you can consume Windows Server licenses for the virtual machines (VMs) running in your Amazon EVS environment, directly through AWS and on a pay-as-you-go basis. This topic describes the resources and workflow involved.

## Windows Server entitlement components
<a name="entitlements-concepts-components"></a>

Windows Server entitlements use the following resources.

 **EVS vCenter connector**   
An EVS vCenter connector establishes a persistent connection between Amazon EVS and vCenter Server. Amazon EVS uses the connector to identify your VMs and monitor their Windows Server entitlement usage.

 **Windows Server entitlement**   
With an entitlement, you get AWS-offered Windows Server licensing coverage for a specific VM. After you create an entitlement, Amazon EVS monitors the VM’s Windows Server license usage so that you can consume licenses on a pay-as-you-go basis.

 **Windows Server activation**   
The process of activating Windows Server on your entitled VMs against an Amazon EVS activation endpoint that you create in your VPC. You perform this activation yourself. For more information, see [Activating Windows Server on entitled VMs](activate-windows-server.md).

## Setup workflow for Windows Server entitlements
<a name="entitlements-concepts-workflow"></a>

Before you begin, make sure that you meet the requirements in [Prerequisites for Windows Server entitlements](entitlements-prerequisites.md).

To use Windows Server entitlements, complete the following steps:

1. Create a vCenter connector so that Amazon EVS can communicate with your vCenter Server appliance. See [Creating a vCenter connector](create-vcenter-connector.md).

1. Create Windows Server entitlements for the VMs you want to cover. See [Creating Windows Server entitlements for your VMs](create-entitlements.md).

1. Activate Windows Server on the entitled VMs. See [Activating Windows Server on entitled VMs](activate-windows-server.md).

After you set up Windows Server entitlements, you can also do the following:
+ Rotate the vCenter credentials that the connector uses. See [Rotating vCenter connector credentials](rotate-vcenter-credentials.md).
+ Stop using Windows Server entitlements when you no longer need AWS offered Windows Server licensing for your VMs. See [Deleting Windows Server entitlements](delete-entitlements.md).
+ Troubleshoot common entitlement issues. See [Troubleshooting Windows Server entitlements](troubleshoot-entitlements.md).