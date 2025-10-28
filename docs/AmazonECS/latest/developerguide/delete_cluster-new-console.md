# Deleting an Amazon ECS cluster

If you are finished using a cluster, you can delete it. After you delete the cluster, it
transitions to the `INACTIVE` state. Clusters with an `INACTIVE`
status may remain discoverable in your account for a period of time. However, this behavior
is subject to change in the future, so you should not rely on `INACTIVE` clusters
persisting.

Before you delete a cluster, you must perform the following operations:

- Delete all services in the cluster. For more information, see [Deleting an Amazon ECS service using the console](delete-service-v2.md "delete-service-v2.md").
- Stop all currently running tasks. For more information, see [Stopping an Amazon ECS task](standalone-task-stop.md "standalone-task-stop.md").
- Deregister all registered container instances in the cluster. For more
  information, see [Deregistering an Amazon ECS container
  instance](deregister_container_instance.md "deregister_container_instance.md").
- Delete the namespace. For more information, see [Deleting namespaces](../../../cloud-map/latest/dg/deleting-namespaces.md "../../../cloud-map/latest/dg/deleting-namespaces.md")
  in the _AWS Cloud Map Developer Guide_.

###### Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, select the cluster to delete.
5. In the upper-right of the page, choose **Delete Cluster**.

A message is displayed when you did not delete all the resources associated with
the cluster. 6. In the confirmation box, enter **delete `cluster
 name`**.
