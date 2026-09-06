

# Using Windows LAPS with AWS Managed Microsoft AD
<a name="ms_using_windows_laps"></a>

Windows Local Administrator Password Solution (Windows LAPS) automatically manages and backs up local administrator passwords on domain-joined Windows machines. Passwords are stored securely in Active Directory and rotated on a configurable schedule, eliminating the security risk of shared or static local administrator passwords across your fleet.

AWS Managed Microsoft AD supports Windows LAPS. The required Active Directory schema extensions and permissions are configured automatically. You only need to create a Group Policy Object (GPO) to enable LAPS on your domain-joined computers.

**Topics**
+ [Prerequisites](#ms_laps_prerequisites)
+ [How Windows LAPS works](#ms_laps_how_it_works)
+ [Verifying the LAPS schema](#ms_laps_verify_schema)
+ [Creating a LAPS Group Policy](#ms_laps_create_gpo)
+ [Configuring LAPS settings](#ms_laps_configure_settings)
+ [Applying the policy and triggering password rotation](#ms_laps_apply_policy)
+ [Retrieving passwords](#ms_laps_retrieve_passwords)
+ [Forcing password rotation](#ms_laps_force_rotation)
+ [Delegating LAPS access](#ms_laps_delegate_access)
+ [Verifying LAPS is working](#ms_laps_verify_working)
+ [Configuration reference](#ms_laps_config_reference)
+ [Troubleshooting Windows LAPS](#ms_laps_troubleshooting)
+ [Limitations](#ms_laps_limitations)
+ [Related resources](#ms_laps_related_resources)

## Prerequisites
<a name="ms_laps_prerequisites"></a>

To use Windows LAPS with AWS Managed Microsoft AD, you need the following:
+ An AWS Managed Microsoft AD directory (Standard or Enterprise edition).
+ Domain-joined Windows machines running Windows Server 2019 or later, or Windows 10/11 with the April 2023 cumulative update or later. For more information about launching instances, see [Ways to join an Amazon EC2 instance to your AWS Managed Microsoft AD](ms_ad_join_instance.md).
+ A domain-joined management instance with Remote Server Administration Tools (RSAT) for Active Directory and Group Policy Management installed.

## How Windows LAPS works
<a name="ms_laps_how_it_works"></a>

When Windows LAPS is configured through Group Policy, the following process occurs:

1. Each domain-joined computer generates a random password for its local Administrator account.

1. The computer stores the password in its own Active Directory computer object.

1. The password is automatically rotated based on your configured schedule (default: 30 days).

1. Authorized administrators retrieve the password from Active Directory when needed.

AWS Managed Microsoft AD handles the following automatically:
+ Active Directory schema extensions for LAPS attributes
+ Permissions for computer objects to store their own passwords
+ A delegated security group (AWS Delegated LAPS Administrators) for password retrieval

## Verifying the LAPS schema
<a name="ms_laps_verify_schema"></a>

Before configuring LAPS, verify that the required schema attributes are present in your directory.

**To verify the LAPS schema attributes**

1. Connect to a domain-joined Windows management instance using the Admin account for your AWS Managed Microsoft AD directory.

1. Open PowerShell and run the following command to confirm the Windows LAPS schema attributes are available:

   ```
   Get-ADObject -SearchBase ((Get-ADRootDSE).SchemaNamingContext) `
       -LDAPFilter "(lDAPDisplayName=computer)" `
       -Properties mayContain |
       Select-Object -ExpandProperty mayContain |
       Where-Object { $_ -like "*LAPS*" }
   ```

   You should see the following attributes listed:
   + `msLAPS-EncryptedDSRMPasswordHistory`
   + `msLAPS-EncryptedDSRMPassword`
   + `msLAPS-EncryptedPasswordHistory`
   + `msLAPS-EncryptedPassword`
   + `msLAPS-Password`
   + `msLAPS-PasswordExpirationTime`

   If these attributes are not present, contact AWS Support. The schema extension is applied automatically during directory creation and patching.

## Creating a LAPS Group Policy
<a name="ms_laps_create_gpo"></a>

Create a new GPO and link it to the organizational unit (OU) containing your computer objects.

**To create and link a LAPS GPO**
+ Run the following PowerShell command:

  ```
  New-GPO -Name "LAPS Policy" |
      New-GPLink -Target "OU=Computers,OU=corp,DC=corp,DC=example,DC=com"
  ```

  Replace the `-Target` value with the distinguished name of the OU that contains your computer objects.

## Configuring LAPS settings
<a name="ms_laps_configure_settings"></a>

After creating the GPO, configure the LAPS policy settings. At minimum, you must configure the backup directory to store passwords in Active Directory.

**To configure the backup directory**
+ 

  ```
  Set-GPRegistryValue -Name "LAPS Policy" `
      -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\LAPS" `
      -ValueName "BackupDirectory" -Type DWord -Value 2
  ```

### Enabling password encryption (recommended)
<a name="ms_laps_enable_encryption"></a>

Password encryption protects stored passwords so that only authorized principals can decrypt them.

**To enable password encryption**
+ 

  ```
  Set-GPRegistryValue -Name "LAPS Policy" `
      -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\LAPS" `
      -ValueName "ADPasswordEncryptionEnabled" -Type DWord -Value 1
  ```

**Important**  
When you enable encryption, you must also configure the encryption principal. By default, encrypted passwords can only be decrypted by Domain Admins. In AWS Managed Microsoft AD, the Admin account is not a member of Domain Admins, so you cannot retrieve passwords unless you set the encryption principal to a group that your Admin account belongs to.

**To configure the encryption principal**
+ 

  ```
  Set-GPRegistryValue -Name "LAPS Policy" `
      -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\LAPS" `
      -ValueName "ADPasswordEncryptionPrincipal" -Type String -Value "corp\AWS Delegated LAPS Administrators"
  ```

  Replace `corp` with your directory's NetBIOS name.

### Customizing password settings (optional)
<a name="ms_laps_password_settings"></a>

You can customize the password length, age, and complexity.

```
# Password length (default: 14, range: 8-64)
Set-GPRegistryValue -Name "LAPS Policy" `
    -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\LAPS" `
    -ValueName "PasswordLength" -Type DWord -Value 20

# Password age in days (default: 30, range: 1-365)
Set-GPRegistryValue -Name "LAPS Policy" `
    -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\LAPS" `
    -ValueName "PasswordAgeDays" -Type DWord -Value 14

# Password complexity (1=Upper+Lower, 2=+Digits, 3=+Special, 4=Improved)
Set-GPRegistryValue -Name "LAPS Policy" `
    -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\LAPS" `
    -ValueName "PasswordComplexity" -Type DWord -Value 4
```

### Managing a custom local administrator account (optional)
<a name="ms_laps_custom_account"></a>

By default, LAPS manages the built-in Administrator account (RID 500). To manage a different local account, configure the account name.

```
Set-GPRegistryValue -Name "LAPS Policy" `
    -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\LAPS" `
    -ValueName "AdministratorAccountName" -Type String -Value "LocalAdmin"
```

**Note**  
If you specify a custom account name, you must ensure that the account exists on the target machines. LAPS does not create the account.

## Applying the policy and triggering password rotation
<a name="ms_laps_apply_policy"></a>

After configuring the GPO, apply the policy on each managed computer and trigger LAPS policy processing.

**To apply the policy and trigger password rotation**
+ Run the following commands on each managed computer:

  ```
  gpupdate /force
  Invoke-LapsPolicyProcessing
  ```

  LAPS processes the policy automatically every hour. The commands above trigger immediate processing without waiting for the next cycle.

## Retrieving passwords
<a name="ms_laps_retrieve_passwords"></a>

Members of AWS Delegated LAPS Administrators or AWS Delegated Administrators can retrieve LAPS passwords.

**To retrieve a LAPS password**
+ 

  ```
  Get-LapsADPassword -Identity <ComputerName> -AsPlainText
  ```

  The following is example output:

  ```
  ComputerName        : SERVER01
  DistinguishedName   : CN=SERVER01,OU=Computers,OU=corp,DC=corp,DC=example,DC=com
  Account             : Administrator
  Password            : [PASSWORD]
  PasswordUpdateTime  : 6/2/2026 2:35:29 PM
  ExpirationTimestamp : 7/2/2026 2:35:29 PM
  Source              : EncryptedPassword
  DecryptionStatus    : Success
  AuthorizedDecryptor : corp\AWS Delegated LAPS Administrators
  ```

## Forcing password rotation
<a name="ms_laps_force_rotation"></a>

To immediately rotate a computer's password (for example, after a security incident), you can mark the password as expired and trigger a new rotation.

**To force password rotation from the management instance**
+ 

  ```
  Set-LapsADPasswordExpirationTime -Identity <ComputerName>
  ```

  The computer generates a new password on its next policy processing cycle.

**To force immediate rotation on the managed computer**
+ Run one of the following commands on the managed computer:

  ```
  Invoke-LapsPolicyProcessing
  ```

  Or:

  ```
  Reset-LapsPassword
  ```

## Delegating LAPS access
<a name="ms_laps_delegate_access"></a>

By default, the Admin account and members of AWS Delegated Administrators can retrieve LAPS passwords. To grant access to additional users, such as helpdesk staff, without giving them full administrative privileges, add them to the AWS Delegated LAPS Administrators group.

**To delegate LAPS password retrieval access**
+ 

  ```
  Add-ADGroupMember -Identity "AWS Delegated LAPS Administrators" -Members "HelpDeskTeam"
  ```

  The AWS Delegated LAPS Administrators group is located in the AWS Delegated Groups OU and can be managed by the Admin account.

## Verifying LAPS is working
<a name="ms_laps_verify_working"></a>

You can verify that LAPS is functioning correctly by checking event logs on managed computers and querying Active Directory from the management instance.

### Checking the event log on managed computers
<a name="ms_laps_verify_event_log"></a>

LAPS writes events to the `Microsoft-Windows-LAPS/Operational` log.

```
Get-WinEvent -LogName 'Microsoft-Windows-LAPS/Operational' -MaxEvents 5 | Format-List TimeCreated, Id, Message
```

Key event IDs:
+ **10018** — Password successfully updated in Active Directory
+ **10017** — Password update failed (check error code)
+ **10021** — Current policy configuration

### Verifying LAPS from the management instance
<a name="ms_laps_verify_from_mgmt"></a>

```
Get-ADComputer <ComputerName> -Properties msLAPS-PasswordExpirationTime |
    Select-Object Name, 'msLAPS-PasswordExpirationTime'
```

## Configuration reference
<a name="ms_laps_config_reference"></a>

All settings are configured under the following registry key:

```
HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\LAPS
```

The following table lists the available LAPS configuration settings.


| Setting | Registry value | Type | Default | Description | 
| --- | --- | --- | --- | --- | 
| BackupDirectory | 2 | DWord | Not configured | Required. Set to 2 for Active Directory. | 
| PasswordLength | 8-64 | DWord | 14 | Length of generated password. | 
| PasswordAgeDays | 1-365 | DWord | 30 | Days before password rotation. | 
| PasswordComplexity | 1-4 | DWord | 4 | 1=Letters, 2=\+Digits, 3=\+Special, 4=Improved. | 
| ADPasswordEncryptionEnabled | 0 or 1 | DWord | 0 | Enable password encryption. | 
| ADPasswordEncryptionPrincipal | Group name | String | Domain Admins | Who can decrypt passwords. | 
| AdministratorAccountName | Account name | String | Built-in Administrator | Which local account to manage. | 
| PostAuthenticationResetDelay | 0-24 | DWord | 24 | Hours after use before rotation. | 
| PostAuthenticationActions | 1-5 | DWord | 3 | Actions after password use (1=reset, 3=reset\+logoff, 5=reset\+reboot). | 

## Troubleshooting Windows LAPS
<a name="ms_laps_troubleshooting"></a>

The following table lists common issues and their resolutions.


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| Get-LapsADPassword returns no data | GPO not applied or computer hasn't processed policy | Run gpupdate /force then Invoke-LapsPolicyProcessing on the managed computer. | 
| Event 10017 with error 0x80070005 | Computer doesn't have permission to write its LAPS attributes | Contact AWS Support. SELF write permissions may need to be reapplied. | 
| "Access Denied" when retrieving password | User not in an authorized group | Add user to AWS Delegated LAPS Administrators. | 
| DecryptionStatus: Unauthorized | Encryption is enabled but ADPasswordEncryptionPrincipal was not configured (defaults to Domain Admins, which the Admin account is not a member of in AWS Managed Microsoft AD) | Set ADPasswordEncryptionPrincipal to corp\\AWS Delegated LAPS Administrators in your LAPS GPO, then run Reset-LapsPassword on the managed computer to generate a new password encrypted for the correct principal. | 
| Encrypted password can't be decrypted | User not in the encryption principal group | Configure ADPasswordEncryptionPrincipal to include your group, then run Reset-LapsPassword on the managed computer to re-encrypt with the new principal. | 
| LAPS not processing policy | GPO not linked to the correct OU | Verify with gpresult /r on the managed computer. | 
| Event 10108 — msLAPSCurrentPasswordVersion attribute not in schema | Expected behavior. This attribute requires a Windows Server 2025 forest schema and is not applicable to AWS Managed Microsoft AD. | This warning is informational and can be safely ignored. All LAPS functionality works without this attribute. It is only used for OS image rollback detection, which is a Windows Server 2025 feature. For more information, see Microsoft Windows LAPS documentation. | 

## Limitations
<a name="ms_laps_limitations"></a>
+ Windows LAPS requires Windows Server 2019 or later (or Windows 10/11 with the April 2023 cumulative update) on managed computers.
+ LAPS manages one local account per computer per GPO. To manage multiple accounts, use separate GPOs.
+ Password history is only available when encryption is enabled.

## Related resources
<a name="ms_laps_related_resources"></a>

The following resources are located on the Microsoft website and provide related information about Windows LAPS.
+ [Windows LAPS overview](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview)
+ [Windows LAPS Group Policy settings](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-management-policy-settings)
+ [Windows LAPS PowerShell cmdlets](https://learn.microsoft.com/en-us/powershell/module/laps/)