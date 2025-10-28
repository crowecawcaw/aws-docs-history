# Installing Active Directory Administration

Tools for AWS Managed Microsoft AD

You can manage your AWS Managed Microsoft AD Active Directory using Active Directory Domain Services and
Active Directory Lightweight Directory Services Tools. To use Active
Directory Domain Services and Active Directory Lightweight Directory Services
Tools, you will need to install them. The following procedures walks you through
how you can install these tools on an Amazon EC2 Windows Server instance or with a
PowerShell command. Alternatively, you can launch a directory administration EC2
instance which already has these tools installed.

EC2 Windows Server instance
Before you can begin this procedure, complete the following:

1. Create an AWS Managed Microsoft AD Active Directory. For more information, see [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
2. Launch and join an EC2 Windows Server instance to your AWS Managed Microsoft AD
   Active Directory. The EC2 instance needs the following policies to
   create users and groups:
   `AmazonSSMManagedInstanceCore` and
   `AmazonSSMDirectoryServiceAccess`. For more
   information, see [Launching a directory administration instance in your
   AWS Managed Microsoft AD Active Directory](console_instance.md "console_instance.md") and [Joining an Amazon EC2 Windows instance to your AWS Managed Microsoft AD
   Active Directory](launching_instance.md "launching_instance.md").
3. You will need the credentials for your Active Directory domain Administrator.
   These credentials were created when the AWS Managed Microsoft AD was created. If you
   followed the procedure in [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory"), your
   Administrator username includes your NetBIOS name,
   `corp\admin`.

###### Installing Active Directory administration tools on a EC2 Windows Server

instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the Amazon EC2 console, choose **Instances**, select the
   Windows Server instance, and then choose
   **Connect**.
3. In the **Connect to instance** page, choose
   **RDP client**.
4. In the **RDP client** tab, choose **Download
   Remote Desktop File**, then choose **Get
   Password** to retrieve your password.
5. In the **Get Windows password**, choose
   **Upload private key file**. Choose the .pem
   private key file associated with the Windows Server instance. After
   uploading the private key file, select **Decrypt
   password**.
6. In the **Windows Security** dialog box, copy your
   local administrator credentials for the Windows Server computer to sign
   in. The username can be in the following formats:
   ``NetBIOS-Name`\admin`
or ``DNS-Name`\admin`. For
   example, `corp\admin` would be the username if you
   followed the procedure in [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
7. Once signed in to the Windows Server instance, open **Server
   Manager** from the Start menu by choosing **Server
   Manager**.
8. In the **Server Manager Dashboard**, choose
   **Add roles and features**.
9. In the **Add Roles and Features Wizard** choose
   **Installation Type**, select **Role-based
   or feature-based installation**, and choose
   **Next**.
10. Under **Server Selection**, make sure the local
    server is selected, and choose **Features** in the left
    navigation pane.
11. In the **Features** tree, select and open
    **Remote Server Administration Tools**,
    **Role Administration Tools**, and **AD DS
    and AD LDS Tools**. With **AD DS and AD LDS
    Tools** selected, **Active Directory module for
    PowerShell**, **AD DS Tools**,
    and **AD LDS Snap-ins and Command-Line Tools** are
    selected. Scroll down and select **DNS Server Tools**,
    and then choose **Next**.

![Installing Microsoft AD Tools, the Add Roles and Features Wizard Features Tree with tools selected.](images/ms-install-ad-tools.png) 12. Review the information and choose **Install**. When
the feature installation is finished, the Active Directory Domain
Services and Active Directory Lightweight Directory Services Tools are
available from the Start menu in the **Administrative
Tools** folder.

PowerShell
You can install the Active Directory Administration Tools
using PowerShell. For example, you can install the Active Directory
remote administration tools from a PowerShell prompt using `Install-WindowsFeature RSAT-ADDS`. For more
information, see [Install-WindowsFeature](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature?view=winserver2012r2-ps "https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature?view=winserver2012r2-ps") on the Microsoft website.

Directory administration instance
You can launch a directory administration EC2 instance in the AWS Management Console
that already has the Active Directory Domain Services and Active Directory
Lightweight Directory Services Tools installed by following the procedures in
[Launching a directory administration instance in your
AWS Managed Microsoft AD Active Directory](console_instance.md "console_instance.md").
