# Using Internet Monitor

Internet Monitor provides visibility into how internet issues impact the performance and availability 
 between your applications hosted on AWS and your end users. It can reduce the time it takes for you to diagnose 
 internet issues from days to minutes. Internet Monitor uses the connectivity data that AWS captures from its global 
 networking footprint to calculate a baseline of performance and availability for internet-facing traffic. This 
 is the same data that AWS uses to monitor internet uptime and availability. With those measurements 
 as a baseline, Internet Monitor raises awareness for you when there are significant problems for your 
 end users (clients) in the different geographic locations where your application runs.

In the Amazon CloudWatch console, you can see a global view of traffic patterns and health events, and easily 
 drill down into information about events, at different geographic granularities (locations). You can clearly 
 visualize impact, and pinpoint the client locations and networks (ASNs, typically internet service providers or ISPs)
 that are affected. If Internet Monitor determines that an internet availability or performance issue is caused by a specific 
 ASN or by the AWS network, it provides that information.

To get started, create a monitor that includes one or more resources, so Internet Monitor can create a traffic profile
 for your AWS application. Then, view information in the Internet Monitor dashboard to visualize data and get insights and suggestions
 about your application's internet traffic.

For information about Regional support, pricing, how Internet Monitor works, and other overview content, see 
 [What is Internet Monitor?](CloudWatch-InternetMonitor.md "CloudWatch-InternetMonitor.md"). 
 To begin working with Internet Monitor, see [Getting started with Internet Monitor using the console](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").
