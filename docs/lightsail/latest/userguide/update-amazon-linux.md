

# Update Amazon Linux on Lightsail instances
<a name="update-amazon-linux"></a>

This guide explains how to update Amazon Lightsail instances created from the Amazon Linux 2023 (AL2023) or Amazon Linux 2 blueprints. The AL2023 blueprint runs Linux kernel 6.1, and the Amazon Linux 2 blueprint runs Linux kernel 4.14. To protect these instances from security vulnerabilities, keep their operating system and kernel up to date.

**Important**  
**CVE-2026-98432**: A flaw in the Linux kernel's IPv4 networking code can let a remote attacker crash the instance, or possibly corrupt memory, by sending specially timed TCP traffic. Amazon Linux rates this issue Important, with a CVSS v3 score of 8.1. To address it, update the kernel to the following version or later, and then reboot the instance:  
AL2023 (kernel 6.1): `6.1.189-236.400.amzn2023`
Amazon Linux 2 (kernel 4.14): `4.14.355-287.758.amzn2`
Amazon Linux 2 (kernel 5.10, if you installed it yourself): `5.10.271-272.1121.amzn2`
For details, see [CVE-2026-98432](https://explore.alas.aws.amazon.com/CVE-2026-98432.html) in the Amazon Linux Security Center.

Lightsail does not update the operating system on your instances after you create them. You are responsible for installing operating system and kernel updates. For more information, see [Update your Lightsail instances and containers](amazon-lightsail-update-management.md).

Every kernel update requires a reboot. Plan the update for a time when a short interruption is acceptable.

This page contains the following sections:
+ [Before you begin](#update-amazon-linux-before-you-begin)
+ [Update AL2023 instances](#update-amazon-linux-2023)
+ [Update Amazon Linux 2 instances](#update-amazon-linux-2)
+ [Additional resources](#update-amazon-linux-resources)

## Before you begin
<a name="update-amazon-linux-before-you-begin"></a>

Before you update your instance, create a snapshot of it. If something goes wrong during the update, you can create a new instance from the snapshot. For more information, see [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md).

To check which kernel your instance runs, connect to it using SSH and run the following command. For instructions on connecting, see [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md).

```
uname -r
```

The output shows the kernel version. For example, `6.1.189-236.400.amzn2023.x86_64` on AL2023, or `4.14.355-287.758.amzn2.x86_64` on Amazon Linux 2.

## Update AL2023 instances
<a name="update-amazon-linux-2023"></a>

AL2023 uses *deterministic upgrades*. A deterministic upgrade means that each instance stays on the AL2023 release that it was created from. A release is a fixed, versioned set of package repositories, so the same command installs the same package versions every time. Because of this, `sudo dnf upgrade` on its own only installs updates from your current release. It doesn't install packages from newer releases, including kernel security fixes. To get the latest fixes, upgrade to the latest release with the `--releasever` option. For more information, see [Deterministic upgrades through versioned repositories](https://docs.aws.amazon.com/linux/al2023/ug/deterministic-upgrades.html) in the *AL2023 User Guide*.

The Lightsail AL2023 blueprint runs kernel 6.1. The following steps update kernel 6.1 to its latest version and keep your instance on kernel 6.1.

1. Create a snapshot of your instance as a backup.

1. Connect to your instance using SSH. For more information, see [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md).

1. Check whether a newer AL2023 release is available:

   ```
   sudo dnf check-release-update
   ```

   If a newer release is available, the output lists it and the command to upgrade to it.

1. Upgrade all packages, including the kernel, to the latest release:

   ```
   sudo dnf upgrade --releasever=latest
   ```

   Review the list of packages, and enter **y** to continue.

1. Reboot the instance to load the new kernel:

   ```
   sudo reboot
   ```

1. After the instance restarts, connect to it again and confirm the kernel version:

   ```
   uname -r
   ```
**Note**  
To address CVE-2026-98432, the version should be `6.1.189-236.400.amzn2023` or later.

To install only the kernel update and the release named in the security advisory, run the command from the advisory instead. For CVE-2026-98432, see [ALAS2023-2026-3365](https://alas.aws.amazon.com/AL2023/ALAS2023-2026-3365.html) on the Amazon Linux Security Center website.

**Note**  
AL2023 also offers kernels 6.12 and 6.18 as separate packages (`kernel6.12` and `kernel6.18`). The steps on this page don't install them. If you want to change to a newer kernel version, see [Updating the Linux kernel on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/kernel-update.html) in the *AL2023 User Guide*, and test your workloads before you change.

## Update Amazon Linux 2 instances
<a name="update-amazon-linux-2"></a>

The Lightsail Amazon Linux 2 blueprint runs kernel 4.14. Unlike AL2023, Amazon Linux 2 installs the latest available packages when you run `yum update`. You don't need to choose a release.

**Note**  
Amazon Linux 2 has reached the end of standard support. We recommend that you move your workloads to an instance created from the AL2023 blueprint. For more information, see [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/).

1. Create a snapshot of your instance as a backup.

1. Connect to your instance using SSH. For more information, see [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md).

1. Update all packages, including the kernel:

   ```
   sudo yum update
   ```

   Review the list of packages, and enter **y** to continue. To update only the kernel, run `sudo yum update kernel` instead.

1. Reboot the instance to load the new kernel:

   ```
   sudo reboot
   ```

1. After the instance restarts, connect to it again and confirm the kernel version:

   ```
   uname -r
   ```
**Note**  
To address CVE-2026-98432, the version should be `4.14.355-287.758.amzn2` or later. If you changed your instance to kernel 5.10, the version should be `5.10.271-272.1121.amzn2` or later.  
For details about the fix, see [ALAS2-2026-4065](https://alas.aws.amazon.com/AL2/ALAS2-2026-4065.html) for kernel 4.14 and [ALAS2KERNEL-5.10-2026-137](https://alas.aws.amazon.com/AL2/ALAS2KERNEL-5.10-2026-137.html) for kernel 5.10 on the Amazon Linux Security Center website.

## Additional resources
<a name="update-amazon-linux-resources"></a>
+ [CVE-2026-98432 in the Amazon Linux Security Center](https://explore.alas.aws.amazon.com/CVE-2026-98432.html)
+ [Updating the Linux kernel on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/kernel-update.html)
+ [Managing packages and operating system updates in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html)
+ [AL2 supported kernels](https://docs.aws.amazon.com/linux/al2/ug/aml2-kernel.html)
+ [Update your Lightsail instances and containers](amazon-lightsail-update-management.md)
+ [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md)