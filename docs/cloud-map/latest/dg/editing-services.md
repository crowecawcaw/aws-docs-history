# Updating an AWS Cloud Map service

Depending on a service's configuration, you can update its tags, Route 53 health check
failure threshold, and time to live (TTL) for DNS resolvers. To update a service, perform
the following procedure.

###### Note

You can't update settings for services associated with HTTP namespaces.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the navigation pane, choose **Namespaces**.
3. On the **Namespaces** page, choose the namespace in
   which the service is created.
4. On the **Namespace:
   `namespace-name`** page, select
   the service you want to edit and choose **View
   details**.
5. On the **Service:
   `service-name`** page, choose
   **Edit**.

###### Note

You can't use the **Edit** button workflow to
edit values for services that allow only API calls for instance
discovery. However, you can add or remove tags on the
**Service:
`service-name`** page. 6. On the **Edit service** page, under **Service
description**, you can update any previously set
description for the service or add a new description. You can also add
tags and update **TTL** for DNS resolvers. 7. Under **DNS configuration**, for
**TTL**, you can specify an updated period of time,
in seconds, that determines how long DNS resolvers cache information for
this record before the resolvers forward another DNS query to Amazon Route 53
to get updated settings. 8. If you've set up Route 53 health checks, for **Failure
threshold**, you can specify a new number
between 1 and 10 that defines the number of consecutive Route 53
health checks a service instance must pass or fail for its
health status to change. 9. Choose **Update service**.

AWS CLI

- Update a service with the `update-service` command (replace the
  `red` value with your own).

```
`aws servicediscovery update-service \
 --id `srv-xxxxxxxxxxx` \
 --service "Description=`new description`,DnsConfig={DnsRecords=[{Type=A,TTL=`60`}]}"`
```

Output:

```
{
    "OperationId": "l3pfx7f4ynndrbj3cfq5fm2qy2z37bms-5m6iaoty"
}
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

3. Update a service with `update_service()` (replace the
   `red` value with your own).

```
response = client.update_service(
    Id='`srv-xxxxxxxxxxx`',
    Service={
        'DnsConfig': {
            'DnsRecords': [
                {
                    'TTL': `300`,
                    'Type': 'A',
                },
            ],
        },
        'Description': "`new description`",
    }
)
```

Example response output

```
{
    "OperationId": "l3pfx7f4ynndrbj3cfq5fm2qy2z37bms-5m6iaoty"
}
```
