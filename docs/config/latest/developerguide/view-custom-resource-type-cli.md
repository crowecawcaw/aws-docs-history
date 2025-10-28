# Read Configuration Items with AWS Config for

Third-Party Resources using the AWS CLI

Read a configuration item for a third-party resource or a custom resource type using
the following procedure:

1. Open a command prompt or a terminal window.
2. Enter the following command:

```
aws configservice list-discovered-resources --resource-type MyCustomNamespace::Testing::WordPress
```

3. Press Enter.

You should see output similar to the following:

```
{
    "resourceIdentifiers": [
        {
            "resourceType": "MyCustomNamespace::Testing::WordPress",
            "resourceId": "resource-001"
        }
    ]
}

```

4. Enter the following command:

```
aws configservice batch-get-resource-config --resource-keys '[ { "resourceType": "MyCustomNamespace::Testing::WordPress", "resourceId": "resource-001" } ]'
```

5. Press Enter.

You should see output similar to the following:

```
{
    "unprocessedResourceKeys": [],
    "baseConfigurationItems": [
        {
            "configurationItemCaptureTime": 1569605832.673,
            "resourceType": "MyCustomNamespace::Testing::WordPress",
            "resourceId": "resource-001",
            "configurationStateId": "1569605832673",
            "awsRegion": "us-west-2",
            "version": "1.3",
            "supplementaryConfiguration": {},
            "configuration": "{\"Id\":\"resource-001\",\"Name\":\"My example custom resource.\",\"PublicAccess\":false}",
            "configurationItemStatus": "ResourceDiscovered",
            "accountId": "`AccountId`"
        }
    ]
}

```
