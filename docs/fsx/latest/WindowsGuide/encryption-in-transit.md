# Encryption of data in transit

Encryption of data in transit is supported on file shares that are mapped on a
compute instance that supports SMB protocol 3.0 or newer. This includes all Windows
versions starting from Windows Server 2012 and Windows 8, and all Linux clients with
Samba client version 4.2 or newer. Amazon FSx for Windows File Server automatically encrypts data in transit
using SMB encryption as you access your file system without the need for you to modify
your applications.

SMB encryption uses AES-128-GCM or AES-128-CCM (with the GCM variant being chosen if the
client supports SMB 3.1.1) as its encryption algorithm, and also provides data integrity
with signing using SMB Kerberos session keys. The use of AES-128-GCM leads to better performance,
for example, up to a 2x performance improvement when copying large files over encrypted
SMB connections.

To meet compliance requirements for always encrypting data-in-transit, you can limit file system access
to only allow access to clients that support SMB encryption. You can also enable or disable
in-transit encryption per file share or to the entire file system. This allows you to have
a mix of encrypted and unencrypted file shares on the same file system.

## Managing encryption in transit

You can use a set of custom PowerShell commands to control the encryption of your data in
transit between your FSx for Windows File Server file system and clients. You can limit file system
access to only clients supporting SMB encryption so that data-in-transit is always
encrypted. When enforcement is turned on for encryption of data-in-transit, users accessing the file system
from clients that do not support SMB 3.0 encryption will not be able to access file shares for which encryption is turned on.

You can also control encryption of data-in-transit on a file share-level instead of file server-level.
You can use file share-level encryption controls to have a mix of encrypted and unencrypted file shares on
the same file system if you want to enforce encryption in-transit for some file shares that have sensitive data,
and allow all users to access some other file shares. Server-wide encryption has precedence over share level encryption.
If global encryption is enabled, you cannot selectively disable encryption for certain shares.

You can manage in-transit encryption on your file system using the Amazon FSx CLI for
remote management on PowerShell. To learn how to use this CLI, see [Using the Amazon FSx CLI for PowerShell](administering-file-systems.md#remote-pwrshell "administering-file-systems.md#remote-pwrshell").

Following are commands that you can use to manage user in-transit encryption on your
file system.

| Encryption in Transit Command                       | Description                                                                                                                                                                                                                                              |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Get-FSxSmbServerConfiguration**                   | Retrieves the Server Message Block (SMB) server configuration. In the system response<br>you can determine the encryption in transit settings for your filesystem based on the values for the<br>`EncryptData` and `RejectUnencryptedAccess` properties. |
| **Set-FSxSmbServerConfiguration**                   | This command has two options for configuring in-transit encryption globally on the file system:<br>• `-EncryptData $True                                                                                                                                 | $False`– Set this parameter to`True`<br>to turn on in-transit data encryption. Set this parameter to `False`to turn off<br>in-transit data encryption.<br>•`-RejectUnencryptedAccess $True | $False` – Set this parameter to<br>`True`to disallow clients that do not support encryption to access the file system.<br>Set this parameter to`False` to allow clients that do not support encryption to<br>access the file system. |
| **Set-FSxSmbShare -name `name` -EncryptData $True** | Set this parameter to `True` to turn on in-transit data encryption for the share.<br>Set this parameter to `False` to turn off in-transit data encryption for the share.                                                                                 |

The online help for each command provides a reference of all command options. To
access this help, run the command with **-?**, for example
**Get-FSxSmbServerConfiguration -?**.
