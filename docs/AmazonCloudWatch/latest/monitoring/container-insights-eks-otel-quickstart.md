

# Quick start: OTel Container Insights on Amazon EKS
<a name="container-insights-eks-otel-quickstart"></a>

This guide walks you through enabling OTel Container Insights on an existing Amazon EKS cluster. By the end of this procedure, your cluster sends infrastructure metrics and container logs to Amazon CloudWatch with Enhanced Observability enabled.

You can enable OTel Container Insights in two ways: by using the AWS Management Console (fastest) or by using the AWS CLI. Both approaches install the same `amazon-cloudwatch-observability` EKS add-on with the OTel Container Insights configuration. You don't need manual agent deployment, Helm charts, or custom collector pipelines. The entire process takes under 5 minutes.

## Prerequisites
<a name="container-insights-eks-otel-quickstart-prereqs"></a>

Before you enable OTel Container Insights, verify that you meet the following requirements.
+ An existing Amazon EKS cluster running Kubernetes version 1.28 or later
+ Platform version `eks.1` or later
+ Version 6.2.0 or later of the `amazon-cloudwatch-observability` add-on
+ AWS CLI version 2.15.0 or later (for CLI-based setup)
+ `kubectl` configured to communicate with your target cluster
+ IAM permissions: `eks:CreateAddon`, `eks:DescribeAddon`, and `iam:CreateServiceLinkedRole`
+ The EKS Pod Identity Agent add-on installed on your cluster, or IAM Roles for Service Accounts (IRSA) configured
+ Outbound internet access from the cluster to CloudWatch endpoints

## Enable OTel Container Insights (console)
<a name="container-insights-eks-otel-quickstart-console"></a>

The AWS Management Console provides the fastest path to enable OTel Container Insights.

