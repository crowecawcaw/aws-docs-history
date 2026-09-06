

# ST\_Envelope
<a name="access-graph-opencypher-22-spatial-functions-st-envelope"></a>

ST\_Envelope returns the minimum bounding box of the input geometry, as follows:
+ If the input geometry is empty, the returned geometry will be POINT EMPTY.
+ If the minimum bounding box of the input geometry degenerates to a point, the returned geometry is a point.
+ If none of the preceding is true, the function returns a counter-clockwise-oriented polygon whose vertices are the corners of the minimum bounding box.

For all nonempty input, the function operates on the 2D projection of the input geometry.

**Syntax**

```
ST_Envelope(geom)
```

**Arguments**
+ `geom` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type.

**Return type**

GEOMETRY

If geom is null, then null is returned.

**Examples**

```
RETURN ST_Envelope(ST_GeomFromText("POLYGON ((2 1, 4 3, 6 1, 5 5, 3 4, 2 1))"))
POLYGON ((2 1, 6 1, 6 5, 2 5, 2 1))
```