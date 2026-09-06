

# Cost optimization strategies
<a name="gamelift-pricing-cost-optimization"></a>

Use these strategies with a managed hosting solution to help reduce your cloud hosting costs while maintaining high performance and player experience.

## Best practices
<a name="gamelift-pricing-cost-optimization-bestpractices"></a>

Follow these tips to incorporate cost optimization practices for your game hosting. At a minimum, we recommend that you schedule regular reviews of your Amazon GameLift Servers costs and usage patterns. If you have pricing-related questions, reach out to your account manager.

**Fleet configuration**
+ **Use the pricing calculator** – Use this tool with your game hosting data to explore options and test out potential configuration scenarios for cost savings. See [AWS Pricing Calculator for Amazon GameLift Servers](https://calculator.aws/#/createCalculator/GameLiftServers).
+ **Save in development** – For development and testing, use smaller, less expensive instance types and run them only when you need to. 
+ **Match instance type to game** – Choose Amazon EC2 instance families, types, and sizes for your fleets that best suit your game's requirements. See the Instance types section in [Choose compute resources for a managed fleet](gamelift-compute.md#gamelift-compute-instance).
+ **Use Graviton instance types** – Graviton instances are powered by ARM-based processors. They offer better price-performance, higher energy efficiency, and lower costs than comparable x86-based instances with the On-Demand pricing model. 
+ **Use Spot instances** – Spot instances are usually lower cost than On-Demand but may not always be available. Combine Spot and On-Demand fleets to balance low cost and high availability (50-85% Spot usage recommended). Use Spot instances for non-critical game modes or during off-peak hours. To monitor Spot instance viability, track metrics such as `InstanceInterruptions` and `GameServerInterruptions`. See [On-Demand Instances versus Spot Instances](gamelift-compute.md#gamelift-compute-spot).
+ **Run servers on Linux** – Build your game server runtime for Linux. Instances that are deployed with Linux are generally more cost-efficient than those with Windows.
+ **Optimize resource utilization** – Configure fleets for maximum efficiency by running as many concurrent game server processes as possible while maintaining performance. See [Optimize game server runtime configuration on managed Amazon GameLift Servers](fleets-multiprocess.md).
+ **Create a multi-region strategy** – Deploying game hosting to multiple locations can give your players lower latency and better backup options. Balance regional coverage and cost efficiency by deploying hosting in your largest player markets first and using secondary locations for overflow capacity during peak times. See [Build a multi-location queue](queues-design-multiregion.md).

**Fleet capacity scaling**
+ **Scale to zero** – When fleets are not in use, manually set fleet capacity to zero to avoid unnecessary charges. See [Manually set capacity for an Amazon GameLift Servers fleet](fleets-updating-capacity.md).
+ **Add auto scaling** – Avoid over-provisioning hosting resources by using auto scaling to adjust game hosting capacity. Match capacity to fluctuating player demand and other key metrics. See [Auto-scale fleet capacity with Amazon GameLift Servers](fleets-autoscaling.md).
+ **Maintain a buffer** – To handle sudden spikes in player demand without making players wait, use target tracking to maintain a buffer of idle game servers. Customize the buffer based on the size and usage patterns of your player base. See [Target-based auto scaling](fleets-autoscaling-target.md).

**Game session placement**
+ **Use placement queues** – Amazon GameLift Servers queues rely on an algorithm to determine the "best possible" hosting locations for game sessions, based on the cost of hosting resources and other factors. See [Configure game session placement](queues-intro.md).
+ **Customize queue priorities** – You can change how a queue prioritizes hosting costs when placing game sessions. See [Prioritize game session placement](queues-design-priority.md).
+ **Monitor placement metrics** – Track how queues are choosing locations for game sessions to identify optimization opportunities. See [Amazon GameLift Servers metrics for queues](monitoring-cloudwatch.md#gamelift-metrics-queue).

**Data transfer**
+ **Track data transfers** – Monitor how data is transferred between your game clients and servers and take steps to optimize activity.
+ **Use data compression** – Consider implementing data compression techniques for data transfers between game clients and servers. Compression plays a crucial role in reducing bandwidth usage as well as improving gameplay performance and latency.

## Resource cost and utilization tools
<a name="gamelift-pricing-cost-optimization-tools"></a>

Explore how to use AWS tools to monitor and optimize your game hosting costs with Amazon GameLift Servers. For information on additional tools, see [AWS Billing and Cost Management](https://docs.aws.amazon.com/account-billing/).

**AWS cost management tools**
+ **Billing console** – Review your AWS bills and usage. See [Getting set up with Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html).
+ **Free Tier usage alerts** – Set up notifications when approaching Free Tier limits. See [Tracking your AWS Free Tier usage](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html).
+ **Amazon CloudWatch billing alerts** – Configure alerts when usage hits custom thresholds. See [Create a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html).

**Cost allocation and tracking**
+ **Cost allocation tags** – Tag your fleets and other resources to organize and track hosting costs. See [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).
+ **Cost reports** – Create reports categorized by assigned tags. See [Using the monthly cost allocation report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html).
+ **AWS Cost Explorer** – Analyze costs, trends, and forecasts with filtering and customizable views. See [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).
+ **AWS Budgets** – Track and take action on your AWS costs and usage. See [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

## Performance monitoring with Amazon GameLift Servers and Amazon CloudWatch
<a name="gamelift-pricing-cost-optimization-metrics"></a>

Monitor these key metrics to optimize resource utilization. View metrics in the Amazon GameLift Servers console or use Amazon CloudWatch dashboards. For details on all available metrics for Amazon GameLift Servers , see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md).
+ **Instance metrics** – `ActiveInstances`, `IdleInstances`, `PercentIdleInstances`
+ **Server process metrics** – `ActiveServerProcesses`, `HealthyServerProcesses`
+ **Game session metrics** – `ActiveGameSessions`, `AvailableGameSessions`
+ **Player session metrics** – `CurrentPlayerSessions`
+ **Queue metrics** – `AverageWaitTime`, `QueueDepth`
+ **Matchmaking metrics** – `CurrentTickets`, `MatchesPlaced`
+ **Hardware performance** – `CPUUtilization`, `NetworkIn`/`NetworkOut`, `DiskReadBytes`/`DiskWriteBytes`
+ **Resource utilization metrics**
  + Use `PercentIdleInstances` to determine optimal fleet size.
  + Track `PercentAvailableGameSessions` to ensure sufficient game hosting capacity.
  + Monitor `InstanceInterruptions` and `GameServerInterruptions` to determine Spot Instance viability.