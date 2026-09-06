

# Update fleet locations
<a name="fleets-update-locations"></a>

You can add or remove a fleet's remote locations using the Amazon GameLift Servers console or the AWS CLI. You can't change a fleet's home Region.

------
#### [ Console ]

1. In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/), in the navigation pane, choose **Fleets**.

1. Choose the fleet you want to update. A fleet must be in `ACTIVE` status before you can edit it.

1. On the Fleet detail page, choose the **Locations** tab to view the fleet's locations. 

1. To add new remote locations, choose **Add** and select the locations you want to deploy instances to. This list doesn't include instances where the fleet's instance type isn't available.

1. With new locations selected, choose **Add**. Amazon GameLift Servers adds the new locations to the list, with status set to `NEW`. Amazon GameLift Servers then begins provisioning an instance in each added location and preparing it to host game sessions.

1. To remove existing remote locations from the fleet, use the check boxes to select one or more listed locations. 

1. With one or more fleets selected, choose **Remove**. The removed locations remain in the list, with status set to `DELETING`. Amazon GameLift Servers then begins the process of terminating activity in the removed location. If there are active instances that are hosting game sessions, Amazon GameLift Servers uses the game server termination process to gracefully end game sessions, terminate game servers, and shut down instances.

------
#### [ AWS CLI ]

 

Use the following AWS CLI commands to update fleet locations:
+ [create-fleet-locations](https://docs.aws.amazon.com/cli/latest/reference/gamelift/create-fleet-locations.html)
+ [delete-fleet-locations](https://docs.aws.amazon.com/cli/latest/reference/gamelift/delete-fleet-locations.html)

------