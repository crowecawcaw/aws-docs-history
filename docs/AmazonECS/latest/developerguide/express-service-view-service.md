# Viewing the details of an Amazon ECS Express Mode service

You can view details about your Express Mode service to monitor its status, configuration, and
performance metrics. The service details page provides comprehensive information about your
service's current state, running tasks, deployment history, and operational metrics.

###### To view an Express Mode service (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the name of the cluster that
   contains your Express Mode service.
4. On the cluster details page, choose the **Services** tab.
5. Configure a filter to view your Express Mode services. For **Filter resource
   management type**, choose **ECS**.

An Express Mode service has a **Express** badge next to the
name. 6. Select the name of your Express Mode service to navigate to the service detail page for your Express Mode service. 7. Review the service information displayed on the service details page:

    1. **Express service Overview** - View basic service information including Application URL,
     Service status, Pending and Running Tasks, and Active Deployments.
    2. **Observability** - View CloudWatch metrics for CPU Utilization (min, max, average)
     Memory Utilization (min, max, average), Target Response time (p50,p90,p99), RequestCount, 4xx Statuses and 5xx Statuses.
    3. **Logs** - View logs from the containers in your tasks.
    4. **Resources** - Your AWS Resources created for your Express Mode service. The Timeline view updates
     automatically after a Create or Update and shows status and events. The Table view provides a searchable table with the status
     and full ARNs for each resource.
    5. **Deployments** - Track deployment history and current deployment status, include the service revision and
     tasks which provide valuable information during updates. The events panel lets you know when your Express Mode service has reached a steady state.
    6. **Configuration** - View service configuration, including the cluster, roles, container configuration, compute, auto scaling and
     networking configuration.
    7. **Tags** - Manage your tags.
