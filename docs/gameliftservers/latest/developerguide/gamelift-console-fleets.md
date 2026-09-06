

# Fleets in the Amazon GameLift Servers console
<a name="gamelift-console-fleets"></a>

The fleet resource represents a set of compute machines that are deployed with and run your game servers. Depending on your hosting solution, you might have managed EC2 fleets, managed container fleets, Anywhere fleets, or a combination.

View information about fleets in the Amazon GameLift Servers console or using the AWS SDK for Amazon GameLift Servers.

------
#### [ Console ]

You can view information on all the fleets created to host your games on Amazon GameLift Servers under your AWS account. In the console's left-side navigation, find the hosting option you want (Anywhere, Managed EC2, Managed containers), and choose **Fleets**. 

For each hosting option, the **Fleets** page lists fleets that are located in your currently selected AWS Region. From the **Fleets** page, you can create a new fleet or view additional detail on a fleet. A fleet's [detail page](gamelift-console-fleets-metrics.md) contains usage information, metrics, game session data, and player session data. You can also edit a fleet record or delete a fleet.

A **Fleets** page displays the following summary information by default. You can adjust the table content as needed using the **Preferences** tool (see the ![Gear icon representing settings or configuration options.](http://docs.aws.amazon.com/gameliftservers/latest/developerguide/images/settings.png) icon in the upper right corner of the table). Custom preferences are saved to your AWS account user and are automatically applied whenever you view this page.
+ **ID** – An identifier assigned to the fleet. This ID is unique within the AWS Region where the fleet is created.
+ **Name** – A friendly name given to the fleet.
+ **Status** – The status of the fleet: **New**, **Downloading**, **Building**, and **Active**.
+ **Creation time** – The date and time the fleet was created.
**Note**  
A fleet displays a warning icon for fleets that were created more than 90 days ago. As a best practice, we recommend replacing fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see [Security best practices for Amazon GameLift Servers](security-best-practices.md).
+ **Fleet type** – The availability of the instances used to host your games, which can potentially impact hosting costs. A managed fleet can use **On-Demand** (always available) or **Spot** (availability varies) instances.
+ **Active instances** – The number of EC2 instances in use for the fleet.
+ **Desired instances** – The number of EC2 instances to keep active.
+ **Game sessions** – The number of active game sessions running in the fleet. The data is delayed by five minutes.
+ **Player sessions** – The number of active player sessions in the fleet. The data is delayed by five minutes.

------
#### [ AWS SDK ]

Use the following AWS CLI commands to retrieve information about this resource:
+ Managed EC2 fleets
  + [ListFleets](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListFeets.html)
  + [ListCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListCompute.html)
  + [DescribeFleetAttributes](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetAttributes.html)
  + [DescribeCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeCompute.html)
  + [DescribeFleetCapacity](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetCapacity.html)
  + [DescribeFleetUtilization](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetUtilization.html)
+ Managed container fleets
  + [ListContainerFleets](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListContainerFleets.html)
  + [DescribeContainerFleet](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeContainerFleet.html)
  + [ListContainerGroupDefinitions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListContainerGroupDefinition.html)
  + [DescribeContainerGroupDefinition](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeContainerGroupDefinition.html)
+ 
  + [ListFleets](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListFeets.html)
  + [ListCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListCompute.html)
  + [DescribeFleetAttributes](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetAttributes.html)
  + [DescribeCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeCompute.html)

------