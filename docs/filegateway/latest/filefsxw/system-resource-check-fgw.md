Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Viewing your gateway system resource

status

When your gateway starts, it checks its virtual CPU cores, root volume size, and RAM.
It then determines whether these system resources are sufficient for your gateway to
function properly. You can view the results of this check on the gateway's local
console.

###### To view the status of a system resource check

1. Log in to your gateway's local console:
   - For more information on logging in to the VMware ESXi console, see
     [Accessing the Gateway Local
     Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common "accessing-local-console.md#MaintenanceConsoleWindowVMware-common").
   - For more information on logging in to the Microsoft Hyper-V local
     console, see [Access the Gateway Local Console
     with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common "accessing-local-console.md#MaintenanceConsoleWindowHyperV-common").
   - For more information on logging in to the KVM local console, see [Accessing the Gateway Local Console
     with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common "accessing-local-console.md#MaintenanceConsoleWindowKVM-common").

2. From the **AWS Appliance Activation - Configuration** main
   menu, enter the corresponding numeral to select **View System Resource
   Check**.

Each resource displays **[OK**],
**[WARNING]**, or **[FAIL]**, indicating
the status of the resource as follows:

| Message       | Description                                                                                                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[OK]**      | The resource has passed the system resource check.                                                                                                                                               |
| **[WARNING]** | The resource doesn't meet the recommended requirements,<br>but your gateway can continue to function. Storage Gateway displays a<br>message that describes the results of the resource<br>check. |
| **[FAIL]**    | The resource doesn't meet the minimum requirements. Your<br>gateway might not function properly. Storage Gateway displays a message<br>that describes the results of the resource check.         |

The console also displays the number of errors and warnings next to the
resource check menu option.
