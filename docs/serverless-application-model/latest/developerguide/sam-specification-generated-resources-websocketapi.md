

# CloudFormation resources generated when AWS::Serverless::WebSocketApi is specified
<a name="sam-specification-generated-resources-websocketapi"></a>

When an `AWS::Serverless::WebSocketApi` is specified, AWS Serverless Application Model (AWS SAM) generates an `AWS::ApiGatewayV2::Api` base CloudFormation resource. In addition, it also always generates an `AWS::ApiGatewayV2::Stage` resource, and for each route defined in the `Routes` property, AWS SAM generates `AWS::ApiGatewayV2::Route`, `AWS::ApiGatewayV2::Integration`, and `AWS::Lambda::Permission` resources.

**`AWS::ApiGatewayV2::Api`**  
*`LogicalId`: *`{{<websocketapi‑LogicalId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::ApiGatewayV2::Stage`**  
*`LogicalId`: *`{{<websocketapi‑LogicalId>}}{{<stage‑name>}}Stage`  
`{{<stage‑name>}}` is the string that the `StageName` property is set to. If `StageName` is not specified, the default value is `default`. For example, if you set `StageName` to `prod`, the `LogicalId` is `{{MyWebSocketApi}}prodStage`.  
*Referenceable property: *`{{<websocketapi‑LogicalId>}}.Stage`

**`AWS::ApiGatewayV2::Route`**  
*`LogicalId`: *`{{<websocketapi‑LogicalId>}}{{<normalized‑route‑key>}}Route`  
`{{<normalized‑route‑key>}}` is the route key with special characters removed. For example, for route key `$connect`, the `LogicalId` is `{{MyWebSocketApi}}connectRoute`.  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::ApiGatewayV2::Integration`**  
*`LogicalId`: *`{{<websocketapi‑LogicalId>}}{{<normalized‑route‑key>}}Integration`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::Lambda::Permission`**  
*`LogicalId`: *`{{<websocketapi‑LogicalId>}}{{<normalized‑route‑key>}}Permission`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to these CloudFormation resources, when `AWS::Serverless::WebSocketApi` is specified, AWS SAM also generates CloudFormation resources for the following scenarios:

**Topics**
+ [Auth property is specified with AuthType set to CUSTOM](#sam-specification-generated-resources-websocketapi-auth)
+ [DomainName property is specified](#sam-specification-generated-resources-websocketapi-domain-name)
+ [BasePath property is specified](#sam-specification-generated-resources-websocketapi-basepath)
+ [Route53 property is specified](#sam-specification-generated-resources-websocketapi-route53)

## Auth property is specified with AuthType set to CUSTOM
<a name="sam-specification-generated-resources-websocketapi-auth"></a>

When the `Auth` property of an `AWS::Serverless::WebSocketApi` is specified with `AuthType` set to `CUSTOM`, AWS SAM generates an `AWS::ApiGatewayV2::Authorizer` CloudFormation resource. If `InvokeRole` is not specified, AWS SAM also generates an `AWS::Lambda::Permission` resource to allow API Gateway to invoke the authorizer function.

**`AWS::ApiGatewayV2::Authorizer`**  
*`LogicalId`: *`{{<websocketapi‑LogicalId>}}Authorizer`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::Lambda::Permission` (when `InvokeRole` is not specified)**  
*`LogicalId`: *`{{<websocketapi‑LogicalId>}}AuthorizerPermission`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

## DomainName property is specified
<a name="sam-specification-generated-resources-websocketapi-domain-name"></a>

When the `DomainName` property of the `Domain` property of an `AWS::Serverless::WebSocketApi` is specified, AWS SAM generates the `AWS::ApiGatewayV2::DomainName` CloudFormation resource.

**`AWS::ApiGatewayV2::DomainName`**  
*`LogicalId`: *`ApiGatewayDomainNameV2{{<sha>}}`  
`{{<sha>}}` is a unique hash value that is generated when the stack is created. For example: `ApiGatewayDomainNameV2{{926eeb5ff1}}`.  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

## BasePath property is specified
<a name="sam-specification-generated-resources-websocketapi-basepath"></a>

When the `BasePath` property of the `Domain` property of an `AWS::Serverless::WebSocketApi` is specified, AWS SAM generates `AWS::ApiGatewayV2::ApiMapping` CloudFormation resources, one for each base path specified.

**`AWS::ApiGatewayV2::ApiMapping`**  
*`LogicalId`: *`{{<websocketapi‑LogicalId>}}{{<basepath>}}ApiMapping`  
`{{<basepath>}}` is the base path value. For example, if you specify `v1` as a base path, the `LogicalId` is `{{MyWebSocketApi}}v1ApiMapping`.  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

## Route53 property is specified
<a name="sam-specification-generated-resources-websocketapi-route53"></a>

When the `Route53` property of the `Domain` property of an `AWS::Serverless::WebSocketApi` is specified, AWS SAM generates an `AWS::Route53::RecordSetGroup` CloudFormation resource.

**`AWS::Route53::RecordSetGroup`**  
*`LogicalId`: *`RecordSetGroup{{<sha>}}`  
`{{<sha>}}` is a unique hash value that is generated when the stack is created. For example: `RecordSetGroup{{926eeb5ff1}}`.  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)