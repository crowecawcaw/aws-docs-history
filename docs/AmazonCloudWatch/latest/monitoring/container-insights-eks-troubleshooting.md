

# Troubleshooting Container Insights on Amazon EKS
<a name="container-insights-eks-troubleshooting"></a>

This section covers common issues that you might encounter when you set up or operate Container Insights on Amazon EKS. Use the following tables and diagnostic commands to identify and resolve problems regardless of whether you use the OTel or Classic approach.

For approach-specific setup guidance, see [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md) or [Setup guide (AWS CLI)](container-insights-eks-classic-setup.md). To compare approaches, see [Compare Container Insights approaches](container-insights-eks-compare.md).

## Metrics not appearing in CloudWatch
<a name="container-insights-eks-troubleshooting-metrics"></a>

If you don't see metrics in the `ContainerInsights` namespace, use the following table to identify the cause.


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| No metrics in the ContainerInsights namespace | IAM role lacks cloudwatch:PutMetricData permission | Attach the CloudWatchAgentServerPolicy managed policy to the agent IAM role. | 
| Metrics appear for some nodes but not others | Agent DaemonSet not scheduled on all nodes because of taints | Add tolerations to the agent DaemonSet to allow scheduling on tainted nodes. | 
| Metrics stop appearing | Agent pod is OOMKilled or restarting | Increase the memory limits in the agent pod resource specification. | 
| Metrics are stale or zero | Network connectivity is blocked | Check VPC security groups and verify that a CloudWatch VPC endpoint exists. | 
| Enhanced metrics are missing | Agent not configured for Enhanced Observability | Set enhancedObservability: true in the agent configuration. | 

## Agent pods not starting
<a name="container-insights-eks-troubleshooting-agent-pods"></a>

If agent pods fail to start or remain in a non-running state, use the following table to diagnose the issue.


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| ImagePullBackOff | Amazon ECR is unreachable or the image tag is incorrect | Verify the image URI and confirm that your nodes can access Amazon ECR. | 
| Pending | Insufficient CPU or memory on the node | Scale the node group or reduce resource requests in the agent pod specification. | 
| CrashLoopBackOff | Invalid configuration or missing volume mount | Check pod logs for configuration errors by running kubectl logs on the affected pod. | 
| FailedScheduling | Node affinity or taints prevent scheduling | Review the nodeSelector and tolerations in the DaemonSet spec. | 
| Exit code 1 | Service account lacks IRSA annotation | Verify that the service account has the eks.amazonaws.com/role-arn annotation. | 

## Add-on installation failures
<a name="container-insights-eks-troubleshooting-addon"></a>

If the `amazon-cloudwatch-observability` add-on fails to install or reports an unhealthy status, use the following table to troubleshoot.


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| CREATE\_FAILED | Conflicting resources from a previous installation | Delete conflicting resources and use --resolve-conflicts OVERWRITE when you create the add-on. | 
| OIDC provider not found | No IAM OIDC identity provider exists for the cluster | Create the provider by running eksctl utils associate-iam-oidc-provider. | 
| Version conflict | Add-on version is incompatible with the Kubernetes version | List compatible versions by running aws eks describe-addon-versions. | 
| DEGRADED status | Health checks are failing because of missing permissions | Check pod logs and verify that the IRSA role has the required policies attached. | 

## Log delivery issues
<a name="container-insights-eks-troubleshooting-logs"></a>

If container logs don't appear in Amazon CloudWatch Logs, use the following table to identify the cause.


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| Log group doesn't exist | Missing logs:CreateLogGroup permission | Add Amazon CloudWatch Logs permissions to the agent IAM role. | 
| Log group exists but is empty | Agent not configured for logs, or Region mismatch | Verify that the agent configuration includes log collection and that the Region matches your cluster Region. | 
| Logs are delayed more than 5 minutes | Flush interval is too high or the node is under heavy load | Reduce the force\_flush\_interval value in the agent configuration. | 
| Performance logs are missing | Agent is configured for application logs only | Verify that the Container Insights performance log section is present in the agent configuration. | 

## Migration-specific issues
<a name="container-insights-eks-troubleshooting-migration"></a>

If you experience issues while migrating between Container Insights approaches, use the following table. For the full migration workflow, see [Migration guides](container-insights-eks-migration-hub.md).


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| Duplicate metrics during parallel run | Both approaches are publishing metrics simultaneously | This behavior is expected during a parallel run. Disable the legacy approach after you validate the new approach. | 
| Different metric values between approaches | Different calculation methods | Small differences (less than 5%) are expected. Large differences indicate a configuration mismatch between approaches. | 
| Rollback fails | Custom configuration was not reapplied | Re-apply your complete configuration values when you roll back. | 
| Alarms fire during migration | Metric gaps during the switchover period | Temporarily set the missing data treatment to notBreaching on affected alarms. | 

## OTel Container Insights issues
<a name="container-insights-eks-troubleshooting-otel"></a>

The following issues are specific to the OTel Container Insights approach. For general setup guidance, see [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md).


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| 403 Forbidden exporter error | IAM role is missing CloudWatch permissions | Verify that the CloudWatchAgentServerPolicy is attached to the agent role. | 
| Connection refused on metrics endpoint | Collector cannot reach the kubelet | Verify that hostNetwork: true is set in the pod spec, or confirm that the service account has the required permissions. | 
| High memory usage | Batch processor queue is too large | Reduce the batch/timeout and batch/send\_batch\_size values in the collector configuration. | 
| Custom metrics not appearing | Receiver not configured for the application endpoint | Add a Prometheus receiver that targets your application metrics port in the collector configuration. | 

## General diagnostic commands
<a name="container-insights-eks-troubleshooting-commands"></a>

Use the following commands to gather information about your Container Insights deployment.

To check agent pod status, run the following command.

```
kubectl get pods -n amazon-cloudwatch
```

To view agent pod logs, run the following command.

```
kubectl logs -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent --tail=50
```

To check the agent DaemonSet status, run the following command.

```
kubectl get daemonset -n amazon-cloudwatch
```

To verify the IAM role on a service account, run the following command.

```
kubectl get serviceaccount -n amazon-cloudwatch -o yaml
```

To check the cluster add-on status, run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```
aws eks describe-addon --cluster-name {{cluster-name}} --addon-name amazon-cloudwatch-observability
```

To list Container Insights log groups, run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```
aws logs describe-log-groups --log-group-name-prefix "/aws/containerinsights/{{cluster-name}}"
```

## Related resources
<a name="container-insights-eks-troubleshooting-related"></a>

For more information about setting up and operating Container Insights on Amazon EKS, see the following topics.
+ [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md) – Set up OTel Container Insights
+ [Setup guide (AWS CLI)](container-insights-eks-classic-setup.md) – Set up Classic Container Insights
+ [Migration guides](container-insights-eks-migration-hub.md) – Migrate between approaches
+ [Compare Container Insights approaches](container-insights-eks-compare.md) – Compare Container Insights approaches