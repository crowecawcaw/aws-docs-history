AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Server status in the Network Data

Collection module

The following table explains the collection status values.

| Status                  | Meaning                                                                                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Collecting or Collected | The last collection attempt for network connections was<br>successful.                                                                                                                                               |
| Erroring or Errored     | The last collection attempt for network connections failed due to<br>either a networking or permissions problem. For additional information,<br>select the checkbox to the left of the server that has the<br>error. |
| Skipped                 | Servers for which no valid credentials were provided. Update or<br>configure additional server credentials.                                                                                                          |
| No data                 | Data collection for the server has not started. To start collecting<br>data, choose **Start collector**.                                                                                                             |
| Pending                 | Collection has been started but no collection attempts have been<br>made. Wait a few minutes, and then refresh the list.                                                                                             |
