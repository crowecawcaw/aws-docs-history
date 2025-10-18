# Add resources to your monitor

When you create a monitor, you must associate your application's resources with it: Amazon Virtual Private Clouds (VPCs), Network Load Balancers, 
 Amazon CloudFront distributions, Network Load Balancers (NLBs), or Amazon WorkSpaces directories. Then, Internet Monitor 
 knows where your application's internet-facing traffic and clients are located, and it can create
 and maintain a traffic profile that determines the relevant measurements to publish for your monitor.

You can add the following types of resources to a monitor in Internet Monitor as *monitored resources*.


* **VPCs:** Each VPC that you add in a Region is a monitored resource. When you add a VPC,
 Internet Monitor monitors the traffic for any internet-facing application in the VPC, for example, an
 application hosted on an Amazon EC2 instance, behind a Network Load Balancer, or in an AWS Fargate container.
* **Network Load Balancers:** Each NLB that you add is a monitored resource.
* **CloudFront distributions:** Each CloudFront distribution that you add is a monitored resource.
* **WorkSpaces directories:** Each WorkSpaces directory that you add in a Region is a monitored resource.
When you monitor traffic for VPCs, traffic for applications that are hosted on load balancers behind the VPC is
 monitored. You can choose to monitor traffic for individual Network Load Balancer load balancers instead of monitoring a VPC with
 multiple load balancers. This can be helpful, for example, if you need to understand and configure features for better
 performance or efficiencies at the load balancer level. Or, you might need compliance information at the Network Load Balancer level.

When you add resources to a monitor in Internet Monitor, be aware of the following:


* Internet Monitor doesn't support adding different types of resources together in one monitor.
* To generate meaningful output with Internet Monitor, VPCs that you add must be connected to the internet by having
 an Internet Gateway configured.
* Internet Monitor doesn't support adding different types of resources together in one monitor.
* There are Regional differences for opt-in Regions to keep in mind when you add VPCs or NLBs as resources. For more information, 
 see [Supported AWS Regions for Internet Monitor](CloudWatch-InternetMonitor.md "CloudWatch-InternetMonitor.md").
* In addition, there are differences for resources about measuring last-mile latency. For Internet Monitor latency measurements, 
 VPCs, NLBs, and WorkSpaces directories do not include last-mile latency.
