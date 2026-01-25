# Monitor your Network Load Balancers

You can use the following features to monitor your load balancers, analyze traffic
patterns, and troubleshoot issues with your load balancers and targets.

**CloudWatch metrics**

You can use Amazon CloudWatch to retrieve statistics about data points for your load
balancers and targets as an ordered set of time-series data, known as
_metrics_. You can use these metrics to verify that your
system is performing as expected. For more information, see [CloudWatch metrics for your Network Load Balancer](load-balancer-cloudwatch-metrics.md "load-balancer-cloudwatch-metrics.md").

**VPC Flow Logs**

You can use VPC Flow Logs to capture detailed information about the traffic
going to and from your Network Load Balancer. For more information, see [VPC flow logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") in the
_Amazon VPC User Guide_.

Create a flow log for each network interface for your load balancer. There is
one network interface per load balancer subnet. To identify the network
interfaces for a Network Load Balancer, look for the name of the load balancer in the
description field of the network interface.

There are two entries for each connection through your Network Load Balancer, one for the
frontend connection between the client and the load balancer and the other for
the backend connection between the load balancer and the target. If the target
group's client IP preservation attribute is enabled, the connection appears to
the instance as a connection from the client. Otherwise, the connection's source
IP is the load balancer's private IP address. If the security group of the
instance doesn't allow connections from the client but the network ACLs for the
load balancer subnet allow them, the logs for the network interface for the load
balancer show "ACCEPT OK" for the frontend and backend connections, while the
logs for the network interface for the instance show "REJECT OK" for the
connection.

If a Network Load Balancer has associated security groups, your flow logs contain entries for
traffic that is allowed or rejected by the security groups. For Network Load Balancers with TLS
listeners, your flow logs entries reflect only the rejected entries.

**Amazon CloudWatch Internet Monitor**

You can use Internet Monitor for visibility into how internet issues impact the performance and availability
between your applications hosted on AWS and your end users. You can also explore, in near real-time, how to improve the
projected latency of your application by switching to use other services, or by rerouting traffic to your
workload through different AWS Regions. For more information, see [Using Amazon CloudWatch Internet Monitor](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.md").

**Access logs**

You can use access logs to capture detailed information about TLS requests
made to your load balancer. The log files are stored in Amazon S3. You can use these
access logs to analyze traffic patterns and to troubleshoot issues with your
targets. For more information, see [Access logs for your Network Load Balancer](load-balancer-access-logs.md "load-balancer-access-logs.md").

**CloudTrail logs**

You can use AWS CloudTrail to capture detailed information about the calls made to
the Elastic Load Balancing API and store them as log files in Amazon S3. You can use these CloudTrail logs
to determine which calls were made, the source IP address where the call came
from, who made the call, when the call was made, and so on. For more information,
see [Log API calls for Elastic Load Balancing using CloudTrail](../userguide/cloudtrail-logs.md "../userguide/cloudtrail-logs.md").
