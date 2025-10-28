# Calculate route matrix

The Matrix Routing service calculates routing matrices, providing travel times or
distances between multiple origins and destinations. This service offers flexible
customization options, allowing you to specify travel modes, traffic conditions, and other
routing parameters. The matrix calculations can vary in size and shape, supporting both
square and non-square matrices, and accommodate dynamic or free-flow traffic data.

For more information, see [CalculateRouteMatrix](../APIReference/API_CalculateRouteMatrix.md "../APIReference/API_CalculateRouteMatrix.md") in the _Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
Calculate route matrix](calculate-route-matrix-how-to.md "calculate-route-matrix-how-to.md").

## Use cases

- **Optimize delivery routes for logistics and
  e-commerce:** Efficiently calculate travel time and distance
  between multiple pickup and delivery locations to optimize routes. Logistics
  companies can use this feature to minimize costs and delivery time by planning
  efficient paths across cities. It is ideal for setting optimized delivery
  windows for same-day or next-day services and planning multi-stop delivery
  routes.
- **Match drivers and passengers in ride-sharing
  applications:** Use route calculations to match drivers with the
  closest passengers by finding the fastest route between locations. Ride-sharing
  apps can enhance user experience by providing real-time driver arrival
  estimates, ensuring prompt pickups and drop-offs. Supports various
  transportation modes like cars, bikes, and scooters.
- **Plan and optimize routes for fleet
  management:** Manage large fleets by optimizing routes to reduce
  fuel consumption and travel time. Fleet managers can assign the most efficient
  routes to vehicles for multiple stops, thereby increasing overall operational
  efficiency. Use cases include service fleets, transportation companies, and
  utilities where optimal route planning is essential for site visits.

## Understand the request

The request includes **Origins** and **Destinations** for route calculations, with optional parameters
to tailor the matrix based on preferences and constraints. For more details, refer to
the API Reference for Calculate Route Matrix API.

- `Origins`: List of origin coordinates in longitude and
  latitude.
- `Destinations`: List of destination coordinates.
- `OptimizeRoutingFor`: Optimization criteria such as "Fastest" or
  "Shortest" route.
- `RoutingBoundary`: Defines boundaries for calculation, either as
  "Unbounded" or restricted to a specific geometry.
- `Avoid`: Features to avoid during route calculation. Ignored if no
  viable route can be found.
- `Traffic`: Traffic-related options impacting route
  calculations.

## Understand the response

The response includes a matrix of calculated routes between origins and destinations,
with details such as distance and duration. Errors and boundaries for the routes are
also provided, if applicable. Refer to the API Reference for additional details on the
Calculate Route Matrix API.

- `RouteMatrix`: Matrix containing travel distances and durations
  between origins and destinations.
- `ErrorCount`: Number of errors encountered during route
  calculations.
- `RoutingBoundary`: Boundary within which the matrix is
  calculated.
