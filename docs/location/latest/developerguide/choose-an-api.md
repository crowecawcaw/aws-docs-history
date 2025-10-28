# Choose the right API

This topic helps you choose an Amazon Location Service API based on common use cases that you may
want to solve with location-based data and services.

Maps

Maps provide access to both dynamic and static map types for a variety of
applications. For more information, See [Amazon Location Service Maps](maps.md "maps.md").

- **Dynamic Maps**: Interactive maps
  that can be customized in real time, allowing users to pan, zoom,
  and overlay data. For more information, See [Dynamic maps](dynamic-maps.md "dynamic-maps.md").
- **Static Maps**: Static images of
  maps that display specific locations or routes without interactive
  elements, suitable for applications with limited interactivity. For
  more information, See [Static maps](static-maps.md "static-maps.md").

Routes

Routes provide capabilities for calculating optimized paths between
locations. These features support applications requiring logistics planning,
distance calculations, and route optimization. Users can also snap location
points to roads for improved accuracy. For more information, See [Amazon Location Service Routes](routes.md "routes.md").

- **CalculateIsolines**: Generates
  isolines based on travel time or distance, useful for defining
  service areas or reachability zones. For more information, See [Calculate isolines](calculate-isolines.md "calculate-isolines.md").
- **CalculateRouteMatrix**: Provides a
  matrix of distances and travel times between multiple origins and
  destinations, supporting logistics and trip planning. For more
  information, See [Calculate route matrix](calculate-route-matrix.md "calculate-route-matrix.md").
- **CalculateRoutes**: Calculates
  optimized routes for point-to-point or multi-stop navigation,
  including customizable routing preferences. For more information,
  See [Calculate routes](calculate-routes.md "calculate-routes.md").
- **OptimizeWaypoints**: Optimizes the
  order of waypoints for the most efficient travel route, minimizing
  distance or time. For more information, See [Optimize waypoints](actions-optimize-waypoints.md "actions-optimize-waypoints.md").
- **SnapToRoads**: Aligns coordinates
  to the nearest road paths, enhancing GPS accuracy by snapping points
  to known roads. For more information, See [Snap to Roads](snap-to-roads.md "snap-to-roads.md").

Places

Places enable applications to search, find, and retrieve details about
points of interest, addresses, and specific locations. These capabilities
enhance location-based services by providing context and improving user
experience in search functions. For more information, See [Amazon Location Service Places](places.md "places.md").

- **Geocode**: Converts addresses or
  place names into geographic coordinates (longitude, latitude),
  supporting applications that require address-to-location
  transformation for mapping and spatial analysis. For more
  information, see [Reverse Geocode](reverse-geocode.md "reverse-geocode.md").
- **Reverse Geocode**: Converts
  geographic coordinates to the nearest address or place name,
  providing context for a location. For more information, See [Reverse Geocode](reverse-geocode.md "reverse-geocode.md").
- **Autocomplete**: Suggests potential
  completions for user-entered text, improving efficiency in search
  input. For more information, See [Autocomplete](autocomplete.md "autocomplete.md").
- **GetPlace**: Retrieves detailed
  information about a specified place, including attributes like
  address, contact details, and opening hours. For more information,
  See [GetPlace](get-place.md "get-place.md").
- **SearchNearby**: Finds places within
  a specified radius of a given geographic point, suitable for "near
  me" searches. For more information, See [Search Nearby](search-nearby.md "search-nearby.md").
- **SearchText**: Allows text-based
  searching for places or points of interest based on a keyword or
  phrase, ideal for finding locations by name or description. For more
  information, See [Search Text](search-text.md "search-text.md").
- **Suggest**: Provides search term
  suggestions as users type, enhancing search relevance and user
  experience. For more information, See [Suggest](suggest.md "suggest.md").

Geofences

Geofencing allows applications to define geographical boundaries and
monitor entry or exit events within these regions. Features include
creating, updating, and deleting geofences, as well as configuring
notifications or triggers for location-based actions when tracked devices
cross geofence boundaries. Ideal for proximity-based notifications, security
monitoring, and asset tracking within predefined areas. For more
information, See [Amazon Location Service Geofences](geofences.md "geofences.md").

Trackers

Tracking enables real-time monitoring of device or asset locations over
time. Features include adding tracked devices, updating their location data,
and retrieving historical position data. Trackers are useful for managing
fleets, monitoring personnel, and ensuring the security of valuable assets
by providing up-to-date location data and movement patterns. For more
information, See [Amazon Location Service trackers](trackers.md "trackers.md").
