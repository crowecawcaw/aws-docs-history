# Provide guest access to your file share

You can configure your S3 File Gateway to allow guest access for any user that is able to
provide the correct guest account username and password. If you want this to be the
only method by which users can access your file gateway, then you do not need to
join the gateway to a Microsoft Active Directory domain. You can also use this guest
access method to create file shares on an S3 File Gateway that is a member of an Active
Directory domain.

When you configure a file share to use the **Guest Access**
authentication method, the guest access username is `smbguest`. Before
you can create a file share using guest access, you need to change the default
password for the `smbguest` user.

You can use the following procedure to change the password for the guest user
`smbguest`.

###### To change the guest access password

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Gateways** from the navigation pane on the left
   side of the console page, and then choose the **Name** of
   the gateway for which you want to provide guest access.
3. From the **Actions** drop down menu, choose
   **Edit SMB settings**, and then choose **Guest
   access settings**.
4. For **Guest password**, enter the guest access password
   you want to set, and then choose **Save changes**.
