

# Deploy OTel Container Insights with Helm
<a name="container-insights-eks-otel-helm"></a>

The Amazon CloudWatch Observability Helm chart provides a flexible deployment option for OTel Container Insights. It installs the CloudWatch agent (OTel-based) with the OpenTelemetry filelog receiver for log collection. The Helm chart is maintained at [https://github.com/aws-observability/helm-charts](https://github.com/aws-observability/helm-charts).

Use the Helm chart when you need one or more of the following capabilities:
+ Fine-grained control over agent configuration
+ OTel-native log collection using the filelog receiver (no Fluent Bit dependency)
+ Custom TLS certificate management through cert-manager
+ Non-EKS Kubernetes clusters (ROSA, self-managed Kubernetes)
+ GitOps workflows with ArgoCD or Flux

## Prerequisites
<a name="container-insights-eks-otel-helm-prereqs"></a>

Before you deploy OTel Container Insights with Helm, verify that you meet the following requirements.
+ An existing Amazon EKS cluster running Kubernetes version 1.28 or later
+ Helm version 3.9 or later
+ `kubectl` configured to communicate with your target cluster
+ IAM permissions: `CloudWatchAgentServerPolicy` managed policy attached to the agent role
+ An OpenID Connect (OIDC) provider configured for IAM Roles for Service Accounts (IRSA)
+ Outbound internet access from the cluster to CloudWatch endpoints

## Install the Helm chart
<a name="container-insights-eks-otel-helm-setup"></a>

Complete the following steps to deploy OTel Container Insights by using the Helm chart.

### Step 1: Add the Helm repository
<a name="container-insights-eks-otel-helm-step1"></a>

Add the AWS Observability Helm chart repository to your local Helm configuration.

**To add the Helm repository**

1. Run the following command to add the repository.

   ```
   helm repo add aws-observability \
     https://aws-observability.github.io/helm-charts
   ```

1. Update the repository to get the latest chart versions.

   ```
   helm repo update
   ```

### Step 2: Create the IAM role
<a name="container-insights-eks-otel-helm-step2"></a>

Create an IAM role that allows the CloudWatch agent to send data to CloudWatch. This role uses IRSA to associate IAM permissions with a Kubernetes service account.

**To create the IAM role for the CloudWatch agent**

1. Retrieve the OIDC issuer URL for your cluster. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

   ```
   aws eks describe-cluster \
     --name {{cluster-name}} \
     --query "cluster.identity.oidc.issuer" \
     --output text
   ```

1. Create the IAM role with a trust policy for IRSA. Replace {{account-id}} with your AWS account ID and {{oidc-id}} with the OIDC provider ID from the preceding step (the portion after `https://oidc.eks.region.amazonaws.com/id/`).

   ```
   aws iam create-role \
     --role-name EKS-CW-Observability-Role \
     --assume-role-policy-document '{
       "Version": "2012-10-17",
       "Statement": [{
         "Effect": "Allow",
         "Principal": {
           "Federated": "arn:aws:iam::{{account-id}}:oidc-provider/oidc.eks.{{region}}.amazonaws.com/id/{{oidc-id}}"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": {
             "oidc.eks.{{region}}.amazonaws.com/id/{{oidc-id}}:sub": "system:serviceaccount:amazon-cloudwatch:cloudwatch-agent"
           }
         }
       }]
     }'
   ```

1. Attach the `CloudWatchAgentServerPolicy` managed policy to the role.

   ```
   aws iam attach-role-policy \
     --role-name EKS-CW-Observability-Role \
     --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
   ```

### Step 3: Install the chart
<a name="container-insights-eks-otel-helm-step3"></a>

Install the Amazon CloudWatch Observability Helm chart with OTel Container Insights enabled.

**To install the Helm chart**
+ Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster, {{region}} with your AWS Region, and {{account-id}} with your AWS account ID.

  ```
  helm install amazon-cloudwatch-observability \
    aws-observability/amazon-cloudwatch-observability \
    --namespace amazon-cloudwatch \
    --create-namespace \
    --set clusterName={{cluster-name}} \
    --set region={{region}} \
    --set agent.serviceAccount.name=cloudwatch-agent \
    --set "agent.serviceAccount.annotations.eks\\.amazonaws\\.com/role-arn=arn:aws:iam::{{account-id}}:role/EKS-CW-Observability-Role" \
    --set otelContainerInsights.enabled=true
  ```
**Important**  
The `otelContainerInsights.enabled` parameter is required. OTel Container Insights is not enabled by default.

### Step 4: Verify the installation
<a name="container-insights-eks-otel-helm-step4"></a>

Confirm that the Helm release and agent pods deployed successfully.

**To verify the Helm installation**

1. Verify that the Helm release status shows `deployed`.

   ```
   helm list -n amazon-cloudwatch
   ```

1. Confirm that the operator pod is running.

   ```
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=amazon-cloudwatch-observability
   ```

1. Confirm that the CloudWatch agent pods are running on all nodes.

   ```
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
   ```

   All agent pods must show `Running` status.

## Key configuration options
<a name="container-insights-eks-otel-helm-config"></a>

The following tables describe the key Helm chart values that you can configure. Pass these values by using the `--set` flag or a custom `values.yaml` file.

### Cluster settings
<a name="container-insights-eks-otel-helm-config-cluster"></a>


| Parameter | Default | Description | 
| --- | --- | --- | 
| clusterName | — | The name of the Amazon EKS cluster. Required. | 
| region | — | The AWS Region where the cluster runs. Required. | 
| otelContainerInsights.enabled | false | Enables OTel Container Insights with the filelog receiver. | 

### Container logs (OTel filelog receiver)
<a name="container-insights-eks-otel-helm-config-logs"></a>


| Parameter | Default | Description | 
| --- | --- | --- | 
| containerLogs.enabled | true | Enables container log collection by using the OTel filelog receiver. | 
| containerLogs.logGroupName | /aws/containerinsights/{{cluster-name}}/application | The CloudWatch Logs log group name for container logs. | 
| containerLogs.logRetentionDays | 7 | The number of days to retain container logs in CloudWatch Logs. | 

### Agent (metrics)
<a name="container-insights-eks-otel-helm-config-agent"></a>


| Parameter | Default | Description | 
| --- | --- | --- | 
| agent.enabled | true | Enables the CloudWatch agent DaemonSet for metric collection. | 
| agent.serviceAccount.name | cloudwatch-agent | The name of the Kubernetes service account for the agent. | 
| agent.resources.requests.cpu | 100m | The CPU request for the agent container. | 
| agent.resources.requests.memory | 128Mi | The memory request for the agent container. | 
| agent.resources.limits.cpu | 200m | The CPU limit for the agent container. | 
| agent.resources.limits.memory | 256Mi | The memory limit for the agent container. | 

### GPU monitoring
<a name="container-insights-eks-otel-helm-config-gpu"></a>


| Parameter | Default | Description | 
| --- | --- | --- | 
| agent.config.logs.metrics\_collected.kubernetes.enhanced\_container\_insights | true | Enables Enhanced Container Insights metrics, including GPU metrics. | 
| dcgmExporter.enabled | false | Enables the DCGM exporter for NVIDIA GPU metrics. Requires NVIDIA GPU nodes. | 
| neuronMonitor.enabled | false | Enables the Neuron monitor for AWS Inferentia and Trainium metrics. | 

## TLS certificate management
<a name="container-insights-eks-otel-helm-tls"></a>

The CloudWatch Observability operator requires TLS certificates for webhook communication. By default, the chart generates self-signed certificates. You can use cert-manager to manage certificates automatically.

### Self-signed certificates (default)
<a name="container-insights-eks-otel-helm-tls-default"></a>

By default, the Helm chart generates a self-signed CA and issues certificates from that CA. No additional configuration is required. The chart automatically rotates these certificates during upgrades.

### cert-manager integration
<a name="container-insights-eks-otel-helm-tls-certmanager"></a>

You can use cert-manager to automate certificate issuance and renewal. This approach is useful when your organization requires externally signed certificates or centralized certificate management.

**To configure cert-manager integration**

1. Verify that cert-manager is installed in your cluster.

   ```
   kubectl get pods -n cert-manager
   ```

1. Install the Helm chart with cert-manager enabled. Replace {{cluster-name}} with the name of your Amazon EKS cluster, {{region}} with your AWS Region, and {{account-id}} with your AWS account ID.

   ```
   helm install amazon-cloudwatch-observability \
     aws-observability/amazon-cloudwatch-observability \
     --namespace amazon-cloudwatch \
     --create-namespace \
     --set clusterName={{cluster-name}} \
     --set region={{region}} \
     --set agent.serviceAccount.name=cloudwatch-agent \
     --set "agent.serviceAccount.annotations.eks\\.amazonaws\\.com/role-arn=arn:aws:iam::{{account-id}}:role/EKS-CW-Observability-Role" \
     --set otelContainerInsights.enabled=true \
     --set admissionWebhooks.certManager.enabled=true
   ```

When cert-manager is enabled, the chart creates a `Certificate` resource that cert-manager uses to issue and manage the webhook TLS certificate automatically.

**Note**  
You can also use cert-manager with external issuers such as HashiCorp Vault. To configure an external issuer, set `admissionWebhooks.certManager.issuerRef.name` and `admissionWebhooks.certManager.issuerRef.kind` to match your cert-manager issuer.

## Upgrade the chart
<a name="container-insights-eks-otel-helm-upgrade"></a>

Upgrade the Helm chart to apply new configuration values or to update to a newer chart version.

**To upgrade the Helm chart**

1. Update the Helm repository to get the latest chart versions.

   ```
   helm repo update
   ```

1. Run the upgrade command with your desired values. Replace {{cluster-name}} with the name of your Amazon EKS cluster, {{region}} with your AWS Region, and {{account-id}} with your AWS account ID.

   ```
   helm upgrade amazon-cloudwatch-observability \
     aws-observability/amazon-cloudwatch-observability \
     --namespace amazon-cloudwatch \
     --set clusterName={{cluster-name}} \
     --set region={{region}} \
     --set agent.serviceAccount.name=cloudwatch-agent \
     --set "agent.serviceAccount.annotations.eks\\.amazonaws\\.com/role-arn=arn:aws:iam::{{account-id}}:role/EKS-CW-Observability-Role" \
     --set otelContainerInsights.enabled=true
   ```

1. Verify that the upgrade completed successfully.

   ```
   helm list -n amazon-cloudwatch
   ```

   The revision number must increment and the status must show `deployed`.

**Tip**  
To avoid losing configuration values during upgrades, store your custom values in a `values.yaml` file and pass it with the `-f values.yaml` flag.

## Uninstall the chart
<a name="container-insights-eks-otel-helm-uninstall"></a>

To remove OTel Container Insights from your cluster, uninstall the Helm release.

**To uninstall the Helm chart**

1. Run the following command to uninstall the release.

   ```
   helm uninstall amazon-cloudwatch-observability \
     --namespace amazon-cloudwatch
   ```

1. Optionally, delete the namespace if it is no longer needed.

   ```
   kubectl delete namespace amazon-cloudwatch
   ```

After you uninstall the Helm chart, the IAM role and OIDC provider configuration remain in your AWS account. Delete these resources separately if they are no longer needed.

```
aws iam detach-role-policy \
  --role-name EKS-CW-Observability-Role \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy

aws iam delete-role \
  --role-name EKS-CW-Observability-Role
```

## Verify data in CloudWatch
<a name="container-insights-eks-otel-helm-verify"></a>

After you install the Helm chart, Container Insights data appears in CloudWatch within 3 to 5 minutes.

### Check metrics
<a name="container-insights-eks-otel-helm-verify-metrics"></a>

**To check metrics in CloudWatch**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Container Insights**.

1. Verify that your cluster appears in the cluster list and that infrastructure metrics are populating.

### Check logs
<a name="container-insights-eks-otel-helm-verify-logs"></a>

To verify that log groups exist for your cluster, run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```
aws logs describe-log-groups \
  --log-group-name-prefix "/aws/containerinsights/{{cluster-name}}" \
  --query "logGroups[].logGroupName" \
  --output table
```

## Troubleshooting
<a name="container-insights-eks-otel-helm-troubleshoot"></a>

Use the following guidance to resolve common issues when you deploy OTel Container Insights with Helm.

### Operator pod in CrashLoopBackOff
<a name="container-insights-eks-otel-helm-ts-operator-crash"></a>

**Symptom:** When you run `kubectl get pods -n amazon-cloudwatch`, the operator pod shows `CrashLoopBackOff` status.

**Cause:** The operator pod can't start because of TLS certificate issues or insufficient permissions.

**Solution:** Complete the following steps to resolve this issue.

1. Check the operator pod logs for certificate-related errors.

   ```
   kubectl logs -n amazon-cloudwatch -l app.kubernetes.io/name=amazon-cloudwatch-observability --tail=50
   ```

1. Verify that the webhook TLS secret exists in the namespace.

   ```
   kubectl get secrets -n amazon-cloudwatch | grep webhook
   ```

1. If you use cert-manager, verify that the `Certificate` resource status shows `Ready`.

   ```
   kubectl get certificate -n amazon-cloudwatch
   ```

1. If the certificate is missing or invalid, uninstall and reinstall the chart to regenerate certificates.

   ```
   helm uninstall amazon-cloudwatch-observability -n amazon-cloudwatch
   ```

### Agent pods not scheduled on all nodes
<a name="container-insights-eks-otel-helm-ts-agent-scheduling"></a>

**Symptom:** The agent DaemonSet shows fewer pods than the number of nodes in your cluster.

**Cause:** Node taints, resource constraints, or node selectors prevent the agent pods from scheduling on certain nodes.

**Solution:** Complete the following steps to resolve this issue.

1. Check the DaemonSet status for scheduling issues.

   ```
   kubectl get daemonset -n amazon-cloudwatch cloudwatch-agent
   ```

1. Check for unschedulable pods and view their events.

   ```
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent --field-selector=status.phase!=Running
   ```

1. If nodes have taints, add tolerations to the Helm chart values. For example, to tolerate all taints, upgrade the chart with the following flag.

   ```
   helm upgrade amazon-cloudwatch-observability \
     aws-observability/amazon-cloudwatch-observability \
     --namespace amazon-cloudwatch \
     --reuse-values \
     --set "agent.tolerations[0].operator=Exists"
   ```

1. Verify that the agent pods now run on all nodes.

   ```
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent -o wide
   ```