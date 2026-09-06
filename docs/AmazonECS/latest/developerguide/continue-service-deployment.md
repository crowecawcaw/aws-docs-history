

# Continuing service deployments
<a name="continue-service-deployment"></a>

When a pause lifecycle hook is configured for an Amazon ECS service deployment, the deployment pauses at the configured lifecycle stage and waits for an explicit action. Use the `ContinueServiceDeployment` API to either continue the deployment to the next lifecycle stage or roll back to the previous service revision.

The following action types are available:
+ `CONTINUE` - This option continues the deployment to the next lifecycle stage.
+ `ROLLBACK` - This option rolls back the service deployment to the previous service revision.

You can continue a deployment that has a pause hook in `AWAITING_ACTION` status. The deployment must be in the `IN_PROGRESS` state. For more information about service deployment states, see [View service history using Amazon ECS service deployments](service-deployment.md).

## Prerequisites
<a name="continue-service-deployment-prerequisites"></a>
+ The pause hook must be in `AWAITING_ACTION` status.
+ You need the `hookId` from the `DescribeServiceDeployments` response.

## Procedure
<a name="continue-service-deployment-procedure"></a>

------
#### [ ECS Console ]

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. In the **Services** section, choose the service.

1. Choose the **Deployments** tab.

1. Verify that the pause hook status shows **Awaiting action**.

1. Choose **Take Action**, then choose **Continue** or **Roll back**.

------
#### [ CLI ]

1. Get the `hookId` by calling `describe-service-deployments`:

   ```
   aws ecs describe-service-deployments \
       --service-deployment-arn arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28
   ```

1. Call `continue-service-deployment` with the `hookId` and the action:

   To continue the deployment:

   ```
   aws ecs continue-service-deployment \
       --hook-id ecs-pause-e7tK9G_WRJqNF_EOMjztDXfKenlJuEUVjsNStf4WLKw \
       --action CONTINUE
   ```

   To roll back the deployment:

   ```
   aws ecs continue-service-deployment \
       --hook-id ecs-pause-e7tK9G_WRJqNF_EOMjztDXfKenlJuEUVjsNStf4WLKw \
       --action ROLLBACK
   ```

   The response includes the service deployment ARN:

   ```
   {
       "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/my-cluster/my-service/EZe5RNVLH6PPzHXINuP28"
   }
   ```

------

## Next steps
<a name="continue-service-deployment-next-steps"></a>
+ Monitor the deployment progress using `DescribeServiceDeployments` or the Amazon ECS console.
+ If additional pause hooks are configured at later lifecycle stages, the deployment pauses again at those stages.