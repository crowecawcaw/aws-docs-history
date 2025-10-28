# Understand how AWS Ground Station uses satellite ephemeris data

An [ephemeris](https://en.wikipedia.org/wiki/Ephemeris "https://en.wikipedia.org/wiki/Ephemeris"), plural ephemerides, is a file or data
structure providing the trajectory of astronomical objects. Historically, this file only referred to tabular data
but, gradually, it has come to direct to a wide variety of data files indicating a spacecraft trajectory.

AWS Ground Station uses ephemeris data to determine when contacts become available for your satellite and correctly
command antennas in the AWS Ground Station Network to point at your satellite. By default, no action is required to
provide AWS Ground Station with ephemerides if your satellite has an assigned [NORAD ID](https://en.wikipedia.org/wiki/Satellite_Catalog_Number "https://en.wikipedia.org/wiki/Satellite_Catalog_Number").

###### Topics

- [Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md")
- [Provide custom ephemeris data](providing-custom-ephemeris-data.md "providing-custom-ephemeris-data.md")
- [Understand which ephemeris is used](which-ephemeris-is-used.md "which-ephemeris-is-used.md")
- [Get the current ephemeris for a satellite](getting-current-ephemeris.md "getting-current-ephemeris.md")
- [Revert to default ephemeris data](reverting-to-default-ephemeris-data.md "reverting-to-default-ephemeris-data.md")
