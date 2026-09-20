

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Using AWS Migration Hub to export server data
<a name="export-server-data"></a>

This topic explains how to export server data by using the AWS Management Console, the AWS Command Line Interface, or the API.<a name="export-data-for-all-servers"></a>

**To use the AWS Management Console to export server data for all servers**

1. Sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/). 

1. In the left navigation pane under **Discover**, choose **Servers**.

1. Choose **Actions**, and then choose **Export discovery data**.

1. In the **Exports** section at the bottom of the screen, choose **Export server details**. This action generates a .zip file that includes the .csv files that are described in the following table.


<table>
<thead>
  <tr><th>File name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>{account_id}_Application.csv</td><td>Details of each application, including the server count, name, and description.</td></tr>
  <tr><td>{account_id}_ApplicationResourceAssociation.csv</td><td>The relationship between servers and applications.</td></tr>
  <tr><td>{account_id}_ImportTemplate</td><td>The summary of each server’s application and tags. This file can be modified and re-imported to update the application associated with the server. </td></tr>
  <tr><td>{account_id}_NetworkInterface.csv</td><td>Details of each network interface including the associated server, address, and switch.</td></tr>
  <tr><td>{account_id}_Server.csv</td><td>Details of each server, including operating system, host name, and hypervisor.</td></tr>
  <tr><td>{account_id}_SystemPerformance.csv</td><td>Details of each server, including CPU, memory and storage configuration, and performance.</td></tr>
  <tr><td>{account_id}_Tags.csv</td><td>Details of each tag associated with a server.</td></tr>
  <tr><td>{account_id}_VMwareInfo.csv</td><td>Details of each VMware configuration, including moRef, vmName, and vCenter.</td></tr>
</tbody>
</table>
<a name="export-agent-data-for-one-server"></a>

**To use the AWS Management Console to export agent data for a specific server**

1. Sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/). 

1. In the left navigation pane under **Discover**, choose **Servers**.

1. Place the cursor in the search field under **Servers**. A drop-down list appears. In that list, under **Properties**, choose **Source**, then choose the **=** operator, and then choose **Source = Agent**.

1. In the search results, choose the name of the server for which you want to export data. This action takes you to the details page for that server.

1. Enter a start time and an end time, and then choose **Export**. The exported .zip file includes the .csv files that are described in the following table.


<table>
<thead>
  <tr><th></th><th></th></tr>
</thead>
<tbody>
  <tr><td>{account_id}_destinationProcessConnection.csv</td><td>Details of the inbound connections into the server.</td></tr>
  <tr><td>{account_id}_networkInterface.csv</td><td>Details of each network interface including address, mask, and name</td></tr>
  <tr><td>{account_id}_osInfo.csv</td><td>Details of the operating system including CPU type, hypervisor and operating system name.</td></tr>
  <tr><td>{account_id}_process.csv</td><td>Details of the processes running on the server.</td></tr>
  <tr><td>{account_id}_sourceProcessConnection.csv</td><td>Details of the outbound connection originating from the server.</td></tr>
  <tr><td>{account_id}_systemPerformance.csv</td><td>Details of the CPU, memory and storage configuration &amp; performance for the server.</td></tr>
</tbody>
</table>
<a name="cli-api-export"></a>

**To use the AWS Command Line Interface or the API to export server data**

1. Run [start-export-task](https://docs.aws.amazon.com/cli/latest/reference/discovery/start-export-task.html). The corresponding API operation is [StartExportTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html)

1. Run [describe-export-tasks](https://docs.aws.amazon.com/cli/latest/reference/discovery/describe-export-tasks.html). The corresponding API operation is [DescribeExportTasks](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html).