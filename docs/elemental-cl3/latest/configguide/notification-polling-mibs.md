

# MIBs in Conductor Live
<a name="notification-polling-mibs"></a>

AWS Elemental provides the following MIBs for use with Conductor Live:

ELEMENTAL-MIB  
This is the base MIB for all AWS Elemental products.   


<table>
<thead>
  <tr><th>Variable</th><th>Values</th></tr>
</thead>
<tbody>
  <tr><td><code>serviceStatus</code></td><td> <ul><li> 0 if the Conductor Live isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>firewallSettings</code></td><td> <ul><li> 0 if the node firewall is off. </li><li> 1 if it is on. </li></ul> </td></tr>
  <tr><td><code>networkSettings</code></td><td>Always 1. Required for some network management systems.</td></tr>
  <tr><td><code>mountPoints</code></td><td>Number of user-mounted file systems in <code>/mnt</code>.</td></tr>
  <tr><td><code>version</code></td><td>The version of the Conductor Live node.</td></tr>
  <tr><td><code>httpdStatus</code></td><td> <ul><li> 0 if the <code>httpd</code> service isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>databaseBackup</code></td><td> <ul><li> 0 if writes (starting backups) is allowed. </li><li> 1 if they aren't allowed. </li></ul> </td></tr>
</tbody>
</table>


ELEMENTAL-CONDUCTOR-MIB  
This MIB describes objects that are specific to Conductor Live.   


<table>
<thead>
  <tr><th>Variable</th><th>Values</th></tr>
</thead>
<tbody>
  <tr><td><code>channelId</code></td><td>The system-assigned numerical ID of the channel. </td></tr>
  <tr><td><code>channelName</code></td><td>The user-defined name of the channel.</td></tr>
  <tr><td><code>channelRunning</code></td><td> <ul><li> 0 if the channel isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>channelError</code></td><td> <ul><li> 0 if the channel isn't in an error state. </li><li> 1 if it is in an error state. </li></ul> </td></tr>
  <tr><td><code>channelLiveEventId</code></td><td>The system-assigned ID of the event associated with the channel.</td></tr>
  <tr><td><code>channelStartTime</code></td><td>Start time of the channel which is provided if the channel is currently running only.</td></tr>
  <tr><td><code>channelDuration</code></td><td>The duration of time that the channel has been running which is provided if the channel is currently running only.</td></tr>
  <tr><td><code>channelAlerts</code></td><td>The text bodies of any active alerts related to the channel, including the time the alert was last set. Each alert is separated by semicolons.</td></tr>
  <tr><td><code>channelMessages</code></td><td>The text bodies of any messages generated in the last 24 hours related to the channel, including the time the message was last set. Each message is separated by semicolons.</td></tr>
  <tr><td><code>nodeId</code></td><td>The numerical ID of the node on which the channel is running.</td></tr>
  <tr><td><code>nodeHostname</code></td><td>Hostname of the node that the channel is running on.</td></tr>
</tbody>
</table>


Both the ELEMENTAL-MIB and ELEMENTAL-LIVE-MIB come installed on Conductor Live. They are located in `/opt/elemental_se/web/public/mib/`.