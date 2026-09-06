

# Secure your Simple AD directory
<a name="simple_ad_security"></a>

**Important Notice**  
Simple AD is no longer open to new customers. For capabilities similar to Simple AD, explore AWS Managed Microsoft AD or AD Connector. For more information, see [Simple AD availability changes](simple-ad-availability-change.md).

This section describes considerations for securing your Simple AD environment.

**Topics**
+ [How to reset a Simple AD krbtgt account password](#simple_ad_reset_krbtgt_acct_pswd)

## How to reset a Simple AD krbtgt account password
<a name="simple_ad_reset_krbtgt_acct_pswd"></a>

The krbtgt account plays an important role in the Kerberos ticket exchanges. The krbtgt account is a special account used for Kerberos ticket-granting ticket (TGT) encryption, and it plays a crucial role in the security of the Kerberos authentication protocol. In Samba AD, krbtgt is represented as a (disabled) user account. The password to this account is randomly generated at the time the domain is provisioned. Access to this secret can result in undetectable total domain compromise as new Kerberos tickets can be printed without auditing. For more information, see [Samba documentation](https://wiki.samba.org/index.php/Samba_Security_Documentation#Particularly_critical_secret_attributes). 

 It is recommended to change this password regularly every 90 days. You can reset the krbtgt account password from an Amazon EC2 Windows instanced joined to your Simple AD.

**Note**  
AWS Simple AD is powered by Samba-AD. Samba-AD doesn't store N-1 hash for the krbtgt account. Therefore, when the krbtgt account password is reset, the Kerberos client will be required to negotiate a new Ticket Granting Ticket (TGT) during their next Service Ticket (ST) request. To minimize potential service disruptions, you should schedule the krbtgt account password resets outside of business hours. This approach mitigates impacts on ongoing operations and ensures smooth authentication continuity.

The following procedures shows how you can reset the krbtgt account password from an Amazon EC2 Windows instance.

**Prerequisites**
+ Before you can begin this procedure, complete the following:
  + You have domain joined an EC2 instance to your Simple AD directory.
    + For more information on how to join an EC2 Windows instance to a Simple AD, see [Joining an Amazon EC2 Windows instance to your Simple AD Active Directory](simple_ad_launching_instance.md). 
  + You have the Simple AD directory administrator credentials. You will be signing in as the Simple AD directory administrator for this procedure.

**Note**  
Some AWS services like Amazon WorkDocs and Amazon WorkSpaces, will create a Simple AD on your behalf.

**Reset Simple AD krbtgt account password**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the Amazon EC2 console, choose **Instances** and select the Windows Server instance. Then choose **Connect**.

1. In the **Connect to instance** page, choose **RDP client**.

1. In the **Windows Security** dialog box, copy your local administrator credentials for the Windows Server computer to sign in. The username can be in the following formats: `NetBIOS-Name\administrator` or `DNS-Name\administrator`. For example, `corp\administrator` would be the username if you followed the procedure in [Create your Simple AD](simple_ad_getting_started.md#how_to_create_simple_ad).

1. Once signed in to the Windows Server computer, open **Windows Administrative Tools** from the Start menu by choosing **Windows Administrative Tools** folder.  
![Windows Start menu showing Windows Administrative Tools folder expanded with system tools.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_5.png)

1. In the Windows Administrative Tools dashboard, open **Active Directory Users and Computers** by choosing **Active Directory User and Computers**.  
![Windows Administrative Tools folder showing Active Directory Users and Computers shortcut.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_6.png)

1. In the **Active Directory Users and Computers** window, select **View** and then choose **Enable Advanced Features**.  
![View menu with Advanced Features option selected.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_7.png)

1. In the **Active Directory Users and Computers** window, select **Users** from the left panel.  
![Active Directory Users and Computers navigation tree with Users folder highlighted.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_8.png)

1. Find the user named **krbtgt**, right click on it and select **Reset Password**.  
![Context menu with Reset Password option highlighted.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_9.png)

1. In the new window, enter the new password, enter it again, and then choose **OK** to reset the krbtgt account password.  
![Reset Password dialog with password fields, checkbox options, and OK and Cancel buttons.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_10.png)

1. In the Windows Administrative Tools dashboard, choose **Active Directory Sites and Services**.  
![Administrative Tools folder showing Active Directory Sites and Services among other shortcuts.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_11.png)

1. In the Active Directory Sites and Services window, expand **Site**, **Default-First-Site-Name**, and **Servers**.  
![Active Directory Sites and Services console showing expanded Servers node with NTDS Settings.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_12.png)

1. In the NTDS Settings window, right click on the server and select **Replicate Now**.  
![Context menu with Replicate Now option highlighted for a connection in NTDS Settings.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/simple_ad_krbtgt_acct_step_13.png)

1. Repeat steps 13 - 14 for your other servers.