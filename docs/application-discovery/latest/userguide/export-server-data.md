

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Using AWS Migration Hub to export server data
<a name="export-server-data"></a>

This topic explains how to export server data by using the AWS Management Console, the AWS Command Line Interface, or the API.<a name="export-data-for-all-servers"></a>

**To use the AWS Management Console to export server data for all servers**

1. Sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/). 

1. In the left navigation pane under **Discover**, choose **Servers**.

1. Choose **Actions**, and then choose **Export discovery data**.

1. In the **Exports** section at the bottom of the screen, choose **Export server details**. This action generates a .zip file that includes the .csv files that are described in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/application-discovery/latest/userguide/export-server-data.html)<a name="export-agent-data-for-one-server"></a>

**To use the AWS Management Console to export agent data for a specific server**

1. Sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/). 

1. In the left navigation pane under **Discover**, choose **Servers**.

1. Place the cursor in the search field under **Servers**. A drop-down list appears. In that list, under **Properties**, choose **Source**, then choose the **=** operator, and then choose **Source = Agent**.

1. In the search results, choose the name of the server for which you want to export data. This action takes you to the details page for that server.

1. Enter a start time and an end time, and then choose **Export**. The exported .zip file includes the .csv files that are described in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/application-discovery/latest/userguide/export-server-data.html)<a name="cli-api-export"></a>

**To use the AWS Command Line Interface or the API to export server data**

1. Run [start-export-task](https://docs.aws.amazon.com/cli/latest/reference/discovery/start-export-task.html). The corresponding API operation is [StartExportTask](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html)

1. Run [describe-export-tasks](https://docs.aws.amazon.com/cli/latest/reference/discovery/describe-export-tasks.html). The corresponding API operation is [DescribeExportTasks](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html).