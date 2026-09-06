

# Viewing Amazon ECS service and task state change events
<a name="viewing-state-events"></a>

The Amazon ECS console provides event capture functionality that stores Amazon ECS-generated events, such as service actions and task state changes, to Amazon CloudWatch Logs through EventBridge. This feature includes a query interface with filtering capabilities to enhance monitoring and troubleshooting.

Events provide detailed information about how your service deployments, services, tasks, and instances operate. You can use this information to troubleshoot task or service deployment failures.

You can use any of the following criteria to filter the events:
+  Deployment ID (This is only available on the service detail page) 
+ Start time
+ End time 
+ Service name (only applicable on cluster detail page, on service detail page, this will be default to current service) 
+ Task ID 
+ Task Last status 
+ Task definition family 
+ Task definition revision 

## Viewing events at the cluster-level
<a name="view-cluster-procedure"></a>

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. Choose **Clusters**.

   The clusters list page displays.

1. Choose the cluster.

   The cluster details page displays.

1. Under **History**, determine the events to view.

   1. To view service action events, choose **Service action events**.

   1. To view task state change events, choose **Task state change events**.

   1. (Optional) In **Query criteria**, enter the filters for the events that you want to view.

1. Choose **Run query**.

   The events display in a list.

1. To view the full details of the event, choose the event.

## Viewing at the service-level
<a name="tasks-procedure"></a>

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster details page, in the **Services** section, choose the service.

   The service details page displays.

1. Under **History**, determine the events to view.

   1. To view service action events, choose **Service action events**.

   1. To view task state change events, choose **Task state change events**.

   1. (Optional) In **Query criteria**, enter the filters for the events that you want to view.

1. Choose **Run query**.

   The events display in a list.

1. To view the full details of the event, choose the event.