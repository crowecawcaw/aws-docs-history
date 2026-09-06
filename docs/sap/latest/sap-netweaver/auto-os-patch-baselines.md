

# Configure patch baselines
<a name="auto-os-patch-baselines"></a>

Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. For information about patch baselines, see [About patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-baselines.html) in the * AWS Systems Manager User Guide*. You can use predefined patch baselines or create custom patch baselines. The sections below contain instructions on how to use both.

For information about patch baselines that is specific to Linux, see [How patch baseline rules work on Linux-based systems](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-how-it-works-linux-rules.html) in the * AWS Systems Manager User Guide*.

For information about the differences between Linux and Windows patching, see [Key differences between Linux and Windows patching](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-differences.html) in the * AWS Systems Manager User Guide*. If your system landscape has a combination of Windows Server and Linux operating systems, such as Windows Server for SAP application servers and Linux for database servers, you can define a baseline for each operating system type.