

# WorkSpaces Pools metrics and dimensions
<a name="monitoring-with-cloudwatch"></a>

Amazon WorkSpaces sends the following WorkSpaces Pools metrics and dimension information to Amazon CloudWatch.

WorkSpaces Pools sends metrics to CloudWatch one time every minute. The `AWS/Workspaces` namespace includes the following metrics.

## Pools usage metrics
<a name="pools-dimensions"></a>


| Metric | Description | 
| --- | --- | 
|  ActiveUserSessionCapacity  | The number of user sessions currently being used for streaming sessions.<br />Units: Count<br />Valid statistics: Average, Minimum, Maximum | 
| ActualUserSessionCapacity | The total number of pool sessions that are available for streaming or are currently streaming.<pre>ActualUserSessionCapacity = AvailableUserSessionCapacity + ActiveUserSessionCapacity</pre><br />Units: Count<br />Valid statistics: Average, Minimum, Maximum | 
|  AvailableUserSessionCapacity  | The number of idle pool sessions currently available for user streaming.<pre>AvailableUserSessionCapacity = ActualUserSessionCapacity - ActiveUserSessionCapacity</pre><br />Units: Count<br />Valid statistics: Average, Minimum, Maximum | 
|  PendingUserSessionCapacity  | The number of sessions being provisioned for your pool. Represents the additional number of streaming sessions the pool can support after provisioning is complete.<br />Units: Count<br />Valid statistics: Average, Minimum, Maximum | 
| UserSessionsCapacityUtilization | The percentage of sessions in a pool that are being used, using the following formula.<pre>UserSessionCapacityUtilization = (ActiveUserSessionCapacity / ActualUserSessionCapacity) * 100</pre><br />Monitoring this metric helps with decisions about increasing or decreasing the value of a pool's desired capacity.<br />Units: Percent<br />Valid statistics: Average, Minimum, Maximum | 
|  DesiredUserSessionCapacity  | The total number of sessions that are either running or pending. This represents the total number of concurrent streaming sessions your pool can support in a steady state.<pre>DesiredUserSessionCapacity = ActualUserSessionCapacity + PendingUserSessionCapacity</pre><br />Units: Count<br />Valid statistics: Average, Minimum, Maximum | 
|  InsufficientCapacityError  | The number of session requests rejected due to lack of capacity.<br />You can set alarms to use this metric to be notified of users waiting for streaming sessions.<br />Units: Count<br />Valid statistics: Average, Minimum, Maximum, Sum | 