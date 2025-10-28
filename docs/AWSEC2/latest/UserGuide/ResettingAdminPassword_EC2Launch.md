# Reset Windows admin password for

EC2 instance using EC2Launch

If you have lost your Windows administrator password and are using a Windows Server 2016 or
later AMI, you can use the [EC2Rescue tool](Windows-Server-EC2Rescue.md "Windows-Server-EC2Rescue.md"), which uses the EC2Launch service to generate
a new password.

If you are using a Windows Server 2016 or later AMI that does not include the EC2Launch v2 agent, you can use EC2Launch v2 to generate a new password.

If you are using a Windows Server AMI earlier than Windows Server 2016, see [Reset Windows admin password for
EC2 instance using EC2Config](ResettingAdminPassword_EC2Config.md "ResettingAdminPassword_EC2Config.md").

###### Warning

When you stop an instance, the data on any instance store volumes is erased.
To keep data from instance store volumes, be sure to back it up to persistent storage.

###### Note

If you have disabled the local administrator account on the instance and your instance
is configured for Systems Manager, you can also re-enable and reset your local administrator
password by using EC2Rescue and Run Command. For more information, see [Use EC2Rescue for Windows Server with
Systems Manager Run Command](ec2rw-ssm.md "ec2rw-ssm.md").

###### Note

There is an AWS Systems Manager Automation document that automatically applies the manual steps
necessary to reset the local administrator password. For more information, see [Reset passwords and SSH keys on EC2 instances](../../../systems-manager/latest/userguide/automation-ec2reset.md "../../../systems-manager/latest/userguide/automation-ec2reset.md")
in the _AWS Systems Manager User Guide_.

To reset your Windows administrator password using EC2Launch, you need to do the following:

