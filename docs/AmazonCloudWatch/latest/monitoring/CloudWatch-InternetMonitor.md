# Global internet weather map in Internet Monitor

Internet Monitor displays a global internet weather map that is available to all AWS customers. To view the map, in the
Amazon CloudWatch console, navigate to **Network Monitoring**, and then choose **Internet
monitors**.

The internet weather map highlights internet events ("outages") all over the world that affect AWS customers, with the
specific cities and networks (ASNs, typically internet service providers) where there are issues with performance
or availability. The map includes internet events from the past 24 hours.

You don't need to create a monitor in Internet Monitor to view the internet weather map. Unlike health events in Internet Monitor, internet events
are not specific to individual customers or their application traffic.

On the internet weather map, you can choose an internet event to learn details about it. For an internet event,
you can see the start time, end time (if the event is over), the current status (Active or Resolved),
and the outage issue type (Availability or Performance). To learn more about how the internet weather
map is created and what is included, see the [global
internet weather map FAQ](CloudWatch-IM-inside-internet-monitor.md#IMGlobalOutagesFAQ "CloudWatch-IM-inside-internet-monitor.md#IMGlobalOutagesFAQ").

To view and work with detailed information that is specific to your application traffic and client locations,
you can create a monitor in Internet Monitor for your application. Then, you'll see performance and availability patterns
and events, current and historical, as well as get health event alerts, tailored to just your application footprint
and customers. The internet weather map gives you an overall view, while a specific monitor filters the information to
just the measurements and details that are relevant to your application. With a monitor, you
can also explore historical metrics and get recommendations for improving client experience for your application.
To learn more, see [Getting started with Internet Monitor using the console](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").
