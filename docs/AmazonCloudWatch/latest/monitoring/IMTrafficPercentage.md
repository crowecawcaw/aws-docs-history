# Choose a percentage of traffic to monitor for your application

The coverage that you choose for the percentage of application traffic to monitor determines how many city-networks
(client locations and ASNs, typically internet service providers) for your application are monitored, up to an
optional city-networks maximum limit that you can also set.

You can choose the percentage of traffic to monitor when you create a monitor, or, with an existing monitor, by
choosing **Edit monitor** on any Internet Monitor dashboard page in the console.

If you choose to monitor less than 100% of your application traffic, you might have an observability gap in with your monitor.
That's because if there are health events that Internet Monitor creates where you aren't monitoring traffic, you won't be aware of
those issues. With a traffic percentage set to less than 100%, you might also have less coverage for the performance and
availability score information about client access to your application.

The following sections describe options to explore traffic percentage settings and coverage, and to get an idea
about the impact of increasing or decreasing coverage.

- [Explore changing your application traffic percentage](#IMExploreTrafficPercentage "#IMExploreTrafficPercentage")
- [View the number of city-networks monitored at different traffic
  percentage settings](#IMExploreTrafficGraphs "#IMExploreTrafficGraphs")

## Explore changing your application traffic percentage

You can explore values that you might want
to change your application traffic percentage to, by viewing the number of city-networks monitored when you change the percentage.
The procedure in this section provides step-by-step information.

In the Internet Monitor console, you can try increasing or decreasing the application traffic percentage for your monitor,
and view the estimated number of your city-networks that would be covered as a result. With this option, you can
quickly see how changing your traffic percentage affects the number of city-monitors are monitored. This can help you
to get a feel for what a good application traffic percentage to choose might be, for your application.

###### To explore monitoring coverage and update percentage of traffic monitored

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. In your list of monitors, choose a monitor.
4. On the **Configure** tab, in the **View and evaluate traffic coverage** section, you
   can evaluate the impact on the total number of city-networks that are monitored, depending on a traffic percentage that
   you choose. You can also update the percentage of traffic that you monitor or change the city-networks limit for
   your monitor.
   - **Explore traffic percentage options:** Under **Compare options for traffic coverage**, in the drop-down menu,
     choose one or more traffic percentages to graph and compare. For each traffic percentage that you choose,
     you can see the number of city-networks that will be monitored when you set that traffic percentage coverage.

   To learn more, see [View number of city-networks monitored at
   different percentages](#IMExploreTrafficGraphs "#IMExploreTrafficGraphs").
   - **Change monitoring coverage:** Under **Explore other traffic coverage options**,
     choose **Update monitoring coverage**.

   In the **Explore and set traffic monitoring coverage** dialog, click the arrows to increase or decrease the
   percentage of traffic to monitor. By choosing 100% traffic, you can see how many city-networks are monitored with full
   coverage for monitoring your application.

   Note: To learn more about how the number of city-networks monitored (estimated here) might affect your costs, choose
   the link to the [CloudWatch Pricing calculator](https://calculator.aws/#/addService/CloudWatch "https://calculator.aws/#/addService/CloudWatch"),
   and then scroll down to Internet Monitor.

   To set a new percentage of traffic to monitor, choose **Update monitor coverage**. Or, to
   keep the current coverage level, choose **Cancel**.

## View the number of city-networks monitored at different traffic percentage settings

You can view the number of city-networks that would be monitored for
your application at different application traffic percentages. The procedure in this section provides step-by-step information.

In the Internet Monitor console, you can view graphs that show how coverage for your city-networks would change at different
of application traffic percentages, over a time interval that you specify. This is a quick way to visualize and compare
the monitoring coverage for your application at specific traffic percentages, all on one graph.

###### To view graphs of application traffic percentage and corresponding city-networks coverage

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**, choose **Internet monitors**.
3. In your list of monitors, choose a monitor.
4. Choose the **Configure** page, and scroll down to **Traffic coverage**.
5. Under **Compare options for traffic coverage**, in the drop-down list, select one or more percentages.
   You can choose one or more application traffic percentages, and the graph of **Total monitored city-networks**
   is updated to display the monitoring coverage Internet Monitor provides for that traffic percentage. By choosing **City-networks
   at 100% traffic**, you can see how many city-networks are monitored with full coverage for monitoring your application.

Keep in mind the following:

- Traffic coverage is computed based on the number of city-networks in the previous hour of your
  application traffic. This means that, after you choose a specific percentage of traffic to monitor, fewer city-networks
  might be monitored for your application than is shown here in a traffic coverage comparison graph.
- To make sure that all your application traffic is monitored, set `TrafficPercentageToMonitor` to 100
  and don’t set `MaxCityNetworksToMonitor`. Alternatively, you can set `MaxCityNetworksToMonitor` to
  500,000, the upper limit in Internet Monitor.
- If you set a city-networks maximum limit, the total number of monitored city-networks never exceeds that limit,
  regardless of the application traffic percentage option that you select.
- You can learn more about how the number of city-networks monitored might affect your costs. On the
  [Pricing calculator for CloudWatch page](https://calculator.aws/#/addService/CloudWatch "https://calculator.aws/#/addService/CloudWatch"), scroll down
  to Internet Monitor.

To set a new percentage of traffic to monitor, under **Explore other traffic coverage options**,
choose **Update monitoring coverage**. In the dialog, choose a percentage of traffic, and then choose
**Update monitor coverage**.
