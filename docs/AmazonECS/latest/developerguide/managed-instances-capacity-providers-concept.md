# Amazon ECS Managed Instances capacity providers

Amazon ECS Managed Instances capacity providers provide a container compute model that gives you access to the full range of AWS capabilities and Amazon EC2 offerings while AWS manages operational and security responsibilities. AWS handles software and OS patching, instance scaling, and maintenance, giving you the operational benefits of Fargate while maintaining access to all AWS capabilities and integrations.

Amazon ECS creates launch templates for your Amazon ECS Managed Instances. This defines how Amazon ECS launches Amazon ECS Managed Instances, including the instance profile for your tasks, network and storage configuration, capacity options, and instance requirements for flexible instance type selection.

## When to use custom capacity

providers

Consider custom capacity providers when your workloads require:

- Specific compute requirements: Applications requiring accelerated compute, specific CPU instruction sets, high network performance, or large memory configurations that aren't available with standard Fargate options.
- GPU workloads: Machine learning inference, real-time image rendering, video encoding, or other GPU-accelerated applications that need access to NVIDIA or AMD GPUs.
- Capacity reservations: Mission-critical workloads that require predictable capacity availability.
- Advanced observability: Security and monitoring tools that require privileged access to the underlying OS, such as eBPF-based monitoring solutions or network analysis tools.
- Cost optimization: Workloads that can benefit from multi-task placement, shared infrastructure components, or need to maximize utilization of larger instance types.

## Monitoring options

Amazon ECS Managed Instances provide comprehensive monitoring capabilities to help you track performance, health, and resource utilization of your containerized workloads. You can choose from different monitoring levels based on your operational requirements.

- **Basic monitoring** – Provides essential metrics at 5-minute intervals for most metrics and 1-minute intervals for status checks. This is enabled by default and incurs no additional charges.
- **Detailed monitoring** – Offers enhanced visibility with all metrics available at 1-minute intervals, enabling faster detection and response to operational issues. For more information, see [Detailed monitoring for Amazon ECS Managed Instances](monitoring-managed-instances.md#detailed-monitoring-managed-instances "monitoring-managed-instances.md#detailed-monitoring-managed-instances").

Both monitoring options integrate seamlessly with CloudWatch to provide dashboards, alarms, and automated responses to help maintain optimal application performance and availability.

## Capacity provider considerations

A cluster can contain a mix of Amazon ECS Managed Instances capacity providers, Auto Scaling group capacity providers, and Fargate
capacity providers. A capacity provider strategy can only contain Amazon ECS Managed Instances capacity providers, Auto Scaling group capacity
providers, or Fargate capacity providers.

## Tag propagation

Capacity providers for Amazon ECS Managed Instances support tag propagation. With tag propagation, all resources managed by the capacity provider — the managed instance, the Amazon ECS container
instance, launch template, volumes, Elastic Network Interfaces — are tagged with
the same tags specified at the capacity provider level. You can specify tags during capacity provider creation and enable tag propagation by specifying the `propagateTags` parameter as `CAPACITY_PROVIDER`.

For more information about tagging Amazon ECS Managed Instances, see [Tags for
Amazon ECS Managed Instances](instance-details-tags-managed-instances.md "instance-details-tags-managed-instances.md").
