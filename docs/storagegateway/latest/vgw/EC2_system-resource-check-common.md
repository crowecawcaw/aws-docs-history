# Viewing your gateway system resource

status

When your gateway starts, it checks its virtual CPU cores, root volume size, and RAM.
It then determines whether these system resources are sufficient for your gateway to
function properly. You can view the results of this check on the gateway's local
console.

###### To view the status of a system resource check

1. Log in to your gateway's local console. For instructions, see [Logging In to Your Amazon EC2 Gateway
   Local Console](EC2_MaintenanceConsoleWindow-common.md "EC2_MaintenanceConsoleWindow-common.md").
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
