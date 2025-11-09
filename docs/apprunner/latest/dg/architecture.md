# App Runner architecture and concepts

AWS App Runner takes your source code or source image from a repository, and creates and maintains a running web service for you in the AWS Cloud.
Typically, you need to call just one App Runner action, [CreateService](../api/API_CreateService.md "../api/API_CreateService.md"), to create your service.

With a source image repository, you provide a ready-to-use container image that App Runner can deploy to run your web service. With a source code repository,
you provide your code and instructions for building and running a web service, and you target a specific runtime environment. App Runner supports several
programming platforms, each with one or more managed runtimes for platform major versions.

At this time, App Runner can retrieve your source code from either a [Bitbucket](https://bitbucket.org/ "https://bitbucket.org/") or [GitHub](https://github.com/ "https://github.com/") repository, or it can retrieve your source image from [Amazon Elastic Container Registry (Amazon ECR)](../../../AmazonECR/latest/userguide.md "../../../AmazonECR/latest/userguide.md") in your AWS account.

The following diagram shows an overview of the App Runner service architecture. In the diagram, there are two example services: one deploys source code from
GitHub, and the other deploys a source image from Amazon ECR. The same flow applies to the Bitbucket repository.

![The App Runner architecture](images/architecture.png)

## App Runner concepts

The following are key concepts related to your web service that's running in App Runner:

- _App Runner service_ – An AWS resource that App Runner uses to deploy and manage your application based on its source code
  repository or container image. An App Runner service is a running version of your application. For more information about creating a service, see [Creating an App Runner service](manage-create.md "manage-create.md").
- _Source type_ – The type of source repository that you provide for deploying your App Runner service: [source code](service-source-code.md "service-source-code.md") or [source image](service-source-image.md "service-source-image.md").
- _Repository provider_ – The repository service that contains your application source (for example, [GitHub](service-source-code.md#service-source-code.providers.github "service-source-code.md#service-source-code.providers.github"), [Bitbucket](service-source-code.md#service-source-code.providers.github "service-source-code.md#service-source-code.providers.github"), or [Amazon ECR](service-source-image.md#service-source-image.providers.ecr "service-source-image.md#service-source-image.providers.ecr")).
- _App Runner connection_ – An AWS resource that lets App Runner access a repository provider account (for example, a GitHub account
  or organization). For more information about connections, see [Managing App Runner connections](manage-connections.md "manage-connections.md").
- _Runtime_ – A base image for deploying a source code repository. App Runner provides a variety of _managed
  runtimes_ for different programming platforms and versions.

For more information, see [App Runner service based on source code](service-source-code.md "service-source-code.md").

- _Deployment_ – An action that applies a version of your source repository (code or image) to an App Runner service. The first
  deployment to the service occurs as part of service creation. Later deployments can occur in one of two ways:
  - _Automatic deployment_ – A CI/CD capability. You can configure an App Runner service to automatically build (for source
    code) and deploy each version of your application as it appears in the repository. This can be a new commit in a source code repository or a new
    image version in a source image repository.
  - _Manual deployment_ – A deployment to your App Runner service that you explicitly start.

- _Custom domain_ – A domain that you associate with your App Runner service. Users of your web application can use this domain
  to access your web service instead of the default App Runner subdomain. For more information, see [Managing custom domain names for an App Runner service](manage-custom-domains.md "manage-custom-domains.md").

###### Note

To augment the security of your App Runner applications, the _\*.awsapprunner.com_ domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further security, we recommend that you use cookies with a `__Host-`
prefix if you ever need to set sensitive cookies in the default domain name for your App Runner applications.
This practice will help to defend your domain against cross-site request
forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.

- _Maintenance_ – An activity that App Runner occasionally performs on the infrastructure that runs your App Runner service. When
  maintenance is in progress, service status temporarily changes to `OPERATION_IN_PROGRESS` (**Operation in progress** in
  the console) for a few minutes. Actions on your service (for example, deployment, configuration update, pause/resume, or deletion) are blocked during
  this time. Try the action again a few minutes later, when the service status returns to `RUNNING`.

###### Note

If your action fails, it doesn't mean that your App Runner service is down. Your application is active and keeps handling requests. It's unlikely for
your service to experience any downtime.

In particular, App Runner migrates your service if it detects issues in the underlying hardware hosting the service. To prevent any service downtime,
App Runner deploys your service to a new set of instances and shifts traffic to them (a blue-green deployment). You might occasionally see a slight
temporary increase in charges.

## App Runner supported configurations

When you configure an App Runner service, you specify the virtual CPU and memory configuration to allocate to your service.
You pay based on the compute configuration that you select. For more information on pricing, see [AWS Resource Groups
Pricing](https://aws.amazon.com/apprunner/pricing "https://aws.amazon.com/apprunner/pricing").

The following table provides information on the vCPU and memory configurations that App Runner supports:

| **CPU**   | **Memory** |
| --------- | ---------- |
| 0.25 vCPU | 0.5 GB     |
| 0.25 vCPU | 1 GB       |
| 0.5 vCPU  | 1 GB       |
| 1 vCPU    | 2 GB       |
| 1 vCPU    | 3 GB       |
| 1 vCPU    | 4 GB       |
| 2 vCPU    | 4 GB       |
| 2 vCPU    | 6 GB       |
| 4 vCPU    | 8 GB       |
| 4 vCPU    | 10 GB      |
| 4 vCPU    | 12 GB      |

## App Runner resources

When you use App Runner, you create and manage a few types of resources in your AWS account. These resources are used to access your code and manage your
services.

The following table provides an overview of these resources:

| **Resource name**          | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service                    | Represents a running version of your application. Much of the rest of this guide describes service types, management, configuration, and<br>monitoring.<br>ARN:<br>`arn:aws:apprunner:`region`:`account-id`:service/`service-name`[/`service-id`]`                                                                                                                                                                                                                                                                      |
| Connection                 | Provides your App Runner services with access to private repositories stored with third-party providers. Exists as a separate resource for sharing<br>across multiple services. For more information about connections, see [Managing App Runner connections](manage-connections.md "manage-connections.md").<br>ARN:<br>`arn:aws:apprunner:`region`:`account-id`:connection/`connection-name`[/`connection-id`]`                                                                                                       |
| AutoScalingConfiguration   | Provides your App Runner services with settings that control the automatic scaling of your application. Exists as a separate resource for sharing<br>across multiple services. For more information about automatic scaling, see [Managing App Runner automatic scaling](manage-autoscaling.md "manage-autoscaling.md").<br>ARN:<br>`arn:aws:apprunner:`region`:`account-id`:autoscalingconfiguration/`config-name`[/`config-revision`[/`config-id`]]`                                                                  |
| ObservabilityConfiguration | Configures additional application observability features for your App Runner services. Exists as a separate resource for sharing across multiple<br>services. For more information about observability configuration, see [Configuring observability for your service](manage-configure-observability.md "manage-configure-observability.md").<br>ARN:<br>`arn:aws:apprunner:`region`:`account-id`:observabilityconfiguration/`config-name`[/`config-revision`[/`config-id`]]`                                          |
| VpcConnector               | Configures VPC settings for your App Runner services. Exists as a separate resource for sharing across multiple services. For more information<br>about VPC functionality, see [Enabling VPC access for outgoing traffic](network-vpc.md "network-vpc.md") .<br>ARN:<br>`arn:aws:apprunner:`region`:`account-id`:vpcconnector/`connector-name`[/`connector-revision`[/`connector-id`]]`                                                                                                                                 |
| VpcIngressConnection       | It's an AWS App Runner resource used to configure incoming traffic. It establishes a connection between a VPC interface endpoint and App Runner service,<br>to make your App Runner service accessible from only within an Amazon VPC. For more information about functionality of VPCIngressConnection, see [Enabling Private endpoint for incoming traffic](network-pl.md "network-pl.md").<br>ARN:<br>`arn:aws:apprunner:`region`:`account-id`:vpcingressconnection/`vpc-ingress-connection-name`[/`connector-id`]]` |

## App Runner resource quotas

AWS imposes some quotas (also known as limits) on your account for AWS resource usage in each AWS Region. The following table lists quotas
related to App Runner resources. Quotas are also listed in [AWS App Runner endpoints and quotas](../../../general/latest/gr/apprunner.md "../../../general/latest/gr/apprunner.md") in the _AWS General Reference_.

| **Resource quota**           | **Description**                                                                                                                                                                                                              | **Default value**                                                                                                                                                                                                   | **Adjustable?** |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | --- |
| Services                     | The maximum number of services that you can create in your account for each AWS Region.                                                                                                                                      | 30                                                                                                                                                                                                                  | Yes             |
| Connections                  | The maximum number of connections that you can create in your account for each AWS Region. You can use a single connection in multiple<br>services.                                                                          | 10                                                                                                                                                                                                                  | Yes             |
| Auto scaling configurations  | names                                                                                                                                                                                                                        | The maximum number of unique names that you can have in auto scaling configurations that you create in your account for each AWS Region.<br>You can use a single auto scaling configuration in multiple services.   | 10              | Yes |
| revisions per name           | The maximum number of auto scaling configuration revisions that you can create in your account for each AWS Region for each unique name.<br>You can use a single auto scaling configuration revision in multiple services.   | 5                                                                                                                                                                                                                   | No              |
| Observability configurations | names                                                                                                                                                                                                                        | The maximum number of unique names that you can have in observability configurations that you create in your account for each AWS Region.<br>You can use a single observability configuration in multiple services. | 10              | Yes |
| revisions per name           | The maximum number of observability configuration revisions that you can create in your account for each AWS Region for each unique name.<br>You can use a single observability configuration revision in multiple services. | 10                                                                                                                                                                                                                  | No              |
| VPC connectors               | The maximum number of VPC connectors that you can create in your account for each AWS Region. You can use a single VPC connector in<br>multiple services.                                                                    | 10                                                                                                                                                                                                                  | Yes             |
| VPC Ingress Connection       | The maximum number of VPC Ingress Connections that you can create in your account for each AWS Region. You can use a single VPC Ingress<br>Connection to access<br>multiple App Runner services.                             | 1                                                                                                                                                                                                                   | No              |

Most quotas are adjustable, and you can request a quota increase for them. For more information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the Service Quotas User Guide.
