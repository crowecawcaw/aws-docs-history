

# AWS Windows Server NitroTPM enabled AMIs
<a name="ami-windows-tpm"></a>

Amazon creates a set of AMIs that are pre-configured with NitroTPM and UEFI Secure Boot requirements, as follows:
+ The TPM 2.0 Command Response Buffer (CRB) driver is installed
+ NitroTPM is enabled
+ UEFI Secure Boot mode is enabled with Microsoft keys

For more detailed information about NitroTPM, see [NitroTPM for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the *Amazon EC2 User Guide*.

## Find Windows Server AMIs configured with NitroTPM and UEFI Secure Boot
<a name="ami-windows-tpm-find"></a>

AWS managed AMIs always include the AMI creation date as part of the name. The best way to ensure that your search returns the AMIs that you're looking for is to add date filtering for the name. Use one of the following command line options to find an AMI.

You can run the following commands from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) pre-installed. AWS CloudShell automatically configures your credentials. To run the PowerShell commands, run `pwsh`.

------
#### [ AWS CLI ]

**Find the latest NitroTPM and UEFI Secure Boot AMIs**  
Use the [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command to retrieve a list of the latest Windows Server AMIs that are configured for NitroTPM and UEFI Secure Boot.

```
aws ssm get-parameters-by-path \
    --path "/aws/service/ami-windows-latest" \
    --recursive \
    --query 'Parameters[*].{Name:Name,Value:Value}' \
    --output text | grep "TPM-Windows_Server" | sort
```

**Find a specific AMI**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command to retrieve Windows Server AMIs that are configured for NitroTPM and UEFI Secure Boot by filtering on the AMI name, the owner, the platform, and the creation date (year and month). Output is formatted as a table with columns for the AMI name and image ID.

```
aws ec2 describe-images \
    --owners amazon \
    --filters \
        "Name=name,Values=TPM-Windows_Server-*" \
        "Name=platform,Values=windows" \
        "Name=creation-date,Values={{2026-10}}*" \
    --query 'Images[].[Name,ImageId]' \
    --output text | sort
```

------
#### [ PowerShell ]

**Find the latest NitroTPM and UEFI Secure Boot AMIs**  
Use the [Get-SSMLatestEC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-SSMLatestEC2Image.html) cmdlet to retrieve a list of the latest Windows Server AMIs that are configured for NitroTPM and UEFI Secure Boot.

```
Get-SSMLatestEC2Image `
    -Path ami-windows-latest `
    -ImageName TPM-Windows* |
Sort-Object Name
```

**Find a specific AMI**  


Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet to retrieve Windows Server AMIs that are configured for NitroTPM and UEFI Secure Boot by filtering on the AMI name, the owner, the platform, and the creation date (year and month). Output is formatted as a table with columns for the AMI name and image ID.

```
Get-EC2Image `
    -Owner amazon `
    -Filter @(
        @{Name = "name"; Values = @("TPM-Windows*")}
        @{Name = "platform"; Values = @("windows")}
        @{Name = "creation-date"; Values = @("{{2026-10}}*")}
    ) |
Sort-Object Name |
Format-Table Name, ImageID -AutoSize
```

------

## Update Secure Boot certificates on Windows instances
<a name="ami-windows-tpm-update-secure-boot-certs"></a>

Microsoft is updating the Secure Boot certificates originally issued in 2011 to ensure Windows devices continue to verify trusted boot software. These older certificates begin expiring in June 2026. Devices that haven't received the newer 2023 certificates will continue to start and operate normally, and standard Windows updates will continue to install. However, these devices will no longer be able to receive new security protections for the early boot process, including updates to Windows Boot Manager, Secure Boot databases, revocation lists, or mitigations for newly discovered boot level vulnerabilities. For more information, see [Microsoft's Secure Boot documentation](https://aka.ms/GetSecureBoot).

**Important**  
Instances launched from NitroTPM enabled Windows AMIs release dated 2026.01.14 or earlier should follow the steps to update Secure Boot certificates on Windows instances. For Windows AMIs release dated 2026.02.11 or later, no further action is needed.

To update to the latest Secure Boot certificates (Microsoft Corporation KEK 2K CA 2023 and Windows UEFI CA 2023), you can either migrate to new instances launched from the latest Windows AMIs, or follow the steps below to update existing instances.

1. Run Windows Update and reboot the instance if prompted.

1. Download the following PowerShell script to the instance: [Update-EC2SecureBootCertificate.ps1](https://s3.amazonaws.com/ec2-downloads-windows/Scripts/Update-EC2SecureBootCertificate.ps1).

1. Open a PowerShell command prompt as an Administrator, and run the downloaded PowerShell script.

   ```
   .\Update-EC2SecureBootCertificate.ps1
   ```

1. Reboot your instance if prompted.

If you encounter errors during the certificate update, contact [AWS Support](https://aws.amazon.com/premiumsupport/).