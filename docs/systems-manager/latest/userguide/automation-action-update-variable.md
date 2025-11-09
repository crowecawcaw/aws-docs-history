AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# `aws:updateVariable`

– Updates a value for a runbook variable

This action updates a value for a runbook variable. The data type of the value must
match the data type of the variable you want to update. Data type conversions aren't
supported. The `onCancel` property isn't supported for the
`aws:updateVariable` action.

###### Input

The input is as follows.

YAML

```
name: updateStringList
action: aws:updateVariable
inputs:
    Name: variable:`variable name`
    Value:
    - "1"
    - "2"
```

JSON

```
{
    "name": "updateStringList",
    "action": "aws:updateVariable",
    "inputs": {
        "Name": "variable:`variable name`",
        "Value": ["1","2"]
    }
}
```

Name

The name of the variable whose value you want to update. You must use the
format `variable:`variable name``

Type: String

Required: Yes

Value

The new value to assign to the variable. The value must match the data
type of the variable. Data type conversions aren't supported.

Type: Boolean | Integer | MapList | String | StringList | StringMap

Required: Yes

Constraints:

- MapList can contain a maximum number of 200 items.
- Key lengths can be a minimum length of 1 and a maximum length of

50.

- StringList can be a minimum number of 0 items and a maximum number
  of 50 items.
- String lengths can be a minimum length of 1 and a maximum length
  of 512.

###### Output

None
