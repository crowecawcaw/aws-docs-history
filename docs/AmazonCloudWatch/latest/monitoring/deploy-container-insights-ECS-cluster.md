# Setting up Container Insights on

Amazon ECS

You can set up Container Insights with enhanced observability or Container Insights on
new and existing Amazon ECS clusters using either the Amazon ECS console or the AWS CLI. Container
Insights collects metrics at the cluster, task, and service levels. Container Insights
with enhanced observability provides additional dimensions and metrics, allowing you to
deep dive down to container level visibility.

If you're using Amazon ECS on an Amazon EC2 instance, launch that instance using an AMI that
includes Amazon ECS agent version 1.29 or later. For information about updating your agent
version, see [Updating the Amazon ECS Container
Agent](../../../AmazonECS/latest/developerguide/ecs-agent-update.md "../../../AmazonECS/latest/developerguide/ecs-agent-update.md").

###### Note

If the customer managed AWS KMS key that you use for your Amazon ECS Container Insights
metrics is not already configured to work with CloudWatch, you must update the key policy to
allow for encrypted logs in CloudWatch Logs. You must also associate your own AWS KMS key with the
log group in
`/aws/ecs/containerinsights/`ClusterName`/performance`.
For more information, see [Encrypt log data in CloudWatch Logs
using AWS Key Management Service](../logs/encrypt-log-data-kms.md "../logs/encrypt-log-data-kms.md").

We recommend that you use Container Insights with enhanced observability instead of
Container Insights as it provides detailed visibility in your container environment,
reducing the mean time to resolution.

## Set up Container Insights

with enhanced observability

You can turn on Container Insights with enhanced observability using the Amazon ECS
console or AWS CLI.

AWS CLI
Use the following command to turn on Container Insights with enhanced
observability.

Set the `containerInsights` account setting to
`enhanced`

```
aws ecs put-account-setting --name containerInsights --value enhanced
```

Example output

```
{
    "setting": {
        "name": "containerInsights",
        "value": "enhanced",
        "principalArn": "arn:aws:iam::123456789012:johndoe",
         "type": user
    }
}
```

###### Note

By default, the `put-account-setting` applies only to the
currently authenticated user. To enable the setting account-wide for all users
and roles, use the root user as in the following example.

```
aws ecs put-account-setting --name containerInsights --value enhanced --principal-arn arn:aws:iam::`accountID`:root
```

After you set this account setting, all new clusters automatically use
Container Insights with enhanced observability. Use the
`update-cluster-settings` command to add Container Insights with
enhanced observability to existing cluster, or to upgrade clusters that currently
use Container Insights to Container Insights with enhanced observability.

```
aws ecs update-cluster-settings --cluster `cluster-name` --settings name=containerInsights,value=enhanced
```

Amazon ECS console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation bar at the top, select the Region for which to view your
   account settings.
3. In the navigation page, choose **Account
   Settings**.
4. Choose **Update**.
5. To use Container Insights with enhanced observability, choose
   **Container Insights with enhanced observability**.
6. Choose **Save changes**.
7. On the confirmation screen, choose **Confirm** to save
   the selection.

After you set this, all new clusters automatically use Container Insights with
enhanced observability. You can add Container Insights with enhanced observability
to existing clusters, or update clusters that currently use Container Insights to
Container Insights with enhanced observability. For more information, see [Updating an Amazon ECS
cluster](../../../AmazonECS/latest/developerguide/update-cluster-v2.md "../../../AmazonECS/latest/developerguide/update-cluster-v2.md") in the _Amazon Elastic Container Service Developer
Guide_.

## Set up Container Insights

You can turn on Container Insights using the Amazon ECS console or AWS CLI.

AWS CLI
To use Container Insights, set the `container Insights` account
setting to `enabled`. Use the following command to turn on Container
Insights.

```
aws ecs put-account-setting --name containerInsights --value enabled
```

Example output

```
{
    "setting": {
        "name": "container Insights",
        "value": "enabled",
        "principalArn": "arn:aws:iam::123456789012:johndoe",
         "type": user
    }
}
```

When you set the `container Insights` account setting to
`enabled`, all new clusters have Container Insights enabled by
default. Use the `update-cluster-settings` command to add Container
Insights to an existing cluster.

```
aws ecs update-cluster-settings --cluster `cluster-name` --settings name=containerInsights,value=enabled
```

Amazon ECS console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation bar at the top, select the Region for which to view your
   account settings.
3. In the navigation page, choose **Account
   Settings**.
4. Choose **Update**.
5. To use Container Insights, choose **Container
   Insights**.
6. Choose **Save changes**.
7. On the confirmation screen, choose **Confirm** to save
   the selection.

After you set this, all new clusters automatically use Container Insights.
Update existing clusters to add Container Insights. For more information, see
[Updating an Amazon ECS
cluster](../../../AmazonECS/latest/developerguide/update-cluster-v2.md "../../../AmazonECS/latest/developerguide/update-cluster-v2.md") in the _Amazon Elastic Container Service Developer
Guide_.
