# Stopping Amazon ECS service deployments

You can manually stop a deployment when a failing deployment was not detected by the
circuit breaker or CloudWatch alarms. The following stop types are available:

- Rollback - This option rolls back the service deployment to the previous service
  revision.

You can use this option even if you didn't configure the service deployment for
the rollback option.
You can stop a deployment that is in any of the following states. For more information
about service deployment states, see [View service history using Amazon ECS service deployments](service-deployment.md "service-deployment.md").

- PENDING - The service deployment moves to the ROLLBACK_REQUESTED state, and then
  the rollback operation starts.
- IN_PROGRESS - The service deployment moves to the ROLLBACK_REQUESTED state, and
  then the rollback operation starts.
- STOP_REQUESTED - The service deployment continues to stop.
- ROLLBACK_REQUESTED - The service deployment continues the rollback
  operation.
- ROLLBACK_IN_PROGRESS - The service deployment continues the rollback
  operation.

## Procedure

Before you begin, configure the required permissions for viewing service deployments. For
more information, see [Permissions required for viewing Amazon ECS service deployments](service-deployment-permissions.md "service-deployment-permissions.md").

Amazon ECS Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster.
3. On the cluster details page, in the **Services** section, choose
   the service.

The service details page displays. 4. On the service details page, choose
**Deployments**.

The deployments page displays. 5. Under **Ongoing deployment**, choose
**Roll back**. Then, in the confirmation
window, choose **Roll back**.

AWS CLI

1. Run `list-service-deployments` to retrieve the service deployment ARN.

Replace the `user-input` with your
values.

```
aws ecs list-service-deployments --cluster `cluster-name` --service `service-name`
```

Note the `serviceDeploymentArn` for the deployment you want
to stop.

```
{
    "serviceDeployments": [
        {
            "serviceDeploymentArn": "arn:aws:ecs:us-west-2:123456789012:service-deployment/cluster-name/service-name/NCWGC2ZR-taawPAYrIaU5",
            "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/cluster-name/service-name",
            "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/cluster-name",
            "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123456789012:service-revision/cluster-name/service-name/4980306466373577095",
            "status": "SUCCESSFUL"
        }
    ]
}

```

2. Run `stop-service-deployments`. Use the `serviceDeploymentArn` that was
   returned from `list-service-deployments`.

Replace the `user-input` with your
values.

```
aws ecs stop-service-deployment --service-deployment-arn arn:aws:ecs:`region`:`123456789012`:service-deployment/`cluster-name`/`service-name`/`NCWGC2ZR-taawPAYrIaU5` --stop-type ROLLBACK
```

## Next steps

Decide what changes need to be made to the service, and then update the service. For
more information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").
