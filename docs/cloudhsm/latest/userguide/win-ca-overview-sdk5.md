# Configure Windows Server as a certificate authority (CA) with

Client SDK 5

In a public key infrastructure (PKI), a certificate authority (CA) is a trusted entity
that issues digital certificates. These digital certificates bind a public key to an identity
(a person or organization) by means of public key cryptography and digital signatures. To
operate a CA, you must maintain trust by protecting the private key that signs the
certificates issued by your CA. You can store the private key in the HSM in your AWS CloudHSM
cluster, and use the HSM to perform the cryptographic signing operations.

In this tutorial, you use Windows Server and AWS CloudHSM to configure a CA. You install the AWS CloudHSM
client software for Windows on your Windows server, then add the Active Directory Certificate
Services (AD CS) role to your Windows Server. When you configure this role, you use an AWS CloudHSM key
storage provider (KSP) to create and store the CA's private key on your AWS CloudHSM cluster. The KSP
is the bridge that connects your Windows server to your AWS CloudHSM cluster. In the last step, you
sign a certificate signing request (CSR) with your Windows Server CA.

For more information, see the following topics:

###### Topics

- [Step 1: Set up the prerequisites](#win-ca-prerequisites-sdk5 "#win-ca-prerequisites-sdk5")
- [Step 2: Create a Windows Server CA with AWS CloudHSM](#win-ca-setup-sdk5 "#win-ca-setup-sdk5")
- [Step 3: Sign a certificate signing request
  (CSR) with your Windows Server CA with AWS CloudHSM](#win-ca-sign-csr-sdk5 "#win-ca-sign-csr-sdk5")

## Step 1: Set up the prerequisites

To set up Windows Server as a certificate authority (CA) with AWS CloudHSM, you need the
following:

- An active AWS CloudHSM cluster with at least one HSM.
- An Amazon EC2 instance running a Windows Server operating system with the AWS CloudHSM client software
  for Windows installed. This tutorial uses Microsoft Windows Server 2016.
- A cryptographic user (CU) to own and manage the CA's private key on the HSM.

###### To set up the prerequisites for a Windows Server CA with AWS CloudHSM

1. Complete the steps in [Getting started](getting-started.md "getting-started.md"). When you launch the Amazon EC2 client, choose a Windows Server AMI. This tutorial uses
   Microsoft Windows Server 2016. When you complete these steps, you have an active cluster
   with at least one HSM. You also have an Amazon EC2 client instance running Windows Server with
   the AWS CloudHSM client software for Windows installed.
2. (Optional) Add more HSMs to your cluster. For more information, see [Adding an HSM to an AWS CloudHSM cluster](add-hsm.md "add-hsm.md").
3. Connect to your client instance. For more information, see [Connect to Your
   Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
4. Create a crypto user (CU) using [Managing HSM users with CloudHSM CLI](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md")
   or [Managing HSM users with CloudHSM Management Utility (CMU)](manage-hsm-users-cmu.md "manage-hsm-users-cmu.md"). Keep track of the
   CU user name and password. You will need them to complete the next step.
5. [Set the login credentials for the HSM](ksp-library-authentication.md "ksp-library-authentication.md"),
   using the CU user name and password that you created in the previous step.
6. In step 5, if you used Windows Credentials Manager to set HSM credentials, download [`psexec.exe`](https://live.sysinternals.com/psexec.exe "https://live.sysinternals.com/psexec.exe") from SysInternals to run the following command as _NT Authority\SYSTEM_:

```
psexec.exe -s "C:\Program Files\Amazon\CloudHsm\tools\set_cloudhsm_credentials.exe" --username `<USERNAME>` --password `<PASSWORD>`
```

Replace `<USERNAME>` and `<PASSWORD>` with the HSM credentials.

To create a Windows Server CA with AWS CloudHSM, go to [Create Windows Server CA](#win-ca-setup-sdk5 "#win-ca-setup-sdk5").

## Step 2: Create a Windows Server CA with AWS CloudHSM

To create a Windows Server CA, you add the Active Directory Certificate Services (AD CS) role
to your Windows Server. When you add this role, you use an AWS CloudHSM key storage provider (KSP) to
create and store the CA's private key on your AWS CloudHSM cluster.

###### Note

When you create your Windows Server CA, you can choose to create a root CA or a subordinate
CA. You typically make this decision based on the design of your public key infrastructure and
the security policies of your organization. This tutorial explains how to create a root CA for
simplicity.

###### To add the AD CS role to your Windows Server and create the CA's private key

1. If you haven't already done so, connect to your Windows server. For more information,
   see [Connect to Your Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
2. On your Windows server, start **Server Manager**.
3. In the **Server Manager** dashboard, choose **Add roles and
   features**.
4. Read the **Before you begin** information, and then choose
   **Next**.
5. For **Installation Type**, choose **Role-based or feature-based
   installation**. Then choose **Next**.
6. For **Server Selection**, choose **Select a server from the server
   pool**. Then choose **Next**.
7. For **Server Roles**, do the following:
   1. Select **Active Directory Certificate Services**.
   2. For **Add features that are required for Active Directory Certificate
      Services**, choose **Add Features**.
   3. Choose **Next** to finish selecting server roles.

8. For **Features**, accept the defaults, and then choose
   **Next**.
9. For **AD CS**, do the following:
   1. Choose **Next**.
   2. Select **Certification Authority**, and then choose
      **Next**.

10. For **Confirmation**, read the confirmation information, and then choose
    **Install**. Do not close the window.
11. Choose the highlighted **Configure Active Directory Certificate Services on the destination server** link.
12. For **Credentials**, verify or change the credentials displayed. Then choose
    **Next**.
13. For **Role Services**, select **Certification Authority**.
    Then choose **Next**.
14. For **Setup Type**, select **Standalone CA**. Then choose
    **Next**.
15. For **CA Type**, select **Root CA**. Then choose
    **Next**.

###### Note

You can choose to create a root CA or a subordinate CA based on the design of your
public key infrastructure and the security policies of your organization. This tutorial
explains how to create a root CA for simplicity. 16. For **Private Key**, select **Create a new private key**.
Then choose **Next**. 17. For **Cryptography**, do the following:

    1. For **Select a cryptographic provider**, choose one of the
     **CloudHSM Key Storage Provider** options from the menu. These are the
     AWS CloudHSM key storage providers. For example, you can choose **RSA#CloudHSM Key
     Storage Provider**.
    2. For **Key length**, choose one of the key length options.
    3. For **Select the hash algorithm for signing certificates issued by this
     CA**, choose one of the hash algorithm options.Choose **Next**.

18. For **CA Name**, do the following:
    1.  (Optional) Edit the common name.
    2.  (Optional) Type a distinguished name suffix.Choose **Next**.

19. For **Validity Period**, specify a time period in years, months, weeks, or
    days. Then choose **Next**.
20. For **Certificate Database**, you can accept the default values, or
    optionally change the location for the database and the database log. Then choose
    **Next**.
21. For **Confirmation**, review the information about your CA; Then choose
    **Configure**.
22. Choose **Close**, and then choose **Close** again.

You now have a Windows Server CA with AWS CloudHSM. To learn how to sign a certificate signing
request (CSR) with your CA, go to [Sign a CSR](#win-ca-sign-csr-sdk5 "#win-ca-sign-csr-sdk5").

## Step 3: Sign a certificate signing request

(CSR) with your Windows Server CA with AWS CloudHSM

You can use your Windows Server CA with AWS CloudHSM to sign a certificate signing request (CSR).
To complete these steps, you need a valid CSR. You can create a CSR in several ways, including
the following:

- Using OpenSSL
- Using the Windows Server Internet Information Services (IIS) Manager
- Using the certificates snap-in in the Microsoft Management Console
- Using the **certreq** command line utility on Windows

The steps for creating a CSR are outside the scope of this tutorial. When you have a CSR,
you can sign it with your Windows Server CA.

###### To sign a CSR with your Windows Server CA

1. If you haven't already done so, connect to your Windows server. For more information,
   see [Connect to Your Instance](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the _Amazon EC2 User Guide_.
2. On your Windows server, start **Server Manager**.
3. In the **Server Manager** dashboard, in the top right corner, choose
   **Tools**, **Certification Authority**.
4. In the **Certification Authority** window, choose your computer
   name.
5. From the **Action** menu, choose **All Tasks**,
   **Submit new request**.
6. Select your CSR file, and then choose **Open**.
7. In the **Certification Authority** window, double-click
   **Pending Requests**.
8. Select the pending request. Then, from the **Action** menu, choose
   **All Tasks**, **Issue**.
9. In the **Certification Authority** window, double-click
   **Issued Requests** to view the signed certificate.
10. (Optional) To export the signed certificate to a file, complete the following
    steps:
    1. In the **Certification Authority** window, double-click the
       certificate.
    2. Choose the **Details** tab, and then choose **Copy to
       File**.
    3. Follow the instructions in the **Certificate Export
       Wizard**.

You now have a Windows Server CA with AWS CloudHSM, and a valid certificate signed by the Windows
Server CA.
