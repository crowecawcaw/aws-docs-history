

# Advanced configuration for OTel Container Insights on Amazon EKS
<a name="container-insights-eks-otel-advanced"></a>

This topic covers advanced configuration scenarios for OTel Container Insights on Amazon EKS. Use these configurations to customize metric collection, filter logs, collect telemetry across accounts, add custom dimensions, and tune resource allocation for large clusters.

## Prerequisites
<a name="container-insights-eks-otel-advanced-prereqs"></a>

Before you configure advanced settings, verify that you meet the following requirements.
+ OTel Container Insights installed and in `ACTIVE` status on your Amazon EKS cluster
+ Amazon EKS cluster running Kubernetes version 1.28 or later
+ AWS CLI version 2.15.0 or later
+ `kubectl` configured to communicate with your target cluster
+ IAM permissions: `eks:UpdateAddon`, `eks:DescribeAddon`, and `iam:AttachRolePolicy` (required for cross-account configuration)

## General configuration pattern
<a name="container-insights-eks-otel-advanced-pattern"></a>

All advanced configurations follow the same pattern. You pass a JSON configuration to the `amazon-cloudwatch-observability` add-on by using the `aws eks update-addon` command.

```
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{{JSON-configuration}}' \
  --resolve-conflicts OVERWRITE
```

**Important**  
The `--resolve-conflicts OVERWRITE` flag replaces any existing add-on configuration. To preserve existing settings, merge them with your new configuration before you run the command.

## Log filtering
<a name="container-insights-eks-otel-advanced-log-filtering"></a>

You can reduce CloudWatch Logs costs by excluding logs that match specific criteria. Use log filtering to drop debug-level or verbose logs before the agent sends them to CloudWatch.

**To configure log filtering**

1. Run the following command to update the add-on with a log filter configuration. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

   ```
   aws eks update-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --configuration-values '{
       "otelContainerInsights": {
         "enabled": true
       },
       "agent": {
         "config": {
           "logs": {
             "metrics_collected": {
               "kubernetes": {
                 "enhanced_container_insights": true
               }
             },
             "exclude_filters": [
               {
                 "type": "log_level_filter",
                 "log_level": "DEBUG"
               }
             ]
           }
         }
       }
     }' \
     --resolve-conflicts OVERWRITE
   ```

1. Verify that the add-on status is `ACTIVE` after the update.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.status" \
     --output text
   ```

The `exclude_filters` configuration removes log entries that match the specified log level before the agent sends them to CloudWatch Logs. This reduces your log ingestion volume and associated costs.

## Multi-account collection
<a name="container-insights-eks-otel-advanced-multi-account"></a>

You can send telemetry from workload accounts to a central monitoring account by configuring cross-account IAM role assumption. This approach gives you a single view of metrics and logs from multiple Amazon EKS clusters across different AWS accounts.

### To set up multi-account collection
<a name="container-insights-eks-otel-advanced-multi-account-setup"></a>

**To create the cross-account role in the monitoring account**

1. In the central monitoring account, create an IAM role with a trust policy that allows the workload account to assume it. Replace {{workload-account-id}} with the AWS account ID of the workload account.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::{{workload-account-id}}:root"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

1. Attach the `CloudWatchAgentServerPolicy` managed policy to the cross-account role.

**To configure the add-on for cross-account delivery**

1. In the workload account, update the add-on to assume the cross-account role. Replace {{cluster-name}} with the name of your Amazon EKS cluster and {{monitoring-account-id}} with the AWS account ID of the central monitoring account.

   ```
   aws eks update-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --configuration-values '{
       "otelContainerInsights": {
         "enabled": true
       },
       "agent": {
         "config": {
           "credentials": {
             "role_arn": "arn:aws:iam::{{monitoring-account-id}}:role/CrossAccountCWObservabilityRole"
           }
         }
       }
     }' \
     --resolve-conflicts OVERWRITE
   ```

1. Verify that the add-on status is `ACTIVE` after the update.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.status" \
     --output text
   ```

## Custom metric dimensions
<a name="container-insights-eks-otel-advanced-dimensions"></a>

You can add custom dimensions derived from Kubernetes labels to your Container Insights metrics. Custom dimensions allow you to filter and group metrics at a finer granularity, such as by team, environment, or application tier.

**To add custom dimensions from Kubernetes labels**

