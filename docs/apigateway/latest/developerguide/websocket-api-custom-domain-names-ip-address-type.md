# IP address types for custom domain names for WebSocket APIs

When you create an custom domain name, you specify the type of IP addresses that can invoke your domain. You can choose IPv4 to
resolve IPv4 addresses to invoke your domain, or you can choose dualstack to allow both IPv4 and IPv6 addresses to invoke
your domain. We recommend that you set the IP address type to dualstack to alleviate IP space exhaustion or for your security
posture. For more information about the benefits of a dualstack IP address
type, see
[IPv6 on
AWS](../../../whitepapers/latest/ipv6-on-aws/internet-protocol-version-6.md "../../../whitepapers/latest/ipv6-on-aws/internet-protocol-version-6.md").

## Considerations for IP address types

The following considerations might impact your use of IP address types.

- The default IP address type for API Gateway custom domain names is IPv4.
- Your custom domain name doesn't need to have the same IP address type for all APIs mapped to it. If you
  disable your default API endpoint, this might affect how callers can invoke your API.

## Change the IP address type of custom domain name

You can change the IP address type by updating the domain name's endpoint configuration. You can update the
endpoint configuration by using the AWS Management Console, the AWS CLI, CloudFormation, or an AWS SDK.

AWS Management Console###### To change the IP address type of a custom domain name

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose a public custom domain name.
3. Choose **Endpoint configuration**.
4. For IP address type, select either **IPv4** or **Dualstack**.
5. Choose **Save**.

AWS CLI
The following [update-domain-name](../../../cli/latest/reference/apigatewayv2/update-domain-name.md "../../../cli/latest/reference/apigatewayv2/update-domain-name.md")
command updates an API to have an IP address type of dualstack:

```
aws apigatewayv2 update-domain-name \
   --domain-name dualstack.example.com \
   --domain-name-configurations CertificateArn=arn:aws:acm:us-east-1:111122223333:certificate/abcd1234-5678-abc,IpAddressType=dualstack
```

The output will look like the following:

```
{
    "ApiMappingSelectionExpression": "$request.basepath",
    "DomainName": "dualstack.example.com",
    "DomainNameConfigurations": [
        {
            "ApiGatewayDomainName": "d-abcd1234.execute-api.us-east-1.amazonaws.com",
            "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/abcd1234-5678-abc",
            "DomainNameStatus": "AVAILABLE",
            "EndpointType": "REGIONAL",
            "HostedZoneId": "Z3LQWSYCGH4ADY",
            "SecurityPolicy": "TLS_1_2",
            "IpAddressType": "dualstack"
        }
    ],
    "Tags": {}
}
```
