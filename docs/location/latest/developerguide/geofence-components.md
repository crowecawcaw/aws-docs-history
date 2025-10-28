# Geofence concepts

This section describes some common geofence concepts, including common terminology and
how to manage geofences.

## Amazon Location Service geofence terminology

Geofence

A virtual boundary for a geographical area on a map.

Geofence collection

A group of geofences that is capable of emitting `Entry`
and `Exit` events, when requested, to evaluate a device's
position against its component geofences.

Geofence geometry

A geometric shape or set of shapes that define the areas to be
included or excluded from a geofence. A geofence geometry can be
represented as a `Circle`, `Polygon`, or
`MultiPolygon`.

A `Circle` is a point with a distance around it. Use a
circle when you want to be notified if a device is within a certain
distance of a location.

A `Polygon` is a list of linear rings which represent the
shape of a geofence. This list _must_ include an
exterior ring representing the outer perimeter of the geofence, and can
optionally include multiple interior rings representing polygonal spaces
within the perimeter, which are excluded from the geofence area.

A `MultiPolygon` is a list `Polygon` elements
which represent the shape of a geofence. The `Polygon`
components of a `MultiPolygon` geometry can define separate
geographical areas that are considered part of the same geofence,
perimeters of larger exterior areas with smaller interior spaces that
are excluded from the geofence, or some combination of these use cases
to form complex geofence boundaries.

For more information about defining geofence geometries, including
syntax requirements, limitations, and examples, see [GeofenceGeometry](../APIReference/API_WaypointGeofencing_GeofenceGeometry.md "../APIReference/API_WaypointGeofencing_GeofenceGeometry.md") in the _Amazon Location Service API
Reference_.
