# Monitoring and config management

Monitoring and config management is an important way to gain
insights and improve the performance of your hybrid networking
environment. AWS provides the following monitoring and config
management services that enable you to monitor your AWS services
and resolve the root causes of performance issues based on your
business needs.

**Amazon**
**CloudWatch** enables you to
access system metrics on the AWS services that are being used,
consolidate system and application level logs, and create business
KPIs as custom metrics for your specific needs. CloudWatch
provides dashboards and alerts that can trigger automated actions
on the platform.

**AWS Health Dashboard**
provides alerts and remediation guidance when AWS is experiencing
events that may impact you and The **Service
Health Dashboard** provides public information about the
regional availability of a service. While the Service Health
Dashboard displays the general status of AWS services, AWS Health Dashboard gives you a personalized view into the
performance and availability of the AWS services underlying your
AWS resources.

**VPC Reachability Analyzer** is a
configuration analysis tool that enables you to perform
connectivity testing between a source resource and a destination
resource in your virtual private clouds (VPCs). When the
destination is reachable, reachability analyzer produces
hop-by-hop details of the virtual network path between the source
and the destination. When the destination is not reachable,
reachability analyzer identifies the blocking component. While VPC
reachability analyzer doesn’t test end to end hybrid connectivity,
it can analyze connectivity between VPN gateways (VGW or TGW) and
a target within a VPC.

**Transit Gateway Network Manager**
(Network Manager) enables you to centrally manage your networks
that are built around transit gateways. You can visualize and
monitor your global network across AWS Regions and on-premises
locations.

**Route Analyzer** is a part of
Transit Gateway Network Manager that allows you to perform an
analysis of the routes in your transit gateway route tables. The
Route Analyzer analyzes the routing path between a specified
source and destination, and returns information about the
connectivity between components. You can use the Route Analyzer to
perform the following actions:

- Verify that the transit gateway route table configuration will
  work as expected before you start sending traffic
- Validate your existing route configuration
- Diagnose route-related issues that are causing traffic
  disruption in your global network

**AWS Config** is a service that
enables you to assess, audit, and evaluate the configurations of
your AWS resources. Config continuously monitors and records your
AWS resource configurations and allows you to automate the
evaluation of recorded configurations against desired
configurations. With Config, you can review changes in
configurations and relationships between AWS resources, dive into
detailed resource configuration histories, and determine your
overall compliance against the configurations specified in your
internal guidelines. This enables you to simplify compliance
auditing, security analysis, change management, and operational
troubleshooting.
