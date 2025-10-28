# Enabling IPv6 for incoming traffic

If you want your service to receive incoming network traffic from IPv6 addresses, or from
both IPv4 and IPv6 addresses, choose the **Dual-stack** address type for the
endpoint. When you’re creating a new application, you can find this setting under
**Configure service** > **Networking** section. The
following procedures explain how to enable IPv4 or dual-stack (IPv6 and IPv4) using the App Runner
console or the App Runner API.

## Managing dual stack for incoming traffic

Manage the dual-stack address type for incoming traffic using one of the following
methods:

- [App Runner console](#network-dual-stack-manage.console "#network-dual-stack-manage.console")
- [App Runner API or AWS CLI](#network-dual-stack-manage.api "#network-dual-stack-manage.api")

###### Note

The following procedures explain how to manage the network address type for **public** incoming traffic. For information about managing dual-stack
or IPv4 address types for **private** endpoints, see [Managing Private endpoints](network-pl-manage.md "network-pl-manage.md").

### App Runner console

You can choose dual-stack address type for the incoming internet traffic, when you
create a service using the App Runner console, or when you update its configuration later.

###### To enable dual-stack address type

1. When [creating](manage-create.md "manage-create.md") or [updating](manage-configure.md "manage-configure.md") a service, expand the
   **Networking** section under **Configure service**.
2. Choose **Public endpoint** for **Incoming network
   traffic**. If you select **Public endpoint**, the
   **Endpoint IP address type** option opens.

See [Managing Private endpoints](network-pl-manage.md "network-pl-manage.md") for a procedure to manage dual-stack or IPv4
address types for private endpoints. 3. Expand **Endpoint IP address type** to view the following IP
address types.

    * **IPv4**
    * **Dual-stack (IPv4 and IPv6)**

###### Note

If you do not expand **Endpoint IP address type** to make a
selection, then App Runner assigns IPv4 as the default configuration. 4. Choose **Dual-stack (IPv4 and IPv6)**. 5. Choose **Next** and then **Create & Deploy**
if you are creating a service. Else, choose **Save changes** if you are
updating a service.

When the service is deployed, your application starts receiving network traffic from
both IPv4 and IPv6 endpoints.

###### To change the address type

1. Follow the steps to [update](manage-configure.md "manage-configure.md") a service and
   navigate to Networking.
2. Navigate to **Endpoint IP address type** under **Incoming
   network traffic** and select the required address type.
3. Choose **Save changes.** Your service is updated with your
   selection.

### App Runner API or AWS CLI

When you call the [CreateService](../api/API_CreateService.md "../api/API_CreateService.md")
or [UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md") App Runner API actions,
use the `IpAddressType` member of the `NetworkConfiguration` parameter
to specify the address type. The supported values that you can specify are `IPv4`
and `DUAL_STACK`. Specify `DUAL_STACK` if you want your service to
receive internet traffic from IPv4 and IPv6 endpoints. If you do not specify any value for
`IpAddressType`, by default IPv4 is applied.

###### Note

For private endpoint examples, see [App Runner API or AWS CLI](network-pl-manage.md#network-pl-manage.api "network-pl-manage.md#network-pl-manage.api").

The following is the example to create a service with the dual stack as IP address. This
example calls an `input.json` file.

###### Example Request to create a service with dual stack support

```
`aws apprunner create-service \
 --cli-input-json file://input.json`
```

###### Example Contents of `input.json`

```
`{
 "ServiceName": "example-service",
 "SourceConfiguration": {
 "ImageRepository": {
 "ImageIdentifier": "public.ecr.aws/aws-containers/hello-app-runner:latest",
 "ImageConfiguration": {
 "Port": "8000"
 },
 "ImageRepositoryType": "ECR_PUBLIC"
 },
 "NetworkConfiguration": {
 "IpAddressType": `"DUAL_STACK"`
 }
 }
}`
```

###### Example Response

```
`{
 "Service": {
 "ServiceName": "example-service",
 "ServiceId": "`<service-id>`",
 "ServiceArn": "arn:aws:apprunner:us-east-2:123456789012:service/example-service/`<service-id>`",
 "ServiceUrl": "1234567890.us-east-2.awsapprunner.com",
 "CreatedAt": "2023-10-16T12:30:51.724000-04:00",
 "UpdatedAt": "2023-10-16T12:30:51.724000-04:00",
 "Status": "OPERATION_IN_PROGRESS",
 "SourceConfiguration": {
 "ImageRepository": {
 "ImageIdentifier": "public.ecr.aws/aws-containers/hello-app-runner:latest",
 "ImageConfiguration": {
 "Port": "8000"
 },
 "ImageRepositoryType": "ECR_PUBLIC"
 },
 "AutoDeploymentsEnabled": false
 },
 "InstanceConfiguration": {
 "Cpu": "1024",
 "Memory": "2048"
 },
 "HealthCheckConfiguration": {
 "Protocol": "TCP",
 "Path": "/",
 "Interval": 5,
 "Timeout": 2,
 "HealthyThreshold": 1,
 "UnhealthyThreshold": 5
 },
 "AutoScalingConfigurationSummary": {
 "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-2:123456789012:autoscalingconfiguration/DefaultConfiguration/1/00000000000000000000000000000001",
 "AutoScalingConfigurationName": "DefaultConfiguration",
 "AutoScalingConfigurationRevision": 1
 },
 "NetworkConfiguration": {
 "IpAddressType": "DUAL_STACK",
 "EgressConfiguration": {
 "EgressType": "DEFAULT"
 },
 "IngressConfiguration": {
 "IsPubliclyAccessible": true
 }
 }
 },
 "OperationId": "24bd100b1e111ae1a1f0e1115c4f11de"
}`
```

For more information on the API parameter, see [NetworkConfiguration](../api/API_NetworkConfiguration.md "../api/API_NetworkConfiguration.md").
