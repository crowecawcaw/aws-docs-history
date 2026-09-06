

AWS App Runner is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Configuring observability for your service
<a name="manage-configure-observability"></a>

AWS App Runner integrates with several AWS services to provide you with an extensive observability suite of tools for your App Runner service. For more information, see [Observability for your App Runner service](monitor.md).

App Runner supports enabling some observability features and configuring their behavior by using a sharable resource called *ObservabilityConfiguration*. You can provide an observability configuration resource when you create or update a service. The App Runner console creates one for you when you create a new App Runner service. Providing an observability configuration is optional. If you don't provide one, App Runner provides a default observability configuration.

You can share a single observability configuration across multiple App Runner services to ensure they have the same observability behavior. For more information, see [Configuring service settings using sharable resources](manage-configure-resources.md).

You can configure the following observability features using observability configurations:
+ *Trace configuration* – Settings for tracing requests that your application serves and downstream calls that it makes. For more information about tracing, see [Tracing for your App Runner application with X-Ray](monitor-xray.md).

## Manage observability
<a name="manage-configure-observability.manage"></a>

Manage observability for your App Runner services using one of the following methods:

------
#### [ App Runner console ]

When you [create a service](manage-create.md) using the App Runner console, or when you [update its configuration later](manage-configure.md), you can configure observability features for your service. Look for the **Observability** configuration section on the console page. 

![App Runner console configuration page showing observability options](http://docs.aws.amazon.com/apprunner/latest/dg/images/manage-configure-observability.png)


------
#### [ App Runner API or AWS CLI ]

When you call the [CreateService](https://docs.aws.amazon.com/apprunner/latest/api/API_CreateService.html) or [UpdateService](https://docs.aws.amazon.com/apprunner/latest/api/API_UpdateService.html) App Runner API actions, you can use the `ObservabilityConfiguration` parameter object to enable observability features and specify an observability configuration resource for your service.

Use the following App Runner API actions to manage your observability configuration resources.
+ [CreateObservabilityConfiguration](https://docs.aws.amazon.com/apprunner/latest/api/API_CreateObservabilityConfiguration.html) – Creates a new observability configuration or a revision to an existing one.
+ [ListObservabilityConfigurations](https://docs.aws.amazon.com/apprunner/latest/api/API_ListObservabilityConfigurations.html) – Returns a list of the observability configurations that are associated with your AWS account, with summary information.
+ [DescribeObservabilityConfiguration](https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeObservabilityConfiguration.html) – Returns a full description of an observability configuration.
+ [DeleteObservabilityConfiguration](https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteObservabilityConfiguration.html) – Deletes an observability configuration. You can delete a specific revision or the latest active revision. You might need to delete unnecessary observability configurations if you reach the observability configuration quota for your AWS account.

------