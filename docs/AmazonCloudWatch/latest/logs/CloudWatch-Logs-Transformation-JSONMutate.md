

# JSON mutate processors
<a name="CloudWatch-Logs-Transformation-JSONMutate"></a>

This section contains information about the JSON mutate processors that you can use with a log event transformer. 

**Contents**
+ [addKeys](#CloudWatch-Logs-Transformation-addKeys)
+ [deleteKeys](#CloudWatch-Logs-Transformation-deleteKeys)
+ [moveKeys](#CloudWatch-Logs-Transformation-moveKeys)
+ [renameKeys](#CloudWatch-Logs-Transformation-renameKeys)
+ [copyValue](#CloudWatch-Logs-Transformation-copyValue)
+ [listToMap](#CloudWatch-Logs-Transformation-listToMap)

## addKeys
<a name="CloudWatch-Logs-Transformation-addKeys"></a>

Use the `addKeys` processor to add new key-value pairs to the log event. 


| Field | Description | Required? | Default | Limits | 
| --- | --- | --- | --- | --- | 
| entries | Array of entries. Each item in the array can contain key, value, and overwriteIfExists fields. | Yes |  | Maximum entries: 5 | 
| key | The key of the new entry to be added | Yes |  | Maximum length: 128<br />Maximum nested key depth: 3 | 
| value | The value of the new entry to be added | Yes |  | Maximum length: 256 | 
| overwriteIfExists | If you set this to true, the existing value is overwritten if key already exists in the event. The default value is false.  | No | false | No limit | 

**Example**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "inner_value"
    }
}
```

The transformer configuration is this, using `addKeys` with `parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "addKeys": {
            "entries": [
                {
                    "key": "outer_key.new_key",
                    "value": "new_value"
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
    "inner_key": "inner_value",
    "new_key": "new_value"
  }
}
```

## deleteKeys
<a name="CloudWatch-Logs-Transformation-deleteKeys"></a>

Use the `deleteKeys` processor to delete fields from a log event. These fields can include key-value pairs. 


| Field | Description | Required? | Default | Limits | 
| --- | --- | --- | --- | --- | 
| withKeys | The list of keys to delete. | Yes | No limit | Maximum entries: 5 | 

**Example**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "inner_value"
    }
}
```

The transformer configuration is this, using `deleteKeys` with `parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "deleteKeys": {
            "withKeys":["outer_key.inner_key"]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "outer_key": {}
}
```

## moveKeys
<a name="CloudWatch-Logs-Transformation-moveKeys"></a>

Use the `moveKeys` processor to move a key from one field to another. 


| Field | Description | Required? | Default | Limits | 
| --- | --- | --- | --- | --- | 
| entries | Array of entries. Each item in the array can contain source, target, and overwriteIfExists fields. | Yes |  | Maximum entries: 5 | 
| source | The key to move | Yes |  | Maximum length: 128<br />Maximum nested key depth: 3 | 
| target | The key to move to | Yes |  | Maximum length: 128<br />Maximum nested key depth: 3 | 
| overwriteIfExists | If you set this to true, the existing value is overwritten if key already exists in the event. The default value is false.  | No | false | No limit | 

**Example**

Take the following example log event:

```
{
    "outer_key1": {
        "inner_key1": "inner_value1"
    },
    "outer_key2": {
        "inner_key2": "inner_value2"
    }
}
```

The transformer configuration is this, using `moveKeys` with `parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "moveKeys": {
            "entries": [
                {
                    "source": "outer_key1.inner_key1",
                    "target": "outer_key2"
                }
            ]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "outer_key1": {},
  "outer_key2": {
    "inner_key2": "inner_value2",
    "inner_key1": "inner_value1"
  }
}
```

## renameKeys
<a name="CloudWatch-Logs-Transformation-renameKeys"></a>

Use the `renameKeys` processor to rename keys in a log event. 


| Field | Description | Required? | Default | Limits | 
| --- | --- | --- | --- | --- | 
| entries | Array of entries. Each item in the array can contain key, target, and overwriteIfExists fields. | Yes | No limit | Maximum entries: 5 | 
| key | The key to rename | Yes | No limit | Maximum length: 128 | 
| target | The new key name | Yes | No limit | Maximum length: 128<br />Maximum nested key depth: 3 | 
| overwriteIfExists | If you set this to true, the existing value is overwritten if key already exists in the event. The default value is false.  | No | false | No limit | 

**Example**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "inner_value"
    }
}
```

The transformer configuration is this, using `renameKeys` with `parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "renameKeys": {
            "entries": [
                {
                    "key": "outer_key",
                    "target": "new_key"
                }
            ]
        }
    }
]
```

The transformed log event would be the following.

```
{
  "new_key": {
    "inner_key": "inner_value"
  }
}
```

## copyValue
<a name="CloudWatch-Logs-Transformation-copyValue"></a>

Use the `copyValue` processor to copy values within a log event. You can also use this processor to add metadata to log events, by copying the values of the following metadata keys into the log events: `@logGroupName`, `@logGroupStream`, `@accountId`, `@regionName`. This is illustrated in the following example.


| Field | Description | Required? | Default | Limits | 
| --- | --- | --- | --- | --- | 
| entries | Array of entries. Each item in the array can contain source, target, and overwriteIfExists fields. | Yes |  | Maximum entries: 5 | 
| source | The key to copy | Yes |  | Maximum length: 128<br />Maximum nested key depth: 3 | 
| target | The key to copy the value to | Yes | No limit | Maximum length: 128<br />Maximum nested key depth: 3 | 
| overwriteIfExists | If you set this to true, the existing value is overwritten if key already exists in the event. The default value is false.  | No | false | No limit | 

**Example**

Take the following example log event:

```
{
    "outer_key": {
        "inner_key": "inner_value"
    }
}
```

The transformer configuration is this, using `copyValue` with `parseJSON`:

```
[
    {
        "parseJSON": {}
    },
    {
        "copyValue": {
            "entries": [
                {
                    "key": "outer_key.new_key",
                    "target": "new_key"
                },
                {
                    "source": "@logGroupName",
                    "target": "log_group_name"
                },
                {
                    "source": "@logGroupStream",
                    "target": "log_group_stream"
                },
                {
                    "source": "@accountId",
                    "target": "account_id"
                },
                {
                    "source": "@regionName",
                    "target": "region_name"
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
    "inner_key": "inner_value"
  },
  "new_key": "inner_value",
  "log_group_name": "myLogGroupName",
  "log_group_stream": "myLogStreamName",
  "account_id": "012345678912",
  "region_name": "us-east-1"
}
```

## listToMap
<a name="CloudWatch-Logs-Transformation-listToMap"></a>

The `listToMap` processor takes a list of objects that contain key fields, and converts them into a map of target keys. 


| Field | Description | Required? | Default | Limits | 
| --- | --- | --- | --- | --- | 
| source | The key in the ProcessingEvent with a list of objects that will be converted to a map | Yes |  | Maximum length: 128<br />Maximum nested key depth: 3 | 
| key | The key of the fields to be extracted as keys in the generated map | Yes |  | Maximum length: 128 | 
| valueKey | If this is specified, the values that you specify in this parameter will be extracted from the source objects and put into the values of the generated map. Otherwise, original objects in the source list will be put into the values of the generated map. | No |  | Maximum length: 128 | 
| target | The key of the field that will hold the generated map  | No | Root node | Maximum length: 128<br />Maximum nested key depth: 3 | 
| flatten | A Boolean value to indicate whether the list will be flattened into single items or if the values in the generated map will be lists.<br />By default the values for the matching keys will be represented in an array. Set `flatten` to `true` to convert the array to a single value based on the value of `flattenedElement`. | No | false |  | 
| flattenedElement | If you set flatten to true, use flattenedElement to specify which element, first or last, to keep.  | Required when `flatten` is set to `true` |  | Value can only be first or last | 

**Example**

Take the following example log event:

```
{
    "outer_key": [
        {
            "inner_key": "a",
            "inner_value": "val-a"
        },
        {
            "inner_key": "b",
            "inner_value": "val-b1"
        },
        {
            "inner_key": "b",
            "inner_value": "val-b2"
        },
        {
            "inner_key": "c",
            "inner_value": "val-c"
        }
    ]
}
```

**Transformer for use case 1:** `flatten` is `false`

```
[
    {
        "parseJSON": {}
    },
    {
        "listToMap": {
            "source": "outer_key"
            "key": "inner_key",
            "valueKey": "inner_value",
            "flatten": false
        }
    }
]
```

The transformed log event would be the following.

```
{
    "outer_key": [
        {
            "inner_key": "a",
            "inner_value": "val-a"
        },
        {
            "inner_key": "b",
            "inner_value": "val-b1"
        },
        {
            "inner_key": "b",
            "inner_value": "val-b2"
        },
        {
            "inner_key": "c",
            "inner_value": "val-c"
        }
    ],
    "a": [
        "val-a"
    ],
    "b": [
        "val-b1",
        "val-b2"
    ],
    "c": [
        "val-c"
    ]
}
```

**Transformer for use case 2:** `flatten` is `true` and `flattenedElement` is `first`

```
[
    {
        "parseJSON": {}
    },
    {
        "listToMap": {
            "source": "outer_key"
            "key": "inner_key",
            "valueKey": "inner_value",
            "flatten": true,
            "flattenedElement": "first"
        }
    }
]
```

The transformed log event would be the following.

```
{
    "outer_key": [
        {
            "inner_key": "a",
            "inner_value": "val-a"
        },
        {
            "inner_key": "b",
            "inner_value": "val-b1"
        },
        {
            "inner_key": "b",
            "inner_value": "val-b2"
        },
        {
            "inner_key": "c",
            "inner_value": "val-c"
        }
    ],
    "a": "val-a",
    "b": "val-b1",
    "c": "val-c"
}
```

**Transformer for use case 3:** `flatten` is `true` and `flattenedElement` is `last`

```
[
    {
        "parseJSON": {}
    },
    {
        "listToMap": {
            "source": "outer_key"
            "key": "inner_key",
            "valueKey": "inner_value",
            "flatten": true,
            "flattenedElement": "last"
        }
    }
]
```

The transformed log event would be the following.

```
{
    "outer_key": [
        {
            "inner_key": "a",
            "inner_value": "val-a"
        },
        {
            "inner_key": "b",
            "inner_value": "val-b1"
        },
        {
            "inner_key": "b",
            "inner_value": "val-b2"
        },
        {
            "inner_key": "c",
            "inner_value": "val-c"
        }
    ],
    "a": "val-a",
    "b": "val-b2",
    "c": "val-c"
}
```