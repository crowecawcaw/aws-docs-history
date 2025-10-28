# CreateNamespace

Use the `CreateNamespace` API operation to create a new namespace for you
to use with Amazon Quick Sight.

You can create a namespace after your AWS account is subscribed to Amazon Quick Sight. The
namespace must be unique within the AWS account. By default, there is a limit of 100
namespaces per AWS account. To increase your limit, create a ticket with AWS
Support.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-namespace
    --aws-account-id `AWSACCOUNTID`
    --namespace `NAMESPACE` \
    --identity-store `QUICKSIGHT`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-namespace
    --cli-input-json file://`createnamespace`.json
```

For more information about the `CreateNamespace` API operation, see [CreateNamespace](../APIReference/API_CreateNamespace.md "../APIReference/API_CreateNamespace.md") in the _Amazon Quick Sight API Reference_.