- [Step 1: Detach the root volume from the
  instance](#resetting-password-ec2launch-step1 "#resetting-password-ec2launch-step1")
- [Step 2: Attach the volume to a temporary
  instance](#resetting-password-ec2launch-step2 "#resetting-password-ec2launch-step2")
- [Step 3: Reset the administrator
  password](#resetting-password-ec2launch-step3 "#resetting-password-ec2launch-step3")
- [Step 4: Restart the original
  instance](#resetting-password-ec2launch-step4 "#resetting-password-ec2launch-step4")

## Step 1: Detach the root volume from the

instance

You can't use EC2Launch to reset an administrator password if the volume on which the password is stored is
attached to an instance as the root volume. You must detach the volume from the original instance before you
can attach it to a temporary instance as a secondary volume.

###### To detach the root volume from the instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance that requires a password reset and choose
   **Instance state**, **Stop instance**.
   After the status of the instance changes to **Stopped**,
   continue with the next step.
4. (Optional) If you have the private key that you specified when you launched
   this instance, continue with the next step. Otherwise, use the following steps
   to replace the instance with a new instance that you launch with a new key
   pair.
   1. Create a new key pair using the Amazon EC2 console. To give your new key
      pair the same name as the one for which you lost the private key, you
      must first delete the existing key pair.
   2. Select the instance to replace. Note the instance type, VPC, subnet,
      security group, and IAM role of the instance.
   3. With the instance selected, choose **Actions**, **Image and templates**,
      **Create image**. Type a name and a description for
      the image and choose **Create image**.
   4. In the navigation pane, choose **AMIs**. Wait for the image status to change to
      **available**. Then, select the image and choose **Launch instance from AMI**.
   5. Complete the fields to launch an instance, making sure to select the same instance type, VPC, subnet,
      security group, and IAM role as the instance to replace, and then
      choose **Launch instance**.
   6. When prompted, choose the key pair that you created for the new
      instance, and then choose **Launch instance**.
   7. (Optional) If the original instance has an associated Elastic IP
      address, transfer it to the new instance. If the original instance has
      EBS volumes in addition to the root volume, transfer them to the new
      instance.

5. Detach the root volume from the original instance as follows:
   1. Select the original instance and choose the **Storage** tab.
      Note the name of the root device under **Root device name**.
      Find the volume with this device name under **Block devices**,
      and note the volume ID.
   2. In the navigation pane, choose **Volumes**.
   3. In the list of volumes, select the volume that you noted as the root device,
      and choose **Actions**, **Detach Volume**.
      After the volume status changes to **available**, continue
      with the next step.

6. If you created a new instance to replace your original instance, you can
   terminate the original instance now. It's no longer needed. For the
   remainder of this procedure, all references to the original instance apply to
   the new instance that you created.

## Step 2: Attach the volume to a temporary

instance

Next, launch a temporary instance and attach the volume to it as a secondary volume. This is the instance you
use to run EC2Launch.

###### To launch a temporary instance and attach the volume

1. Launch the temporary instance as follows:
   1. In the navigation pane, choose **Instances**, choose **Launch instances**, and then select an AMI.

   ###### Important

   To avoid disk signature collisions, you must select an AMI for a
   different version of Windows. For example, if the original instance
   runs Windows Server 2019, launch the temporary instance using the
   base AMI for Windows Server 2016. 2. Leave the default instance type and choose **Next: Configure
   Instance Details**. 3. On the **Configure Instance Details** page, for
   **Subnet**, select the same Availability Zone as
   the original instance and choose **Review and
   Launch**.

   ###### Important

   The temporary instance must be in the same Availability Zone as
   the original instance. If your temporary instance is in a different
   Availability Zone, you can't attach the original instance's root
   volume to it. 4. On the **Review Instance Launch** page, choose
   **Launch**. 5. When prompted, create a new key pair, download it to a safe location
   on your computer, and then choose **Launch
   Instances**.

2. Attach the volume to the temporary instance as a secondary volume as
   follows:
   1. In the navigation pane, choose **Volumes**, select the
      volume that you detached from the original instance, and then choose
      **Actions**, **Attach Volume**.
   2. In the **Attach Volume** dialog box, for
      **Instances**, start typing the name or ID of your
      temporary instance and select the instance from the list.
   3. For **Device**, type `xvdf` (if
      it isn't already there), and choose **Attach**.

## Step 3: Reset the administrator

password

Next, connect to the temporary instance and use EC2Launch to reset the administrator password.

###### To reset the administrator password

1. Connect to the temporary instance and use the EC2Rescue for Windows Server tool on
   the instance to reset the administrator password as follows:
   1. Download the [EC2Rescue for Windows Server](https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip "https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip") zip file, extract the contents, and
      run **EC2Rescue.exe**.
   2. On the **License Agreement** screen, read the license
      agreement, and, if you accept the terms, choose **I
      Agree**.
   3. On the **Welcome to EC2Rescue for Windows Server** screen,
      choose **Next**.
   4. On the **Select mode** screen, choose
      **Offline instance**.
   5. On the **Select a disk** screen, select the
      **xvdf** device and choose
      **Next**.
   6. Confirm the disk selection and choose **Yes**.
   7. After the volume has loaded, choose **OK**.
   8. On the **Select Offline Instance Option** screen,
      choose **Diagnose and Rescue**.
   9. On the **Summary** screen, review the information and
      choose **Next**.
   10. On the **Detected possible issues** screen, select
       **Reset Administrator Password** and choose
       **Next**.
   11. On the **Confirm** screen, choose
       **Rescue**, **OK**.
   12. On the **Done** screen, choose
       **Finish**.
   13. Close the EC2Rescue for Windows Server tool, disconnect from the temporary
       instance, and then return to the Amazon EC2 console.

2. Detach the secondary (`xvdf`) volume from the temporary instance as
   follows:
   1. In the navigation pane, choose **Instances** and
      select the temporary instance.
   2. On the **Storage** tab for the temporary instance, note
      the ID of the EBS volume listed as **xvdf**.
   3. In the navigation pane, choose **Volumes**.
   4. In the list of volumes, select the volume noted in the previous step,
      and choose **Actions**, **Detach
      Volume**. After the volume status changes to
      **available**, continue with the next step.

## Step 4: Restart the original

instance

After you have reset the administrator password using EC2Launch, reattach the volume to the original instance as
the root volume and connect to the instance using its key pair to retrieve the administrator password.

###### To restart the original instance

1. Reattach the volume to the original instance as follows:
   1. In the navigation pane, choose **Volumes**, select the volume
      that you detached from the temporary instance, and then choose **Actions**,
      **Attach Volume**.
   2. In the **Attach Volume** dialog box, for
      **Instances**, start typing the name or ID of your
      original instance and then select the instance.
   3. For **Device**, type
      `/dev/sda1`.
   4. Choose **Attach**. After the volume status changes to
      `in-use`, continue to the next step.

2. In the navigation pane, choose **Instances**. Select the
   original instance and choose **Instance state**,
   **Start instance**. After the
   instance state changes to `Running`, continue to the next
   step.
3. Retrieve your new Windows administrator password using the private key for the
   new key pair and connect to the instance. For more information, see [Connect to your Windows instance using RDP](connecting_to_windows_instance.md "connecting_to_windows_instance.md").
4. (Optional) If you have no further use for the temporary instance, you can
   terminate it. Select the temporary instance, and choose
   **Instance State**,
   **Terminate instance**.
