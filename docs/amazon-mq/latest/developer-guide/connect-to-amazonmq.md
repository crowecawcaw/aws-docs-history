

# Connecting to Amazon MQ
<a name="connect-to-amazonmq"></a>

You can connect to Amazon MQ from other AWS services using service endpoints and broker endpoints. 

## Service endpoints
<a name="connect-service-enpoints"></a>

The following connection methods are used for the **Amazon MQ service API:**


| Domains | Connection method | 
| --- | --- | 
| `mq.{{region}}.amazonaws.com` | IPv4 | 
| `mq.{{region}}.api.aws` | Dual-stack (IPv4 and IPv6) | 
| `mq-fips.{{region}}.amazonaws.com` | FIPS with IPv4 only | 
| `mq-fips.{{region}}.api.aws` | FIPS with Dual-stack | 

## Broker endpoints
<a name="connect-broker-endpoints"></a>

The following connection methods are used for **Amazon MQ brokers:**


| Domains | Connection method | 
| --- | --- | 
| `{{brokerId}}.mq.{{region}}.amazonaws.com` | IPv4 | 
| `{{brokerId}}.mq.{{region}}.on.aws` | Dual-stack (IPv4 and IPv6) Amazon MQ for ActiveMQ brokers do not support dual-stack. | 

## Connect to Amazon MQ using Dual-stack (IPv4 and IPv6) endpoints
<a name="dual-stack-enpoints"></a>

 Dual-stack endpoints support both IPv4 and IPv6 traffic. When you make a request to a dual-stack endpoint, the endpoint URL resolves to an IPv4 or an IPv6 address. For more information on dual-stack and FIPS endpoints, see the [SDK Reference guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html). 

 Amazon MQ supports Regional dual-stack endpoints, which means that you must specify the AWS Region as part of the endpoint name. Dual-stack endpoint names use the following naming convention: `mq.{{region}}.api.aws`. For example, the dual-stack endpoint name for the `eu-west-1` Region is `mq.eu-west-1.api.aws`. 

For the full list of Amazon MQ endpoints, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/amazon-mq.html). 

## Connect to Amazon MQ using AWS PrivateLink
<a name="connect-with-private-link"></a>

 [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) endpoints for Amazon MQ API with support for IPv4 and IPv6 provides private connectivity between virtual private clouds (VPCs) and the Amazon MQ API without exposing your traffic to the public internet. 

**Note**  
 Support for PrivateLink is only available for the Amazon MQ API endpoint, not the broker endpoint. For more information on privately connecting to a broker endpoint, see [Configuring a private Amazon MQ broker](configuring-private-broker.md). 

 To access Amazon MQ API using PrivateLink, you must first create an [interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the specific VPC you want to connect from. When you create the VPC endpoint, use the service name `com.amazonaws.{{region}}.mq` or `com.amazonaws.{{region}}.mq-fips` for FIPS endpoints. 

 When you call Amazon MQ using the AWS CLI or SDK, you must specify the endpoint URL to use the dual-stack domain name: `mq.{{region}}.api.aws` or `mq-fips.{{region}}.api.aws`. PrivateLink for Amazon MQ does not support the default domain name ending in `amazonaws.com`. For more information , see [Dual-stack and FIPS endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html) in the SDK Reference Guide. 

 The following CLI example shows how to call the `describe-broker-engine-type` in the Asia Pacific (Sydney) Region through an Amazon MQ VPC endpoint. 

```
AWS_USE_DUALSTACK=true aws mq describe-broker-engine-types --region ap-southeast-2
```

 For other ways to configure the endpoint in CLI, see [Using endpoints in the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-endpoints.html) 

 You can also determine user access to the VPC endpoints using VPC endpoint policies. For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html). 