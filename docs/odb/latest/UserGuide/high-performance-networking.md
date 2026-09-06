

# High Performance Networking for Oracle Database@AWS
<a name="high-performance-networking"></a>

## Overview
<a name="hpn-overview"></a>

Oracle Database@AWS High Performance Networking provides consistent, sub-millisecond network roundtrip latency between your Amazon EC2 application instances and Oracle Database@AWS databases. This capability is designed for latency-sensitive workloads such as payment processing, securities trading, high-volume transaction processing, and manufacturing execution systems that require predictable, low-latency connectivity to Oracle Exadata databases.

**Note**  
High Performance Networking is available for Exadata VM clusters and Autonomous VM clusters on Dedicated Exadata Infrastructure. It does not apply to Autonomous Database Serverless.

When you create an ODB network, a placement group is automatically associated with it. You can use this placement group when launching Amazon EC2 instances to ensure optimized instance placement that delivers consistent sub-millisecond latency to your Oracle Database@AWS database.

### How It Works
<a name="hpn-how-it-works"></a>

Oracle Database@AWS High Performance Networking uses Amazon EC2 placement groups to ensure that your application instances are placed in close physical proximity to your Oracle Exadata infrastructure within an AWS Availability Zone (AZ). This proximity minimizes network hops and reduces latency variability, delivering consistent and predictable performance for your most demanding database workloads.

Key characteristics:
+ **Automatic placement group provisioning** – A placement group is automatically created and associated with every new ODB network.
+ **Consistent latency** – Consistent sub-millisecond network roundtrip latency between Amazon EC2 instances and Oracle Database@AWS databases.
+ **Compatible with existing Amazon EC2 workflows** – Works with standard Amazon EC2 APIs, the AWS Management Console, and supports Amazon EC2 On-Demand Capacity Reservations (ODCR), Savings Plans, and Reserved Instances. Also compatible with Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS) when using launch templates with Auto Scaling groups.
+ **No additional cost** – High performance networking is available at no extra charge. Standard Amazon EC2 usage charges apply for launched instances.