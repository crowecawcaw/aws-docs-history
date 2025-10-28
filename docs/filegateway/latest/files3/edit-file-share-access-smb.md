# Limit user and group access for your SMB

file share

We recommend adding allowed or denied users or groups to limit access to your file
share. If you don't, the file share will be available to all authenticated
users.

###### To edit SMB access settings

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **File shares**, and then choose the SMB file share
   that you want to edit.
3. For **Actions**, choose **Edit file share access
   settings**.
4. In the **User and group file share access** section, choose
   your settings.

For **Allowed users and groups**, choose **Add
allowed user** or **Add allowed group** and enter
an AD user or group that you want to allow file share access. Repeat this
process to allow as many users and groups as necessary. Any users not in the
**Allowed user and groups** list will be denied
access.

For **Denied users and groups**, choose **Add denied
user** or **Add denied group** and enter an AD
user or group that you want to deny file share access. Repeat this process to
deny as many users and groups as necessary. If the **Allowed users and
groups** list is empty, all users other than those on the
**Denied users and groups** list will be granted
access.

###### Note

Enter only the AD user or group name. The domain name is implied by the
membership of the gateway in the specific AD that the gateway is joined
to.

If you don't specify any allowed or denied users or groups, any
authenticated AD user can export the file share.
