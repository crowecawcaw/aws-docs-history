

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# EXISTS condition
<a name="r_exists_condition"></a>

EXISTS conditions test for the existence of rows in a subquery, and return true if a subquery returns at least one row. If NOT is specified, the condition returns true if a subquery returns no rows.

## Syntax
<a name="r_exists_condition-synopsis"></a>

```
[ NOT ] EXISTS (table_subquery)
```

## Arguments
<a name="r_exists_condition-arguments"></a>

 EXISTS   
Is true when the *table\_subquery* returns at least one row.

NOT EXISTS   
Is true when the *table\_subquery* returns no rows.

 *table\_subquery*   
A subquery that evaluates to a table with one or more columns and one or more rows.

## Example
<a name="r_exists_condition-example"></a>

This example returns all date identifiers, one time each, for each date that had a sale of any kind:

```
select dateid from date
where exists (
select 1 from sales
where date.dateid = sales.dateid
)
order by dateid;

dateid
--------
1827
1828
1829
...
```