# Observability

## Standard Kubernetes Monitoring

You can monitor Spaces using standard Kubernetes tools like `kubectl` describe and `kubectl` logs.

**Monitoring Space Status**

```
# List all Spaces with status
kubectl get workspace -A

# Get detailed information about a specific Space
kubectl describe workspace <workspace-name>
```

**Viewing Space Logs**

```
# View workspace container logs
kubectl logs -l workspace.jupyter.org/workspace-name=<workspace-name> -c workspace

# View SSM agent sidecar logs (for remote IDE connectivity)
kubectl logs -l workspace.jupyter.org/workspace-name=<workspace-name> -c ssm-agent-sidecar

# Follow logs in real-time
kubectl logs -l workspace.jupyter.org/workspace-name=<workspace-name> -c workspace -f
```

**Understanding Space Conditions**

Spaces report four condition types in their status:

- **Available**:
  `True` when the Space is ready for use. All required resources (pods, services,
  storage) are running and healthy.
- **Progressing**:
  `True` when the Space is being created, updated, or reconciled. Transitions to `False` once stable.
- **Degraded**:
  `True` when errors are detected with the Space resources. Check the condition message for details.
- **Stopped**:
  `True` when the Space desired status is set to `Stopped`. The pods are terminated but storage and configuration are preserved.

## CloudWatch Logs Integration

You can install the CloudWatch logging add-on to send Space logs to Amazon
CloudWatch Logs for centralized log management and retention. This enables log
aggregation across multiple clusters and integration with CloudWatch Insights for
querying and analysis. All of the above available `kubectl` logs are queryable in CloudWatch with this plugin.

**Reference:** [https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci.html](sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci.md "sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci.md").

## HyperPod Observability Add-on

The SageMaker HyperPod observability add-on provides comprehensive dashboards for
monitoring Space resource utilization. After installing the add-on, you can view
Space memory and CPU usage in the **Tasks** tab of the
HyperPod console, which displays metrics in Amazon Managed Grafana
dashboards.

**Reference:** [https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-observability-addon.html](sagemaker-hyperpod-observability-addon.md "sagemaker-hyperpod-observability-addon.md")

**Key metrics available:**

- CPU and memory utilization per Space
- GPU metrics (if applicable)
