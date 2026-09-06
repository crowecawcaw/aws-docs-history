

# Transit routing
<a name="transit-routing"></a>

Transit routing calculates routes using public transportation. When the travel mode is set to `Transit`, the route is computed using public transit networks including buses, subways, trains, and other transit types. Transit routes include pedestrian legs for walking to and from transit stops.

## Public transit coverage
<a name="transit-coverage"></a>

For the list of countries, cities, and operators with public transit coverage, see the [Amazon Location Service transit coverage list](https://github.com/aws-geospatial/amazon-location-docs-resources/blob/main/routes/transit_coverage.csv) on the GitHub website.

## Supported transit modes
<a name="transit-supported-modes"></a>

The following transit modes are supported.


| Mode | Description | 
| --- | --- | 
| `AerialTramway` | Aerial tramways and cable cars that transport passengers suspended above ground on overhead cables. | 
| `Airplane` | Airplane services that are part of the public transit network. | 
| `Bus` | Standard public bus services operating on fixed routes. | 
| `BusRapidTransit` | Rapid bus services that operate on dedicated lanes with limited stops, offering faster service than standard buses. | 
| `CityTrain` | City and commuter trains that operate within urban and suburban areas. | 
| `Ferry` | Boat and ferry services that are part of the public transit network, transporting passengers across waterways. | 
| `FunicularRailway` | Inclined railways and funiculars that use cable traction to ascend and descend steep slopes. | 
| `HighSpeedTrain` | High-speed trains that operate on dedicated tracks at speeds significantly faster than conventional rail. | 
| `IntercityTrain` | Long-distance trains connecting major cities. | 
| `InterregionalTrain` | Inter-regional and fast trains that connect areas between cities and regions. | 
| `LightRail` | Trams and light rail systems that typically operate at street level or on dedicated tracks within urban areas. | 
| `Monorail` | Monorail systems that operate on a single rail or beam, typically elevated above street level. | 
| `PrivateBus` | Privately operated bus and taxi services that supplement the public transit network. | 
| `RegionalTrain` | Regional trains that serve shorter routes within a geographic area, making frequent stops at local stations. | 
| `Subway` | Underground metro and subway systems that operate on dedicated tracks beneath city streets. | 

## Modes
<a name="transit-modes"></a>

By default, all transit modes are allowed. You can control which modes are used with either `AllowedModes` or `ExcludedModes`:
+ `AllowedModes` – Only the specified modes are used. All other modes are disabled.
+ `ExcludedModes` – The specified modes are disabled. All other modes remain enabled.

You cannot use `AllowedModes` and `ExcludedModes` together in the same request.

## Unsupported fields
<a name="transit-unsupported-fields"></a>

Transit routing supports a different set of request fields compared to other travel modes. The following top-level fields are not supported when the travel mode is set to `Transit`.


| Field | Description | 
| --- | --- | 
| `Allow` | Road features to allow during route calculation, such as high occupancy lanes. | 
| `Avoid` | Road features or areas to avoid during route calculation, such as toll roads or ferries. | 
| `Driver` | Driver-related options such as schedule or rest rules. | 
| `Exclude` | Exclusion options such as specific countries to avoid. | 
| `OptimizeRoutingFor` | Optimization objective for routing, such as fastest or shortest distance. | 
| `SpanAdditionalFeatures` | Additional span-level features such as speed limits or road attributes. | 
| `Tolls` | Toll cost calculation options. | 
| `Traffic` | Traffic usage options for route calculation. | 
| `TravelStepType` | Turn-by-turn step type for route instructions. | 
| `Waypoints` | Intermediate waypoints along the route. | 