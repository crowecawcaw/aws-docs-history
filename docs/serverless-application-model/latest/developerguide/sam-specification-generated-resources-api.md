# CloudFormation resources generated when

AWS::Serverless::Api is specified

When an `AWS::Serverless::Api` is specified, AWS Serverless Application Model (AWS SAM) always generates
an `AWS::ApiGateway::RestApi` base CloudFormation resource. In addition, it also always
generates an `AWS::ApiGateway::Stage` and an
`AWS::ApiGateway::Deployment` resource.

**`AWS::ApiGateway::RestApi`**

_`LogicalId`:_ `<api‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

**`AWS::ApiGateway::Stage`**

_`LogicalId`:_ `<api‑LogicalId>`<stage‑name>`Stage`

`<stage‑name>` is the string
that the `StageName` property is set to. For example, if you set
`StageName` to `Gamma`, the `LogicalId` is
``MyRestApiGamma`Stage`.

_Referenceable property:_ ``<api‑LogicalId>`.Stage`

**`AWS::ApiGateway::Deployment`**

_`LogicalId`:_ ``<api‑LogicalId>`Deployment`<sha>``

`<sha>` is a unique hash value
that is generated when the stack is created. For example,
``MyRestApi`Deployment`926eeb5ff1``.

_Referenceable property:_ ``<api‑LogicalId>`.Deployment`

In addition to these CloudFormation resources, when `AWS::Serverless::Api` is specified,
AWS SAM generates additional CloudFormation resources for the following scenarios.

###### Scenarios

- [DomainName
  property is specified](#sam-specification-generated-resources-api-domain-name "#sam-specification-generated-resources-api-domain-name")
- [UsagePlan
  property is specified](#sam-specification-generated-resources-api-usage-plan "#sam-specification-generated-resources-api-usage-plan")

## DomainName

property is specified

When the `DomainName` property of the `Domain` property of an
`AWS::Serverless::Api` is specified, AWS SAM generates the
`AWS::ApiGateway::DomainName` CloudFormation resource.

**`AWS::ApiGateway::DomainName`**

_`LogicalId`:_ `ApiGatewayDomainName`<sha>``

`<sha>` is a unique hash value
that is generated when the stack is created. For example:
`ApiGatewayDomainName`926eeb5ff1``.

_Referenceable property:_ ``<api‑LogicalId>`.DomainName`

## UsagePlan

property is specified

When the `UsagePlan` property of the `Auth` property of an
`AWS::Serverless::Api` is specified, AWS SAM generates the following CloudFormation
resources: `AWS::ApiGateway::UsagePlan`,
`AWS::ApiGateway::UsagePlanKey`, and
`AWS::ApiGateway::ApiKey`.

**`AWS::ApiGateway::UsagePlan`**

_`LogicalId`:_ ``<api‑LogicalId>`UsagePlan`

_Referenceable property:_ ``<api‑LogicalId>`.UsagePlan`

**`AWS::ApiGateway::UsagePlanKey`**

_`LogicalId`:_ ``<api‑LogicalId>`UsagePlanKey`

_Referenceable property:_ ``<api‑LogicalId>`.UsagePlanKey`

**`AWS::ApiGateway::ApiKey`**

_`LogicalId`:_ ``<api‑LogicalId>`ApiKey`

_Referenceable property:_ ``<api‑LogicalId>`.ApiKey`
