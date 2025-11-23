# Creating an AWS Cloud Map service for an application

component

After creating a namespace, you can create services to represent different components of
your application that serve particular purposes. For example, you can create a service for
resources in your application that process payments.

###### Note

You can't create multiple services that are accessible by DNS queries with names that
differ only by case (such as EXAMPLE and example). Trying to do so will result in these
services having the same DNS name. If you use a namespace that's only accessible by API
calls, then you can create services that with names that differ only by case.

Follow these steps to create a service using the AWS Management Console, AWS CLI, and SDK for
Python.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the navigation pane, choose
   **Namespaces**.
3. On the **Namespaces** page, choose the namespace
   that you want to add the service to.
4. On the **Namespace:
   `namespace-name`** page,
   choose **Create service**.
5. For **Service name**, enter a name that describes
   the instances that you register when using this service. The value
   is used to discover AWS Cloud Map service instances either in API calls
   or in DNS queries.

###### Note

If you want AWS Cloud Map to create an **SRV**
record when you register an instance and you're using a system
that requires a specific **SRV** format (such
as [HAProxy](http://www.haproxy.org/ "http://www.haproxy.org/")),
specify the following for **Service
name**:

    * Start the name with an underscore (\_), for example
     **\_exampleservice**.
    * End the name with
     `._protocol`, for example
     **.\_tcp**.When you register an instance, AWS Cloud Map creates an

**SRV** record and assigns a name by
concatenating the service name and the namespace name, for
example:

**\_exampleservice.\_tcp.example.com** 6. (Optional) For **Service description**, enter a
description for the service. The description that you enter here
appears on the **Services** page and on the detail
page for each service. 7. If the namespace supports DNS queries, under **Service
discovery configuration**, you can configure
discoverability at the service level. Choose between allowing both
API calls and DNS queries or only API calls for the discovery of
instances in this service.

###### Note

If you choose **API calls**, AWS Cloud Map will not
create SRV records when you register an instance.

If you choose **API and DNS**, follow these steps
to configure DNS records. You can add or remove DNS records.

    1. For **Routing policy**, select the
     Amazon Route 53 routing policy for the DNS records that AWS Cloud Map
     creates when you register instances. You can select between
     **Weighted routing** and
     **Multivalue answer routing**. For more
     information, see [Routing policy](services-route53.md#services-dns-routing-policy "services-route53.md#services-dns-routing-policy").


    ###### Note

    You can't use the console to configure AWS Cloud Map to
     create a Route 53 alias record when you register an
     instance. If you want AWS Cloud Map to create alias records
     for an ELB load balancer when you register instances
     programmatically, choose **Weighted
     routing** for **Routing
     policy**.
    2. For **Record type**, choose the DNS
     record type that determines what Route 53 returns in response
     to DNS queries by AWS Cloud Map. For more information, see [Record type](services-route53.md#services-dns-record-type "services-route53.md#services-dns-record-type").
    3. For **TTL**, specify a numerical value to
     define the time to live (TTL) value, in seconds, at the
     service level. The value of TTL determines how long DNS
     resolvers cache information for this record before the
     resolvers forward another DNS query to Amazon Route 53 to get
     updated settings.

8. Under **Health check configuration**, for
   **Health check options**, choose the type of
   health check applicable for service instances. You can choose not to
   configure any health checks, or you can choose between a Route 53
   health check or an external health check for your instances. For
   more information, see [AWS Cloud Map service health check
   configuration](services-health-checks.md "services-health-checks.md").

###### Note

Route 53 health checks are configurable only for services in
public DNS namespaces.

If you choose **Route 53 health checks**, provide
the following information.

    1. For **Failure threshold**, provide a
     number between 1 and 10 that defines the number of
     consecutive Route 53 health checks a service instance must pass
     or fail for its health status to change.
    2. For **Health check protocol**, select the
     method Route 53 will use to check the health of the service
     instances.
    3. If you choose **HTTP** or
     **HTTPS** health check protocol, for
     **Health check path**, provide a path
     that you want Amazon Route 53 to request when performing health
     checks. The path can be any value such as the file
     `/docs/route53-health-check.html`. When the
     resource is healthy, the returned value is an HTTP status
     code of a 2xx or 3xx format. You can also include query
     string parameters, for example,
     `/welcome.html?language=jp&login=y`. The
     AWS Cloud Map console automatically adds a leading slash (/)
     character.

For more information about Route 53 health checks, see [How Amazon Route 53 Determines Whether a Health Check Is
Healthy](../../../Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.md "../../../Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.md") in the _Amazon Route 53
Developer Guide_. 9. (Optional) Under **Tags**, choose **Add
tags** and then specify a key and a value to tag your
namespace. You can specify one or more tags to add to your
namespace. Tags allow you to categorize your AWS resources so you
can more easily manage them. For more information, see [Tagging your AWS Cloud Map resources](using-tags.md "using-tags.md"). 10. Choose **Create service**.

AWS CLI

- Create a service with the `create-service` command. Replace the
  `red` values with your own.

```
`aws servicediscovery create-service \
 --name `service-name` \
 --namespace-id `ns-xxxxxxxxxxx` \
 --dns-config "NamespaceId=`ns-xxxxxxxxxxx`,RoutingPolicy=MULTIVALUE,DnsRecords=[{Type=`A`,TTL=`60`}]"`
```

Output:

```
{
        "Service": {
        "Id": "srv-xxxxxxxxxxx",
        "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-xxxxxxxxxxx",
        "Name": "service-name",
        "NamespaceId": "ns-xxxxxxxxxxx",
        "DnsConfig": {
            "NamespaceId": "ns-xxxxxxxxxxx",
            "RoutingPolicy": "MULTIVALUE",
            "DnsRecords": [
                {
                    "Type": "A",
                    "TTL": 60
                }
            ]
        },
        "CreateDate": 1587081768.334,
        "CreatorRequestId": "567c1193-6b00-4308-bd57-ad38a8822d25"
    }
}
```

AWS SDK for Python (Boto3)
If you don't already have `Boto3` installed, you can find
instructions for installing, configuring, and using `Boto3`
[here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation").

1. Import `Boto3` and use `servicediscovery` as
   your service.

```
import boto3
client = boto3.client('servicediscovery')
```

2. Create a service with `create_service()`. Replace the
   `red` values with your own. For more
   information, see [create_service](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/client/create_service.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery/client/create_service.html").

```
response = client.create_service(
    DnsConfig={
        'DnsRecords': [
            {
                'TTL': `60`,
                'Type': '`A`',
            },
        ],
        'NamespaceId': '`ns-xxxxxxxxxxx`',
        'RoutingPolicy': '`MULTIVALUE`',
    },
    Name='`service-name`',
    NamespaceId='`ns-xxxxxxxxxxx`',
)
```

Example response output

```
{
    'Service': {
        'Arn': 'arn:aws:servicediscovery:us-west-2:123456789012:service/srv-xxxxxxxxxxx',
        'CreateDate': 1587081768.334,
        'DnsConfig': {
            'DnsRecords': [
                {
                    'TTL': 60,
                    'Type': 'A',
                },
            ],
            'NamespaceId': 'ns-xxxxxxxxxxx',
            'RoutingPolicy': 'MULTIVALUE',
        },
        'Id': 'srv-xxxxxxxxxxx',
        'Name': 'service-name',
        'NamespaceId': 'ns-xxxxxxxxxxx',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}
```

## Next steps

After creating a service, you can register your application resources as service
instances that contain information about how your application can locate the resource.
For more information about registering AWS Cloud Map service instances, see [Registering a resource as an AWS Cloud Map service
instance](registering-instances.md "registering-instances.md").

You can also specify custom metadata such as endpoint weights, API timeouts, and retry policies as service attributes after creating a service. For more information, see [ServiceAttributes](../api/API_ServiceAttributes.md "../api/API_ServiceAttributes.md") and
[`UpdateServiceAttributes`](../api/API_UpdateServiceAttributes.md "../api/API_UpdateServiceAttributes.md") in the _AWS Cloud Map API Reference_.
