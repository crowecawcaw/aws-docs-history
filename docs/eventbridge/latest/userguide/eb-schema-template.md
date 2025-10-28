# Creating a schema by using a template in Amazon EventBridge

You can create a schema from a template file you download, or by editing a template directly in the EventBridge
console.

## Create a schema from a template file

To get the template, you download it from the console. You can edit the
template so that the schema matches your events. Then upload your new template through
the console.

###### To download the schema template

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Schema registry**.
3. In the **Getting started** section under **Schema
   template**, choose **Download**.

Alternatively, you can copy the JSON template from the following code example.

```
{
    "openapi": "3.0.0",
    "info": {
      "version": "1.0.0",
      "title": "Event"
    },
    "paths": {},
    "components": {
      "schemas": {
        "Event": {
          "type": "object",
          "properties": {
            "ordinal": {
              "type": "number",
              "format": "int64"
            },
            "name": {
              "type": "string"
            },
            "price": {
              "type": "number",
              "format": "double"
            },
            "address": {
              "type": "string"
            },
            "comments": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "created_at": {
              "type": "string",
              "format": "date-time"
            }
          }
        }
      }
    }
  }
```

###### To upload a schema template

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Schemas** and then choose
   **Create schema**.
3. (Optional) Select or create a schema registry.
4. Under **Schema details**, enter a name for your
   schema.
5. (Optional) Enter a description for your schema.
6. For **Schema type**, choose either **OpenAPI
   3.0** or **JSON Schema Draft 4**.
7. On the **Create** tab, in the text box, either drag your
   schema file to the text box, or paste the schema source.
8. Select **Create**.

## Edit a schema template directly in the

console

You can create a schema directly in the EventBridge console.

###### To edit a schema in the console

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Schemas** and then choose
   **Create schema**.
3. (Optional) Select or create a schema registry.
4. Under **Schema details**, enter a name for your
   schema.
5. For **Schema type**, choose either **OpenAPI
   3.0** or **JSON Schema Draft 4**.
6. (Optional) Enter a description for the schema to create.
7. On the **Create** tab, choose **Load
   template**.
8. In the text box, edit the template so that the schema matches your [events](eb-events.md "eb-events.md").
9. Select **Create**.
