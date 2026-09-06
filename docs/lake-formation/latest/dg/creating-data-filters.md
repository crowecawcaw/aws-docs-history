

# Creating a data filter
<a name="creating-data-filters"></a>

You can create one or more data filters for each Data Catalog table.

**To create a data filter for a Data Catalog table (console)**

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

   Sign as a data lake administrator, the target table owner, or a principal who has a Lake Formation permission on the target table.

1. In the navigation pane, under **Data catalog**, choose **Data filters**.

1. On the **Data filters** page, choose **Create new filter**.

1. In the **Create data filter** dialog box, enter the following information:
   + Data filter name 
   + Target database – Specify the database that contains the table.
   + Target table 
   + Column-level access – Leave this set to **Access to all columns** to specify row filtering only. Choose **Include columns** or **Exclude columns** to specify column or cell filtering, and then specify the columns to include or exclude.

     Nested columns – If you're applying the filter on a table that contains nested columns, you can explicitly specify sub-structures of the nested struct columns within a data filter. 

     When you grant SELECT permission to a principal on this filer, the principal executing the following query, will only see the data for `customer.customerName` and not `customer.customerId`.

     ```
     SELECT "customer" FROM "example_db"."example_table";
     ```  
![Column-level access settings showing Include columns selected with 4 of 11 columns checked.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/nested-column-filter.png)

      When you grant permissions to the `customer` column, the principal receives the access to the column and the nested fields under the column (`customerName` and `customerID`). 
   + Row filter expression – Enter a filter expression to specify row or cell filtering. For supported data types and operators, see [PartiQL support in row filter expressions](partiql-support.md). Choose **Access to all rows** to grant access to all .

     You can include partial column structs from nested columns in a row filter expression to filter rows that contain specific value.

     When a principal is granted permissions to a table with a row filter expression `Select * from example_nestedtable where customer.customerName <>'John'`, and **Column-level** access is set to **Access to all columns**, the query results shows only rows where `customerName <>'John'` evaluates to true.

   The following screenshot shows a data filter that implements cell filtering. In queries against the `orders` table, it denies access to the `customer_name` column and shows only rows that have 'pharma' in the `product_type` column.  
![The data filter window contains these fields, arranged vertically: Data filter name; Target database; Target table; Option button group with the options Access to all columns, Include columns, and Exclude columns; Select columns (drop-down list); Row filter expression (multi-line text box). The Exclude columns option is selected, the customer_name column is selected for exclusion, and the Row filter expression field contains 'product_type='pharma'.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/data-filter-sample-pharma.png)

1. Choose **Create filter**.

**To create a data filter with cell-filter policies on a nested field**

 This section uses the following sample schema to show how to create a data cells filter: 

```
[
    { name: "customer", type: "struct<customerId:string,customerName:string>" },
    { name: "customerApplication", type: "struct<appId:string>" },
    { name: "product", type: "struct<offer:struct<prodId:string,listingId:string>,type:string>" },
    { name: "purchaseId", type: "string" },
]
```

1. On the **Create a data filter**, page enter a name for the data filter.

1.  Next, use the drop-down to choose a database name and table name. 

1. In the **Column-level access** section, choose Included columns, and select a nested column (`customer.customerName`).

1. In the **Row-level access** section, choose the **Access to all rows** option.

1. Choose **Create filter**.

   When you grant `SELECT` permission on this filter, the principal gets access to all rows in the `customerName` column.

1. Next, define another data filter for the same database/table.

1. In the **Column-level access** section, choose Included columns, and select another nested column (`customer.customerid`).

1. In the **Row-level access** section, choose **Filter rows**, and enter a **Row filter expression** (`customer.customerid <> 5`).

1. Choose **Create filter**.

   When you grant `SELECT` permission on this filter, the principal receives access to all rows in the `customerName`, and `customerId` fields except the cell where the value is 5 in the `customerId` column.