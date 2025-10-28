# Get started with Amazon Location Service Geofences

Geofences are powerful tools for defining geographic boundaries and triggering actions
based on location updates. This guide walks you through the process of creating and
using geofence collection resources in Amazon Location. By setting up geofences and evaluating
locations against them, you can monitor movement and generate automated events, such as
notifications when a device enters or exits a defined area. These features are ideal for
applications like fleet tracking, location-based notifications, and more.

1.  Create a geofence collection resource in your AWS account.
2.  Add geofences to the collection. You can use the geofence upload tool on the
    Amazon Location console or the Amazon Location Geofences API. For more information about
    available options, see [Authenticate with Amazon Location Service](access.md "access.md"). A geofence can be defined as a
    `Circle`, `Polygon`, or `MultiPolygon`. Use
    a `Polygon` or `MultiPolygon` to determine when a device
    enters a specific area. Use a `Circle` to determine when a device
    comes within a certain distance (radius) of a point. For more information, see
    [Amazon Location Service geofence terminology](geofence-components.md#geofence-terminology "geofence-components.md#geofence-terminology").
3.  You can start evaluating locations against all your geofences. When a location
    update crosses the boundaries of one or more geofences, your geofence collection
    resource emits one of the following geofence event types on Amazon
    EventBridge:

        * **ENTER** – One event is generated for
         each geofence where the location update crosses its boundary by entering
         it.
        * **EXIT** – One event is generated for
         each geofence where the location update crosses its boundary by exiting
         it.

    For more information, see [React to Amazon Location Service events with Amazon EventBridge](location-events.md "location-events.md"). You can also
    integrate monitoring using services such as Amazon CloudWatch and AWS CloudTrail. For more
    information see, [Monitor with Amazon CloudWatch](cloudwatch.md "cloudwatch.md") and [Monitor and log with AWS CloudTrail](cloudtrail.md "cloudtrail.md").
    For example, you are tracking a fleet of trucks and want to be notified when a truck
    comes within a certain area of any of your warehouses. Create a geofence for the area
    around each warehouse. When the trucks send you updated locations, use Amazon Location Service to
    evaluate those positions and see if a truck has entered (or exited) one of the geofence
    areas.

###### Note

You're billed by the number of geofence collections you evaluate against. Your
bill is not affected by the number of geofences in each collection. Since each
geofence collection may contain up to 50,000 geofences, you may want to combine your
geofences into fewer collections, where possible, to reduce your cost of geofence
evaluations. The events generated will include the ID of the individual geofence in
the collection, as well as the ID of the collection.
