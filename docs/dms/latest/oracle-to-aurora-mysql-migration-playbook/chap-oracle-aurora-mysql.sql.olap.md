

# Oracle OLAP functions and MySQL Window functions
<a name="chap-oracle-aurora-mysql.sql.olap"></a>

The following sections detail the steps for configuring AWS DMS to handle OLAP functions and Window functions during replication.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  | N/A |  `GREATEST` and `LEAST` functions might get different results in MySQL. `CONNECT BY` isn’t supported by MySQL, a workaround is available. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.olap.oracle"></a>

Oracle OLAP functions extend the functionality of standard SQL analytic functions by providing capabilities to compute aggregate values based on a group of rows. You can apply the OLAP functions to logically partitioned sets of results within the scope of a single query expression. OLAP functions are usually used in combination with Business Intelligence reports and analytics. They can help boost query performance as an alternative to achieving the same result using more complex non-OLAP SQL code.

### Common Oracle OLAP functions
<a name="chap-oracle-aurora-mysql.sql.olap.oracle.common"></a>


| Function type | Related functions | 
| --- | --- | 
| Aggregate |  `average_rank`, `avg`, `count`, `dense_rank`, `max`, `min`, `rank`, `sum`  | 
| Analytic |  `average_rank`, `avg`, `count`, `dense_rank`, `lag`, `lag_variance`, `lead_variance_percent`, `max`, `min`, `rank`, `row_number`, `sum`, `percent_rank`, `cume_dist`, `ntile`, `first_value`, `last_value`  | 
| Hierarchical |  `hier_ancestor`, `hier_child_count`, `hier_depth`, `hier_level`, `hier_order`, `hier_parent`, `hier_top`  | 
| Lag |  `lag`, `lag_variance`, `lag_variance_percent`, `lead`, `lead_variance`, `lead_variance_percent`  | 
| OLAP DML |  `olap_dml_expression`  | 
| Rank |  `average_rank`, `dense_rank`, `rank`, `row_number`  | 

For more information, see [OLAP Functions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/OLAP-Functions.html#GUID-2AE523A7-630C-4907-B91B-89861C141EBD) and [Functions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Functions.html#GUID-D079EFD3-C683-441F-977E-2C9503089982) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.olap.mysql"></a>

Some Oracle OLAP functions are aggregative functions in Aurora MySQL. For more information, see [Single-Row and Aggregate Functions](chap-oracle-aurora-mysql.sql.aggregate.md).

You can replace other OLAP functions with window functions, which are currently not available in Aurora MySQL.

Aurora MySQL version 5.7 does not support window functions.

**Note**  
 Amazon Relational Database Service (Amazon RDS) for MySQL version 8 supports window functions that for each row from a query perform a calculation using rows related to that row. These include functions such as `RANK()`, `LAG()`, and `NTILE()`. In addition several existing aggregate functions now can be used as window functions such as `SUM()` and `AVG()`. For more information, see [Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html) in the *MySQL documentation*.

### Migration considerations
<a name="chap-oracle-aurora-mysql.sql.olap.mysql.considerations"></a>

As a temporary workaround, rewrite the code to remove the use of Window Functions, and revert to using more traditional SQL code solutions.

In most cases, you can find an equivalent SQL query, although it may be less optimal in terms of performance, simplicity, and readability. See the examples below for migrating window functions to code that uses correlated subqueries.

**Note**  
You may want to archive the original code and then reuse it in the future when Aurora MySQL is upgraded to version 8. The documentation for version 8 indicates the window function syntax is ANSI compliant and will be compatible with Oracle PL\\SQL syntax.

For more information, see [Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html) in the *MySQL documentation*.

### Examples
<a name="chap-oracle-aurora-mysql.sql.olap.mysql.examples"></a>

The following examples demonstrate ANSI SQL compliant subquery solutions:

Create and populate an `OrderItems` table.

```
CREATE TABLE OrderItems(
OrderID INT NOT NULL, Item VARCHAR(20) NOT NULL,
Quantity SMALLINT NOT NULL,
PRIMARY KEY(OrderID, Item));

INSERT INTO OrderItems (OrderID, Item, Quantity)
  VALUES (1, 'M8 Bolt', 100), (2, 'M8 Nut', 100),
    (3, 'M8 Washer', 200);
```

Rank items based on ordered quantity. This is a workaround for the window ranking function.

```
SELECT Item, Quantity,
(SELECT COUNT(*) FROM OrderItems
  AS OI2 WHERE OI.Quantity > OI2.Quantity) + 1
    AS QtyRank
FROM OrderItems AS OI;
```

Calculate the grand total. This is a workaround for a partitioned window aggregate function.

```
SELECT Item, Quantity,
(SELECT SUM(Quantity) FROM OrderItems
  AS OI2 WHERE OI2.OrderID = OI.OrderID)
  AS TotalOrderQty
FROM OrderItems AS OI;
```

For more information, see [Window Function Descriptions](https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html) in the *MySQL documentation*.