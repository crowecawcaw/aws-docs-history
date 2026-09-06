

# Setting up CPU and memory monitoring
<a name="runtime-monitoring-setting-cpu-mem-monitoring"></a>

After you enable Runtime Monitoring and assess that the coverage status of your cluster is **Healthy**, you can set up and view the insight metrics. 

The following topics can help you evaluate how the deployed agent performs against the CPU and memory limits for the GuardDuty agent.

## Setting up monitoring on Amazon ECS cluster
<a name="ecs-runtime-cpu-memory-monitoring-agent"></a>

The following steps from the *Amazon CloudWatch User Guide* can help you evaluate how the deployed agent performs against the CPU and memory limits for the GuardDuty agent:

1. [Setting up Container Insights on Amazon ECS for cluster- and service-level metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.html)

1. [Amazon ECS Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html)

## Setting up monitoring on Amazon EKS cluster
<a name="eks-runtime-cpu-memory-monitoring-agent"></a>

After the GuardDuty security agent gets deployed and you assess that the coverage status of your cluster is **Healthy**, you can set up and view the Container Insights metrics.

**Evaluate performance of the security agent**  

1. [Setting up Container Insights on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.html) in the *Amazon CloudWatch User Guide*

1. [Amazon EKS and Kubernetes Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.html) in the *Amazon CloudWatch User Guide*

**Manage performance with security agent v1.5.0 and above**  
With security agent [v1.5.0 and above](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-agent-release-history.html#eks-runtime-monitoring-agent-release-history), when the insights indicate that the associated GuardDuty agent is reaching the assigned limits, you can configure specific parameters. For more information, see [Configure EKS add-on parameters](guardduty-configure-security-agent-eks-addon.md).