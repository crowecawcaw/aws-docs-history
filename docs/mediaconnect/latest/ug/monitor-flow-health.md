# Monitoring the health of a MediaConnect flow

The **Alerts** tab on the MediaConnect console displays a list of alerts
that occurred when you started or stopped the current flow. For the full list of
alerts for a flow, see Amazon CloudWatch.

MediaConnect displays the following alerts on the **Alerts** tab:

- Contextual error messages about your flow, called [stream
  errors](#monitor-flow-health-stream-alerts "#monitor-flow-health-stream-alerts").
- The entitlement that this flow is based on is already in use. This occurs
  if you create more than one flow based on the same entitlement. If the one
  of those flows is already running, MediaConnect displays an alert if you try to
  start the second flow.
- The entitlement that this flow is based on no longer exists. This occurs
  if the account that granted the entitlement (the content originator) revokes
  the entitlement.
- The entitlement that this flow is based on does not have an active source.
  This occurs if the originator's flow is deleted or stopped. When you start
  your flow based on that entitlement, there is no content coming from the
  originator's flow.
- The decryption or encryption information for the flow isn't valid. This
  can happen for a number of reasons. For example, the decryption key doesn't
  match the type for the specified algorithm. Or, your flow is based on an
  entitlement that uses SPEKE encryption and MediaConnect can't contact the
  conditional access (CA) platform key provider.
- Your flow is based on an entitlement, and the content originator's flow
  already has the maximum number of outputs.

## Stream errors

MediaConnect **Alerts** can also contain contextual errors for the
flow's sources and outputs. These are called _stream
errors_ and follow a specific format.

- Source `source name` Stream Error:
  `error message`. Please investigate the
  flow source.
- Output `output name` Stream Error:
  `error message`. Please investigate the
  flow output.

The error message will provide more context for the issue and you can use it
as an indicator of where to begin troubleshooting.

**Example**

If you received the following alert on a flow named _NationalBroadcast_:

Source `StudioFeed2` Stream Error: `CDI
 Configuration Error`. Please investigate the flow
source.

This would indicate an error with the inbound CDI at the source. Specifically,
your next step should be to verify the settings for the _StudioFeed2_ source on the flow named _NationalBroadcast_. You would need to pay special attention to
the CDI-specific source settings such as the **inbound port**,
the **VPC interface** being used, and the **media
streams**.

## Viewing flow alerts

###### To view any active alerts (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the
   flow.
3. Choose the **Alerts** tab.

The service displays a list of alerts, if there are any, on the
flow.
