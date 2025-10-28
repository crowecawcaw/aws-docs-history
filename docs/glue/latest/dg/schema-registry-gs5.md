# Updating a schema or registry

Once created you can edit your schemas, schema versions, or registry.

## Updating a registry

You can update a registry using the AWS Glue APIs or the AWS Glue console. The name of an existing registry cannot be edited. You can edit the description for a registry.

###### AWS Glue APIs

To update an existing registry, use the [UpdateRegistry action (Python: update_registry)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-UpdateRegistry "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-UpdateRegistry") API.

Specify a `RegistryId` structure to indicate the registry that you want to update. Pass a `Description` to change the description for a registry.

```
aws glue update-registry --description updatedDescription --registry-id RegistryArn="arn:aws:glue:us-east-2:901234567890:registry/registryName1"
```

###### AWS Glue console

To update a registry using the AWS Glue console:

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](<https://console.aws.amazon.com/glue\ "https://console.aws.amazon.com/glue">).
2. In the navigation pane, under **Data catalog**, choose **Schema registries**.
3. Choose a registry from the the list of registries, by checking its box.
4. In the **Action** menu, choose **Edit registry**.
