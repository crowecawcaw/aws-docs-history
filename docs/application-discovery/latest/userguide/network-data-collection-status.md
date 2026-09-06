

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Server status in the Network Data Collection module
<a name="network-data-collection-status"></a>

The following table explains the collection status values.


| Status | Meaning | 
| --- | --- | 
| Collecting or Collected | The last collection attempt for network connections was successful. | 
| Erroring or Errored | The last collection attempt for network connections failed due to either a networking or permissions problem. For additional information, select the checkbox to the left of the server that has the error. | 
| Skipped | Servers for which no valid credentials were provided. Update or configure additional server credentials. | 
| No data | Data collection for the server has not started. To start collecting data, choose Start collector. | 
| Pending | Collection has been started but no collection attempts have been made. Wait a few minutes, and then refresh the list. | 