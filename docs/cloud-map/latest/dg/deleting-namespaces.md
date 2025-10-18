# Deleting an AWS Cloud Map namespace

After you're done using a namespace, you can delete it. When you delete a namespace, you can
 no longer use it to register or discover service instances.

###### Note

 When you delete a DNS namespace, AWS Cloud Map deletes the corresponding Amazon Route 53 hosted
 zone created during namespace creation.

Before deleting a namespace, you must deregister all service instances and then delete all services that were created in the namespace. For more information, see [Deregistering an AWS Cloud Map service instance](deregistering-instances.md "deregistering-instances.md") and [Deleting an AWS Cloud Map service](deleting-services.md "deleting-services.md").

After you've deregistered instances and deleted services that were created in a namespace,
 follow these steps to delete the namespace.


AWS Management Console
1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the navigation pane, choose **Namespaces**.
3. Select the namespace that you want to delete, then choose
 **Delete**.
4. Confirm that you want to delete the service by choosing **Delete**
 again.


AWS CLI
* Delete a namespace with the `delete-namespace` command (replace the `red` value
 with your own). If the namespace still contains one or more services, the request
 fails.



```
`aws servicediscovery delete-namespace --id `ns-xxxxxxxxxxx``
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
3. Delete a namespace with `delete_namespace()` (replace the
 `red` value with your own). If the namespace still contains one or
 more services, the request fails.



```
response = client.delete_namespace(
    Id='`ns-xxxxxxxxxxx`',
)
# If you want to see the response
print(response)
```

Example response output



```
{
    'OperationId': 'gv4g5meo7ndmeh4fqskygvk23d2fijwa-k98y6drk',
    'ResponseMetadata': {
        '...': '...',
    },
}
```
