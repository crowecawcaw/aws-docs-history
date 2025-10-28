# Bring Your Own Windows desktop licenses in WorkSpaces

If your licensing agreement with Microsoft allows it, you can bring and deploy your Windows 10 or 11
desktop on your WorkSpaces. To do this, you must enable Bring Your Own License (BYOL)
and provide a Windows 10 or 11 license that meets the requirements below. For more information about
using Microsoft software on AWS, see
[Amazon Web Services and Microsoft](https://aws.amazon.com/windows/faq/ "https://aws.amazon.com/windows/faq/").

To stay compliant with Microsoft licensing terms, AWS runs your BYOL WorkSpaces
on hardware that is dedicated to you in the AWS Cloud. By bringing your own license, you can
provide a consistent experience for your users. For more information, see [WorkSpaces Pricing](https://aws.amazon.com/workspaces/pricing/ "https://aws.amazon.com/workspaces/pricing/").

###### Important

Image creation is not supported on Windows 11 systems that have been upgraded from one
version of Windows 11 to a newer version of Windows 11 (a Windows feature/version
upgrade). For example, a Windows 11 23H2 system which was upgraded to 24H2 cannot be used
to create an image. However, Windows cumulative or security updates are supported by the
WorkSpaces image-creation process.

###### Topics

- [Using Bring Your Own Windows desktop licenses in WorkSpaces](#byol-process "#byol-process")
- [Videos on uploading and creating BYOL images](byol-videos.md "byol-videos.md")
- [Link BYOL accounts in WorkSpaces](link-byol-account.md "link-byol-account.md")
- [Common error messages and their solutions](windows-images-common-errors.md "windows-images-common-errors.md")
- [List of SysPrep error messages and error fixes](images-errors-sysprep.md "images-errors-sysprep.md")

## Using Bring Your Own Windows desktop licenses in WorkSpaces

Use the following steps to import and use your own Windows desktop license in Amazon WorkSpaces

Before you begin, verify the following:

- Your Microsoft licensing agreement allows Windows to run in a virtual hosted
  environment.
- If you will be using non-GPU-enabled bundles (bundles other than Graphics.g4dn, GraphicsPro.g4dn, Graphics, and
  GraphicsPro), verify that you will use a minimum of 50 WorkSpaces per Region. These 50
  WorkSpaces can be any mix of AlwaysOn and AutoStop WorkSpaces. Using a minimum
  of 50 WorkSpaces per Region is a requirement for running your WorkSpaces on dedicated hardware.
  Running your WorkSpaces on dedicated hardware is necessary to comply with Microsoft
  licensing requirements. The dedicated hardware is provisioned on the AWS side,
  so your VPC can stay on default tenancy.

If you plan to use GPU-enabled (Graphics.g4dn, GraphicsPro.g4dn, Graphics, and GraphicsPro) bundles, verify that
you will run a minimum of 4 AlwaysOn or 20 AutoStop GPU-enabled WorkSpaces in a
Region per month on dedicated hardware.

###### Note

    + As part of the image import process, AWS automatically retrieves
     system logs to resolve image import errors, provide troubleshooting
     help, and provide accurate error messages to users.
    + Graphics.g4dn, GraphicsPro.g4dn, Graphics, and GraphicsPro bundles are not available in the Africa (Cape Town) Region and the Israel (Tel Aviv) Region.
    + To run your WorkSpaces in the Africa (Cape Town) Region, you are required to run a minimum of 400 WorkSpaces in the Africa (Cape Town) Region.
    + Value bundles are not available for Windows 11 and WorkSpaces Pools. For more information about migrating your existing value bundle WorkSpaces
     see [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").
    + For the best video conferencing experience we recommend using Power (4 vCPU, 16 GB memory or higher) bundles.

- WorkSpaces can use a management interface in the /16 IP address range. The
  management interface is connected to a secure WorkSpaces management network used for
  interactive streaming. This allows WorkSpaces to manage your WorkSpaces. For more
  information, see [Network interfaces](workspaces-port-requirements.md#network-interfaces "workspaces-port-requirements.md#network-interfaces"). You must reserve a /16 netmask from at
  least one of the following IP address ranges for this purpose:
  - 10.0.0.0/8
  - 100.64.0.0/10
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 198.18.0.0/15

###### Note

    + As you adopt the WorkSpaces service, the available management interface IP address
     ranges frequently change. To determine which ranges are currently available, run the
     [list-available-management-cidr-ranges](../../../cli/latest/reference/workspaces/list-available-management-cidr-ranges.md "../../../cli/latest/reference/workspaces/list-available-management-cidr-ranges.md") AWS Command Line Interface (AWS CLI) command.
    + In addition to the /16 CIDR block that you select, the 54.239.224.0/20 IP
     address range is used for management interface traffic in all AWS Regions.

- Before importing a BYOL customized virtual machine image, [validate your image](#windows_images_run_byol_checker_script "#windows_images_run_byol_checker_script").

WorkSpaces only supports images with UEFI boot mode enabled. For more information on how EC2 Image Builder detects the boot mode,
see [Volume types and file systems supported by VM Import/Export](../../../vm-import/latest/userguide/prerequisites.md#vmimport-volume-types:~:text=Linux/Unix-,Windows,-GUID%20Partition%20Table "../../../vm-import/latest/userguide/prerequisites.md#vmimport-volume-types:~:text=Linux/Unix-,Windows,-GUID%20Partition%20Table") in the _VM Import/Export User Guide_.

#### Windows versions supported for BYOL

Your VM must run one of the following Windows versions:

- Windows 10 Version 22H2 (November 2022 Update)
- Windows 10 Enterprise LTSC 2019 (1809)
- Windows 10 Enterprise LTSC 2021 (21H2)
- Windows 11 Enterprise 23H2 (October 2023 release)
- Windows 11 Enterprise 22H2 (October 2022 release)
- Windows 11 Enterprise 24H2 (October 2024 release)

All supported OS versions support all of the compute types available in the AWS Region
where you're using WorkSpaces. Versions of Windows that are no longer supported by
Microsoft are not guaranteed to work and are not supported by AWS Support.

###### Note

Windows 10 N and Windows 11 N versions are not supported for BYOL at this time.

After you have confirmed that you meet the prerequisites for using Windows BYOL with WorkSpaces,
you need to enable your account to use BYOL images.

1. In the WorkSpaces Console, navigate to the Account Settings page.
2. In the Bring Your Own License (BYOL) section, your account’s BYOL enablement
   status is shown. If the status shows that your account is not enabled, choose the
   **Get Started with BYOL** button.
3. On the BYOL page, choose Enable account for BYOL.

###### Note

Enabling your account for BYOL only applies to a single region. Take note of which
region you are currently in, and if you wish to use a different region, switch to that
region before enabling your account. 4. A popup modal appears confirming that you understand the minimum requirements to use
BYOL WorkSpaces. Confirm your understanding of the requirements and choose Enable account.

###### Note

If you plan to use Graphics WorkSpaces with BYOL, create an AWS Support ticket. Graphics
BYOL enablement is not yet supported through the WorkSpaces Console. 5. In most cases, accounts are automatically enabled. However, some accounts require
additional review. The enablement status is shown on the BYOL page once refreshed. 6. When your account is enabled for BYOL, proceed to the next step.

###### Note

This step only applies to custom VM images that are going to be imported. If you are importing a Windows ISO, you can skip this step.

If you are importing a customized virtual machine image, we recommend you run the WorkSpaces Image Checker tool
to ensure your VM is compatible with WorkSpaces. The Image Checker tool runs a series of tests and can help fix
compatibility issues.

###### To download the Image Compatibility Checker script

Before you download and run the Image Compatibility Checker script, verify that the latest
Windows security updates are installed on your VM. While this script runs, it
disables the Windows Update service.

1. Download the Image Compatibility Checker script .zip file from [ImageCompatibilityChecker.zip](https://tools.amazonworkspaces.com/ImageCompatibilityChecker.zip "https://tools.amazonworkspaces.com/ImageCompatibilityChecker.zip") to your `Downloads` folder.
2. In your `Downloads` folder, create a
   `BYOL` folder.
3. Extract the files from `ImageCompatibilityChecker.zip` and copy them to
   the `Downloads\BYOL` folder.
4. Delete the `Downloads\ImageCompatibilityChecker.zip` folder so that only
   the extracted files remain.
   Check that Windows VM is not enabled with BitLocker.

###### Ensure Windows VM is not enabled with BitLocker

1. Open Powershell as an administrator.
2. Run the following command:

```
manage-bde -off  `DriveLetter`:
```

3. Check the status of BitLocker by running this command:

```
manage-bde -Status  `DriveLetter`:
```

4.  Ensure the values shown match these:

        * **BitLocker Version** – None
        * **Conversion Status** – Fully Decrypted
        * **Percentage Encrypted** – 0.0%
        * **Encryption Method** – None
        * **Protection Status** – Protection Off
        * **Lock Status** – Unlocked

    Perform these steps to run the Image Compatibility Checker script.

###### To run the Image Compatibility Checker script

1. Open Powershell as administrator.
   1. Select the Windows Start button.
   2. Right-click **Windows PowerShell**.
   3. Choose **Run as administrator**.
   4. If prompted by User Account Control, choose **Yes**.

2. At the PowerShell command prompt, change to the directory where the Image Compatibility
   Checker script is located. For example, if the script is located in the
   `Downloads\BYOL` directory, enter the following command
   and press
   **Enter**:

`cd
 C:\Users\`username`\Downloads\BYOL` 3. Enter the following command to update the PowerShell execution policy on the
computer. Doing so allows the Image Compatibility Checker script to run:

`Set-ExecutionPolicy AllSigned` 4. When prompted to confirm whether to change the PowerShell execution policy,
enter **A** to specify Yes to All. 5. Enter the following command to run the Image Compatibility Checker script:

`.\ImageCompatibilityChecker.exe` 6. If a security notification appears, press the **R** key to Run
Once. 7. In the **WorkSpaces Image Validation** dialog box, choose **Run
Tests**. 8. After each test is completed, you can view the status of the test. For any test with a status
of **FAILED**, choose **Info** to display
information about how to resolve the issue that caused the failure. If any tests
display a status of **WARNING**, choose the **Fix All
Warnings** button. 9. If applicable, resolve any issues that cause test failures and warnings, and repeat
[Step 7](#step_begin_tests "#step_begin_tests") and [Step 8](#step_resolve_issues "#step_resolve_issues")
until the VM passes all tests. All failures and warnings must be resolved before
you export the VM. 10. The BYOL script checker generates two log files,
`WorkSpacesImageCompatabilityCheckLog`YYYY-MM-DD_HHmmss`.txt`
and `ImageInfo.text`. These files are located in the
directory that contains the Image Compatibility Checker script files.

###### Tip

Do not delete these files. If an issue occurs, they might be helpful in
troubleshooting. 11. After your VM passes all tests, you get a **Validation
Successful** message.

You will also see a prompt to run Sysprep. Close the prompt and don't run
Sysprep yet. 12. Shut down the VM and export it. For more information, see [Export your VM from its virtualization environment](../../../vm-import/latest/userguide/export-vm-image.md "../../../vm-import/latest/userguide/export-vm-image.md")
in the VM Import/Export User Guide. 13. (Optional) Start the VM and run the Image Compatibility Checker script one more time. All
validations should pass. A screen will pop up again with a button to run
Sysprep. Choose **Run Sysprep**. If Sysprep is successful, your
exported VM that you exported from step 12 can be imported into Amazon Elastic Compute Cloud
(Amazon EC2).

If Sysprep is unsuccessful, review the Sysprep logs in the
`%WINDIR%\System32\Sysprep\Panther` path, roll back to the
exported VM from step 12, resolve the reported issues, and complete step 12
again by exporting the fixed VM. You will then re-run the Image Compatibility Checker script to
ensure the issues have been resolved.

The most common reason for a Sysprep failure is that the Modern AppX Packages
have not been uninstalled for all users. Use the `Remove-AppxPackage`
PowerShell cmdlet to remove the AppX Packages. 14. Import the VM that you exported in step 12 into Amazon EC2.

Perform these steps to import your image and create a WorkSpaces BYOL image:

1. Go to the navigation pane and choose **Images**, then **Import Image**.
2. Follow the steps on the **Import Image** page based on the base image option and type of image you want to import:
   - **VM import** – Imports a virtual machine image that has already been customized. You can import a `VHDX`, `VMDK`, or `OVF` file.
   - **ISO import** – Imports a Windows ISO image that you downloaded from Microsoft and has not been customized.
   - **AMI import** – Imports an existing Amazon EC2 AMI to use as your WorkSpaces BYOL image.

3. Do one of the following:
   - For **VM import** option, upload your file to Amazon S3 then specify the location of the file to import. Note that the S3 bucket you use needs to be in the same region that you intend to deploy BYOL WorkSpaces.
   - For **ISO import**, import a Windows ISO image that you downloaded from Microsoft and has not been customized. Note that the S3 bucket you use needs to be in the same region that you intend to deploy BYOL WorkSpaces.
   - For **AMI import**, specify the AMI ID.

4. Go to **Infrastructure configuration**.

WorkSpaces automatically creates an Amazon EC2 Image Builder pipeline to build your BYOL image. The infrastructure configuration defines how EC2 Image Builder is configured to build your image. You can customize this by using the following settings:

    * **Service defaults** – Creates and uses a default IAM role and policy to build your image.
    * **Use an existing infrastructure configuration** – Offers a selection a customized infrastructure configurations that are set up in the **Amazon EC2 Image Builder**. For more information,
     see [Create an infrastructure configuration](../../../imagebuilder/latest/userguide/create-infra-config.md "../../../imagebuilder/latest/userguide/create-infra-config.md") in the *EC2 Image Builder User Guide*.

5. Go to **Advanced settings** and select if you want to terminate the EC2 build instance if your image encounters import errors.
   - If you choose to terminate the instance on failure, you will not be able to access the instance to debug errors during the image import workflow.
   - If you choose to not terminate the instance, the instance can be used to debug errors but you may incur additional costs for running the EC2 instance.

6. Go to **Image details** to specify the properties of your image: including an image name.
   - **Image Name** – Unique identifier for your image.
   - **Compute type** – Specify if this image should use non-graphics/base hardware or Graphics hardware
   - **OS version** – Choose the Windows operating system version of the image
   - **Semantic version** – Define a semantic version for the image, which will be stored in EC2 Image Builder. For more information,
     see [Semantic versioning in Image Builder](../../../imagebuilder/latest/userguide/ibhow-semantic-versioning.md "../../../imagebuilder/latest/userguide/ibhow-semantic-versioning.md") in the _EC2 Image Builder User Guide_

###### Note

During the BYOL Import process, EC2 Image Builder resources will be created in your AWS account. In order to create the image, a service linked
role named `AWSServiceRoleForImageBuilder` is automatically created if it does not already exist. This role will contain the AWS Managed
Policy [`AWSServiceRoleForImageBuilder`](../../../aws-managed-policy/latest/reference/AWSServiceRoleForImageBuilder.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForImageBuilder.md").
You must also have the [required permissions for VM Import/Export](../../../vm-import/latest/userguide/required-permissions.md "../../../vm-import/latest/userguide/required-permissions.md") to import a custom VM image.

While your image is being created, the status on the **Images** page of the console appears as **Pending**. The BYOL ingestion process takes a minimum of 90 minutes.

Errors that occur when importing your image will show on the **Images** page along with suggested resolutions. Detailed logs are found in Amazon CloudWatch under the **Image Builder** log group created while importing your image. The possible error types are:

- **Image errors** – The image could not be built by EC2 Image Builder. Fix the issues in your virtualization environment and import a new image.
- **Image Builder errors** – There was an error while attempting to build your image. Review the Image Builder logs in Amazon CloudWatch for further details
- **EC2 errors** – There are issues with your image that could not automatically be fixed. To resolve these errors, you can connect to the Amazon EC2 instance if it was set to not terminate on build failure and directly perform fixes. You can then retry import from the Images page.
- **Auto-fixed errors** – These issues have been automatically remediated by WorkSpaces. No further action is required.
  For detailed information on common errors, see [Common error messages and their solutions.](windows-images-common-errors.md "windows-images-common-errors.md")

BYOL WorkSpaces run on dedicated hardware to stay compliant with Microsoft licensing terms. To support this, a BYOL management
interface is created so that a secure connection between your WorkSpaces and the AWS managed WorkSpaces management network. For more information,
see [Network interfaces](workspaces-port-requirements.md#network-interfaces "workspaces-port-requirements.md#network-interfaces").

If you have another AWS account that is enabled for BYOL in the same region, you should use the same management interface
across accounts to reserve fewer IP addresses. To do so, do not choose a management interface IP address range and
see **Link BYOL accounts** below.

###### Choosing a management interface IP address range

1. Return to the BYOL page in **Account Settings**.
2. In the **Choose IP range section**, select the **Choose IP range** button.
3. Enter a search range by providing an IP address range that is available on your network. WorkSpaces returns available /16 netmask IP address ranges that match your search.
4. Choose an available IP address range (shown as CIDR blocks).

###### Note

Once you choose the IP range for your management interface, it cannot be changed.

#### Link BYOL accounts

If you have another AWS account that is enabled for BYOL in the same region, that shares the same payer account,
you should use the same management interface across accounts to reserve fewer IP addresses. Linking accounts also
avoids the need to meet the minimum BYOL requirements for each account, as the minimum requirement is shared across
linked accounts. If you do not have another account already enabled for BYOL under the same payer account, skip
this procedure.

To link to an existing BYOL account, do not select an IP address range.

###### Linking BYOL accounts

1. Log into the AWS account that is already enabled for BYOL WorkSpaces.
2. Navigate to the BYOL page in **Account Settings**.
3. In the **Choose IP range** section, select the **Send Invitation**
   button under the **Account linking** section.
4. Provide the AWS account ID of the account that is not enabled for BYOL and you wish to link to.

###### Note

The two accounts must be using BYOL in the same region. 5. Once the linking invitation is sent, return to the AWS account that is not yet enabled for BYOL.
In the **Account Settings** page you will see a banner notification showing that you have
a pending BYOL account linking invitation. Choose **View invitation** in the banner. 6. Confirm the account linking invitation.

If you wish to use a different management interface for two accounts under the same payer account, contact AWS Support for assistance.

After you create your BYOL image by following the instructions inyou can use the image to create a custom bundle. For information,
see [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md "create-custom-bundle.md").

To use BYOL images for WorkSpaces, you must create a directory for this purpose.

To create a directory for WorkSpaces, see [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md").
Ensure that you choose Enable Dedicated WorkSpaces when creating the directory.

###### Important

If you do not see the Enabled Dedicated WorkSpaces option when registering the directory, make sure you have completed the steps to Enable BYOL in your account and region.

If you've already registered an AWS Managed Microsoft AD directory or an AD Connector directory for WorkSpaces that doesn't run on dedicated hardware, you can set up a new AWS
Managed Microsoft AD directory or AD Connector directory for this purpose. You can also deregister the directory and then register it again as a directory for dedicated WorkSpaces.
To learn more about registering and deregistering an existing AWS Directory Service directory, see Register an existing AWS Directory Service directory with WorkSpaces Personal.

#### Launch your BYOL WorkSpaces Personal

To launch a personal WorkSpaces, see [Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md "create-workspaces-personal.md").

#### Launch your BYOL WorkSpaces Pool

To launch a WorkSpaces Pool, you have to launch a personal WorkSpace, create an image of that personal WorkSpace, then use that image to launch a pool.

###### To create an image for BYOL WorkSpaces Pools

1. Launch a personal WorkSpace with the BYOL image you want to use for your WorkSpaces Pools. For information about how to launch WorkSpaces Personal, see Create a WorkSpace in WorkSpaces Personal.
2. Login in to the personal WorkSpace and make sure all your Windows updates are installed.
3. Update your Amazon EC2 configurations. To update your EC2 configurations using Windows 10, see Install the latest version of EC2Config. To update your EC2 configurations using Windows 11, see Install the latest version of EC2Launch.
4. Add a Windows defender exclusion list. For more information, see Add an exclusion to Windows Security .

Add the following folders to the exclusion list in Windows Defender:

    * `C:\Program Files\Amazon\`
    * `C:\ProgramData\Amazon\*`
    * `C:\Program Files\NICE\`
    * `C:\ProgramData\NICE\`
    * `C:\Program Files (x86)\AWS Tools\*`
    * `C:\Program Files (x86)\AWS SDK for .NET\*`
    * `C:\AWSEUC\` ((This is for the session scrip)

5. Disable Windows update on startup by entering the following command.
6. Open Powershell as administrator.
   1. Select the Windows Start button.
   2. Right-click **Windows PowerShell**.
   3. Choose **Run as administrator**.
   4. If prompted by User Account Control, choose **Yes**.

7. Run following commands:

```
New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" -Force
```

```
New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" -Force
```

```
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" -Name "NoAutoUpdate" -Value 1 -Force
```

8. Reboot the WorkSpace. For more information, see Reboot a WorkSpace in WorkSpaces Personal.

###### Note

We recommend doing the following before you begin creating an image for BYOL WorkSpaces Pools.

    * Remove unnecessary startup applications.
    * Remove or disable unnecessary scheduled tasks. Open the start menu, choose Scheduled tasks, select the tasks you want to disable and then choose Disable.

9. Run image checker after the reboot by entering the following command.

```
C:\Program Files\Amazon\ImageChecker.exe
```

10. Resolve any errors found by the image checker. For more information, see Tips for resolving issues detected by the Image Checker.
11. After all tests have passed the image checker, go back to the WorkSpaces console.
12. In the navigation pane, under WorkSpaces, choose Personal. Choose the BYOL personal WorkSpaces, then choose Actions, Create image.
13. In the navigation pane, choose Images. Under Images, check if the image is created.

You can now launch WorkSpaces Pools with the image you created. For more information about launching WorkSpaces Pools, see Create a WorkSpaces Pool.
