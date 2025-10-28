# Fleets in the Amazon GameLift Servers console

You can view information on all the fleets created to host your games on Amazon GameLift Servers under
your AWS account. The list shows fleets created your current Region. From the
**Fleets** page, you can create a new fleet or view additional detail
on a fleet. A fleet's [detail page](gamelift-console-fleets-metrics.md "gamelift-console-fleets-metrics.md")
contains usage information, metrics, game session data, and player session data. You can
also edit a fleet record or delete a fleet.

To view the **Fleets** page, choose **Fleets** from the
navigation pane.

The **Fleets** page displays the following summary information by
default. You can adjust the table content as needed using the **Preferences**
tool (see the ![Gear icon representing settings or configuration options.](images/settings.png)
icon in the upper right corner of the table). Custom preferences are saved to your AWS
account user and are automatically applied whenever you view this page.

- **ID** – An identifier assigned to the fleet. This ID is
  unique within the AWS Region where the fleet is created.
- **Name** – A friendly name given to the fleet.
- **Status** – The status of the fleet:
  **New**, **Downloading**,
  **Building**, and **Active**.
- **Creation time** – The date and time the fleet was
  created.

###### Note

A fleet displays a warning icon for fleets that were created more than 90
days ago. As a best practice, we recommend replacing fleets every 30 days to
maintain a secure and up-to-date runtime environment for your hosted game
servers. For guidance, see [Security best practices for Amazon GameLift Servers](security-best-practices.md "security-best-practices.md").

- **Fleet type** – The availability of the instances used to
  host your games, which can potentially impact hosting costs. A fleet can use
  **On-Demand** (always available) or **Spot**
  (availability varies) instances.
- **Active instances** – The number of EC2 instances in use
  for the fleet.
- **Desired instances** – The number of EC2 instances to
  keep active.
- **Game sessions** – The number of active game sessions
  running in the fleet. The data is delayed by five minutes.
- **Player sessons** – The number of active player sessions
  in the fleet. The data is delayed by five minutes.
