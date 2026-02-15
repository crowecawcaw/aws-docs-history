# Columnstore index functionality

This topic provides reference information about the compatibility of columnstore indexes when migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. Aurora PostgreSQL does not offer a directly comparable feature to SQL Server’s columnstore indexes, which are used for data compression and query performance improvement in data warehousing scenarios.

| Feature compatibility    | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                 |
| ------------------------ | ---------------------------------- | ------------------------- | ----------------------------------------------- |
| No feature compatibility | No automation                      | N/A                       | Aurora PostgreSQL offers no comparable feature. |

## SQL Server Usage

SQL Server provides columnstore indexes that use column-based data storage to compress data and improve query performance in data warehouses. Columnstore indexes are the preferred data storage format for data warehousing and analytic workloads. As a best practice, use Columnstore indexes with fact tables and large dimension workloads.

### Examples

The following example creates

```
CREATE TABLE products(ID [int] NOT NULL, OrderDate [int] NOT NULL, ShipDate [int] NOT NULL);
GO

CREATE CLUSTERED COLUMNSTORE INDEX cci_T1 ON products;
GO
```

For more information, see [Columnstore indexes: Overview](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview?view=sql-server-2017") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) doesn’t currently provide a directly comparable alternative for SQL Server columnstore index.
