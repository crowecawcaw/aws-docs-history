# Routes pricing

Please see below for pricing buckets for each API:

## Calculate Routes

This price is based on the number of API requests. `CalculateRoutes`
has three pricing buckets: Core, Advanced, and Premium.

**Core**

This price bucket supports the travel modes Car, Truck, and
Pedestrian, without toll cost calculation.

**Advanced**

This price bucket supports alternative travel modes such as Scooter,
without toll cost calculation.

**Premium**

This price bucket supports toll cost calculation. You will be charged
at Premium price when you request toll cost calculation by setting the
request parameters `LegAdditionalFeatures["Tolls"]` or
`SpanAdditionalFeatures["TollSystems"]`, regardless of
travel mode.

## Calculate Route Matrix

This price is based on the number of routes calculated. The number of routes
calculated in each request is equal to the number of origins multiplied by the
number of destinations, `Number of Routes = Number of origins x Number of
 Destinations`. For example, when using a matrix size of 300 origins by 100
destinations, the total number of routes calculated is 30,000 (300 x 100 =
30,000).

###### Note

Route calculations are billed for each origin and destination pair. If you use
a large matrix of origins and destinations, your costs will increase
accordingly.

`CalculateRouteMatrix` has 2 pricing buckets: Core and Advanced.

**Core**

This price bucket supports travel modes Car, Truck, and
Pedestrian.

**Advanced**

This price bucket supports alternative travel modes, such as
Scooter.

## Optimize Waypoint

This price is based on the number of API requests. `OptimizeWaypoint`
has 2 pricing buckets: Advanced and Premium.

**Advanced**

This pricing bucket supports up to 30 waypoints in a single request;
travel modes for Car, Truck and Pedestrian, with the bounding box of the
input points within 200km, and with no optional parameters such as
`Avoid`, `Clustering`, `Driver`,
`Exclude.Countries`,
`TravelModeOptions.Truck.HazardousCargos`,
`TravelModeOptions.Truck.TunnelRestrictionCode`, and no
additional waypoints or destination constraints such as
`AccessHours`, `AppointmentTime`,
`Before`, `Heading`,
`ServiceDuration`, `SideOfStreet`.

###### Note

Automatic clustering could occur when waypoints are in close
proximity, but it is still considered as advanced pricing
bucket.

**Premium**

This pricing bucket supports up to 50 waypoints in a single request;
with no restrictions on travel modes; bounding box of the input points
within 500km; and with optional parameters such as `Avoid`,
`Clustering`, `Driver`,
`Exclude.Countries`,
`TravelModeOptions.Truck.HazardousCargos`,
`TravelModeOptions.Truck.TunnelRestrictionCode`. In
addition, this pricing bucket supports optional waypoint and destination
constraints , such as `AccessHours`,
`AppointmentTime`, `Before`,
`Heading`, `ServiceDuration`,
`SideOfStreet`.

###### Note

A single request can only support up to 20 waypoints if any of the
optional waypoint and destination constraints is applied.

## Snap-to-road

This price is based on the number of API requests. `SnaptoRoad` has 2
pricing buckets: Advanced and Premium.

**Advanced**

This pricing bucket supports travel modes Car, Truck and Pedestrian,
with a `TracePoints` count up to 200 and with a maximum
airline distance between `TracePoints` of 100
kilometers.

**Premium**

This pricing bucket has no restrictions on travel modes, up to 5,000
`TracePoints` points.

## Calculate Isoline

This price is based on the number of Isolines calculated in the response.
`CalculateIsoline` has 2 pricing buckets: Advanced and
Premium.

**Advanced**

This pricing bucket supports travel modes Car, Truck and Pedestrian,
with `Thresholds.Time` values up to 60 minutes or
`Thresholds.Distance` values up to 100 kilometers.

**Premium**

This pricing bucket has no restrictions on travel modes, with
`Thresholds.Time` values up to 180 minutes or
`Thresholds.Distance` values up to 300KM.
