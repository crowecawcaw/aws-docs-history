

# Creating a Simple AD user
<a name="simple_ad_manage_users_groups_create_user"></a>

Use the following procedure to create a user with an Amazon EC2 instance that is joined to your Simple AD directory. Before you can create users, you need to complete the procedures in [Installing the Active Directory Administration Tools](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_install_ad_tools.html).

**Note**  
When using Simple AD, if you create a user account on a Linux instance with the option "Force user to change password at first login," that user will not be able to initially change their password using **kpasswd**. In order to change the password the first time, a domain administrator must update the user password using the Active Directory Management Tools.

**To create a user**

1. Connect to the instance where the Active Directory Administration Tools were installed.

1. Open the Active Directory Users and Computers tool from the Windows Start menu. There is a shortcut to this tool found in the **Windows Administrative Tools** folder.
**Tip**  
You can run the following from a command prompt on the instance to open the Active Directory Users and Computers tool box directly.  

   ```
   %SystemRoot%\system32\dsa.msc
   ```

1. In the directory tree, select an OU under your directory's NetBIOS name OU where you want to store your user (for example, **corp\\Users**). For more information about the OU structure used by directories in AWS, see [What gets created with your AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md).  
![Active Directory Users and Computers tool showing example OU structure.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/create-security-groups-OU.png)

1. On the **Action** menu, choose **New**, and then choose **User** to open the new user wizard.

1. On the first page of the wizard, enter the values for the following fields, and then choose **Next**.
   + **First name**
   + **Last name**
   + **User logon name**

1. On the second page of the wizard, enter a temporary password in **Password** and **Confirm Password**. Make sure the **User must change password at next logon** option is selected. None of the other options should be selected. Choose **Next**.

1. On the third page of the wizard, verify that the new user information is correct and choose **Finish**. The new user will appear in the **Users** folder.