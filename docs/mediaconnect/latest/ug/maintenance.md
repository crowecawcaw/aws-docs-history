

# Maintenance in MediaConnect
<a name="maintenance"></a>

AWS Elemental MediaConnect routinely performs maintenance on underlying systems for security, reliability, and operational performance. These maintenance activities include actions such as patching the operating system, updating drivers, and installing software updates.

Maintenance applies to both router I/Os (inputs and outputs) and flows. For active resources, MediaConnect interrupts the resource to apply updates. For idle resources, updates are applied automatically the next time the resource starts.

To minimize disruption, configure a *maintenance window* for each resource. A maintenance window specifies the preferred day and start hour for maintenance to occur. The window duration is two hours. When you configure a window, MediaConnect automatically applies updates at a time within that window.

**Important**  
The two-hour window duration does not mean your resource is affected for two hours. MediaConnect applies updates at some point within the two-hour window. 

If you operate redundant resources for resilience—for example, redundant flows or router I/Os in different AWS Regions—select different maintenance windows for each redundant resource. Choosing different days or times prevents simultaneous patching of redundant resources and helps maintain availability during maintenance events.

**Topics**
+ [How maintenance works](how-maintenance-works.md)
+ [Viewing router I/O maintenance status](viewing-router-io-maintenance.md)
+ [Setting router I/O maintenance windows](setting-router-io-maintenance.md)
+ [Viewing flow maintenance status](viewing-flows-maintenance.md)
+ [Setting flow maintenance windows](setting-flow-maintenance.md)
+ [Manually restarting resources for maintenance](manual-restart-maintenance.md)