1. Run the following command to configure custom dimensions. Replace {{cluster-name}} with the name of your Amazon EKS cluster and {{label-key}} with the Kubernetes label to use as a dimension.

   ```
   aws eks update-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --configuration-values '{
       "otelContainerInsights": {
         "enabled": true
       },
       "agent": {
         "config": {
           "logs": {
             "metrics_collected": {
               "kubernetes": {
                 "enhanced_container_insights": true,
                 "metric_dimensions": {
                   "custom_dimensions": ["{{label-key}}"]
                 }
               }
             }
           }
         }
       }
     }' \
     --resolve-conflicts OVERWRITE
   ```

1. Verify that the add-on status is `ACTIVE` after the update.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.status" \
     --output text
   ```

After the configuration takes effect, the specified Kubernetes labels appear as dimensions on your Container Insights metrics in CloudWatch.

## Resource tuning for large clusters
<a name="container-insights-eks-otel-advanced-resource-tuning"></a>

For large clusters, you might need to increase the CPU and memory limits for the CloudWatch agent DaemonSet. The default resource allocation works well for small clusters, but larger clusters generate more telemetry data and require additional agent resources.

The following table provides sizing guidelines based on cluster size.


| Cluster size | CPU request | CPU limit | Memory request | Memory limit | 
| --- | --- | --- | --- | --- | 
| Small (20 nodes or fewer) | 100m | 200m | 128Mi | 256Mi | 
| Medium (21–100 nodes) | 200m | 400m | 256Mi | 512Mi | 
| Large (100\+ nodes) | 300m | 500m | 384Mi | 768Mi | 
| Extra-large (500\+ nodes) | 500m | 1000m | 512Mi | 1Gi | 

**To configure resource limits for the agent DaemonSet**

1. Run the following command to set resource requests and limits. Replace {{cluster-name}} with the name of your Amazon EKS cluster and the resource values with values from the preceding table.

   ```
   aws eks update-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --configuration-values '{
       "otelContainerInsights": {
         "enabled": true
       },
       "agent": {
         "resources": {
           "requests": {
             "cpu": "{{cpu-request}}",
             "memory": "{{memory-request}}"
           },
           "limits": {
             "cpu": "{{cpu-limit}}",
             "memory": "{{memory-limit}}"
           }
         }
       }
     }' \
     --resolve-conflicts OVERWRITE
   ```

1. Verify that the add-on status is `ACTIVE` and that agent pods restart with the new resource allocation.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.status" \
     --output text
   ```

1. Confirm that the agent pods are running with the new resource limits.

   ```
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent -o jsonpath='{.items[0].spec.containers[0].resources}'
   ```

## Verify configuration changes
<a name="container-insights-eks-otel-advanced-verify"></a>

After you apply any advanced configuration, verify that the add-on is healthy and that agent pods restarted successfully.

**To verify configuration changes**

1. Check that the add-on status is `ACTIVE`. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.{Status:status,ConfigValues:configurationValues}" \
     --output table
   ```

1. Verify that agent pods restarted and are in `Running` status.

   ```
   kubectl get pods -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent
   ```

   All agent pods must show `Running` status with a recent restart time.

## Troubleshooting
<a name="container-insights-eks-otel-advanced-troubleshoot"></a>

Use the following guidance to resolve common issues with advanced configurations.

### Add-on update fails with ConfigurationConflict
<a name="container-insights-eks-otel-advanced-ts-config-conflict"></a>

**Symptom:** The `aws eks update-addon` command returns a `ConfigurationConflict` error.

**Cause:** The JSON configuration that you provided is malformed or contains invalid keys.

**Solution:** Complete the following steps to resolve this issue.

1. Validate your JSON configuration by using a JSON linter or by running the following command.

   ```
   echo '{{your-json-configuration}}' | python3 -m json.tool
   ```

1. Verify that all configuration keys are valid for the `amazon-cloudwatch-observability` add-on.

1. Retry the update with the corrected JSON.

### Cross-account metrics not appearing in the monitoring account
<a name="container-insights-eks-otel-advanced-ts-cross-account"></a>

**Symptom:** After you configure multi-account collection, metrics don't appear in the central monitoring account.

**Cause:** The cross-account IAM role trust policy or permissions are incorrect.

**Solution:** Complete the following steps to resolve this issue.

1. Verify that the trust policy in the monitoring account allows the workload account to assume the role.

1. Verify that the cross-account role has the `CloudWatchAgentServerPolicy` managed policy attached.

1. Check the agent logs for `AssumeRole` errors.

   ```
   kubectl logs -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent --tail=100 | grep -i "AssumeRole\|AccessDenied"
   ```

1. Verify that the agent IAM role in the workload account has `sts:AssumeRole` permission for the cross-account role ARN.