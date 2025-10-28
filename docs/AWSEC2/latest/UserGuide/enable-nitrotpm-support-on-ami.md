# Enable a Linux AMI for NitroTPM

To enable NitroTPM for an instance, you must launch the instance using an AMI
with NitroTPM enabled. You must configure your Linux AMI with NitroTPM support
when you register it. You can't configure NitroTPM support later on.

For the list of Windows AMIs that are preconfigured for NitroTPM support, see
[Requirements for using NitroTPM with Amazon EC2
instances](enable-nitrotpm-prerequisites.md "enable-nitrotpm-prerequisites.md").

You must create an AMI with NitroTPM configured by using the [RegisterImage](../APIReference/API_RegisterImage.md "../APIReference/API_RegisterImage.md") API. You can't use the Amazon EC2 console or VM Import/Export.

###### To enable a Linux AMI for NitroTPM

1. Launch a temporary instance with your required Linux AMI. Note the ID of its
   root volume, which you can find in the console on the **Storage**
   tab for the instance.
2. After the instance reaches the `running` state, create a snapshot
   of the instance's root volume. For more information, see [Create a snapshot of an EBS volume](../../../ebs/latest/userguide/ebs-create-snapshot.md "../../../ebs/latest/userguide/ebs-create-snapshot.md").
3. Register the snapshot you created as an AMI. In the block device mapping,
   specify the snapshot that you created for the root volume.

The following is an example [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command.
For `--tpm-support`, specify `v2.0`.
For `--boot-mode`, specify `uefi`.

```
aws ec2 register-image \
    --name `my-image` \
    **--boot-mode uefi** \
    --architecture x86_64 \
    --root-device-name /dev/xvda \
    --block-device-mappings DeviceName=/dev/xvda,Ebs={SnapshotId=`snap-0abcdef1234567890`} \
    **--tpm-support v2.0**
```

The following is an example for the [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") cmdlet.

```
$block = @{SnapshotId=`snap-0abcdef1234567890`}
Register-EC2Image `
    -Name `my-image` `
    -Architecture "x86_64" `
    -RootDeviceName /dev/xvda `
    -BlockDeviceMapping @{DeviceName="/dev/xvda";Ebs=$block} `
    -BootMode Uefi `
    -TpmSupport V20
```

4. Terminate the temporary instance that you launched in step 1.
