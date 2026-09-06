

# Outposts server maintenance
<a name="outpost-maintenance"></a>

Under the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS is responsible for the hardware and software that run AWS services. This applies to AWS Outposts, just as it does to an AWS Region. For example, AWS manages security patches, updates firmware, and maintains the Outpost equipment. AWS also monitors the performance, health, and metrics for your Outposts server and determines whether any maintenance is required.

**Warning**  
Data on instance store volumes is lost if the underlying disk drive fails, or if the instance terminates. To prevent data loss, we recommend that you back up your long-term data on instance store volumes to persistent storage, such as an Amazon S3 bucket or a network storage device in your on-premises network.

**Topics**
+ [Update contact details](#outpost-owner-update)
+ [Hardware maintenance](#outpost-hardware-maintenance-events)
+ [Firmware updates](#outpost-firmware-updates)
+ [Best practices for power and network events](#outpost-power-network-events)
+ [Cryptographically shred server data](#outpost-server-cryptographically-shred-data)

## Update contact details
<a name="outpost-owner-update"></a>

If the Outpost owner changes, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/) with the new owner's name and contact information.

## Hardware maintenance
<a name="outpost-hardware-maintenance-events"></a>

If AWS detects an irreparable issue with hardware during the server-provisioning process or while hosting Amazon EC2 instances running on your Outposts server, we will notify the owner of the instances that the affected instances are scheduled for retirement. For more information, see [Instance retirement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-retirement.html) in the *Amazon EC2 User Guide*.

AWS terminates the affected instances on the instance retirement date. The data on instance store volumes does not persist after instance termination. Therefore, it is important that you take action before the instance retirement date. First, transfer your long-term data from the instance store volumes for each affected instance to persistent storage, such as an Amazon S3 bucket or a network storage device in your network.

A replacement server will be shipped to the Outpost site. Then, do the following:
+ Remove the network and power cables from the irreparable server and if necessary remove it from your rack.
+ Install the replacement server in the same location. Follow the installation instructions in [Outposts server installation](https://docs.aws.amazon.com/outposts/latest/install-server/install-server.html).
+ Pack the irreparable server to AWS in the same packaging that the replacement server arrived in.
+ Use the pre-paid return shipment label that is available in the console attached to the order configuration details or the replacement server order.
+ Return the server to AWS. For more information, see [Return an AWS Outposts server](https://docs.aws.amazon.com/outposts/latest/server-userguide/shipping-outposts-server.html).

## Firmware updates
<a name="outpost-firmware-updates"></a>

Updating the Outpost firmware does not typically affect the instances on your Outpost. In the rare case that we need to reboot the Outpost equipment to install an update, you will receive an instance retirement notice for any instances running on that capacity.

## Best practices for power and network events
<a name="outpost-power-network-events"></a>

As stated in the [AWS Service Terms](https://aws.amazon.com/service-terms/) for AWS Outposts customers, the facility where the Outposts equipment is located must meet the minimum [power](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-power) and [network](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-networking) requirements to support the installation, maintenance, and use of the Outposts equipment. An Outposts server  can operate correctly only when power and network connectivity is uninterrupted.

### Power events
<a name="outpost-power-events"></a>

With complete power outages, there is an inherent risk that an AWS Outposts resource may not return to service automatically. In addition to deploying redundant power and backup power solutions, we recommend that you do the following in advance to mitigate the impact of some of the worst-case scenarios:
+ Move your services and applications off the Outposts equipment in a controlled fashion, using DNS-based or off-rack load-balancing changes.
+ Stop containers, instances, databases in an ordered incremental fashion and use the reverse order when restoring them.
+ Test plans for the controlled moving or stopping of services.
+ Back-up critical data and configurations and store it outside the Outposts.
+ Keep power downtimes to a minimum.
+ Avoid repeated switching of the power feeds (off-on-off-on) during the maintenance.
+ Allow for extra time within the maintenance window to deal with the unexpected.
+ Manage the expectations of your users and customers by communicating a wider maintenance window time-frame than you would normally need.
+ After power is restored, create a case at [AWS Support Center](https://console.aws.amazon.com/support/home#/) to request verification that AWS Outposts and the related services are running.

### Network connectivity events
<a name="outpost-network-events"></a>

The service link connection between your Outpost and the AWS Region or Outposts home Region will typically automatically recover from network interruptions or issues that may occur in your upstream corporate network devices or in the network of any third party connectivity provider once the network maintenance is completed. During the time the service link connection is down, your Outposts operations are limited to local network activities.

Amazon EC2 instances, LNI networking, and instance storage volumes on the Outposts server will continue to operate normally and can be accessed locally through the local network and LNI. Similarly, AWS service resources such as Amazon ECS worker nodes continue to run locally. However, API availability will be degraded. For example, the run, start, stop, and terminate APIs might not work. Instance metrics and logs will continue to be cached locally for up to 7 days, and will be pushed to the AWS Region when connectivity returns. Disconnection beyond 7 days might result in loss of metrics and logs.

If the service link is down because of an on-site power issue or the loss of network connectivity, the Health Dashboard sends a notification to the account that owns the Outposts. Neither you nor AWS can suppress the notification of a service link interruption, even if the interruption is expected. For more information, see [Getting started with your Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html) in the *AWS Health User Guide*.

In the case of a planned service maintenance that will affect network connectivity, take the following proactive steps to limit the impact of potential problematic scenarios:
+ If you are in control of the network maintenance, limit the duration of downtime for the service link. Include a step in your maintenance process that verifies that the network has recovered.
+ If you are not in control of the network maintenance, monitor the service link downtime with respect to the announced maintenance window and escalate early to the party in charge of the planned network maintenance if the service link is not back up at the end of the announced maintenance window.

### Resources
<a name="outpost-power-network-resources"></a>

Here are some monitoring related resources that can provide reassurance that the Outposts is operating normally after a planned or unplanned power or network event:
+ The AWS blog [Monitoring best practices for AWS Outposts](https://aws.amazon.com/blogs/mt/monitoring-best-practices-for-aws-outposts/) covers observability and event management best practices specific to Outposts.
+ The AWS blog [Debugging tool for network connectivity from Amazon VPC](https://aws.amazon.com/blogs/networking-and-content-delivery/debugging-tool-for-network-connectivity-from-amazon-vpc/) explains the *AWSSupport-SetupIPMonitoringFromVPC* tool. This tool is an AWS Systems Manager document (SSM document) that creates an Amazon EC2 Monitor Instance in a subnet specified by you and monitors target IP addresses. The document runs ping, MTR, TCP trace-route and trace-path diagnostic tests and stores the results in Amazon CloudWatch Logs which can be visualized in a CloudWatch dashboard (e.g. latency, packet loss). For Outposts monitoring, the Monitor Instance should be in one subnet of the parent AWS Region and configured to monitor one or more of your Outpost instances using its private IP(s) - this will provide packet loss graphs and latency between AWS Outposts and the parent AWS Region.
+ The AWS blog [Deploying an automated Amazon CloudWatch dashboard for AWS Outposts using AWS CDK](https://aws.amazon.com/blogs/compute/deploying-an-automated-amazon-cloudwatch-dashboard-for-aws-outposts-using-aws-cdk/) describes the steps involved in deploying an automated dashboard.
+ If you have questions or need more information, see [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#creating-a-support-case) in the *AWS Support User Guide*.

## Cryptographically shred server data
<a name="outpost-server-cryptographically-shred-data"></a>

The Nitro Security Key (NSK) is required to decrypt data on the server. When you return the server to AWS, either because you are replacing the server or discontinuing the service, you can destroy the NSK to cryptographically shred the data on the server.

**To cryptographically shred data on the server**

1. Remove the NSK from the server before shipping the server back to AWS.

1. Ensure that you have the correct NSK that shipped with the server.

1. Remove the small hex tool / Allen wrench from under the sticker.

1. Use the hex tool to turn the small screw under the sticker three full turns. This action destroys the NSK and cryptographically shreds all data on the server.  
![An NSK with labels identifying the hex tool and the thumbscrew where you insert the hex tool.](http://docs.aws.amazon.com/outposts/latest/server-userguide/images/nsk-details.png)