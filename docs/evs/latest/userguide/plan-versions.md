

# Choose VCF and ESX versions

When you create an Amazon Elastic VMware Service environment, the value that you choose sets the deployment mode and, in EVS-deployed mode, the VMware Cloud Foundation (VCF) version. Choose the mode and the version first, because they decide who installs VCF, which instance types you can use, and which ESX builds your hosts can run.

For the supported versions, instance types, and ESX builds in one table, see [Supported VCF versions by instance type](versions-provided.md#current-vcf-versions).

## Choose a VCF version and deployment mode
<a name="plan-versions-mode"></a>

When you create an environment, the value that you choose sets the deployment mode, as the following table shows.


| Deployment mode | Value that you choose | Who installs VCF | 
| --- | --- | --- | 
| Self-deployed |  `SELF_DEPLOYED`  | You do. Amazon EVS creates the VLAN subnets. You add the hosts and install VCF yourself. You can deploy VCF 5.x or VCF 9.x in this mode. Amazon EVS provides VCF 9.0 and 9.1 as the VCF 9.x versions. | 
| EVS-deployed |  `VCF-5.2.2` or `VCF-5.2.1`  | Amazon EVS installs VCF 5.2.x when it creates the environment. EVS-deployed mode doesn’t support VCF 9.x deployments. | 

For a side-by-side comparison of the two modes, see [Differences between deployment modes](deployment-mode-differences.md). For the steps in each mode, see [Deploy in Self-deployed mode](getting-started-self-deployed.md) and [Deploy in EVS-deployed mode](evs-deployed-overview.md).

Some instance types are available only with some VCF versions. For example, diskless hosts are available only with VCF 9.x. Check the table before you choose an instance type. For more information, see [Choose instance types](plan-instance-types.md).

Some VCF versions have the status `RESTRICTED`. To use a restricted version, you must request access first. For more information, see [Request access to restricted VCF versions](versions-provided.md#version-restrictions).

Amazon EVS doesn’t provide every VCF and ESX version that Broadcom releases. Before you choose a version, check that the other VMware products that you plan to use support it in the [Broadcom Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability?col=1).

If you plan to deploy VCF 9.x with the EVS Deployment Orchestrator (EDO), check which VCF versions EDO supports before you choose. EDO is a tool in the [Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs). For more information, see [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md).

## Choose an ESX version
<a name="plan-versions-esx"></a>

Each VCF version has a default ESX version that is based on the Broadcom VCF Bill of Materials (BOM). How you choose the ESX version depends on when you choose it.

 **When you create an environment**   
You can’t choose a specific ESX version. Amazon EVS applies the default ESX version for the VCF version that you select.

 **When you add a host**   
You can choose any ESX version that Amazon EVS provides for the instance type of the host. If you don’t choose one, Amazon EVS uses the default ESX version. For the `SELF_DEPLOYED` value, `get-versions` reports the default as `defaultEsxVersion`.

 **After you add a host**   
You can upgrade its ESX version only with vCenter Lifecycle Manager.

Confirm that the ESX version that you choose is compatible with your VCF release in the Broadcom Interoperability Matrix. For more information, see [ESX version considerations](versions-provided.md#esx-versions).

## Check which versions are available to you
<a name="plan-versions-check"></a>

The versions and builds available to your account can differ from the table, for example when a version is restricted. You can check them in two ways.
+ In the Amazon EVS console, the create environment wizard shows the VCF versions, and the add host wizard shows the ESX versions.
+ With the AWS CLI, run the `get-versions` command for the Region where you plan to deploy.

In the following command, replace `<region-code>` with the Region where you plan to deploy.

```bash
aws evs get-versions --region <region-code>
```

The response lists each VCF version with its status, default ESX version, and instance types. It also lists the ESX versions that you can choose for each instance type. For an example response, see [Check what is available to you](versions-provided.md#check-provided-versions).

Next, choose an instance type. See [Choose instance types](plan-instance-types.md).