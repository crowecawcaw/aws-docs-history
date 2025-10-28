# Getting

started with workflow monitor

The following steps provide a basic overview of using workflow monitor for the first time.

1. Setup workflow monitor IAM permissions for administrator and operator level roles: [Workflow monitor IAM policies](monitor-with-workflow-monitor-configure-getting-started-IAM.md "monitor-with-workflow-monitor-configure-getting-started-IAM.md")
2. Build alarm templates or import predefined templates created by AWS:
   [CloudWatch
   alarms](monitor-with-workflow-monitor-configure-alarms.md "monitor-with-workflow-monitor-configure-alarms.md")
3. Build notification events that will be delivered by EventBridge: [EventBridge rules](monitor-with-workflow-monitor-configure-notifications.md "monitor-with-workflow-monitor-configure-notifications.md")
4. Discover signal maps using your existing AWS Elemental resources: [Signal maps](monitor-with-workflow-monitor-configure-signal-maps.md "monitor-with-workflow-monitor-configure-signal-maps.md")
5. Attach the alarm templates and notification rules to your signal map:
   [Attaching
   templates](monitor-with-workflow-monitor-configure-signal-maps-attach.md "monitor-with-workflow-monitor-configure-signal-maps-attach.md")
6. Deploy the templates to begin monitoring the signal map: [Deploying monitoring templates](monitor-with-workflow-monitor-configure-deploy.md "monitor-with-workflow-monitor-configure-deploy.md")
7. Monitor and review your workflow monitor resources using the overview section of the
   AWS console: [Overview](monitor-with-workflow-monitor-operate-overview.md "monitor-with-workflow-monitor-operate-overview.md")

![The individual steps of setting up workflow monitor. Begin by creating the IAM roles. Next, create templates for alarms and events. Next, discover a signal map and attach your templates to the map. After a signal map has templates attached, the templates must be deployed. The final step is monitoring using the templates and overview resources.](images/workflowmonitor-overview-steps.png)
