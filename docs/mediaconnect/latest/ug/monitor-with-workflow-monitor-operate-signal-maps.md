# Using workflow monitor

signal maps

From the **overview** section of the console, you can select
a specific signal map to view more information about that signal map and its
attached monitoring resources.

After selecting a signal map, you will be presented with the signal map and a
number of tabbed section containing more information:

- CloudWatch alarms
- EventBridge rules
- AWS Elemental alerts
- Metrics
- Logs
- Basic details
  **Navigating the signal map**

A signal map will contain nodes for every supported AWS resource discovered by
workflow monitor. Certain resources, such as MediaLive channels and MediaPackage endpoints can
display thumbnail previews of the content, if thumbnail previews are available.

Selecting a resource node, and selecting **View selected resource
details** from the **Actions** dropdown menu will
take you to the associated service's details page. For example, selecting a
MediaLive channel and selecting **View selected resource details**
will open the MediaLive console's details page for that channel.

Selecting a resource node will filter the list of active alarms to only that
node. If you select the resource's **Target ARN** in the active
alarm, you will be taken to the associated service's details page, with the
selected resource open.
