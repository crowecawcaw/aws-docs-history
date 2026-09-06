

# ST\_Point
<a name="access-graph-opencypher-22-spatial-functions-st-point"></a>

ST\_Point returns a point from the input coordinate values.

**Syntax**

```
ST_Point(x, y, z)
```

**Arguments**
+ `x` - A value of data type DOUBLE PRECISION that represents a first coordinate.
+ `y` - A value of data type DOUBLE PRECISION that represents a second coordinate.
+ `z` - (optional)

**Coordinate order**

When working with geographic coordinates, the first argument (`x`) represents **longitude** and the second argument (`y`) represents **latitude**. This follows the standard coordinate order used in spatial databases and the ISO 19125 standard.

```
// Correct: longitude first, latitude second
ST_Point(-84.4281, 33.6367)  // Atlanta airport

// Incorrect: latitude first, longitude second
ST_Point(33.6367, -84.4281)  // This will return NaN in distance calculations
```

**Valid coordinate ranges**

For geographic data, ensure coordinates fall within valid ranges:
+ Longitude (`x`): -180 to 180
+ Latitude (`y`): -90 to 90

Coordinates outside these ranges will return `NaN` (Not a Number) when used with distance calculation functions like `ST_DistanceSpheroid`.

**Return type**

GEOMETRY of subtype POINT

If x or y is null, then null is returned.

**Examples**

The following constructs a point geometry from the input coordinates.

```
RETURN ST_Point(5.0, 7.0); 
POINT(5 7)
```