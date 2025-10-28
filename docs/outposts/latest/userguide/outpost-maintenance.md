# Outposts rack maintenance

Under the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"),
AWS is responsible for the hardware and software that run AWS services. This applies to
AWS Outposts, just as it does to an AWS Region. For example, AWS manages security patches,
updates firmware, and maintains the Outpost equipment. AWS also monitors the performance,
health, and metrics for your Outposts rack and determines whether any maintenance is
required.

###### Warning

Data on instance store volumes is lost if the underlying disk drive fails,
or if the instance stops, hibernates, or terminates. To prevent data loss, we recommend that
you back up your long-term data on instance store volumes to persistent storage, such as an
Amazon S3 bucket, an Amazon EBS volume, or a network storage device in your on-premises network.

###### Contents

- [Update contact details](#outpost-owner-update "#outpost-owner-update")
- [Hardware maintenance](#outpost-hardware-maintenance-events "#outpost-hardware-maintenance-events")
- [Firmware updates](#outpost-firmware-updates "#outpost-firmware-updates")
- [Network equipment maintenance](#outpost-network-equipment-maintenance "#outpost-network-equipment-maintenance")
- [Best practices for power and network
  events](#outpost-power-network-events "#outpost-power-network-events")

## Update contact details

If the Outpost owner changes, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") with the new owner's name
and contact information.

## Hardware maintenance

If AWS detects an irreparable issue with hardware during the server-provisioning process
or while hosting Amazon EC2 instances running on your Outposts rack, we will notify the owner of the instances that the affected instances are scheduled for
retirement. For more information, see [Instance retirement](../../../AWSEC2/latest/UserGuide/instance-retirement.md "../../../AWSEC2/latest/UserGuide/instance-retirement.md") in the _Amazon EC2 User Guide_.

The Outpost owner and instance owner can work together to
resolve the issue. The instance owner can stop and start an affected instance to migrate it to
available capacity. Instance owners can stop and start the affected instances at a time that
is convenient for them. Otherwise, AWS stops and starts the affected instances on the
instance retirement date. If there is no additional capacity on the Outpost, the instance
remains in the stopped state. The Outpost owner can try to free up used capacity or request
additional capacity for the Outpost so that the migration can complete.

If hardware maintenance is required, AWS will contact the
Outpost owner to confirm a date and time for the AWS installation team to visit. Visits can
be scheduled as soon as two business days from the time that the Outpost owner speaks with the
AWS team.

When the AWS installation team arrives on site, they will
replace the unhealthy hosts, switches, or rack elements and bring the new capacity online.
They will not perform any hardware diagnostics or repairs on site. If they replace a host,
they will remove and destroy the NIST-compliant physical security key, effectively shredding
any data that might remain on the hardware. This ensures that no data leaves your site. If
they replace an Outpost networking device, network configuration information might be present
on the device when it is removed from the site. This information might include IP addresses
and ASNs used to establish virtual interfaces for configuring the path to your local network
or back to the Region.

## Firmware updates

Updating the Outpost firmware does not typically affect the instances on your Outpost. In
the rare case that we need to reboot the Outpost equipment to install an update, you will
receive an instance retirement notice for any instances running on that capacity.

## Network equipment maintenance

Maintenance of Outpost Networking Devices (OND) is performed without affecting regular
Outpost operations and traffic. If maintenance is required traffic is shifted away from the
OND. You might notice temporary changes in BGP advertisements, such as AS-Path prepending, and
corresponding changes in traffic patterns on Outpost uplinks. With OND firmware updates, you
might notice BGP flapping.

We recommend that you configure customer network equipment to receive BGP advertisements
from Outposts without changing the BGP attributes, and enable BGP multipath/load balancing
to achieve optimal inbound traffic flows. AS-Path prepending is used for local gateway prefixes
to shift traffic away from ONDs if maintenance is required. The customer network should prefer
routes from Outposts with an AS-Path length of 1 over routes with an AS-Path length of 4.

The customer network should advertise equal BGP prefixes with the same attributes to
all ONDs. The Outpost network load balances outbound traffic between all uplinks by default.
Routing policies are used on the Outpost side to shift traffic away from an OND if
maintenance is required. This traffic shift requires equal BGP prefixes from the customer
side on all ONDs. If maintenance is required on the customer network, we recommend that you
use AS-Path prepending to temporarily shift traffic array from specific uplinks.

## Best practices for power and network

events

As stated in the [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/") for AWS Outposts customers, the facility where the Outposts equipment
is located must meet the minimum [power](outposts-requirements.md#facility-power "outposts-requirements.md#facility-power") and
[network](outposts-requirements.md#facility-networking "outposts-requirements.md#facility-networking") requirements to support the installation, maintenance, and use of the
Outposts equipment. An Outposts rack
can operate correctly only when power and network
connectivity is uninterrupted.

### Power events

With complete power outages, there is an inherent risk that an AWS Outposts resource may not
return to service automatically. In addition to deploying redundant power and backup power
solutions, we recommend that you do the following in advance to mitigate the impact of some
of the worst-case scenarios:

- Move your services and applications off the Outposts equipment in a controlled
  fashion, using DNS-based or off-rack load-balancing changes.
- Stop containers, instances, databases in an ordered incremental fashion and use the
  reverse order when restoring them.
- Test plans for the controlled moving or stopping of services.
- Back-up critical data and configurations and store it outside the Outposts.
- Keep power downtimes to a minimum.
- Avoid repeated switching of the power feeds (off-on-off-on) during the
  maintenance.
- Allow for extra time within the maintenance window to deal with the
  unexpected.
- Manage the expectations of your users and customers by communicating a wider
  maintenance window time-frame than you would normally need.
- After power is restored, create a case at [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to request
  verification that AWS Outposts and the related services are running.

### Network connectivity events

The service link connection between your Outpost and the AWS Region or Outposts home
Region will typically automatically recover from network interruptions or issues that may
occur in your upstream corporate network devices or in the network of any third party
connectivity provider once the network maintenance is completed. During the time the service
link connection is down, your Outposts operations are limited to local network
activities.

Amazon EC2 instances, Local gateway, and Amazon EBS volumes on the
Outposts will continue to operate normally and can be accessed locally through the local
network. Similarly, AWS service resources such as Amazon ECS worker nodes continue to run
locally. However, API availability will be degraded. For example, the run, start, stop, and
terminate APIs might not work. Instance metrics and logs will continue to be cached locally
for up to 7 days, and will be pushed to the AWS Region when connectivity returns.
Disconnection beyond 7 days might result in loss of metrics and logs.

For more information, see the question _What
happens when my facility's network connection goes down?_ on the [AWS Outposts rack FAQs](https://aws.amazon.com/outposts/rack/faqs/#Support_.26_maintenance "https://aws.amazon.com/outposts/rack/faqs/#Support_.26_maintenance")
page.

If the service link is down because of an on-site power issue or the loss of network
connectivity, the AWS Health Dashboard sends a notification to the account that owns the Outposts. Neither
you nor AWS can suppress the notification of a service link interruption, even if the
interruption is expected. For more information, see [Getting started with your
AWS Health Dashboard](../../../health/latest/ug/getting-started-health-dashboard.md "../../../health/latest/ug/getting-started-health-dashboard.md") in the _AWS Health User Guide_.

In the case of a planned service maintenance that will affect network connectivity, take
the following proactive steps to limit the impact of potential problematic scenarios:

- If your Outposts rack connects to the parent AWS Region through Internet or public Direct
  Connect, then in advance of a planned maintenance, capture a trace-route. Having a
  working (pre-network-maintenance) network path and a problematic
  (post-network-maintenance) network path to identify the differences would help in
  troubleshooting. If you escalate a post-maintenance issue to AWS or your ISP, you can
  include this information.

Capture a trace-route between:

    + The public IP addresses at the Outposts location and the IP address returned by
     the `outposts.`region`.amazonaws.com`. Replace
     `region` with the name of the parent AWS Region.
    + Any instance in the parent Region with public Internet connectivity and the
     public IP addresses at the Outposts location.

- If you are in control of the network maintenance, limit the duration of downtime for
  the service link. Include a step in your maintenance process that verifies that the
  network has recovered.
- If you are not in control of the network maintenance, monitor the service link
  downtime with respect to the announced maintenance window and escalate early to the
  party in charge of the planned network maintenance if the service link is not back up at
  the end of the announced maintenance window.

### Resources

Here are some monitoring related resources that can provide reassurance that the
Outposts is operating normally after a planned or unplanned power or network event:

- The AWS blog [Monitoring best practices for
  AWS Outposts](https://aws.amazon.com/blogs/mt/monitoring-best-practices-for-aws-outposts/ "https://aws.amazon.com/blogs/mt/monitoring-best-practices-for-aws-outposts/") covers observability and event management best practices specific to
  Outposts.
- The AWS blog [Debugging tool for network connectivity from Amazon VPC](https://aws.amazon.com/blogs/networking-and-content-delivery/debugging-tool-for-network-connectivity-from-amazon-vpc/ "https://aws.amazon.com/blogs/networking-and-content-delivery/debugging-tool-for-network-connectivity-from-amazon-vpc/") explains the
  _AWSSupport-SetupIPMonitoringFromVPC_ tool. This tool is an
  AWS Systems Manager document (SSM document) that creates an Amazon EC2 Monitor Instance in a subnet
  specified by you and monitors target IP addresses. The document runs ping, MTR, TCP
  trace-route and trace-path diagnostic tests and stores the results in Amazon CloudWatch Logs which
  can be visualized in a CloudWatch dashboard (e.g. latency, packet loss). For Outposts
  monitoring, the Monitor Instance should be in one subnet of the parent AWS Region and
  configured to monitor one or more of your Outpost instances using its private IP(s) -
  this will provide packet loss graphs and latency between AWS Outposts and the parent AWS
  Region.
- The AWS blog [Deploying an automated Amazon CloudWatch dashboard for AWS Outposts using AWS CDK](https://aws.amazon.com/blogs/compute/deploying-an-automated-amazon-cloudwatch-dashboard-for-aws-outposts-using-aws-cdk/ "https://aws.amazon.com/blogs/compute/deploying-an-automated-amazon-cloudwatch-dashboard-for-aws-outposts-using-aws-cdk/")
  describes the steps involved in deploying an automated dashboard.
- If you have questions or need more information, see [Creating a
  support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the _AWS Support User Guide_.
