# Configure local groups for your

gateway

Local Group settings allow you to grant Active Directory users or groups special
permissions for the SMB file shares on your gateway.

You can use Local Group settings to assign Gateway Admin permissions. Gateway
Admins can use the Shared Folders Microsoft Management Console snap-in to
force-close files that are open and locked.

###### Note

You must add at least one Gateway Admin user or group before you can join your
gateway to an Active Directory domain.

###### To assign Gateway Admins

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Gateways**, then choose the gateway for which
   you want to edit SMB settings.
3. From the **Actions** dropdown menu, choose **Edit
   SMB settings**, then choose **Local Group
   settings**.
4. In the **Local Group settings** section, choose your
   settings. This section appears only for file shares that use Active
   Directory.

For **Gateway Admins**, add Active Directory users and
groups that you want to grant local Gateway Admin permissions. Add one user
or group per line, including the domain name. For example,
`corp\Domain Admins`. To create additional lines,
choose **Add new Gateway Admin**.

###### Note

Editing Gateway Admins disconnects and reconnects all SMB file
shares. 5. Choose **Save changes**, then choose
**Proceed** to acknowledge the warning message that
appears.
