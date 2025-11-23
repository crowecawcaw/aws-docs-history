# Reporting ad tracking data

MediaTailor provides two options for tracking and reporting on how much of an ad a viewer has
watched. In the server-side ad reporting approach, MediaTailor tracks the ad and sends beacons
(tracking signals) directly to the ad server. Alternatively, in the client-side tracking
approach, the client player (the user's device) tracks the ad and sends the beacons to the
ad server. The type of ad reporting used in a playback session depends on the specific
request the player makes to initiate the session in MediaTailor.

For information about passing session and player data to the ad server using dynamic
variables, see [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md"). For details about
session initialization parameters, see [MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md").

###### Topics

- [MediaTailor server-side ad tracking and
  reporting](ad-reporting-server-side.md "ad-reporting-server-side.md")
- [Client-side ad tracking](ad-reporting-client-side.md "ad-reporting-client-side.md")
