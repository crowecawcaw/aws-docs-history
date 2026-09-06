

# CloudFormation resources generated when AWS::Serverless::GraphQLApi is specified
<a name="sam-specification-generated-resources-graphqlapi"></a>

When you specify an `AWS::Serverless::GraphQLApi` resource in an AWS Serverless Application Model (AWS SAM) template, AWS SAM always creates the following base AWS CloudFormation resources.

**`AWS::AppSync::DataSource`**  
*`LogicalId`: *`{{<graphqlapi-LogicalId><datasource-RelativeId><datasource-Type>}}DataSource`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::AppSync::FunctionConfiguration`**  
*`LogicalId`: *`{{<graphqlapi-LogicalId><function-RelativeId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::AppSync::GraphQLApi`**  
*`LogicalId`: *`{{<graphqlapi-LogicalId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::AppSync::GraphQLSchema`**  
*`LogicalId`: *`{{<graphqlapi-LogicalId>}}Schema`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::AppSync::Resolver`**  
*`LogicalId`: *`{{<graphqlapi-LogicalId><OperationType><resolver-RelativeId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to these CloudFormation resources, when `AWS::Serverless::GraphQLApi` is specified, AWS SAM may also generate the following CloudFormation resources.

`AWS::AppSync::ApiCache`  
*`LogicalId`: *`{{<graphqlapi-LogicalId>}}ApiCache`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

`AWS::AppSync::ApiKey`  
*`LogicalId`: *`{{<graphqlapi-LogicalId><apikey-RelativeId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

`AWS::AppSync::DomainName`  
*`LogicalId`: *`{{<graphqlapi-LogicalId>}}DomainName`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

`AWS::AppSync::DomainNameApiAssociation`  
*`LogicalId`: *`{{<graphqlapi-LogicalId>}}DomainNameApiAssociation`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

AWS SAM may also use the `AWS::Serverless::Connector` resource to provision permissions. For more information, see [CloudFormation resources generated when you specify AWS::Serverless::Connector](sam-specification-generated-resources-connector.md).