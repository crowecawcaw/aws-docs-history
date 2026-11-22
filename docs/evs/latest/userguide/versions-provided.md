

# Supported VCF versions and instance types

Amazon Elastic VMware Service supports the following VMware Cloud Foundation (VCF) versions and ESX builds on each Amazon EC2 instance type, for both deployment modes. Each row is an instance type. The VCF 5.2.x column covers EVS-deployed mode, which installs only VCF 5.2.x. The VCF 9.0 and VCF 9.1 columns cover the VCF 9.x versions that you deploy in Self-deployed mode, which is the only mode that supports VCF 9.x. You can also deploy VCF 5.x in Self-deployed mode. The last column lists the ESX builds, including the ESXi 8.0 builds for VCF 5.x.

## Supported VCF versions by instance type
<a name="current-vcf-versions"></a>

The following table shows the supported VCF versions and ESX builds for each instance type.


| Instance type | Storage | vCPUs and memory | VCF 5.2.x | VCF 9.0 | VCF 9.1 | ESX builds you can choose when you add a host | 
| --- | --- | --- | --- | --- | --- | --- | 
|  `i4i.metal`  | Local NVMe | 128 vCPUs, 1,024 GiB | 5.2.2, 5.2.1 (Restricted) | Available | Available | ESXi 8.0 U3b to 8.0 U3k, and ESX 9.0.2.0 to 9.1.1.0 | 
|  `i7i.metal-24xl`  | Local NVMe | 96 vCPUs, 768 GiB | 5.2.2, 5.2.1 (Restricted) | Available | Available | ESXi 8.0 U3b to 8.0 U3k, and ESX 9.0.2.0 to 9.1.1.0 | 
|  `i7i.metal-48xl`  | Local NVMe | 192 vCPUs, 1,536 GiB | 5.2.2 | Available | Available | ESXi 8.0 U3b to 8.0 U3k, and ESX 9.0.2.0 to 9.1.1.0 | 
|  `r7i.metal-24xl`  | Diskless | 96 vCPUs, 768 GiB | Not available | Available | Available | ESX 9.0.2.0 to 9.1.1.0 | 
|  `r7i.metal-48xl`  | Diskless | 192 vCPUs, 1,536 GiB | Not available | Available | Available | ESX 9.0.2.0 to 9.1.1.0 | 

All hosts in a VCF cluster must use the same instance type.

