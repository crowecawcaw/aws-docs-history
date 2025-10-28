# Health

monitoring agent

This section describes the set of health checks that SageMaker HyperPod uses to regularly
monitor cluster instance health for issues with devices such as accelerators (GPU and
Trainium cores) and networking (EFA). SageMaker HyperPod health-monitoring agent (HMA)
continuously monitors the health status of each GPU-based or Trainium-based instance.
When it detects any instance or GPU failures, the agent marks the instance as
unhealthy.

SageMaker HyperPod HMA performs the same health checks for both EKS and Slurm orchestrators.
For more information about HMA, see [SageMaker HyperPod
health-monitoring agent](sagemaker-hyperpod-eks-resiliency-health-monitoring-agent.md "sagemaker-hyperpod-eks-resiliency-health-monitoring-agent.md").
