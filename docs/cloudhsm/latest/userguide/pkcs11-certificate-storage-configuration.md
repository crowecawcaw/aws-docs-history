# Enabling certificate storage

You can enable certificate storage on hsm2m.medium clusters using the PKCS #11 library configuration
tool. This feature is available in SDK versions 5.13 and later. For a list of operations that support
the certificate object type, see
[Certificate storage API operations](pkcs11-certificate-storage-api.md "pkcs11-certificate-storage-api.md").

To enable certificate storage, follow these steps for your operating system:

Linux

- ###### **Enable certificate storage**

Run the following command:

```
`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 --enable-certificate-storage`
```

Windows

- ###### **Enable certificate storage**

Open a command prompt and run the following command:

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" --enable-certificate-storage`
```
