# x-amazon-apigateway-tag-value property

Specifies the value of an [AWS tag](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") for an HTTP API. You can use the `x-amazon-apigateway-tag-value` property as part of the root-level [OpenAPI tag object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#tag-object "https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#tag-object") to specify AWS tags for
an HTTP API. If you specify a tag name without the `x-amazon-apigateway-tag-value` property, API Gateway creates a tag with an empty string for a value.

To learn more about tagging, see [Tagging your API Gateway resources](apigateway-tagging.md "apigateway-tagging.md").

| Property name                   | Type     | Description              |
| ------------------------------- | -------- | ------------------------ |
| `name`                          | `String` | Specifies the tag key.   |
| `x-amazon-apigateway-tag-value` | `String` | Specifies the tag value. |

## `x-amazon-apigateway-tag-value` example

The following example specifies two tags for an HTTP API:

- "Owner": "Admin"
- "Prod": ""

```
"tags": [
    {
      "name": "Owner",
      "x-amazon-apigateway-tag-value": "Admin"
    },
    {
      "name": "Prod"
    }
]
```
