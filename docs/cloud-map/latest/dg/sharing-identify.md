# Identifying a shared AWS Cloud Map namespace

Owners and consumers can identify shared namespaces using the AWS Cloud Map console and
AWS CLI. The namespace owner can be identified by using the `ResourceOwner`
property. The AWS account that creates a service or registers an instance in the
shared namespace can be identified by using the `CreatedByAccount`
property.

AWS Cloud Map console

###### To identify a shared namespace using the AWS Cloud Map console

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. On the **Namespaces** page, under
   **Resource Owner**, you can find the ID of the
   AWS account that owns the namespace.
3. Choose the **Domain name** of the namespace you
   want to identify.
4. On the **Namespace:
   `namespace-name`** page,
   in the **Namespace information** section, under
   **Resource owner**, you can find the ID of the
   AWS account that owns the namespace.

AWS CLI
To identify a shared namespace using the AWS CLI, use the [list-namespaces](../../../cli/latest/reference/servicediscovery/list-namespaces.md "../../../cli/latest/reference/servicediscovery/list-namespaces.md") command. The command returns the namespaces
that you own and namespaces that are shared with you. The
`ResourceOwner` field shows the AWS account ID of the
namespace owner.

The following `list-namespaces` call is made by account
`111122223333`.

```
aws servicediscovery list-namespaces
```

Output:

```
{
    "Namespaces": [
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:111122223333:namespace/ns-abcdef01234567890",
            "CreateDate": 1585354387.357,
            "Id": "ns-abcdef01234567890",
            "Name": "local",
            "Properties": {
                "DnsProperties": {
                    "HostedZoneId": "Z06752353VBUDTC32S84S"
                },
                "HttpProperties": {
                    "HttpName": "local"
                 }
            },
            "Type": "DNS_PRIVATE",
            "ServiceCount": 2,
           **"ResourceOwner": "111122223333"**
        },
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:444455556666:namespace/ns-021345abcdef6789",
            "CreateDate": 1586468974.698,
            "Description": "Shared second namespace",
            "Id": "ns-021345abcdef6789",
            "Name": "My-second-namespace",
            "Properties": {
                "DnsProperties": {},
                "HttpProperties": {
                    "HttpName": "Shared-second-namespace"
                }
            },
            "Type": "HTTP",
            "ServiceCount": 0,
            **"ResourceOwner": "444455556666"**
        }
    ]
}
```

In this scenario, namespace `ns-abcdef01234567890` is created
and owned by `111122223333` and namespace
`ns-021345abcdef6789` is created and owned by
`444455556666`. Namespace
`ns-021345abcdef6789` is shared with account
`111122223333` by account
`444455556666`.
