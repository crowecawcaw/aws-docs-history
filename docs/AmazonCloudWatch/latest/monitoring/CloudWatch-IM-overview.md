# Track real-time performance and availability in Internet Monitor (Overview page)

The **Overview** page in the Internet Monitor console shows you a high-level view of performance and availability
for the traffic that your monitor tracks, and a timeline of when health events have impacted your monitored traffic.
The page also provides the top suggestion for a configuration change that could reduce latency for clients who
use your application in your top client location (by traffic volume).

**Traffic overview and Status**
The **Traffic overview** section provides an overall look at your application's
availability and performance. Note that this section shows _aggregated_ overall performance and availability scores that
consider all of the traffic for applications towards all end users and service locations. You can see health scores for specific client
locations and service locations by searching and filtering measurements information on the **Analyze** tab.

Under **Status**, you can see if your monitor is actively creating data
for your monitor or is waiting for data to be available. You can also see the percentage of your application's traffic
that you're monitoring. If you want to change the percentage, see the **Configure** page.

Internet Monitor uses a statistical process to create availability and performance scores for your monitored traffic.
AWS has substantial historical data about internet performance and availability for network traffic between
geographic locations for different ASNs and AWS services. Internet Monitor uses the connectivity data that AWS has captured
from its global networking footprint to calculate a baseline of availability and performance for internet traffic.
This is the same data that we use at AWS to monitor our own internet uptime and availability.

With those measurements as a baseline, Internet Monitor can detect when the performance and availability for your application
has dropped, compared to the baseline. To make it easier to see those drops,
we report that information to you as a performance score and an availability score.

For more information, see [How AWS calculates performance and availability
scores](CloudWatch-IM-inside-internet-monitor.md#IMExperienceScores "CloudWatch-IM-inside-internet-monitor.md#IMExperienceScores").

**Health events timeline**
The **Health events timeline** graph displays health events that have occurred during the
past 24 hours. A summary below the graph shows your application's current and recent impact. For details, you can choose **See
more health events**.

To change the thresholds for health events, go to the **Configure** page.

**Reduce latency for your top Region**
Internet Monitor automatically evaluates the AWS Region that your current application configuration uses most (that is, the
Region with the highest client volume), and determines if another Region could provide a better aggregate
time to first byte (TTFB) for your clients.

Note that because this is the aggregate TTFB, if you move traffic from one Region to another, TTFB for most locations is
expected to improve but clients in some Regions could see no change or reduced performance..

To explore more latency improvement suggestions, including details at more granular levels (such as by client
location), see the **Optimize** page.
