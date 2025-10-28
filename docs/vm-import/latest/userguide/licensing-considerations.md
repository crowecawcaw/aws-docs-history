# Licensing considerations

We recommend that you review the following licensing considerations appropriate for
the operating system that you wish to import.

###### Topics

- [Licensing considerations for
  Linux/Unix](#licensing-considerations-linux "#licensing-considerations-linux")
- [Licensing considerations for
  Windows](#licensing-considerations-windows "#licensing-considerations-windows")

## Licensing considerations for

Linux/Unix

Linux operating systems support only the `BYOL` license type for a VM
import task.

Migrated Red Hat Enterprise Linux (RHEL) VMs must use Cloud Access (BYOS)
licenses. For more information, see [Red
Hat Cloud Access](https://www.redhat.com/en/technologies/cloud-computing/cloud-access "https://www.redhat.com/en/technologies/cloud-computing/cloud-access") on the Red Hat website.

Migrated SUSE Linux Enterprise Server VMs must use SUSE Public Cloud Program
(BYOS) licenses. For more information, see [SUSE Public Cloud Program—Bring Your Own Subscription](https://www.suse.com/media/flyer/suse_subscription_portability_in_the_public_cloud_flyer.pdf "https://www.suse.com/media/flyer/suse_subscription_portability_in_the_public_cloud_flyer.pdf").

## Licensing considerations for

Windows

Windows Server operating systems support either the `BYOL` or
`AWS` license type. Windows client operating systems (such as Windows 10) support only BYOL licenses.

By default, an AWS license is used when you create a VM import task if the VM
has a Windows Server OS. Otherwise, a BYOL license is used.

The following rules apply when you use your BYOL Microsoft license, either through
MSDN or [Windows Software Assurance Per User](https://download.microsoft.com/download/5/c/7/5c727885-ec15-4920-818b-4d140ec6c38a/Windows_SA_per_User_at_a_Glance.pdf "https://download.microsoft.com/download/5/c/7/5c727885-ec15-4920-818b-4d140ec6c38a/Windows_SA_per_User_at_a_Glance.pdf"):

- Your BYOL instances are priced at the prevailing Amazon EC2 Linux instance
  pricing, provided that you meet the following conditions:
  - Run on a Dedicated Host ([Dedicated
    Hosts](../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md")).
  - Launch from VMs sourced from software binaries provided by you
    using AWS VM Import/Export, which are subject to the current terms and
    abilities of AWS VM Import/Export.
  - Designate the instances as BYOL instances.
  - Run the instances within your designated AWS Regions, and where
    AWS offers the BYOL model.
  - Activate using Microsoft keys that you provide or which are used
    in your key management system.

- You must account for the fact that when you start an Amazon EC2 instance, it
  can run on any one of many servers within an Availability Zone. This means
  that each time you start an Amazon EC2 instance (including a stop/start), it may
  run on a different server within an Availability Zone. You must account for
  this fact in light of the limitations on license reassignment as described
  in Microsoft's document [Volume Licensing Product Terms](https://www.microsoftvolumelicensing.com/Downloader.aspx?documenttype=PT&lang=English&usg=AOvVaw3eaE46-Gb5hQg3r8RIv8S7 "https://www.microsoftvolumelicensing.com/Downloader.aspx?documenttype=PT&lang=English&usg=AOvVaw3eaE46-Gb5hQg3r8RIv8S7"), or consult your specific use
  rights to determine if your rights are consistent with this usage.
- You must be eligible to use the BYOL program for the applicable Microsoft
  software under your agreements with Microsoft, for example, under your MSDN
  user rights or under your Windows Software Assurance Per User Rights. You
  are solely responsible for obtaining all required licenses and for complying
  with all applicable Microsoft licensing requirements, including the PUR/PT.
  Further, you must have accepted Microsoft's End User License Agreement
  (Microsoft EULA), and by using the Microsoft Software under the BYOL
  program, you agree to the Microsoft EULA.
- AWS recommends that you consult with your own legal and other advisers
  to understand and comply with the applicable Microsoft licensing
  requirements. Usage of the Services (including usage of the
  **licenseType** parameter and **BYOL**
  flag) in violation of your agreements with Microsoft is not authorized or
  permitted.

For more information, see _[Generating Windows Server and SQL Server on Amazon EC2 estimates](../../../pricing-calculator/latest/userguide/windows-workload-estimates.md "../../../pricing-calculator/latest/userguide/windows-workload-estimates.md")
in the AWS Pricing Calculator User Guide_.
