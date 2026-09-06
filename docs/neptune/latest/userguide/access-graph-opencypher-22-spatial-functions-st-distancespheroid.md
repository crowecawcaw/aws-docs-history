

# ST\_DistanceSpheroid
<a name="access-graph-opencypher-22-spatial-functions-st-distancespheroid"></a>

Returns the minimum distance in meters between two lon/lat geometries. The spheroid is WGS84/SRID 4326.

**Syntax**

```
ST_DistanceSpheroid(geom1, geom2);
```

**Arguments**
+ `geom1` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type.
+ `geom2` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type.

**Return type**

FLOAT

If geom is null, then null is returned.

**Examples**

```
RETURN ST_DistanceSpheroid(
    ST_GeomFromText('POINT(-110 42)'),
    ST_GeomFromText('POINT(-118 38)'))
814278.77
```