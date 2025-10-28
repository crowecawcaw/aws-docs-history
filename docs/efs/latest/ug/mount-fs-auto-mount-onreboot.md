# Automatically mounting EFS file systems

You can use the EFS mount helper or NFS to configure an Amazon EC2 instance to automatically
mount an EFS file system when the instance starts.

- Using the EFS mount helper:
  - Attach an EFS file system when you create a new EC2 Linux
    instance using the EC2 launch instance wizard.
  - Update the EC2 `/etc/fstab` file with an entry for the
    EFS file system.

- Using [NFS without the
  EFS mount helper](nfs-automount-efs.md "nfs-automount-efs.md") to update the EC2 `/etc/fstab` file, for
  EC2 Linux and Mac instances.

###### Note

The EFS mount helper does not support automatic mounting on EC2 Mac instances
running macOS Big Sur or Monterey. Instead, you can use [NFS to
configure the /etc/fstab file on an EC2 Mac instance](nfs-automount-efs.md "nfs-automount-efs.md") to automatically mount
an EFS file system.

###### Topics

- [Enabling automatic mounting on new
  EC2 Linux instances](mount-fs-auto-mount-on-creation.md "mount-fs-auto-mount-on-creation.md")
- [Enabling automatic
  mounting on existing EC2 Linux instances](mount-fs-auto-mount-update-fstab.md "mount-fs-auto-mount-update-fstab.md")
- [Enabling automatic mounting
  on EC2 Linux or Mac instances using NFS](nfs-automount-efs.md "nfs-automount-efs.md")
