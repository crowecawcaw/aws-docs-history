# Places terminology

This section provides essential definitions to understand core concepts within
Amazon Location Service Places, such as location data types, geographic boundaries, and filtering
options. These terms enable accurate use of the Places API capabilities.

**Location**

A specific point on Earth's surface, typically defined by geographic
coordinates (longitude and latitude). Locations can represent any place or
area, such as a city, building, or point of interest.

**Places**

Any location that includes administrative areas, addresses, points of
interest (POI), geographic areas, and more. Places often have associated
information, such as name, address, coordinates, types, business hours,
contacts, and categories.

**Address**

Includes point-based addresses (like offices, homes), street addresses,
and interpolated addresses, providing precise location data.

See the definition of _interpolation_
below.

**Secondary Address**

An address that includes secondary designators, such as a suite or unit
number, building, or floor information.

**Inferred Secondary Address**

An inferred address that includes secondary designators, such as a suite or unit number,
building, or floor information. Inferred secondary addresses are derived from the input query
and are not guaranteed to exist.

**Point of Interest (POI)**

A POI refers to notable locations, such as businesses (like restaurants,
stores) or landmarks (like parks, monuments).

**Administrative areas**

Regions such as countries, provinces, states, districts, blocks, and
postal areas that organize geographical data.

**Geographic area**

Areas including cities, localities, and neighborhoods, offering additional
levels of granularity in geographical data.

**Position**

A precise set of coordinates (longitude and latitude) that pinpoints where
a place is located on a map.

**Bias position**

A reference point in geographic data that helps prioritize search results
closer to this location, enhancing relevance in searches.

**Bounding box**

A rectangular geographic area defined by southwest and northeast
coordinates, used to narrow down searches or display content within the area
on a map.

**Place type**

A classification for places based on function or characteristics. Types
include country, region, locality, district, postal area, block,
intersection, street address, point address, interpolated address, or
POI.

**Category**

A grouping for businesses and landmarks based on the type of services or
activities they offer, such as restaurants, hotels, schools, and parks.
Categories make it easier for users to find specific types of POIs in
searches.

**Match score**

An indicator of how closely a search result aligns with the input, aiding
in determining relevance.

**Interpolation**

The method of estimating unknown addresses by using known address
locations as reference points.

**ISO 3166 country codes**

Amazon Location Service Places use International Organization for Standardization (ISO)
3166 country codes for identifying countries or regions. Find the code for
each country on the ISO Online Browsing Platform.