**To enable OTel Container Insights by using the console**

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/](https://console.aws.amazon.com/eks/).

1. Choose **Clusters**, and then choose your cluster name.

1. Choose the **Observability** tab.

1. Choose **Enable Container Insights** and follow the on-screen instructions.

For a detailed console walkthrough, see [Enable OTel Container Insights from the console](container-insights-eks-otel-console.md).

## Enable OTel Container Insights (AWS CLI)
<a name="container-insights-eks-otel-quickstart-cli"></a>

Use the following steps to enable OTel Container Insights by using the AWS CLI.

### Step 1: Create the IAM role
<a name="container-insights-eks-otel-quickstart-cli-step1"></a>

Create an IAM role that allows the CloudWatch Observability add-on to send data to CloudWatch.

**To create the CloudWatch Observability add-on IAM role**

1. Run the following command to create the role with a trust policy for EKS Pod Identity.

   ```
   aws iam create-role \
     --role-name EKS-CloudWatch-Observability-Role \
     --assume-role-policy-document '{
       "Version": "2012-10-17",
       "Statement": [{
         "Effect": "Allow",
         "Principal": { "Service": "pods.eks.amazonaws.com" },
         "Action": ["sts:AssumeRole", "sts:TagSession"]
       }]
     }'
   ```

1. Attach the `CloudWatchAgentServerPolicy` managed policy to the role.

   ```
   aws iam attach-role-policy \
     --role-name EKS-CloudWatch-Observability-Role \
     --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
   ```

### Step 2: Create the Pod Identity association
<a name="container-insights-eks-otel-quickstart-cli-step2"></a>

Associate the IAM role with the CloudWatch agent service account in your cluster.

**To create the Pod Identity association**
+ Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster and {{account-id}} with your AWS account ID.

  ```
  aws eks create-pod-identity-association \
    --cluster-name {{cluster-name}} \
    --namespace amazon-cloudwatch \
    --service-account cloudwatch-agent \
    --role-arn arn:aws:iam::{{account-id}}:role/EKS-CloudWatch-Observability-Role
  ```

### Step 3: Install the Amazon CloudWatch Observability add-on
<a name="container-insights-eks-otel-quickstart-cli-step3"></a>

Install the `amazon-cloudwatch-observability` add-on with OTel Container Insights enabled.

**To install the add-on**
+ Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

  ```
  aws eks create-addon \
    --cluster-name {{cluster-name}} \
    --addon-name amazon-cloudwatch-observability \
    --configuration-values '{"otelContainerInsights":{"enabled":true}}'
  ```
**Important**  
The `otelContainerInsights.enabled` configuration is required. OTel Container Insights is not enabled by default.

### Step 4: Verify the add-on status
<a name="container-insights-eks-otel-quickstart-cli-step4"></a>

Confirm that the add-on installed successfully.

**To verify the add-on status**
+ Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

  ```
  aws eks describe-addon \
    --cluster-name {{cluster-name}} \
    --addon-name amazon-cloudwatch-observability \
    --query "addon.status" \
    --output text
  ```

  The expected output is `ACTIVE`.

### Step 5: Confirm agent pods are running
<a name="container-insights-eks-otel-quickstart-cli-step5"></a>

Verify that the CloudWatch agent pods are running in the `amazon-cloudwatch` namespace.

**To confirm agent pods are running**
+ Run the following command.

  ```
  kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
  ```

  All agent pods must show `Running` status.

## Verify data in CloudWatch
<a name="container-insights-eks-otel-quickstart-verify"></a>

After you complete the setup, Container Insights data appears in CloudWatch within 3 to 5 minutes.

### Check metrics
<a name="container-insights-eks-otel-quickstart-verify-metrics"></a>

**To check metrics in CloudWatch**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Query Studio**.

1. Search for metrics such as `container_cpu_usage_seconds_total` by using PromQL.

### Check logs
<a name="container-insights-eks-otel-quickstart-verify-logs"></a>

To verify that log groups exist for your cluster, run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```
aws logs describe-log-groups \
  --log-group-name-prefix "/aws/containerinsights/{{cluster-name}}" \
  --query "logGroups[].logGroupName" \
  --output table
```

### Expected time-to-data
<a name="container-insights-eks-otel-quickstart-verify-latency"></a>

The following table shows the expected latency for each signal type after you enable OTel Container Insights.


| Signal | Expected latency | 
| --- | --- | 
| Infrastructure metrics | 2–3 minutes | 
| Container logs | 2–3 minutes | 
| Performance log events | 3–5 minutes | 

## Troubleshooting
<a name="container-insights-eks-otel-quickstart-troubleshoot"></a>

Use the following guidance to resolve common issues when you enable OTel Container Insights on Amazon EKS.

### Add-on status shows CREATE\_FAILED or DEGRADED
<a name="container-insights-eks-otel-quickstart-ts-create-failed"></a>

**Symptom:** When you run `aws eks describe-addon`, the status shows `CREATE_FAILED` or `DEGRADED`.

**Cause:** The add-on installation failed, typically because of insufficient IAM permissions or a missing Pod Identity association.

**Solution:** Complete the following steps to resolve this issue.

1. Run the following command to check for detailed error information. Replace {{cluster-name}} with the name of your cluster.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.health"
   ```

1. Verify that the IAM role exists and has the `CloudWatchAgentServerPolicy` attached.

1. Verify that the Pod Identity association targets the correct namespace (`amazon-cloudwatch`) and service account (`cloudwatch-agent`).

1. Delete the failed add-on and reinstall it after you resolve the issue.

   ```
   aws eks delete-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability
   ```

### Agent pods are in CrashLoopBackOff or Pending state
<a name="container-insights-eks-otel-quickstart-ts-crashloop"></a>

**Symptom:** When you run `kubectl get pods -n amazon-cloudwatch`, one or more pods show `CrashLoopBackOff` or `Pending` status.

**Cause:** The agent pods can't start because of insufficient node resources, missing permissions, or network connectivity issues.

**Solution:** Complete the following steps to resolve this issue.

1. Check the pod events for detailed error messages.

   ```
   kubectl describe pod -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
   ```

1. Check the agent container logs for startup errors.

   ```
   kubectl logs -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent --tail=50
   ```

1. Verify that your nodes have sufficient CPU and memory available for the agent pods.

1. Verify that the EKS Pod Identity Agent add-on is installed and running.

   ```
   kubectl get pods -n kube-system -l app.kubernetes.io/name=eks-pod-identity-agent
   ```

### Metrics not appearing in CloudWatch after 5 minutes
<a name="container-insights-eks-otel-quickstart-ts-no-metrics"></a>

**Symptom:** The agent pods show `Running` status, but no metrics appear in CloudWatch after 5 minutes.

**Cause:** The agent can't send data to CloudWatch, typically because of network restrictions or incorrect IAM permissions.

**Solution:** Complete the following steps to resolve this issue.

1. Verify that the agent pods can reach CloudWatch endpoints. Check that your VPC security groups and network ACLs allow outbound HTTPS traffic (port 443) to CloudWatch endpoints.

1. Check the agent logs for permission errors or connection timeouts.

   ```
   kubectl logs -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent --tail=100 | grep -i "error\|timeout\|denied"
   ```

1. Verify that the IAM role has the `CloudWatchAgentServerPolicy` policy attached and that the trust policy allows `pods.eks.amazonaws.com`.

1. If you use a VPC endpoint for CloudWatch, confirm that the endpoint policy allows the required actions.