# Revert to default ephemeris data

When you upload custom ephemeris data it will override the default ephemerides AWS Ground Station uses for that
particular satellite. AWS Ground Station does not use the default ephemeris again until there are no currently
enabled, unexpired customer-provided ephemerides available for use. AWS Ground Station also does not list contacts
past the expiration time of the current customer-provided ephemeris, even if there is a default ephemeris available
past that expiration time.

To revert back to the default [Space-Track](https://www.space-track.org/ "https://www.space-track.org/") ephemerides, you will need to do one of the following:

- Delete (using [DeleteEphemeris](../APIReference/API_DeleteEphemeris.md "../APIReference/API_DeleteEphemeris.md")) or disable (using [UpdateEphemeris](../APIReference/API_UpdateEphemeris.md "../APIReference/API_UpdateEphemeris.md")) all
  enabled customer-provided ephemerides. You can list the customer-provided ephemerides for a satellite using
  [ListEphemerides](../APIReference/API_ListEphemerides.md "../APIReference/API_ListEphemerides.md").
- Wait for all existing customer-provided ephemerides to expire.

You can confirm that the default ephemeris is being used by calling [GetSatellite](../APIReference/API_GetSatellite.md "../APIReference/API_GetSatellite.md") and verifying
that the `source` of the current ephemeris for the satellite is `SPACE_TRACK`. See
[Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md") for more information on default ephemerides.
