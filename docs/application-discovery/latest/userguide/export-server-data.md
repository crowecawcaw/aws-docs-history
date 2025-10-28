AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Using AWS Migration Hub to export server data

This topic explains how to export server data by using the AWS Management Console, the AWS Command Line Interface,
or the API.

###### To use the AWS Management Console to export server data

for all servers

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane under **Discover**, choose
   **Servers**.
3. Choose **Actions**, and then choose **Export
   discovery data**.
4. In the **Exports** section at the bottom of the screen,
   choose **Export server details**. This action generates a .zip
   file that includes the .csv files that are described in the following
   table.

| File name                                        | Description                                                                                                                                        |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {account_id}\_Application.csv                    | Details of each application, including the server count, name, and description.                                                                    |
| {account_id}\_ApplicationResourceAssociation.csv | The relationship between servers and applications.                                                                                                 |
| {account_id}\_ImportTemplate                     | The summary of each server’s application and tags. This file can be modified and re-imported to update the application associated with the server. |
| {account_id}\_NetworkInterface.csv               | Details of each network interface including the associated server, address, and switch.                                                            |
| {account_id}\_Server.csv                         | Details of each server, including operating system, host name, and hypervisor.                                                                     |
| {account_id}\_SystemPerformance.csv              | Details of each server, including CPU, memory and storage configuration, and performance.                                                          |
| {account_id}\_Tags.csv                           | Details of each tag associated with a server.                                                                                                      |
| {account_id}\_VMwareInfo.csv                     | Details of each VMware configuration, including moRef, vmName, and vCenter.                                                                        | ###### To use the AWS Management Console to export agent data for a specific server 1. Sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/"). 2. In the left navigation pane under **Discover**, choose **Servers**. 3. Place the cursor in the search field under **Servers**. A drop-down list appears. In that list, under **Properties**, choose **Source**, then choose the **=** operator, and then choose **Source = Agent**. 4. In the search results, choose the name of the server for which you want to export data. This action takes you to the details page for that server. 5. Enter a start time and an end time, and then choose **Export**. The exported .zip file includes the .csv files that are described in the following table. |
|                                                  |                                                                                                                                                    |
| ---                                              | ---                                                                                                                                                |
| {account_id}\_destinationProcessConnection.csv   | Details of the inbound connections into the server.                                                                                                |
| {account_id}\_networkInterface.csv               | Details of each network interface including address, mask, and name                                                                                |
| {account_id}\_osInfo.csv                         | Details of the operating system including CPU type, hypervisor and operating system name.                                                          |
| {account_id}\_process.csv                        | Details of the processes running on the server.                                                                                                    |
| {account_id}\_sourceProcessConnection.csv        | Details of the outbound connection originating from the server.                                                                                    |
| {account_id}\_systemPerformance.csv              | Details of the CPU, memory and storage configuration & performance for the server.                                                                 | ###### To use the AWS Command Line Interface or the API to export server data 1. Run [start-export-task](../../../cli/latest/reference/discovery/start-export-task.md "../../../cli/latest/reference/discovery/start-export-task.md"). The corresponding API operation is [StartExportTask](../APIReference/API_StartExportTask.md "../APIReference/API_StartExportTask.md") 2. Run [describe-export-tasks](../../../cli/latest/reference/discovery/describe-export-tasks.md "../../../cli/latest/reference/discovery/describe-export-tasks.md"). The corresponding API operation is [DescribeExportTasks](../APIReference/API_DescribeExportTasks.md "../APIReference/API_DescribeExportTasks.md").                                                                                                                                                                                                                      |
