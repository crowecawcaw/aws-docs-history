# Setting up CPU and memory

monitoring

After you enable Runtime Monitoring and assess that the coverage status of your cluster is **Healthy**, you can set up and view the insight metrics.

The following topics can help you evaluate how the deployed agent performs against the CPU
and memory limits for the GuardDuty agent.

The following steps from the _Amazon CloudWatch User Guide_ can help you evaluate how
the deployed agent performs against the CPU and memory limits for the GuardDuty agent:

1. [Setting
   up Container Insights on Amazon ECS for cluster- and service-level metrics](../../../AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.md "../../../AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.md")
2. [Amazon ECS Container
   Insights metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.md")
   After the GuardDuty security agent gets deployed and you assess that the coverage status of your
   cluster is **Healthy**, you can set up and view the Container insight
   metrics.

**Evaluate performance of the security agent**

1. [Setting up
   Container Insights on Amazon EKS and Kubernetes](../../../AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.md "../../../AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.md") in the
   _Amazon CloudWatch User Guide_
2. [Amazon EKS and Kubernetes
   Container Insights metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.md") in the _Amazon CloudWatch User Guide_

**Manage performance with security agent v1.5.0 and
above**

With security agent [v1.5.0 and above](runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history "runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history"), when the insights indicate that the associated GuardDuty agent is
reaching the assigned limits, you can configure specific parameters. For more information, see
[Configure EKS add-on
parameters](guardduty-configure-security-agent-eks-addon.md "guardduty-configure-security-agent-eks-addon.md").
