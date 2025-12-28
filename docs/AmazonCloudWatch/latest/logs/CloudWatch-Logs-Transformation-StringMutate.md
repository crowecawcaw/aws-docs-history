# String mutate

processors

This section contains information about the string mutate processors that you can use with a log event
transformer.

###### Contents

- [lowerCaseString](CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-lowerCaseString "CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-lowerCaseString")
- [upperCaseString](CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-upperCaseString "CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-upperCaseString")
- [splitString](CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-splitString "CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-splitString")
- [substituteString](CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-substituteString "CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-substituteString")
- [trimString](CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-trimString "CloudWatch-Logs-Transformation-StringMutate.md#CloudWatch-Logs-Transformation-trimString")

## lowerCaseString

The `lowerCaseString` processor converts a string to its lowercase
version.

| Field    | Description                            | Required? | Default | Limits              |
| -------- | -------------------------------------- | --------- | ------- | ------------------- |
| withKeys | A list of keys to convert to lowercase | Yes       |         | Maximum entries: 10 |

**Example**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "INNER_VALUE"
    }
}
```

The transformer configuration is this, using `lowerCaseString` with
`parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "lowerCaseString": {
            "withKeys":["outer_key.inner_key"]
        }
    }
]

```

The transformed log event would be the following.

```
{
  "outer_key": {
    "inner_key": "inner_value"
  }
}
```

## upperCaseString

The `upperCaseString` processor converts a string to its uppercase
version.

| Field    | Description                            | Required? | Default | Limits              |
| -------- | -------------------------------------- | --------- | ------- | ------------------- |
| withKeys | A list of keys to convert to uppercase | Yes       |         | Maximum entries: 10 |

**Example**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "inner_value"
    }
}
```

The transformer configuration is this, using `upperCaseString` with
`parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "upperCaseString": {
            "withKeys":["outer_key.inner_key"]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "outer_key": {
    "inner_key": "INNER_VALUE"
  }
}
```

## splitString

The `splitString` processor is a type of string mutate processor
which splits a field into an array using a delimiting character.

| Field     | Description                                                                                  | Required? | Default | Limits              |
| --------- | -------------------------------------------------------------------------------------------- | --------- | ------- | ------------------- |
| entries   | Array of entries. Each item in the array must contain<br>`source` and `delimiter`<br>fields. | Yes       |         | Maximum entries: 10 |
| source    | The key of the field value to split                                                          | Yes       |         | Maximum length: 128 |
| delimiter | The delimiter string to split the field value on                                             | Yes       |         | Maximum length: 128 |

**Example 1**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "inner_value"
    }
}
```

The transformer configuration is this, using `splitString` with
`parseJSON`:

```
[
     {
        "parseJSON": {}
    },
    {
         "splitString": {
            "entries": [
                {
                    "source": "outer_key.inner_key",
                    "delimiter": "_"
                }
            ]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "outer_key": {
    "inner_key": [
      "inner",
      "value"
    ]
  }
}
```

**Example 2**

The delimiter to split the string on can be multiple characters long.

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "item1, item2, item3"
    }
}
```

The transformer configuration is as follows:

```
[
     {
        "parseJSON": {}
    },
    {
         "splitString": {
            "entries": [
                {
                    "source": "outer_key.inner_key",
                    "delimiter": ", "
                }
            ]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "outer_key": {
    "inner_key": [
      "item1",
      "item2",
      "item3"
    ]
  }
}
```

## substituteString

The `substituteString` processor is a type of string mutate
processor which matches a key’s value against a regular expression and replaces
all matches with a replacement string.

| Field   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required? | Default | Limits                                                                                                          |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| entries | Array of entries. Each item in the array must contain<br>`source`, `from`, and `to`<br>fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes       |         | Maximum entries: 10                                                                                             |
| source  | The key of the field to modify                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes       |         | Maximum length: 128<br>Maximum nested key depth: 3                                                              |
| from    | The regular expression string to be replaced. Special<br>regex characters such as [ and ] must be escaped using \\<br>when using double quotes and with \ when using single quotes<br>or when configured from the AWS Management Console. For more information,<br>see [Class Pattern](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html") on the Oracle web site.<br>You can wrap a pattern in `(...)` to create a<br>numbered capturing group and create<br>`(?P<group_name>...)` named capturing<br>groups that can be referenced in the `to`<br>field. | Yes       |         | Maximum length: 128                                                                                             |
| to      | The string to be substituted for each match of<br>`from` Backreferences to capturing groups can be<br>used. Use the form $n for numbered groups such as<br>`$1` and use `${group_name}` for named<br>groups such as $`{my_group}`.>                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes       |         | Maximum length: 128<br>Maximum number of backreferences: 10<br>Maximum number of duplicate backreferences:<br>2 |

**Example 1**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key1": "[]",
        "inner_key2": "123-345-567",
        "inner_key3": "A cat takes a catnap."
    }
}
```

The transformer configuration is this, using `substituteString`
with `parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "substituteString": {
            "entries": [
                {
                    "source": "outer_key.inner_key1",
                    "from": "\\[\\]",
                    "to": "value1"
                },
                {
                    "source": "outer_key.inner_key2",
                    "from": "[0-9]{3}-[0-9]{3}-[0-9]{3}",
                    "to": "xxx-xxx-xxx"
                },
                {
                    "source": "outer_key.inner_key3",
                    "from": "cat",
                    "to": "dog"
                }
            ]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "outer_key": {
    "inner_key1": "value1",
    "inner_key2": "xxx-xxx-xxx",
    "inner_key3": "A dog takes a dognap."
  }
}
```

**Example 2**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key1": "Tom, Dick, and Harry",
        "inner_key2": "arn:aws:sts::123456789012:assumed-role/MyImportantRole/MySession"
    }
}
```

The transformer configuration is this, using `substituteString`
with `parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "substituteString": {
            "entries": [
                {
                    "source": "outer_key.inner_key1",
                    "from": "(\w+), (\w+), and (\w+)",
                    "to": "$1 and $3"
                },
                {
                    "source": "outer_key.inner_key2",
                    "from": "^arn:aws:sts::(?P<account_id>\\d{12}):assumed-role/(?P<role_name>[\\w+=,.@-]+)/(?P<role_session_name>[\\w+=,.@-]+)$",
                    "to": "${account_id}:${role_name}:${role_session_name}"
                }
            ]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "outer_key": {
    "inner_key1": "Tom and Harry",
    "inner_key2": "123456789012:MyImportantRole:MySession"
  }
}
```

## trimString

The `trimString` processor removes whitespace from the beginning
and end of a key.

| Field    | Description            | Required? | Default | Limits              |
| -------- | ---------------------- | --------- | ------- | ------------------- |
| withKeys | A list of keys to trim | Yes       |         | Maximum entries: 10 |

**Example**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "   inner_value  "
    }
}
```

The transformer configuration is this, using `trimString` with
`parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "trimString": {
            "withKeys":["outer_key.inner_key"]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "outer_key": {
    "inner_key": "inner_value"
  }
}
```
