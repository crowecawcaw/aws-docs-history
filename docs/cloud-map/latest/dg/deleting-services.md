# Deleting an AWS Cloud Map service

Before you can delete a service, you must deregister all service instances that were
registered using the service. For more information, see [Deregistering an AWS Cloud Map service instance](deregistering-instances.md "deregistering-instances.md").

After deregistering all instances registered using the service, perform the following procedure to delete the service.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the navigation pane, choose **Namespaces**.
3. Choose the option for the namespace that contains the service that you want to
   delete.
4. On the **Namespace: `namespace-name`** page,
   choose the option for the service that you want to delete.
5. Choose **Delete**.
6. Confirm that you want to delete the service.

AWS CLI

- Delete a service with the `delete-service` command (replace the `red` value
  with your own).

```
`aws servicediscovery delete-service --id `srv-xxxxxx``
```

AWS SDK for Python (Boto3)

1. If you don't already have `Boto3` installed, you can find instructions for
   installing, configuring, and using `Boto3`
   [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation").
2. Import `Boto3` and use `servicediscovery` as your service.

```
import boto3
client = boto3.client('servicediscovery')
```

3. Delete a service with `delete_service()` (replace the
   `red` value with your own).

```
response = client.delete_service(
    Id='`srv-xxxxxx`',
)
# If you want to see the response
print(response)
```

Example response output

```
{
    'ResponseMetadata': {
        '...': '...',
    },
}
```
