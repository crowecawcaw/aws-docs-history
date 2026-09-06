

# BTRIM function
<a name="BTRIM"></a>

The BTRIM function trims a string by removing leading and trailing blanks or by removing leading and trailing characters that match an optional specified string. 

## Syntax
<a name="BTRIM-synopsis"></a>

```
BTRIM(string [, trim_chars ] )
```

## Arguments
<a name="BTRIM-arguments"></a>

 *string*   
The input VARCHAR string to be trimmed. 

 *trim\_chars*   
The VARCHAR string containing the characters to be matched. 

## Return type
<a name="BTRIM-return-type"></a>

The BTRIM function returns a VARCHAR string. 

## Examples
<a name="BTRIM-examples"></a>

The following example trims leading and trailing blanks from the string `' abc '`: 

```
select '     abc    ' as untrim, btrim('     abc    ') as trim;

untrim    | trim
----------+------
   abc    | abc
```

The following example removes the leading and trailing `'xyz'` strings from the string `'xyzaxyzbxyzcxyz'`. The leading and trailing occurrences of `'xyz'` are removed, but occurrences that are internal within the string are not removed. 

```
select 'xyzaxyzbxyzcxyz' as untrim,
btrim('xyzaxyzbxyzcxyz', 'xyz') as trim;

     untrim      |   trim
-----------------+-----------
 xyzaxyzbxyzcxyz | axyzbxyzc
```

The following example removes the leading and trailing parts from the string `'setuphistorycassettes'` that match any of the characters in the *trim\_chars* list `'tes'`. Any `t`, `e`, or `s` that occur before another character that is not in the *trim\_chars* list at the beginning or ending of the input string are removed. 

```
SELECT btrim('setuphistorycassettes', 'tes');

     btrim      
-----------------
 uphistoryca
```