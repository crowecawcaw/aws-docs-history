# Default ephemeris data

By default, AWS Ground Station uses publicly available data from
[Space-Track](https://www.space-track.org/ "https://www.space-track.org/"), and no action is required to supply AWS Ground Station
with these default ephemerides. These ephemerides are
[two-line element sets (TLEs)](https://en.wikipedia.org/wiki/Two-line_element_set "https://en.wikipedia.org/wiki/Two-line_element_set")
associated with your satellite's [NORAD ID](https://en.wikipedia.org/wiki/Satellite_Catalog_Number "https://en.wikipedia.org/wiki/Satellite_Catalog_Number").
All default ephemerides have a priority of `0`. As a result, they will be overridden, always, by
any non-expired, custom ephemerides uploaded via the ephemeris API, which must always have
a priority of `1`, or greater.

Satellites without a NORAD ID must upload custom ephemeris data to AWS Ground Station. For example, satellites that
have just launched or that are intentionally omitted from the
[Space-Track](https://www.space-track.org/ "https://www.space-track.org/") catalog would have no NORAD ID and would
need to have custom ephemerides uploaded. For more information on providing custom ephemeris data, see:
[Providing Custom Ephemeris Data](providing-custom-ephemeris-data.md "providing-custom-ephemeris-data.md").
