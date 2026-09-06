

# Intermodal routing
<a name="intermodal-routing"></a>

Intermodal routing calculates routes that combine multiple transport types in a single journey. When the travel mode is set to `Intermodal`, the route may include transit, pedestrian, rental, taxi, and vehicle legs. Pedestrian legs are always enabled and are used to connect between other transport types.

## Intermodal coverage
<a name="intermodal-coverage"></a>

Intermodal routes can combine transit, rental, and taxi legs. The countries, cities, and operators covered for each are listed below.

### Transit coverage
<a name="intermodal-transit-coverage"></a>

For the list of countries, cities, and operators with public transit coverage, see the [Amazon Location Service transit coverage list](https://github.com/aws-geospatial/amazon-location-docs-resources/blob/main/routes/transit_coverage.csv) on the GitHub website.

### Rental coverage
<a name="intermodal-rental-coverage"></a>

For the list of countries, cities, and operators with rental coverage, see the [Amazon Location Service rental coverage list](https://github.com/aws-geospatial/amazon-location-docs-resources/blob/main/routes/rental_coverage.csv) on the GitHub website.

### Taxi coverage
<a name="intermodal-taxi-coverage"></a>

For the list of countries and operators with taxi coverage, see the [Amazon Location Service taxi coverage list](https://github.com/aws-geospatial/amazon-location-docs-resources/blob/main/routes/taxi_coverage.csv) on the GitHub website.

## Leg types
<a name="intermodal-leg-types"></a>

An intermodal route consists of one or more legs, each representing a different transport type. The following leg types can appear in an intermodal route.


| Leg type | Description | 
| --- | --- | 
| Pedestrian | Walking segments that connect other legs. Always enabled and cannot be disabled. | 
| Transit | Public transit segments using buses, trains, subways, and other transit modes. Supports the same transit modes as Transit routing. | 
| Rental | Rental segments. Currently supports car share. | 
| Taxi | Taxi segments. Currently supports car-based taxis. | 
| Vehicle | Private vehicle segments. Currently supports car. | 

## EnabledFor options
<a name="intermodal-enabled-for"></a>

For transit, rental, taxi, and vehicle legs, you can use `EnabledFor` to control which portion of the route allows that leg type. The following values are supported.


| Value | Description | 
| --- | --- | 
| `FirstLeg` | Enable this leg type for the first non-pedestrian leg of the route. | 
| `LastLeg` | Enable this leg type for the last non-pedestrian leg of the route. | 
| `EntireRoute` | Enable this leg type for the entire route. | 
| `None` | Disable this leg type entirely. | 

## Modes
<a name="intermodal-modes"></a>

For transit, rental, taxi, and vehicle legs, you can control which modes are used with `AllowedModes` or `ExcludedModes`. These are configured at the individual leg type level.
+ `AllowedModes` – Only the specified modes are used. All other modes are disabled.
+ `ExcludedModes` – The specified modes are disabled. All other modes remain enabled.

You cannot use `AllowedModes` and `ExcludedModes` together for the same leg type.

## Unsupported fields
<a name="intermodal-unsupported-fields"></a>

Intermodal routing supports a different set of request fields compared to other travel modes. The following top-level fields are not supported when the travel mode is set to `Intermodal`.


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
| `TravelStepType` | The `TurnByTurn` value is not supported for intermodal routing. | 
| `Waypoints` | Intermediate waypoints along the route. | 