# Delete a fleet

You can delete a fleet when you no longer need it. Deleting a fleet permanently
removes all data associated with game sessions and player sessions, and collected metric
data. As an alternative, you can retain the fleet, disable auto scaling, and manually
scale the fleet to 0 instances.

###### Note

If the fleet has a VPC peering connection, first request authorization by calling
[CreateVpcPeeringAuthorization](../apireference/API_CreateVpcPeeringAuthorization.md "../apireference/API_CreateVpcPeeringAuthorization.md"). Amazon GameLift Servers deletes the VPC peering connection
during fleet deletion.

You can use either the Amazon GameLift Servers console or the AWS CLI tool to delete a
fleet.

Console

1. In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), in the navigation pane, choose
   **Fleets**.
2. Choose the fleet you want to delete. You can only delete fleets in
   `ACTIVE` or `ERROR` status.
3. Choose **Delete**.
4. In the **Delete fleet** dialog box, confirm the
   deletion by entering `delete`.
5. Choose **Delete**.

AWS CLI

Use the following AWS CLI command to delete a fleet:

- [delete-fleet](../../../cli/latest/reference/gamelift/delete-fleet.md "../../../cli/latest/reference/gamelift/delete-fleet.md")
