# Define manifest start and end times from

AWS Elemental MediaPackage

MediaPackage accepts requests for up to 24 hours of content.

When requests with start and end parameters that are within the startover window are sent to
this endpoint, MediaPackage generates a manifest for the requested timeframe. If the start parameter is
outside of the startover window, or if the end parameter is before the startover window, the
playback request fails. If no start and end parameters are used, the service generates a standard
manifest.

Start and end parameters denote the beginning and end of a time-shifted manifest from MediaPackage.
The playback device can append parameters to the end of a manifest request. Alternatively, the
start and end parameters can be specified for the manifest through Filter Configuration
parameters. For more information, see step 7 in [Manifest fields](endpoints-create.md#endpoints-manifest "endpoints-create.md#endpoints-manifest").

For packager-specific rules about how you can notate the parameters, see [Time-shifted query
parameters](msettings-params.md "msettings-params.md").

The start and end parameters determine the time boundaries of the manifest. These are the
expected behaviors based on request start and end parameters:

- If both start and end parameters are specified, the resulting manifest has a fixed start
  and end time that correspond to the specified start and end parameters.
- If the end time is in the future, the tags in the manifest are consistent
  with an event manifest. The manifest will continue to grow until it reaches the end time, at
  which point it will become a VOD manifest.
- If start or end parameters are used that are before the first segment is ingested, or
  after the last segment is ingested, the playback duration won't match the manifest duration as
  requested through the query parameters.
  - If the start time is specified and the value is earlier than when the first segment is
    ingested, MediaPackage uses the actual time that the first segment is ingested as the start of the
    manifest.
  - If the end time is specified and is later than when the last segment is ingested, MediaPackage
    uses the actual time that the last segment is ingested as the end of the manifest.

- If a start parameter is specified without an end parameter, the resulting manifest will
  have a fixed start time corresponding to the specified start parameter, while the end of the
  manifest will grow as the live content progresses.

###### Note

For TS output, many playback devices start playback at the current time ("now"). To view
the content from the actual start time of the playback window, viewers can seek back on the
playback progress bar.

- If no start time or end time parameters are specified, the service will generate a
  standard manifest.
