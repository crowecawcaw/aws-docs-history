# Configuring an App Runner service

When you [create an AWS App Runner service](manage-create.md "manage-create.md"), you set various configuration values. You can change some of these
configuration settings after you create the service. Other settings can be applied only while creating the service and cannot be changed thereafter. This
topic discusses the configuration of your service using the App Runner API, the App Runner console, and an App Runner configuration file.

###### Topics

- [Configure your service using the App Runner API or AWS CLI](#manage-configure.api "#manage-configure.api")
- [Configure your service using the App Runner console](#manage-configure.console "#manage-configure.console")
- [Configure your service using an App Runner configuration file](#manage-configure.file "#manage-configure.file")
- [Configuring observability for your service](manage-configure-observability.md "manage-configure-observability.md")
- [Configuring service settings using sharable resources](manage-configure-resources.md "manage-configure-resources.md")
- [Configuring health checks for your service](manage-configure-healthcheck.md "manage-configure-healthcheck.md")

## Configure your service using the App Runner API or AWS CLI

The API defines which settings can be changed after service creation. The following list discusses the relevant actions, types, and
limitations.

- [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") action – Can be called after creation to update some configuration
  settings.
  - _Can be updated_ – You can update settings in the `SourceConfiguration`,
    `InstanceConfiguration`, and `HealthCheckConfiguration` parameters. However, in `SourceConfiguration`, you
    can't switch your source type from code to image or the other way around. You must provide the same repositoryparameter as you provided when you
    created the service. It's either `CodeRepository` or `ImageRepository`.

  You can also update the following ARNs of separate configuration resources associated with the service:

      - `AutoScalingConfigurationArn`
      - `VpcConnectorArn`

  - _Cannot be updated_ – You can't change the `ServiceName` and `EncryptionConfiguration`
    parameters that are available in the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md") action. They can't be changed after
    they're created. The [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") action doesn't include these parameters.
  - _API vs. file_ – You can set the `ConfigurationSource` parameter of the [CodeConfiguration](../api/API_CodeConfiguration.md "../api/API_CodeConfiguration.md") type (used for source code repositories as part of
    `SourceConfiguration`) to `Repository`. In this case, App Runner ignores the configuration settings in
    `CodeConfigurationValues`, and reads these settings from a [configuration file](config-file.md "config-file.md") in your repository.
    If you set `ConfigurationSource` to `API`, App Runner gets all configuration settings from the API call and ignores the
    configuration file, even if one exists.

- [TagResource](../api/API_TagResource.md "../api/API_TagResource.md") action – Can be called after your service is created to add tags to the
  service or update values of existing tags.
- [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md") action – Can be called after your service is created to remove tags
  from the service.

###### Note

If you create an outbound traffic VPC connector for a service, the service startup process that follows will experience a one-time latency. You can set
this configuration for a new service when you create it, or afterward, with a service update. For more information, see [One-time latency](network-vpc.md#network-vpc.VPC-connector.latency "network-vpc.md#network-vpc.VPC-connector.latency") in the _Networking with App Runner_
chapter of this guide.

## Configure your service using the App Runner console

The console uses the App Runner API to apply configuration updates. The update rules that the API imposes, as defined in the previous section, determine
what you can configure using the console. Some settings that were available during service creation aren't available for modification later on. In
addition, if you decide to use a [configuration file](config-file.md "config-file.md"), additional settings are hidden in the console, and App Runner reads them
from the file.

###### To configure your service

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Services**, and then choose your App Runner service.

The console displays the service dashboard with a **Service overview**.

![App Runner service dashboard page showing Activity list](/images/apprunner/latest/dg/images/console-dashboard.png) 3. On the service dashboard page, choose the **Configuration** tab.

Result: The console displays the current configuration settings of your service in several sections: **Source and deployment**,
**Configure build**, and **Configure service**. 4. To update settings in any category, choose **Edit**. 5. On the configuration edit page, make any desired changes, and then choose **Save changes**.

###### Note

If you create an outbound traffic VPC connector for a service, the service startup process that follows will experience a one-time latency. You can set
this configuration for a new service when you create it, or afterward, with a service update. For more information, see [One-time latency](network-vpc.md#network-vpc.VPC-connector.latency "network-vpc.md#network-vpc.VPC-connector.latency") in the _Networking with App Runner_
chapter of this guide.

## Configure your service using an App Runner configuration file

When you create or update an App Runner service, you can instruct App Runner to read some configuration settings from a configuration file that you provide as
part of your source repository. By doing this, you can manage the settings that are related to your source code under source control, together with the
code itself. The configuration file also provides certain advanced settings that you can't set using the console or the API. For more information, see
[Setting App Runner service options using a configuration file](config-file.md "config-file.md").

###### Note

If you create an outbound traffic VPC connector for a service, the service startup process that follows will experience a one-time latency. You can set
this configuration for a new service when you create it, or afterward, with a service update. For more information, see [One-time latency](network-vpc.md#network-vpc.VPC-connector.latency "network-vpc.md#network-vpc.VPC-connector.latency") in the _Networking with App Runner_
chapter of this guide.
