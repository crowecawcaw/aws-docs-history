# Creating an AWS Managed Microsoft AD user

You can create AWS Managed Microsoft AD users
with the Active Directory Administration Tools and PowerShell.
Before you can create user with the Active Directory Administration Tools, you will need to complete the procedure in [Installing Active Directory Administration
Tools for AWS Managed Microsoft AD](ms_ad_install_ad_tools.md "ms_ad_install_ad_tools.md").

Active Directory Administration Tools
Use the following procedure to create an AWS Managed Microsoft AD user with Active Directory Administration Tools.

1. Connect to the instance where the Active Directory Administration Tools were installed.
2. Open the Active Directory Users and Computers tool from the Windows Start menu. There is a shortcut to
   this tool found in the **Windows Administrative Tools** folder.

###### Tip

You can run the following from a command prompt on the instance to
open the Active Directory Users and Computers tool box directly.

```
%SystemRoot%\system32\dsa.msc
```

3. In the directory tree, select an
   OU under your directory's NetBIOS name OU where you want to store your user (for example, `corp\Users`). For more information about the OU structure used by directories in AWS, see [What gets created with your
   AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md").

![Active Directory Users and Computers tool showing example OU structure.](/images/directoryservice/latest/admin-guide/images/create-security-groups-OU.png) 4. On the **Action** menu, choose **New**, and then
choose **User** to open the new user wizard. 5. On the first page of the wizard, enter the values for the following fields, and then
choose **Next**.

    * **First name**
    * **Last name**
    * **User logon name**

6. On the second page of the wizard, enter a temporary password in
   **Password** and **Confirm Password**. Make sure the
   **User must change password at next logon** option is selected. None of
   the other options should be selected. Choose **Next**.
7. On the third page of the wizard, verify that the new user information is correct and
   choose **Finish**. The new user will appear in the
   **Users** folder.

PowerShell
Use the following procedure to create an AWS Managed Microsoft AD user with PowerShell.

1. Connect to the instance joined to your Active Directory domain as the Active Directory administrator.
2. Open PowerShell.
3. Type the following command replacing the username `jane.doe` with
   the username of the user you want to create. You will be prompted by PowerShell
   to provide a password for the new user. For more information on Active Directory password complexity
   requirements, see [Microsoft documentation](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements "https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements"). For more information on the
   New-ADUser command, see [Microsoft documentation](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps "https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps").

```
New-ADUser -Name "`jane.doe`" -Enabled $true -AccountPassword (Read-Host -AsSecureString 'Password')
```
