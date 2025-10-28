# Routes Terminology

**Route**

A route provides details for traveling from a departure position through waypoint positions to a destination. It includes travel distance, travel time, route geometry, speed limits, spans, and other attributes.

**Route Matrix**

A matrix representing travel distance and travel time from a set of origins to a set of destinations. It is useful as an input for route planning or optimization applications.

**Waypoint**

Waypoints are intermediate stops along a route from the departure point to the destination. The route follows the stopover order as specified in the request.

**Leg**

A leg represents the journey between two consecutive positions on a route. If the positions are off-road, they are moved to the nearest road. A route with no waypoints consists of a single leg. Routes with one or more waypoints have multiple legs, with each leg representing travel from one waypoint to the next. Certain legs, like those involving ferries, contain specific information pertinent to that leg type.

**Step**

A step is a segment within a leg, providing summary details for that part of the journey. Types of steps include:

- **Default Steps** – Basic steps with human-readable instructions, suited for web applications that display a route overview.
- **Turn-by-Turn Steps** – Detailed steps suitable for turn-by-turn applications, providing granular instructions.
- **Before Travel Steps** – Steps to complete before starting the journey. Example: boarding a ferry.
- **After Travel Steps** – Steps to complete after reaching the end of a journey. Example: de-boarding a ferry.

**Span**

A span represents a continuous stretch of a road that shares a consistent set of attributes. New spans are created along a route whenever one of the requested attributes changes.

**Segment**

A segment is a navigable portion of a road, typically represented as a linear stretch.

**Route Geometry**

Route geometry depicts the path of a route for visualization, analysis, or other uses. Each route leg’s geometry can be represented as a compressed, encoded polyline or as a simple line string.

**Flexible Polyline**

A compact, encoded polyline format for representing geometry. Recommended for limiting response size and optimized for client-side decoding.

**Simple Line String**

A GeoJSON LineString format representing geometry. This format produces a larger response payload and is an ordered array of coordinates that can be used to plot routes on a map.
