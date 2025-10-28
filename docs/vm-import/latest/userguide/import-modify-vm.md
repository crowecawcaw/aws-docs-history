# Programmatic modifications made to VMs by VM Import/Export

When importing a VM using the `ImportImage` API, AWS modifies the file
system and adds drivers to make the imported VM bootable. When writing a modified
file, AWS retains the original file at the same location under a new name. The
following actions may occur:

###### General

- For parity with images provided by AWS, the AWS Systems Manager client is installed on
  the VM.

###### Windows

- Modifying registry settings to make the VM bootable.

###### Linux

- Installing Citrix PV drivers either directly in OS or modify initrd/initramfs
  to contain them.
- Modifying network scripts to replace static IPs with dynamic IPs.
- Modifying `/etc/fstab`, commenting out invalid entries and
  replacing device names with UUIDs. If no matching UUID can be found for a
  device, the `nofail` option is added to the device description. You
  must correct the device naming and remove `nofail` after import. As a
  best practice when preparing your VMs for import, we recommend that you specify
  your VM disk devices by UUID rather than device name.

Entries in `/etc/fstab` that contain non-standard file
system types (cifs, smbfs, vboxsf, sshfs, etc.) are disabled.

- Modifying grub bootloader settings such as the default entry and
  timeout.

## Import VM without modifications

If you need to import a VM without programmatic modifications, we recommend that you
follow these steps instead of using `ImportImage`.

###### Important

If you use this process, AWS does not do any post-import validations to ensure
that the image is bootable. It is your responsibility to ensure that you properly
prepare your VM for exporting.

###### To import a VM without modifications

1. Prepare your VM for export. For more information, see [Configurations to export VMs from your virtualization
   environment](prepare-vm-image.md "prepare-vm-image.md").
2. Export the boot disk for your VM in one of the following file formats: VHD/VHDX,
   VMDK, or raw. For more information, refer to the documentation for your virtualization
   environment.
3. Use the [put-object](../../../cli/latest/reference/s3api/put-object.md "../../../cli/latest/reference/s3api/put-object.md") command to upload the exported boot disk file to an Amazon S3 bucket in
   the Region where you want to create the image.
4. Use the [import-snapshot](../../../cli/latest/reference/ec2/import-snapshot.md "../../../cli/latest/reference/ec2/import-snapshot.md") command to import the boot disk as a snapshot. For more
   information about importing a snapshot, see [Import a disk as an EBS snapshot using VM Import/Export](vmimport-import-snapshot.md "vmimport-import-snapshot.md").

###### Note

You can monitor the progress of the import snapshot task using the [describe-import-snapshot-tasks](../../../cli/latest/reference/ec2/describe-import-snapshot-tasks.md "../../../cli/latest/reference/ec2/describe-import-snapshot-tasks.md") command.

Make a note of the snapshot ID returned by the command. You'll need it for the
next step. 5. Use the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command to register a new AMI, and specify the snapshot from
the previous step as the root device volume.

Make a note of the image ID returned by the command. You'll need it for the
next step. 6. After the AMI reaches the `available` state, you can use it to launch
instances.
