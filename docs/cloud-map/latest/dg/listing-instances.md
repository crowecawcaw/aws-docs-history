# Listing AWS Cloud Map service instances

To view a list of the service instances that you registered using a service, perform the
 following procedure.


AWS Management Console
1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the navigation pane, choose **Namespaces**.
3. Choose the name of the namespace that contains the service for which you want to list
 service instances.
4. Choose the name of the service that you used to create the service instances. You'll see
 a list of instances under **Service instances**. You can enter the instance
 ID in the search field to list a specific instance. The **Created by** field shows the ID of the AWS account that registered the instance.


###### Note

If the namespace in which the instance is registered is a shared namespace, the AWS account ID under
 **Created
 by** may not be the same as your account ID.
 For more information about shared namespaces, see [Shared AWS Cloud Map namespaces](sharing-namespaces.md "sharing-namespaces.md").


AWS CLI
* List service instances with the `list-instances` command (replace the `red` value
 with your own).



```
`aws servicediscovery list-instances --service-id `srv-xxxxxxxxx``
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
3. List service instances with `list_instances()` (replace the
 `red` value with your own).



```
response = client.list_instances(
    ServiceId='srv-xxxxxxxxx',
)
# If you want to see the response
print(response)
```

Example response output



```
{
    'Instances': [
        {
            'Attributes': {
                'AWS_INSTANCE_IPV4': '172.2.1.3',
                'AWS_INSTANCE_PORT': '808',
            },
            'Id': 'i-xxxxxxxxxxxxxxxxx',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}
```
