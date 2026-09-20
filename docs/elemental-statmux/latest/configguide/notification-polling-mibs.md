

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Management Information Bases (MIBs) in AWS Elemental Statmux
<a name="notification-polling-mibs"></a>

AWS Elemental provides the following management information bases (MIBs) for use with AWS Elemental Statmux:

ELEMENTAL-MIB  
This is the base MIB for all AWS Elemental products.  


<table>
<thead>
  <tr><th>Variable</th><th>Values</th></tr>
</thead>
<tbody>
  <tr><td><code>serviceStatus</code></td><td> <ul><li> 0 if the AWS Elemental Statmux isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>firewallSettings</code></td><td> <ul><li> 0 if the node firewall is off. </li><li> 1 if it is on. </li></ul> </td></tr>
  <tr><td><code>networkSettings</code></td><td>Always 1. Required for some network management systems.</td></tr>
  <tr><td><code>mountPoints</code></td><td>Number of user-mounted filesystems in <code>/mnt</code>.</td></tr>
  <tr><td><code>version</code></td><td>The version of the AWS Elemental Statmux node.</td></tr>
  <tr><td><code>httpdStatus</code></td><td> <ul><li> 0 if the <code>httpd</code> service isn't running. </li><li> 1 if it is running. </li></ul> </td></tr>
  <tr><td><code>databaseBackup</code></td><td> <ul><li> 0 if writes (starting backups) is allowed. </li><li> 1 if they aren't allowed. </li></ul> </td></tr>
</tbody>
</table>


ELEMENTAL-MIB comes installed on AWS Elemental Statmux. It's located in `/opt/elemental_se/web/public/mib/`.

For more information, access the AWS Elemental Statmux web interface, go to the **Support** page and choose **SNMP Interface**.