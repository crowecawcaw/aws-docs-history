# Components and terms for Internet Monitor

Internet Monitor uses or references the following concepts.



**Monitor**
A monitor includes the resources for a single application that you want to view internet
 performance and availability measurements for, and that you want to get health event alerts about.
 When you create a monitor for an application, you add resources for the application to define 
 the cities (locations) for Internet Monitor to monitor. Internet Monitor uses the traffic patterns 
 from the application resources that you add so that it can publish internet performance 
 and availability measurements specific to just the locations and ASNs (typically, internet service 
 providers or ISPs) that communicate with your application. In other words, the resources that you add 
 create a scope of the *city-networks* that you want Internet Monitor to monitor and that you 
 want it to publish measurements for.


**Resource added to monitor ("monitored resource")**
A resource that you add to a monitor is a "monitored resource" in Internet Monitor. That is:



* Each VPC that you add in a Region is a monitored resource. When you add a VPC,
 Internet Monitor monitors the traffic for any internet-facing application in the VPC, for example, an
 application hosted on an Amazon EC2 instance, behind a Network Load Balancer, or an AWS Fargate container.
* Each Network Load Balancer that you add in a Region is a monitored resource.
* Each WorkSpaces directory that you add in a Region is a monitored resource.
* Each CloudFront distribution that you add is a monitored resource.

**Autonomous System Number (ASN)**
In Internet Monitor, an ASN typically refers to an internet service provider (ISP), such as Verizon or Comcast. 
 An ASN is a network provider that a client uses to access your internet application. An Autonomous System (AS) is a set of 
 internet routable internet protocol (IP) prefixes that belong to a network or a collection of networks that are all managed, 
 controlled, and supervised by one organization. 


**City-network (location and ASN)**
A city-network is the location (such as a city) that clients access your application resources from and the ASN, 
 typically an internet service provider (ISP), that clients access the resources through. To help control your bill, you can set a limit for
 the maximum number of city-networks for Internet Monitor to monitor for each monitor. You pay only for the actual number of city-networks that you monitor,
 up to the maximum number. For more information, see [Choosing a city-network maximum limit](IMCityNetworksMaximum.md "IMCityNetworksMaximum.md").
 


**Internet measurements**
Internet Monitor also publishes internet measurements to log files in CloudWatch Logs every five minutes for the top 500 city-networks
 for your monitored application traffic.


These measurements quantify the performance score, availability score, bytes transferred (bytes in and bytes out), and round-trip 
 time for your application's city-networks. These are measurements for the city-networks specific to 
 your VPCs, Network Load Balancers, CloudFront distributions, or WorkSpaces directories. Optionally, you can choose to publish internet measurements 
 and events for all monitored city-networks (up to the 500,000 city-networks service limit) to an Amazon S3 bucket.


**Metrics**
Internet Monitor generates aggregated metrics for CloudWatch metrics, for global traffic to your application and global 
 traffic to each AWS Region. For more information, see [View Internet Monitor metrics or set alarms in CloudWatch Metrics](CloudWatch-IM-view-cw-tools-metrics-dashboard.md "CloudWatch-IM-view-cw-tools-metrics-dashboard.md").


**Health event**
Internet Monitor creates a health event to alert you to a specific problem 
 that affects your application. Internet Monitor detects internet issues, such as increased network latency, across the world. It then uses its 
 historical internet measurements from across the AWS global infrastructure footprint to calculate the impact of 
 current issues on your application, and creates health events. Internet Monitor, by default, creates health events based on both overall
 impact and local impact thresholds. To learn more about health events, see [When Internet Monitor creates and resolves health events](CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop "CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop").


The default health event threshold, for both performance scores and availability scores, is 95%. If you like, 
 you can specify your own custom thresholds for when Internet Monitor creates health events. For more information about configuring 
 thresholds, see [Change health event thresholds](CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview "CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview"). 


Each health event includes information about the impacted city-networks. You can view health events in the CloudWatch console, 
 or by using an AWS SDK or AWS CLI with Internet Monitor API actions. Internet Monitor also sends Amazon EventBridge notifications for health events. For more 
 information, see [When Internet Monitor creates and resolves health events](CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop "CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop").


**Internet event**
Internet Monitor displays information about recent global health events, called internet events,
 on an internet weather map that is available to all AWS customers. You don't need to create a monitor in Internet Monitor to 
 view the internet weather map. Unlike health events, internet events are not specific to individual customers or their application 
 traffic. For more information, see 
 [Global internet weather map in Internet Monitor](CloudWatch-InternetMonitor.md "CloudWatch-InternetMonitor.md").



**Thresholds**
Internet Monitor creates health events based on both overall thresholds and local thresholds. You can change the default
 thresholds and configure other options, such as turning off local thresholds. For more information about configuring 
 thresholds, see [Change health event thresholds](CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview "CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview"). 


**Performance and availability scores**
By analyzing the data that AWS collects, Internet Monitor can detect when the performance and availability for 
 your application has dropped, compared to estimated baselines that Internet Monitor calculates. To make it easier to see those drops, Internet Monitor reports 
 the information to you as scores. A performance score represents the estimated percentage of traffic that is **not** 
 seeing a performance drop. Similarly, an availability score represents the estimated percentage of traffic that is **not** 
 seeing a availability drop. For more 
 information, see [How AWS calculates performance and availability scores](CloudWatch-IM-inside-internet-monitor.md#IMExperienceScores "CloudWatch-IM-inside-internet-monitor.md#IMExperienceScores").


**Bytes transferred and monitored bytes transferred**
Bytes transferred is the total number of bytes of ingress and egress traffic between an application 
 in AWS and the city-network (that is, the location and the ASN, typically the internet service provider) where 
 clients access an application. Monitored bytes transferred is a similar metric, but includes only bytes for monitored 
 traffic.


**Round-trip time**
Round-trip time (RTT) is how long it takes for a request from a client user to return a response to the user. 
 When RTT is aggregated across client locations (cities or other geographies), the value is weighted by how much 
 of your application traffic is driven by each client location.
