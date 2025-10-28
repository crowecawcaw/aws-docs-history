Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Attach an Amazon FSx for Windows File Server file system

You must have an FSx for Windows File Server file system before you can attach it to an FSx File Gateway. If
you don't have a file system, you must create one. For instructions, see [Step 1:
Create Your File System](../../../fsx/latest/WindowsGuide/getting-started-step1.md "../../../fsx/latest/WindowsGuide/getting-started-step1.md") in the _Amazon FSx for Windows File Server User Guide_.

The next step is to attach an Amazon FSx file system to the gateway. When you attach an Amazon FSx
file system, all the file shares on the file system are made available to Amazon FSx File Gateway
(FSx File Gateway) for you to mount.

###### Note

The following limitations apply when writing to an Amazon FSx file system from
Amazon FSx File Gateway:

- Your Amazon FSx file system and your FSx File Gateway must be owned by the same
  AWS account and located in the same AWS Region.
- Each gateway can support up to five attached file systems. When you're
  attaching a file system, the Storage Gateway console notifies you if the selected
  gateway is at capacity. In that case, you must choose a different gateway or
  detach a file system before you can attach another one.
- FSx File Gateway supports soft storage quotas (which warn you when users surpass
  their data limits), but does not support hard quotas (which enforce data limits
  by denying write access). Soft quotas are supported for all users except the
  Amazon FSx admin user. For more information about setting up storage quotas, see
  [Storage
  quotas](../../../fsx/latest/WindowsGuide/managing-user-quotas.md "../../../fsx/latest/WindowsGuide/managing-user-quotas.md") in the Amazon FSx User Guide.
- We don't recommend using Microsoft Distributed File System (DFS) to redirect
  users to your Amazon FSx file system through FSx File Gateway. Instead, configure DFS to
  redirect directly to the Amazon FSx file system in the AWS Cloud as described in
  [Grouping multiple file
  systems with DFS Namespaces](../../../fsx/latest/WindowsGuide/group-file-systems.md "../../../fsx/latest/WindowsGuide/group-file-systems.md") in the
  _Amazon FSx for Windows File Server User Guide_.

###### To attach an Amazon FSx file system

1.  In the Storage Gateway console, on the **FSx file systems** >
    **Attach FSx file system** page, complete the following fields
    in the **FSx file system settings** section:
    - For **FSx file system name**, choose the file system that
      you want to attach from the dropdown list.
    - For **Local Endpoint IP address**, enter the gateway IP
      address that clients will use to browse file shares on the FSx file
      system.

    ###### Note

        + You must specify an IP address for each file system attached
         to the gateway.
        + For Amazon EC2 gateways, you can specify the private IP address of
         the EC2 instance, unless it is already in use by a different
         file system, in which case you must add a new private address to
         the gateway, then restart it. For more information, see [Multiple IP
         addresses](../../../AWSEC2/latest/UserGuide/MultipleIP.md "../../../AWSEC2/latest/UserGuide/MultipleIP.md") in the *Amazon EC2 User
         Guide*.
        + For on-premises gateways, you can specify the IP address of
         the primary network interface (static or DHCP), unless it is
         already in use by a different file system, in which case you
         must provide a different IP address from the same subnet as the
         primary interface, which will be made available as a virtual IP.
         Do not use an IP address assigned to any network interface other
         than the primary.

2.  In the **Service account settings** section, provide the service
    account sign-in credentials that is associated with the Amazon FSx file system.

###### Note

This service account must have Backup Operators privileges from the Active
Directory service that is associated with your Amazon FSx file systems or have
equivalent permissions.

###### Important

To ensure sufficient permissions to files, folders, and file metadata, we
recommend that you make the service account a member of the file system
administrators group.

If you are using AWS Directory Service for Microsoft Active Directory with
Amazon FSx for Windows File Server, the service account must be a member of the AWS Delegated
FSx Administrators group.

If you are using a self-managed Active Directory with Amazon FSx for Windows File Server, we
recommend that the service account be a member of the _custom delegated
file system administrators_ group you specified for file system
administration when you created your Amazon FSx file system.

If you chose not to create a _custom delegated file system
administrators_ group when you created the Amazon FSx filesystem, the
default group is _Domain Admins_. While you can make the
service account a member of this group instead, it is not recommended as a best
practice.

For more information, see [Delegating privileges to your Amazon FSx service account](../../../fsx/latest/WindowsGuide/self-managed-AD-best-practices.md#connect_delegate_privileges "../../../fsx/latest/WindowsGuide/self-managed-AD-best-practices.md#connect_delegate_privileges") in the
_Amazon FSx for Windows File Server User Guide_. 3. In the **Audit logs** section, choose **Existing log
groups**, and choose the log that you want to use to monitor access to
your Amazon FSx file system. You can create a new one. If you don't want to monitor your
system, choose
**Disable logging**. 4. For **Automated cache refresh setting**, if you want your cache
to refresh automatically, choose **Set refresh interval** and
specify an interval between 5 minutes and 30 days. 5. (Optional) In the **Tags** section, choose **Add new
tag** to add one or more keys and a value for tagging your
settings. 6. Choose **Next** and review the settings. To change your settings,
you can choose **Edit** in each section. 7. When you are done, choose **Finish**.
**Next step**

[Mount and use your Amazon FSx file share](use-fsxw-gateway.md "use-fsxw-gateway.md")
