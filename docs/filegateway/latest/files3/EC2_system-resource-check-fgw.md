# Viewing your gateway system resource

status

When your File Gateway starts, it checks its virtual CPU cores, root volume size, and
RAM. It then determines whether the available system resources are sufficient for your
gateway to function properly. You can view the results of the system resource check by
using the gateway local console.

###### To view the status of a system resource check

1. Log in to the local console on your Amazon EC2 File Gateway. For instructions, see
   [Logging in to your Amazon EC2 gateway
   local console](EC2_MaintenanceConsoleWindow-fgw.md "EC2_MaintenanceConsoleWindow-fgw.md").
2. From the **AWS Appliance Activation - Configuration** main
   menu, enter the corresponding numeral to select **View System Resource
   Check**.

The gateway local console displays **[OK**],
**[WARNING]**, or **[FAIL]** to indicate
the status of the resource as follows:

| Message       | Description                                                                                                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **[OK]**      | The resource has passed the system resource check.                                                                                                                                                 |
| **[WARNING]** | The resource does not meet the recommended requirements, but your gateway can continue to function. The gateway local console displays a message that describes the results of the resource check. |
| **[FAIL]**    | The resource does not meet the minimum requirements. Your gateway might not function properly. The gateway local console displays a message that describes the results of the resource check.      | The local console also displays the number of errors and warnings next to the resource check menu option. |
