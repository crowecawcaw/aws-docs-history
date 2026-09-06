

# Add tags when an application is created
<a name="how-tagging-create"></a>

You add tags when creating an application using the `tags` parameter of the [CreateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html) action.

The following example request shows the `Tags` node for a `CreateApplication` request:

```
"Tags": [ 
    { 
        "Key": "Key1",
        "Value": "Value1"
    },
    { 
        "Key": "Key2",
        "Value": "Value2"
    }
]
```