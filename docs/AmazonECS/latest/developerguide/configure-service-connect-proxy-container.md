

# Configure Service Connect proxy container
<a name="configure-service-connect-proxy-container"></a>

When a service uses Service Connect, Amazon ECS automatically adds a proxy container to each task in the service. You can configure the settings for this proxy container with the `containerConfigurations` list in the `serviceConnectConfiguration` object. Your changes take effect after you deploy the service.

These settings control the behavior of the proxy container itself, such as the verbosity of the logs that the proxy writes about its own operations. For detailed metadata about the individual requests the proxy handles, use Service Connect access logs instead. For more information, see [Amazon ECS Service Connect access logs](service-connect-envoy-access-logs.md).

## Set the proxy log level
<a name="configure-service-connect-proxy-container-log-level"></a>

The log level setting controls how much operational detail the proxy container writes to its application logs. If you don't specify a log level, the default is `info`.

Set the log level to `debug` to collect more detailed proxy logs when you troubleshoot connectivity and traffic routing issues between services. Debug logging increases the volume of logs that the proxy container writes. Service Connect delivers the proxy logs to the log group you set in the `logConfiguration` of `serviceConnectConfiguration`.

**Important**  
Revert your log level back to `info` once troubleshooting is complete to avoid excessive log generation and storage costs.

The following example sets the proxy log level to `debug`.

```
{
    "serviceConnectConfiguration": {
        "enabled": true,
        "namespace": "myapp.namespace",
        "services": [
            ...
        ],
        "containerConfigurations": [
            {
                "logLevel": "debug"
            }
        ]
    }
}
```