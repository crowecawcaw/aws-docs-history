

# INITCAP
<a name="sql-reference-initcap"></a>

```
INITCAP ( <character-expression> )
```

Returns a converted version of the input string such that the first character of each space-delimited word is upper-cased, and all other characters are lower-cased.

## Examples
<a name="sql-reference-initcap-examples"></a>


| Function | Result | 
| --- | --- | 
| INITCAP('Each FIRST lEtTeR is cAPITALIZED') | Each First Letter Is Capitalized | 

## 
<a name="sqlrf-initcap-notes"></a>

**Note**  
The INITCAP function is not part of the SQL:2008 standard. It is an Amazon Kinesis Data Analytics extension.