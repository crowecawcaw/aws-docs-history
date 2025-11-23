# Direct Connect maintenance

Direct Connect is committed to ensuring service security, availability, and scalability.
To maintain these standards, periodic maintenance is required on the hardware network
devices. Direct Connect maintenance is divided into two types - **planned**
and **emergency**.

These maintenance events include addressing security vulnerabilities, hardware issues,
performing device migrations to comply with standards, fixing defects, and delivering new
features. By following the practices described in [Maintenance event
preparation](#overview-maintenance-prep "#overview-maintenance-prep"), you can better prepare your Direct
Connect environment to avoid disruptions during maintenance events. If you have a
non-resilient network setup or a single connection, you’ll experience an interruption in
connectivity between your on-premises network and AWS resources.

Direct Connect sends email notifications about planned and emergency maintenance events to
the email address associated with the AWS account that owns the Direct Connect connection
or virtual interface resource. If you’re using a Direct Connect hosted connection with one
of the Direct Connect Delivery Partners, email notifications are sent to both you and the
partner account about the maintenance event. You can also add additional email addresses or
distribution lists to receive notifications. See [Update the alternate contacts for your AWS account](../../../accounts/latest/reference/manage-acct-update-contact-alternate.md "../../../accounts/latest/reference/manage-acct-update-contact-alternate.md") for more
information.

###### Maintenance events

- [Planned maintenance](#operations-maintenance-planned "#operations-maintenance-planned")
- [Emergency maintenance](#operations-maintenance-emergency "#operations-maintenance-emergency")
- [Third-party maintenance](#operations-maintenance-partner "#operations-maintenance-partner")
- [Maintenance event
  preparation](#overview-maintenance-prep "#overview-maintenance-prep")
- [Maintenance event
  postponement](#operations-maintenance-rescehedule "#operations-maintenance-rescehedule")

## Direct Connect planned maintenance

Planned maintenance events involve network upgrades such as operating system patching and
configuration updates on hardware device endpoints that are required to improve
availability and deliver new features.

These maintenance events are scheduled 14 days in advance and typically occur during a
four-hour window in low-traffic hours at the Direct Connect location where the
device endpoint resides. Maintenance activities usually complete before the full
four-hour window expires and you’ll receive a notification once work is complete. In
rare cases where unforeseen circumstances require extending the maintenance window,
we'll send a separate notification with the revised completion estimate.

Using the following schedule, the initial notification and reminder notifications are sent
to the AWS account that owns the resource:

- 14 calendar days before planned maintenance event,
- 7 calendar days before planned maintenance event, and
- 1 day prior to the planned maintenance event.

###### Note

Calendar days include non-business days and local holidays.

In addition,

- Receive notifications in your monitoring or ticketing system by integrating with
  AWS Health. To integrate AWS Health, see [Monitoring events
  in AWS Health with Amazon EventBridge](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md") in the _AWS Health User
  Guide_.
- View planned maintenance schedules on your [AWS Health Dashboard](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status").

Under rare circumstances, a planned maintenance event cannot happen as scheduled. Should
this occur, we'll send a cancellation notification and will reschedule the event in
the future following the same process as above.

## Direct Connect emergency maintenance

Emergency maintenance events are initiated on a critical basis to prevent imminent
service impacting events or resolve impairments which have already resulted in a
disruption to connectivity. In such cases, taking immediate action is necessary to
restore the affected endpoint to a healthy state.

While we strive to provide advance notice whenever possible, some situations may
require maintenance to start immediately. You will receive notifications when emergency
maintenance is scheduled or underway, and again when it is completed.

These events typically occur during a two-hour window at the Direct Connect location where
the device endpoint resides. Maintenance activities usually complete within this window.
In cases where unforeseen circumstances require extending the maintenance window, such
as hardware replacement, we’ll send a separate notification with the revised completion
estimate.

## Third-party maintenance

Beyond AWS initiated maintenance events, your Direct Connect Delivery partner or network
service provider who is providing network connectivity from your on-premises to the
Direct Connect location might perform maintenance activities. Direct Connect Delivery
partners receive maintenance event notifications from AWS so that they can plan their
own maintenance schedules to avoid overlap. AWS does not have visibility into a
partner’s maintenance activities, so you’ll need to check with them for their scheduling
process, notification methods, and best practices.

## Maintenance event preparation

To ensure production workloads continue to function during a maintenance event, Direct
Connect recommends that you use the AWS Direct Connect Resiliency Toolkit to configure
your network connections for maximum resiliency. For an example model of maximum
resiliency, see [Maximum resiliency](resiliency_toolkit.md#maximum_resiliency "resiliency_toolkit.md#maximum_resiliency").

Using maximum resiliency, connections are spread across at least two Direct Connect
locations, with termination on two unique device endpoints within each Direct Connect
location. This provides multiple layers of redundancy, which reduces the risk of a
single endpoint failure and helps to maintain connectivity during maintenance events.
Direct Connect will never schedule a planned maintenance event that will simultaneously
take down your redundant connections. For the steps to use the AWS Direct Connect Resiliency Toolkit to
configure maximum resiliency, see [Configure maximum resiliency](max-resiliency-set-up.md "max-resiliency-set-up.md").

During a planned maintenance event, Direct Connect drains traffic to and from the connection
endpoint undergoing maintenance and forces traffic to use your redundant connections.
This allows for more seamless network traffic re-routing without the need for manual
intervention if maximum resiliency were not configured. Alternately, you might choose to
control traffic re-routing between redundant connections during the maintenance windows
by using local preference Border Gateway Protocol (BGP) communities. For more
information about BGP communities, see [Routing policies and BGP communities](routing-and-bgp.md "routing-and-bgp.md").

Configuring your Direct Connect environment with the maximum resiliency model helps ensure
your business is not impacted during maintenance events and infrastructure failures.
When properly implemented and tested, you typically do not need to take any actions for
these maintenance events.

### Resiliency validation

If you’ve configured your Direct Connect environment to be resilient, regularly validate
that your traffic routes through other redundant connections when a connection is
out-of-service. Regular proactive testing can help identify and resolve any
potential issues before they impact production workloads during a real maintenance
event or failure scenario. This will ensure greater confidence in the reliability of
your network during a maintenance event. Use the Direct Connect Failover test to
validate the resiliency of your redundant connections. For the steps to use the
Direct Connect Failover test, see [Direct Connect failover test](resiliency_failover.md "resiliency_failover.md").

You can also leverage Amazon CloudWatch Network Monitor to provide active monitoring of
your Direct Connect connections. For more information, see [Monitor hybrid connectivity with Amazon CloudWatch Network Synthetic Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/ "https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/").

## Requests for maintenance event postponement or

cancellation

Direct Connect devices are shared across multiple customers. Therefore, we do not accommodate
specific requests for maintenance rescheduling or cancellation. Rescheduling or
cancellation requests for one customer can negatively impact other customers using that
endpoint. This can also pose a risk for mitigating availability or security issues in a
timely manner.
