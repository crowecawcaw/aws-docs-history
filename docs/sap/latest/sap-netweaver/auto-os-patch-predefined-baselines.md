

# Predefined patch baselines
<a name="auto-os-patch-predefined-baselines"></a>

Patch manager provides predefined patch baselines for each of the supported operating systems. If your patching requirement patches the predefined baseline configuration, you might be able to use a predefined patch baseline for operating system patching. Alternatively, you can create your own custom patch baselines. This gives you greater control over which patches are approved or rejected for your environment.

For information about predefined patch baselines, see [Viewing AWS predefined patch baselines (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/view-predefined-patch-baselines.html) in the * AWS Systems Manager User Guide*.

**Note**  
SUSE Linux Enterprise Server for SAP Applications and Red Hat Enterprise Linux for SAP Applications require custom patch baselines.

The following table is a subset of the predefined patch baselines in the Patch Manager documentation. To view the full list of predefined patch baselines, see [About predefined baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baselines.html#patch-manager-baselines-pre-defined) in the * AWS Systems Manager User Guide*. The predefined patch baselines listed here are applicable to SAP.


| Name | Supported operating system | Details | 
| --- | --- | --- | 
|  ` AWS-OracleLinuxDefaultPatchBaseline`  | Oracle Linux | Approves all operating system patches that are classified as "Security" and that have a severity level of "Important" or "Moderate". Also approves all patches that are classified as "Bugfix" 7 days after release. Patches are auto-approved 7 days after they are released or updated.¹ | 
|  ` AWS-RedHatDefaultPatchBaseline`  | Red Hat Enterprise Linux (RHEL) | Approves all operating system patches that are classified as "Security" and that have a severity level of "Critical" or "Important". Also approves all patches that are classified as "Bugfix". Patches are auto-approved 7 days after they are released or updated.¹ | 
|  ` AWS-SuseDefaultPatchBaseline`  | SUSE Linux Enterprise Server (SLES) | Approves all operating system patches that are classified as "Security" and with a severity of "Critical" or "Important". Patches are auto-approved 7 days after they are released or updated.¹ | 
|  ` AWS-DefaultPatchBaseline`  | Windows Server | Approves all Windows Server operating system patches that are classified as "CriticalUpdates" or "SecurityUpdates" and that have an MSRC severity of "Critical" or "Important". Patches are auto-approved 7 days after they are released or updated.¹ | 

¹ For Amazon Linux and Amazon Linux 2, the 7-day wait before patches are auto-approved is calculated from an `Updated Date` value in `updateinfo.xml`, not a `Release Date` value. Various factors can affect the `Updated Date` value. Other operating systems handle release and update dates differently. For information to help you avoid unexpected results with auto-approval delays, see [How package release dates and update dates are calculated](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-how-it-works-release-dates.html) in the * AWS Systems Manager User Guide*.