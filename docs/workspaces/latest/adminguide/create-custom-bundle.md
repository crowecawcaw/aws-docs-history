# Create a custom WorkSpaces image and bundle for WorkSpaces Personal

If you've launched a Windows or Linux WorkSpace and have customized it, you can create
a custom image and custom bundles from that WorkSpace.

A _custom image_ contains only the OS, software, and settings for
the WorkSpace. A _custom bundle_ is a combination of
both that custom image and the hardware from which a WorkSpace can be launched.

###### Note

Ensure you wait at least 2 hours after deleting a bundle before creating a
new bundle with the same name.

After you create a custom image, you can build a custom bundle that combines the
custom image and the underlying compute and storage configuration that you select. You
can then specify this custom bundle when you launch new WorkSpaces to ensure that the
new WorkSpaces have the same consistent configuration (hardware and software).

You can use the same custom image to create various custom bundles by selecting
different compute and storage options for each bundle.

###### Important

- If you plan to create an image from a Windows 10 WorkSpace, note that
  image creation is not supported on Windows 10 systems that have been
  upgraded from one version of Windows 10 to a newer version of Windows 10 (a
  Windows feature/version upgrade). However, Windows cumulative or security
  updates are supported by the WorkSpaces image-creation process.
- After January 14, 2020, images cannot be created from public Windows 7
  bundles. You might want to consider migrating your Windows 7 WorkSpaces to
  Windows 10. For more information, see [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").
- The Graphics bundle is no longer supported as of November 30, 2023, and the GraphicsPro bundle reaches end-of-life on October 31, 2025. We
  recommend migrating your WorkSpaces to a supported GPU bundle. For more
  information, see [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").
- GraphicsPro bundle reaches end-of-life on October 31, 2025. We recommend
  migrating your GraphicsPro WorkSpaces to supported GPU bundle before October 31,

2025. For more information, see [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").

- Custom bundle storage volumes can't be smaller than image storage volumes.
- Plus applications bundles with Office 2016 or Office 2019 will no longer be supported after October 14, 2025. We recommend migrating your WorkSpaces bundles with those Office version to use Office 2021. For more information, see, [Manage applications in WorkSpaces Personal](manage-applications.md "manage-applications.md").
  Custom bundles cost the same as the public bundles they are created from. For more
  information about pricing, see [Amazon WorkSpaces Pricing](https://aws.amazon.com/workspaces/pricing/ "https://aws.amazon.com/workspaces/pricing/").

###### Contents

- [Requirements to create Windows
  custom images](#windows_custom_image_requirements "#windows_custom_image_requirements")
- [Requirements to create Linux
  custom images](#linux_custom_image_requirements "#linux_custom_image_requirements")
- [Best practices](#custom_image_best_practices "#custom_image_best_practices")
- [(Optional) Step 1: Specify a custom computer
  name format for your image](#custom_computer_name "#custom_computer_name")
- [Step 2: Run the Image Checker](#run_image_checker "#run_image_checker")
- [Step 3: Create a custom image and
  custom bundle](#create_custom_image_bundle "#create_custom_image_bundle")
- [What's included with Windows WorkSpaces custom
  images](#image_creation_windows "#image_creation_windows")
- [What's included with Linux WorkSpace custom
  images](#image_creation_linux "#image_creation_linux")

## Requirements to create Windows

custom images

###### Note

Windows currently defines 1 GB as 1,073,741,824 bytes. Customers will need to
ensure they have greater than 12,884,901,888 bytes (or 12 GiB) free on C drive
and the user profile is less than 10,737,418,240 bytes (or 10 GiB) to create an
image of a WorkSpace.

- The status of the WorkSpace must be **Available** and its
  modification state must be **None**.
- All applications and user profiles on WorkSpaces images must be compatible
  with Microsoft Sysprep.
- All applications to include in the image must be installed on the
  `C` drive.
- For Windows 7 WorkSpaces, and its total size (files and data) must be less than
  10 GB.
- For Windows 7 WorkSpaces, the `C` drive must have at least
  12 GB of available space.
- All application services running on the WorkSpace must use a local system
  account instead of domain user credentials. For example, you cannot have a
  Microsoft SQL Server Express installation running with a domain user's
  credentials.
- The WorkSpace must not be encrypted. Image creation from an encrypted
  WorkSpace is not currently supported.
- The following components are required in an image. Without these
  components, the WorkSpaces that you launch from the image will not function
  correctly. For more information, see [Required configuration and service components
  for WorkSpaces Personal](required-service-components.md "required-service-components.md").
  - Windows PowerShell version 3.0 or later
  - Remote Desktop Services
  - AWS PV drivers
  - Windows Remote Management (WinRM)
  - Teradici PCoIP agents and drivers
  - STXHD agents and drivers
  - AWS and WorkSpaces certificates
  - Skylight agent

## Requirements to create Linux

custom images

- The status of the WorkSpace must be **Available** and its
  modification state must be **None**.
- All applications to include in the image must be installed outside of the
  user volume (the `/home` directory).
- The root volume (/) should be less than 97% full.
- The WorkSpace must not be encrypted. Image creation from an encrypted
  WorkSpace is not currently supported.
- The following components are required in an image. Without these
  components, the WorkSpaces that you launch from the image will not function
  correctly:
  - Cloud-init
  - Teradici PCoIP or DCV agents and drivers
  - Skylight agent

## Best practices

Before you create an image from a WorkSpace, do the following:

- Use a separate VPC that is not connected to your production
  environment.
- Deploy the WorkSpace in a private subnet and use a NAT instance for
  outbound traffic.
- Use a small Simple AD directory.
- Use the smallest volume size for the source WorkSpace, and then adjust the
  volume size as needed when creating the custom bundle.
- Install all operating system updates (except Windows feature/version
  updates) and all application updates on the WorkSpace. For more information,
  see the [Important note](#important_note "#important_note") at the start of
  this topic.
- Delete cached data from the WorkSpace that shouldn't be included in the
  bundle (for example, browser history, cached files, and browser
  cookies).
- Delete configuration settings from the WorkSpace that shouldn't be
  included in the bundle (for example, email profiles).
- Switch to dynamic IP address settings using DHCP.
- Make sure that you haven't exceeded your quota for WorkSpace images
  allowed in a Region. By default, you're allowed 40 WorkSpace images per
  Region. If you've reached this quota, new attempts to create an image will
  fail. To request a quota increase, use the [WorkSpaces Limits
  form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=workspaces "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=workspaces").
- Make sure that you aren't trying to create an image from an encrypted
  WorkSpace. Image creation from an encrypted WorkSpace is not currently
  supported.
- If you're running any antivirus software on the WorkSpace, disable it
  while you're attempting to create an image.
- If you have a firewall enabled on your WorkSpace, make sure that it isn't
  blocking any necessary ports. For more information, see [IP address and port requirements for
  WorkSpaces Personal](workspaces-port-requirements.md "workspaces-port-requirements.md").
- For Windows WorkSpaces, don't configure any Group Policy Objects (GPOs)
  before image creation.
- For Windows WorkSpaces, do not customize the default user profile
  (`C:\Users\Default`) before creating an image. We
  recommend making any customizations to the user profile through GPOs, and
  applying them after image creation. GPOs can be easily modified or rolled
  back, and are therefore less prone to error than customizations made to the
  default user profile.
- For Linux WorkSpaces, see also the ["Best Practices to Prepare Your Amazon WorkSpaces for Linux
  Images"](../../../whitepapers/latest/workspaces-linux-best-practices/welcome.md "../../../whitepapers/latest/workspaces-linux-best-practices/welcome.md") whitepaper.
- If you want to use smart cards on Linux WorkSpaces with DCV
  enabled, see [Use smart cards for authentication in WorkSpaces Personal](smart-cards.md "smart-cards.md") for
  the customizations that you must make to your Linux WorkSpace before
  creating your image.
- Ensure you update networking dependency drivers like ENA, NVMe, and PV drivers on your WorkSpaces. You should do this at least once every 6 months.
  For more information, see
  [Install or upgrade Elastic Network Adapter (ENA) driver](../../../AWSEC2/latest/WindowsGuide/enhanced-networking-ena.md#ena-adapter-driver-install-upgrade-win "../../../AWSEC2/latest/WindowsGuide/enhanced-networking-ena.md#ena-adapter-driver-install-upgrade-win") ,
  [AWS NVMe drivers for Windows instances](../../../AWSEC2/latest/WindowsGuide/aws-nvme-drivers.md "../../../AWSEC2/latest/WindowsGuide/aws-nvme-drivers.md"),
  and [Upgrade PV drivers on Windows instances](../../../AWSEC2/latest/WindowsGuide/Upgrading_PV_drivers.md "../../../AWSEC2/latest/WindowsGuide/Upgrading_PV_drivers.md").
- Ensure you update the EC2Config, EC2Launch, and EC2Launch V2 agents to the latest versions periodically. You should do this at least once every 6 months. For more information, see
  [Update EC2Config and EC2Launch](../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#upgdate-ec2config-ec2launch "../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#upgdate-ec2config-ec2launch").

## (Optional) Step 1: Specify a custom computer

name format for your image

For the WorkSpaces launched from your custom or Bring Your Own License (BYOL)
images, you can specify a custom prefix for the computer name format instead of
using the [default computer name
format](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md"). To specify a custom prefix, follow the appropriate procedure for
your image type.

###### Note

By default, the format of the computer name for Windows 10 WorkSpaces is `DESKTOP-XXXXX`
and for Windows 11 WorkSpaces, `WORKSPA-XXXXX`.

1. On the WorkSpace that you're using to create your custom image,
   open
   `C:\ProgramData\Amazon\EC2-Windows\Launch\Sysprep\Unattend.xml`
   in Notepad or another text editor. For more information about
   working with the `Unattend.xml` file, see [Answer files (unattend.xml)](https://docs.microsoft.com/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs "https://docs.microsoft.com/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs") in the Microsoft
   documentation.

###### Note

To access the C: drive from the Windows File Explorer on your
WorkSpace, enter `C:\` in the address
bar. 2. In the `<settings pass="specialize">` section,
make sure that `<ComputerName>` is set to an
asterisk (`*`). If `<ComputerName>` is
set to any other value, your custom computer name settings will be
ignored. For more information about the
`<ComputerName>` setting, see [ComputerName](https://docs.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-shell-setup-computername "https://docs.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-shell-setup-computername") in the Microsoft documentation. 3. In the `<settings pass="specialize">` section,
set `<RegisteredOrganization>` and
`<RegisteredOwner>` to your preferred
values.

During Sysprep, the values that you specify for
`<RegisteredOwner>` and
`<RegisteredOrganization>` are concatenated
together, and the first 7 characters of the combined string are used
to create the computer name. For example, if you specify
`Amazon.com` for
`<RegisteredOrganization>` and
`EC2` for
`<RegisteredOwner>`. For Windows 10-based images,
the computer names for the WorkSpaces using custom bundles will start with
EC2AMAZ-`xxxxxxx`. For Windows 11 based images,
the computer names for the WorkSpaces using custom bundles will start with
WORKSPA-`xxxxxxx`.

###### Note

    * The `<RegisteredOrganization>` and
     `<RegisteredOwner>` values in the
     `<settings pass="oobeSystem">` section are
     ignored by Sysprep.
    * Both <RegisteredOrganization> and <RegisteredOwner>
     are required values.

4. Save your changes to the `Unattend.xml`
   file.

1. If you are using Windows 10, open `C:\Program
Files\Amazon\Ec2ConfigService\Sysprep2008.xml` in
   Notepad or another text editor. If you are using Windows 11, open
   `C:\ProgramData\Amazon\EC2Launch\sysprep\OOBE_unattend.xml`.
1. In the `<settings pass="specialize">` section,
   if you're using Windows 10, uncomment `<ComputerName>*</ComputerName>`.
   If you're using Windows 11, you won't need to uncomment this section.
   Make sure that `<ComputerName>` is set to an
   asterisk (`*`). If `<ComputerName>` is
   set to any other value, your custom computer name settings will be
   ignored. For more information about the
   `<ComputerName>` setting, see [ComputerName](https://docs.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-shell-setup-computername "https://docs.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-shell-setup-computername") in the Microsoft documentation.
1. In the `<settings pass="specialize">` section,
   the `<RegisteredOrganization>` field will be present
   for Windows 10 and Windows 11.
   The `<RegisteredOwner>` tag
   will only be present in Windows 10 by default. If you're using Windows 11, you
   will need to add this tag.
   Set `<RegisteredOrganization>` and
   `<RegisteredOwner>` to your preferred values.

During Sysprep, the values that you specify for
`<RegisteredOwner>` and
`<RegisteredOrganization>` are concatenated
together, and the first 7 characters of the combined string are used
to create the computer name. For example, if you specify
`Amazon.com` for
`<RegisteredOrganization>` and
`EC2` for
`<RegisteredOwner>`, the computer names for the
WorkSpaces created from your custom bundle will start with
EC2AMAZ-`xxxxxxx`.

###### Note

    * The `<RegisteredOrganization>` and
     `<RegisteredOwner>` values in the
     `<settings pass="oobeSystem">` section are
     ignored by Sysprep.
    * Both <RegisteredOrganization> and <RegisteredOwner>
     are required values.

4. If you are using Windows 10, save your changes to the
   `Sysprep2008.xml` file. If you are using
   Windows 11, save your changes to
   `OOBE_unattend.xml`

## Step 2: Run the Image Checker

###### Note

The Image Checker is available only for Windows WorkSpaces. If you are
creating an image from a Linux WorkSpace, skip to [Step 3: Create a custom image and
custom bundle](#create_custom_image_bundle "#create_custom_image_bundle").

To confirm that your Windows WorkSpace meets the requirements for image creation,
we recommend running the Image Checker. The Image Checker performs a series of tests
on the WorkSpace that you want to use to create your image, and provides guidance on
how to resolve any issues it finds.

###### Important

- The WorkSpace must pass all of the tests run by the Image Checker
  before you can use it for image creation.
- Before you run the Image Checker, verify that the latest Windows
  security and cumulative updates are installed on your WorkSpace.

To get the Image Checker, do one of the following:

- [Reboot your WorkSpace](reboot-workspaces.md "reboot-workspaces.md"). The Image
  Checker is downloaded automatically during the reboot and installed at
  `C:\Program Files\Amazon\ImageChecker.exe`.
- Download the Amazon WorkSpaces Image Checker from [https://tools.amazonworkspaces.com/ImageChecker.zip](https://tools.amazonworkspaces.com/ImageChecker.zip "https://tools.amazonworkspaces.com/ImageChecker.zip")
  and
  extract the `ImageChecker.exe` file. Copy this file to
  `C:\Program Files\Amazon\`.

###### To run the Image Checker

1. Open the `C:\Program Files\Amazon\ImageChecker.exe`
   file.
2. In the **Amazon WorkSpaces Image Checker** dialog box,
   choose **Run**.
3. After each test is completed, you can view the status of the test.

For any test with a status of **FAILED**, choose
**Info** to display information about how to resolve
the issue that caused the failure. For more information about how to resolve
these issues, see [Tips for resolving issues detected by the
Image Checker](#image_checker_tips "#image_checker_tips").

If any tests display a status of **WARNING**, choose the
**Fix All Warnings** button.

The tool generates an output log file in the same directory where the
Image Checker is located. By default, this file is located at
`C:\Program
 Files\Amazon\ImageChecker_`yyyyMMddhhmmss`.log`.

###### Tip

Do not delete this log file. If an issue occurs, this log file might
be helpful in troubleshooting. 4. If applicable, resolve any issues that cause test failures and warnings,
and repeat the process of running the Image Checker until the WorkSpace
passes all tests. All failures and warnings must be resolved before you can
create an image. 5. After your WorkSpace passes all tests, you see a **Validation
Successful** message. You are now ready to create a custom
bundle.

### Tips for resolving issues detected by the

Image Checker

In addition to consulting the following tips for resolving issues that are
detected by the Image Checker, be sure to review the Image Checker log file at
`C:\Program
 Files\Amazon\ImageChecker_`yyyyMMddhhmmss`.log`.

Install the latest version of [Microsoft Windows
PowerShell](https://docs.microsoft.com/powershell "https://docs.microsoft.com/powershell").

###### Important

The PowerShell execution policy for a WorkSpace must be set to
allow **RemoteSigned** scripts. To
check the execution policy, run the **Get-ExecutionPolicy** PowerShell command. If the
execution policy is not set to **Unrestricted** or **RemoteSigned**, run the **Set-ExecutionPolicy –ExecutionPolicy RemoteSigned**
command to change the value of the execution policy. The **RemoteSigned** setting allows the execution
of scripts on Amazon WorkSpaces, which is required to create an
image.

Only the `C` and `D` drives can
be present on a WorkSpace that's used for imaging. Remove all other
drives, including virtual drives.

- The Create Image process can't run until Windows is rebooted
  to finish installing security or cumulative updates. Reboot
  Windows to apply these updates, and make sure that no other
  pending Windows security or cumulative updates need to be
  installed.
- Image creation is not supported on Windows 10 systems that
  have been upgraded from one version of Windows 10 to a newer
  version of Windows 10 (a Windows feature/version upgrade).
  However, Windows cumulative or security updates are supported by
  the WorkSpaces image-creation process.

If there are problems with your Sysprep file, contact the
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to get your EC2Config or EC2Launch
repaired.

For Windows 7 WorkSpaces, the user profile
(`D:\Users\`username``)
must be less than 10 GB total. Remove files as needed to reduce the size
of the user profile.

For Windows 7 WorkSpaces, you must have at least 12 GB of free space on
drive `C`. Remove files as needed to free up space on
drive `C`. For Windows 10 WorkSpaces, ignore if you
receive a `FAILED` message and the disk space is above
2GB.

To run the Create Image process, no services on the WorkSpace can be
running under a domain account. All services must be running under a
local account.

###### To run services under a local account

1. Open `C:\Program
Files\Amazon\ImageChecker_`yyyyMMddhhmmss`.log`
   and find the list of services that are running under a domain
   account.
2. In the Windows search box, enter
   `services.msc` to open the Windows
   Services Manager.
3. Under **Log On As**, look for the services
   that are running under domain accounts. (Services running as
   **Local System**, **Local
   Service**, or **Network Service**
   do not interfere with image creation.)
4. Select a service that is running under a domain account, and
   then choose **Action**,
   **Properties**.
5. Open the **Log On** tab. Under **Log
   on as**, choose **Local System
   account**.
6. Choose **OK**.

You must configure all network adapters on the WorkSpace to use DHCP
instead of static IP addresses.

###### To set all network adapters to use DHCP

1. In the Windows search box, enter `control
panel` to open the Control Panel.
2. Choose **Network and Internet**.
3. Choose **Network and Sharing Center**.
4. Choose **Change adapter settings**, and
   select an adapter.
5. Choose **Change settings of this
   connection**.
6. On the **Networking** tab, select
   **Internet Protocol Version 4 (TCP/IPv4)**,
   and then choose **Properties**.
7. In the **Internet Protocol Version 4 (TCP/IPv4)
   Properties** dialog box, select **Obtain an
   IP address automatically**.
8. Choose **OK**.
9. Repeat this process for all network adapters on the
   WorkSpace.

The Create Image process requires Remote Desktop Services to be
enabled.

###### To enable Remote Desktop Services

1. In the Windows search box, enter
   `services.msc` to open the Windows
   Services Manager.
2. In the **Name** column, find **Remote
   Desktop Services**.
3. Select **Remote Desktop Services**, and then
   choose **Action**,
   **Properties**.
4. On the **General** tab, for **Startup
   type**, choose **Manual** or
   **Automatic**.
5. Choose **OK**.

The WorkSpace that you're using to create images must have a user
profile
(`D:\Users\`username``).
If this test fails, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") for
assistance.

The environment variable path for the local machine is missing entries
for System32 and for Windows PowerShell. These entries are required for
Create Image to run.

###### To configure your environment variable path

1. In the Windows search box, enter `environment
variables` and then choose **Edit the
   system environment variables**.
2. In the **System Properties** dialog box, open
   the **Advanced** tab, and choose
   **Environment Variables**.
3. In the **Environment Variables** dialog box,
   under **System variables**, select the
   **Path** entry and then choose
   **Edit**.
4. Choose **New**, and add the following
   path:

`C:\Windows\System32` 5. Choose **New** again, and add the following
path:

`C:\Windows\System32\WindowsPowerShell\v1.0\` 6. Choose **OK**. 7. Restart the WorkSpace.

###### Tip

The order in which items appear in the environment
variable path matters. To determine the correct order, you
might want to compare the environment variable path of your
WorkSpace with one from a newly created WorkSpace or a new
Windows instance.

The Create Image process requires the Windows Modules Installer
service to be enabled.

###### To enable the Windows Modules Installer service

1. In the Windows search box, enter
   `services.msc` to open the Windows
   Services Manager.
2. In the **Name** column, find
   **Windows Modules Installer**.
3. Select **Windows Modules Installer**, and
   then choose **Action**,
   **Properties**.
4. On the **General** tab, for **Startup
   type**, choose **Manual** or
   **Automatic**.
5. Choose **OK**.

The Create Image process requires the Amazon SSM Agent service to be
disabled.

###### To disable the Amazon SSM Agent service

1. In the Windows search box, enter
   `services.msc` to open the Windows
   Services Manager.
2. In the **Name** column, find **Amazon
   SSM Agent**.
3. Select **Amazon SSM Agent**, and then choose
   **Action**,
   **Properties**.
4. On the **General** tab, for **Startup
   type**, choose
   **Disabled**.
5. Choose **OK**.

To configure SSL/TLS for Windows, see [How to Enable TLS 1.2](https://docs.microsoft.com/configmgr/core/plan-design/security/enable-tls-1-2 "https://docs.microsoft.com/configmgr/core/plan-design/security/enable-tls-1-2") in the Microsoft Windows
documentation.

There can be only one WorkSpaces user profile
(`D:\Users\`username``)
on the WorkSpace that you're using to create images. Delete any user
profiles that don't belong to the intended user of the WorkSpace.

For image creation to work, your WorkSpace can have only three user
profiles on it:

- The user profile of the intended user of the WorkSpace
  (`D:\Users\`username``)
- The default user profile (also known as Default
  Profile)
- The Administrator user profile
  If there are additional user profiles, you can delete them through the
  advanced system properties in the Windows Control Panel.

###### To delete a user profile

1. To access the advanced system properties, do one of the
   following:
   - Press the **Windows key+Pause
     Break**, and then choose **Advanced
     system settings** in the left pane of the
     **Control Panel** >
     **System and Security** >
     **System** dialog box.
   - In the Windows search box, enter `control
panel`. In the Control Panel, choose
     **System and Security**, then
     choose System, and then choose **Advanced system
     settings** in the left pane of the
     **Control Panel** >
     **System and Security** >
     **System** dialog box.

2. In the **System Properties** dialog box, on
   the **Advanced** tab, choose
   **Settings** under **User
   Profiles**.
3. If any profile is listed other than the Administrator profile,
   the Default Profile, and the profile of the intended WorkSpaces
   user, select that additional profile and choose
   **Delete**.
4. When asked if you want to delete the profile, choose
   **Yes**.
5. If necessary, repeat Steps 3 and 4 to remove any other
   profiles that don't belong on the WorkSpace.
6. Choose **OK** twice and close the Control
   Panel.
7. Restart the WorkSpace.

One or more AppX packages are in a staged state. This might cause a
Sysprep error during image creation.

###### To remove all staged AppX packages

1. In the Windows search box, enter
   `powershell`. Choose **Run as
   Administrator**.
2. When asked "Do you want to allow this app to make changes to
   your device?", choose **Yes**.
3. In the Windows PowerShell window, enter the following commands
   to list all staged AppX packages, and press Enter after each
   one.

```
$workSpaceUserName = $env:username
```

```
$allAppxPackages = Get-AppxPackage -AllUsers
```

```
$packages = $allAppxPackages |    Where-Object { `
                                (($_.PackageUserInformation -like "*S-1-5-18*" -and !($_.PackageUserInformation -like "*$workSpaceUserName*")) -and `
                                ($_.PackageUserInformation -like "*Staged*" -or $_.PackageUserInformation -like "*Installed*")) -or `
                                ((!($_.PackageUserInformation -like "*S-1-5-18*") -and $_.PackageUserInformation -like "*$workSpaceUserName*") -and `
                                $_.PackageUserInformation -like "*Staged*")
                                }
```

4. Enter the following command to remove all staged AppX
   packages, and press Enter.

```
$packages | Remove-AppxPackage -ErrorAction SilentlyContinue
```

5. Run the Image Checker again. If this test still fails, enter
   the following commands to remove all AppX packages, and press
   Enter after each one.

```
Get-AppxProvisionedPackage -Online | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue
```

```
Get-AppxPackage -AllUsers | Remove-AppxPackage -ErrorAction SilentlyContinue
```

Image creation is not supported on Windows systems that have been
upgraded from one version of Windows 10 to a newer version of Windows 10
(a Windows feature/version upgrade).

To create images, use a WorkSpace that has not undergone a Windows
feature/version upgrade.

The rearm feature allows you to extend the activation period for the
trial version of Windows. The Create Image process requires that the
rearm count be a value other than 0.

###### To check the Windows rearm count

1. On the Windows **Start** menu, choose
   **Windows System**, then choose
   **Command Prompt**.
2. In the Command Prompt window, enter the following command, and
   then press Enter.

`cscript C:\Windows\System32\slmgr.vbs /dlv`
To reset the rearm count to a value other than 0, see [Sysprep (Generalize) a Windows installation](https://docs.microsoft.com/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation "https://docs.microsoft.com/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation") in the
Microsoft Windows documentation.

#### Other troubleshooting

tips

If your WorkSpace passes all of the tests run by the Image Checker, but
you are still unable to create an image from the WorkSpace, check for the
following issues:

- Make sure that the WorkSpace isn't assigned to a user within a
  **Domain Guests** group. To check
  if there are any domain accounts, run the following PowerShell
  command.

```
Get-WmiObject -Class Win32_Service | Where-Object { $_.StartName -like "*$env:USERDOMAIN*" }
```

- For Windows 7 WorkSpaces only: If problems occur while the user
  profile is being copied during image creation, check for the
  following issues:
  - Long profile paths can cause image creation errors. Make
    sure that the paths of all folders within the user profile
    are less than 261 characters.
  - Make sure to grant full permissions on the profile folder
    to the system and all application packages.
  - If any files in the user profile are locked by a process
    or are in use during image creation, copying the profile
    might fail.

- Some Group Policy Objects (GPOs) restrict access to the RDP
  certificate thumbprint when it is requested by the EC2Config service
  or the EC2Launch scripts during Windows instance configuration.
  Before you try to create an image, move the WorkSpace to a new
  organizational unit (OU) with blocked inheritance and no GPOs
  applied.
- Make sure that the Windows Remote Management (WinRM) service is
  configured to start automatically. Do the following:
  1.  In the Windows search box, enter
      `services.msc` to open the Windows
      Services Manager.
  2.  In the **Name** column, find
      **Windows Remote Management
      (WS-Management)**.
  3.  Select **Windows Remote Management
      (WS-Management)**, and then choose
      **Action**,
      **Properties**.
  4.  On the **General** tab, for
      **Startup type**, choose
      **Automatic**.
  5.  Choose **OK**.

## Step 3: Create a custom image and

custom bundle

After you have validated your WorkSpace image, you can proceed with creating your
custom image and custom bundle.

###### To create a custom image and custom bundle

1. If you are still connected to the WorkSpace, disconnect by choosing
   **Amazon WorkSpaces** and
   **Disconnect** in the WorkSpaces client
   application.
2. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
3. In the navigation pane, choose **WorkSpaces**.
4. Select the WorkSpace to open its details page and choose **Create
   image**. If the status of the WorkSpace is
   **Stopped**, you must start it first (choose
   **Actions**, **Start WorkSpaces**)
   before you can choose **Actions**, **Create
   Image**.

###### Note

To create an image programmatically, use the CreateWorkspaceImage API
action. For more information, see [CreateWorkspaceImage](../api/API_CreateWorkspaceImage.md "../api/API_CreateWorkspaceImage.md") in the _Amazon WorkSpaces API Reference_. 5. A message displays, prompting you to reboot (restart) your WorkSpace
before continuing. Rebooting your WorkSpace updates your Amazon WorkSpaces software
to the latest version.

Reboot your WorkSpace by closing the message and following the steps in
[Reboot a WorkSpace in WorkSpaces Personal](reboot-workspaces.md "reboot-workspaces.md").
When you're done, repeat [Step 4](#step_create_image "#step_create_image") of this
procedure, but this time choose **Next** when the reboot
message appears. To create an image, the status of the WorkSpace must be
**Available** and its modification state must be
**None**. 6. Enter an image name and a description that will help you identify the
image, and then choose **Create Image**. While the image is
being created, the status of the WorkSpace is **Suspended**
and the WorkSpace is unavailable.

###### Note

When entering an image description, make sure you don't use the special character "-" or you will get an error. 7. In the navigation pane, choose **Images**. The image is
complete when the status of the WorkSpace changes to
**Available** (this can take up to 45 minutes). 8. Select the image and choose **Actions**, **Create
bundle**.

###### Note

To create a bundle programmatically, use the
**CreateWorkspaceBundle** API action. For more
information, see [CreateWorkspaceBundle](../api/API_CreateWorkspaceBundle.md "../api/API_CreateWorkspaceBundle.md") in the
_Amazon WorkSpaces API Reference_. 9. Enter a bundle name and a description, and then do the following:

    * For **Bundle hardware type**, choose the hardware
     to use when launching WorkSpaces from this custom bundle.
    * For **Storage settings**, select one of the
     default combinations for the root volume and user volume size, or
     select **Custom**, and then enter values (up to
     2000 GB) for **Root volume size** and
     **User volume size**.


    The default available size combinations for the root volume (for
     Microsoft Windows, the `C` drive, for Linux, /)
     and the user volume (for Windows, the `D` drive;
     for Linux, /home) are as follows:




    	+ Root: 80 GB, User: 10 GB, 50 GB, or 100 GB
    	+ Root: 175 GB, User: 100 GB
    	+ Storage requirements for GPU-enabled WorkSpaces scale proportionally with instance sizing. As you select larger GPU-enabled WorkSpaces configurations,
    	 you must allocate correspondingly larger storage volumes to maintain optimal performance and accommodate increased workload demands.
    	 For the smallest instance size, begin with the following storage allocation: Root: 100 GB, User: 100 GB
    Alternatively, you can expand the root and user volumes up to 2000
     GB each.


    ###### Note

    To ensure that your data is preserved, you cannot decrease the
     size of the root or user volumes after you launch a WorkSpace.
     Instead, make sure that you specify the minimum sizes for these
     volumes when launching a WorkSpace.



    	+ You can launch a Value, Standard, Performance, Power,
    	 or PowerPro WorkSpace with a minimum of 80 GB for the root
    	 volume and 10 GB for the user volume.
    	+ You can launch a GeneralPurpose.4xlarge or GeneralPurpose.8xlarge
    	 WorkSpace with a minimum of 175GB for the root volume and 100 GB
    	 for the user volume.

10. Choose **Create bundle**.
11. To confirm that your bundle has been created, choose
    **Bundles** and verify that the bundle is
    listed.

## What's included with Windows WorkSpaces custom

images

When you create an image from a Windows 7, Windows 10, or
Windows 11 WorkSpace, the entire contents of the `C` drive are
included.

For Windows 10 or 11 WorkSpaces, the user profile in
`D:\Users\`username`` is not
included in the custom image.

For Windows 7 WorkSpaces, the entire contents of the user profile in
`D:\Users\`username`` are
included, except for the following:

- Contacts
- Downloads
- Music
- Pictures
- Saved games
- Videos
- Podcasts
- Virtual machines
- .virtualbox
- Tracing
- appdata\local\temp
- appdata\roaming\apple computer\mobilesync\
- appdata\roaming\apple computer\logs\
- appdata\roaming\apple computer\itunes\iphone software updates\
- appdata\roaming\macromedia\flash
  player\macromedia.com\support\flashplayer\sys\
- appdata\roaming\macromedia\flash player\#sharedobjects\
- appdata\roaming\adobe\flash player\assetcache\
- appdata\roaming\microsoft\windows\recent\
- appdata\roaming\microsoft\office\recent\
- appdata\roaming\microsoft office\live meeting
- appdata\roaming\microsoft shared\livemeeting shared\
- appdata\roaming\mozilla\firefox\crash reports\
- appdata\roaming\mcafee\common framework\
- appdata\local\microsoft\feeds cache
- appdata\local\microsoft\windows\temporary internet files\
- appdata\local\microsoft\windows\history\
- appdata\local\microsoft\internet explorer\domstore\
- appdata\local\microsoft\internet explorer\imagestore\
- appdata\locallow\microsoft\internet explorer\iconcache\
- appdata\locallow\microsoft\internet explorer\domstore\
- appdata\locallow\microsoft\internet explorer\imagestore\
- appdata\local\microsoft\internet explorer\recovery\
- appdata\local\mozilla\firefox\profiles\

## What's included with Linux WorkSpace custom

images

When you create an image from an Amazon Linux WorkSpace, the entire contents of the user
volume (/home) are removed. The contents of the root volume (/) are included, except
the following applicable folders and keys, which are removed:

- /tmp
- /var/spool/mail
- /var/tmp
- /var/lib/dhcp
- /var/lib/cloud
- /var/cache
- /var/backups
- /etc/sudoers.d
- /etc/udev/rules.d/70-persistent-net.rules
- /etc/network/interfaces.d/50-cloud-init.cfg
- /var/log/amazon/ssm
- /var/log/pcoip-agent
- /var/log/skylight
- /var/lock/.skylight.domain-join.lock
- /var/lib/skylight/domain-join-status
- /var/lib/skylight/configuration-data
- /var/lib/skylight/config-data.json
- /home
- /etc/default/grub.d/zz-hibernation.cfg
- /etc/netplan/zz-workspaces-domain.yaml
- /etc/netplan/yy-workspaces-base.yaml
- /var/lib/AccountsService/users

The following keys are shredded during custom image creation:

- /etc/ssh/ssh_host\_\*\_key
- /etc/ssh/ssh_host\_\*\_key.pub
- /var/lib/skylight/tls.\*
- /var/lib/skylight/private.key
- /var/lib/skylight/public.key
