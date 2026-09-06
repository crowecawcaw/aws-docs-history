

# BASE64 function
<a name="base64"></a>

The BASE64 function converts an expression to a base 64 string using [RFC2045 Base64 transfer encoding for MIME](https://datatracker.ietf.org/doc/html/rfc2045).

## Syntax
<a name="base64-syntax"></a>

```
base64(expr)
```

## Arguments
<a name="base64-arguments"></a>

 *expr*   
A BINARY expression or a STRING which the function will interpret as BINARY.

## Return type
<a name="base64-return-type"></a>

`STRING`

## Example
<a name="base64-example"></a>

To convert the given string input into its Base64 encoded representation. use the following example. The result is the Base64 encoded representation of the input string 'Spark SQL', which is 'U3BhcmsgU1FM'.

```
SELECT base64('Spark SQL');
 U3BhcmsgU1FM
```