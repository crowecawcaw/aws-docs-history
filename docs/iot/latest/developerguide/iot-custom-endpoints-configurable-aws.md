# Creating and configuring AWS

managed domains

You create a configurable endpoint on an AWS managed domain by using the [CreateDomainConfiguration](../apireference/API_CreateDomainConfiguration.md "../apireference/API_CreateDomainConfiguration.md") API. A domain configuration for an AWS managed
domain consists of the following:

- `domainConfigurationName`

A user-defined name that identifies the domain configuration and the value
must be unique to your AWS Region. You can't use domain configuration names
that start with `IoT:` because they are reserved for default
endpoints.

- `defaultAuthorizerName` (optional)

The name of the custom authorizer to use on the endpoint.

- `allowAuthorizerOverride` (optional)

A Boolean value that
specifies whether devices can override the default authorizer by specifying
a different authorizer in the HTTP header of the request. This value is
required if a value for `defaultAuthorizerName` is
specified.

- `serviceType` (optional)

The service type that the endpoint delivers. AWS IoT Core only supports the
`DATA` service type. When you specify `DATA`,
AWS IoT Core returns an endpoint with an endpoint type of
`iot:Data-ATS`. You can't create a configurable `iot:Data`
(VeriSign) endpoint.

- `TlsConfig` (optional)

An object that specifies the TLS configuration for a domain. For more
information, see [Configuring TLS settings in domain
configurations](iot-endpoints-tls-config.md "iot-endpoints-tls-config.md").
The following example AWS CLI command creates a domain configuration for a
`Data` endpoint.

```
aws iot create-domain-configuration --domain-configuration-name "`myDomainConfigurationName`" --service-type "DATA"
```

The output of the command can look like the following.

```
{
    "domainConfigurationName": "`myDomainConfigurationName`",
    "domainConfigurationArn": "arn:aws:iot:`us-east-1`:`123456789012:domainconfiguration/myDomainConfigurationName/itihw`"
}
```
