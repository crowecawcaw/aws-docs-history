Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Configuring additional cache

storage

As your application needs change, you can increase the gateway's cache storage
capacity. You can add storage capacity to your gateway without interrupting
functionality or causing downtime. When you add more storage, you do so with the gateway
VM turned on.

###### Important

When adding cache to an existing gateway, you must create new disks on the gateway
host hypervisor or Amazon EC2 instance. Do not remove or change the size of existing
disks that have already been allocated as cache.

###### To configure additional cache

storage for your gateway

1. Provision one or more new disks on your gateway host hypervisor or Amazon EC2
   instance. For information about how to provision a disk on a hypervisor, see
   your hypervisor's documentation. For information about provisioning Amazon EBS
   volumes for an Amazon EC2 instance, see [Amazon EBS volumes](../../../AWSEC2/latest/UserGuide/ebs-volumes.md "../../../AWSEC2/latest/UserGuide/ebs-volumes.md") in the
   _Amazon Elastic Compute Cloud User Guide for Linux Instances_. In the
   following steps, you will configure this disk as cache storage.
2. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
3. In the navigation pane, choose **Gateways**.
4. Search for your gateway and select it from the list.
5. From the **Actions** menu, choose **Configure cache
   storage**.
6. In the **Configure cache storage** section, identify the
   disks you provisioned. If you don't see your disks, choose the refresh icon
   to refresh the list. For each disk, choose **Cache** from the
   **Allocated to** drop-down menu.

###### Note

**Cache** is the only available option for allocating
disks on a File Gateway. 7. Choose **Save changes** to save your configuration
settings.
