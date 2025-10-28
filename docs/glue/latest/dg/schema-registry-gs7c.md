# Deleting a registry

You may want to delete a registry when the schemas it contains should no longer be organized under that registry. You will need to reassign those schemas to another registry.

Deleting one or more registries is a permanent action that cannot be undone. Make sure that the registry or registries no longer needed.

The default registry can be deleted using the AWS CLI.

###### AWS Glue API

To delete the entire registry including the schema and all of its versions, call the [DeleteRegistry action (Python: delete_registry)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteRegistry "aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-DeleteRegistry") API. Specify a `RegistryId` structure to identify the registry.

For example:

```
aws glue delete-registry --registry-id RegistryArn="arn:aws:glue:us-east-2:901234567890:registry/registryName1"
```

```
aws glue delete-registry --registry-id RegistryName="TestRegistry-deletebyname"
```

To get the status of the delete operation, you can call the `GetRegistry` API after the asynchronous call.

###### AWS Glue console

To delete a registry from the AWS Glue console:

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](<https://console.aws.amazon.com/glue\ "https://console.aws.amazon.com/glue">).
2. In the navigation pane, under **Data catalog**, choose **Schema registries**.
3. Choose a registry from the list, by checking a box.
4. In the **Action** menu, choose **Delete registry**.
5. Enter the text `Delete` in the field to confirm deletion.
6. Choose **Delete**.
   The registries you selected are deleted from AWS Glue.
