

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ANY\_VALUE function
<a name="r_ANY_VALUE"></a>

The ANY\_VALUE function returns any value from the input expression values nondeterministically. This function returns `NULL` if the input expression doesn't result in any rows being returned. The function can also return `NULL` if there are `NULL` values in the input expression. If the input contains `NULL` values mixed with non-`NULL` values, `NULL` might be returned. If all values are `NULL`, `NULL` is returned. If no rows match the condition, `NULL` is returned.

## Syntax
<a name="r_ANY_VALUE-synopsis"></a>

```
ANY_VALUE( [ DISTINCT | ALL ] expression )
```

## Arguments
<a name="r_ANY_VALUE-arguments"></a>

DISTINCT \| ALL  
Specify either DISTINCT or ALL to return any value from the input expression values. The DISTINCT argument has no effect and is ignored.

 *expression *   
The target column or expression on which the function operates. The *expression* is one of the following data types:  
+ SMALLINT
+ INTEGER
+ BIGINT
+ DECIMAL
+ REAL
+ DOUBLE PRECISON
+ BOOLEAN
+ CHAR
+ VARCHAR
+ DATE
+ TIMESTAMP
+ TIMESTAMPTZ
+ TIME
+ TIMETZ
+ INTERVAL YEAR TO MONTH
+ INTERVAL DAY TO SECOND
+ VARBYTE
+ SUPER
+ HLLSKETCH
+ GEOMETRY
+ GEOGRAPHY

## Returns
<a name="r_ANY_VALUE-returns"></a>

Returns the same data type as *expression*. 

## Usage notes
<a name="r_ANY_VALUE-usage-notes"></a>

If a statement that specifies the ANY\_VALUE function for a column also includes a second column reference, the second column must appear in a GROUP BY clause or be included in an aggregate function. 

## Examples
<a name="r_ANY_VALUE-examples"></a>

The examples use the event table that is created in [Step 4: Load sample data from Amazon S3](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-sample-db.html) in the *Amazon Redshift Getting Started Guide*. The following example returns an instance of any dateid where the eventname is Eagles. 

```
select any_value(dateid) as dateid, eventname from event where eventname ='Eagles' group by eventname;
```

Following are the results.

```
dateid | eventname
-------+---------------
 1878  | Eagles
```

The following example returns an instance of any dateid where the eventname is Eagles or Cold War Kids. 

```
select any_value(dateid) as dateid, eventname from event where eventname in('Eagles', 'Cold War Kids') group by eventname;
```

Following are the results.

```
dateid | eventname
-------+---------------
 1922  | Cold War Kids
 1878  | Eagles
```