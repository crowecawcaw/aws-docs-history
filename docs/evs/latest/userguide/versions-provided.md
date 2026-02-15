# VCF versions and EC2 instance types provided by Amazon EVS

Amazon EVS provides multiple versions of VMware Cloud Foundation (VCF), ESX, and EC2 instance types that you can select when creating an environment and creating a host.

## Checking provided VCF versions, ESX versions, and EC2 instance types

The AWS console shows the list of VCF versions provided by Amazon EVS in the create environment wizard. The available ESX versions are visible when you select an instance type while adding a host to an existing environment. You can also view VCF versions, ESX versions, and EC2 instance types using the CLI.

###### Example

Amazon EVS console

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. On the navigation menu, choose **Environments**.
3. Do one of the following:

**To check VCF versions:**

    1. Select **Create Environment**.
    2. Under the **Validate Amazon EVS requirements**, choose your VCF version to see if the status is available or restricted for you.

**To check ESX versions:**

    1. Select an existing environment.
    2. Choose **Create host**.
    3. Select an instance type to see the available ESX versions.

AWS CLI

Run the following command to retrieve information about VCF and ESX versions:

```
aws evs get-versions --region <region-name>
```

Example response:

```
{
   "instanceTypeEsxVersions": [
      {
         "esxVersions": [ "ESXi-8.0U3b-24280767","ESXi-8.0U3g-24859861" ],
         "instanceType": "i4i.metal"
      }
   ],
   "vcfVersions": [
      {
            "vcfVersion": "VCF-5.2.1",
            "status": "RESTRICTED",
            "defaultEsxVersion": "ESXi-8.0U3b-24280767",
            "instanceTypes": ["i4i.metal"]
      },
      {
            "vcfVersion": "VCF-5.2.2",
            "status": "AVAILABLE",
            "defaultEsxVersion": "ESXi-8.0U3g-24859861",
            "instanceTypes": ["i4i.metal"]
      }
   ]
}
```

###### Note

If the version you need shows `RESTRICTED`, and you have a particular need, see [Requesting access to restricted VCF versions](#version-restrictions "#version-restrictions") for more information on how to get access to that version.

## Current VCF versions in Amazon EVS

Amazon EVS currently provides the following VCF versions for environment creation:

| VCF version | Default ESX version  | Status     | EC2 instance types |
| ----------- | -------------------- | ---------- | ------------------ |
| VCF-5.2.2   | ESXi-8.0U3g-24859861 | AVAILABLE  | i4i.metal          |
| VCF-5.2.1   | ESXi-8.0U3b-24280767 | RESTRICTED | i4i.metal          |

###### Note

When creating a new Amazon EVS environment, you must specify a VCF version.

## ESX version considerations

Each VCF version has a default ESX version based on the Broadcom VCF Bill of Materials (BOM). When creating a new environment, you cannot choose a specific ESX version. The default ESX version for the selected VCF version is applied automatically.

However, when adding a host to your environment, you can select an available ESX version for your chosen instance type. If you don’t specify one, Amazon EVS uses the default ESX version associated with your environment’s VCF version.

After a host has been added, its ESX version can only be upgraded using vCenter Lifecycle Manager.

###### Note

Amazon EVS does not provide all versions of VCF and ESX released by Broadcom. For software interoperability information, refer to the [Broadcom Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability?col=1 "https://interopmatrix.broadcom.com/Interoperability?col=1"). For full hardware compatibility with AWS EC2 instances, refer to the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/ "https://compatibilityguide.broadcom.com/").

## Requesting access to restricted VCF versions

If you need access to a VCF version that with a `RESTRICTED` status, [contact AWS Support](http://support..aws.amazon.com/support/home#/case/create "http://support..aws.amazon.com/support/home#/case/create") with the following information:

- Your AWS account ID
- The AWS region
- The specific VCF version you need
- Your use case and business justification (for example, security/compliance, compatibility/dependency, and others)

AWS Support will review your request and either approve or request additional information. After approval, the version status will change to `AVAILABLE` in the AWS console or `get-versions` API response.
