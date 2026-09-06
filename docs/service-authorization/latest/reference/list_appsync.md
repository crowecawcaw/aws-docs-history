

# Actions, resources, and condition keys for AWS AppSync
<a name="list_appsync"></a>

AWS AppSync (service prefix: `appsync`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/appsync/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/appsync/latest/devguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/appsync/appsync.json) for this service.

**Topics**
+ [API operations defined by AWS AppSync](#list_appsync-operations)
+ [Actions defined by AWS AppSync](#list_appsync-actions-as-permissions)
+ [Permission-only actions for AWS AppSync](#list_appsync-permission-only-actions)
+ [Resource types defined by AWS AppSync](#list_appsync-resources-for-iam-policies)
+ [Condition keys for AWS AppSync](#list_appsync-policy-keys)

## API operations defined by AWS AppSync
<a name="list_appsync-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_appsync-actions-as-permissions).




- **   AssociateApi  **
  - **IAM action:**  [appsync:AssociateApi](#list_appsync-action-AssociateApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateMergedGraphqlApi  **
  - **IAM action:**  [appsync:AssociateMergedGraphqlApi](#list_appsync-action-AssociateMergedGraphqlApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appsync:AssociateSourceGraphqlApi](#list_appsync-action-AssociateSourceGraphqlApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AssociateSourceGraphqlApi  **
  - **IAM action:**  [appsync:AssociateMergedGraphqlApi](#list_appsync-action-AssociateMergedGraphqlApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appsync:AssociateSourceGraphqlApi](#list_appsync-action-AssociateSourceGraphqlApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateApi  **
  - **IAM action:**  [appsync:CreateApi](#list_appsync-action-CreateApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appsync:TagResource](#list_appsync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appsync.amazonaws.com / **Access level:** Write

- **   CreateApiCache  **
  - **IAM action:**  [appsync:CreateApiCache](#list_appsync-action-CreateApiCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApiKey  **
  - **IAM action:**  [appsync:CreateApiKey](#list_appsync-action-CreateApiKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannelNamespace  **
  - **IAM action:**  [appsync:CreateChannelNamespace](#list_appsync-action-CreateChannelNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appsync:TagResource](#list_appsync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataSource  **
  - **IAM action:**  [appsync:CreateDataSource](#list_appsync-action-CreateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appsync.amazonaws.com / **Access level:** Write

- **   CreateDomainName  **
  - **IAM action:**  [appsync:CreateDomainName](#list_appsync-action-CreateDomainName)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appsync:TagResource](#list_appsync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFunction  **
  - **IAM action:**  [appsync:CreateFunction](#list_appsync-action-CreateFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGraphqlApi  **
  - **IAM action:**  [appsync:CreateGraphqlApi](#list_appsync-action-CreateGraphqlApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appsync:TagResource](#list_appsync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appsync.amazonaws.com / **Access level:** Write

- **   CreateResolver  **
  - **IAM action:**  [appsync:CreateResolver](#list_appsync-action-CreateResolver) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateType  **
  - **IAM action:**  [appsync:CreateType](#list_appsync-action-CreateType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApi  **
  - **IAM action:**  [appsync:DeleteApi](#list_appsync-action-DeleteApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApiCache  **
  - **IAM action:**  [appsync:DeleteApiCache](#list_appsync-action-DeleteApiCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApiKey  **
  - **IAM action:**  [appsync:DeleteApiKey](#list_appsync-action-DeleteApiKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChannelNamespace  **
  - **IAM action:**  [appsync:DeleteChannelNamespace](#list_appsync-action-DeleteChannelNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSource  **
  - **IAM action:**  [appsync:DeleteDataSource](#list_appsync-action-DeleteDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainName  **
  - **IAM action:**  [appsync:DeleteDomainName](#list_appsync-action-DeleteDomainName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFunction  **
  - **IAM action:**  [appsync:DeleteFunction](#list_appsync-action-DeleteFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGraphqlApi  **
  - **IAM action:**  [appsync:DeleteGraphqlApi](#list_appsync-action-DeleteGraphqlApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResolver  **
  - **IAM action:**  [appsync:DeleteResolver](#list_appsync-action-DeleteResolver) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteType  **
  - **IAM action:**  [appsync:DeleteType](#list_appsync-action-DeleteType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateApi  **
  - **IAM action:**  [appsync:DisassociateApi](#list_appsync-action-DisassociateApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMergedGraphqlApi  **
  - **IAM action:**  [appsync:DisassociateMergedGraphqlApi](#list_appsync-action-DisassociateMergedGraphqlApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateSourceGraphqlApi  **
  - **IAM action:**  [appsync:DisassociateSourceGraphqlApi](#list_appsync-action-DisassociateSourceGraphqlApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EvaluateCode  **
  - **IAM action:**  [appsync:EvaluateCode](#list_appsync-action-EvaluateCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   EvaluateMappingTemplate  **
  - **IAM action:**  [appsync:EvaluateMappingTemplate](#list_appsync-action-EvaluateMappingTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   FlushApiCache  **
  - **IAM action:**  [appsync:FlushApiCache](#list_appsync-action-FlushApiCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApi  **
  - **IAM action:**  [appsync:GetApi](#list_appsync-action-GetApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApiAssociation  **
  - **IAM action:**  [appsync:GetApiAssociation](#list_appsync-action-GetApiAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApiCache  **
  - **IAM action:**  [appsync:GetApiCache](#list_appsync-action-GetApiCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChannelNamespace  **
  - **IAM action:**  [appsync:GetChannelNamespace](#list_appsync-action-GetChannelNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSource  **
  - **IAM action:**  [appsync:GetDataSource](#list_appsync-action-GetDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSourceIntrospection  **
  - **IAM action:**  [appsync:GetDataSourceIntrospection](#list_appsync-action-GetDataSourceIntrospection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainName  **
  - **IAM action:**  [appsync:GetDomainName](#list_appsync-action-GetDomainName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunction  **
  - **IAM action:**  [appsync:GetFunction](#list_appsync-action-GetFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGraphqlApi  **
  - **IAM action:**  [appsync:GetGraphqlApi](#list_appsync-action-GetGraphqlApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGraphqlApiEnvironmentVariables  **
  - **IAM action:**  [appsync:GetGraphqlApiEnvironmentVariables](#list_appsync-action-GetGraphqlApiEnvironmentVariables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntrospectionSchema  **
  - **IAM action:**  [appsync:GetIntrospectionSchema](#list_appsync-action-GetIntrospectionSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResolver  **
  - **IAM action:**  [appsync:GetResolver](#list_appsync-action-GetResolver) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchemaCreationStatus  **
  - **IAM action:**  [appsync:GetSchemaCreationStatus](#list_appsync-action-GetSchemaCreationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSourceApiAssociation  **
  - **IAM action:**  [appsync:GetSourceApiAssociation](#list_appsync-action-GetSourceApiAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetType  **
  - **IAM action:**  [appsync:GetType](#list_appsync-action-GetType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApiKeys  **
  - **IAM action:**  [appsync:ListApiKeys](#list_appsync-action-ListApiKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApis  **
  - **IAM action:**  [appsync:ListApis](#list_appsync-action-ListApis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChannelNamespaces  **
  - **IAM action:**  [appsync:ListChannelNamespaces](#list_appsync-action-ListChannelNamespaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSources  **
  - **IAM action:**  [appsync:ListDataSources](#list_appsync-action-ListDataSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainNames  **
  - **IAM action:**  [appsync:ListDomainNames](#list_appsync-action-ListDomainNames) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctions  **
  - **IAM action:**  [appsync:ListFunctions](#list_appsync-action-ListFunctions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGraphqlApis  **
  - **IAM action:**  [appsync:ListGraphqlApis](#list_appsync-action-ListGraphqlApis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResolvers  **
  - **IAM action:**  [appsync:ListResolvers](#list_appsync-action-ListResolvers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResolversByFunction  **
  - **IAM action:**  [appsync:ListResolversByFunction](#list_appsync-action-ListResolversByFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSourceApiAssociations  **
  - **IAM action:**  [appsync:ListSourceApiAssociations](#list_appsync-action-ListSourceApiAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [appsync:ListTagsForResource](#list_appsync-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTypes  **
  - **IAM action:**  [appsync:ListTypes](#list_appsync-action-ListTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTypesByAssociation  **
  - **IAM action:**  [appsync:ListTypesByAssociation](#list_appsync-action-ListTypesByAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutGraphqlApiEnvironmentVariables  **
  - **IAM action:**  [appsync:PutGraphqlApiEnvironmentVariables](#list_appsync-action-PutGraphqlApiEnvironmentVariables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDataSourceIntrospection  **
  - **IAM action:**  [appsync:StartDataSourceIntrospection](#list_appsync-action-StartDataSourceIntrospection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSchemaCreation  **
  - **IAM action:**  [appsync:StartSchemaCreation](#list_appsync-action-StartSchemaCreation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSchemaMerge  **
  - **IAM action:**  [appsync:StartSchemaMerge](#list_appsync-action-StartSchemaMerge) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [appsync:TagResource](#list_appsync-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [appsync:UntagResource](#list_appsync-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApi  **
  - **IAM action:**  [appsync:UpdateApi](#list_appsync-action-UpdateApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appsync.amazonaws.com / **Access level:** Write

- **   UpdateApiCache  **
  - **IAM action:**  [appsync:UpdateApiCache](#list_appsync-action-UpdateApiCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApiKey  **
  - **IAM action:**  [appsync:UpdateApiKey](#list_appsync-action-UpdateApiKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChannelNamespace  **
  - **IAM action:**  [appsync:UpdateChannelNamespace](#list_appsync-action-UpdateChannelNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataSource  **
  - **IAM action:**  [appsync:UpdateDataSource](#list_appsync-action-UpdateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appsync.amazonaws.com / **Access level:** Write

- **   UpdateDomainName  **
  - **IAM action:**  [appsync:UpdateDomainName](#list_appsync-action-UpdateDomainName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFunction  **
  - **IAM action:**  [appsync:UpdateFunction](#list_appsync-action-UpdateFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGraphqlApi  **
  - **IAM action:**  [appsync:UpdateGraphqlApi](#list_appsync-action-UpdateGraphqlApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appsync.amazonaws.com / **Access level:** Write

- **   UpdateResolver  **
  - **IAM action:**  [appsync:UpdateResolver](#list_appsync-action-UpdateResolver) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSourceApiAssociation  **
  - **IAM action:**  [appsync:UpdateSourceApiAssociation](#list_appsync-action-UpdateSourceApiAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateType  **
  - **IAM action:**  [appsync:UpdateType](#list_appsync-action-UpdateType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS AppSync
<a name="list_appsync-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_AssociateApi.html)  **
  - **Description:** Grants permission to attach a GraphQL API to a custom domain name in AppSync
  - **Resource types (\*required):** [domain\*](#list_appsync-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateMergedGraphqlApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_AssociateMergedGraphqlApi.html)  **
  - **Description:** Grants permission to associate a merged API to a source API
  - **Resource types (\*required):** [graphqlapi\*](#list_appsync-resource-graphqlapi)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateSourceGraphqlApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_AssociateSourceGraphqlApi.html)  **
  - **Description:** Grants permission to associate a source API to a merged API
  - **Resource types (\*required):** [graphqlapi\*](#list_appsync-resource-graphqlapi)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateApi.html)  **
  - **Description:** Grants permission to create an API
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appsync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateApiCache](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateApiCache.html)  **
  - **Description:** Grants permission to create an API cache in AppSync
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateApiKey](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateApiKey.html)  **
  - **Description:** Grants permission to create a unique key that you can distribute to clients who are executing your API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateChannelNamespace](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateChannelNamespace.html)  **
  - **Description:** Grants permission to create a channel namespace
  - **Resource types (\*required):** [channelNamespace\*](#list_appsync-resource-channelNamespace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appsync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataSource](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateDataSource.html)  **
  - **Description:** Grants permission to create a data source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDomainName](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateDomainName.html)  **
  - **Description:** Grants permission to create a custom domain name in AppSync
  - **Resource types (\*required):** [domain\*](#list_appsync-resource-domain)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appsync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFunction](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateFunction.html)  **
  - **Description:** Grants permission to create a new function
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGraphqlApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateGraphqlApi.html)  **
  - **Description:** Grants permission to create a GraphQL API, which is the top level AppSync resource
  - **Resource types (\*required):** 
  - **Condition keys:** [appsync:Visibility](#list_appsync-appsync_Visibility)<br />[aws:RequestTag/${TagKey}](#list_appsync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResolver](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateResolver.html)  **
  - **Description:** Grants permission to create a resolver. A resolver converts incoming requests into a format that a data source can understand, and converts the data source's responses into GraphQL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateType](https://docs.aws.amazon.com/appsync/latest/APIReference/API_CreateType.html)  **
  - **Description:** Grants permission to create a type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteApi.html)  **
  - **Description:** Grants permission to delete a API. This will also clean up every AppSync resource below that API
  - **Resource types (\*required):** [api\*](#list_appsync-resource-api)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApiCache](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteApiCache.html)  **
  - **Description:** Grants permission to delete an API cache in AppSync
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApiKey](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteApiKey.html)  **
  - **Description:** Grants permission to delete an API key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteChannelNamespace](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteChannelNamespace.html)  **
  - **Description:** Grants permission to delete a channel namespace
  - **Resource types (\*required):** [channelNamespace\*](#list_appsync-resource-channelNamespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataSource](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteDataSource.html)  **
  - **Description:** Grants permission to delete a data source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDomainName](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteDomainName.html)  **
  - **Description:** Grants permission to delete a custom domain name in AppSync
  - **Resource types (\*required):** [domain\*](#list_appsync-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFunction](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteFunction.html)  **
  - **Description:** Grants permission to delete a function
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGraphqlApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteGraphqlApi.html)  **
  - **Description:** Grants permission to delete a GraphQL Api. This will also clean up every AppSync resource below that API
  - **Resource types (\*required):** [graphqlapi\*](#list_appsync-resource-graphqlapi)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResolver](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteResolver.html)  **
  - **Description:** Grants permission to delete a resolver
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteType](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DeleteType.html)  **
  - **Description:** Grants permission to delete a type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DisassociateApi.html)  **
  - **Description:** Grants permission to detach a GraphQL API to a custom domain name in AppSync
  - **Resource types (\*required):** [domain\*](#list_appsync-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateMergedGraphqlApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DisassociateMergedGraphqlApi.html)  **
  - **Description:** Grants permission to remove an associated source API from a merged API identified by the source API
  - **Resource types (\*required):** [mergedApiAssociation\*](#list_appsync-resource-mergedApiAssociation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateSourceGraphqlApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_DisassociateSourceGraphqlApi.html)  **
  - **Description:** Grants permission to remove an associated source API from a merged API identified by the merged API
  - **Resource types (\*required):** [sourceApiAssociation\*](#list_appsync-resource-sourceApiAssociation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [EvaluateCode](https://docs.aws.amazon.com/appsync/latest/APIReference/API_EvaluateCode.html)  **
  - **Description:** Grants permission to evaluate code with a runtime and context
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [EvaluateMappingTemplate](https://docs.aws.amazon.com/appsync/latest/APIReference/API_EvaluateMappingTemplate.html)  **
  - **Description:** Grants permission to evaluate template mapping
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [EventConnect](https://docs.aws.amazon.com/appsync/latest/devguide/using-your-event-api.html)  **
  - **Description:** Grants permission to connect to an Event API
  - **Resource types (\*required):** [api\*](#list_appsync-resource-api)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EventPublish](https://docs.aws.amazon.com/appsync/latest/devguide/using-your-event-api.html)  **
  - **Description:** Grants permission to publish events to a channel namespace
  - **Resource types (\*required):** [channelNamespace\*](#list_appsync-resource-channelNamespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EventSubscribe](https://docs.aws.amazon.com/appsync/latest/devguide/using-your-event-api.html)  **
  - **Description:** Grants permission to subscribe to a channel namespace
  - **Resource types (\*required):** [channelNamespace\*](#list_appsync-resource-channelNamespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [FlushApiCache](https://docs.aws.amazon.com/appsync/latest/APIReference/API_FlushApiCache.html)  **
  - **Description:** Grants permission to flush an API cache in AppSync
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetApi.html)  **
  - **Description:** Grants permission to retrieve an API
  - **Resource types (\*required):** [api\*](#list_appsync-resource-api)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApiAssociation](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetApiAssociation.html)  **
  - **Description:** Grants permission to read custom domain name - GraphQL API association details in AppSync
  - **Resource types (\*required):** [domain\*](#list_appsync-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApiCache](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetApiCache.html)  **
  - **Description:** Grants permission to read information about an API cache in AppSync
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetChannelNamespace](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetChannelNamespace.html)  **
  - **Description:** Grants permission to retrieve a channel namespace
  - **Resource types (\*required):** [channelNamespace\*](#list_appsync-resource-channelNamespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataSource](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetDataSource.html)  **
  - **Description:** Grants permission to retrieve a data source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataSourceIntrospection](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetDataSourceIntrospection.html)  **
  - **Description:** Grants permission to retrieve a data source introspection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDomainName](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetDomainName.html)  **
  - **Description:** Grants permission to read information about a custom domain name in AppSync
  - **Resource types (\*required):** [domain\*](#list_appsync-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunction](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetFunction.html)  **
  - **Description:** Grants permission to retrieve a function
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGraphqlApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetGraphqlApi.html)  **
  - **Description:** Grants permission to retrieve a GraphQL API
  - **Resource types (\*required):** [graphqlapi\*](#list_appsync-resource-graphqlapi)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGraphqlApiEnvironmentVariables](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetGraphqlApiEnvironmentVariables.html)  **
  - **Description:** Grants permission to retrieve the environment variables for a GraphQL API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIntrospectionSchema](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetIntrospectionSchema.html)  **
  - **Description:** Grants permission to retrieve the introspection schema for a GraphQL API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResolver](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetResolver.html)  **
  - **Description:** Grants permission to retrieve a resolver
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSchemaCreationStatus](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetSchemaCreationStatus.html)  **
  - **Description:** Grants permission to retrieve the current status of a schema creation operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSourceApiAssociation](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetSourceApiAssociation.html)  **
  - **Description:** Grants permission to read information about a merged API associated source API
  - **Resource types (\*required):** [sourceApiAssociation\*](#list_appsync-resource-sourceApiAssociation)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetType](https://docs.aws.amazon.com/appsync/latest/APIReference/API_GetType.html)  **
  - **Description:** Grants permission to retrieve a type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListApiKeys](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListApiKeys.html)  **
  - **Description:** Grants permission to list the API keys for a given API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApis](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListApis.html)  **
  - **Description:** Grants permission to list APIs
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListChannelNamespaces](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListChannelNamespaces.html)  **
  - **Description:** Grants permission to list channel namespace
  - **Resource types (\*required):** [api\*](#list_appsync-resource-api)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSources](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListDataSources.html)  **
  - **Description:** Grants permission to list the data sources for a given API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomainNames](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListDomainNames.html)  **
  - **Description:** Grants permission to enumerate custom domain names in AppSync
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFunctions](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListFunctions.html)  **
  - **Description:** Grants permission to list the functions for a given API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGraphqlApis](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListGraphqlApis.html)  **
  - **Description:** Grants permission to list GraphQL APIs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResolvers](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListResolvers.html)  **
  - **Description:** Grants permission to list the resolvers for a given API and type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResolversByFunction](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListResolversByFunction.html)  **
  - **Description:** Grants permission to list the resolvers that are associated with a specific function
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSourceApiAssociations](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListSourceApiAssociations.html)  **
  - **Description:** Grants permission to list source APIs associated to a given merged API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [api](#list_appsync-resource-api) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [channelNamespace](#list_appsync-resource-channelNamespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domain](#list_appsync-resource-domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [graphqlapi](#list_appsync-resource-graphqlapi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTypes](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListTypes.html)  **
  - **Description:** Grants permission to list the types for a given API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTypesByAssociation](https://docs.aws.amazon.com/appsync/latest/APIReference/API_ListTypesByAssociation.html)  **
  - **Description:** Grants permission to list the types for a given merged API and source API association
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutGraphqlApiEnvironmentVariables](https://docs.aws.amazon.com/appsync/latest/APIReference/API_PutGraphqlApiEnvironmentVariables.html)  **
  - **Description:** Grants permission to update the environment variables for a GraphQL API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  **
  - **Description:** Grants permission to set a web ACL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [StartDataSourceIntrospection](https://docs.aws.amazon.com/appsync/latest/APIReference/API_StartDataSourceIntrospection.html)  **
  - **Description:** Grants permission to introspect a data source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartSchemaCreation](https://docs.aws.amazon.com/appsync/latest/APIReference/API_StartSchemaCreation.html)  **
  - **Description:** Grants permission to add a new schema to your GraphQL API. This operation is asynchronous - GetSchemaCreationStatus can show when it has completed
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartSchemaMerge](https://docs.aws.amazon.com/appsync/latest/APIReference/API_StartSchemaMerge.html)  **
  - **Description:** Grants permission to initiate a schema merge for a given merged API and associated source API
  - **Resource types (\*required):** [sourceApiAssociation\*](#list_appsync-resource-sourceApiAssociation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/appsync/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [api](#list_appsync-resource-api) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appsync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Resource types (\*required):** [channelNamespace](#list_appsync-resource-channelNamespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appsync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Resource types (\*required):** [domain](#list_appsync-resource-domain) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appsync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Resource types (\*required):** [graphqlapi](#list_appsync-resource-graphqlapi) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appsync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [api](#list_appsync-resource-api) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Resource types (\*required):** [channelNamespace](#list_appsync-resource-channelNamespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Resource types (\*required):** [domain](#list_appsync-resource-domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Resource types (\*required):** [graphqlapi](#list_appsync-resource-graphqlapi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appsync-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateApi.html)  **
  - **Description:** Grants permission to update an API
  - **Resource types (\*required):** [api\*](#list_appsync-resource-api)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApiCache](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateApiCache.html)  **
  - **Description:** Grants permission to update an API cache in AppSync
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApiKey](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateApiKey.html)  **
  - **Description:** Grants permission to update an API key for a given API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateChannelNamespace](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateChannelNamespace.html)  **
  - **Description:** Grants permission to update a channel namespace
  - **Resource types (\*required):** [channelNamespace\*](#list_appsync-resource-channelNamespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataSource](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateDataSource.html)  **
  - **Description:** Grants permission to update a data source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDomainName](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateDomainName.html)  **
  - **Description:** Grants permission to update a custom domain name in AppSync
  - **Resource types (\*required):** [domain\*](#list_appsync-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFunction](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateFunction.html)  **
  - **Description:** Grants permission to update an existing function
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGraphqlApi](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateGraphqlApi.html)  **
  - **Description:** Grants permission to update a GraphQL API
  - **Resource types (\*required):** [graphqlapi\*](#list_appsync-resource-graphqlapi)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResolver](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateResolver.html)  **
  - **Description:** Grants permission to update a resolver
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSourceApiAssociation](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateSourceApiAssociation.html)  **
  - **Description:** Grants permission to update a merged API source API association
  - **Resource types (\*required):** [sourceApiAssociation\*](#list_appsync-resource-sourceApiAssociation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateType](https://docs.aws.amazon.com/appsync/latest/APIReference/API_UpdateType.html)  **
  - **Description:** Grants permission to update a type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS AppSync
<a name="list_appsync-permission-only-actions"></a>

The following actions are defined by AWS AppSync but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  **
  - **Description:** Grants permission to associate a web ACL and a resource
  - **Resource types (\*required):** [api](#list_appsync-resource-api) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [graphqlapi](#list_appsync-resource-graphqlapi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/appsync/latest/devguide/merge-api.html)  **
  - **Description:** Grants permission to remove a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  **
  - **Description:** Grants permission to disassociate a web ACL and a resource
  - **Resource types (\*required):** [api](#list_appsync-resource-api) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [graphqlapi](#list_appsync-resource-graphqlapi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetResourcePolicy](https://docs.aws.amazon.com/appsync/latest/devguide/merge-api.html)  **
  - **Description:** Grants permission to read a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWebACLForResource](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  **
  - **Description:** Grants permission to get associated web ACLs for a resource
  - **Resource types (\*required):** [api](#list_appsync-resource-api) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [graphqlapi](#list_appsync-resource-graphqlapi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GraphQL](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#aws-iam-authorization)  **
  - **Description:** Grants permission to send a GraphQL query to a GraphQL API
  - **Resource types (\*required):** [field\*](#list_appsync-resource-field) / **Condition keys:**  
  - **Resource types (\*required):** [graphqlapi\*](#list_appsync-resource-graphqlapi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListResourcesForWebACL](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html)  **
  - **Description:** Grants permission to get associated resources for a web ACL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/appsync/latest/devguide/merge-api.html)  **
  - **Description:** Grants permission to set a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SourceGraphQL](https://docs.aws.amazon.com/appsync/latest/devguide/using-your-api.html)  **
  - **Description:** Grants permission to send a GraphQL query to a source API of a merged API
  - **Resource types (\*required):** [field\*](#list_appsync-resource-field) / **Condition keys:**  
  - **Resource types (\*required):** [graphqlapi\*](#list_appsync-resource-graphqlapi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS AppSync
<a name="list_appsync-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [api](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-welcome.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${ApiId} | [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_) | 
|  [channelNamespace](https://docs.aws.amazon.com/appsync/latest/eventapi/channel-namespaces.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${ApiId}/channelNamespace/${ChannelNamespaceName} | [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_) | 
|  [datasource](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${GraphQLAPIId}/datasources/${DatasourceName} |   | 
|  [domain](https://docs.aws.amazon.com/appsync/latest/devguide/custom-domain-name.html)  | arn:${Partition}:appsync:${Region}:${Account}:domainnames/${DomainName} | [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_) | 
|  [field](https://docs.aws.amazon.com/appsync/latest/devguide/configuring-resolvers.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${GraphQLAPIId}/types/${TypeName}/fields/${FieldName} |   | 
|  [function](https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${GraphQLAPIId}/functions/${FunctionId} |   | 
|  [graphqlapi](https://docs.aws.amazon.com/appsync/latest/devguide/designing-a-graphql-api.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${GraphQLAPIId} | [aws:ResourceTag/${TagKey}](#list_appsync-aws_ResourceTag___TagKey_) | 
|  [mergedApiAssociation](https://docs.aws.amazon.com/appsync/latest/devguide/merged-api.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${SourceGraphQLAPIId}/mergedApiAssociations/${Associationid} |   | 
|  [sourceApiAssociation](https://docs.aws.amazon.com/appsync/latest/devguide/merged-api.html)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${MergedGraphQLAPIId}/sourceApiAssociations/${Associationid} |   | 
|  [type](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html#adding-a-root-query-type)  | arn:${Partition}:appsync:${Region}:${Account}:apis/${GraphQLAPIId}/types/${TypeName} |   | 

## Condition keys for AWS AppSync
<a name="list_appsync-policy-keys"></a>

AWS AppSync defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [appsync:Visibility](iam-policy-structure.html#amazon-appsync-keys)  | Filters access by the visibility of an API | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 