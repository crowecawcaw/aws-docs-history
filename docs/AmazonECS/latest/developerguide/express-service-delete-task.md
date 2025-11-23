# Delete Amazon ECS Express Mode services

When you delete an Express Mode service, you remove the service and delete its associated resources including the cluster, load balancer, and other infrastructure components.

###### Important

Deleting an Express Mode service will stop all running tasks and make your application unavailable. This action cannot be undone.

The following resources may be deleted depending on your selection:

- The Amazon ECS cluster (if no other services are running)
- The Amazon ECS service, task definition, and any running tasks
- Service security group
- CloudWatch log group
- Metric alarm
- ACM Certificate
- The Application Load Balancer (if no other services are configured), target group, security group, listener, and listener rule
- Amazon EC2 Auto Scaling policy, scalable target
  Consider the following::

- Ensure you have backed up any important data before deletion
- Consider scaling the service to zero tasks before deletion to gracefully stop traffic
- Review dependencies that might be affected by the deletion

## Difference between deleting an Express Mode service and a service

When you delete a service, Amazon ECS will delete the service if there are no running tasks. Amazon ECS does not delete target groups associated
with the service or the default cluster (if it was used). When you delete an Express Mode service, Amazon ECS will delete the service as well as any
resources that are distinct to the Express Mode service service. For example, if the Express Mode service service created the load balancer and is the
only service using the load balancer it will delete the associated load balancer. If the load balancer is being shared, even with resources not
managed by Express Mode, it will not be deleted.

## Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, select the cluster for the
   service.
3. On the **Clusters** page, choose the cluster.
4. Choose the **Services** tab.
5. Select the services to delete.
6. Choose **Delete**.
7. In the **Delete confirmation** dialog box:
   1. Enter `delete` to confirm the deletion.

8. Choose **Delete** to confirm.
9. Stay on the page to monitor deletion progress and view a list of resources that have been removed, as well as those that have been retained and may require manual cleanup.
