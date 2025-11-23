# Registering a resource as an AWS Cloud Map service

instance

You can register your application's resources as instances in a AWS Cloud Map service. For example,
assume you've created a service called `users` for all application resources that
manage user data. You can then register a DynamoDB table that's used to store user data as an
instance in this service.

###### Note

The following features are not available on the AWS Cloud Map console:

- When you register a service instance using the console, you can't create an alias
  record that routes traffic to an ELB (ELB) load balancer. When you register an instance,
  you must include the `AWS_ALIAS_DNS_NAME` attribute. For more information, see
  [RegisterInstance](../api/API_RegisterInstance.md "../api/API_RegisterInstance.md") in the _AWS Cloud Map API Reference_.
- If you register an instance using a service that includes a custom health check, you
  can't specify the initial status for the custom health check. By default, the initial
  status of a custom health checks is **Healthy**. If you want the initial
  health status to be **Unhealthy**, register the instance programmatically
  and include the `AWS_INIT_HEALTH_STATUS` attribute. For more information, see
  [RegisterInstance](../api/API_RegisterInstance.md "../api/API_RegisterInstance.md") in the _AWS Cloud Map API Reference_.
  To register an instance in a service, follow these steps.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/ "https://console.aws.amazon.com/cloudmap/").
2. In the navigation pane, choose **Namespaces**.
3. On the **Namespaces** page, choose the namespace that contains
   the service that you want to use as a template for registering a service
   instance.
4. On the **Namespace: `namespace-name`**
   page, choose the service that you want to use.
5. On the **Service: `service-name`** page,
   choose **Register service instance**.
6. On the **Register service instance** page, choose an
   **Instance type**. Depending on the namespace instance discovery
   configuration, you can choose to specify an IP address, an Amazon EC2 instance ID, or other
   identifying information for a resource that doesn't have an IP address.

###### Note

You can choose **EC2 instance** only in HTTP namespaces. 7. For **Service instance ID**, provide an identifier associated
with the service instance.

###### Note

If you want to update an existing instance, provide the
identifier associated with the instance you want to update. Then, use the next steps to update values
and reregister the instance. 8. Based on your choice of **Instance type**, perform the following
steps.

###### Important

You can't use the `AWS_` prefix (not case sensitive) in a key when you specify a custom attribute.

| Instance type                                | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IP address                                   | 1. Under **Standard attributes**, for **IPv4<br>address**, provide an IPv4 address, if any, where your<br>application can access the resource that's associated with this service<br>instance.<br>2. For **IPv6 address**, provide an IPv6 IP address,<br>if any, where your applications can access the resource that's<br>associated with this service instance.<br>3. For **Port**, specify any port your application<br>must include to access the resource that's associated with this service<br>instance. **Port\*<br>• is required when the service<br>includes an SRV record or an Amazon Route 53 health check.<br>4. (Optional) Under **Custom attributes\*\*, specify any<br>key-value pairs you want to associate with the resource. |
| EC2 instance                                 | 1. For **EC2 instance ID**, select the ID of the Amazon EC2<br>instance that you want to register as a AWS Cloud Map service instance.<br>2. (Optional) Under **Custom attributes**, specify any<br>key-value pairs you want to associate with the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Identifying information for another resource | 1. Under **Standard attributes**, if the service<br>configuration includes a **CNAME\*<br>• DNS record, you'll<br>see a **CNAME\*<br>• field. For **CNAME**,<br>specify the domain name that you want Route 53 to return in response to DNS<br>queries (for example, `example.com`).<br>2. Under **Custom attributes**, specify any<br>identifying information for a resource that isn't an IP address or an<br>Amazon EC2 instance ID as a key-value pair. For example, you can register a<br>Lambda function by specifying a key called `function` and<br>providing the name of the Lambda function as a value. You can also<br>specify a key called `name` and provide a name that you can<br>use for programmatic instance discovery.         |

9. Choose **Register service instance**.

AWS CLI

- When you submit a `RegisterInstance` request:

      + For each DNS record that you define in the service that's specified by
       `ServiceId`, a record is created or updated in the hosted zone that's
       associated with the corresponding namespace.
      + If the service includes `HealthCheckConfig`, a health check is
       created based on the settings in the health check configuration.
      + Any health checks are associated with each of the new or updated
       records.

  Register a service instance with the `register-instance` command (replace the
  `red` values with your own).

```
`aws servicediscovery register-instance \
 --service-id `srv-xxxxxxxxx` \
 --instance-id `myservice-xx` \
 --attributes=`AWS_INSTANCE_IPV4=172.2.1.3,AWS_INSTANCE_PORT=808``
```

AWS SDK for Python (Boto3)

1. If you don't already have `Boto3` installed, you can find instructions
   for installing, configuring, and using `Boto3`
   [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation").
2. Import `Boto3` and use `servicediscovery` as your
   service.

```
import boto3
client = boto3.client('servicediscovery')
```

3.  When you submit a `RegisterInstance` request:

        * For each DNS record that you define in the service that's specified by
         `ServiceId`, a record is created or updated in the hosted zone that's
         associated with the corresponding namespace.
        * If the service includes `HealthCheckConfig`, a health check is
         created based on the settings in the health check configuration.
        * Any health checks are associated with each of the new or updated
         records.

    Register a service instance with `register_instance()` (replace the
    `red` values with your own).

```
response = client.register_instance(
    Attributes={
        'AWS_INSTANCE_IPV4': '172.2.1.3',
        'AWS_INSTANCE_PORT': '808',
    },
    InstanceId='`myservice-xx`',
    ServiceId='`srv-xxxxxxxxx`',
)
# If you want to see the response
print(response)
```

Example response output

```
{
    'OperationId': '4yejorelbukcjzpnr6tlmrghsjwpngf4-k95yg2u7',
    'ResponseMetadata': {
        '...': '...',
    },
}
```
