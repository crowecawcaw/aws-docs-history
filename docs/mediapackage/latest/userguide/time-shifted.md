# Time-shifted viewing with AWS Elemental MediaPackage

Time-shifted viewing is available with live workflows in AWS Elemental MediaPackage.

_Time-shifted viewing_ means that viewers can start watching a live stream
at a time earlier than "now," permitting them to join from the beginning a show that's already in
progress or to watch a show that's already completed. Time-shifted viewing effectively makes live
events available for viewing on demand. MediaPackage supports time-shifted viewing for content that's up
to 336 hours (14 days) old. You can enable time-shifted viewing for some or all of this content by
defining the **startover window** on the endpoint. Manifests from within the
startover window can be time shifted.

The following steps describe time-shift options and how to set them up. In these steps, "now"
is determined either by the program date time (PDT) present in the source content from the encoder
or, if this PDT information is not included, by the MediaPackage ingest time of the most recent
segment.

###### Important

When using time-shifted viewing, we recommend using consistent playback windows across
player sessions, rather than generating a unique start or end time for each viewer. This yields
better caching at the CDN, and will avoid running into potential throttling related to those
requests, on the MediaPackage level.

## Step 1: Set the startover window

To create time-shifted manifests, you must define the live content that will be made
available to view on demand. In MediaPackage, this eligible content is identified in your startover
window. The startover window can be up to 24 hours long. You can set the window on the endpoint
object, either through the MediaPackage console or MediaPackage API.

You might notice that the manifest lags behind real time when you initially create a
startover window on an endpoint. This is because MediaPackage starts filling the manifest from the start
of the window, and works up to "now." So, if you have a 24-hour startover window, MediaPackage fills the
manifest starting 24 hours ago and working up to "now."

## Step 2: Choose time-shifted options

You can apply time-shifted options to all manifests that originate from a MediaPackage endpoint by
configuring the option on the endpoint. Alternatively, you can apply these options dynamically at
the time of the content playback request by including query parameters.

You can choose from the following time-shifted options:

- Delay content availability: Set a delay for availability of live content.
- Define a manifest start and end: Set the time blocks of content are available from within
  the startover window. These blocks are defined by times provided in the start and end
  parameters.
- Limit a manifest duration : blocks of content with the specified duration are available
  within the startover window. The blocks are defined by the duration (in seconds) of the content
  and can come from different places in the startover window.

To use time shifting on all manifests that originate from an endpoint, set the filter
configuration in the manifest settings of the endpoint. For more information, see [Manifest fields](endpoints-create.md#endpoints-manifest "endpoints-create.md#endpoints-manifest").

To use time shifting dynamically across requests, append query parameters to playback
requests. For more information, see [Time-shifted query
parameters](msettings-params.md "msettings-params.md").

Learn more about these options in the following topics.

###### Topics

- [Time-shifted query
  parameters](msettings-params.md "msettings-params.md")
- [Time delay](time-delay.md "time-delay.md")
- [Start and end parameters](start-and-end-parameters-rules.md "start-and-end-parameters-rules.md")
- [Window duration](window-seconds.md "window-seconds.md")
- [Time-shifted viewing examples](time-shift-examples.md "time-shift-examples.md")
