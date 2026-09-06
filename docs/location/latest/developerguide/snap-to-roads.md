

# Snap to Roads
<a name="snap-to-roads"></a>

The Snap to Road API enhances the accuracy of geographic positioning by aligning GPS coordinates to the nearest road segments on a digital map. This API takes raw longitude and latitude data, often collected from mobile devices or vehicles, and "snaps" these points to the corresponding road network, correcting inaccuracies caused by GPS drift or signal loss. By integrating the Snap to Road API, you can ensure your applications provide reliable and accurate data, supporting better decision-making and operational efficiency across various scenarios.

For more information, see [SnapToRoads](https://docs.aws.amazon.com/location/latest/APIReference/API_SnapToRoads.html) in the *Amazon Location Service API Reference*.

For example requests, responses, cURL, and CLI commands for this API, see [How to use Snap to Roads](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-roads-how-to.html).

## Use cases
<a name="use-cases"></a>
+ **Enhance navigation accuracy by snapping to the road network:** Efficiently align GPS coordinates to the nearest road segments to improve navigation accuracy. This feature is valuable for mapping and navigation services, providing users with precise directions and real-time location updates, thus enhancing the navigation experience.
+ **Improve data accuracy for fleet management applications:** Correct the reported positions of vehicles by snapping their GPS coordinates to the closest roadways. In fleet management systems, this feature ensures accurate vehicle tracking, enabling optimized logistics and better operational efficiency.

## Understand the request
<a name="understanding-request"></a>

The request requires `TracePoints` to match to roads, with optional parameters like `SnappedGeometryFormat` and `SnapRadius` for controlling geometry format and snapping radius. .

**TracePoints**  
A list of coordinates to be snapped to the road network.

**SnappedGeometryFormat**  
The format of the returned geometry, such as "FlexiblePolyline" or "Simple".

**SnapRadius**  
The radius around trace points within which road snapping is considered.

## Understand the response
<a name="understanding-response"></a>

The response contains corrected geometry and snapped trace points, with properties like `SnappedGeometry` and `SnappedTracePoints` to indicate accuracy and snapping confidence. .

**SnappedGeometry**  
The corrected geometry of the snapped route.

**SnappedTracePoints**  
The adjusted coordinates of the trace points snapped to roads.

**Notices**  
Warnings or informational messages about the snapping process.