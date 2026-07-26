# EC2 instances or ECS tasks not appearing as billable resources

When a parent resource (such as an Auto Scaling group, ECS service, or EKS deployment) manages an EC2
instance, ECS task, EKS pod, or network interface, Next generation Resilience Hub classifies that resource as
_ephemeral_. Ephemeral resources are transient. The parent resource
replaces them automatically through lifecycle events. Next generation Resilience Hub assesses them through
their parent, not independently.

The following resource types are ephemeral when managed by a parent:

| Resource type                | Example parent                       |
| ---------------------------- | ------------------------------------ |
| `AWS::EC2::Instance`         | Auto Scaling group or EKS node group |
| `AWS::ECS::Task`             | ECS service                          |
| `AWS::EKS::Pod`              | EKS deployment or replica set        |
| `AWS::EC2::NetworkInterface` | EC2 instance managed by Auto Scaling |

Standalone instances of these types (not managed by a parent) remain billable.
