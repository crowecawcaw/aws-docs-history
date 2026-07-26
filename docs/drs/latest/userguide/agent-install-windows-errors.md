# Windows agent installation errors

This page covers errors that you might encounter when you install the AWS Elastic Disaster Recovery agent on Windows source servers. Each section describes the error message, its cause, and the resolution.

###### Topics

- [Error: This app can't run on your PC](#error-app-cant-run "#error-app-cant-run")
- [Error: Cannot open self or archive](#error-corrupted-installer "#error-corrupted-installer")
- [Error: TLS connection error downloading installer](#error-tls-connection "#error-tls-connection")
- [Error: The directory is not empty](#error-directory-not-empty "#error-directory-not-empty")
- [Error: Certificate verification failed](#error-certificate-verify-failed "#error-certificate-verify-failed")
- [Error: BitLocker is not supported](#error-bitlocker "#error-bitlocker")
- [Error: net.exe or sc.exe not found](#error-net-sc-path "#error-net-sc-path")

## Error: This app can't run on your PC

**Error message:** **`This app can't run on your PC`** when you run `AwsReplicationWindowsInstaller.exe`.

**Cause:** Windows is running in 32-bit mode. AWS Elastic Disaster Recovery requires a 64-bit operating system.

**Resolution:**

1. Verify the system architecture. Open **Settings**, choose **System**, and then choose **About**. Check the **System type** field.
2. If the value is `32-bit operating system, x64-based processor`, you are running 32-bit Windows on 64-bit hardware. Reinstall Windows as 64-bit.
3. If the value is `32-bit operating system, x86-based processor`, the hardware does not support 64-bit. You cannot use AWS Elastic Disaster Recovery on this server.
4. If the system is 64-bit but the error still appears, check for AppLocker policies, SmartScreen, or Windows Defender Application Control blocking the executable. Right-click `AwsReplicationWindowsInstaller.exe` and select **Run as administrator**.

## Error: Cannot open self or archive

**Error message:** **`Cannot open self AwsReplicationWindowsInstaller.exe or archive`**

**Cause:** The installer file is corrupted or the download was incomplete due to a network interruption or browser timeout.

**Resolution:**

1. Re-download the installer from the AWS Elastic Disaster Recovery console or direct URL.
2. Verify the file hash matches the published hash:

   1. Download the published hash:

   ```
   https://aws-elastic-disaster-recovery-hashes-`REGION`.s3.`REGION`.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512
   ```
   2. Compute the local hash in PowerShell:

   ```
   Get-FileHash .\AwsReplicationWindowsInstaller.exe -Algorithm SHA512
   ```
   3. Compare the two values. If they differ, download the installer again.

3. If the hash matches but the error persists, check if antivirus software quarantined or modified the file.

## Error: TLS connection error downloading installer

**Error message:** **`The underlying connection was closed: An unexpected error occurred on a send`**

**Cause:** The Windows server is using TLS 1.0 or 1.1 by default. AWS Elastic Disaster Recovery endpoints require TLS 1.2. This is common on Windows Server 2012 and earlier.

**Resolution:**

- **Per-session fix (PowerShell):**

```
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
```

- **Permanent fix:** Enable TLS 1.2 system-wide through the registry:

```
Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\.NETFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value 1 -Type DWord
Set-ItemProperty -Path 'HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v4.0.30319' -Name 'SchUseStrongCrypto' -Value 1 -Type DWord
```

- Restart PowerShell after applying registry changes.

## Error: The directory is not empty

**Error message:** **`OSError: [WinError 145] The directory is not empty`**

**Cause:** A previous installation attempt was interrupted, leaving temporary files that cannot be cleaned up. This can also be caused by antivirus locking files or Group Policy restrictions.

**Resolution:**

1. Run the installer as Administrator. Right-click `AwsReplicationWindowsInstaller.exe` and select **Run as administrator**.
2. Verify the user has Full Control permissions on the temporary directory shown in the error.
3. Temporarily disable antivirus or endpoint protection software.
4. Check that no Group Policy Object (GPO) blocks deletion of temporary files.
5. If a previous partial installation exists, uninstall it first through Add/Remove Programs.

## Error: Certificate verification failed

**Error message:** **`CERTIFICATE_VERIFY_FAILED`** or **`certificate verify failed`**

**Cause:** The Windows certificate store does not contain the Amazon Trust Services root CA certificates required to validate AWS Elastic Disaster Recovery endpoint TLS connections. This occurs on air-gapped servers or systems that cannot reach Windows Update.

**Resolution:**

- **Option 1 (internet access):** Run Windows Update, or open Microsoft Edge once. Windows auto-downloads trusted root CAs when a browser first connects to HTTPS sites.
- **Option 2 (no internet or air-gapped):** Download Amazon root certificates from [https://www.amazontrust.com/repository/](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/") and import them:

```
Import-Certificate -FilePath .\AmazonRootCA1.cer -CertStoreLocation Cert:\LocalMachine\Root
```

###### Important

Modifying the trusted certificate store is typically managed by system administrators. Consult your admin before importing certificates on production servers.

## Error: BitLocker is not supported

**Error message:** **`BitLocker is not supported. Please disable BitLocker and try again`**

**Cause:** AWS Elastic Disaster Recovery performs block-level replication and cannot read data from BitLocker-encrypted volumes. The replication driver requires direct block access.

**Resolution:**

1. Disable BitLocker on all volumes to be replicated:

```
manage-bde -off C:
```

2. Wait for decryption to complete. Check the status:

```
manage-bde -status C:
```

3. Run the installer again after decryption completes.

###### Note

BitLocker must remain disabled while using AWS Elastic Disaster Recovery.

###### Important

Disabling BitLocker decrypts the drive. Verify this is acceptable per your organization's security policy before proceeding.

## Error: net.exe or sc.exe not found

**Error message:** Installation fails because `net.exe` or `sc.exe` cannot be located.

**Cause:** The `C:\Windows\System32` directory is not included in the system PATH environment variable.

**Resolution:**

1. Verify in PowerShell:

```
$env:Path -split ';' | Where-Object { $_ -like '*System32*' }
```

2. If System32 is missing from PATH, add it permanently:

```
$machinePath = [System.Environment]::GetEnvironmentVariable('Path', 'Machine')
[System.Environment]::SetEnvironmentVariable('Path', $machinePath + ';C:\Windows\System32', 'Machine')
```

3. Restart the PowerShell session and run the installer again.
