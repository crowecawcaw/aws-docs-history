# IP_TO_INT

Converts the Internet Protocol version 4 (IPv4) value of the source column or other value to the corresponding
integer value in the target column, and returns the result in a new column. This
function works for IPv4 only.

For example, consider the following IP address.

```
192.168.1.1
```

If you use this value as an input to `IP_TO_INT`, the output value is
as follows.

```
3232235777
```

###### Parameters

- `sourceColumn` – The name of an existing column.
- `value` – A character string to evaluate.
- `targetColumn` – The name of the new column to be created.
  You can specify either `sourceColumn` or `value`, but not
  both.

###### Example

```
{
    "RecipeAction": {
        "Operation": "IP_TO_INT",
        "Parameters": {
            "sourceColumn": "my_ip_address",
            "targetColumn": "IP_TO_INT Column 1"
        }
    }
}
```
