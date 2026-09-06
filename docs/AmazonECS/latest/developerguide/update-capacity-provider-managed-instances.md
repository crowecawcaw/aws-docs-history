

# Updating Amazon ECS Managed Instances monitoring
<a name="update-capacity-provider-managed-instances"></a>

You can modify the monitoring option for your Amazon ECS Managed Instances capacity provider to change between basic and detailed monitoring. This allows you to adjust the level of monitoring data collected without recreating the capacity provider.

For more information about monitoring options, see [Monitoring Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-managed-instances.html).

## Console procedure
<a name="update-capacity-provider-managed-instances-console"></a>

**To update monitoring for Amazon ECS Managed Instances (Amazon ECS console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. From the navigation bar, select the Region to use.

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose your cluster name.

1. On the cluster page, choose the **Infrastructure** tab.

1. Under **Advanced configuration**, choose one of the following monitoring options:
   + To have CloudWatch send status-check metrics, choose **Basic**.
   + To have CloudWatch send all metrics metrics, choose **Detailed**.

1. Choose **Update**.

To update tags associated with an existing Amazon ECS Managed Instances capacity provider, follow these steps:

1. In the navigation pane, choose **Clusters**.

1. On the clusters page, choose **Infrastructure**.

1. On the infrastructure page, choose the capacity provider that you created.

1. On the capacity provider page, choose **Tags**.

1. Under **Tags**, choose **Manage tags**.

1. To add a tag, specify the key and value of the tag that you want to add and then choose **Save**. To add multiple tags at once, choose **Add tag** for each tag that you want to add. You can add a maximum of 50 tags.

   To remove a tag, choose **Remove**.
**Note**  
If tag propagation is enabled, tags added or removed after capacity provider creation don't apply to resources previously created by the capacity provider.

## AWS CLI procedure
<a name="update-capacity-provider-managed-instances-cli"></a>

You can update a capacity provider for Amazon ECS Managed Instances using the AWS CLI. Use the latest version of the AWS CLI. For more information on how to upgrade to the latest version, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**To update monitoring for Amazon ECS Managed Instances (AWS CLI)**

1. To enable detailed monitoring, use the following command:

   ```
   aws ecs update-capacity-provider \
       --name {{my-managed-instances-provider}} \
       --managed-instances-provider '{
           "instanceLaunchTemplateUpdate": {
               "monitoring": "DETAILED"
           }
       }'
   ```

1. To enable basic monitoring, use the following command:

   ```
   aws ecs update-capacity-provider \
       --name {{my-managed-instances-provider}} \
       --managed-instances-provider '{
           "instanceLaunchTemplateUpdate": {
               "monitoring": "BASIC"
           }
       }'
   ```