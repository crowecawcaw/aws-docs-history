# Modules

Modules are configurable components that process RTB traffic flowing through your links.
You can use modules to implement rate limiting, filtering, error handling, and other traffic
management capabilities. RTB Fabric provides built-in modules that are available at no additional
charge, and you can configure them using the RTB Fabric API.

On a link details page, choose the **Modules** tab to view
information about modules that have been configured for the current link. RTB Fabric
only supports viewing modules in the console. You can configure modules with the RTB Fabric
API using the `UpdateLinkModuleFlow` operation.

###### Topics

- [Built-in modules](#built-in-modules "#built-in-modules")
- [Configuring modules](#configuring-modules "#configuring-modules")

## Built-in modules

RTB Fabric provides the following built-in modules that you can configure for your links:

- **QPS rate limiter** – Controls the rate of requests flowing through the link by limiting queries per second (QPS).
  This module helps protect downstream systems from traffic spikes and ensures consistent
  performance under varying load conditions.
- **OpenRTB filter** – Filters RTB requests and responses based on OpenRTB protocol specifications.
  This module validates message formats, removes invalid fields, and ensures
  compliance with OpenRTB standards.
- **Error masker** – Masks sensitive information in error responses to prevent data leakage while
  maintaining debugging capabilities. This module helps protect confidential data
  when errors occur during RTB processing.

All built-in modules are available at no additional charge. You can configure multiple
modules on a single link, and they will be applied in the order you specify during configuration.

## Configuring modules

Module configuration is only available through the RTB Fabric API. You cannot configure
modules using the RTB Fabric console. Use the [UpdateLinkModuleFlow API operation](../api/API_UpdateLinkModuleFlow.md "../api/API_UpdateLinkModuleFlow.md")
to add, modify, or remove modules from your links. This operation allows you to define the
processing flow for RTB traffic by specifying which modules to apply, their configuration
parameters, and the order in which they execute.

### Example: Adding a QPS rate limiter module

The following example shows how to add a QPS rate limiter module to a link using the AWS Command Line Interface (AWS CLI).

**Add a QPS rate limiter module to a link**

```
`$` `aws rtbfabric update-link-module-flow \
--gateway-id `rtb-gw-source123` \
--link-id `link-abc456def` \
--client-token `"unique-update-token-789"` \
--modules `'[
 {
 "name": "rate-limiter-module",
 "version": "1.0.0",
 "dependsOn": [],
 "moduleParameters": {
 "rateLimiter": {
 "tps": 1000.0
 }
 }
 }
]'` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

For detailed information about module configuration parameters and API usage,
see the [AWS RTB Fabric API Reference](../api.md "../api.md").
