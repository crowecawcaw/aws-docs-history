# PartiQL data types for DynamoDB

The following table lists the data types you can use with PartiQL for DynamoDB.

| DynamoDB data type | PartiQL representation   | Notes                                                                                                                                               |
| ------------------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| `Boolean`          | TRUE                     | FALSE                                                                                                                                               | Not case sensitive. |
| `Binary`           | N/A                      | Only supported via code.                                                                                                                            |
| `List`             | [ value1, value2,...]    | There are no restrictions on the data types that can be stored in a<br>List type, and the elements in a List do not have to be of the same<br>type. |
| `Map`              | { 'name' : value }       | There are no restrictions on the data types that can be stored in a<br>Map type, and the elements in a Map do not have to be of the same<br>type.   |
| `Null`             | NULL                     | Not case sensitive.                                                                                                                                 |
| `Number`           | 1, 1.0, 1e0              | Numbers can be positive, negative, or zero. Numbers can have up to 38<br>digits of precision.                                                       |
| `Number Set`       | <<number1, number2>>     | The elements in a number set must be of type Number.                                                                                                |
| `String Set`       | <<'string1', 'string2'>> | The elements in a string set must be of type String.                                                                                                |
| `String`           | 'string value'           | Single quotes must be used to specify String values.                                                                                                |

## Examples

The following statement demonstrates how to insert the following data types:
`String`, `Number`, `Map`, `List`,
`Number Set` and `String Set`.

```
INSERT INTO TypesTable value {'primarykey':'1',
'NumberType':1,
'MapType' : {'entryname1': 'value', 'entryname2': 4},
'ListType': [1,'stringval'],
'NumberSetType':<<1,34,32,4.5>>,
'StringSetType':<<'stringval','stringval2'>>
}
```

The following statement demonstrates how to insert new elements into the
`Map`, `List`, `Number Set` and `String
 Set` types and change the value of a `Number` type.

```
UPDATE TypesTable
SET NumberType=NumberType + 100
SET MapType.NewMapEntry=[2020, 'stringvalue', 2.4]
SET ListType = LIST_APPEND(ListType, [4, <<'string1', 'string2'>>])
SET NumberSetType= SET_ADD(NumberSetType, <<345, 48.4>>)
SET StringSetType = SET_ADD(StringSetType, <<'stringsetvalue1', 'stringsetvalue2'>>)
WHERE primarykey='1'
```

The following statement demonstrates how to remove elements from the
`Map`, `List`, `Number Set` and `String
 Set` types and change the value of a `Number` type.

```
UPDATE TypesTable
SET NumberType=NumberType - 1
REMOVE ListType[1]
REMOVE MapType.NewMapEntry
SET NumberSetType = SET_DELETE( NumberSetType, <<345>>)
SET StringSetType = SET_DELETE( StringSetType, <<'stringsetvalue1'>>)
WHERE primarykey='1'
```

For more information, see [DynamoDB data types](HowItWorks.md#HowItWorks.DataTypes "HowItWorks.md#HowItWorks.DataTypes").
