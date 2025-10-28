# Updating a schema

You can update the description or compatibility setting for a schema.

To update an existing schema, use the [UpdateSchema action (Python: update_schema)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-UpdateSchema "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-UpdateSchema") API.

Specify a `SchemaId` structure to indicate the schema that you want to update. One of `VersionNumber` or `Compatibility` has to be provided.

Code example 11:

```
aws glue update-schema --description testDescription --schema-id SchemaName="testSchema1",RegistryName="registryName1" --schema-version-number LatestVersion=true --compatibility NONE
```

```
aws glue update-schema --description testDescription --schema-id SchemaArn="arn:aws:glue:us-east-2:901234567890:schema/registryName1/testSchema1" --schema-version-number LatestVersion=true --compatibility NONE
```
