# Change the Default Internet

Explorer Home Page for Users' Streaming Sessions in Amazon AppStream 2.0

You can use Group Policy to change the default Internet Explorer home page for users'
streaming sessions. Alternatively, if you do not have Group Policy in your environment
or prefer not to use Group Policy, you can use the AppStream 2.0 Template User account
instead.

###### Note

The following steps apply to Windows fleets only.

###### Contents

- [Use Group Policy
  to Change the Default Internet Explorer Home Page](customize-fleets-change-ie-homepage-group-policy.md "customize-fleets-change-ie-homepage-group-policy.md")
- [Use the AppStream 2.0
  Template User Account to Change the Default Internet Explorer Home Page](customize-fleets-change-ie-homepage-template-user.md "customize-fleets-change-ie-homepage-template-user.md")

###### To change the default Internet Explorer home page by using Group Policy

preferences

You can use Group Policy preferences to set a default home page that users can
change. For more information about working with Group Policy preferences, see [Configure a Registry Item](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753092(v=ws.11)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753092(v=ws.11)") and [Group Policy Preferences Getting Started Guide](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731892(v=ws.10)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731892(v=ws.10)") in the Microsoft
documentation.

1. In your directory or on a domain controller, open the command prompt as an
   administrator, type `gpmc.msc`, and then press ENTER.
2. In the left console tree, select the OU in which you want to create a new GPO,
   or use an existing GPO, and then do either of the following:
   - Create a new GPO by opening the context (right-click) menu and
     choosing **Create a GPO in this domain, Link it here**.
     For **Name**, provide a descriptive name for this
     GPO.
   - Select an existing GPO.

3. Open the context menu for the GPO, and choose **Edit**.
4. Under **User Configuration**, expand
   **Preferences**, and then choose **Windows
   Settings**.
5. Open the context (right-click) menu for **Registry** and
   choose **New**, **Registry Item**.
6. In the **New Registry Properties** dialog box, specify the
   following registry settings for Group Policy to configure:
   - For **Action**, choose **Update**.
   - For **Hive**, choose
     **HKEY_CURRENT_USER**.
   - For **Key Path**, browse to and select
     HKEY_CURRENT_USER\SOFWARE\Microsoft\Internet Explorer\Main.
   - For **Value Name**, enter **Start
     Page**.
   - For **Value Data**, enter your home page URL.

7. On the **Common** tab, choose **Apply
   Once**, **Do not Re-Apply**.

###### Note

To enable your users to choose the **Use Default** button
in their Internet Explorer browser settings and reset their default home
page to your company home page, you can also set a value for
Default_Page_URL without choosing **Apply Once** and
**Do not Re-Apply**. 8. Choose **OK** and close the GPMC.
