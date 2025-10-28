# Limit client access for your NFS file share

We recommend editing the NFS client access settings to to define a list of specific
client IP addresses or CIDR block ranges for NFS clients that are allowed to connect to
your NFS file share. If you choose not to limit access, any client on your network can
mount to your file share.

###### To limit client access for your NFS file share

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **File shares** from the navigation pane on the left
   side of the console page, and then choose the **File share ID**
   of the NFS file share that you want to edit.
3. From the **Actions** drop down menu, choose **Edit
   file share access settings**.

The **Access object** section displays a list of IP addresses
and CIDR blocks that are currently allowed to connect to the NFS file share. If
access is not currently limited, you will see an entry under **Allowed
clients** for the 0.0.0.0/0 CIDR block, which indicates that all
possible IPv4 addresses are allowed to connect. 4. Under **Allowed clients**, to the right of the 0.0.0.0/0 CIDR
block, choose **Remove**. 5. Choose **Add client**, and then provide an IP address or
address range in CIDR notation for the clients that you want to allow. 6. Repeat the previous step to add more IP addresses or ranges as necessary. If
make a mistake or need to revoke access, you can choose
**Remove** to the right of the IP address or range that you
want to delete from the list. 7. Choose **Save changes** when finished.
