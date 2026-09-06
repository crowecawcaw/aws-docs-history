

# Deleting an Amazon ECS cluster
<a name="delete_cluster-new-console"></a>

If you are finished using a cluster, you can delete it. After you delete the cluster, it transitions to the `INACTIVE` state. Clusters with an `INACTIVE` status may remain discoverable in your account for a period of time. However, this behavior is subject to change in the future, so you should not rely on `INACTIVE` clusters persisting.

Before you delete a cluster, you must perform the following operations:
+ Delete all services in the cluster. For more information, see [Deleting an Amazon ECS service using the console](delete-service-v2.md).
+ Stop all currently running tasks. For more information, see [Stopping an Amazon ECS task](standalone-task-stop.md).
+ Deregister all registered container instances in the cluster. For more information, see [Deregistering an Amazon ECS container instance](deregister_container_instance.md).
+ Delete the namespace. For more information, see [Deleting namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/deleting-namespaces.html) in the *AWS Cloud Map Developer Guide*.

**Procedure**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. From the navigation bar, select the Region to use.

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, select the cluster to delete.

1. Choose **Delete Cluster**. 

   A message is displayed when you did not delete all the resources associated with the cluster.

1. In the confirmation box, enter **delete {{cluster name}}**.