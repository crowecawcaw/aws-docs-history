

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Sorting data collectors in the AWS Migration Hub console
<a name="sort-data-collectors"></a>

If you deployed many data collectors, you can sort the displayed list of deployed collector's on the **Data Collectors** page of the console. You sort the list by applying filters in the search bar. You can search and filter on most of the criteria specified in the **Data Collectors** list.

The following table shows the search criteria that you can use for **Agents**, including operators, values, and a definition of the values.


| Search Criterion | Operator | Value: Definition | 
| --- | --- | --- | 
| Agent ID | == | Any agent ID selected from the pre-populated list from which a collection tool is installed. | 
| Hostname | ==<br />\!= | For agents, any host name selected from the pre-populated list of hosts where an agent is installed. | 
| Collection status | ==<br />\!= | Started: Data is being collected and sent to Application Discovery Service<br />Start scheduled: Data collection is scheduled to start. Data will be sent to Application Discovery Service on next ping, and status will change to **Started**.<br />Stopped: Data is not being collected or sent to Application Discovery Service.<br />Stop scheduled: Data collection is scheduled to stop. Data will stop being sent to Application Discovery Service on next ping, and status will change to **Stopped**. | 
| Health | ==<br />\!= | Healthy: Data collection isn't turned on. The tool is functioning normally.<br />Unhealthy: The tool is in an error state. Data isn't being collected or reported.<br />Unknown: No connection established in over an hour.<br />Shutdown: The tool last communicated "shutting down" due to a system, service, or daemon shut down. If a reboot or tool upgrade occurred, status will change to another state at the first reporting cycle.<br />Running: Data collection is turned on. The tool is functioning normally. | 
| IP address | ==<br />\!= | Any IP address selected from the pre-populated list where a collection tool is installed. | 

The following table shows the search criteria that you can use for **Agentless collectors**, including operators, values, and a definition of the values.


| Search Criterion | Operator | Value: Definition | 
| --- | --- | --- | 
| ID | == | Any agentless collector ID selected from the pre-populated list from which a collection tool is installed. | 
| Hostname | ==<br />\!= | For agentless collectors, any host name selected from the pre-populated list of hosts where an agentless collectors is installed. | 
| Status | ==<br />\!= | Collecting data: Data collection is turned on. The tool is functioning normally.<br />Ready to configure— Data collection isn't turned on. The tool is functioning normally.<br />Requires attention— The tool is in an error state and needs attention.<br />Unknown: No connection established in over an hour.<br />Shut down: The tool last communicated "shutting down" due to a system, service, or daemon shut down. If a reboot or tool upgrade occurred, status will change to another state at the first reporting cycle. | 
| IP address | ==<br />\!= | Any IP address selected from the pre-populated list where a collection tool is installed. | 

**To sort data collectors by applying search filters**

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the Migration Hub console navigation pane under **Discover**, choose **Data Collectors**.

1. Choose either the **Agentless collectors** or **Agents** tab.

1. Click inside the search bar and choose a search criterion from the list.

1. Choose an operator from the next list.

1. Choose a value from the last list.