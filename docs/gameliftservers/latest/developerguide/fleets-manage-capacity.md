# Scaling game hosting capacity with Amazon GameLift Servers

Hosting capacity, measured in instances, represents the number of game sessions that Amazon GameLift Servers
can host concurrently and the number of concurrent players that those game sessions can
accommodate. One of the most challenging tasks with game hosting is scaling capacity to meet
player demand without wasting money on resources that you don't need. For more information,
see [Scaling fleet capacity](gamelift-howitworks.md#gamelift-howitworks-capacity "gamelift-howitworks.md#gamelift-howitworks-capacity").

Capacity is adjusted at the fleet location level. All fleets have at least one location:
the fleet's home AWS Region. When viewing or scaling capacity, the information is listed
by location, including the fleet's home Region and any additional remote locations.

You can manually set the number of instances to maintain, or you can set up auto scaling
to dynamically adjust capacity as player demand changes. We recommend that you start by
turning on the target-based auto scaling option. The goal of target-based auto scaling is to
maintain enough hosting resources to accommodate current players plus a little extra to
handle unexpected spikes in player demand. For most games, target-based auto scaling offers
a highly effective scaling solution.

You can do most fleet scaling activities using the Amazon GameLift Servers console. You can also use an
AWS SDK or the AWS Command Line Interface (AWS CLI) with the [service API for Amazon GameLift Servers](../apireference/Welcome.md "../apireference/Welcome.md").

###### Topics

- [To manage fleet capacity in the
  console](#fleet-manage-capacity-howto "#fleet-manage-capacity-howto")
- [Set Amazon GameLift Servers capacity limits](fleets-capacity-limits.md "fleets-capacity-limits.md")
- [Manually set capacity for a Amazon GameLift Servers fleet](fleets-updating-capacity.md "fleets-updating-capacity.md")
- [Auto-scale fleet capacity with Amazon GameLift Servers](fleets-autoscaling.md "fleets-autoscaling.md")
- [Scale Amazon GameLift Servers container fleets](containers-scaling.md "containers-scaling.md")

## To manage fleet capacity in the

console

1. Open the
   [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/").
2. In the navigation pane, choose **Hosting**, **Fleets**.
3. On the **Fleets** page, choose the name of an active fleet to open the fleet's
   detail page.
4. Choose the **Scaling** tab. On this tab, you can:
   - View historical scaling metrics for the entire fleet.
   - View and update capacity settings for each fleet location, including
     scaling limits and current capacity settings.
   - Update target-based auto scaling, view rule-based auto scaling
     policies applied to the entire fleet, and suspend auto scaling activity
     for each location.
