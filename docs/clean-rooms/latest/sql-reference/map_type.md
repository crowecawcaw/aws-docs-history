# MAP type

Use the MAP type to represent values comprising a set of key-value pairs.

```
map(keyType, valueType, valueContainsNull)
```

`keyType`: the data type of keys

`valueType`: the data type of values

Keys aren't allowed to have `null` values. Use
`valueContainsNull` to indicate if values of a MAP type value can have
`null` values.
