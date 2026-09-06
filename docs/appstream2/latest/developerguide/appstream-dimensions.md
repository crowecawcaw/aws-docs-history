

# Fleet Usage Metrics for Single-session Fleets
<a name="appstream-dimensions"></a>

The following are fleet usage metrics for single-session fleets.


| Metric | Description | Dimensions | Statistics | Units | 
| --- | --- | --- | --- | --- | 
| ActualCapacity | The total number of instances that are available for streaming or are currently streaming.<pre>ActualCapacity = AvailableCapacity + InUseCapacity</pre> | [Fleet] | Average, Minimum, Maximum | Count | 
|  AvailableCapacity  | The number of idle instances currently available for user sessions.<pre>AvailableCapacity = ActualCapacity - InUseCapacity</pre> | [Fleet] | Average, Minimum, Maximum | Count | 
| CapacityUtilization | The percentage of instances in a fleet that are being used, using the following formula.<pre>CapacityUtilization = (InUseCapacity/ActualCapacity) * 100</pre><br />Monitoring this metric helps with decisions about increasing or decreasing the value of a fleet's desired capacity. | [Fleet] | Average, Minimum, Maximum | Percent | 
|  DesiredCapacity  | The total number of instances that are either running or pending. This represents the total number of concurrent streaming sessions your fleet can support in a steady state.<pre>DesiredCapacity = ActualCapacity + PendingCapacity</pre> | [Fleet] | Average, Minimum, Maximum | Count | 
|  InUseCapacity  | The number of instances currently being used for streaming sessions. One `InUseCapacity` count represents one streaming session. | [Fleet] | Average, Minimum, Maximum | Count | 
|  PendingCapacity  | The number of instances being provisioned by WorkSpaces Applications. Represents the additional number of streaming sessions the fleet can support after provisioning is complete. When provisioning starts, it usually takes 10-20 minutes for an instance to become available for streaming. | [Fleet] | Average, Minimum, Maximum | Count | 
| RunningCapacity | The total number of instances currently running. Represents the number of concurrent streaming sessions that can be supported by the fleet in its current state.<br />This metric is provided for Always-On fleets only, and has the same value as the `ActualCapacity` metric. | [Fleet] | Average, Minimum, Maximum | Count | 
|  InsufficientCapacityError  | The number of session requests rejected due to lack of capacity.<br />You can set alarms to use this metric to be notified of users waiting for streaming sessions. | [Fleet] | Average, Minimum, Maximum, Sum | Count | 
|  InsufficientConcurrencyLimitError  | The number of Elastic fleet session requests rejected due to reaching max concurrent streaming capacity.<br />You can set alarms to use this metric to be notified of users waiting for streaming sessions. | [Fleet] | Average, Minimum, Maximum, Sum | Count | 