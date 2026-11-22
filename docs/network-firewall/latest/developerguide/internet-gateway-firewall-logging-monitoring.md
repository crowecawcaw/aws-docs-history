

# Logging and monitoring

Automated internet firewall offers the same logging and monitoring controls as AWS Network Firewall, applied at organization scale. You get centralized visibility into internet activity from all in-scope VPCs in one location. A network administrator can see access requests across the organization centrally.

For more information about logging and monitoring in AWS Network Firewall, see the following resources:
+ Logging and monitoring overview – [Monitoring and reporting in Network Firewall](nwfw-monitoring-reporting.md).
+ CloudWatch metrics – [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md).

## Monitor VPC traffic path with VPC flow logs
<a name="internet-gateway-firewall-vpc-flow-logs"></a>

VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from elastic network interfaces in your VPC. By looking at VPC flow logs, you can deduce that automated internet firewall was used on the traffic path to the internet. You can then view the automated internet firewall flow logs and alert logs to determine the action that automated internet firewall took on the traffic.

Create a flow log for your VPC using the steps in [Work with flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-flow-logs.html) in the *Amazon VPC User Guide*.

When you create the flow log, make sure that you use a custom format that includes the `traffic-path` field.

When you view the flow logs, if egress traffic from an elastic network interface (ENI) is processed by automated internet firewall, the `traffic-path` field has the value `9` in the VPC Flow Log record.

**Note**  
The `traffic-path` field is only available for egress traffic from the ENI. The value for ingress traffic is always `-`.