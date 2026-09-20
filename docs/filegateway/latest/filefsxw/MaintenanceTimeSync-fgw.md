

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Configuring a Network Time Protocol (NTP) server for your gateway
<a name="MaintenanceTimeSync-fgw"></a>

You can view and edit Network Time Protocol (NTP) server configurations and synchronize the VM time on your gateway with your hypervisor host.

**To manage system time**

1. Log in to your gateway's local console:
   + For more information on logging in to the VMware ESXi local console, see [Accessing the Gateway Local Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common).
   + For more information on logging in to the Microsoft Hyper-V local console, see [Access the Gateway Local Console with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common).
   + For more information on logging in to the KVM local console, see [Accessing the Gateway Local Console with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common).

1. From the **AWS Appliance Activation - Configuration** main menu, enter the corresponding numeral to select **System Time Management**.

1. From the **System Time Management** menu, enter the corresponding numeral to perform one of the following tasks.


<table>
<thead>
  <tr><th>To Perform This Task</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td>View and synchronize your VM time with NTP server time.</td><td>Enter the corresponding numeral to select <b>View and Synchronize System Time</b>.<br />The current time of your VM is displayed. Your File Gateway determines the time difference from your gateway VM, and your NTP server time prompts you to synchronize the VM time with NTP time.<br />After your gateway is deployed and running, in some scenarios the gateway VM's time can drift. For example, suppose that there is a prolonged network outage and your hypervisor host and gateway don't get time updates. In this case, the gateway VM's time is different from the true time. When there is a time drift, a discrepancy occurs between the stated times when operations such as snapshots occur and the actual times that the operations occur.<br />For a gateway deployed on VMware ESXi, setting the hypervisor host time and synchronizing the VM time to the host is sufficient to avoid time drift. For more information, see <a href="GettingStartedSyncVMTime-common.md">Synchronize VM time with VMware host time</a>. <br />For a gateway deployed on Microsoft Hyper-V, you should periodically check your VM's time. For more information, see <a href="MaintenanceTimeSync-hyperv.md">Synchronize VM time with Hyper-V or Linux KVM host time</a>.<br />For a gateway deployed on KVM, you can check and synchronize the VM time using <code>virsh</code> command line interface for KVM.</td></tr>
  <tr><td>Edit your NTP server configuration</td><td>Enter the corresponding numeral to select <b>Edit NTP Configuration</b>.<br />You are prompted to provide a preferred and a secondary NTP server.</td></tr>
  <tr><td>View your NTP server configuration</td><td>Enter the corresponding numeral to select <b>View NTP Configuration</b>.<br />Your NTP server configuration is displayed.</td></tr>
</tbody>
</table>
