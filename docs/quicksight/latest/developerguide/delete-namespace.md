# DeleteNamespace

Use the `DeleteNamespace` API operation to delete a namespace
and the users and groups that are associated with the namespace. This is an asynchronous process. Assets including dashboards, analyses, datasets, and data sources are not deleted. To delete these assets, you use the relevant API operations for each asset, such as `DeleteDashboard` or `DeleteDataSet`.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-namespace
    --aws-account-id `AWSACCOUNTID`
    --namespace `NAMESPACE`
```

Find a namespace by running the `ListNamespaces` operation.

For more information about the `DeleteNamespace` API operation, see [DeleteNamespace](../APIReference/API_DeleteNamespace.md "../APIReference/API_DeleteNamespace.md") in the _Amazon Quick Sight API Reference_.
