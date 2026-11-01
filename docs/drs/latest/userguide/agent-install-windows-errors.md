

# Windows agent installation errors
<a name="agent-install-windows-errors"></a>

This page covers errors that you might encounter when you install the AWS Elastic Disaster Recovery agent on Windows source servers. Each section describes the error message, its cause, and the resolution.

**Topics**
+ [DRS-INST-011: Windows version not supported](#error-app-cant-run)
+ [DRS-INST-023: BitLocker is not supported](#error-bitlocker)
+ [DRS-INST-909: net.exe or sc.exe not found](#error-net-sc-path)
+ [Environment errors](#windows-environment-errors)

## DRS-INST-011: Windows version not supported
<a name="error-app-cant-run"></a>

**Error message:** Error code: DRS-INST-011 - Windows version not supported

**Cause:** The installer detected a Windows version or architecture that AWS Elastic Disaster Recovery does not support. AWS Elastic Disaster Recovery requires a 64-bit operating system. On 32-bit Windows, the installer cannot start, so Windows displays a generic compatibility error instead of this error code.

**Resolution:**

1. Verify the system architecture. Open **Settings**, choose **System**, and then choose **About**. Check the **System type** field.

1. If the value is `32-bit operating system, x64-based processor`, you are running 32-bit Windows on 64-bit hardware. Reinstall Windows as 64-bit.

1. If the value is `32-bit operating system, x86-based processor`, the hardware does not support 64-bit. You cannot use AWS Elastic Disaster Recovery on this server.

1. If the system is 64-bit but the error still appears, check for AppLocker policies, SmartScreen, or Windows Defender Application Control blocking the executable. Right-click `AwsReplicationWindowsInstaller.exe` and select **Run as administrator**.

## DRS-INST-023: BitLocker is not supported
<a name="error-bitlocker"></a>

**Error message:** Error code: DRS-INST-023 - BitLocker is not supported

**Cause:** AWS Elastic Disaster Recovery performs block-level replication and cannot read data from BitLocker-encrypted volumes. The replication driver requires direct block access.

**Resolution:**

1. Disable BitLocker on all volumes to be replicated:

   ```
   manage-bde -off C:
   ```

1. Wait for decryption to complete. Check the status:

   ```
   manage-bde -status C:
   ```

1. Run the installer again after decryption completes.

**Note**  
BitLocker must remain disabled while using AWS Elastic Disaster Recovery.

**Important**  
Disabling BitLocker decrypts the drive. Verify this is acceptable per your organization's security policy before proceeding.

## DRS-INST-909: net.exe or sc.exe not found
<a name="error-net-sc-path"></a>

**Error message:** Error code: DRS-INST-909 - net.exe or sc.exe not found

**Cause:** The `C:\Windows\System32` directory is not included in the system PATH environment variable.

**Resolution:**

1. Verify in PowerShell:

   ```
   $env:Path -split ';' | Where-Object { $_ -like '*System32*' }
   ```

1. If System32 is missing from PATH, add it permanently:

   ```
   $machinePath = [System.Environment]::GetEnvironmentVariable('Path', 'Machine')
   [System.Environment]::SetEnvironmentVariable('Path', $machinePath + ';C:\Windows\System32', 'Machine')
   ```

1. Restart the PowerShell session and run the installer again.

## Environment errors
<a name="windows-environment-errors"></a>

### Cannot open self or archive
<a name="error-corrupted-installer"></a>

**Error message:** Cannot open self AwsReplicationWindowsInstaller.exe or archive

**Cause:** The installer file is corrupted or the download was incomplete due to a network interruption or browser timeout.

**Resolution:**

1. Re-download the installer from the AWS Elastic Disaster Recovery console or direct URL.

1. Verify the file hash matches the published hash:

   1. Download the published hash:

      ```
      https://aws-elastic-disaster-recovery-hashes-{{REGION}}.s3.{{REGION}}.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512
      ```

   1. Compute the local hash in PowerShell:

      ```
      Get-FileHash .\AwsReplicationWindowsInstaller.exe -Algorithm SHA512
      ```

   1. Compare the two values. If they differ, download the installer again.

1. If the hash matches but the error persists, check if antivirus software quarantined or modified the file.

### TLS connection error downloading installer
<a name="error-tls-connection"></a>

**Error message:** The underlying connection was closed: An unexpected error occurred on a send

**Cause:** The Windows server is using TLS 1.0 or 1.1 by default. AWS Elastic Disaster Recovery endpoints require TLS 1.2. This is common on Windows Server 2012 and earlier.

**Resolution:**
+ **Per-session fix (PowerShell):**

  ```
  [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
  ```
+ **Permanent fix:** Enable TLS 1.2 system-wide through the registry:

  ```
  Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\.NETFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value 1 -Type DWord
  Set-ItemProperty -Path 'HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value 1 -Type DWord
  ```
+ Restart PowerShell after applying registry changes.

### The directory is not empty
<a name="error-directory-not-empty"></a>

**Error message:** OSError: [WinError 145] The directory is not empty

**Cause:** A previous installation attempt was interrupted, leaving temporary files that cannot be cleaned up. This can also be caused by antivirus locking files or Group Policy restrictions.

**Resolution:**

1. Run the installer as Administrator. Right-click `AwsReplicationWindowsInstaller.exe` and select **Run as administrator**.

1. Verify the user has Full Control permissions on the temporary directory shown in the error.

1. Temporarily disable antivirus or endpoint protection software.

1. Check that no Group Policy Object (GPO) blocks deletion of temporary files.

1. If a previous partial installation exists, uninstall it first through Add/Remove Programs.

### Certificate verification failed
<a name="error-certificate-verify-failed"></a>

**Error message:** CERTIFICATE\_VERIFY\_FAILED or certificate verify failed

**Cause:** The Windows certificate store does not contain the Amazon Trust Services root CA certificates required to validate AWS Elastic Disaster Recovery endpoint TLS connections. This occurs on air-gapped servers or systems that cannot reach Windows Update.

**Resolution:**
+ **Option 1 (internet access):** Run Windows Update, or open Microsoft Edge once. Windows auto-downloads trusted root CAs when a browser first connects to HTTPS sites.
+ **Option 2 (no internet or air-gapped):** Download the Amazon root certificates from the [Amazon Trust Services repository](https://www.amazontrust.com/repository/) on the amazontrust.com website, and then import them:

  ```
  Import-Certificate -FilePath .\AmazonRootCA1.cer -CertStoreLocation Cert:\LocalMachine\Root
  ```

  Before you import certificates on a production server, check with your system administrator, who typically manages the trusted certificate store.