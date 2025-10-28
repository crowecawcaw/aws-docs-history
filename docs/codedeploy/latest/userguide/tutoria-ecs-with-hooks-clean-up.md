# Step 7: Clean up

When you have finished this tutorial, clean up the resources associated with it to avoid
incurring charges for resources that you aren't using. The resource names in this step are the
names suggested in this tutorial (for example, `ecs-demo-codedeploy-app`
for the name of your CodeDeploy application). If you used different names, then be sure to use
those in your cleanup.

###### To clean up the tutorial resources

1. Use the [delete-deployment-group](../../../cli/latest/reference/deploy/delete-deployment-group.md "../../../cli/latest/reference/deploy/delete-deployment-group.md") command to delete the CodeDeploy deployment group.

```
`aws deploy delete-deployment-group --application-name `ecs-demo-deployment-group` --deployment-group-name `ecs-demo-dg` --region `aws-region-id``
```

2. Use the [delete-application](../../../cli/latest/reference/deploy/delete-application.md "../../../cli/latest/reference/deploy/delete-application.md") command to delete the CodeDeploy application.

```
`aws deploy delete-application --application-name `ecs-demo-deployment-group` --region `aws-region-id``
```

3. Use the [delete-function](../../../cli/latest/reference/lambda/delete-function.md "../../../cli/latest/reference/lambda/delete-function.md")
   command to delete your Lambda hook function.

```
`aws lambda delete-function --function-name `AfterAllowTestTraffic``
```

4. Use the [delete-log-group](../../../cli/latest/reference/logs/delete-log-group.md "../../../cli/latest/reference/logs/delete-log-group.md")
   command to delete your CloudWatch log group.

```
`aws logs delete-log-group --log-group-name `/aws/lambda/AfterAllowTestTraffic``
```
