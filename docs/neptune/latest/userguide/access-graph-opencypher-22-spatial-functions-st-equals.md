

# ST\_Equals
<a name="access-graph-opencypher-22-spatial-functions-st-equals"></a>

ST\_Equals returns true if the 2D projections of the input geometries are topologically equal. Geometries are considered topologically equal if they have equal point sets. In topologically equal geometries, the order of vertices may differ while maintaining this equality.

**Syntax**

```
ST_Equals(geom1, geom2)
```

**Arguments**
+ `geom1` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type.
+ `geom2` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type. This value is compared with geom1 to determine if it is equal to geom1.

**Return type**

BOOLEAN

If geom1 or geom2 is null, then null is returned.

If geom1 or geom2 are not Geometries, then a BadRequestException is returned.

**Examples**

```
RETURN ST_Equals(
    ST_GeomFromText('POLYGON ((0 2,1 1,0 -1,0 2))'), 
    ST_GeomFromText('POLYGON((-1 3,2 1,0 -3,-1 3))'));
false
```

The following checks if the two linestrings are geometrically equal.

```
RETURN ST_Equals(
    ST_GeomFromText('LINESTRING (1 0, 10 0)'), 
    ST_GeomFromText('LINESTRING(1 0,5 0,10 0)'));
true
```