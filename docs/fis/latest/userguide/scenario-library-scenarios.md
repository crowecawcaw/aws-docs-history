# Scenarios reference

Scenarios included in the scenario library are designed to use [tags](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md") where possible and each scenario describes the required tags in the **Prerequisites** and **How it works** sections of the scenario description. You can tag your resources with those pre-defined tags or you can set your own tags using the shared parameter editing experience (see [Using a scenario](scenario-library.md#using-a-scenario "scenario-library.md#using-a-scenario")).

This reference describes the common scenarios in the AWS FIS scenario library. You can also list the supported scenarios using the AWS FIS console.

For more information, see [Working with the AWS FIS scenario library](scenario-library.md "scenario-library.md").

AWS FIS supports the following Amazon EC2 scenarios. These scenarios target instances using [tags](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md"). You can use your own tags or use the default tags included in the scenario. Some of these scenarios [use SSM documents](actions-ssm-agent.md "actions-ssm-agent.md").

- **EC2 stress: instance failure** - Explore the effect of instance failure by stopping one or more EC2 instances.

Target instances in the current region that have a specific tag attached. In this scenario we will stop those instances and restart them at the end of the action duration, by default 5 min.

- **EC2 stress: Disk** - Explore impact of increased disk utilization on your EC2 based application.

In this scenario we will target EC2 instances in the current region that have a specific tag attached. In this scenario you can customize an increasing amount disk utilization injected on targeted EC2 instances for the action duration, by default 5 min for each disk stress action.

- **EC2 stress: CPU** - Explore impact of increased CPU on your EC2 based application.

In this scenario we will target EC2 instances in the current region that have a specific tag attached. In this scenario you can customize an increasing amount of CPU stress injected on targeted EC2 instances for the action duration, by default 5 min for each CPU stress action.

- **EC2 stress: Memory** - Explore impact of increased memory utilization on your EC2 based application.

In this scenario we will target EC2 instances in the current region that have a specific tag attached. In this scenario you can customize an increasing amount of memory stress injected on targeted EC2 instances for the action duration, by default 5 min for each memory stress action.

- **EC2 stress: Network Latency** - Explore impact of increased network latency on your EC2 based application.

In this scenario we will target EC2 instances in the current region that have a specific tag attached. In this scenario you can customize an increasing amount of network latency injected on targeted EC2 instances for the action duration, by default 5 min for each latency action.
AWS FIS supports the following Amazon EKS scenarios. These scenarios target EKS pods using a Kubernetes application labels. You can use your own labels or use the default labels included in the scenario. For more information about EKS with FIS, see [EKS Pod actions](eks-pod-actions.md "eks-pod-actions.md").

- **EKS stress: Pod Delete** - Explore the effect of EKS pod failure by deleting one or more pods.

In this scenario we will target pods in the current region that are associated with an application label. In this scenario we will terminate all matched pods. Re-creation of pods will be controlled by kubernetes configuration.

- **EKS stress: CPU** - Explore impact of increased CPU on your EKS based application.

In this scenario we will target pods in the current region that are associated with an application label. In this scenario you can customize an increasing amount of CPU stress injected on targeted EKS pods for the action duration, by default 5 min for each CPU stress action.

- **EKS stress: Disk** - Explore impact of increased disk utilization on your EKS based application.

In this scenario we will target pods in the current region that are associated with an application label. In this scenario you can customize an increasing amount of disk stress injected on targeted EKS pods for the action duration, by default 5 min for each CPU stress action.

- **EKS stress: Memory** - Explore impact of increased memory utilization on your EKS based application.

In this scenario we will target pods in the current region that are associated with an application label. In this scenario you can customize an increasing amount of memory stress injected on targeted EKS pods for the action duration, by default 5 min for each memory stress action.

- **EKS stress: Network latency** - Explore impact of increased network latency on your EKS based application.

In this scenario we will target pods in the current region that are associated with an application label. In this scenario you can customize an increasing amount of network latency injected on targeted EKS pods for the action duration, by default 5 min for each latency action.
AWS FIS supports the following scenarios for single-AZ, multi-AZ and multi-Region applications. These scenarios target multiple resource types.

- **AZ Availability: Power Interruption** - Inject the expected symptoms of a complete interruption of power in an Availability Zone (AZ). Learn more about [AZ Availability: Power Interruption](az-availability-scenario.md "az-availability-scenario.md").
- **AZ: Application Slowdown** - Add latency between resources within a single Availability Zone (AZ) to slow down an application. Learn more about [AZ: Application Slowdown](az-application-slowdown-scenario.md "az-application-slowdown-scenario.md").
- **Cross-AZ: Traffic Slowdown** - Inject packet loss to disrupt and slow down traffic between Availability Zones (AZs). Learn more about [Cross-AZ: Traffic Slowdown](cross-az-traffic-slowdown-scenario.md "cross-az-traffic-slowdown-scenario.md").
- **Cross-Region: Connectivity** - Block application network traffic from the experiment Region to the destination Region and pause cross-Region data replication. Learn more about using [Cross-Region: Connectivity](cross-region-scenario.md "cross-region-scenario.md").
  AWS FIS supports the following scenarios for Amazon EBS volumes. These scenarios target volumes using
  tags. You can use your own tags or use the default tags included in the scenario. The target
  volumes must be in the same Availability Zone. For more information, [Fault testing on Amazon EBS](../../../ebs/latest/userguide/ebs-fis.md "../../../ebs/latest/userguide/ebs-fis.md").

- **EBS: Sustained Latency** — Explore impact of
  persistent I/O latency on your application.

In this scenario, we will target volumes in the current Availability Zone that have a
specific tag attached. This scenario injects constant latency of 500 ms on 50 percent of
read and 100 percent of write operations for a volume, using a single latency action over
a 15-minute period. In this scenario, you can customize the amount of latency injected,
the percentage of I/O injected, and the duration for the action.

- **EBS: Increasing Latency** — Explore impact of
  increasing I/O latency on your application.

In this scenario, we will target volumes in the current Availability Zone that have a
specific tag attached. This scenario injects increasing latency of 50 ms, 200 ms, 700 ms,
1 second, and 15 seconds on 10 percent of read and 25 percent of write operations for a
volume using five latency actions over a 15-minute period. In this scenario, you can
customize the amount of latency injected, the percentage of I/O injected, and the action
duration, for each latency action.

- **EBS: Intermittent Latency** — Explore impact
  of intermittent I/O latency spikes on your application.

In this scenario, we will target volumes in the current Availability Zone that have a
specific tag attached. This scenario injects three sharp intermittent latency spikes of
30 seconds, 10 seconds, and 20 seconds on 0.1 percent of the read and write I/O operations
for a volume, using three latency actions, with intervals of recovery in between each
spike over a 15-minute period. In this scenario, you can customize the amount of latency
injected, the percentage of I/O injected, and the action duration, for each latency action.

- **EBS: Decreasing Latency** — Explore impact of
  decreasing I/O latency on your application.

In this scenario, we will target volumes in the current Availability Zone that have a
specific tag attached. This scenario injects decreasing latency of 20 seconds, 5 seconds,
900 ms, 300 ms, and 40 ms on 10 percent of read and write operations for a volume, using
five latency actions over a 15-minute period. In this scenario, you can customize the
amount of latency injected, the percentage of I/O injected, and the action duration, for
each latency action.
