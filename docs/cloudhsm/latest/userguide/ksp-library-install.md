# Install the Key storage provider (KSP) for AWS CloudHSM Client SDK 5

Use the following sections to install the Key storage provider (KSP) for AWS CloudHSM Client SDK 5.

###### Note

To run a single HSM cluster with Client SDK 5, you must first manage
client key durability settings by setting
`disable_key_availability_check` to `True`.
For more information, see [Key
Synchronization](manage-key-sync.md "manage-key-sync.md") and [Client SDK 5 Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

###### To install and configure the Key Storage Provider (KSP)

1. Install the Key Storage Provider (KSP) for Windows Server on x86_64 architecture, open PowerShell as an administrator and run the following command:

```
`PS C:\>` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-latest.msi -Outfile C:\AWSCloudHSMKSP-latest.msi`
```

```
`PS C:\>` `Start-Process msiexec.exe -ArgumentList '/i C:\AWSCloudHSMKSP-latest.msi /quiet /norestart /log C:\client-install.txt' -Wait`
```

2. Use the configure tool to specify the location of the issuing certificate. For instructions, see [Specify the location of the issuing certificate](cluster-connect.md#specify-cert-location "cluster-connect.md#specify-cert-location").
3. To connect to your cluster, see [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to").
4. You can find the Key Storage Provider (KSP) files in the following locations:
   - Windows binaries:

   ```
   `C:\Program Files\Amazon\CloudHSM`
   ```

   Windows configuration scripts and log files:

   ```
   `C:\ProgramData\Amazon\CloudHSM`
   ```
