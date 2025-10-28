# VCF subscriptions

###### Note

Amazon EVS does not support perpetual vSphere licenses.
You must have a valid and active VMware Cloud Foundation subscription to use Amazon EVS.

Amazon EVS uses VMware Cloud Foundation (VCF) subscriptions with license portability entitlements that you bring to AWS (BYOS).
To successfully deploy an Amazon EVS environment, you need to provide a valid VCF solution key and a vSAN license key in the environment creation request.
The vSphere license key serves as the solution key for VCF.
Each VCF license key can be used for only one Amazon EVS environment.
Environment creation fails if you attempt to use a VCF license key that is already in use in another environment.

Your VCF solution key must have at least 256 cores to provide adequate core capacity for the four initial EC2 i4i.metal hosts that Amazon EVS deploys upon environment creation.
Each i4i.metal host requires 64 cores.
The vSAN license key must have at least 110 TiB of vSAN capacity.
Environment creation fails if you attempt to use undersized license keys.

###### Note

Your VCF subscription will be available to Amazon EVS across all AWS Regions for license compliance.
Amazon EVS does not validate license keys.
To validate license keys, visit [Broadcom support](https://support.broadcom.com/web/ecx "https://support.broadcom.com/web/ecx").

###### Note

Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance.

## Subscription management

You are responsible for managing your VCF subscriptions.
Your VCF subscriptions must be managed in SDDC Manager.
Removing your license keys from SDDC Manager or replacing them with an in-use license key will result in a failed environment status check, preventing you from adding hosts to your Amazon EVS environment.
For more information about environment status checks, [Monitor your environment's status and resources](evs-env-status-check.md "evs-env-status-check.md") and [Troubleshoot failed environment status checks](troubleshooting.md#troubleshoot-env-status "troubleshooting.md#troubleshoot-env-status").
For more information about VCF license keys, see [Managing License Keys in VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/license-management-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/license-management-admin.html") in the VMware Cloud Foundation documentation.

###### Important

Use the SDDC Manager user interface to manage VCF solution and vSAN license keys.
Amazon EVS requires that you maintain valid VCF solution and vSAN license keys in SDDC Manager for the service to function properly.
While keys must be assigned to your hosts and vSAN cluster using the vSphere Client, you must make sure that those keys also appear in the licensing screen of the SDDC Manager user interface.

## Adding VCF license keys

In the Broadcom support portal, you can purchase additional VCF license keys, split license keys if you already have large keys, or merge multiple license keys.
This allows you to license hosts that you added to your environment after initial deployment, or license additional environments.
Make sure that purchased license keys are added in the vCenter Sever and SDDC Manager inventory.
If adding hosts, ensure that your licenses are assigned to the correct hosts in vSphere and have adequate cores and vSAN storage capacity.
Amazon EVS does not support unlicensed hosts.
For more information, see [Configuring License Settings for Assets in the vSphere Client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/license-management-host-management/managing-licenses-host-management/configuring-license-settings-for-assets-in-the-vsphere-client-host-management.html#GUID-670D0552-5880-441C-AEEA-AE78C52CA075-en "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/license-management-host-management/managing-licenses-host-management/configuring-license-settings-for-assets-in-the-vsphere-client-host-management.html#GUID-670D0552-5880-441C-AEEA-AE78C52CA075-en") in the VMware documentation.

New unexpired license keys must be assigned to vCenter Server before the license key’s evaluation period expires to remain active.
Active license keys are required to successfully set up an Amazon EVS environment.
You environment will fail to deploy if an expired license key is provided.
For more information about VCF license key creation, see [Create a New License](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/license-management-host-management/managing-licenses-host-management/create-a-new-license-host-management.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/license-management-host-management/managing-licenses-host-management/create-a-new-license-host-management.html") in the VMware documentation.
If you are experiencing issues with your added license keys, see [Key coverage check failed](troubleshooting.md#troubleshoot-key-coverage "troubleshooting.md#troubleshoot-key-coverage").

## Removing VCF license keys

You can remove VCF license keys from the SDDC Manager inventory to reduce your core and vSAN capacity after deleting hosts in your environment.
To remain in compliance with the licensing models of products that you use with vSphere, you must remove all unassigned license keys from the inventory.
If you have split, merged, or upgraded license keys in the Broadcom Support Portal, you must remove the old license keys.
For more information, see [Remove a license](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/license-management-host-management/managing-licenses-host-management/remove-a-license-host-management.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/license-management-host-management/managing-licenses-host-management/remove-a-license-host-management.html") in the VMware documentation.
