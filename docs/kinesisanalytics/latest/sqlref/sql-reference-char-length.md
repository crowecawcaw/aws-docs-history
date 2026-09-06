

# CHAR\_LENGTH / CHARACTER\_LENGTH
<a name="sql-reference-char-length"></a>

```
 CHAR_LENGTH | CHARACTER_LENGTH ( <character-expression> )
```

Returns the length in characters of the string passed as the input argument. Returns null if input argument is null.

## Examples
<a name="sql-reference-char-length-examples"></a>


|  |  | 
| --- |--- |
|  <pre>CHAR_LENGTH('one')</pre>  |  3  | 
|  <pre>CHAR_LENGTH('')</pre>  |  0  | 
|  <pre>CHARACTER_LENGTH('fred')</pre>  |  4  | 
|  <pre>CHARACTER_LENGTH( cast (null as varchar(16) )</pre>  |  null  | 
|  <pre>CHARACTER_LENGTH( cast ('fred' as char(16) )</pre>  |  16  | 

## Limitations
<a name="sql-reference-char-length-limitations"></a>

Amazon Kinesis Data Analytics streaming SQL does not support the optional USING CHARACTERS \| OCTETS clause. This is a departure from the SQL:2008 standard.