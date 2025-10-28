# Get suggestions to optimize application performance in Internet Monitor (Optimize page)

Use the **Optimize** page in the Internet Monitor console to get suggestions for how to optimize application performance
for your clients. Internet Monitor evaluates your monitored application traffic, and determines if you can reduce latency
by changing the AWS Regions that you've configured for your application. Optionally, you can also view latency changes if you choose to
include Amazon CloudFront in the suggestions.

You can review suggestions for your application's top Regions by traffic volume, or for top client locations, also by
traffic volume.

\***\*Suggestions to reduce latency for top Regions\*\***
To help you quickly understand your best options for reducing latency for your clients,
Internet Monitor automatically provides suggestions for improving latency in your application for your top Regions (by traffic volume).

You can also explore configuration changes for all the Regions
where your application serves clients. This includes getting details about each suggested change at deeper levels of granularity, for example,
by specific client location. To explore all Regional configurations and expected latency changes for your application,
choose **Optimization suggestions for all Regions**.

\***\*Suggestions to reduce latency for all Regions\*\***
To explore suggestions for reducing latency for all Regions where clients access your application,
choose **Optimization suggestions for all Regions** to open a new dashboard page. On this page,
you can select different Regions to configure, with the option of including CloudFront as a configuration comparison,
and then compare the times to first byte (TTFBs) for each selected configuration.

Then, for each comparison, you can also see a table with at a more granular level (by client location), with the
average expected TTFB for each one.

\***\*Suggestions to reduce latency for top locations\*\***
Internet Monitor also provides suggestions for reducing application latency for your clients by specific location. When the
table lists multiple suggestions for the same location, expand the city location for that row to see details.

Be aware that if you change a configuration to use a different Region or to use CloudFront, latency improvements can vary by
client location. For example, latency might improve for some locations, but stay the same or worsen for others.

\***\*Suggestions to reduce latency by updating routing configurations\*\***
Note: These suggestions are only relevant for application traffic to Regional load balancers.
The table is not shown for monitors that you create for CloudFront distributions or WorkSpaces resources.

With Internet Monitor, you can view information about latency toward AWS locations for IPv4 IP prefixes
that access your application using different DNS resolvers (typically ISPs). Using this information, you can take steps to reduce
latency for specific groups of users by routing a set of IP address prefixes, specified by a CIDR
collection, to your endpoints in a Region that results in lower latency for your users. If you
don't already have a CIDR collection for the prefixes, you can go to Amazon Route 53 to create one.
Then, you can update your routing in Route 53 to route IP addresses in the collection to a specific Region.

If you want to create a CIDR collection for a set of IP address prefixes, you can easily do so by
selecting a row or rows that includes the IP prefixes that you want, and then choosing **Add to CIDR
collection**. Then, in the Route 53 console, you can configure a routing policy that routes IP
addresses in the collection to the Region with lower latency for your application.

To learn more about IP-based routing in Route 53, see [IP-based routing](../../../Route53/latest/DeveloperGuide/routing-policy-ipbased.md "../../../Route53/latest/DeveloperGuide/routing-policy-ipbased.md").

By viewing the suggestions on this page, you can start planning configurations and deployments that can improve
performance for your clients. Note that you might see a dash (-) instead of a value in a column, when data is not available to display.

For more information about TTFB calculations, see [AWS
calculations for TTFB and latency](CloudWatch-IM-inside-internet-monitor.md#IMCalculateTTFB "CloudWatch-IM-inside-internet-monitor.md#IMCalculateTTFB"). To review a specific example of how to improve performance,
see [Using Internet Monitor for a Better Gaming Experience](https://aws.amazon.com/blogs/gametech/using-cloudwatch-internet-monitor-for-a-better-gaming-experience/ "https://aws.amazon.com/blogs/gametech/using-cloudwatch-internet-monitor-for-a-better-gaming-experience/").
