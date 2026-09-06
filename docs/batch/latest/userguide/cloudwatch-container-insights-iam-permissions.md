

# IAM permissions for Container Insights
<a name="cloudwatch-container-insights-iam-permissions"></a>

To enable or change Container Insights on a compute environment, AWS Batch requires the `ecs:UpdateCluster` permission. How you provide this permission depends on your compute environment's service role configuration.

Using the AWS Batch service-linked role (recommended)  
If your compute environment uses the *AWSServiceRoleForBatch* service-linked role, the `ecs:UpdateCluster` permission is included automatically. No action is required.  
For more information, see [Using service-linked roles for AWS Batch](using-service-linked-roles.md).

Using a custom service role  
If your compute environment uses a custom service role, you must add the `ecs:UpdateCluster` permission to that role. Without this permission, updating Container Insights settings causes the compute environment to go to an `INVALID` state.  
Add the following statement to your custom service role's policy:  

```
{
    "Effect": "Allow",
    "Action": "ecs:UpdateCluster",
    "Resource": "arn:aws:ecs:*:*:cluster/*"
}
```

**Note**  
If updating Container Insights fails because of missing permissions, the compute environment status changes to `INVALID` with a status reason explaining the error. After you correct the permissions, submit any `UpdateComputeEnvironment` request to trigger a retry. AWS Batch automatically reconciles the Container Insights setting on the next update workflow.