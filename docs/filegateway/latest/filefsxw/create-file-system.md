Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Create an Amazon FSx for Windows File Server file system

To create an Amazon FSx File Gateway in AWS Storage Gateway, the first step is to create an
Amazon FSx for Windows File Server file system. If you've already created an Amazon FSx file system, go to the
next step, [Create and activate an
Amazon FSx File Gateway](create-gateway-file.md "create-gateway-file.md").

###### Note

The following limitations apply when writing to an Amazon FSx file system from an
FSx File Gateway:

- Your Amazon FSx file system and your FSx File Gateway must be owned by the same AWS
  account and located in the same AWS Region.
- Each gateway can support five attached file systems. When attaching a file
  system, the Storage Gateway console notifies you if the selected gateway is at
  capacity. In that case, you must choose a different gateway or detach a file
  system before you can attach another one.
- FSx File Gateway supports soft storage quotas (issuing warnings when users
  surpass their data limits), but does not support hard quotas (enforcing data
  limits by denying write access). Soft quotas are supported for all users
  except the Amazon FSx admin user. For more information about setting up storage
  quotas, see [Storage
  quotas](../../../fsx/latest/WindowsGuide/managing-user-quotas.md "../../../fsx/latest/WindowsGuide/managing-user-quotas.md") in the _Amazon FSx for Windows File Server User
  Guide_.
- We don't recommend using Microsoft Distributed File System (DFS) to
  redirect users to your Amazon FSx file system through FSx File Gateway. Instead,
  configure DFS to redirect directly to the Amazon FSx file system in the
  AWS Cloud as described in [Grouping multiple
  file systems with DFS Namespaces](../../../fsx/latest/WindowsGuide/group-file-systems.md "../../../fsx/latest/WindowsGuide/group-file-systems.md") in the
  _Amazon FSx for Windows File Server User Guide_.
- Some file operations on the FSx File Gateway, such as top-level folder renames or permission changes, can result in multiple file operations that lead to a high I/O load on your FSx for Windows File Server file system. If your file system doesn't have enough performance resources for your workload, the file system might delete [shadow copies](../../../fsx/latest/WindowsGuide/shadow-copies-fsxW.md "../../../fsx/latest/WindowsGuide/shadow-copies-fsxW.md") because it prioritizes availability for ongoing I/O over historical shadow copy retention.

In the Amazon FSx console, check the **Monitoring and performance** page to see if your file system is under-provisioned. If it is, you can switch to SSD storage, increase throughput capacity, or increase SSD IOPS to handle your workload.

###### To create an FSx for Windows File Server file system

1. Open the AWS Management Console at [https://console.aws.amazon.com/fsx/home/](https://console.aws.amazon.com/fsx/home/ "https://console.aws.amazon.com/fsx/home/"), and choose the Region that you want
   to create your gateway in.
2. Follow the instructions in [Getting Started with
   Amazon FSx](../../../fsx/latest/WindowsGuide/getting-started.md "../../../fsx/latest/WindowsGuide/getting-started.md") in the _Amazon FSx for Windows File Server User Guide_.
