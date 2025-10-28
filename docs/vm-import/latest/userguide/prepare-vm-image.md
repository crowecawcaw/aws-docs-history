# Configurations to export VMs from your virtualization

environment

Before you can import your VM to Amazon EC2, you need to export it from your virtualization
environment. Use the following guidelines to configure your VM before exporting
it.

###### Topics

- [General configurations](#prepare-vm-image-general "#prepare-vm-image-general")
- [Linux/Unix configurations](#prepare-vm-image-linux "#prepare-vm-image-linux")
- [Windows configurations](#prepare-vm-image-windows "#prepare-vm-image-windows")

## General configurations

The following configurations should be made in your VM before you export it from
your virtualization environment. You should also review the section specific to your
operating system for additional required configurations.

- Disable any antivirus or intrusion detection software on your VM. These
  services can be re-enabled after the import process is complete.
- Uninstall the VMware Tools from your VMware VM.
- Disconnect any CD-ROM drives (virtual or physical).
- Your source VM must have a functional DHCP client service. Ensure that the
  service can start and is not disabled administratively. All static IP
  addresses currently assigned to the source VM are removed during import.
  When your imported instance is launched in an Amazon VPC, it receives a primary
  private IP address from the IPv4 address range of the subnet. If you don't
  specify a primary private IP address when you launch the instance, we select
  an available IP address in the subnet's IPv4 range for you. For more
  information, see [VPC
  and Subnet Sizing](../../../vpc/latest/userguide/VPC_Subnets.md#VPC_Sizing "../../../vpc/latest/userguide/VPC_Subnets.md#VPC_Sizing").

## Linux/Unix configurations

The following configurations should be made in your Linux VM before you export it
from your virtualization environment. This section assumes you have already reviewed
[General configurations](#prepare-vm-image-general "#prepare-vm-image-general").

- Enable Secure Shell (SSH) for remote access.
- Make sure that your host firewall (such as Linux
  **iptables**) allows access to SSH. Otherwise, you won't
  be able to access your instance after the import is complete.
- Make sure that you have configured a non-root user to use public key-based
  SSH to access your instance after it is imported. The use of password-based
  SSH and root login over SSH are both possible, but not recommended. The use
  of public keys and a non-root user is recommended because it is more secure.
  VM Import does not configure an `ec2-user` account as part of the
  import process.
- Make sure that your Linux VM uses GRUB (GRUB legacy) or GRUB 2 as its
  bootloader.
- Make sure that your Linux VM uses one of the following for the root file
  system: EXT2, EXT3, EXT4, Btrfs, JFS, or XFS.
- Make sure that your Linux VM is not using predictable network interface
  device names.
- Shut down your VM before exporting it from your virtualization
  environment.

## Windows configurations

The following configurations should be made in your Windows VM before you export
it from your virtualization environment. This section assumes you have already
reviewed [General configurations](#prepare-vm-image-general "#prepare-vm-image-general").

- Enable Remote Desktop (RDP) for remote access.
- Make sure that your host firewall (Windows firewall or similar), if
  configured, allows access to RDP. Otherwise, you cannot access your instance
  after the import is complete.
- Make sure that the administrator account and all other user accounts use
  secure passwords. All accounts must have passwords or the import process
  might fail.
- Install .NET Framework 4.5 or later on the VM. We install the .NET
  framework on your VM as needed.
- Disable Autologon on your Windows VM.
- Open **Control Panel** > **System and
  Security** > **Windows Update**. In the left
  pane, choose **Change settings**. Choose the desired
  setting. Be aware that if you choose **Download updates but let me
  choose whether to install them** (the default value) the update
  check can temporarily consume between 50% and 99% of CPU resources on the
  instance. The check usually occurs several minutes after the instance
  starts. Make sure that there are no pending Microsoft updates, and that the
  computer is not set to install software when it reboots.
- Apply the following hot fixes as needed:
  - [You cannot change system time if RealTimeIsUniversal registry
    entry is enabled in Windows](https://support.microsoft.com/en-us/topic/you-cannot-change-system-time-if-realtimeisuniversal-registry-entry-is-enabled-in-windows-78cf9fbe-eeca-4b06-a67a-2dacdf5189f9 "https://support.microsoft.com/en-us/topic/you-cannot-change-system-time-if-realtimeisuniversal-registry-entry-is-enabled-in-windows-78cf9fbe-eeca-4b06-a67a-2dacdf5189f9")
  - [High CPU usage during DST changeover in Windows Server 2008,
    Windows 7, or Windows Server 2008 R2](https://support.microsoft.com/en-us/topic/high-cpu-usage-during-dst-changeover-in-windows-server-2008-windows-7-or-windows-server-2008-r2-5c8a8dee-3510-cf7b-8296-05c13fd23bed "https://support.microsoft.com/en-us/topic/high-cpu-usage-during-dst-changeover-in-windows-server-2008-windows-7-or-windows-server-2008-r2-5c8a8dee-3510-cf7b-8296-05c13fd23bed")

- Set the RealTimeIsUniversal registry key. For more information, see [Set
  the time for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md") in the
  _Amazon EC2 User Guide_.
- Run System Preparation (Sysprep) on your Windows Server VM images, either
  before or after importing your VM.
  - If you run Sysprep before importing your VM, the import process
    adds an answer file (`unattend.xml`) to the VM
    that automatically accepts the End User License Agreement (EULA) and
    sets the locale to EN-US.
  - If you run Sysprep after importing your VM, we recommend that you
    use EC2Launch (Windows Server 2016 and later) or EC2Config (through
    Windows Server 2012 R2) to run Sysprep.

###### To include your own answer file instead of the default

(`unattend.xml`)

    1. Copy the following sample file below and set the
     **processorArchitecture** parameter to
     **x86** or **amd64**,
     depending on your operating system architecture:



    ```
    <?xml version='1.0' encoding='UTF-8'?>
    <unattend xmlns:wcm='https://schemas.microsoft.com/WMIConfig/2002/State' xmlns='urn:schemas-microsoft-com:unattend'>
     <settings pass='oobeSystem'>
      <component versionScope='nonSxS' processorArchitecture='`x86 or amd64`' name='Microsoft-Windows-International-Core' publicKeyToken='31bf3856ad364e35' language='neutral'>
       <InputLocale>en-US</InputLocale>
       <SystemLocale>en-US</SystemLocale>
       <UILanguage>en-US</UILanguage>
       <UserLocale>en-US</UserLocale>
      </component>
      <component versionScope='nonSxS' processorArchitecture='`x86 or amd64`' name='Microsoft-Windows-Shell-Setup' publicKeyToken='31bf3856ad364e35' language='neutral'>
       <OOBE>
        <HideEULAPage>true</HideEULAPage>
        <SkipMachineOOBE>true</SkipMachineOOBE>
        <SkipUserOOBE>true</SkipUserOOBE>
       </OOBE>
      </component>
     </settings>
    </unattend>
    ```
    2. Save the file in the `C:\Windows\Panther`
     directory with the name `unattend.xml`.
    3. Run Sysprep with the **/oobe** and
     **/generalize** options. These options strip all
     unique system information from the Windows installation and prompt
     you to reset the administrator password.
    4. Shut down the VM and export it from your virtualization
     environment.
