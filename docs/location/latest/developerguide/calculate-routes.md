

# Calculate routes
<a name="calculate-routes"></a>

The Routes API calculates routes between two or more locations with or without avoidances for different travel modes such as car, truck, scooter, pedestrian, transit, and intermodal. With this API, you can customize routing options and request additional route-related information to meet specific needs. This API supports turn-by-turn navigation and customizes route calculations by applying parameters like avoiding toll roads, motorways, or ferries. The API also returns speed limits and toll costs.

For more information, see [CalculateRoutes](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html) in the *Amazon Location Service API Reference*.

For example requests, responses, cURL, and CLI commands for this API, see [How to use Calculate routes](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-how-to.html).

![An overview of Amazon Location Service Routes.](http://docs.aws.amazon.com/location/latest/developerguide/images/routesV2/P2P-Turn-by-turn-navigation.gif)


## Use cases
<a name="use-cases"></a>
+ **Display geographic details on a route map:** Use advanced mapping features to visualize detailed routes with rich geographic information, including landmarks, terrain, and urban infrastructure. Enhance decision-making by allowing users to view clear routes from their starting point to their destination. This feature can support navigation, planning, and various logistics scenarios, and display routes for travel modes such as cars, trucks, scooters, pedestrians, transit, and intermodal. Customize routes by adding elements like avoidances or toll calculations.
+ **Show turn-by-turn navigation:** Provide seamless navigation support on web and mobile devices. Users can access turn-by-turn directions, ensuring efficient travel. Both platforms can leverage navigation instructions to offer routes for personal or business travel, including speed limits.
+ **Calculate toll costs along routes:** Incorporate toll cost calculations into route planning to provide accurate pricing estimates for routes that include toll roads, bridges, or tunnels. Display toll costs upfront to help drivers and planners make cost-effective decisions and avoid tolls when necessary.
+ **Ensure compliance with speed limits:** Integrate speed limit data to help drivers stay within legal limits, reducing the risk of fines and promoting safer, fuel-efficient driving. Logistics and fleet management can also benefit by monitoring speed compliance in real time.
+ **Assist with freight and vehicle routing solutions:** Simplify freight and vehicle routing operations by integrating routes, navigation, and tracking capabilities into logistics portals. Efficiently plan routes for multiple deliveries, track shipments in real-time, and manage fuel costs through better routing.
+ **Plan public transit journeys:** Calculate routes using public transportation such as buses, subways, trains, and monorails. Transit routes include walking directions to and from stops, departure and arrival times, and transit line information.
+ **Combine transport types with intermodal routing:** Calculate routes that combine multiple transport types in a single journey, including transit, pedestrian, rental, taxi, and vehicle legs. Intermodal routing enables end-to-end trip planning that reflects how people actually travel in urban environments.

## Understand the request
<a name="understanding-request"></a>

**Note**  
 For customers in `ap-southeast-1` and `ap-southeast-5`, supported request and response fields may differ. Refer to the [CalculateRoutes API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html) for details. 

The request requires `Origin` and `Destination` parameters, while optional parameters like `Allow`, `Avoid`, and `Traffic` customize the route to meet specific needs and constraints. .

**Origin**  
The start position of the route in longitude and latitude.

**Destination**  
The end position of the route.

**Waypoints**  
Intermediate positions to include along a route between the start and end positions.

**OptimizeRoutingFor**  
Optimization criteria for the route, such as fastest or shortest.

**LegGeometryFormat**  
Format of the geometry returned for each route leg.

**Avoid**  
Features to be avoided during route calculation, ignored if no alternative route is found.

**Traffic**  
Traffic-related options affecting route calculation.

**Tolls**  
Toll-related options impacting route calculations and toll costs.

**LegAdditionalFeatures**  
Features that can be enabled within the response for each leg of the journey.

**SpanAdditionalFeatures**  
Span features that can be enabled within the response for each leg of the journey.

**TravelMode**  
Specifies the mode of transport. Supported values include `Car`, `Truck`, `Scooter`, `Pedestrian`, `Transit`, and `Intermodal`.

**TravelModeOptions**  
Travel mode-specific options. Includes options for `Transit` (such as allowed/excluded modes, max transfers, and pedestrian options) and `Intermodal` (such as transit, rental, taxi, vehicle, and pedestrian options).

## Understand the response
<a name="understanding-response"></a>

The response provides route details such as the legs of the journey, notices about route calculations, and summary information including distance and duration. .

**Routes**  
Array of routes containing legs and associated properties.

**Notices**  
Warnings or informational messages about the route.

**LegGeometryFormat**  
Specifies the format of the route's geometry.

### Leg details
<a name="leg-details"></a>

Each leg of a journey can be of type Ferry, Pedestrian, Vehicle, Transit, Rental, or Taxi depending on the transport mode. While each leg contains properties agnostic to transport mode, specific properties can be found under:

**FerryLegDetails**  
Ferry-specific properties for the leg.

**VehicleLegDetails**  
Vehicle-specific properties for the leg.

**PedestrianLegDetails**  
Pedestrian-specific properties for the leg.

**TransitLegDetails**  
Transit-specific properties for the leg, including transit line information, stops, and schedules.

**RentalLegDetails**  
Rental-specific properties for the leg, such as car-share details.

**TaxiLegDetails**  
Taxi-specific properties for the leg.

### Steps
<a name="steps"></a>

Each leg of a journey is divided into steps that describe actions for portions of the route. A step can be either Default, suitable for basic applications, or TurnByTurn, suitable for turn-by-turn navigation. Each step contains properties agnostic to step type, such as duration and distance, and other specific properties like ExitStepDetails, which applies only to exit steps.

**BeforeTravelSteps**  
Steps to perform before beginning the journey.

**TravelSteps**  
Steps to perform during the journey.

**AfterTravelSteps**  
Steps to perform after completing the journey.

### Spans
<a name="spans"></a>

Each leg of a journey can be split into spans. A span is a portion of the leg with the same values for the set of requested `SpanAdditionalFeatures`. Spans are divided by road properties such as `SpeedLimit`, road names, or regions. Returned spans can be used to visualize road attributes and access-related information.