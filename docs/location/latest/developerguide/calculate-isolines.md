# Calculate isolines

The Calculate Isolines API allows you to determine areas reachable within specified time
or distance limits. By considering factors such as road restrictions, traffic conditions,
and travel mode, it generates isolines that outline accessible areas, supporting urban
planning, logistics, and service accessibility applications. This API can be used for urban
planning, real estate analysis, and accessibility studies by visualizing service reach,
transportation options, or resources within a set timeframe or distance limit. By displaying
these isolines on a map, users can assess travel reach within specific constraints,
enhancing decision-making for site selection, service coverage, and resource
allocation.

For more information, see [CalculateIsolines](../APIReference/API_CalculateIsolines.md "../APIReference/API_CalculateIsolines.md")
in the _Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
Calculate isolines](calculate-isolines-how-to.md "calculate-isolines-how-to.md").

## Use cases

- **Assess healthcare accessibility through travel time
  isolines:** Generate isolines to evaluate access to healthcare
  facilities from various neighborhoods based on travel times. Healthcare
  organizations can use this feature to identify underserved areas and make
  informed decisions about clinic locations or mobile health services, thereby
  improving community healthcare access.
- **Analyze market reach for retail expansion using travel
  time isolines:** Create isolines to represent customer access to
  retail locations based on travel times. Retail businesses can assess new store
  locations and understand customer demographics, using these visualizations to
  strategically expand and optimize sales potential.
- **Optimize logistics and delivery zones with
  isolines:** Generate isolines to define delivery zones based on
  time-sensitive logistics requirements. Logistics companies can visualize areas
  reachable within specific timeframes from distribution centers, improving route
  planning, operational efficiency, and timely deliveries.
- **Plan tourism and recreational access with
  isolines:** Visualize travel times from tourist attractions to
  nearby accommodations. Tourism boards can help travelers find convenient lodging
  options, promoting local businesses and enhancing the travel experience by
  displaying these isolines on a map.
- **Improve emergency response planning through
  isolines:** Generate isolines to assess response times from
  emergency service locations to various areas in a community. Emergency
  management teams can identify regions within critical response times, optimizing
  resource allocation to improve response during incidents.
- **Analyze commuting patterns for workforce planning with
  isolines:** Generate isolines to visualize commuting times and
  identify areas with high travel times. Businesses can use these insights for
  remote work policies or office relocations, enhancing employee satisfaction and
  productivity.

## Understand the request

The request accepts parameters like `Origin`, `Destination`, and
`Thresholds` for defining isolines. Optional parameters, such as
`Allow`, `Avoid`, and `TravelModeOptions`, allow
customization of isoline constraints. For more information, see the
.

**Origin**

The starting point for isoline calculation in longitude and
latitude.

**Thresholds**

Time or distance limits used to define the isoline boundary.

**TravelMode**

The mode of transport, such as car, pedestrian, or truck.

**OptimizeIsolineFor**

Optimization criteria, such as Accurate, Balanced, or Fast
calculation.

**DepartureTime**

Time of departure, if specified, for calculating time-dependent
isolines.

**ArrivalTime**

Time of arrival, if specified, for calculating time-dependent
isolines.

**IsolineGranularity**

The maximum number of points and resolution of the isoline
boundary.

## Understand the response

The response includes isolines with properties like
`IsolineGeometryFormat`, outlining the reachable area based on request
parameters. .

**Isolines**

Calculated isolines with associated properties, including geometries and
connections.

**Geometries**

List of geometries outlining the calculated isoline boundaries.

**Connections**

Connections between isoline geometries, including the geometry for each
connection.
