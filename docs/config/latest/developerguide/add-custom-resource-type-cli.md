# Record Configuration Items with AWS Config for

Third-Party Resources using the AWS CLI

Record a configuration item for a third-party resource or a custom resource type using
the following procedure:

Ensure you register the resource type
`MyCustomNamespace::Testing::WordPress` with its matching schema.

1. Open a command prompt or a terminal window.
2. Enter the following command:

```
aws configservice put-resource-config --resource-type MyCustomNamespace::Testing::WordPress --resource-id resource-001 --schema-version-id 00000001 --configuration  '{
  "Id": "resource-001",
  "Name": "My example custom resource.",
  "PublicAccess": false
}'
```

###### Note

As defined in the type schema, `writeOnlyProperties` will be removed
from the configuration prior to being recorded by AWS Config. This means that these values
will not be present when the configuration is obtained from read APIs. For more
information on `writeOnlyProperties`, see [Resource type schema](../../../cloudformation-cli/latest/userguide/resource-type-schema.md "../../../cloudformation-cli/latest/userguide/resource-type-schema.md").
