# Generate Amazon GameLift Servers pricing estimates

With AWS Pricing Calculator, you can [create a
pricing estimate for Amazon GameLift Servers](https://calculator.aws/#/createCalculator/GameLiftServers "https://calculator.aws/#/createCalculator/GameLiftServers"). You don't need an AWS account or in-depth knowledge of
AWS to use the calculator.

AWS Pricing Calculator calculator guides you through the decisions that affect service costs to give you an
idea of how much Amazon GameLift Servers might cost for your game project. If you're not yet sure how you plan to
use Amazon GameLift Servers, then use the default values to generate an estimate. When planning for production
usage, the calculator can help you test out potential scenarios and generate more accurate
estimates.

## Estimate Amazon GameLift Servers managed hosting

This option provides a cost estimate for hosting your games on Amazon GameLift Servers managed servers,
including the costs for server instance usage and data transfer. With Amazon GameLift Servers managed hosting,
there is no additional cost for FlexMatch matchmaking.

If you are hosting or plan to host game servers in more than one AWS Region or on more
than one instance type, create an estimate for each Region and instance type.

### Amazon GameLift Servers instances

This section helps you estimate the type and number of compute resources that you need to
host game sessions for your players. Amazon GameLift Servers uses [Amazon Elastic Compute Cloud (Amazon EC2) instances](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") to manage
game servers. In Amazon GameLift Servers, you deploy a fleet of instances with a specific instance type and
operating system. If you have or plan to have multiple fleets, create an estimate for each
fleet.

To get started, open the [Configure Amazon GameLift Servers page](https://calculator.aws/#/createCalculator/GameLift "https://calculator.aws/#/createCalculator/GameLift") of AWS Pricing Calculator. Add a **Description**, choose a
**Region**, and then choose **Estimate Amazon GameLift Servers hosting (Instance + Data
Transfer Out)**. Under **Amazon GameLift Servers instances**, complete the following
fields:

- **Peak concurrent players (peak CCU)**

This is the maximum number of players who can connect to your game servers at the same
time. This field indicates how much hosting capacity Amazon GameLift Servers needs to meet peak player demand.
Enter the daily peak number of players that you expect to host using instances in your chosen
AWS Region.

For example, if you want to let 1,000 players connect to your game at any one time, keep
the default value of `1000`.

- **Average CCU per hour as a percentage of peak daily CCU**

This is the average number of concurrent players per hour over a 24-hour period. We use
this value to estimate the amount of sustained hosting capacity that Amazon GameLift Servers needs to maintain
for your players. If you're not sure what percentage value to use, keep the default value of
`50` percent. For games with stable player demand, we recommend entering
a value of `70` percent.

For example, if your game has an average hourly CCU of 6,000 and a peak CCU of 10,000,
then enter the value of `60` percent.

- **Game sessions per instance**

This is the number of game sessions that each of your game server instances can host
concurrently. Factors that can affect this number include the resource requirements of your
game server, the number of players to host in each game session, and player performance
expectations. If you know the number of concurrent game sessions for your game, then enter
that value. Alternatively, keep the default value of `20`.

- **Players per game session**

This is the average number of players who connect to a game session, as defined in your
game design. If you have game modes with different number of players, estimate an average
number of players per game session across your entire game. The default value is
`8`.

- **Instance idle buffer %**

This is the percentage of unused hosting capacity to maintain in reserve to handle sudden
spikes in player demand. Buffer size is a percentage of the total number of instances in a
fleet. The default value is `10` percent.

For example, with a 20 percent idle buffer, a fleet supporting players with 100 active
instances maintains 20 idle instances.

- **Spot instance %**

Amazon GameLift Servers fleets can use a combination of On-Demand Instances and Spot Instances. While
On-Demand Instances offer more reliable availability, Spot Instances offer a highly
cost-efficient alternative. We recommend using a combination to optimize both cost savings and
availability. For information about how Amazon GameLift Servers uses Spot Instances, see [On-Demand Instances versus Spot
Instances](gamelift-compute.md#gamelift-compute-spot "gamelift-compute.md#gamelift-compute-spot").

For this field, enter the percentage of Spot Instances to maintain in a fleet. We
recommend a Spot Instance percentage between 50 and 85 percent. The default value is
`50` percent.

For example, if you deploy a fleet with 100 instances and specify
`40` percent, Amazon GameLift Servers works to maintain 60 On-Demand Instances and 40 Spot
Instances.

- **Instance type**

Amazon GameLift Servers fleets can use a range of Amazon EC2 instance types that vary in computing power,
memory, storage, and networking capabilities. When you configure a Amazon GameLift Servers fleet, choose an
instance type that best fits your game's needs. For information about selecting an instance
type with Amazon GameLift Servers, see [Choose compute resources for a managed fleet](gamelift-compute.md "gamelift-compute.md").

If you know the instance type that you're using or plan to use in your Amazon GameLift Servers fleet,
choose that type. If you're not sure what type to choose, consider choosing
**c5.large**. This is a high-availability type with average size and
capabilities.

- **Operating system**

This field specifies the operating system that your game servers run on—either
Linux or Windows. The default value is **Linux**.

### Data transfer out (DTO)

This section helps you estimate the cost for traffic between your game clients and the game
servers. Data transfer fees apply to outbound traffic only. Inbound data transfer has no
cost.

On the [Configure Amazon GameLift Servers
page](https://calculator.aws/#/createCalculator/GameLift "https://calculator.aws/#/createCalculator/GameLift") of AWS Pricing Calculator, expand **Data transfer out (DTO)**, and then complete
the following fields:

- **DTO estimate type**

You can choose to estimate DTO in either of the following two ways, depending on how you
track data transfer for your game.

    + **Per month (in GB)** – If you track monthly traffic for your
     game servers, choose this type.
    + **Per player** – If you track data transfer by player, choose
     this type. This is the default type.


    In the following field, you estimate per-player DTO based on the number of player hours
     that you calculated in the previous section.

- **DTO per month (in GB)**

If you chose the **Per month (in GB)** DTO estimate type, then enter
your estimated monthly DTO usage in GB from each instance, per Region.

- **DTO per player**

If you chose the **Per player** DTO estimate type, then enter your
game's estimated DTO usage per player in KB/sec. The default value is
`4`.

When you're done configuring your Amazon GameLift Servers pricing estimate, choose **Add to my
estimate**. For more information about creating and managing estimates in AWS Pricing Calculator, see
[Create an estimate, configure a service, and add more services](../../../pricing-calculator/latest/userguide/create-estimate.md "../../../pricing-calculator/latest/userguide/create-estimate.md") in the _AWS Pricing Calculator
User Guide_.
