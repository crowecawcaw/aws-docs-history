# Listing AWS Cloud Map services in a namespace

To view a list of the services that you created in a namespace, perform the following
procedure.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the navigation pane, choose **Namespaces**.
3. Choose the **Domain name** of the namespace that
   contains the services that you want to list. You can view a list of all
   services under **Services** and enter the service name
   or ID in the search field to find a specific service. You can identify
   the AWS account that created the service by using the
   **Created by** field and the account that owns the
   service by using the **Resource owner** field.

###### Note

If the namespace is a shared namespace, the AWS account ID under
**Resource owner** is the account that created
and shared the namespace. The account ID under **Created
by** can differ from the ID under **Resource
owner** if a namespace consumer created the service. The account IDs may not be the same as your account ID.
For more information about shared namespaces, see [Shared AWS Cloud Map namespaces](sharing-namespaces.md "sharing-namespaces.md").

AWS CLI

- List services with the `list-services` command. The following command
  lists all services in a namespace using the namespace ID as the filter.
  Replace the `red` value with your own.

```
`aws servicediscovery list-services --filters Name=NAMESPACE_ID,Values=`ns-1234567890abcdef`,Condition=EQ`
```

AWS SDK for Python (Boto3)

1. If you don't already have `Boto3` installed, you can find
   instructions for installing, configuring, and using `Boto3`
   [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation").
2. Import `Boto3` and use `servicediscovery` as
   your service.

```
import boto3
client = boto3.client('servicediscovery')
```

3. List services with `list_services()`.

```
response = client.list_services()
# If you want to see the response
print(response)
```

Example response output

```
{
    'Services': [
        {
            'Arn': 'arn:aws:servicediscovery:us-west-2:123456789012:service/srv-xxxxxxxxxxxxxxxx',
            'CreateDate': 1587081768.334,
            'DnsConfig': {
                'DnsRecords': [
                    {
                        'TTL': 60,
                        'Type': 'A',
                    },
                ],
                'RoutingPolicy': 'MULTIVALUE',
            },
            'Id': 'srv-xxxxxxxxxxxxxxxx',
            'Name': 'myservice',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}
```
