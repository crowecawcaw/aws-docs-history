

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# MOD function
<a name="r_MOD"></a>

Returns the remainder of two numbers, otherwise known as a *modulo* operation. To calculate the result, the first parameter is divided by the second.

## Syntax
<a name="r_MOD-synopsis"></a>

```
MOD(number1, number2)
```

## Arguments
<a name="r_MOD-arguments"></a>

 *number1*   
The first input parameter is an `INTEGER`, `SMALLINT`, `BIGINT`, or `DECIMAL` number. If either parameter is a `DECIMAL` type, the other parameter must also be a `DECIMAL` type. If either parameter is an `INTEGER`, the other parameter can be an `INTEGER`, `SMALLINT`, or `BIGINT`. Both parameters can also be `SMALLINT` or `BIGINT`, but one parameter cannot be a `SMALLINT` if the other is a `BIGINT`. 

 *number2*   
The second parameter is an `INTEGER`, `SMALLINT`, `BIGINT`, or `DECIMAL` number. The same data type rules apply to *number2* as to *number1*. 

## Return type
<a name="r_MOD-return-type"></a>

The return type of the MOD function is the same numeric type as the input parameters, if both input parameters are the same type. If either input parameter is an `INTEGER`, however, the return type will also be an `INTEGER`. Valid return types are `DECIMAL`, `INT`, `SMALLINT`, and `BIGINT`.

## Usage notes
<a name="r_MOD-usage-notes"></a>

You can use `%` as a modulo operator.

## Examples
<a name="r_MOD-example"></a>

To return the remainder when a number is divided by another, use the following example.

```
SELECT MOD(10, 4);
               
+-----+
| mod |
+-----+
|   2 |
+-----+
```

To return a `DECIMAL` result when using the MOD function, use the following example.

```
SELECT MOD(10.5, 4);
               
+-----+
| mod |
+-----+
| 2.5 |
+-----+
```

To cast a number before running the MOD function, use the following example. For more information, see [CAST function](r_CAST_function.md).

```
SELECT MOD(CAST(16.4 AS INTEGER), 5);
               
+-----+
| mod |
+-----+
|   1 |
+-----+
```

To check if the first parameter is even by dividing it by 2, use the following example.

```
SELECT mod(5,2) = 0 AS is_even;
               
+---------+
| is_even |
+---------+
| false   |
+---------+
```

To use *%* as a modulo operator, use the following example.

```
SELECT 11 % 4 as remainder;
               
 +-----------+
| remainder |
+-----------+
|         3 |
+-----------+
```

The following example uses the TICKIT sample database. For more information, see [Sample database](c_sampledb.md).

To return information for odd-numbered categories in the CATEGORY table, use the following example. 

```
SELECT catid, catname
FROM category
WHERE MOD(catid,2)=1
ORDER BY 1,2;

+-------+-----------+
| catid |  catname  |
+-------+-----------+
|     1 | MLB       |
|     3 | NFL       |
|     5 | MLS       |
|     7 | Plays     |
|     9 | Pop       |
|    11 | Classical |
+-------+-----------+
```