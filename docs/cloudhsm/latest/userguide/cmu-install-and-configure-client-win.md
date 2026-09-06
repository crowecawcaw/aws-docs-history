

# Install and configure the AWS CloudHSM client for CMU (Windows)
<a name="cmu-install-and-configure-client-win"></a>

To work with a hardware security module (HSM) in your AWS CloudHSM cluster on Windows using the cloudhsm\_mgmt\_util (CMU), you need the AWS CloudHSM client software for Windows. You should install it on the Windows Server instance that you created previously. 

**Note**  
If you are updating the client, existing configuration files from previous installations are *not* overwritten.
The AWS CloudHSM client installer for Windows automatically registers the Cryptography API: Next Generation (CNG) and Key Storage Provider (KSP). To uninstall the client, run the installer again and follow the uninstall instructions.
If you are using Linux, you can install the Linux client. For more information, see [Install and configure the AWS CloudHSM client for CMU (Linux)](cmu-install-and-configure-client-linux.md). 

**To install (or update) the latest Windows client and command line tools**

1. Connect to your Windows Server instance.

1. Download the [AWSCloudHSMClient-latest.msi installer](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMClient-latest.msi).

1. If installing Client SDK 3 on cloudhsm\_mgmt\_util, complete the following steps to ensure all the nodes in the cluster are synced.

   1. Run **configure.exe -a {{<IP of one of the HSMs>}}**.

   1. Restart the client service.

   1. Run **configure.exe -m**.

1. Go to your download location and run the installer (**AWSCloudHSMClient-latest.msi**) with administrative privilege.

1. Follow the installer instructions, then choose **Close** after the installer has finished.

1. Copy your self-signed issuing certificate—[the one that you used to sign the cluster certificate](initialize-cluster.md#sign-csr)—to the `C:\ProgramData\Amazon\CloudHSM` folder. 

1. Run the following command to update your configuration files. Be sure to stop and start the client during reconfiguration if you are updating it:

   ```
   PS C:\> & "C:\Program Files\Amazon\CloudHSM\configure.exe" -a {{<HSM IP address>}}
   ```

1. Go to [Activate the cluster in AWS CloudHSM](activate-cluster.md).