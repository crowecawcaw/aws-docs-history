# CloudFormation resources generated

when AWS::Serverless::GraphQLApi is specified

When you specify an `AWS::Serverless::GraphQLApi` resource in an AWS Serverless Application Model
(AWS SAM) template, AWS SAM always creates the following base AWS CloudFormation resources.

**`AWS::AppSync::DataSource`**

_`LogicalId`:_ ``<graphqlapi-LogicalId><datasource-RelativeId><datasource-Type>`DataSource`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

**`AWS::AppSync::FunctionConfiguration`**

_`LogicalId`:_ `<graphqlapi-LogicalId><function-RelativeId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

**`AWS::AppSync::GraphQLApi`**

_`LogicalId`:_ `<graphqlapi-LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

**`AWS::AppSync::GraphQLSchema`**

_`LogicalId`:_ ``<graphqlapi-LogicalId>`Schema`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

**`AWS::AppSync::Resolver`**

_`LogicalId`:_ `<graphqlapi-LogicalId><OperationType><resolver-RelativeId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

In addition to these CloudFormation resources, when `AWS::Serverless::GraphQLApi` is
specified, AWS SAM may also generate the following CloudFormation resources.

`AWS::AppSync::ApiCache`

_`LogicalId`:_ ``<graphqlapi-LogicalId>`ApiCache`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

`AWS::AppSync::ApiKey`

_`LogicalId`:_ `<graphqlapi-LogicalId><apikey-RelativeId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

`AWS::AppSync::DomainName`

_`LogicalId`:_ ``<graphqlapi-LogicalId>`DomainName`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

`AWS::AppSync::DomainNameApiAssociation`

_`LogicalId`:_ ``<graphqlapi-LogicalId>`DomainNameApiAssociation`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

AWS SAM may also use the `AWS::Serverless::Connector` resource to provision
permissions. For more information, see [CloudFormation resources generated when
you specify AWS::Serverless::Connector](sam-specification-generated-resources-connector.md "sam-specification-generated-resources-connector.md").