Instance types with the Diskless storage type have no local NVMe storage, so they can’t use vSAN on local disks and require external storage for the principal datastore. They support only VCF 9.x. For more information, see [Deploy in Self-deployed mode](getting-started-self-deployed.md), [External storage options for diskless hosts](external-storage-diskless.md), and [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

For the network bandwidth and other hardware details of each instance type, see [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/). For the AWS Regions where Amazon EVS is available, see [Amazon Elastic VMware Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/evs.html) in the * AWS General Reference*.

## Column key
<a name="column-key"></a>
+  **VCF 5.2.x** is deployed in EVS-deployed mode, where Amazon EVS installs VCF. The cells name the releases that you can choose. Release 5.2.2 is the API value `VCF-5.2.2` with the default ESX version `ESXi-8.0U3g-24859861`. Release 5.2.1 is the API value `VCF-5.2.1` with the default ESX version `ESXi-8.0U3b-24280767`.
+  **VCF 9.0** and **VCF 9.1**, which includes VCF 9.1.1, are deployed in Self-deployed mode. Both use the API value `SELF_DEPLOYED`. Amazon EVS creates the VLAN subnets, and you add the hosts and install VCF 9.x yourself. When you add a host without `--esx-version`, Amazon EVS uses the default ESX version for Self-deployed mode, which `get-versions` reports as `defaultEsxVersion`. For the steps, see [Deploy in Self-deployed mode](getting-started-self-deployed.md).
+  **Available** means that you can choose the version. **Restricted** means that you must request access first. For more information, see [Request access to restricted VCF versions](#version-restrictions). **Not available** means that the instance type doesn’t support the version.
+  **ESX builds** are the builds that you can choose when you add a host of that instance type. The exact build strings are in the `instanceTypeEsxVersions` field of the `get-versions` response.

## Check what is available to you
<a name="check-provided-versions"></a>

The VCF versions and ESX builds available to you can differ from the table, for example when a version is restricted. The Amazon EVS console shows the VCF versions in the create environment wizard, and the ESX versions when you add a host. You can also use the AWS CLI to view the VCF versions, ESX versions, and EC2 instance types. If a version shows the Restricted status, see [Request access to restricted VCF versions](#version-restrictions) to request access.

To check the versions in the Amazon EVS console or with the AWS CLI, do the following.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. On the navigation menu, choose **Environments**.

1. Do one of the following:

   To check VCF versions, do the following.

   1. Choose **Create Environment**.

   1. Under **Validate Amazon EVS requirements**, choose your VCF version. The status shows whether the version is available or restricted for your account.

   To check ESX versions, do the following.

   1. Choose an existing environment.

   1. Choose **Create host**.

   1. Select an instance type to see the available ESX versions.
Run the following command to retrieve information about VCF and ESX versions. Replace `<region-code>` with the code of the Region that you want to check.  

```bash
aws evs get-versions --region <region-code>
```
The following is example output.  

```json
{
    "vcfVersions": [
        {
            "vcfVersion": "VCF-5.2.1",
            "status": "RESTRICTED",
            "defaultEsxVersion": "ESXi-8.0U3b-24280767",
            "instanceTypes": [
                "i4i.metal",
                "i7i.metal-24xl"
            ]
        },
        {
            "vcfVersion": "VCF-5.2.2",
            "status": "AVAILABLE",
            "defaultEsxVersion": "ESXi-8.0U3g-24859861",
            "instanceTypes": [
                "i4i.metal",
                "i7i.metal-24xl",
                "i7i.metal-48xl"
            ]
        },
        {
            "vcfVersion": "SELF_DEPLOYED",
            "status": "AVAILABLE",
            "defaultEsxVersion": "ESXi-9.0.2.0.25148076",
            "instanceTypes": [
                "i4i.metal",
                "i7i.metal-24xl",
                "i7i.metal-48xl",
                "r7i.metal-24xl",
                "r7i.metal-48xl"
            ]
        }
    ],
    "instanceTypeEsxVersions": [
        {
            "instanceType": "i4i.metal",
            "esxVersions": [
                "ESXi-8.0U3b-24280767",
                "ESXi-8.0U3g-24859861",
                "ESXi-9.0.2.0.25148076",
                "ESXi-9.0.2.0100.25595025",
                "ESXi-9.1.0.0100.25433460",
                "ESXi-9.1.0.0200.25557999",
                "ESXi-9.1.1.0.25714478",
                "ESXi-8.0U3i-25205845",
                "ESXi-8.0U3j-25429389",
                "ESXi-8.0U3k-25595708"
            ]
        },
        {
            "instanceType": "i7i.metal-24xl",
            "esxVersions": [
                "ESXi-8.0U3b-24280767",
                "ESXi-8.0U3g-24859861",
                "ESXi-9.0.2.0.25148076",
                "ESXi-9.0.2.0100.25595025",
                "ESXi-9.1.0.0100.25433460",
                "ESXi-9.1.0.0200.25557999",
                "ESXi-9.1.1.0.25714478",
                "ESXi-8.0U3i-25205845",
                "ESXi-8.0U3j-25429389",
                "ESXi-8.0U3k-25595708"
            ]
        },
        {
            "instanceType": "i7i.metal-48xl",
            "esxVersions": [
                "ESXi-8.0U3b-24280767",
                "ESXi-8.0U3g-24859861",
                "ESXi-9.0.2.0.25148076",
                "ESXi-9.0.2.0100.25595025",
                "ESXi-9.1.0.0100.25433460",
                "ESXi-9.1.0.0200.25557999",
                "ESXi-9.1.1.0.25714478",
                "ESXi-8.0U3i-25205845",
                "ESXi-8.0U3j-25429389",
                "ESXi-8.0U3k-25595708"
            ]
        },
        {
            "instanceType": "r7i.metal-24xl",
            "esxVersions": [
                "ESXi-9.0.2.0.25148076",
                "ESXi-9.0.2.0100.25595025",
                "ESXi-9.1.0.0100.25433460",
                "ESXi-9.1.0.0200.25557999",
                "ESXi-9.1.1.0.25714478"
            ]
        },
        {
            "instanceType": "r7i.metal-48xl",
            "esxVersions": [
                "ESXi-9.0.2.0.25148076",
                "ESXi-9.0.2.0100.25595025",
                "ESXi-9.1.0.0100.25433460",
                "ESXi-9.1.0.0200.25557999",
                "ESXi-9.1.1.0.25714478"
            ]
        }
    ]
}
```

## ESX version considerations
<a name="esx-versions"></a>

Each VCF version has a default ESX version based on the Broadcom VCF Bill of Materials (BOM). When you create an environment, you can’t choose a specific ESX version. Amazon EVS applies the default ESX version for the selected VCF version.

When you add a host to your environment, you can select an available ESX version for the instance type that you choose. If you don’t specify one, Amazon EVS uses the default ESX version for the VCF version of your environment.

After you add a host, you can upgrade its ESX version only with vCenter Lifecycle Manager.

**Note**  
Amazon EVS doesn’t provide every VCF and ESX version that Broadcom releases. For software interoperability information, see the [Broadcom Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability?col=1). For hardware compatibility of AWS EC2 instances, see the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/).

## Request access to restricted VCF versions
<a name="version-restrictions"></a>

To use a VCF version with the `RESTRICTED` status, [contact AWS Support](https://support.console.aws.amazon.com/support/home#/case/create) with the following information:
+ Your AWS account ID
+ The AWS Region
+ The specific VCF version that you need
+ Your use case and business justification (for example, security and compliance, or a compatibility dependency)

 AWS Support reviews your request and either approves it or asks for more information. After approval, the version status changes to `AVAILABLE` in the Amazon EVS console and in the `get-versions` response.