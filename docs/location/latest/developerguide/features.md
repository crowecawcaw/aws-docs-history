# Key features of Amazon Location

Amazon Location offers a comprehensive set of features to enhance your location-based
applications and services. This page provides an overview of the key capabilities
available, including Maps, Places, Routes, and Geofences and Trackers. Leveraging these
features, you can build rich, location-aware experiences tailored to your specific use
cases, whether it's delivering real-time location intelligence, enabling location-based
services, or optimizing logistics and transportation operations.

Amazon Location provides the following features:

**Maps**

Amazon Location Service Maps lets you visualize location information and is the
foundation of many location-based service capabilities. Amazon Location Service offers both
dynamic and static maps.

Dynamic Maps allow you to create interactive maps using map tiles, with
the option to use pre-built map styles such as standard, monochrome, hybrid,
and satellite. You can stitch the Dynamic Maps content (Tiles, Styles,
Glyphs, and Sprites) together using a map rendering engine, such as
MapLibre.

Static Maps allow you to create pre-rendered, non-interactive map images
that display a fixed geographical area to be embedded in applications
without complex renderers.

For more information, see [Amazon Location Service Maps](maps.md "maps.md").

**Places**

Amazon Location Service Places lets you integrate search and geocode functionality into
your application. You can:

- Use geocode (Forward and Reverse) to convert a place, such an
  admin area, street, or address into geographic coordinates and vice
  versa.
- Use places search (Text and Nearby) to search for points of
  interest and get information on contact, access points, and opening
  hours.
- Use autocomplete or suggestions to autofill or predict an address
  or place based on user input. You can also use Get Place to get
  place details by place ID.

For more information, see [Amazon Location Service Places](places.md "places.md").

**Routes**

Amazon Location Service Routes lets you find routes, service area, and optimize and
analyze routes. You can do the following:

- Estimate travel time and distance based on an up-to-date road
  network and live traffic information.
- Create a service area or isoline based on distance and time
  thresholds of your business need.
- Calculate a matrix (time and distance) for multiple origins and
  destinations and use the same for route planning.
- Align GPS traces to the nearest road segment, to improve accuracy
  of vehicle tracking and route visualization.
- Find the most efficient order to travel to multiple destinations,
  also known as solving the travelling salesman problem.

For more information, see [Amazon Location Service Routes](routes.md "routes.md").

**Geofences**

Amazon Location Service Geofences lets you give your application the ability to detect
and act when a device enters or exits a deﬁned geographical boundary known
as a geofence. Automatically send an entry or exit event to Amazon EventBridge when a
geofence breach is detected. This lets you initiate downstream actions, such
as sending a notiﬁcation to a target.

For more information, see [Amazon Location Service Geofences](geofences.md "geofences.md").

**Trackers**

Amazon Location Service Trackers let you retrieve the current and historical location of
devices that are running your tracking-enabled application. You can also
link trackers with Amazon Location Service geofences to evaluate location updates from your
devices against your geofences automatically. Trackers can help you reduce
costs by filtering position updates that haven't moved before storing or
evaluating them against geofences.

For more information, see [Amazon Location Service trackers](trackers.md "trackers.md").
