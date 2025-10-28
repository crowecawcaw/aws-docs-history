# Deleting an Amazon ECS service using the console

The following are some of the reasons you would delete a service:

- The application is no longer needed
- You are migrating the service to a new environment
- The application is not actively being used
- The application is using more resources than needed and you are trying to optmize
  your costs
  The service is automatically scaled down to zero before it is deleted. Load balancer
  resources or service discovery resources associated with the service are not affected by
  the service deletion. To delete your Elastic Load Balancing resources, see one of the following topics,
  depending on your load balancer type: [Delete an Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-delete.md "../../../elasticloadbalancing/latest/application/load-balancer-delete.md") or [Delete a Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-delete.md "../../../elasticloadbalancing/latest/network/load-balancer-delete.md").

When you delete a service, Amazon ECS deletes all service deployments and service revisions for
the service.

When you delete a service, if there are still running tasks that require cleanup, the
service status moves from `ACTIVE` to `DRAINING`, and the service is
no longer visible in the console or in the `ListServices` API operation. After
all tasks have transitioned to either `STOPPING` or `STOPPED` status,
the service status moves from `DRAINING` to `INACTIVE`. Services in
the `DRAINING` or `INACTIVE` status can still be viewed with the
`DescribeServices` API operation.

###### Important

If you attempt to create a new service with the same name as an existing service
in either `ACTIVE` or `DRAINING` status, you'll receive an
error.

###### Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, select the cluster for
   the service.
3. On the **Clusters** page, choose the
   cluster.
4. On the **Cluster :
   `name`** page, choose the
   **Services** tab.
5. Select the services, and then choose **Delete**.
6. To delete a service even if it wasn't scaled down to zero tasks, select
   **Force delete service**.
7. At the confirmation prompt, enter **delete**, and
   then choose **Delete**.
