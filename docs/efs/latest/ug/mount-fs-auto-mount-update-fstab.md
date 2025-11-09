# Enabling automatic

mounting on existing EC2 Linux instances

The `/etc/fstab` file contains information about file systems. The
command `mount -a`, which runs during instance start-up, mounts all the file
systems listed in `/etc/fstab`. In this procedure, you will manually
update the `/etc/fstab` on an Amazon EC2 Linux instance so that the instance
uses the EFS mount helper to automatically remount an EFS file system
when the instance restarts.

###### Note

EFS file systems do not support automatic mounting using
`/etc/fstab` with the EFS mount helper on EC2 Mac instances
running macOS Big Sur or Monterey. Instead, you can use [NFS with /etc/fstab](nfs-automount-efs.md "nfs-automount-efs.md") to automatically mount your file system
on EC2 Mac instances running macOS Big Sur and Monterey.

This method uses the EFS mount helper to mount the file system. The mount
helper is part of the `amazon-efs-utils` set of tools.

The `amazon-efs-utils` tools are available for installation on Amazon
Linux and Amazon Linux 2 Amazon Machine Images (AMIs). For more information about
`amazon-efs-utils`, see [Installing the Amazon EFS client](using-amazon-efs-utils.md "using-amazon-efs-utils.md"). If you are using another Linux distribution, such
as Red Hat Enterprise Linux (RHEL), manually build and install
`amazon-efs-utils`. For more information, see [Installing the Amazon EFS client on other Linux
distributions](installing-amazon-efs-utils.md#installing-other-distro "installing-amazon-efs-utils.md#installing-other-distro").

## Prerequisites

The following requirements need to be in place before you can successfully implement
this procedure:

- You have already created the EFS file system that you want to be automatically
  remounted. For more information, see [Quick create using the console](creating-using-create-fs.md#gs-step-two-create-efs-resources "creating-using-create-fs.md#gs-step-two-create-efs-resources").
- You have already created the EC2 Linux instance that you want to configure to
  automatically remount an EFS file system.
- The EFS mount helper is installed on the EC2 Linux instance. For more information, see
  [Installing the Amazon EFS client](using-amazon-efs-utils.md "using-amazon-efs-utils.md").

## Update the /etc/fstab file

Perform the following steps to update the /etc/fstab on an EC2 Linux instance so
that the instance uses the EFS mount helper to automatically remount an EFS
file system when the instance restarts.

###### To update the /etc/fstab file on your EC2 instance

1. Connect to your EC2 instance. For more information, see [Connect to your
   EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
   _Amazon EC2 User Guide_.
2. Open the `/etc/fstab` file in
   an editor.
3. For automatic mounting using either IAM authorization or an EFS access
   point:
   - To automatically mount with IAM authorization to an EC2 instance that
     has an instance profile, add the following line to the
     `/etc/fstab` file.

   ```
   `file-system-id`:/ `efs-mount-point` efs _netdev,noresvport,tls,iam 0 0
   ```

   - To automatically mount with IAM authorization to a Linux instance using a credentials file, add the following line to the `/etc/fstab` file.

   ```
   `file-system-id`:/ `efs-mount-point` efs _netdev,noresvport,tls,iam,awsprofile=`namedprofile` 0 0
   ```

   - To automatically mount a file system using an EFS access point, add
     the following line to the `/etc/fstab` file.

   ```
   `file-system-id`:/ `efs-mount-point` efs _netdev,noresvport,tls,accesspoint=`access-point-id` 0 0
   ```

###### Warning

Use the `_netdev` option, used to identify network file systems, when
mounting your file system automatically. If `_netdev` is missing, your
EC2 instance might stop responding. This result is because network file
systems need to be initialized after the compute instance starts its networking. For
more information, see [Automatic mounting fails and the instance is
unresponsive](troubleshooting-efs-mounting.md#automount-fails "troubleshooting-efs-mounting.md#automount-fails").

For more information, see [Mounting with IAM authorization](mounting-IAM-option.md "mounting-IAM-option.md") and [Mounting with EFS access points](mounting-access-points.md "mounting-access-points.md"). 4. Save the changes to the file.

###### Note

In some cases, your EC2 instance might need to start regardless of the status
of your mounted EFS file system. In such cases, add the `nofail`
option to your file system's entry in your `/etc/fstab` file.

The line of code you added to the `/etc/fstab` file does the
following.

| Field                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ``file-system-id`:/` | The ID for your EFS file system. You can get this ID from the<br>console or programmatically from the CLI or an AWS SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `efs-mount-point`    | The mount point for the EFS file system on your EC2<br>instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `efs`                | The type of file system. When you're using the mount helper, this type is<br>always `efs`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `mount options`      | Mount options for the file system. This is a comma-separated list of the<br>following options:<br>• `_netdev` – This option tells the operating system that the<br>file system resides on a device that requires network access. This option<br>prevents the instance from mounting the file system until the network has been<br>enabled on the client.<br>• `noresvport` – Tells the NFS client to use a new<br>Transmission Control Protocol (TCP) source port when a network connection<br>is reestablished. Doing this helps make sure that the EFS file<br>system has uninterrupted availability after a network recovery<br>event.<br>• `tls` – Enables<br>encryption of data in transit.<br>• `iam` – Use this option to mount with IAM authorization to an EC2<br>instance that has an instance profile. Using the `iam` mount<br>option requires also using the `tls` option. For more<br>information, see [Using IAM to control access to file<br>systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md").<br>• `awsprofile=`namedprofile`` –<br>Use this option with the `iam` and `tls` options to<br>mount with IAM authorization to a Linux instance using a credentials<br>file. For more information about EFS access points, see [Using IAM to control access to file<br>systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md").<br>• `accesspoint=`access-point-id``<br>– Use this option with the `tls` option to mount using<br>an EFS access point. For more information about EFS<br>access points, see [Working with access points](efs-access-points.md "efs-access-points.md"). |
| `0`                  | A nonzero value indicates that the file system should be backed up by<br>`dump`. For EFS, this value should be<br>`0`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `0`                  | The order in which `fsck` checks file systems at boot. For<br>EFS file systems, this value should be `0` to indicate<br>that `fsck` should not run at start-up.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
