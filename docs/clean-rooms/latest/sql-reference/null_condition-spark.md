

# Null condition
<a name="null_condition-spark"></a>

The NULL condition tests for nulls, when a value is missing or unknown. 

## Syntax
<a name="null_condition-synopsis"></a>

```
expression IS [ NOT ] NULL
```

## Arguments
<a name="null_condition-arguments"></a>

 *expression*   
Any expression such as a column. 

IS NULL   
Is true when the expression's value is null and false when it has a value. 

 IS NOT NULL   
Is false when the expression's value is null and true when it has a value. 

## Example
<a name="null_condition-example"></a>

This example indicates how many times the SALES table contains null in the QTYSOLD field: 

```
select count(*) from sales
where qtysold is null;
count
-------
0
(1 row)
```