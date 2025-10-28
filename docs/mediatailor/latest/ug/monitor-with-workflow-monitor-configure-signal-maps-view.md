# Viewing signal maps of AWS media workflows

Workflow monitor signal maps allow you to see a visual mapping of all connected AWS resources in your media workflow.

**Signal map views**

After selecting a signal map, you have two views that can be used to
monitor or configure the signal map. **Monitor signal map**
and **Configure signal map** is a context-sensitive button
found in the upper-right of the signal map console section.

If you select the signal map using the **Signal maps**
section of the navigation pane, your signal map will be displayed in the
configuration view. The configuration view allows you to make changes to the
template groups attached to this signal map, deploy the attached templates,
and view the basic details and tags of the signal map.

If you select the signal map using the **Overview**
section of the navigation pane, your signal map will be displayed in
monitoring view. The monitoring view displays the CloudWatch alarms, EventBridge rules,
alerts, logs, and metrics for this signal map.

The view can be changed at any time by selecting the
**Monitor/Configure signal map** button in the
upper-right. The configuration view requires administrator-level IAM
permissions. Required IAM permissions can be viewed here: [Workflow monitor IAM policies](monitor-with-workflow-monitor-configure-getting-started-IAM.md "monitor-with-workflow-monitor-configure-getting-started-IAM.md")

**Navigating the signal map**

A signal map will contain nodes for every supported AWS resource
discovered by workflow monitor. Certain resources, such as MediaLive channels and MediaPackage
endpoints can display thumbnail previews of the content, if thumbnail previews are
available.

Selecting a resource node, and selecting **View selected resource
details** from the **Actions** dropdown menu
will take you to the associated service's details page. For example,
selecting a MediaLive channel and selecting **View selected resource
details** will open the MediaLive console's details page for that
channel.

Selecting a resource node will filter the list of active alarms to only
that node. If you select the resource's **Target ARN** in
the active alarm, you will be taken to the associated service's details
page, with the selected resource open.
