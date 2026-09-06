

# UNHEX function
<a name="UNHEX"></a>

The UNHEX function converts a hexadecimal string back to its original string representation.

This function can be useful in scenarios where you need to work with data that has been stored or transmitted in a hexadecimal format, and you need to restore the original string representation for further processing or display.

The UNHEX function is the counterpart to the [HEX function](HEX.md).

## Syntax
<a name="UNHEX-syntax"></a>

```
unhex(expr)
```

## Arguments
<a name="UNHEX-arguments"></a>

 *expr*   
A STRING expression of hexadecimal characters.

## Return type
<a name="UNHEX-returns"></a>

UNHEX returns a BINARY. 

If the length of *expr* is odd, the first character is discarded and the result is padded with a null byte. If *expr* contains non hex characters the result is NULL.

## Example
<a name="UNHEX-example"></a>

The following example converts a hexadecimal string back to its original string representation by using the UNHEX() and DECODE() functions together. The first part of the query, uses the UNHEX() function to convert the hexadecimal string '537061726B2053514C' to its binary representation. The second part of the query, uses the DECODE() function to convert the binary data obtained from the UNHEX() function back to a string, using the 'UTF-8' character encoding. The output of the query, is he original string 'Spark\_SQL' that was converted to hexadecimal and then back to a string.

```
SELECT decode(unhex('537061726B2053514C'), 'UTF-8');
 Spark SQL
```