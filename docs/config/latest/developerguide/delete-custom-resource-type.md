# Delete Third-Party Resources from AWS Config

using the AWS CLI

Enter the following command to delete a third-party resource:

```
aws configservice delete-resource-config --resource-type MyCustomNamespace::Testing::WordPress --resource-id resource-002
```

If successful, the command executes with no additional output.
