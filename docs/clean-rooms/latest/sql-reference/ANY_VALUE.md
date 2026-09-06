

# ANY\_VALUE function
<a name="ANY_VALUE"></a>

The ANY\_VALUE function returns any value from the input expression values nondeterministically. This function can return NULL if the input expression doesn't result in any rows being returned. 

## Syntax
<a name="ANY_VALUE-synopsis"></a>

```
ANY_VALUE (expression[, isIgnoreNull] )
```

## Arguments
<a name="ANY_VALUE-arguments"></a>

 *expression *   
The target column or expression on which the function operates. The *expression* is one of the following data types:

*isIgnoreNull*  
A boolean that determines if the function should return only non-null values.

## Returns
<a name="ANY_VALUE-returns"></a>

Returns the same data type as *expression*. 

## Usage notes
<a name="ANY_VALUE-usage-notes"></a>

If a statement that specifies the ANY\_VALUE function for a column also includes a second column reference, the second column must appear in a GROUP BY clause or be included in an aggregate function. 

## Examples
<a name="ANY_VALUE-examples"></a>

The following example returns an instance of any `dateid` where the `eventname` is `Eagles`. 

```
select any_value(dateid) as dateid, eventname from event where eventname ='Eagles' group by eventname;
```

Following are the results.

```
dateid | eventname
-------+---------------
 1878  | Eagles
```

The following example returns an instance of any `dateid` where the `eventname` is `Eagles` or `Cold War Kids`. 

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