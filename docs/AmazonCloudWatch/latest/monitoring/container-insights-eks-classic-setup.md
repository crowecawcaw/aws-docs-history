

# Setup guide (AWS CLI)
<a name="container-insights-eks-classic-setup"></a>

This guide walks you through installing Enhanced Container Insights (Classic) on an existing Amazon EKS cluster by using the AWS CLI. The add-on deploys a CloudWatch agent as a DaemonSet that collects infrastructure metrics, container logs, and performance data.

**Maintenance mode**  
Enhanced Container Insights (Classic) is in maintenance mode. For new deployments, you should recommend [OTel Container Insights (Recommended)](container-insights-eks-otel.md).

## Prerequisites
<a name="container-insights-eks-classic-setup-prereqs"></a>

Before you begin, verify that you meet the following requirements.
+ An existing Amazon EKS cluster running Kubernetes version 1.25 or later
+ Platform version `eks.1` or later
+ AWS CLI version 2.12.0 or later
+ `kubectl` configured to communicate with your target cluster
+ IAM permissions: `eks:CreateAddon`, `eks:DescribeAddon`, `iam:CreateServiceLinkedRole`, `iam:CreateRole`, and `iam:AttachRolePolicy`
+ The EKS Pod Identity Agent add-on installed on your cluster, or IAM Roles for Service Accounts (IRSA) configured
+ Outbound internet access from the cluster to CloudWatch endpoints

## Step 1: Create the IAM role
<a name="container-insights-eks-classic-setup-step1"></a>

Create an IAM role that allows the CloudWatch agent to send data to CloudWatch.

**To create the CloudWatch agent IAM role**

1. Run the following command to create the role with a trust policy for EKS Pod Identity.

   ```
   aws iam create-role \
     --role-name EKS-CloudWatch-Agent-Role \
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
     --role-name EKS-CloudWatch-Agent-Role \
     --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
   ```

## Step 2: Create the Pod Identity association
<a name="container-insights-eks-classic-setup-step2"></a>

Associate the IAM role with the CloudWatch agent service account in your cluster.

**To create the Pod Identity association**
+ Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster and {{account-id}} with your AWS account ID.

  ```
  aws eks create-pod-identity-association \
    --cluster-name {{cluster-name}} \
    --namespace amazon-cloudwatch \
    --service-account cloudwatch-agent \
    --role-arn arn:aws:iam::{{account-id}}:role/EKS-CloudWatch-Agent-Role
  ```

## Step 3: Install the Amazon CloudWatch Observability add-on
<a name="container-insights-eks-classic-setup-step3"></a>

Install the `amazon-cloudwatch-observability` add-on on your cluster.

**To install the add-on**
+ Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

  ```
  aws eks create-addon \
    --cluster-name {{cluster-name}} \
    --addon-name amazon-cloudwatch-observability \
    --addon-version {{v5.x.x-eksbuild.x}}
  ```

  Replace {{v5.x.x-eksbuild.x}} with the latest available v5.x version. Installing without `--addon-version` installs the latest version (v6.2.0\+), which activates the OTel pipeline instead of Classic.

## Step 4: Verify the add-on status
<a name="container-insights-eks-classic-setup-step4"></a>

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

## Step 5: Confirm agent pods are running
<a name="container-insights-eks-classic-setup-step5"></a>

Verify that the CloudWatch agent pods are running in the `amazon-cloudwatch` namespace.

**To confirm agent pods are running**
+ Run the following command.

  ```
  kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
  ```

  All agent pods must show `Running` status.

## Verify data in CloudWatch
<a name="container-insights-eks-classic-setup-verify"></a>

After you complete the setup, Container Insights data appears in CloudWatch within 3 to 5 minutes.

**To verify Container Insights data**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Container Insights**.

1. Verify that metrics such as `node_cpu_utilization` and `pod_memory_utilization` appear for your cluster.

## Troubleshooting
<a name="container-insights-eks-classic-setup-troubleshoot"></a>

Use the following guidance to resolve common issues when you install Enhanced Container Insights (Classic) on Amazon EKS.

### Add-on status shows CREATE\_FAILED or DEGRADED
<a name="container-insights-eks-classic-setup-ts-create-failed"></a>

**Symptom:** When you run `aws eks describe-addon`, the status shows `CREATE_FAILED` or `DEGRADED`.

**Cause:** The add-on installation failed because of insufficient IAM permissions or a missing Pod Identity association.

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

### Metrics not appearing in CloudWatch after 5 minutes
<a name="container-insights-eks-classic-setup-ts-no-metrics"></a>

**Symptom:** The agent pods show `Running` status, but no metrics appear in CloudWatch after 5 minutes.

**Cause:** The agent can't send data to CloudWatch because of network restrictions or incorrect IAM permissions.

**Solution:** Complete the following steps to resolve this issue.

1. Verify that your VPC security groups and network ACLs allow outbound HTTPS traffic (port 443) to CloudWatch endpoints.

1. Check the agent logs for permission errors or connection timeouts.

   ```
   kubectl logs -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent --tail=100 | grep -i "error\|timeout\|denied"
   ```

1. Verify that the IAM role has the `CloudWatchAgentServerPolicy` policy attached and that the trust policy allows `pods.eks.amazonaws.com`.

### Agent pods stuck in Pending or CrashLoopBackOff
<a name="container-insights-eks-classic-setup-ts-crashloop"></a>

**Symptom:** When you run `kubectl get pods -n amazon-cloudwatch`, one or more pods show `Pending` or `CrashLoopBackOff` status.

**Cause:** The agent pods can't start because of insufficient node resources, image pull failures, or missing permissions.

**Solution:** Complete the following steps to resolve this issue.

1. Check the pod events for detailed error messages.

   ```
   kubectl describe pod -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
   ```

1. Verify that your nodes have sufficient CPU and memory available for the agent pods.

1. Verify that the EKS Pod Identity Agent add-on is installed and running.

   ```
   kubectl get pods -n kube-system -l app.kubernetes.io/name=eks-pod-identity-agent
   ```

## Next steps
<a name="container-insights-eks-classic-setup-next"></a>

Ready to upgrade? For step-by-step instructions to move from Enhanced Container Insights (Classic) to OTel Container Insights, see [Migrate from Enhanced Container Insights (Classic) to OTel Container Insights](container-insights-eks-migrate-from-classic.md).