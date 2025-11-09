# Revert to default ephemeris data

When you upload custom ephemeris data it will override the default ephemerides AWS Ground Station uses for that
particular satellite. AWS Ground Station does not use the default ephemeris again until there are no currently
enabled, unexpired customer-provided ephemerides available for use. AWS Ground Station also does not list contacts
past the expiration time of the current customer-provided ephemeris, even if there is a default ephemeris available
past that expiration time.

###### Note

Azimuth elevation ephemerides do not have default values and do not override satellite ephemerides.
They are explicitly selected when reserving a contact using the `trackingOverrides`
parameter. If you no longer wish to use azimuth elevation ephemeris, simply reserve contacts without specifying
tracking overrides, and the system will use the active satellite ephemeris instead.

## Reverting TLE and OEM ephemerides

To revert back to the default [Space-Track](https://www.space-track.org/ "https://www.space-track.org/") ephemerides
for a satellite, you will need to do one of the following:

- Delete (using [DeleteEphemeris](../APIReference/API_DeleteEphemeris.md "../APIReference/API_DeleteEphemeris.md"))
  or disable (using [UpdateEphemeris](../APIReference/API_UpdateEphemeris.md "../APIReference/API_UpdateEphemeris.md")) all
  enabled customer-provided ephemerides. You can list the customer-provided ephemerides for a satellite using
  [ListEphemerides](../APIReference/API_ListEphemerides.md "../APIReference/API_ListEphemerides.md").
- Wait for all existing customer-provided ephemerides to expire.

You can confirm that the default ephemeris is being used by calling
[GetSatellite](../APIReference/API_GetSatellite.md "../APIReference/API_GetSatellite.md") and verifying
that the `source` of the current ephemeris for the satellite is `SPACE_TRACK`. See
[Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md") for more information on default ephemerides.

## Managing azimuth elevation ephemerides

Since azimuth elevation ephemerides are explicitly selected for each contact and are not associated
with satellites, there is no concept of "reverting" to a default. Instead, you can manage azimuth
elevation ephemerides as follows:

- _To stop using azimuth elevation ephemeris:_ Simply reserve new contacts without
  specifying `trackingOverrides` and specifying a `satelliteArn`.
  The contact will use the active ephemeris for the specified satellite instead.
- _To remove unused azimuth elevation ephemerides:_
  Use [DeleteEphemeris](../APIReference/API_DeleteEphemeris.md "../APIReference/API_DeleteEphemeris.md")
  to delete azimuth elevation ephemerides that are no longer needed. Note that you cannot delete
  an ephemeris that is currently being used by a scheduled contact.

To list all azimuth elevation ephemerides in your account,
use [ListEphemerides](../APIReference/API_ListEphemerides.md "../APIReference/API_ListEphemerides.md").
Azimuth elevation ephemerides can be identified by the `ephemerisType` field,
or by the presence of a `groundStation` field instead of a `satelliteId` field in the response.
