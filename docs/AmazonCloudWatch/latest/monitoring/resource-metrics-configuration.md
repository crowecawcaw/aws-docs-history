

# CloudWatch detailed monitoring for OpenTelemetry metrics
<a name="resource-metrics-configuration"></a>

Detailed monitoring gives you higher-resolution OpenTelemetry metrics for supported resources, which helps you diagnose performance issues faster. You can enable detailed monitoring for individual AWS resources through one centralized Amazon CloudWatch API, without building custom per-service infrastructure.

You identify each resource by its Amazon Resource Name (ARN). A resource can have only one configuration at a time.

## Key concepts for ResourceMetricsConfiguration
<a name="resource-metrics-configuration-concepts"></a>

Before you use ResourceMetricsConfiguration, review these terms. The terms explain how a configuration maps to a resource. They also explain which metrics CloudWatch collects by default and what happens when you update a configuration.

One configuration per resource  
Each AWS resource identified by its ARN can have at most one ResourceMetricsConfiguration. The resource ARN serves as the unique identifier for the configuration. You do not need a separate configuration ID.

Metric selections  
You can optionally specify which detailed metrics to collect by providing a `MetricSelections` list. Each selection contains an `IncludeMetrics` field with metric names. You can include between 1 and 500 metric names for each selection.

Default behavior  
When you create a configuration without specifying `MetricSelections`, CloudWatch collects all available detailed metrics for the resource. When you specify `MetricSelections`, CloudWatch collects only the listed metrics.

Full replacement on update  
When you update a configuration, the new `MetricSelections` value completely replaces the previous value. To add metrics to an existing selection, include the full list of metrics that you want to collect.

To start collecting detailed metrics for a resource, see [Enabling detailed monitoring for a resource](#resource-metrics-configuration-enable).

## Enabling detailed monitoring for a resource
<a name="resource-metrics-configuration-enable"></a>

To enable detailed monitoring for a supported resource, create a ResourceMetricsConfiguration. You can use the AWS CLI or the `AWS::CloudWatch::ResourceMetricsConfiguration` CloudFormation resource type.

**Note**  
If you attempt to create a ResourceMetricsConfiguration for a resource type that does not support detailed monitoring, the operation returns a `ValidationException`.

**To enable detailed monitoring (AWS CLI)**

1. Run the following command, replacing the placeholder ARN with the ARN of the resource that you want to monitor.

   ```
   aws cloudwatch create-resource-metrics-configuration \
       --resource-arn {{arn:aws:service:us-east-1:123456789012:resource-type/resource-id}}
   ```

1. To collect only specific metrics instead of all available detailed metrics, include the `--metric-selections` parameter.

   ```
   aws cloudwatch create-resource-metrics-configuration \
       --resource-arn {{arn:aws:service:us-east-1:123456789012:resource-type/resource-id}} \
       --metric-selections '[{"IncludeMetrics": ["{{MetricName1}}", "{{MetricName2}}"]}]'
   ```

**To enable detailed monitoring (CloudFormation)**
+ Add the `AWS::CloudWatch::ResourceMetricsConfiguration` resource type to your CloudFormation template.

  ```
  Resources:
    DetailedMonitoring:
      Type: AWS::CloudWatch::ResourceMetricsConfiguration
      Properties:
        ResourceArn: {{arn:aws:service:us-east-1:123456789012:resource-type/resource-id}}
  ```

## Checking if detailed monitoring is enabled
<a name="resource-metrics-configuration-get"></a>

To check whether detailed monitoring is enabled for a specific resource, use the `GetResourceMetricsConfiguration` operation.

**To check detailed monitoring status (AWS CLI)**

1. Run the following command for the resource that you want to check.

   ```
   aws cloudwatch get-resource-metrics-configuration \
       --resource-arn {{arn:aws:service:us-east-1:123456789012:resource-type/resource-id}}
   ```

1. If detailed monitoring is enabled, the command returns the configuration details, including any metric selections. If no configuration exists, the command returns an error.

## Updating the metric selection
<a name="resource-metrics-configuration-update"></a>

You can update an existing ResourceMetricsConfiguration to change which metrics CloudWatch collects. The update fully replaces the `MetricSelections` value.

**To update the metric selection (AWS CLI)**

1. Run the following command. Include the complete list of metrics you want to collect.

   ```
   aws cloudwatch update-resource-metrics-configuration \
       --resource-arn {{arn:aws:service:us-east-1:123456789012:resource-type/resource-id}} \
       --metric-selections '[{"IncludeMetrics": ["{{MetricName1}}", "{{MetricName2}}"]}]'
   ```

1. Verify the update by calling `GetResourceMetricsConfiguration`.

**Important**  
The `--metric-selections` parameter fully replaces the previous value. To add a metric to an existing selection, include all previously selected metrics in addition to the new metric.

## Disabling detailed monitoring
<a name="resource-metrics-configuration-disable"></a>

To disable detailed monitoring for a resource, delete its ResourceMetricsConfiguration. After you delete the configuration, CloudWatch stops collecting detailed metrics for that resource.

**To disable detailed monitoring (AWS CLI)**

1. Run the following command for the resource that you no longer want to monitor.

   ```
   aws cloudwatch delete-resource-metrics-configuration \
       --resource-arn {{arn:aws:service:us-east-1:123456789012:resource-type/resource-id}}
   ```

1. Verify that the configuration was deleted by calling `GetResourceMetricsConfiguration`. The command returns an error if no configuration exists.

## Required IAM permissions for ResourceMetricsConfiguration
<a name="resource-metrics-configuration-permissions"></a>

Ensure your IAM policy includes the actions for the operations you use.


| Operation | Required IAM action | 
| --- | --- | 
| Create a configuration | `cloudwatch:CreateResourceMetricsConfiguration` | 
| Get a configuration | `cloudwatch:GetResourceMetricsConfiguration` | 
| Update a configuration | `cloudwatch:UpdateResourceMetricsConfiguration` | 
| Delete a configuration | `cloudwatch:DeleteResourceMetricsConfiguration` | 

The following example IAM policy grants permissions for all ResourceMetricsConfiguration operations, scoped to a single resource with the `cloudwatch:ResourceArn` condition key.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:CreateResourceMetricsConfiguration",
                "cloudwatch:GetResourceMetricsConfiguration",
                "cloudwatch:UpdateResourceMetricsConfiguration",
                "cloudwatch:DeleteResourceMetricsConfiguration"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:ResourceArn": "arn:aws:service:us-east-1:123456789012:resource-type/resource-id"
                }
            }
        }
    ]
}
```

**Note**  
The ResourceMetricsConfiguration APIs do not support resource-level permissions. You must use `"Resource": "*"` in your IAM policy and scope access with the `cloudwatch:ResourceArn` condition key, as shown in the preceding example.

For more information about `cloudwatch:ResourceArn`, including how to match multiple resources with wildcards, see [Condition keys for resource metrics configuration access](iam-cw-condition-keys-resource-arn.md).