# Creating a Simple AD group

Use the following procedure to create a security group with an Amazon EC2 instance that is joined
to your Simple AD directory. Before you can create security groups, you need to complete the procedures
in [Installing the Active Directory Administration Tools](simple_ad_install_ad_tools.md "simple_ad_install_ad_tools.md").

###### To create a group

1. Connect to the instance where the Active Directory Administration Tools were installed.
2. Open the Active Directory Users and Computers tool. There is a shortcut to
   this tool in the **Administrative Tools** folder.

###### Tip

You can run the following from a command prompt on the instance to
open the Active Directory Users and Computers tool box directly.

```
%SystemRoot%\system32\dsa.msc
```

3. In the directory tree, select an
   OU under your directory's NetBIOS name OU where you want to store your group (for example, Corp\Users).
   For more information about the OU structure used by directories in AWS, see [What gets created with your
   AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md").

![Active Directory Users and Computers tool showing example OU structure.](images/create-security-groups-OU.png) 4. On the **Action** menu, click **New**, and then
click **Group** to open the new group wizard. 5. Type a name for the group in **Group name**, select a **Group
scope** that meets your needs, and select **Security** for the **Group
type**. For more information on Active Directory group scope and security groups, see [Active Directory security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups") in Microsoft Windows Server documentation. 6. Click **OK**. The new security group will appear in the
**Users** folder.
