# Manually set capacity for a Amazon GameLift Servers fleet

When you create a new fleet, Amazon GameLift Servers automatically sets the desired instances to one
instance in each fleet location. Then, Amazon GameLift Servers deploys one new instance in each location. To
change fleet capacity, you can add a target-based auto scaling policy, or you can manually
set the number of instances that you want for a location. For more information, see [Scaling fleet capacity](gamelift-howitworks.md#gamelift-howitworks-capacity "gamelift-howitworks.md#gamelift-howitworks-capacity").

Setting a fleet's capacity manually can be useful when you don't need auto scaling or when
you need to hold capacity at a specified level. Manually setting capacity works only if you
aren't using a target-based auto scaling policy. If you have a target-based auto scaling
policy, it immediately resets the desired capacity based on its own scaling rules.

You can manually set capacity in the Amazon GameLift Servers console or by using the AWS Command Line Interface (AWS CLI). The
fleet's status must be active.

## Suspend auto scaling

You can suspend all auto scaling activity for each fleet location. With auto scaling
suspended, the desired number of instances in the fleet location remains the same unless
manually changed. When you suspend auto scaling for a location, it affects the fleet's
current policies and any policies that you may define in the future.

## To manually set fleet

capacity

Console

1. Open the
   [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/").
2. In the navigation pane, choose **Hosting**, **Fleets**.
3. On the **Fleets** page, choose the name of an active fleet to open the fleet's
   detail page.
4. On the **Scaling** tab, under **Suspended
   auto-scaling locations**, select each location that you
   want to suspend auto scaling for, and then choose
   **Suspend**.
5. Under **Scaling capacity**, select a location
   that you want to set manually, and then choose
   **Edit**.
6. In the **Edit scaling capacity** dialog box, set
   your preferred value for **Desired instances**, and
   then choose **Confirm**. This tells Amazon GameLift Servers the
   number of instances to maintain in an active state, ready to host
   game sessions.

Amazon GameLift Servers responds to the changes by deploying additional instances or
shutting down unneeded ones. As Amazon GameLift Servers completes this process, the number of
active instances in the location changes to match the updated desired
instances value. This process may take a little time.

AWS CLI

1. **Check current capacity settings.**
   In a command line window, use the [describe-fleet-location-capacity](../../../cli/latest/reference/gamelift/describe-fleet-location-capacity.md "../../../cli/latest/reference/gamelift/describe-fleet-location-capacity.md") command with the fleet
   ID and location that you want to change capacity for. This command
   returns a [FleetCapacity](../apireference/API_FleetCapacity.md "../apireference/API_FleetCapacity.md") object that includes the location's
   current capacity settings. Determine whether the instance limits can
   accommodate the new desired instances setting.

```
aws gamelift describe-fleet-location-capacity \
    --fleet-id `<fleet identifier>` \
    --location `<location name>`
```

2. **Update desired capacity.** Use the
   [update-fleet-capacity](../../../cli/latest/reference/gamelift/update-fleet-capacity.md "../../../cli/latest/reference/gamelift/update-fleet-capacity.md") command with the fleet ID,
   location, and a new value for desired instances. If this value falls
   outside the current limit range, you can adjust limit values in the
   same command.

```
--fleet-id `<fleet identifier>`
--location `<location name>`
--desired-instances `<fleet capacity as an integer>`
--max-size `<maximum capacity>`    [Optional]
--min-size `<minimum capacity>`    [Optional]
```

Example:

```
aws gamelift update-fleet-capacity \
    --fleet-id fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa \
    --location us-west-2 \
    --desired-instances 5 \
    --max-size 10 \
    --min-size 1
```

If your request is successful, Amazon GameLift Servers returns the fleet ID. If the new
desired instances setting is outside the minimum and maximum limits, Amazon GameLift Servers
returns an error.
