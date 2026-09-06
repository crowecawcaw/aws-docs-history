

# ST\_Distance
<a name="access-graph-opencypher-22-spatial-functions-st-distance"></a>

For input geometries, ST\_Distance returns the minimum Euclidean distance between the 2D projections of the two input geometry values.

**Syntax**

```
ST_Distance(geo1, geo2)
```

**Arguments**
+ `geo1` - A value of data type GEOMETRY, or an expression that evaluates to a GEOMETRY type.
+ `geo2` - A value of data type GEOMETRY, or an expression that evaluates to a GEOMETRY.

**Return type**

DOUBLE PRECISION in the same units as the input geometries.

If geo1 or geo2 is null, then null is returned.

If the input parameter is not a Geometry, then a BadRequestException is returned.

**Examples**

```
RETURN ST_Distance(
    ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'), 
    ST_GeomFromText('POLYGON((-1 -3,-2 -1,0 -3,-1 -3))'));
1.4142135623731
```