

# xxHASH64 function
<a name="xxhash64"></a>

The xxhash64 function returns a 64-bit hash value of the arguments. 

The xxhash64() function is a non-cryptographic hash function designed to be fast and efficient. It's often used in data processing and storage applications, where a unique identifier for a piece of data is needed, but the exact contents of the data don't need to be kept secret. 

In the context of a SQL query, the xxhash64() function could be used for various purposes, such as: 
+ Generating a unique identifier for a row in a table 
+ Partitioning data based on a hash value 
+ Implementing custom indexing or data distribution strategies 

The specific use case would depend on the requirements of the application and the data being processed.

## Syntax
<a name="xxhash64-syntax"></a>

```
xxhash64(expr1, expr2, ...)
```

## Arguments
<a name="xxhash64-arguments"></a>

*expr1*  
An expression of any type.

*expr2*  
An expression of any type.

## Returns
<a name="xxhash64-returns"></a>

Returns a 64-bit hash value of the arguments (BIGINT). Hash seed is 42.

## Example
<a name="xxhash64-example"></a>

The following example generates a 64-bit hash value (5602566077635097486) based on the provided input. The first argument is a string value, in this case, the word "Spark". The second argument is an array containing the single integer value 123. The third argument is an integer value representing the seed for the hash function.

```
SELECT xxhash64('Spark', array(123), 2);
 5602566077635097486
```