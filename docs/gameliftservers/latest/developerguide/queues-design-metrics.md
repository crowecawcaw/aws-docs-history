# Evaluate queue metrics

Use metrics to evaluate how well your queues are performing. You can view metrics
related to queues in the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift "https://console.aws.amazon.com/gamelift") or
in Amazon CloudWatch. For a list and descriptions of queue metrics, see [Amazon GameLift Servers metrics for queues](monitoring-cloudwatch.md#gamelift-metrics-queue "monitoring-cloudwatch.md#gamelift-metrics-queue").

Queue metrics can provide insight about the following:

- **Overall queue performance** – Queue
  metrics indicate how successfully a queue responds to placement requests. These
  metrics can also help you identify when and why placements fail. For queues with
  manually scaled fleets, the `AverageWaitTime` and
  `QueueDepth` metrics can indicate when you should adjust capacity
  for a queue.
- **FleetIQ algorithm performance** – For
  placement requests using the FleetIQ algorithm, metrics show how often the
  algorithm finds ideal game session placement. The placement may prioritize using
  resources with the lowest player latency or resources with the lowest cost.
  There are also error metrics that identify common reasons why Amazon GameLift Servers can't find
  an ideal placement. For more information about metrics, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **Location specific placements** – For
  multi-location queues, metrics show successful placements by location. For
  queues that use the FleetIQ algorithm, this data provides useful insight into
  where player activity occurs.
  When evaluating metrics for FleetIQ algorithm performance, consider the following
  tips:

- To track the queue's rate of finding an ideal placement, use the
  `PlacementsSucceeded` metric in combination with the FleetIQ
  metrics for lowest latency and lowest price.
- To boost a queue's rate of finding an ideal placement, review the following
  error metrics:
  - If the `FirstChoiceOutOfCapacity` is high, adjust capacity
    scaling for the queue's fleets.
  - If the `FirstChoiceNotViable` error metric is high, look at
    your Spot Instance fleets. Spot Instance fleets are considered not
    viable when the interruption rate for a particular instance type is too
    high. To resolve this issue, change the queue to use Spot Instance
    fleets with different instance types. We recommend that you include Spot
    Instance fleets with different instance types in each location.
