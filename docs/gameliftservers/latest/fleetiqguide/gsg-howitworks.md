# How Amazon GameLift Servers FleetIQ works

The Amazon GameLift Servers FleetIQ solution is a game hosting layer that supplements the full set of computing
resource management tools that you get with Amazon EC2 and Auto Scaling. In addition to offering a slate
of features specific to game hosting, Amazon GameLift Servers FleetIQ provides an extra layer of logic that makes
it possible to use low-cost Spot Instances for game hosting. This solution lets you directly
manage your Amazon EC2 and Auto Scaling resources and integrate as needed with other AWS
services.

When using Amazon GameLift Servers FleetIQ, you prepare to launch Amazon EC2 instances as usual: make an Amazon
Machine Image (AMI) with your game server software, create an Amazon EC2 launch template, and
define configuration settings for an Auto Scaling group. However, instead of creating an Auto Scaling group
directly, you create a Amazon GameLift Servers FleetIQ game server group with your Amazon EC2 and Auto Scaling resources and
configuration. This action prompts Amazon GameLift Servers FleetIQ to create both a game server group and a
corresponding Auto Scaling group. The game server group is linked to and manages certain aspects of
the Auto Scaling group.

After the Auto Scaling group is created, you have full access to your Amazon EC2 and Auto Scaling resources.
You can change the configuration of your Auto Scaling groups, add multi-level scaling policies or
load balancers, and integrate with other AWS services. You can connect directly to
instances in the group. As part of its optimization logic, Amazon GameLift Servers FleetIQ also makes periodic
updates to certain Auto Scaling group properties. You can track the availability status of all
instances deployed by the Auto Scaling group.

You can temporarily suspend Amazon GameLift Servers FleetIQ activity for a game server group at any time. You
also have the option to delete a game server group but retain the corresponding Auto Scaling
group.

###### Topics

- [Amazon GameLift Servers FleetIQ logic](gsg-howitworks-logic.md "gsg-howitworks-logic.md")
- [Key resources and components](gsg-howitworks-resources.md "gsg-howitworks-resources.md")
