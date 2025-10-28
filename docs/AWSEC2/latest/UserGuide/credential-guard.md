# Credential Guard for Windows instances

The AWS Nitro System supports Credential Guard for Amazon Elastic Compute Cloud (Amazon EC2) Windows instances. Credential Guard is a Windows virtualization-based
security (VBS) feature that enables the creation of isolated environments to protect security
assets, such as Windows user credentials and code integrity enforcement, beyond Windows kernel
protections. When you run EC2 Windows instances, Credential Guard uses the AWS Nitro System to protect
Windows login credentials from being extracted from the operating system's memory.

###### Contents

- [Prerequisites](#credential-guard-prerequisites "#credential-guard-prerequisites")
- [Launch a supported instance](#credential-guard-launch-instance "#credential-guard-launch-instance")
- [Disable memory integrity](#disable-memory-integrity "#disable-memory-integrity")
- [Turn on Credential Guard](#turn-on-credential-guard "#turn-on-credential-guard")
- [Verify that Credential Guard is running](#verify-credential-guard "#verify-credential-guard")

## Prerequisites

Your Windows instance must meet the following prerequisites to utilize Credential Guard.

**Amazon Machine Images (AMIs)**

The AMI must be preconfigured to enable NitroTPM and UEFI Secure
Boot. For more information on supported AMIs, see [Requirements for using NitroTPM with Amazon EC2
instances](enable-nitrotpm-prerequisites.md "enable-nitrotpm-prerequisites.md").

**Memory integrity**

_Memory integrity_, also known as
_hypervisor-protected code integrity (HVCI)_ or
_hypervisor enforced code integrity_, isn't supported. Before you
turn on Credential Guard, you must ensure this feature is disabled. For more information, see
[Disable memory integrity](#disable-memory-integrity "#disable-memory-integrity").

**Instance types**

The following instance types support Credential Guard across all sizes unless noted
otherwise: `C5`, `C5d`, `C5n`, `C6i`,
`C6id`, `C6in`, `C7i`, `C7i-flex`,
`M5`, `M5d`, `M5dn`, `M5n`,
`M5zn`, `M6i`, `M6id`, `M6idn`,
`M6in`, `M7i`, `M7i-flex`, `R5`,
`R5b`, `R5d`, `R5dn`, `R5n`,
`R6i`, `R6id`, `R6idn`, `R6in`
`R7i`, `R7iz`, `T3`.

###### Note

- Though NitroTPM has some required instance types in common, the instance type
  must be one of the preceding instance types to support Credential Guard.
- Credential Guard isn't supported for:
  - Bare metal instances.
  - The following instance types: `C7i.48xlarge`,
    `M7i.48xlarge`, and `R7i.48xlarge`.

For more information about instance types, see the [Amazon EC2 Instance Types Guide](../../../ec2/latest/instancetypes/instance-types.md "../../../ec2/latest/instancetypes/instance-types.md").

## Launch a supported instance

You can use the Amazon EC2 console or AWS Command Line Interface (AWS CLI) to launch an instance which can
support Credential Guard. You will need a compatible AMI ID for launching your instance which is
unique for each AWS Region.

###### Tip

You can use the following link to discover and launch instances with compatible Amazon
provided AMIs in the Amazon EC2 console:

[https://console.aws.amazon.com/ec2/v2/home?#Images:visibility=public-images;v=3;search=:TPM-Windows_Server;ownerAlias=amazon](https://console.aws.amazon.com/ec2/v2/home?#Images:visibility=public-images;v=3;search=:TPM-Windows_Server;ownerAlias=amazon "https://console.aws.amazon.com/ec2/v2/home?#Images:visibility=public-images;v=3;search=:TPM-Windows_Server;ownerAlias=amazon")

Console

###### To launch an instance

Follow the steps to [launch an instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"),
specifying a supported instance type and a preconfigured Windows AMI.

AWS CLI

###### To launch an instance

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command to launch an instance using a
supported instance type and preconfigured Windows AMI.

```
aws ec2 run-instances \
    --image-id resolve:ssm:/aws/service/ami-windows-latest/`TPM-Windows_Server-2022-English-Full-Base` \
    --instance-type `c6i.large` \
    --region `us-east-1` \
    --subnet-id `subnet-0abcdef1234567890`
    --key-name `key-name`
```

PowerShell

###### To launch an instance

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") command to launch an instance using a
supported instance type and preconfigured Windows AMI.

```
New-EC2Instance `
    -ImageId resolve:ssm:/aws/service/ami-windows-latest/`TPM-Windows_Server-2022-English-Full-Base` `
    -InstanceType `c6i.large` `
    -Region `us-east-1` `
    -SubnetId `subnet-0abcdef1234567890` `
    -KeyName `key-name`
```

## Disable memory integrity

You can use the Local Group Policy Editor to disable memory integrity in supported
scenarios. The following guidance can be applied for each configuration setting under
**Virtualization Based Protection of Code Integrity**:

- Enabled without lock – Modify the setting to
  **Disabled** to disable memory integrity.
- Enabled with UEFI lock – Memory integrity has
  been enabled with UEFI lock. Memory integrity can't be disabled once it has been enabled
  with UEFI lock. We recommend creating a new instance with memory integrity disabled and
  terminating the unsupported instance if it's not in use.

###### To disable memory integrity with the Local Group Policy Editor

1. Connect to your instance as a user account with administrator privileges using
   the Remote Desktop Protocol (RDP). For more information, see [Connect to your Windows instance using an RDP client](connect-rdp.md "connect-rdp.md").
2. Open the Start menu and search for `cmd` to start a
   command prompt.
3. Run the following command to open the Local Group Policy Editor:
   `gpedit.msc`
4. In the Local Group Policy Editor, choose **Computer
   Configuration**, **Administrative Templates**,
   **System**, **Device Guard**.
5. Select **Turn On Virtualization Based Security**, then select
   **Edit policy setting**.
6. Open the settings drop-down for **Virtualization Based Protection of
   Code Integrity**, choose **Disabled**, then choose
   **Apply**.
7. Reboot the instance to apply the changes.

## Turn on Credential Guard

After you have launched a Windows instance with a supported instance type and compatible
AMI, and confirmed that memory integrity is disabled, you can turn on Credential Guard.

###### Important

Administrator privileges are required to perform the following steps to turn on
Credential Guard.

###### To turn on Credential Guard

1. Connect to your instance as a user account with administrator privileges using the
   Remote Desktop Protocol (RDP). For more information, see [Connect to your Windows instance using an RDP client](connect-rdp.md "connect-rdp.md").
2. Open the Start menu and search for `cmd` to start a command
   prompt.
3. Run the following command to open the Local Group Policy Editor:
   `gpedit.msc`
4. In the Local Group Policy Editor, choose **Computer
   Configuration**, **Administrative Templates**,
   **System**, **Device Guard**.
5. Select **Turn On Virtualization Based Security**, then select
   **Edit policy setting**.
6. Choose **Enabled** within the **Turn On Virtualization
   Based Security** menu.
7. For **Select Platform Security Level**, choose **Secure
   Boot and DMA Protection**.
8. For **Credential Guard Configuration**, choose **Enabled
   with UEFI lock**.

###### Note

The remaining policy settings are not required to enable Credential Guard and can be left
as **Not Configured**.

The following image displays the VBS settings configured as described
previously:

![Virtualization Based Security Group Policy Object settings with Turn On Virtualization Based Security enabled.](images/vbs-credential-guard-gpo-enabled.png) 9. Reboot the instance to apply the settings.

## Verify that Credential Guard is running

You can use the Microsoft System Information (`Msinfo32.exe`) tool to confirm
that Credential Guard is running.

###### Important

You must first reboot the instance to finish applying the policy settings required to
enable Credential Guard.

###### To verify Credential Guard is running

1. Connect to your instance using the Remote Desktop Protocol (RDP). For more
   information, see [Connect to your Windows instance using an RDP client](connect-rdp.md "connect-rdp.md").
2. Within the RDP session to your instance, open the Start menu and search for
   `cmd` to start a command prompt.
3. Open System Information by running the following command:
   `msinfo32.exe`
4. The Microsoft System Information tool lists the details for VBS configuration. Next
   to Virtualization-based security Services, confirm that **Credential
   Guard** appears as **Running**.

The following image displays VBS is running as described previously:

![An image of the Microsoft System Information Tool with the Virtualization-based security line showing a status of Running, confirming Credential Guard is running.](images/vbs-credential-guard-msinfo32-enabled.png)
