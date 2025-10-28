# Set the routing mode for your custom domain name

You can choose which routing mode API Gateway uses to route traffic to your APIs. For more information, see
[Send traffic
to your APIs through your custom domain name in API Gateway](rest-api-routing-mode.md "rest-api-routing-mode.md"). This section discusses routing modes for custom domain names.
You must set a routing mode for your custom domain name to route traffic to your APIs. The following routing modes
are supported:

- ROUTING_RULE_THEN_API_MAPPING – Use this mode to send traffic to
  your APIs with both routing rules and API mappings. In this mode, all routing rules take priority over any API
  mappings. For an example of this mode, see [Example 2: Routing rules and API mappings](rest-api-routing-rules-examples.md#rest-api-routing-rules-examples-rule-and-mappings "rest-api-routing-rules-examples.md#rest-api-routing-rules-examples-rule-and-mappings").
- ROUTING_RULE_ONLY – Use this mode to only allow routing rules to
  send traffic to your APIs. When your custom domain name uses this mode, you can't create an API mapping, but
  you can use the [get-api-mappings](../../../cli/latest/reference/apigatewayv2/get-api-mappings.md "../../../cli/latest/reference/apigatewayv2/get-api-mappings.md") command
  to view them. API callers can’t use API mappings to access this domain name.
- API_MAPPING_ONLY – Use this mode to only allow API mappings to send
  traffic to your APIs. When your custom domain name uses this mode, you can't create a routing rule, but you
  can use the `list-routing-rules` command to view them. API callers can’t use routing rules to
  access this domain name.

This is the default routing mode for all your existing domain names, and any new domain names you create.
When you create a custom domain name using `apigateway`, `API_MAPPING_ONLY` is called
`BASE_PATH_MAPPING_ONLY` and `ROUTING_RULE_THEN_API_MAPPING` is called
`ROUTING_RULE_THEN_BASE_PATH_MAPPING`. This behavior is only present for the AWS CLI, AWS CloudFormation, or any
SDKs, not in the AWS Management Console.

The following procedure shows how to change the routing mode for an existing custom domain name. When you
change the routing mode of your custom domain name, API callers can’t access your domain name using any
unsupported routing modes.

AWS Management Console1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway"). 2. Choose **Custom domain names** from the main navigation
pane. 3. Choose a custom domain name. 4. For **Domain details**, choose
**Edit**. 5. For **Routing mode**, choose
**ROUTING_RULE_THEN_API_MAPPING**. 6. Choose **Save**.

If you change the routing mode to `ROUTING_RULE_ONLY` or `API_MAPPING_ONLY`, any
API mappings or routing rules you've created are removed from the domain name details page of the console. If you
change the routing mode to support either routing rules or API mappings, these resources will return.

AWS CLI - apigatewayv2
The following
[update-domain-name](../../../cli/latest/reference/apigatewayv2/update-domain-name.md "../../../cli/latest/reference/apigatewayv2/update-domain-name.md") command updates a domain name to use the routing mode
`ROUTING_RULE_THEN_API_MAPPING`:

```
aws apigatewayv2 update-domain-name \
  --domain-name 'api.example.com' \
  --routing-mode "ROUTING_RULE_THEN_API_MAPPING"
```

The output will look like the following:

```
{
"ApiMappingSelectionExpression": "$request.basepath",
"DomainName": "api.example.com",
"DomainNameArn": "arn:aws:apigateway:us-west-2::/domainnames/api.example.com",
"DomainNameConfigurations": [
  {
      "ApiGatewayDomainName": "d-abcdefg.execute-api.us-west-2.amazonaws.com",
      "CertificateArn": "arn:aws:acm:us-west-2:111122223333:certificate/abcdefg-123456-abcdefg",
      "DomainNameStatus": "AVAILABLE",
      "EndpointType": "REGIONAL",
      "HostedZoneId": "Z2OJLYMUO9EFXC",
      "SecurityPolicy": "TLS_1_2"
   }
 ],
"RoutingMode": "ROUTING_RULE_THEN_API_MAPPING",
"Tags": {}
}
```

AWS CLI - apigateway
The following
[update-domain-name](../../../cli/latest/reference/apigateway/update-domain-name.md "../../../cli/latest/reference/apigateway/update-domain-name.md") command updates a private custom domain name to use the routing mode
`ROUTING_RULE_THEN_BASE_PATH_MAPPING`:

```
aws apigateway update-domain-name \
  --domain-name 'private.example.com' \
  --patch-operations "op='replace',path='/routingMode',value='ROUTING_RULE_THEN_BASE_PATH_MAPPING'"
```

The output will look like the following:

```
{
"domainName": "private.example.com",
"domainNameId": "abcd1234",
"domainNameArn": "arn:aws:apigateway:us-west-2:111122223333:/domainnames/private.example.com+abcd1234",
"certificateArn": "arn:aws:acm:us-west-2:111122223333:certificate/a1b2c3d4-5678-90ab-cdef",
"certificateUploadDate": "2024-09-10T10:31:20-07:00",
"endpointConfiguration": {
  "types": [
    "PRIVATE"
   ],
  "ipAddressType": "dualstack"
  },
"domainNameStatus": "AVAILABLE",
"securityPolicy": "TLS_1_2",
"policy": "...",
"routingMode" : "ROUTING_RULE_THEN_BASE_PATH_MAPPING"
}
```
