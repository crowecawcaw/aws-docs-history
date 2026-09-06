

# Overview of Amazon Aurora MySQL
<a name="Aurora.AuroraMySQL.Overview"></a>

The following sections provide an overview of Amazon Aurora MySQL.

**Topics**
+ [Amazon Aurora MySQL performance enhancements](#Aurora.AuroraMySQL.Performance)
+ [Amazon Aurora MySQL and spatial data](#Aurora.AuroraMySQL.Spatial)
+ [Aurora MySQL version 8.4 compatible with MySQL 8.4](AuroraMySQL.MySQL84.md)
+ [Aurora MySQL version 3 compatible with MySQL 8.0](AuroraMySQL.MySQL80.md)
+ [Aurora MySQL version 2 compatible with MySQL 5.7](AuroraMySQL.CompareMySQL57.md)

## Amazon Aurora MySQL performance enhancements
<a name="Aurora.AuroraMySQL.Performance"></a>

Amazon Aurora includes performance enhancements to support the diverse needs of high-end commercial databases.

## Amazon Aurora MySQL and spatial data
<a name="Aurora.AuroraMySQL.Spatial"></a>

The following list summarizes the main Aurora MySQL spatial features and explains how they correspond to spatial features in MySQL: 
+ Aurora MySQL version 2 supports the same spatial data types and spatial relation functions as MySQL 5.7. For more information about these data types and functions, see [Spatial Data Types](https://dev.mysql.com/doc/refman/5.7/en/spatial-types.html) and [Spatial Relation Functions](https://dev.mysql.com/doc/refman/5.7/en/spatial-relation-functions-object-shapes.html) in the MySQL 5.7 documentation.
+ Aurora MySQL version 3 supports the same spatial data types and spatial relation functions as MySQL 8.0. For more information about these data types and functions, see [Spatial Data Types](https://dev.mysql.com/doc/refman/8.0/en/spatial-types.html) and [Spatial Relation Functions](https://dev.mysql.com/doc/refman/8.0/en/spatial-relation-functions-object-shapes.html) in the MySQL 8.0 documentation.
+ Aurora MySQL version 8.4 supports the same spatial data types and spatial relation functions as MySQL 8.4. For more information about these data types and functions, see [Spatial Data Types](https://dev.mysql.com/doc/refman/8.4/en/spatial-types.html) and [Spatial Relation Functions](https://dev.mysql.com/doc/refman/8.4/en/spatial-relation-functions-object-shapes.html) in the MySQL 8.4 documentation.
+ Aurora MySQL supports spatial indexing on InnoDB tables. Spatial indexing improves query performance on large datasets for queries on spatial data. In MySQL, spatial indexing for InnoDB tables is available in MySQL 5.7 and 8.0.

  Aurora MySQL uses a different spatial indexing strategy from MySQL for high performance with spatial queries. The Aurora spatial index implementation uses a space-filling curve on a B-tree, which is intended to provide higher performance for spatial range scans than an R-tree.
**Note**  
In Aurora MySQL, a transaction on a table with a spatial index defined on a column with a spatial reference identifier (SRID) can't insert into an area selected for update by another transaction.

The following data definition language (DDL) statements are supported for creating indexes on columns that use spatial data types.

### CREATE TABLE
<a name="Aurora.AuroraMySQL.Spatial.create_table"></a>

You can use the `SPATIAL INDEX` keywords in a `CREATE TABLE` statement to add a spatial index to a column in a new table. Following is an example.

```
CREATE TABLE test (shape POLYGON NOT NULL, SPATIAL INDEX(shape));
```

### ALTER TABLE
<a name="Aurora.AuroraMySQL.Spatial.alter_table"></a>

You can use the `SPATIAL INDEX` keywords in an `ALTER TABLE` statement to add a spatial index to a column in an existing table. Following is an example.

```
ALTER TABLE test ADD SPATIAL INDEX(shape);
```

### CREATE INDEX
<a name="Aurora.AuroraMySQL.Spatial.create_index"></a>

You can use the `SPATIAL` keyword in a `CREATE INDEX` statement to add a spatial index to a column in an existing table. Following is an example.

```
CREATE SPATIAL INDEX shape_index ON test (shape);
```