# Install and configure the AWS CloudHSM client for

KMU (Windows)

To work with a hardware security module (HSM) in your AWS CloudHSM cluster on Windows using the
key_mgmt_util (KMU), you need the AWS CloudHSM client software for Windows. You should install it
on the Windows Server instance that you created previously.

###### To install (or update) the latest Windows client and command line tools

1. Connect to your Windows Server instance.
2. Download the latest (**AWSCloudHSMClient-latest.msi**) from the [downloads page](client-history.md "client-history.md").
3. Go to your download location and run the installer (**AWSCloudHSMClient-latest.msi**) with administrative privilege.
4. Follow the installer instructions, then choose **Close** after the
   installer has finished.
5. Copy your self-signed issuing certificate—[the one
   that you used to sign the cluster certificate](initialize-cluster.md#sign-csr "initialize-cluster.md#sign-csr")—to the
   `C:\ProgramData\Amazon\CloudHSM` folder.
6. Run the following command to update your configuration files. Be sure to stop and start the
   client during reconfiguration if you are updating it:

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\configure.exe" -a `<HSM IP address>``
```

7. Go to [Activate the cluster in AWS CloudHSM](activate-cluster.md "activate-cluster.md").
   **Notes**:

- If you are updating the client, existing configuration files from previous
  installations are _not_ overwritten.
- The AWS CloudHSM client installer for Windows automatically registers the Cryptography API: Next Generation (CNG) and Key Storage Provider (KSP). To
  uninstall the client, run the installer again and follow the uninstall
  instructions.
- If you are using Linux, you can install the Linux client. For more information,
  see [Install and configure the AWS CloudHSM client
  for KMU (Linux)](kmu-install-and-configure-client-linux.md "kmu-install-and-configure-client-linux.md").
