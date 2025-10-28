# AWS CloudFormation resources generated

when AWS::Serverless::HttpApi is specified

When an `AWS::Serverless::HttpApi` is specified, AWS Serverless Application Model
(AWS SAM) generates an `AWS::ApiGatewayV2::Api` base AWS CloudFormation resource.

**`AWS::ApiGatewayV2::Api`**

_`LogicalId`:_ `<httpapi‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

In addition to this AWS CloudFormation resource, when `AWS::Serverless::HttpApi` is
specified, AWS SAM also generates AWS CloudFormation resources for the following scenarios:

###### Scenarios

- [StageName
  property is specified](#sam-specification-generated-resources-httpapi-stage-name "#sam-specification-generated-resources-httpapi-stage-name")
- [StageName
  property is not specified](#sam-specification-generated-resources-httpapi-not-stage-name "#sam-specification-generated-resources-httpapi-not-stage-name")
- [DomainName
  property is specified](#sam-specification-generated-resources-httpapi-domain-name "#sam-specification-generated-resources-httpapi-domain-name")

## StageName

property is specified

When the `StageName` property of an `AWS::Serverless::HttpApi`
is specified, AWS SAM generates the `AWS::ApiGatewayV2::Stage` AWS CloudFormation
resource.

**`AWS::ApiGatewayV2::Stage`**

_`LogicalId`:_ `<httpapi‑LogicalId>`<stage‑name>`Stage`

`<stage‑name>` is the
string that the `StageName` property is set to. For example, if
you set `StageName` to `Gamma`, the
`LogicalId` is:
`MyHttpApiGamma`Stage.

_Referenceable property:_ ``<httpapi‑LogicalId>`.Stage`

## StageName

property is _not_ specified

When the `StageName` property of an `AWS::Serverless::HttpApi`
is _not_ specified, AWS SAM generates the
`AWS::ApiGatewayV2::Stage` AWS CloudFormation resource.

**`AWS::ApiGatewayV2::Stage`**

_`LogicalId`:_ ``<httpapi‑LogicalId>`ApiGatewayDefaultStage`

_Referenceable property:_ ``<httpapi‑LogicalId>`.Stage`

## DomainName

property is specified

When the `DomainName` property of the `Domain` property of an
`AWS::Serverless::HttpApi` is specified, AWS SAM generates the
`AWS::ApiGatewayV2::DomainName` AWS CloudFormation resource.

**`AWS::ApiGatewayV2::DomainName`**

_`LogicalId`:_ `ApiGatewayDomainNameV2`<sha>``

`<sha>` is a unique hash value
that is generated when the stack is created. For example,
`ApiGatewayDomainNameV2``926eeb5ff1`.

_Referenceable property:_ ``<httpapi‑LogicalId>`.DomainName`
