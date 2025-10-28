# Updating the signal map of your AWS media workflow

If a change is made to your workflow, you might need to rediscover the
signal map and redeploy monitoring resources. Workflow monitor is a visualization
and monitoring tool that does not have the ability to make any changes to
your workflow. Signal maps represent a point-in-time visualization of your
workflow. In the event that you add, remove, or significantly modify parts
of your media workflow, we recommend that you rediscover the signal map. If
you have monitoring resources attached to the signal map, we recommend you
redeploy monitoring after the rediscovery process.

###### To rediscover a signal map

1. From the workflow monitor console's navigation pane, select **Signal
   maps** and select the signal map you want to work
   with.
2. Verify that you are in the **Configure signal
   map** view. For more information about changing views, see: [Viewing signal maps](monitor-with-workflow-monitor-configure-signal-maps-view.md "monitor-with-workflow-monitor-configure-signal-maps-view.md")
3. In the upper-right of the signal map page, select the
   **Actions** dropdown menu. Select
   **Rediscover**.
4. You will be presented with the rediscovery screen. Select a
   resource that is a part of the workflow you are rediscovering.
   Select the **Rediscover** button.
5. The signal map will be rebuilt according to the current workflow.
   If you need to redeploy monitoring resources, stay on this signal
   map's page. Any previously attached monitoring templates will remain
   attached, but will need to be redeployed.

###### To redeploy monitoring templates after a signal map rediscovery

1. After the rediscovery, you will be directed to the updated signal
   map. To redeploy the monitoring templates, select **Deploy
   monitor** from the **Actions**
   dropdown menu.
2. You will be asked to confirm the deployment and presented with the
   number of any CloudWatch and EventBridge resources that will be created. If you
   would like to proceed, select **Deploy**.
3. The status of the deployment is displayed next to the name of the
   signal map. After a few moments of resource creation and deployment,
   your signal map monitoring will begin.
