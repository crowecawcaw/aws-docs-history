

# VCF licensing

Amazon Elastic VMware Service (Amazon EVS) uses VMware Cloud Foundation (VCF) subscriptions with license portability entitlements that you bring to AWS (BYOS). You must have a valid and active VCF subscription to use Amazon EVS, whichever way you deploy VCF.

**Note**  
Amazon EVS doesn’t support perpetual vSphere licenses.

Your VCF subscription is available to Amazon EVS across all AWS Regions for license compliance.

## License keys by deployment mode
<a name="vcf-license-mgmt-by-mode"></a>

VCF 9.x environments are deployed using Evaluation Mode. A valid VCF subscription must be provided before the evaluation period expires.

What you do and don’t do with license keys depends on the deployment mode, as the following table shows.


| Deployment mode | You do | You don’t | 
| --- | --- | --- | 
| VCF 9.x (Self-deployed) | Provide a valid VCF subscription before the evaluation period expires. After you install VCF, add the license keys that your VCF deployment needs in your VCF management appliance, and manage them there. | Provide license keys when you create the environment. | 
| VCF 5.2.x (EVS-deployed) | Provide a VCF solution key and a vSAN license key in the environment creation request. You use the vSphere license key as the VCF solution key. Manage the keys in SDDC Manager. | Use a license key that is already in use in another Amazon EVS environment. | 

Amazon EVS doesn’t validate license keys. To validate a license key, use the [Broadcom support portal](https://support.broadcom.com/web/ecx).

## Key requirements at environment creation
<a name="vcf-license-mgmt-creation"></a>

The requirements in this section apply when you provide license keys in the environment creation request, which you do for VCF 5.2.x.

Each VCF license key can be used for only one Amazon EVS environment. Environment creation fails if you use a VCF license key that is already in use in another environment.

Your VCF solution key must have enough cores for the four initial hosts that Amazon EVS deploys when it creates the environment. The required core count depends on the instance type that you select, because each instance type has a different number of cores.


| Instance type | Cores per host | Minimum cores for four hosts (VCF solution key) | 
| --- | --- | --- | 
|  `i4i.metal`  | 64 | 256 | 
|  `i7i.metal-24xl`  | 48 | 192 | 
|  `i7i.metal-48xl`  | 96 | 384 | 

The vSAN license key must meet the capacity requirement for the instance type that you select.


| Instance type | Minimum vSAN capacity for four hosts (vSAN license key) | 
| --- | --- | 
|  `i4i.metal`  | 110 TiB | 
|  `i7i.metal-24xl`  | 82 TiB | 
|  `i7i.metal-48xl`  | 164 TiB | 

Environment creation fails if you use undersized license keys. Your environment also fails to deploy if you provide an expired license key.

For more information about VCF license keys in VCF 5.2.x, see [Managing License Keys in VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/license-management-admin.html) in the Broadcom documentation.

## Manage license keys in SDDC Manager
<a name="license-mgmt"></a>

You are responsible for managing your VCF subscriptions. In environments where Amazon EVS deploys VCF 5.2.x, you manage your VCF solution and vSAN license keys in SDDC Manager.

**Important**  
Amazon EVS requires that you maintain valid VCF solution and vSAN license keys in SDDC Manager for the service to function properly. You assign keys to your hosts and vSAN cluster in the vSphere Client. You must also make sure that those keys appear on the licensing screen of the SDDC Manager user interface.

If you remove your license keys from SDDC Manager, or replace them with a key that is in use elsewhere, the environment status check fails. A failed status check prevents you from adding hosts to your Amazon EVS environment. For more information, see [Monitor environment status](evs-env-status-check.md) and [Troubleshoot environment status checks](troubleshoot-status-checks.md).

## Add VCF license keys
<a name="add-vcf-license"></a>

To license hosts that you add after the initial deployment, or to license more environments, do the following.

1. In the Broadcom support portal, purchase more VCF license keys, or split or merge existing license keys.

1. Add the purchased license keys to the vCenter Server and SDDC Manager inventory.

1. When you add hosts, assign the license keys to the correct hosts in vSphere. Make sure that the keys have enough cores and vSAN storage capacity.

1. Assign new license keys to vCenter Server before the evaluation period of the key expires, so that they stay active.

Amazon EVS doesn’t support unlicensed hosts.

For more information, see [Configuring License Settings for Assets in the vSphere Client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/license-management/managing-licenses/configuring-license-settings-for-assets-in-the-vsphere-client.html#GUID-670D0552-5880-441C-AEEA-AE78C52CA075-en) and [Create a New License](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/license-management/managing-licenses/create-a-new-license.html) in the Broadcom documentation. If you have problems with license keys that you added, see [Troubleshoot environment status checks](troubleshoot-status-checks.md).

## Remove VCF license keys
<a name="remove-vcf-license"></a>

After you delete hosts, you can remove VCF license keys from the SDDC Manager inventory to reduce your core and vSAN capacity.
+ To stay in compliance with the licensing models of the products that you use with vSphere, remove all unassigned license keys from the inventory.
+ If you split, merged or upgraded license keys in the Broadcom support portal, remove the old license keys.

For more information, see [Remove a license](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/license-management/managing-licenses/remove-a-license.html) in the Broadcom documentation.

Next, plan security, support, and recovery. See [Plan security, support, and recovery](plan-security-support.md).