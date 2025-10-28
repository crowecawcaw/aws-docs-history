# Tracker concepts

This section details common trackers concepts.

## Common Amazon Location Service trackers terminology

**Tracker resource**

An AWS resource that receives location updates from devices. The tracker
resource provides support for location queries, such as current and historic
device location. Linking a tracker resource to a geofence collection
evaluates location updates against all geofences in the linked geofence
collection automatically.

**Position data tracked**

A tracker resource stores information about your devices over time. The
information includes a series of position updates, where each update
includes location, time, and optional metadata. The metadata can include a
position's accuracy, and up to three key-value pairs to help you track key
information about each position, such as speed, direction, tire pressure,
remaining fuel, or engine temperature of the vehicle you are tracking.
Trackers maintain device location history for 30 days.

**Position filtering**

Position filtering can help you control costs and improve the quality of
your tracking application by filtering out position updates that don't
provide valuable information before the updates are stored or evaluated
against geofences.

You can choose `AccuracyBased`, `DistanceBased`, or
`TimeBased` filtering. By default, position filtering is set
to `TimeBased`.

You can configure position filtering when you create or update tracker
resources.

**RFC 3339 timestamp format**

Amazon Location Service trackers use the [RFC 3339](https://tools.ietf.org/html/rfc3339 "https://tools.ietf.org/html/rfc3339") format, which
follows the [International Organization for Standardization (ISO) 8601](https://www.iso.org/iso-8601-date-and-time-format.html "https://www.iso.org/iso-8601-date-and-time-format.html")
format for dates and time.

The format is "YYYY-MM-DDThh:mm:ss.sssZ+00:00":

- `YYYY-MM-DD` — Represents the date format.
- `T` — Indicates that the time values will
  follow.
- `hh:mm:ss.sss` — Represents the time in 24-hour
  format.
- `Z` — Indicates that the time zone used is UTC, which
  can be followed with deviations from the UTC time zone.
- `+00:00` — Optionally indicate deviations from the UTC
  time zone. For example, +01:00 indicates UTC + 1 hour.

**Example**

For July 2, 2020, at 12:15:20 in the afternoon, with an adjustment of an
additional 1 hour to the UTC time zone.

```
2020-07-02T12:15:20.000Z+01:00
```
