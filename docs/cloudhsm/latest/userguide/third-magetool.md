

# Use Microsoft Manifest Generation and Editing Tool (Mage.exe) with AWS CloudHSM to sign files
<a name="third-magetool"></a>

**Note**  
AWS CloudHSM supports only the 64-bit Mage tool included in the Windows SDK for .NET Framework 4.8.1 and later.

The following topics provide an overview of how to use [ Mage.exe ](https://learn.microsoft.com/en-us/dotnet/framework/tools/mage-exe-manifest-generation-and-editing-tool) with AWS CloudHSM.

**Topics**
+ [Step 1: Set up the prerequisites](#magetool-prereqs)
+ [Step 2: Create a signing certificate](#magetool-csr)
+ [Step 3: Sign a file](#magetool-sign)

## Step 1: Set up the prerequisites
<a name="magetool-prereqs"></a>

To use Microsoft Mage.exe with AWS CloudHSM, you need the following:
+ An Amazon EC2 instance running a Windows operating system
+ A certificate authority (CA), either self-maintained or from a third-party provider
+ An active AWS CloudHSM cluster in the same virtual private cloud (VPC) as your EC2 instance, with at least one HSM
+ A crypto user (CU) to own and manage keys in the AWS CloudHSM cluster
+ An unsigned file or executable
+ The Microsoft Windows Software Development Kit (SDK)

**To set up the prerequisites for using AWS CloudHSM with Mage.exe**

1. Launch a Windows EC2 instance and an AWS CloudHSM cluster by following the instructions in the [Getting Started](getting-started.md) section of this guide.

1. If you want to host your own Windows Server CA, complete steps 1 and 2 in [Configuring Windows Server as a Certificate Authority with AWS CloudHSM](win-ca-overview-sdk5.md). Otherwise, use your publicly trusted third-party CA.

1. Download and install Microsoft Windows SDK for .NET Framework 4.8.1 or later on your Windows EC2 instance:
   + [Microsoft Windows SDK 10](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk)

   The `mage.exe` executable is part of the Windows SDK Tools. The default installation location is:

   ```
   C:\Program Files (x86)\Windows Kits\{{<SDK version>}}\bin\{{<version number>}}\x64\Mage.exe
   ```

After completing these steps, you can use the Microsoft Windows SDK, your AWS CloudHSM cluster, and your CA to [create a signing certificate](#magetool-csr).

## Step 2: Create a signing certificate
<a name="magetool-csr"></a>

Now that you've installed the Windows SDK on your EC2 instance, you can use it to generate a certificate signing request (CSR). The CSR is an unsigned certificate that you submit to your CA for signing. In this example, we use the `certreq` executable included with the Windows SDK to generate the CSR.

**To generate a CSR using the certreq executable**

1. Connect to your Windows EC2 instance. For more information, see [Connect to Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-connect-to-instance-windows) in the *Amazon EC2 User Guide*.

1. Create a file named `request.inf` with the following content. Replace the `Subject` information with your organization's details:

   ```
   [Version]
   Signature= $Windows NT$
   [NewRequest]
   Subject = "C={{<Country>}},CN={{<www.website.com>}},O={{<Organization>}},OU={{<Organizational-Unit>}},L={{<City>}},S={{<State>}}"
   RequestType=PKCS10
   HashAlgorithm = SHA256
   KeyAlgorithm = RSA
   KeyLength = 2048
   ProviderName = "CloudHSM Key Storage Provider"
   KeyUsage = "CERT_DIGITAL_SIGNATURE_KEY_USAGE"
   MachineKeySet = True
   Exportable = False
   ```

   For an explanation of each parameter, see [Microsoft's documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1#BKMK_New).

1. Run `certreq.exe` to generate the CSR:

   ```
   certreq.exe -new request.inf request.csr
   ```

   This command generates a new key pair on your AWS CloudHSM cluster and uses the private key to create the CSR.

1. Submit the CSR to your CA. If you're using a Windows Server CA, follow these steps:

   1. Open the CA tool:

      ```
      certsrv.msc
      ```

   1. In the new window, right-click the CA server's name. Choose **All Tasks**, and then choose **Submit new request**.

   1. Navigate to the location of `request.csr` and choose **Open**.

   1. Expand the **Server CA** menu and navigate to the **Pending Requests** folder. Right-click the request you just created, choose **All Tasks**, and then choose **Issue**.

   1. Navigate to the **Issued Certificates** folder.

   1. Choose **Open** to view the certificate, and then choose the **Details** tab.

   1. Choose **Copy to File** to start the Certificate Export Wizard. Save the DER-encoded X.509 file to a secure location as `signedCertificate.cer`.

   1. Exit the CA tool and run the following command to move the certificate file to the Personal Certificate Store in Windows:

      ```
      certreq.exe -accept signedCertificate.cer
      ```

You can now use your imported certificate to [sign a file](#magetool-sign).

## Step 3: Sign a file
<a name="magetool-sign"></a>

Now that you have Mage.exe and your imported certificate, you can sign a file. You need to know the certificate's SHA-1 hash, or *thumbprint*. The thumbprint ensures that Mage.exe only uses certificates verified by AWS CloudHSM. In this example, we use PowerShell to get the certificate's hash.

**To obtain a certificate's thumbprint and use it to sign a file**

1. Navigate to the directory containing `mage.exe`. The default location is:

   ```
   C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8.1 Tools\x64
   ```

1. To create a sample application file using Mage.exe, run the following command:

   ```
   mage.exe -New Application -ToFile C:\Users\Administrator\Desktop\sample.application
   ```

1. Open PowerShell as an administrator and run the following command:

   ```
   Get-ChildItem -path cert:\LocalMachine\My
   ```

   Copy the `Thumbprint`, `Key Container`, and `Provider` values from the output.  
![The certificate's hash will be displayed as the thumbprint, keycontainer and provider in the output](http://docs.aws.amazon.com/cloudhsm/latest/userguide/images/certstore-my-certificate.png)

1. Sign your file by running the following command:

   ```
   mage.exe -Sign -CertHash {{<thumbprint>}} -KeyContainer {{<keycontainer>}} -CryptoProvider {{<CloudHSM Key Storage Provider/Cavium Key Storage Provider>}} C:\Users\Administrator\Desktop\{{<sample.application>}}
   ```

   If the command is successful, PowerShell returns a success message.

1. To verify the signature on the file, use the following command:

   ```
   mage.exe -Verify -CryptoProvider {{<CloudHSM Key Storage Provider/Cavium Key Storage Provider>}} C:\Users\Administrator\Desktop\{{<sample.application>}}
   ```