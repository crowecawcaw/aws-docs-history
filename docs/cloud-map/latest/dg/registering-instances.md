

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


<table>
<thead>
  <tr><th>Instance type</th><th>Steps</th><th></th></tr>
</thead>
<tbody>
  <tr><td>IP address</td><td> <ol><li> Under <b>Standard attributes</b>, for <b>IPv4 address</b>, provide an IPv4 address, if any, where your application can access the resource that's associated with this service instance. </li><li> For <b>IPv6 address</b>, provide an IPv6 IP address, if any, where your applications can access the resource that's associated with this service instance. </li><li>  For <b>Port</b>, specify any port your application must include to access the resource that's associated with this service instance. <b>Port</b> is required when the service includes an SRV record or an Amazon Route 53 health check. </li><li> (Optional) Under <b>Custom attributes</b>, specify any key-value pairs you want to associate with the resource. <br /> </li></ol> </td><td></td></tr>
  <tr><td>EC2 instance</td><td> <ol><li> For <b>EC2 instance ID</b>, select the ID of the Amazon EC2 instance that you want to register as a AWS Cloud Map service instance. </li><li> (Optional) Under <b>Custom attributes</b>, specify any key-value pairs you want to associate with the resource. </li></ol> </td><td></td></tr>
  <tr><td>Identifying information for another resource</td><td> <ol><li> Under <b>Standard attributes</b>, if the service configuration includes a <b>CNAME</b> DNS record, you'll see a <b>CNAME</b> field. For <b>CNAME</b>, specify the domain name that you want Route 53 to return in response to DNS queries (for example, <code>example.com</code>). </li><li> Under <b>Custom attributes</b>, specify any identifying information for a resource that isn't an IP address or an Amazon EC2 instance ID as a key-value pair. For example, you can register a Lambda function by specifying a key called <code>function</code> and providing the name of the Lambda function as a value. You can also specify a key called <code>name</code> and provide a name that you can use for programmatic instance discovery. </li></ol> </td><td></td></tr>
</tbody>
</table>


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