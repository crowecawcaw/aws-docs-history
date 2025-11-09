Amazon Cloud Directory is no longer be open to new customers. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# Create Your Directory

Before you can create a directory in Amazon Cloud Directory, AWS Directory Service requires
that you first apply a schema to it. A directory cannot be created without a schema and
typically has one schema applied to it. However, you use Cloud Directory API operations to apply
additional schemas to a directory. For more information, see [ApplySchema](../../../amazoncds/latest/APIReference/API_ApplySchema.md "../../../amazoncds/latest/APIReference/API_ApplySchema.md") in the _Amazon Cloud Directory API Reference
Guide_.

###### To create a Cloud Directory

1.  In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, under **Cloud Directory**, choose **Directories**.
2.  Choose **Set up Cloud Directory**.
3.  Under **Choose a schema to apply to your new directory**, type the friendly name of your directory, such as `User Repository`, and then choose one of the following options:

        * **Managed schema**
        * **Sample schema**
        * **Custom schema**

    Sample schemas and custom schemas are placed in the **Development** state, by default. For more information about schema states, see
    [Schema Lifecycle](schemas_lifecycle.md "schemas_lifecycle.md"). Before a schema can be applied to a
    directory, it must be converted into the **Published** state. To successfully publish a sample schema using the console, you must have
    permissions to the following actions:

        * `clouddirectory:Get*`
        * `clouddirectory:List*`
        * `clouddirectory:CreateSchema`
        * `clouddirectory:CreateDirectory`
        * `clouddirectory:PutSchemaFromJson`
        * `clouddirectory:PublishSchema`
        * `clouddirectory:DeleteSchema`

    Since sample schemas are read-only templates provided by AWS Directory Service, they cannot be published
    directly. Instead, when you choose to create a directory based on a sample schema, the
    console creates a temporary copy of the sample schema you selected and places it in the
    **Development** state. It then creates a copy of that
    development schema and places it in the **Published** state.
    Once published, the development schema is deleted, which is why the
    `DeleteSchema` action is necessary when publishing a sample schema.

4.  Choose **Next**.
5.  Review the directory information and make any necessary changes. When the information
    is correct, choose **Create**.
