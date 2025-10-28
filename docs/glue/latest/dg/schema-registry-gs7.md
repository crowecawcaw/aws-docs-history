# Deleting a schema or registry

Deleting a schema, a schema version, or a registry are permanent actions that cannot be undone.

## Deleting a schema

You may want to delete a schema when it will no longer be used within a registry, using the AWS Management Console, or the [DeleteSchema action (Python: delete_schema)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteSchema "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteSchema") API.

Deleting one or more schemas is a permanent action that cannot be undone. Make sure that the schema or schemas are no longer needed.

To delete a schema from the registry, call the [DeleteSchema action (Python: delete_schema)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteSchema "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteSchema") API, specifying the `SchemaId` structure to identify the schema.

For example:

```
aws glue delete-schema --schema-id SchemaArn="arn:aws:glue:us-east-2:901234567890:schema/registryName1/schemaname"
```

```
aws glue delete-schema --schema-id SchemaName="TestSchema6-deleteschemabyname",RegistryName="default-registry"
```

###### AWS Glue console

To delete a schema from the AWS Glue console:

1. Sign in to the AWS Management Console and
   open the AWS Glue console at [https://console.aws.amazon.com/glue/](<https://console.aws.amazon.com/glue\ "https://console.aws.amazon.com/glue">).
2. In the navigation pane, under **Data catalog**, choose **Schema registries**.
3. Choose the registry that contains your schema from the the list of registries.
4. Choose one or more schemas from the list, by checking the boxes.
5. In the **Action** menu, choose **Delete schema**.
6. Enter the text `Delete` in the field to confirm deletion.
7. Choose **Delete**.

The schema(s) you specified are deleted from the registry.

## Deleting a schema version

As schemas accumulate in the registry, you may want to delete unwanted schema versions using the AWS Management Console, or the [DeleteSchemaVersions action (Python: delete_schema_versions)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteSchemaVersions "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteSchemaVersions") API. Deleting one or more schema versions is a permanent action that cannot be undone. Make sure that the schema versions are no longer needed.

When deleting schema versions, take note of the following constraints:

- You cannot delete a check-pointed version.
- The range of contiguous versions cannot be more than 25.
- The latest schema version must not be in a pending state.

Specify the `SchemaId` structure to identify the schema, and specify `Versions` as a range of versions to delete. For more information on specifying a version or range of versions, see [DeleteRegistry action (Python: delete_registry)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteRegistry "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteRegistry"). The schema versions you specified are deleted from the registry.

Calling the [ListSchemaVersions action (Python: list_schema_versions)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-ListSchemaVersions "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-ListSchemaVersions") API after this call will list the status of the deleted versions.

For example:

```
aws glue delete-schema-versions --schema-id SchemaName="TestSchema6",RegistryName="default-registry" --versions "1-1"
```

```
aws glue delete-schema-versions --schema-id SchemaArn="arn:aws:glue:us-east-2:901234567890:schema/default-registry/TestSchema6-NON-Existent" --versions "1-1"
```

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](<https://console.aws.amazon.com/glue\ "https://console.aws.amazon.com/glue">).
2. In the navigation pane, under **Data catalog**, choose **Schema registries**.
3. Choose the registry that contains your schema from the the list of registries.
4. Choose one or more schemas from the list, by checking the boxes.
5. In the **Action** menu, choose **Delete schema**.
6. Enter the text `Delete` in the field to confirm deletion.
7. Choose **Delete**.

The schema versions you specified are deleted from the registry.
