

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Management Information Bases (MIBs) in AWS Elemental Server
<a name="notification-polling-mibs"></a>

AWS Elemental provides the following management information bases (MIBs) for use with AWS Elemental Server:

ELEMENTAL-MIB  
This is the base MIB for all AWS Elemental products.  


<table>
<thead>
  <tr><th>Variable</th><th>Values</th></tr>
</thead>
<tbody>
  <tr><td><code>serviceStatus</code></td><td> <ul><li> 0 if the AWS Elemental Server isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>firewallSettings</code></td><td> <ul><li> 0 if the node firewall is off. </li><li> 1 if it is on. </li></ul> </td></tr>
  <tr><td><code>networkSettings</code></td><td>Always 1. Required for some network management systems.</td></tr>
  <tr><td><code>mountPoints</code></td><td>Number of user-mounted filesystems in <code>/mnt</code>.</td></tr>
  <tr><td><code>version</code></td><td>The version of the AWS Elemental Server node.</td></tr>
  <tr><td><code>httpdStatus</code></td><td> <ul><li> 0 if the <code>httpd</code> service isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>databaseBackup</code></td><td> <ul><li> 0 if writes (starting backups) is allowed. </li><li> 1 if they aren't allowed. </li></ul> </td></tr>
</tbody>
</table>


ELEMENTAL-SERVER-MIB  
This MIB describes objects that are specific to AWS Elemental Server.   


<table>
<thead>
  <tr><th>Variable</th><th>Values</th></tr>
</thead>
<tbody>
  <tr><td><code>jobId</code></td><td>The numerical ID of the job. This is the index to the jobTable.</td></tr>
  <tr><td><code>jobPending</code></td><td> <ul><li> 0 if the job isn't a pending state. </li><li> 1 if it is a pending state. </li></ul> </td></tr>
  <tr><td><code>jobRunning</code></td><td> <ul><li> 0 if the job isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>jobError</code></td><td> <ul><li> 0 if the job isn't in an error state. </li><li> 1 if it is in an error state. </li></ul> </td></tr>
  <tr><td><code>jobComplete</code></td><td> <ul><li> 0 if the job isn't running complete. </li><li> 1 if it is in a complete state. </li></ul> </td></tr>
  <tr><td><code>nodeId</code></td><td>The numerical ID of the node that the job is running on.</td></tr>
</tbody>
</table>


Both the ELEMENTAL-MIB and ELEMENTAL-LIVE-MIB come installed on AWS Elemental Server. They are located in `/opt/elemental_se/web/public/mib/`.

For more information, access the AWS Elemental Server web interface, go to the **Support** page and choose **SNMP Interface**.