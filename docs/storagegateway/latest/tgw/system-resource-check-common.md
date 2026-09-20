

# Viewing your gateway system resource status
<a name="system-resource-check-common"></a>

When your gateway starts, it checks its virtual CPU cores, root volume size, and RAM. It then determines whether these system resources are sufficient for your gateway to function properly. You can view the results of this check on the gateway's local console.

**To view the status of a system resource check**

1. Log in to your gateway's local console:
   + For more information on logging in to the VMware ESXi console, see [Accessing the Gateway Local Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common).
   + For more information on logging in to the Microsoft Hyper-V local console, see [Access the Gateway Local Console with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common).
   + For more information on logging in to the KVM local console, see [Accessing the Gateway Local Console with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common).

1. From the **AWS Appliance Activation - Configuration** main menu, enter the corresponding numeral to select **View System Resource Check**.

   Each resource displays **[OK**], **[WARNING]**, or **[FAIL]**, indicating the status of the resource as follows:


<table>
<thead>
  <tr><th>Message</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>[OK]</b></td><td>The resource has passed the system resource check.</td></tr>
  <tr><td><b>[WARNING]</b></td><td>The resource doesn't meet the recommended requirements, but your gateway can continue to function. Storage Gateway displays a message that describes the results of the resource check.</td></tr>
  <tr><td><b>[FAIL]</b></td><td>The resource doesn't meet the minimum requirements. Your gateway might not function properly. Storage Gateway displays a message that describes the results of the resource check.</td></tr>
</tbody>
</table>


   The console also displays the number of errors and warnings next to the resource check menu option.