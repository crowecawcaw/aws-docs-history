# How Internet Monitor works

This section provides information about how Internet Monitor works. This includes descriptions of how AWS collects the data
that it uses to help detect connectivity issues across the internet, and how performance and availability scores are
calculated.

**Contents**

- [How Internet Monitor focuses on just your application traffic footprint](#IMTheAWSAdvantage "#IMTheAWSAdvantage")
- [How AWS measures connectivity issues and calculates measurements](#IMHowAWSMeasuresConnectivityIssues "#IMHowAWSMeasuresConnectivityIssues")
- [Geolocation accuracy in Internet Monitor](#IMGeolocationSourceAccuracy "#IMGeolocationSourceAccuracy")
- [When Internet Monitor creates and resolves health events](#IMHealthEventStartStop "#IMHealthEventStartStop")
- [Health event report timing](#IMEventDelay "#IMEventDelay")
- [How Internet Monitor works with IPv4 and IPv6 traffic](#IMIPv4IPv6 "#IMIPv4IPv6")
- [How Internet Monitor selects the subset of city-networks to include](#IM100citynetworks "#IM100citynetworks")
- [How the global internet weather map is created (Frequently Asked Questions)](#IMGlobalOutagesFAQ "#IMGlobalOutagesFAQ")

**How Internet Monitor focuses on just your application traffic footprint**
Internet Monitor focuses monitoring on just the subset of the internet that's accessed by the users of your AWS resources,
instead of broadly monitoring your website from every Region in the world as other tools do. It’s also a cost effective solution,
affordable for large and small companies.

Internet Monitor uses the same powerful probes and issue-detection algorithms that AWS takes advantage of internally and alerts
you to connectivity issues that affect your application by creating health events in Internet Monitor. Internet Monitor then gives you access to
the resulting performance and availability map, by overlaying the traffic profile that it creates from your
active viewers, based on your application resources.

Using this information, Internet Monitor shows you just relevant events (that is, the events from places where you have active viewers),
and just the impact those events have on your overall viewer volume. So, how much impact an event has, percentage-wise, is
based on your total traffic worldwide.

Internet Monitor stores internet measurements for pairs of your client locations and ASNs, or _city-networks_.
Internet Monitor also creates aggregated CloudWatch metrics for traffic to your application, and to each AWS Region and edge location.

In addition, Internet Monitor publishes internet measurements to CloudWatch Logs internet every five minutes for the top 500 city-networks
that send traffic to each monitor, to support using CloudWatch tools and other methods with your data. Optionally,
you can choose to publish internet measurements for all monitored city-networks
(up to the 500,000 city-networks service limit) to an Amazon S3 bucket. For more information, see [Publish internet measurements to Amazon S3 in Internet Monitor](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").

The benefits of Internet Monitor include the following:

- Using Internet Monitor doesn't place additional load or cost on your application that's hosted on AWS.
- You don't need to include performance measurement code in your client-side resources, or in your application.
- You can get visibility into performance and availability across the internet that your application is
  connected to, including "last mile" information.

Note that because Internet Monitor creates measurements based on your AWS resources, Internet Monitor only creates events that are
specific to your application traffic. Global internet issues in general are not reported. In addition, when
the service location is an AWS Region, the measurements and events emitted are designed to represent connectivity at a Regional level
and don’t accurately represent connectivity between an end user location and an Availability Zone.

**How AWS measures connectivity issues and calculates measurements**
Internet Monitor uses internet connectivity data between different AWS Regions and Amazon CloudFront points of presence (POPs) to different
client locations through Autonomous System Numbers (ASNs), typically internet service providers (ISPs). This is the
connectivity data that is used internally by AWS operators, on a daily basis, to proactively detect connectivity issues across
the global internet.

For every AWS Region, we know which portions of the internet communicate with the Region and do the following:

- We actively monitor those portions of the internet, with a rolling 30-day window.
- We use both network and higher-level protocol probes, including both inbound and outbound probing.

AWS has active and passive probes that measure the latency (performance) at the 90th percentile and reachability (availability) from
every AWS Region and from the CloudFront service to the entire internet. Abnormal patterns in connectivity
between a service and a customer location are monitored, and then reported as alerts to the customer.

See the following sections for details:

- [Calculating availability and RTT](#IMCalculateLatency "#IMCalculateLatency")
- [Calculating performance and availability scores](#IMExperienceScores "#IMExperienceScores")
- [Calculating TTFB and RTT (latency)](#IMCalculateTTFB "#IMCalculateTTFB")
- [Regional and Availability Zone measurements and aggregation](#IMRegionalAZaggregation "#IMRegionalAZaggregation")

**Calculating availability and RTT**
Round-trip time (RTT) is how long it takes for a request from the user to return a response to the user. When round-trip time is
aggregated across end user locations, the value is weighted by the amount of your traffic that is driven by each end user
location.

As an example, with two end user locations, one serving 90% of traffic with a 5 ms RTT, and the other serving 10% of traffic with a 10 ms RTT,
the result is an aggregated RTT of 5.5 ms (which comes from 5 ms \* 0.9 + 10 ms \* 0.1).

Note that there are differences for resources about measuring last-mile latency. For Internet Monitor latency measurements, VPCs, Network Load Balancers, and WorkSpaces
directories do not include last-mile latency.

**Calculating performance and availability scores**
AWS has substantial historical data about internet performance and availability between AWS services and different city-networks
(locations and ASNs). By applying statistical analysis to the data, Internet Monitor can detect when the performance and availability
for your application has dropped, compared to an estimated baseline that it has calculated. To make it easier to see those drops,
that information is reported to you in the form of health scores: a performance score and an availability score.

Health scores are calculated at different granularities. At the finest granularity, we compute the health score for a geographic region,
such as a city or a metro area, and an ASN (a _city-network_). We also roll up the individual health scores to overall
health score numbers for an application in a monitor. If you view performance or availability scores without filtering for any specific
geography or service provider, Internet Monitor provides overall health scores.

Overall health scores span your whole application for the specified time period. When the performance or availability score for your
application's city-network pairs across your application reaches or drops below the corresponding health event threshold for performance or availability
Internet Monitor triggers a health event. By default, the threshold is 95% for both overall performance and availability. Internet Monitor also creates
health events based on local thresholds—if the option is enabled, as it is by default—based on values that you configure.
To learn more about configuring health event thresholds, see [Change health event
thresholds](CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview "CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview").

When you explore information
in the monitor and log files to investigate issues and learn more, you can filter by specific cities (locations), networks (ASNs or internet
service providers), or both. So, you can use filters to see health scores for different cities, ASNs, or city-network pairs, depending on the
filters that you choose.

- An _availability score_ represents the estimated percentage of traffic that is **not** seeing
  an availability drop. Internet Monitor estimates the percentage of traffic experiencing a drop from the total traffic seen and availability metrics
  measurements. For example, an availability score of 99% for an end user and service location pair is equivalent to
  1% of the traffic experiencing an availability drop for that pair.
- A _performance score_ represents the percentage of traffic that is **not**
  seeing a performance drop. For example, a performance score of 99% for an end user and service location pair is equivalent to
  1% of the traffic experiencing a performance drop for that pair.

**Calculating TTFB and RTT (latency)**

Time to first byte (TTFB) refers to the time between when a client makes a request and when it receives the first byte of information
from the server. AWS calculations for TTFB measure the time elapsed from Amazon EC2 or Amazon CloudFront to the Internet Monitor
measurement node (including the last mile of the node). That is, Internet Monitor measures time from the user to the Amazon EC2 Region for TTFB for EC2,
and from the user to CloudFront for TTFB for CloudFront.

For round-trip time (RTT), Internet Monitor includes the time from the city-network (that is, the client
location and ASN, typically an internet service provider), as mapped by the public IP address,
to the AWS Region. This means that Internet Monitor does not have last mile visibility for users who access the internet from
behind a gateway or VPN.

Note that there are differences for resources about measuring last-mile latency. For Internet Monitor latency measurements, VPCs, Network Load Balancers, and WorkSpaces
directories do not include last-mile latency.

Internet Monitor includes average TTFB information in the **Traffic optimization suggestions** section
of the **Traffic insights** tab on the CloudWatch dashboard, to help you evaluate options for different setups
for your application that can improve performance.

**Regional and Availability Zone measurements and aggregation**
Although Internet Monitor aggregates measurements and shares impact at a Regional level, it calculates impact at an Availability Zone (AZ)
level. This means that, if, for an event, only one AZ is impacted and most of your traffic flows through that AZ, you do see
impact for your traffic. However, for the same event, if your application traffic does not flow through an impacted AZ, you
do not see impact.

Note that this applies only to resources that aren't WorkSpaces directories. WorkSpaces directories are
measured only on a Regional level.

**Geolocation accuracy in Internet Monitor**

For location information, Internet Monitor uses IP-geolocation data supplied by
[MaxMind](https://dev.maxmind.com/geoip "https://dev.maxmind.com/geoip").
The accuracy of the location information in Internet Monitor measurements depends on the accuracy of MaxMind's data.

Be aware that `Metro` level measurements might not be accurate for locations outside of the
United States.

**When Internet Monitor creates and resolves health events**
Internet Monitor creates and closes health events for the application traffic that you monitor based on the current
thresholds that are set. Internet Monitor has a default threshold configuration, and you can also set your own configuration for thresholds.
Internet Monitor determines the overall impact that connectivity issues are having on your application, and the impact on local areas
where your application has clients, and creates health events when the thresholds are crossed.

Internet Monitor calculates the impact of connectivity issues on a client location based on the historical data
about internet performance and availability for network traffic that's available to the service through AWS. It applies the
information relevant to your application, based on the geographic locations for ASNs and services where clients
use your application: the city-network pairs that are affected. The locations are determined from the resources
that you add to your monitor. Then Internet Monitor uses statistical analysis to detect when performance and availability has dropped,
affecting the client experience for your application.

The performance and availability scores that Internet Monitor calculates are represented as the percentage of traffic
that is **not** seeing a drop. Impact is the opposite of this: it's a representation
of how much an issue is problematic for a customer's end users. So if there is a global availability drop of 93%,
for example, the corresponding impact would be 7%.

When the performance or availability score for your application's city-network pairs globally reaches or drops below the
corresponding health event threshold for performance or availability, this triggers Internet Monitor to generate a health event. By default,
the threshold is 95% for both performance and availability. The values to meet, or drop below, the threshold are cumulative,
so it could mean several smaller events combine to meet the threshold percentage, or that a single event meets or falls below
the threshold level.

As long as performance or availability scores that triggered the event are at or below the corresponding health event threshold
percentage for overall impact, the health event stays active. When the score or combined scores that triggered the event rise above the threshold,
Internet Monitor resolves the health event.

Internet Monitor also creates health events based on local thresholds and the percentage of overall traffic that an issue has an impact on.
You can configure options for local thresholds, or turn off local thresholds altogether.

The default health event threshold, for both performance scores and availability scores, is 95%. If you like,
you can specify your own custom thresholds for when Internet Monitor creates health events. For more information about configuring
thresholds, see [Change health event thresholds](CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview "CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview").

**Health event report timing**
Internet Monitor uses an aggregator to gather all signals about internet issues, to create health events in monitors within minutes.

When possible, Internet Monitor analyzes the origin of a health event, to determine whether it was caused by AWS or an ASN.
Health event analysis continues after an event is resolved. Internet Monitor can update events with new information for up to an hour.

**How Internet Monitor works with IPv4 and IPv6 traffic**
Internet Monitor measures health toward a network over only IPv4, and shows you health events, and
availability and performance metrics, if you serve traffic to that network over any IP family (IPv4
or IPv6). If you serve traffic from a dual-stack resource, such as a dual-stack CloudFront distribution,
Internet Monitor raises a health event and shows a drop in a performance score or availability score only if
IPv4 traffic has the same issues for the resource as IPv6 traffic does.

Note that the Internet Monitor metrics for overall bytes in and bytes out accurately reflect all internet
traffic (IPv4 and IPv6).

**How Internet Monitor selects the subset of city-networks to include**
When you set a maximum limit for the number of city-networks monitored by your monitor
or choose a percentage of traffic to monitor, Internet Monitor chooses
the city-networks to include (monitor) based on highest recent traffic volume.

For example, if you set a maximum city-networks limit of 100, Internet Monitor monitors (up to) 100 city-networks
based on your application traffic during a recent one hour period. Specifically,
Internet Monitor monitors the top 100 city-networks that have had the most traffic in the most recent one hour window
_before_ the latest one hour window.

To illustrate this, say that the current time is 2:30 PM. In this scenario, the traffic that
you see in your monitor was captured between 1:00 PM and 2:00 PM, and the traffic volume
measurement that Internet Monitor uses to determine the top 100 city-networks was captured between 12:00 PM and 1:00 PM.

**How the global internet weather map is created (Frequently Asked Questions)**
The Internet Monitor internet weather map is available on the Internet Monitor console to all authenticated AWS customers. This section
includes details about how the internet weather map is created and how to use it.

**What is the Internet Monitor internet weather map?**
The internet weather map provides a visual representation of internet issues across the world. It
highlights impacted client locations, that is, cities plus ASN (typically internet service providers). The map shows
a combination of availability and performance issues that have recently impacted clients' internet experience
for top client locations and AWS services globally.

**Where does data for the map come from?**
The data is based on a combination of active and passive probing of the internet. To learn more about how Internet Monitor measures data
you can read the section [How AWS measures connectivity issues](#IMHowAWSMeasuresConnectivityIssues "#IMHowAWSMeasuresConnectivityIssues").

**How often is the map updated?**
The internet weather map is updated every 15 minutes.

**Which networks are tracked for outages?**
AWS tracks networks all around the world that represent important IP prefixes used by
customers for making internet connections to AWS. We scope outages to client locations that
are top talkers for volume of traffic sent to and received from the AWS network.

**What determines whether an internet event is included on the map?**
Here are some high level criteria that we use to determine whether an internet event is
included on the internet weather map:

- AWS detects that there is an availability or performance event.
- If the event is short lived, for example, it lasts less than 5 minutes, we ignore it.
- Then, if the event is in a client location that is classified as a top talker, it's
  considered an outage.

**What thresholds are used for the internet weather map?**
Thresholds for determining outages are not static for the internet weather map. Internet Monitor determines what constitutes
an event based on detecting a deviation from expected values. You can learn more about how this works by reviewing
[how Internet Monitor determines when to create health events](#IMHealthEventStartStop "#IMHealthEventStartStop") for monitors
that you create with the service. When you create a monitor, Internet Monitor generates internet traffic health measurements
that are specific to your own application traffic. Internet Monitor also alerts you to health events for issues that affect
your application's internet traffic.

**What can I do with this data?**
The internet weather map provides a quick summary of key internet events that happened around the world
in the last 24 hours. It helps you to get a sense of the internet monitoring experience, without needing to
onboard your own internet traffic to Internet Monitor. To leverage the full potential of the internet monitoring capabilities
of AWS and to personalize it for your applications and services hosted on AWS, you can create a monitor
in Internet Monitor.

When you create a monitor, you enable Internet Monitor to identify the specific internet paths that affect your
application clients, and you get access to features and capabilities that can help you improve your client
experience. You'll also be proactively notified of new internet issues that specifically impact your
application traffic and clients.

**How can I get more details about events?**
Click an outage on the map to see details that include when an event started and ended,
the impacted city and ASN, and what type of issue it was (that is, a performance issue or an availability issue).

To get more detailed information about events, and to get custom measurements for your application traffic,
[create a monitor in Internet Monitor](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").
