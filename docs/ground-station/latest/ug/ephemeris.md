# Understand how AWS Ground Station uses ephemerides

An [ephemeris](https://en.wikipedia.org/wiki/Ephemeris "https://en.wikipedia.org/wiki/Ephemeris"), plural ephemerides, is a file or data
structure providing the trajectory of astronomical objects. Historically, this file only referred to tabular data
but, gradually, it has come to direct to a wide variety of data files indicating a spacecraft trajectory.

The Ephemeris API allows custom ephemerides to be uploaded to AWS Ground Station for use with a satellite.
These ephemerides override the default ephemerides from
[Space-Track](https://www.space-track.org/ "https://www.space-track.org/") (see:
[Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md")).
We support receiving ephemeris data in Orbit Ephemeris Message (OEM), two-line element
(TLE), and azimuth elevation formats.

AWS Ground Station uses ephemeris data to determine when contacts become available based on the provided ephemeris and correctly
command antennas in the AWS Ground Station network. By default, no action is required to
provide AWS Ground Station with ephemerides if your satellite has an assigned [NORAD ID](https://en.wikipedia.org/wiki/Satellite_Catalog_Number "https://en.wikipedia.org/wiki/Satellite_Catalog_Number").

Uploading custom ephemerides can improve the quality of tracking,
handle early operations where no [Space-Track](https://www.space-track.org/ "https://www.space-track.org/")
ephemerides are available to AWS Ground Station, and account for maneuvers.

Alternatively, AWS Ground Station supports an azimuth elevation format, which allow you to directly specify antenna pointing directions
without providing satellite orbital information. This is useful for scenarios where precise antenna pointing is
required because satellite trajectory information is imprecise or unknown.

###### Topics

- [Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md")
- [Provide custom ephemeris data](providing-custom-ephemeris-data.md "providing-custom-ephemeris-data.md")
- [Reserve contacts with custom ephemeris](reserving-contacts-with-custom-ephemeris.md "reserving-contacts-with-custom-ephemeris.md")
- [Understand which ephemeris is used](which-ephemeris-is-used.md "which-ephemeris-is-used.md")
- [Get the current ephemeris for a satellite](getting-current-ephemeris.md "getting-current-ephemeris.md")
- [Revert to default ephemeris data](reverting-to-default-ephemeris-data.md "reverting-to-default-ephemeris-data.md")
