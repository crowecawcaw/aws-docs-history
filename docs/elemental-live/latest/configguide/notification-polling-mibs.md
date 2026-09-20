

# Management Information Bases (MIBs) in Elemental Live
<a name="notification-polling-mibs"></a>

AWS Elemental provides the following management information bases (MIBs) for use with Elemental Live:

ELEMENTAL-MIB  
ELEMENTAL-MIB is the base MIB for all AWS Elemental products. The following table describes the variables included in this MIB.  


<table>
<thead>
  <tr><th>Variable</th><th>Values</th></tr>
</thead>
<tbody>
  <tr><td><code>serviceStatus</code></td><td> <ul><li> 0 if the Elemental Live isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>firewallSettings</code></td><td> <ul><li> 0 if the node firewall is off. </li><li> 1 if it is on. </li></ul> </td></tr>
  <tr><td><code>networkSettings</code></td><td>Always 1. Required for some network management systems.</td></tr>
  <tr><td><code>mountPoints</code></td><td>Number of user-mounted filesystems in <code>/mnt</code>.</td></tr>
  <tr><td><code>version</code></td><td>The version of the Elemental Live node.</td></tr>
  <tr><td><code>httpdStatus</code></td><td> <ul><li> 0 if the <code>httpd</code> service isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>databaseBackup</code></td><td> <ul><li> 0 if writes (starting backups) is allowed. </li><li> 1 if they aren't allowed. </li></ul> </td></tr>
</tbody>
</table>


ELEMENTAL-LIVE-MIB  
ELEMENTAL-LIVE-MIB describes objects that are specific to Elemental Live. The following table describes the variables included in this MIB.  


<table>
<thead>
  <tr><th>Variable</th><th>Values</th></tr>
</thead>
<tbody>
  <tr><td><code>eventId</code></td><td>The numerical ID of the live event. This is the index to the liveEventsTable.</td></tr>
  <tr><td><code>eventName</code></td><td>The name of the live event.</td></tr>
  <tr><td><code>eventRunning</code></td><td> <ul><li> 0 if the event isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>eventError</code></td><td> <ul><li> 0 if the event isn't in an error state. </li><li> 1 if it is in an error state. </li></ul> </td></tr>
  <tr><td><code>eventStatus</code></td><td>Status information about the live event. Formatted in XML.</td></tr>
  <tr><td><code>nodeId</code></td><td>The numerical ID of the node that the event is running on.</td></tr>
</tbody>
</table>


Both the ELEMENTAL-MIB and ELEMENTAL-LIVE-MIB come installed on Elemental Live. They are located in `/opt/elemental_se/web/public/mib/`.

For more information, access the Elemental Live web interface, go to the **Support** page and choose **SNMP Interface**.