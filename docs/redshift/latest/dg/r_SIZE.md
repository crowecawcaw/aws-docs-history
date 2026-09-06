

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SIZE
<a name="r_SIZE"></a>

 Returns the binary in-memory size of a `SUPER` type constant or expression as an `INTEGER`. 

## Syntax
<a name="r_SIZE-synopsis"></a>

```
SIZE(super_expression)
```

## Arguments
<a name="r_SIZE-parameters"></a>

*super\_expression*  
 A `SUPER` type constant or expression. 

## Return type
<a name="r_SIZE-returns"></a>

`INTEGER`

## Examples
<a name="r_SIZE-examples"></a>

 To use SIZE to get the in-memory size of several `SUPER` type expressions, use the following example. 

```
CREATE TABLE test_super_size(a SUPER);
            
INSERT INTO test_super_size 
VALUES
  (null),
  (TRUE),
  (JSON_PARSE('[0,1,2,3]')),
  (JSON_PARSE('{"a":0,"b":1,"c":2,"d":3}'))
;

SELECT a, SIZE(a) 
FROM test_super_size 
ORDER BY 2, 1;

+---------------------------+------+
|             a             | size |
+---------------------------+------+
| true                      |    4 |
| NULL                      |    4 |
| [0,1,2,3]                 |   23 |
| {"a":0,"b":1,"c":2,"d":3} |   52 |
+---------------------------+------+
```