

# Adding a schema version
<a name="schema-registry-gs5c"></a>

When you add a schema version, you will need to compare the versions to make sure the new schema will be accepted.

To add a new version to an existing schema, use the [RegisterSchemaVersion action (Python: register\_schema\_version)](aws-glue-api-schema-registry-api.md#aws-glue-api-schema-registry-api-RegisterSchemaVersion) API.

Specify a `SchemaId` structure to indicate the schema for which you want to add a version, and a `SchemaDefinition` to define the schema.

Code example 12:

```
aws glue register-schema-version --schema-definition "{\"type\": \"record\", \"name\": \"r1\", \"fields\": [ {\"name\": \"f1\", \"type\": \"int\"}, {\"name\": \"f2\", \"type\": \"string\"} ]}" --schema-id SchemaArn="arn:aws:glue:us-east-1:901234567890:schema/registryName/testschema"
```

```
aws glue register-schema-version --schema-definition "{\"type\": \"record\", \"name\": \"r1\", \"fields\": [ {\"name\": \"f1\", \"type\": \"int\"}, {\"name\": \"f2\", \"type\": \"string\"} ]}" --schema-id SchemaName="testschema",RegistryName="testregistry"
```

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue\).

1. In the navigation pane, under **Data catalog**, choose **Schemas**.

1. Choose the schema from the the list of schemas, by checking its box.

1. Choose one or more schemas from the list, by checking the boxes.

1. In the **Action** menu, choose **Register new version**.

1. In the **New version** box, enter or paste your new schema.

1. Choose **Compare with previous version** to see differences with the previous schema version.

1. Optionally, choose **Add metadata** to add version metadata to annotate or classify your schema version. Enter **Key** and optional **Value**.

1. Choose **Register version**.

![Adding a schema version.](http://docs.aws.amazon.com/glue/latest/dg/images/schema_reg_add_schema_version.png)


The schema(s) version appears in the list of versions. If the version changed the compatibility mode, the version will be marked as a checkpoint.

## Example of a schema version comparison
<a name="schema-registry-gs5c1"></a>

When you choose to **Compare with previous version**, you will see the previous and new versions displayed together. Changed information will be highlighted as follows:
+ *Yellow*: indicates changed information.
+ *Green*: indicates content added in the latest version.
+ *Red*: indicates content removed in the latest version.

You can also compare against earlier versions.

![Example of a schema version comparison.](http://docs.aws.amazon.com/glue/latest/dg/images/schema_reg_version_comparison.png)
