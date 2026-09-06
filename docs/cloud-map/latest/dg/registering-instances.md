

# Registering a resource as an AWS Cloud Map service instance
<a name="registering-instances"></a>

You can register your application's resources as instances in a AWS Cloud Map service. For example, assume you've created a service called `users` for all application resources that manage user data. You can then register a DynamoDB table that's used to store user data as an instance in this service.

**Note**  
The following features are not available on the AWS Cloud Map console:  
When you register a service instance using the console, you can't create an alias record that routes traffic to an Elastic Load Balancing (ELB) load balancer. When you register an instance, you must include the `AWS_ALIAS_DNS_NAME` attribute. For more information, see [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html) in the *AWS Cloud Map API Reference*.
If you register an instance using a service that includes a custom health check, you can't specify the initial status for the custom health check. By default, the initial status of a custom health checks is **Healthy**. If you want the initial health status to be **Unhealthy**, register the instance programmatically and include the `AWS_INIT_HEALTH_STATUS` attribute. For more information, see [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html) in the *AWS Cloud Map API Reference*.

To register an instance in a service, follow these steps.

------
#### [ AWS Management Console ]

1. Sign in to the AWS Management Console and open the AWS Cloud Map console at [https://console.aws.amazon.com/cloudmap/](https://console.aws.amazon.com/cloudmap/).

1. In the navigation pane, choose **Namespaces**.

1. On the **Namespaces** page, choose the namespace that contains the service that you want to use as a template for registering a service instance.

1. On the **Namespace: {{namespace-name}}** page, choose the service that you want to use.

1. On the **Service: {{service-name}}** page, choose **Register service instance**.

1. On the **Register service instance** page, choose an **Instance type**. Depending on the namespace instance discovery configuration, you can choose to specify an IP address, an Amazon EC2 instance ID, or other identifying information for a resource that doesn't have an IP address.
**Note**  
You can choose **EC2 instance** only in HTTP namespaces.

1. For **Service instance ID**, provide an identifier associated with the service instance.
**Note**  
If you want to update an existing instance, provide the identifier associated with the instance you want to update. Then, use the next steps to update values and reregister the instance.

1. Based on your choice of **Instance type**, perform the following steps.
**Important**  
You can't use the `AWS_` prefix (not case sensitive) in a key when you specify a custom attribute.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloud-map/latest/dg/registering-instances.html)

1. Choose **Register service instance**.

------
#### [ AWS CLI ]
+ 

  When you submit a `RegisterInstance` request:
  + For each DNS record that you define in the service that's specified by `ServiceId`, a record is created or updated in the hosted zone that's associated with the corresponding namespace.
  + If the service includes `HealthCheckConfig`, a health check is created based on the settings in the health check configuration.
  + Any health checks are associated with each of the new or updated records.

  Register a service instance with the `[register-instance](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/register-instance.html)` command (replace the {{red}} values with your own).

  ```
  aws servicediscovery register-instance \
      --service-id {{srv-xxxxxxxxx}} \
      --instance-id {{myservice-xx}} \
      --attributes={{AWS_INSTANCE_IPV4=172.2.1.3,AWS_INSTANCE_PORT=808}}
  ```

------
#### [ AWS SDK for Python (Boto3) ]

1. If you don't already have `Boto3` installed, you can find instructions for installing, configuring, and using `Boto3` [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation).

1. Import `Boto3` and use `servicediscovery` as your service.

   ```
   import boto3
   client = boto3.client('servicediscovery')
   ```

1. 

   When you submit a `RegisterInstance` request:
   + For each DNS record that you define in the service that's specified by `ServiceId`, a record is created or updated in the hosted zone that's associated with the corresponding namespace.
   + If the service includes `HealthCheckConfig`, a health check is created based on the settings in the health check configuration.
   + Any health checks are associated with each of the new or updated records.

   Register a service instance with `register_instance()` (replace the {{red}} values with your own).

   ```
   response = client.register_instance(
       Attributes={
           'AWS_INSTANCE_IPV4': '172.2.1.3',
           'AWS_INSTANCE_PORT': '808',
       },
       InstanceId='{{myservice-xx}}',
       ServiceId='{{srv-xxxxxxxxx}}',
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

------