

# Windows Server entitlements

A Windows Server entitlement gives a virtual machine (VM) in your Amazon Elastic VMware Service environment Windows Server licensing coverage through AWS. You pay only for what you use, per vCPU-hour.

## Choose how to license Windows Server
<a name="entitlements-license-choice"></a>

You have two ways to license Windows Server for the VMs in your environment:

 **Bring your own licenses**   
If you have eligible Windows Server licenses with portability rights, you can bring them to your Windows VMs. You don’t need Windows Server entitlements for those VMs.

 **Use Windows Server entitlements**   
For VMs without portability rights, you consume Windows Server licenses through AWS and pay per vCPU-hour.

For prices, see [Amazon EVS pricing](https://aws.amazon.com/evs/pricing).

## How Windows Server entitlements work
<a name="entitlements-concepts-components"></a>

Windows Server entitlements use the following resources.

 **vCenter connector**   
A vCenter connector is a persistent connection between Amazon EVS and vCenter Server. Amazon EVS uses the connector to identify your VMs and monitor their Windows Server entitlement usage.

 **Windows Server entitlement**   
An entitlement gives a specific VM Windows Server licensing coverage offered by AWS. After you create an entitlement, Amazon EVS starts to monitor the Windows Server entitlement usage of that VM.

 **Windows Server activation**   
You activate Windows Server on each entitled VM against an Amazon EVS activation endpoint that you create in your VPC. You perform this activation yourself.

### When the connector loses contact with vCenter
<a name="entitlements-grace-period"></a>

Amazon EVS needs the vCenter connector to reach vCenter Server. If the connector reachability check fails, the entitlements of all Windows Server VMs under that vCenter Server change to `AT_RISK`. You have 8 hours from the first failed check to restore the connection.
+ If you restore the connection within 8 hours, Amazon EVS keeps your entitlements without further action.
+ If you don’t restore the connection within 8 hours, Amazon EVS removes the entitlements and changes their status to `ENTITLEMENT_REMOVED`. License usage tracking stops as of the time the connection was lost.

For causes and solutions, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).

## Before you begin
<a name="entitlements-prerequisites"></a>

Before you set up Windows Server entitlements, make sure that you meet the following prerequisites.
+ You have an active Amazon EVS environment.
+ You have a dedicated vCenter user for the connector to use. We recommend that you give this user a ReadOnly role. Don’t use credentials with elevated or administrative permissions.
+ You have created a secret in AWS Secrets Manager that holds the credentials of the dedicated vCenter user. The secret must contain two keys, `username` and `password`.
+ You have added the tag `EvsAccess=true` to the secret. If you encrypted the secret with your own AWS KMS key, you have also added the tag `EvsAccess=true` to the AWS KMS key.
+ The VMs that you want to cover run a supported Windows Server guest operating system. Amazon EVS supports Windows Server 2016 or later.

## Setup workflow
<a name="entitlements-concepts-workflow"></a>

To use Windows Server entitlements, complete these steps in order:

1. Create a vCenter connector so that Amazon EVS can communicate with your vCenter Server appliance. For instructions, see [Create a connector](evs-env-create-connector.md).

1. Create Windows Server entitlements for the VMs that you want to cover. For instructions, see [Create Windows Server entitlements](create-entitlements.md).

1. Activate Windows Server on the entitled VMs. For instructions, see [Activate Windows Server on entitled VMs](activate-windows-server.md).

After setup, you can also do the following:
+ Rotate the vCenter credentials that the connector uses. For instructions, see [Rotate vCenter connector credentials](rotate-vcenter-credentials.md).
+ Delete entitlements when you no longer need Windows Server licensing from AWS for a VM. For instructions, see [Delete Windows Server entitlements](delete-entitlements.md).
+ Resolve entitlement issues. For more information, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).

**Topics**