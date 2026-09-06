

# Getting started with workflow monitor
<a name="monitor-with-workflow-monitor-configure-getting-started"></a>

The following steps provide a basic overview of using workflow monitor for the first time. 

1. Setup workflow monitor IAM permissions for administrator and operator level roles: [Workflow monitor IAM policies](monitor-with-workflow-monitor-configure-getting-started-IAM.md) 

1. Build alarm templates or import predefined templates created by AWS: [CloudWatch alarms](monitor-with-workflow-monitor-configure-alarms.md)

1. Build notification events that will be delivered by EventBridge: [EventBridge rules ](monitor-with-workflow-monitor-configure-notifications.md)

1. Discover signal maps using your existing AWS Elemental resources: [Signal maps ](monitor-with-workflow-monitor-configure-signal-maps.md)

1. Attach the alarm templates and notification rules to your signal map: [Attaching templates](monitor-with-workflow-monitor-configure-signal-maps-attach.md)

1. Deploy the templates to begin monitoring the signal map: [Deploying monitoring templates](monitor-with-workflow-monitor-configure-deploy.md)

1. Monitor and review your workflow monitor resources using the overview section of the AWS console: [Overview](monitor-with-workflow-monitor-operate-overview.md)

![The individual steps of setting up workflow monitor. Begin by creating the IAM roles. Next, create templates for alarms and events. Next, discover a signal map and attach your templates to the map. After a signal map has templates attached, the templates must be deployed. The final step is monitoring using the templates and overview resources.](http://docs.aws.amazon.com/medialive/latest/ug/images/workflowmonitor-overview-steps.png)
