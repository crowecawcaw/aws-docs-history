# Add execution blocks

You add steps to workflows in your Region switch plan, to perform the individual steps to complete
failover or switchover for your application. For details about the functionality and behavior of each type of
execution block, see the following descriptions.

Region switch runs a plan evaluation immediately after you create a plan or update it, and then every 30
minutes during steady state. Region switch stores information about plan evaluation in all the
Regions where your plan is configured. Each execution block section here includes information
about what is evaluated when Region switch runs plan evaluation.

Region switch includes execution block types that help scale compute resources as part of recovery. If you
use these execution blocks in a plan, be aware that Region switch does not guarantee that the desired compute
capacity with be attained.
If you have a critical application and need to guarantee access to capacity, we recommend that you reserve the capacity.
There are strategies that you can follow to reserve compute capacity in a secondary Region while also
limiting cost. To learn more, see [Pilot light with reserved capacity: How to optimize DR cost using On-Demand Capacity Reservations](https://aws.amazon.com/blogs/architecture/pilot-light-with-reserved-capacity-how-to-optimize-dr-cost-using-on-demand-capacity-reservations/ "https://aws.amazon.com/blogs/architecture/pilot-light-with-reserved-capacity-how-to-optimize-dr-cost-using-on-demand-capacity-reservations/").

Region switch supports the following execution blocks.

| Execution block                                                                                                             | Function                                                                                                                            | Ungraceful configuration                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [ARC Region switch plan execution block](region-switch-plan-block.md "region-switch-plan-block.md")                         | Orchestrate recovery for multiple applications in one execution by specifying child plans to execute.                               | Start child plans with their ungraceful configurations.                                                         |
| [Amazon EC2 Auto Scaling group execution block](ec2-auto-scaling-block.md "ec2-auto-scaling-block.md")                      | Scale EC2 compute resources that are in an Auto Scaling group as part of your plan execution.                                       | Specify the minimum percentage of compute capacity that should be matched in the Region that you're activating. |
| [Amazon EKS resource scaling execution block](eks-resource-scaling-block.md "eks-resource-scaling-block.md")                | Scale Amazon EKS cluster pods as part of your plan execution.                                                                       | N/A                                                                                                             |
| [Amazon ECS service scaling execution block](ecs-service-scaling-block.md "ecs-service-scaling-block.md")                   | Scale Amazon ECS service tasks as part of your plan execution.                                                                      | N/A                                                                                                             |
| [ARC routing control execution block](arc-routing-controls-block.md "arc-routing-controls-block.md")                        | Add a step to change the state of one or more ARC routing controls, to redirect your application traffic<br>to a target AWS Region. | N/A                                                                                                             |
| [Amazon Aurora Global Database execution block](aurora-global-database-block.md "aurora-global-database-block.md")          | Perform a recovery workflow for an Aurora global database.                                                                          | Perform an Aurora global databases failover (can potentially cause data loss).                                  |
| [Amazon DocumentDB Global Cluster execution block](documentdb-global-cluster-block.md "documentdb-global-cluster-block.md") | Perform a recovery workflow for a Amazon DocumentDB global cluster.                                                                 | Perform a Amazon DocumentDB global cluster failover (can potentially cause data loss).                          |
| [Manual approval execution block](manual-approval-block.md "manual-approval-block.md")                                      | Insert an approval step, to require approval or cancellation of an execution before proceeding.                                     | N/A                                                                                                             |
| [Custom action Lambda execution block](custom-action-lambda-block.md "custom-action-lambda-block.md")                       | Add a custom step for running a Lambda function, to enable custom actions.                                                          | Skip the step.                                                                                                  |
| [Amazon Route 53 health check execution block](route53-health-check-block.md "route53-health-check-block.md")               | Specifies the Regions that your application traffic will be redirected to during failover.                                          | N/A                                                                                                             |
