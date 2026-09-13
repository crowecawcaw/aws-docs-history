

# SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns
<a name="smsus02-bp01"></a>

Provision streaming infrastructure to follow actual viewer demand rather than a fixed peak assumption. Streaming demand is highly variable across the day, the week, and individual events, so capacity sized for the highest conceivable peak spends most of its life idle, consuming resources for an audience that isn't watching.

**Desired outcome:**
+ Media processing and delivery capacity scales up and down with real-time viewer demand rather than holding a static peak.
+ Delivery quality adapts to each viewer's network and device, so no more bit rate is sent than the conditions can use.
+ Non-time-critical processing runs during off-peak or lower-carbon-intensity periods rather than competing with peak demand.

**Common anti-patterns:**
+ Provisioning media processing capacity for the highest conceivable peak and leaving it running continuously, so most capacity sits idle most of the time.
+ Delivering a single high bit rate to all viewers regardless of device or network, sending more bits than many sessions can use.
+ Running batch transcoding and other deferrable work during peak demand periods, adding load when the system is already busy.
+ Scaling on a fixed schedule that doesn't reflect actual viewing patterns, so capacity and demand drift apart.

**Benefits of establishing this best practice:**
+ Reduced idle capacity, because infrastructure scales to demand rather than a static peak.
+ Lower delivery energy, because adaptive bit rate sends only the quality each session can use.
+ Smoother resource use, because deferrable work is shifted away from peak periods.
+ Cost that tracks demand, because capacity is right-sized continuously rather than provisioned for a worst case.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

The core inefficiency in streaming infrastructure is the gap between provisioned and used capacity. Demand varies by orders of magnitude between a quiet weekday morning and a marquee live event, so capacity fixed at the peak is idle for the majority of its life while still consuming resources. Demand-responsive scaling closes that gap by adding capacity as concurrency rises and removing it as concurrency falls, so resource use tracks the audience. A sudden demand spike, such as the start of a live event, can outrun reactive scaling, so combine reactive scaling with predictive scaling or pre-warming ahead of known events rather than relying on reaction alone.

Adaptive bit rate streaming applies the same match-to-demand principle to delivery. Rather than sending one quality level to every viewer, it matches the rendition to the viewer's measured network and device capability, so a session that can't use a high bit rate isn't sent one. This reduces delivery bits across the audience without degrading the experience, because the quality delivered is the quality the session can actually use.

Much media processing (catalog transcoding, analytics, and packaging of non-live content) is deferrable, so running it during off-peak or lower-carbon-intensity periods moves load away from peak demand and can place it when the grid is cleaner. Energy use isn't measurable per stream, so use resource proxies such as capacity utilization, idle instance hours, and bytes delivered per session. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes monthly.

### Implementation steps
<a name="implementation-steps"></a>

1. **Analyze viewing patterns to establish demand profiles:** Examine historical viewing data to identify peak and off-peak periods and the shape of demand around events, and use these profiles to drive scaling and scheduling decisions.

1. **Scale media processing to demand:** Configure Amazon EC2 Auto Scaling for media processing components against concurrency and utilization metrics, so capacity follows the audience rather than a fixed peak.

1. **Pre-warm capacity for known spikes:** Use predictive scaling or scheduled scaling ahead of known live events so a sudden demand spike doesn't outrun reactive scaling.

1. **Deliver with adaptive bit rate streaming:** Implement adaptive bit rate protocols (HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH)) with a rendition ladder so each session receives only the quality its network and device can use.

1. **Schedule deferrable work off-peak:** Run batch transcoding, analytics, and other non-time-critical processing during off-peak or lower-carbon-intensity periods rather than during peak demand.

1. **Monitor utilization and refine policies:** Track the following in Amazon CloudWatch, and refine scaling and scheduling against these metrics and the monthly account-level figures from the AWS Customer Carbon Footprint Tool.
+ Capacity utilization
+ Idle instance hours
+ Bytes per session

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS03-BP01 Implement efficient encoding and delivery mechanisms](smsus03-bp01.html)
+ [SMSUS04-BP01 Design efficient, scalable live streaming workflows](smsus04-bp01.html)

**Related documents**
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part I](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part II, Codecs and Implementation](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-ii-codecs-and-implementation/)

**Related services**
+ [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)