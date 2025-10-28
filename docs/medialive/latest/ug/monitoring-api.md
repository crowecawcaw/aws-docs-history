# Monitoring alerts using the AWS SDKs or API

You can use your preferred AWS SDK or API to monitor alerts about channel activity,
multiplex activity, and activity on the nodes in an AWS Elemental MediaLive Anywhere cluster.

There is an operation for each resource:

- `ListAlerts` for a specific channel, with optional state
  (SET or CLEARED) filter. The response includes information about the alert, the
  alert status, and the applicable pipeline.
- `ListMultiplexAlerts` for a specific multiplex, with
  optional state (SET or CLEARED) filter. The response includes information about the
  alert, the alert status, and the applicable pipeline.
- `ListClusterAlerts`, for a specific cluster, with an
  optional state (SET or CLEARED) filter. The response includes information about the
  alert, the alert status, and the node and channel that the alert applies to.
  You can query for alerts from when the alert is first set until the alert has been in a
  CLEARED state for approximately 5 minutes.

## Tips for ListAlerts and

ListMultiplexAlerts

The information in the response for channels and multiplexes is the
following:

- Alert type: A short description, usually 3 to 4 words.
- Messages: A long description.
- ID: The ID is created when the alert is first set. Note the
  following:
  - The ID is a hash of a monotonically increasing count.
  - Each channel (or multiplex) has its own ID series that increments
    independently of other series.

  This means that two channels might each have an alert with the
  same ID during the same time period, especially if the channels
  start at close to the same time. Therefore in your code, you should
  assign a unique identity to each alert by combining the channel ID
  and alert ID.
  - The rollover of IDs for one channel (or multiplex) is reset each
    time the channel (or multiplex) restarts. Keep this in mind when
    performing a query.

## Tips for ListClusterAlerts

The information in the response for clusters is the following:

- Alert type: `CLUSTER_NODE_HEALTH` for every type of alert.
- Message: A long description, which might include variables that resolve
  differently in each cluster or in each instance of an alert.
- ID: A long description that is often equivalent to the message.
