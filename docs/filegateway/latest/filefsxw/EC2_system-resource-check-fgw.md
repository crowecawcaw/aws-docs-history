

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Viewing your gateway system resource status
<a name="EC2_system-resource-check-fgw"></a>

When your File Gateway starts, it checks its virtual CPU cores, root volume size, and RAM. It then determines whether the available system resources are sufficient for your gateway to function properly. You can view the results of the system resource check by using the gateway local console.

**To view the status of a system resource check**

1. Log in to the local console on your Amazon EC2 File Gateway. For instructions, see [Logging in to your Amazon EC2 gateway local console](EC2_MaintenanceConsoleWindow-fgw.md).

1. From the **AWS Appliance Activation - Configuration** main menu, enter the corresponding numeral to select **View System Resource Check**.

   The gateway local console displays **[OK**], **[WARNING]**, or **[FAIL]** to indicate the status of the resource as follows:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_system-resource-check-fgw.html)

   The local console also displays the number of errors and warnings next to the resource check menu option.