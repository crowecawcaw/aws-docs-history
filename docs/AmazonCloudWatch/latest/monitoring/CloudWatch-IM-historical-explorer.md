# Analyze historical data in Internet Monitor (Analyze page)

On the **Analyze** page in the Internet Monitor console, you can view your application's the top client locations
for the traffic that you monitor, by traffic volume. You can also view graphs showing performance and
availability scores for your traffic over time, as well as graphs of other internet traffic metrics for
your application's monitored traffic.

To start exploring Internet Monitor data for your application traffic, select a time period. Then, choose a specific geographical location, such a city, and
(optionally) other filters. Internet Monitor applies the filters to your data, and then you can see graphs of the data that show measurements
for your application. The graphs included on the **Analyze** page include your application's performance score,
availability score, monitored bytes transferred (for VPCs, Network Load Balancers, and CloudFront distributions) or client connection counts (for WorkSpaces
directories), and round-trip time (RTT) for your application over time.

The options at the top of the **Analyze** page determine the timeframe and
types of traffic shown in the graphs on the page. You can filter by client locations or ASN, or choose to show
traffic graphs at a specific granularity (the default is city level).

**Top client locations**
The **Top client locations** graph displays your top monitored traffic locations,
by default. You can choose another field to sort the graph by, or you can sort the graph in other ways, for example, by lowest
traffic locations.

The filters that you choose for the page determine the Regions, timeframe, and so on for the locations.

**Traffic health scores**

This section shows you graphs of traffic health scores and metrics for your monitored traffic.
These graphs reflect data for the filters that you choose at the top of the page.

The **Traffic health scores** graph shows you performance and availability information
for your local and overall traffic by calling out health events that have impacted your monitored client traffic.
AWS has substantial historical data about internet performance and availability for network traffic between
geographic locations for different ASNs and AWS services. Internet Monitor uses the connectivity data that AWS has captured
from its global networking footprint to calculate a baseline of
performance and availability for internet traffic. This is the same data that we use at AWS to monitor our own internet
uptime and availability.

With those measurements as a baseline, Internet Monitor can detect when the performance and availability for your application
has dropped, compared to the baseline. To make it easier to see those drops,
we report that information to you as a performance score and an availability score. For more information, see
[How AWS calculates performance and availability
scores](CloudWatch-IM-inside-internet-monitor.md#IMExperienceScores "CloudWatch-IM-inside-internet-monitor.md#IMExperienceScores").

Additional graphs show the monitored bytes transferred (for VPCs, Network Load Balancers, and CloudFront
distributions) or client connection counts (for WorkSpaces directories), and round-trip time (RTT) for your
application traffic.

Note that when round-trip time (RTT) is aggregated across end-user locations, the value is weighted by the amount
of your traffic that is driven by each client location. For example, with two client locations, one serving 90% of
traffic with a 5 ms RTT, and the other serving 10% of traffic with a 10 ms RTT,
the result is an aggregated RTT of 5.5 ms (which comes from 5 ms \* 0.9 + 10 ms \* 0.1).

You can also explore the internet measurements that Internet Monitor stores for your monitored traffic by using CloudWatch
tools or other methods. For more information, see [Exploring your data with CloudWatch tools and the Internet Monitor query interface](CloudWatch-IM-view-cw-tools.md "CloudWatch-IM-view-cw-tools.md").
In addition, you can create CloudWatch alarms based on Internet Monitor data, for example, to notify you of health events. For more
information, see [Create alarms with Internet Monitor](CloudWatch-IM-create-alarm.md "CloudWatch-IM-create-alarm.md").
