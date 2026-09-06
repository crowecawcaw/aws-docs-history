

# ST\_GeometryType
<a name="access-graph-opencypher-22-spatial-functions-st-geometrytype"></a>

ST\_GeometryType returns the type of the geometry as a string.

**Syntax**

```
ST_GeometryType(geom)
```

**Arguments**
+ `geom` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type.

**Return type**

STRING

If geom is null, then null is returned.

If the input parameter is not a Geometry, then a BadRequestException is returned.

**Examples**

```
RETURN ST_GeometryType(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
ST_LineString
```