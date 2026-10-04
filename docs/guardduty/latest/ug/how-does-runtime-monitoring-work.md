

# How it works
<a name="how-does-runtime-monitoring-work"></a>

Runtime Monitoring uses a lightweight security agent to observe the runtime behavior of your Amazon EC2, Amazon EKS, and Amazon ECS on Fargate workloads and detect threats. It works end to end as follows:

1. **The agent is deployed to your resources.** GuardDuty can deploy and update the agent for you (automated agent configuration), or you can deploy and manage it yourself (manual agent configuration). The steps depend on the resource type.

1. **The agent collects runtime events.** On each monitored resource, the agent observes operating system-level activity, such as process execution, file access, and network connections.

1. **The agent sends events to GuardDuty.** The agent delivers the events to the GuardDuty backend. The data remains within the AWS network, and GuardDuty doesn't charge for the events transmitted from your compute resources to GuardDuty. For details, see [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md).

1. **GuardDuty analyzes the events and generates findings.** When it detects suspicious behavior, such as privilege escalation or communication with a known malicious host, GuardDuty generates a finding. To see the up-to-date list of findings that GuardDuty generates, see [GuardDuty Runtime Monitoring finding types](findings-runtime-monitoring.md).

The agent runs within defined CPU and memory limits, so its resource consumption stays predictable and doesn't degrade the performance or availability of the workloads running on the same host. For these limits, see [Prerequisites to enabling Runtime Monitoring](runtime-monitoring-prerequisites.md).

**Topics**
+ [Enabling Runtime Monitoring](runtime-monitoring-enablement.md)
+ [Deploying the security agent to Amazon EKS](how-runtime-monitoring-works-eks.md)
+ [Deploying the security agent to Amazon EC2](how-runtime-monitoring-works-ec2.md)
+ [Deploying the security agent to Amazon ECS on Fargate](how-runtime-monitoring-works-ecs-fargate.md)
+ [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md)
+ [Tracking Runtime Monitoring coverage](runtime-monitoring-after-configuration.md)