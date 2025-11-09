Amazon Cloud Directory is no longer be open to new customers. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# Create a Schema

Amazon Cloud Directory supports uploading of a compliant JSON file for schema creation. To create a new schema, you can either create your own JSON file from scratch or download one of the existing schemas listed in the console. Then upload it as a custom schema. For more
information, see [Custom Schemas](schemas_customschematopic.md "schemas_customschematopic.md").

You can also create, delete, download, list, publish, update and upgrade schemas using the Cloud Directory APIs. For more information about schema API operations, see the [Amazon Cloud Directory API Reference Guide](../../../amazoncds/latest/APIReference/welcome.md "../../../amazoncds/latest/APIReference/welcome.md").

Choose either of the procedures below, depending on your preferred method.

###### To create a custom schema

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, under **Cloud Directory**, choose **Schemas**.
2. Create a JSON file with all of your new schema definitions. For more information about
   how to format a JSON file, see [JSON Schema Format](schemas_jsonformat.md#schemas_json "schemas_jsonformat.md#schemas_json").
3. In the console, choose **Upload new schema**.
4. In the **Upload new schema** dialog, type a name for the schema.
5. Select **Choose file**, select the new
   JSON file that you just created, and then choose **Open**.
6. Choose **Upload**. This adds a new schema to your schema library and places it in the **Development** state. For more information about schema states, see [Schema Lifecycle](schemas_lifecycle.md "schemas_lifecycle.md").

###### To create a custom schema based on an existing one in the console

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, under **Cloud Directory**, choose **Schemas**.
2. In the table listing the schemas, select the option near the schema you want to copy.
3. Choose **Actions**.
4. Choose **Download schema**.
5. Rename the JSON file, edit it as needed, and then save the file. For more information
   about how to format a JSON file, see [JSON Schema Format](schemas_jsonformat.md#schemas_json "schemas_jsonformat.md#schemas_json").
6. In the console, choose **Upload new schema**, select the JSON
   file that you just edited, and then choose **Open**.

This adds a new schema to your schema library and places it in the **Development** state. For more information about schema states, see [Schema Lifecycle](schemas_lifecycle.md "schemas_lifecycle.md").
