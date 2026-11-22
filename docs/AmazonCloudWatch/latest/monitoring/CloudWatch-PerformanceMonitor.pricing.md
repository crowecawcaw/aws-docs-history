

# Pricing for Performance Monitor

With Performance Monitor, there are no upfront costs or long-term commitments. Pricing for Performance Monitor has two components:
+ **Monthly charge**: A fixed monthly charge that includes a set volume of network flows across all of your monitored VPCs.
+ **Usage charge**: A charge for the network flows above the included volume, measured in million flows per hour.

A network flow is a unique combination of source IP address, destination IP address, source port, destination port, and protocol that Performance Monitor observes in a five-minute window. For example, an application server in one VPC that connects over TCP to a database in another VPC counts as one flow.

The first time that you use Performance Monitor, you get a 30-day free trial for all of your accounts.

You're also charged standard CloudWatch prices for any additional metrics, dashboards, alarms, or insights that you create.

For more information about Performance Monitor and Amazon CloudWatch pricing, see Network Monitoring on the [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) page.