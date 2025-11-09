AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Sorting data collectors in the AWS Migration Hub

console

If you deployed many data collectors, you can sort the displayed list of deployed
collector's on the **Data Collectors** page of the console. You sort
the list by applying filters in the search bar. You can search and filter on most of the
criteria specified in the **Data Collectors** list.

The following table shows the search criteria that you can use for
**Agents**, including operators, values, and a definition of the
values.

| Search Criterion  | Operator | Value: Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent ID          | ==       | Any agent ID selected from the pre-populated list from which a<br>collection tool is installed.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Hostname          | ==<br>!= | For agents, any host name selected from the pre-populated list of<br>hosts where an agent is installed.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Collection status | ==<br>!= | Started: Data is being collected and sent to Application Discovery Service<br>Start scheduled: Data collection is scheduled to start. Data will<br>be sent to Application Discovery Service on next ping, and status will change to<br>**Started**.<br>Stopped: Data is not being collected or sent to Application Discovery Service.<br>Stop scheduled: Data collection is scheduled to stop. Data will<br>stop being sent to Application Discovery Service on next ping, and status will change to<br>**Stopped**.                 |
| Health            | ==<br>!= | Healthy: Data collection isn't turned on. The tool is<br>functioning normally.<br>Unhealthy: The tool is in an error state. Data isn't being<br>collected or reported.<br>Unknown: No connection established in over an hour.<br>Shutdown: The tool last communicated "shutting down" due to a<br>system, service, or daemon shut down. If a reboot or tool upgrade<br>occurred, status will change to another state at the first reporting<br>cycle.<br>Running: Data collection is turned on. The tool is functioning<br>normally. |
| IP address        | ==<br>!= | Any IP address selected from the pre-populated list where a<br>collection tool is installed.                                                                                                                                                                                                                                                                                                                                                                                                                                         |

The following table shows the search criteria that you can use for **Agentless
collectors**, including operators, values, and a definition of the
values.

| Search Criterion | Operator | Value: Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID               | ==       | Any agentless collector ID selected from the pre-populated list<br>from which a collection tool is installed.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Hostname         | ==<br>!= | For agentless collectors, any host name selected from the<br>pre-populated list of hosts where an agentless collectors is<br>installed.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Status           | ==<br>!= | Collecting data: Data collection is turned on. The tool is<br>functioning normally.<br>Ready to configure— Data collection isn't turned on.<br>The tool is functioning normally.<br>Requires attention— The tool is in an error state and needs<br>attention.<br>Unknown: No connection established in over an hour.<br>Shut down: The tool last communicated "shutting down" due to a<br>system, service, or daemon shut down. If a reboot or tool upgrade<br>occurred, status will change to another state at the first reporting<br>cycle. |
| IP address       | ==<br>!= | Any IP address selected from the pre-populated list where a<br>collection tool is installed.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

###### To sort data collectors by applying search filters

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console
   at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane under **Discover**,
   choose **Data Collectors**.
3. Choose either the **Agentless collectors** or
   **Agents** tab.
4. Click inside the search bar and choose a search criterion from the
   list.
5. Choose an operator from the next list.
6. Choose a value from the last list.
