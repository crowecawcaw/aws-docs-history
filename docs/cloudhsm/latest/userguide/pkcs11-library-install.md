# Install the PKCS #11 library for AWS CloudHSM Client SDK 5

This topic provides instructions for installing the latest version of the PKCS #11 library for the
AWS CloudHSM Client SDK 5 version series. For more information about the Client SDK or PKCS #11 library, see [Using the Client SDK](use-hsm.md "use-hsm.md") and [PKCS #11 library](pkcs11-library.md "pkcs11-library.md").

With Client SDK 5, you are not required to install or run a client daemon.

To run a single HSM cluster with Client SDK 5, you must first manage client key
durability settings by setting `disable_key_availability_check` to
`True`. For more information, see [Key
Synchronization](manage-key-sync.md "manage-key-sync.md") and [Client SDK 5 Configure
Tool](configure-sdk-5.md "configure-sdk-5.md").

For more information about the PKCS #11 library in Client SDK 5, see [PKCS #11 library](pkcs11-library.md "pkcs11-library.md").

###### Note

To run a single HSM cluster with Client SDK 5, you must first manage
client key durability settings by setting
`disable_key_availability_check` to `True`.
For more information, see [Key
Synchronization](manage-key-sync.md "manage-key-sync.md") and [Client SDK 5 Configure Tool](configure-sdk-5.md "configure-sdk-5.md").

###### To install and configure the PKCS #11 library

1. Use the following commands to download and install the PKCS #11 library.

Amazon Linux 2023
Install the PKCS #11 library for Amazon Linux 2023 on X86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-latest.amzn2023.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-pkcs11-latest.amzn2023.x86_64.rpm`
```

Install the PKCS #11 library for Amazon Linux 2023 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-latest.amzn2023.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-pkcs11-latest.amzn2023.aarch64.rpm`
```

Amazon Linux 2
Install the PKCS #11 library for Amazon Linux 2 on X86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-latest.el7.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-pkcs11-latest.el7.x86_64.rpm`
```

Install the PKCS #11 library for Amazon Linux 2 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-latest.el7.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-pkcs11-latest.el7.aarch64.rpm`
```

RHEL 9 (9.2+)
Install the PKCS #11 library for RHEL 9 on X86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-latest.el9.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-pkcs11-latest.el9.x86_64.rpm`
```

Install the PKCS #11 library for RHEL 9 on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-latest.el9.aarch64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-pkcs11-latest.el9.aarch64.rpm`
```

RHEL 8 (8.3+)
Install the PKCS #11 library for RHEL 8 on X86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-latest.el8.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-pkcs11-latest.el8.x86_64.rpm`
```

Ubuntu 24.04 LTS
Install the PKCS #11 library for Ubuntu 24.04 LTS on X86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_latest_u24.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-pkcs11_latest_u24.04_amd64.deb`
```

Install the PKCS #11 library for Ubuntu 24.04 LTS on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_latest_u24.04_arm64.deb`
```

```
`$` `sudo apt install ./cloudhsm-pkcs11_latest_u24.04_arm64.deb`
```

Ubuntu 22.04 LTS
Install the PKCS #11 library for Ubuntu 22.04 LTS on X86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_latest_u22.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-pkcs11_latest_u22.04_amd64.deb`
```

Install the PKCS #11 library for Ubuntu 22.04 LTS on ARM64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_latest_u22.04_arm64.deb`
```

```
`$` `sudo apt install ./cloudhsm-pkcs11_latest_u22.04_arm64.deb`
```

Ubuntu 20.04 LTS
Install the PKCS #11 library for Ubuntu 20.04 LTS on X86_64 architecture:

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Focal/cloudhsm-pkcs11_latest_u20.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-pkcs11_latest_u20.04_amd64.deb`
```

Windows Server
Install the PKCS #11 library for Windows Server on X86_64 architecture:

    1. Download [PKCS #11 library for Client SDK 5](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-latest.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-latest.msi").
    2. Run the PKCS #11 library installer (**AWSCloudHSMPKCS11-latest.msi**) with Windows administrative
     privilege.

2. Use the configure tool to specify the location of the issuing
   certificate. For instructions, see [Specify the location of the issuing certificate](cluster-connect.md#specify-cert-location "cluster-connect.md#specify-cert-location").
3. To connect to your cluster, see [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to").
4. You can find the PKCS #11 library files in the following locations:
   - Linux binaries, configuration scripts, and log files:

   ```
   `/opt/cloudhsm`
   ```

   Windows binaries:

   ```
   `C:\Program Files\Amazon\CloudHSM`
   ```

   Windows configuration scripts and log files:

   ```
   `C:\ProgramData\Amazon\CloudHSM`
   ```
