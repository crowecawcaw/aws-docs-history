# Flow logs basics

You can create a flow log for a VPC, a subnet, or a network interface. If you create a
flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored.

Flow log data for a monitored network interface is recorded as _flow log
records_, which are log events consisting of fields that describe the
traffic flow. For more information, see [Flow log records](flow-log-records.md "flow-log-records.md").

To create a flow log, you specify:

- The resource for which to create the flow log
- The type of traffic to capture (accepted traffic, rejected traffic, or all
  traffic)
- The destinations to which you want to publish the flow log data
  In the following example, you create a flow log that captures
  accepted traffic for the network interface for one of the EC2 instances in a private subnet and publishes the flow log
  records to an Amazon S3 bucket.

![Flow logs for an instance](images/flow-logs-diagram-s3.png)
In the following example, a flow log captures all traffic for
a subnet and publishes the flow log records to Amazon CloudWatch Logs. The flow log captures traffic for all network interfaces in the subnet.

![Flow logs for a subnet](images/flow-logs-diagram-cw.png)
After you create a flow log, it can take several minutes to begin collecting and
publishing data to the chosen destinations. Flow logs do not capture real-time log
streams for your network interfaces. For more information, see [2. Create a flow log](working-with-flow-logs.md#create-flow-log "working-with-flow-logs.md#create-flow-log").

If you launch an instance into your subnet after you create a flow log for your
subnet or VPC, we create a log stream (for CloudWatch Logs) or log file object (for Amazon S3)
for the new network interface as soon as there is network traffic for the network
interface.

You can create flow logs for network interfaces that are created by other AWS
services, such as:

- Elastic Load Balancing
- Amazon RDS
- Amazon ElastiCache
- Amazon Redshift
- Amazon WorkSpaces
- NAT gateways
- Transit gateways
  Regardless of the type of network interface, you must use the Amazon EC2 console or the
  Amazon EC2 API to create a flow log for a network interface.

You can apply tags to your flow logs. Each tag consists of a key and an optional value,
both of which you define. Tags can help you organize your flow logs, for example by
purpose or owner.

If you no longer require a flow log, you can delete it. Deleting a flow log disables
the flow log service for the resource, so that no new flow log records are created or
published. Deleting a flow log does not delete any existing flow log data. After you
delete a flow log, you can delete the flow log data directly from the destination when
you are finished with it. For more information, see [4. Delete a flow log](working-with-flow-logs.md#delete-flow-log "working-with-flow-logs.md#delete-flow-log").
