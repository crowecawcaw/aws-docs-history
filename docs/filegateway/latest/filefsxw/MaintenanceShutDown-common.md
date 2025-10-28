Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Shutting down your gateway VM

You might need to shutdown or reboot your VM for maintenance, such as when applying a
patch to your hypervisor. You shut down on-premises gateway VMs using your hypervisor
interface, and Amazon EC2 instances using the Amazon EC2 console.

###### Important

If you stop and start an Amazon EC2 gateway that uses ephemeral storage, the gateway will
be permanently offline. This happens because the physical storage disk is replaced.
There is no work-around for this issue. The only resolution is to delete the gateway and
activate a new one on a new EC2 instance.
