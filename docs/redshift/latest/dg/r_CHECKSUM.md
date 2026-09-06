

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CHECKSUM function
<a name="r_CHECKSUM"></a>

Computes a checksum value for building a hash index. 

## Syntax
<a name="r_CHECKSUM-synopsis"></a>

```
CHECKSUM(expression)
```

## Argument
<a name="r_CHECKSUM-argument"></a>

 *expression*   
The input expression must be a VARCHAR, INTEGER, or DECIMAL data type. 

## Return type
<a name="r_CHECKSUM-return-type"></a>

The CHECKSUM function returns an integer. 

## Example
<a name="r_CHECKSUM-example"></a>

The following example computes a checksum value for the COMMISSION column: 

```
select checksum(commission)
from sales
order by salesid
limit 10;

checksum
----------
10920
1140
5250
2625
2310
5910
11820
2955
8865
975
(10 rows)
```