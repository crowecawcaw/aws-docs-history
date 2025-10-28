Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Add tags when an application is created

You add tags when creating an application using the `tags` parameter of the [CreateApplication](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md") action.

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
