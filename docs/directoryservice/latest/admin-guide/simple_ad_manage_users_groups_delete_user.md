# Deleting a Simple AD user

Use the following procedure to delete a user with an Amazon EC2 Windows instance that is joined to your Simple AD directory.

###### To delete a user

1. Connect to the instance where the Active Directory Administration Tools were installed.
2. Open the Active Directory Users and Computers tool from the Windows Start menu. There is a shortcut to this tool found in the **Windows Administrative Tools** folder.

###### Tip

You can run the following from a command prompt on the instance to open the Active Directory Users and Computers tool box directly.

```
%SystemRoot%\system32\dsa.msc
```

3. In the directory tree, select the OU containing the user that you want to delete (for example, `corp\Users`).

![Active Directory Users and Computers tool showing example OU structure.](images/create-security-groups-OU.png) 4. Select the user you wish to delete. On the **Action** menu, choose **Delete**. 5. A dialog box will appear prompting you to confirm you want to delete the user. Choose **Yes** to delete the user. This permanently deletes the selected user.
