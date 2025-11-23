# Choose a city-networks maximum limit

In addition to setting a traffic percentage for your monitor in Internet Monitor, you can also set a maximum
limit for the number of city-networks monitored. This section describes how the city-networks limit can
help you manage billing costs, and provides information and an example to help you determine a limit to set,
if you choose to set one.

Internet Monitor can monitor traffic for some or all of the locations where clients access your AWS application
resources. You can set a monitoring limit for the number of _city-networks_, that is, the client locations
and the ASNs (typically internet service providers) that clients access your application through.

You choose a [percentage of application traffic](IMTrafficPercentage.md "IMTrafficPercentage.md") to monitor when you create your
monitor. The default percentage is 100%. You can update the percentage at any time, by editing the monitor.

The maximum limit that you set for the number of city-networks helps to make sure that your bill is predictable. For more information, see
[Amazon CloudWatch Pricing](https://aws.amazon.com//cloudwatch/pricing/ "https://aws.amazon.com//cloudwatch/pricing/").
You can also learn how different values for the number of city-networks actually monitored can affect your bill by using the CloudWatch price calculator.
To explore options, on the [Pricing calculator for CloudWatch page](https://calculator.aws/#/addService/CloudWatch "https://calculator.aws/#/addService/CloudWatch"),
scroll down to Internet Monitor.

To update your monitor and change the maximum city-networks limit, see [Edit a monitor in Internet Monitor](CloudWatch-IM-get-started.md "CloudWatch-IM-get-started.md").

## How billing works with city-networks maximum limits

Setting a maximum limit for the number of city-networks monitored can help prevent unexpected
costs in your bill. This is useful, for example, if your traffic patterns vary widely. Billing costs increase for each city-network that is monitored
after the first 100 city-networks, which are included (across all monitors per account). If you set a city-networks maximum limit, it caps the number of
city-networks that Internet Monitor monitors for your application, regardless of the percentage of traffic that you choose to monitor.

You only pay for the number of city-networks that are actually monitored. The city-network maximum limit that you choose
lets you set a cap on the total that can be included when Internet Monitor monitors traffic with your monitor. You can change the maximum
limit at any time by editing your monitor.

To explore options, on the [Pricing calculator for CloudWatch](https://calculator.aws/#/addService/CloudWatch "https://calculator.aws/#/addService/CloudWatch")
page, scroll down to Internet Monitor. For more information
on Internet Monitor pricing, see the Internet Monitor section on the [Amazon CloudWatch Pricing](https://aws.amazon.com//cloudwatch/pricing/ "https://aws.amazon.com//cloudwatch/pricing/") page.

## How to choose a city-networks maximum limit

Optionally, you can set a city-networks maximum limit. To help you decide on a maximum limit that you
might want to select, consider how much traffic you want to monitor for your application. Be aware that if you
choose 100% for the _traffic percentage to monitor_ for your monitor, and then specify a city-networks
maximum limit, depending on the limit that you choose, you might not monitor 100% of your application traffic. The
city-networks maximum that you set takes precedence over the traffic percentage to monitor that you set.

To view how the percentage of traffic to monitor that you choose affects the number of city-monitors that are included
for your application monitoring, which can help you decide whether to set a city-networks maximum limit, follow the steps in
[View the number of city-networks monitored at different traffic
percentage settings](IMTrafficPercentage.md#IMExploreTrafficGraphs "IMTrafficPercentage.md#IMExploreTrafficGraphs").

To explore your options in more detail, you can use Internet Monitor metrics, as described in the following examples. These examples show how
to select a maximum city-networks limit that is best for you, depending on the breadth of application internet traffic coverage you want. Using the
[queries for Internet Monitor metrics in CloudWatch Metrics](CloudWatch-IM-view-cw-tools-metrics-dashboard.md "CloudWatch-IM-view-cw-tools-metrics-dashboard.md") can help you
understand more about your application internet traffic coverage.

## Example of determining a city-networks maximum limit

As an example, say that you've set a monitoring maximum limit of 100 city-networks and that your application is accessed by clients across 2637
city-networks. In CloudWatch Metrics, you'd see the following Internet Monitor metrics returned:

```
CityNetworksMonitored 100
TrafficMonitoredPercent  12.5
CityNetworksFor90PercentTraffic  2143
CityNetworksFor100PercentTraffic  2637
```

From this example, you can see that you're currently monitoring 12.5% of your internet traffic, with the maximum limit set to 100 city-networks.
If you want to monitor 90% of your traffic, the next metric provides information about that: `CityNetworksFor90PercentTraffic`
indicates that you would need to monitor 2,143 city-networks for 90% coverage. To do that, you would update your monitor and
set the maximum city-networks limit to 2,143.

Similarly, say you'd like to have 100% internet traffic monitoring for your application. The next metric,
`CityNetworksFor100PercentTraffic`, indicates that to do this, you should update your monitor to set the maximum city-networks limit to
2,637.

If you now set the maximum to 5,000 city-networks, since that's greater than 2,637, you see the
following metrics returned:

```
CityNetworksMonitored 2637
TrafficMonitoredPercent  100
CityNetworksFor90PercentTraffic  2143
CityNetworksFor100PercentTraffic  2637
```

From these metrics, you can see that with the higher limit, you monitor all 2,637 city-networks, which is 100% of your internet
traffic.
