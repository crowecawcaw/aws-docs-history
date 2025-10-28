# One-time file system setup tasks using the Amazon FSx CLI for remote management on PowerShell

Use the following Amazon FSx CLI for Remote Management on PowerShell
commands to quickly implement the file system administration tasks following our best practices.

## Managing storage consumption

Use the following commands to manage your file system storage consumption.

- To turn on data deduplication with the default schedule, run the following command.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock { Enable-FsxDedup }
```

Optionally, use the following command to get data deduplication operating on your files soon
after a file is created, without requiring any minimum file age.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock { Set-FSxDedupConfiguration -MinimumFileAgeDays 0 }
```

For more information, see [Reducing storage costs with Data Deduplication](managing-storage-configuration.md#using-data-dedup "managing-storage-configuration.md#using-data-dedup").

- Use the following command to turn on user storage quotas in “Track” mode, which is for reporting purposes only and not for enforcement.

```
$QuotaLimit = `Quota limit in bytes`
$QuotaWarningLimit = `Quota warning threshold in bytes`
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock { Enable-FSxUserQuotas -Track -DefaultLimit $Using:QuotaLimit -DefaultWarningLimit $Using:QuotaWarningLimit }

```

For more information, see [Managing storage quotas](managing-user-quotas.md "managing-user-quotas.md").

## Turning on shadow copies to enable end-users to recover files and folders to previous versions

Turn on shadow copies with the default schedule (weekdays 7 AM and 12 noon), as
follows.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock { Set-FsxShadowStorage -Default }

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock { Set-FsxShadowCopySchedule -Default -Confirm:$False}

```

For more information, see [Configuring shadow copies to use the default storage and schedule](setting-up-fsx-shadow-copies.md "setting-up-fsx-shadow-copies.md").

## Enforcing encryption in transit

The following command enforces encryption for clients connecting to your file system.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock { Set-FsxSmbServerConfiguration -EncryptData $True -RejectUnencryptedAccess $True -Confirm:$False}
```

You can close all open sessions and force clients currently connected to reconnect using encryption.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock { Close-FSxSmbSession -Confirm:$False}
```

For more information, see [Managing encryption in transit](encryption-in-transit.md#manage-encrypt-in-transit "encryption-in-transit.md#manage-encrypt-in-transit") and
[User sessions and open files](manage-sessions-and-files.md "manage-sessions-and-files.md").
