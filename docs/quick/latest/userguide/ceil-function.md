

# Ceil
<a name="ceil-function"></a>

`ceil` rounds a decimal value to the next highest integer. For example, `ceil(29.02)` returns `30`.

## Syntax
<a name="ceil-function-syntax"></a>

```
ceil({{decimal}})
```

## Arguments
<a name="ceil-function-arguments"></a>

 *decimal*   
A field that uses the decimal data type, a literal value like **17.62**, or a call to another function that outputs a decimal.

## Return type
<a name="ceil-function-return-type"></a>

Integer

## Example
<a name="ceil-function-example"></a>

The following example rounds a decimal field to the next highest integer.

```
ceil(salesAmount)
```

The following are the given field values.

```
20.13
892.03
57.54
```

For these field values, the following values are returned.

```
21
893
58
```