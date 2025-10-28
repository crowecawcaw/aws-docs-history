# Delete a user's account with an Amazon EC2 instance

You can use the following procedure to delete a user with an Amazon EC2 instance that's joined to your AWS Managed Microsoft AD.

###### Note

Before you complete this procedure, you must install the Active Directory administration tools.
For more information, see [Install the Active Directory administration tools](ms_ad_install_ad_tools.md "ms_ad_install_ad_tools.md").

###### To delete a user

1. Open the Active Directory Users and Computers tool. There is a shortcut to this tool in the **Windows Administrative Tools** folder.

###### Tip

You can run the following from a command prompt on the instance to open the Active Directory Users and Computers tool box directly.

```
%SystemRoot%\system32\dsa.msc
```

2. In the directory tree, select the OU containing the user that you want to delete (for example, Corp\Users).
3. Select the user you wish to delete. On the **Action** menu, choose **Delete**.
4. A dialog box will appear prompting you to confirm you want to delete the user. Choose **Yes** to delete the user.
   Deleted users are stored temporarily in the AD Recycle Bin.
   For more information about the AD Recycle Bin, see [The AD Recycle Bin: Understanding, Implementing, Best Practices, and Troubleshooting](https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/the-ad-recycle-bin-understanding-implementing-best-practices-and/ba-p/396944 "https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/the-ad-recycle-bin-understanding-implementing-best-practices-and/ba-p/396944") in
   Microsoft's Ask the Directory Services Team blog.
