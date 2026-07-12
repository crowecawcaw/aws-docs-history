# Actions, resources, and condition keys for Amazon SimpleDB

Amazon SimpleDB (service prefix: `sdb`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../AmazonSimpleDB/latest/DeveloperGuide.md "../../../AmazonSimpleDB/latest/DeveloperGuide.md").
- View a list of the [API operations available for
  this service](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.md "../../../AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/sdb/sdb.json "https://servicereference.us-east-1.amazonaws.com/v1/sdb/sdb.json") for this service.

###### Topics

- [API operations defined by Amazon SimpleDB](#list_simpledb-operations "#list_simpledb-operations")
- [Actions defined by Amazon SimpleDB](#list_simpledb-actions-as-permissions "#list_simpledb-actions-as-permissions")
- [Resource types defined by Amazon SimpleDB](#list_simpledb-resources-for-iam-policies "#list_simpledb-resources-for-iam-policies")
- [Condition keys for Amazon SimpleDB](#list_simpledb-policy-keys "#list_simpledb-policy-keys")

## API operations defined by Amazon SimpleDB

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_simpledb-actions-as-permissions "#list_simpledb-actions-as-permissions").

| Operation         | SDK client | IAM action                                                                                                 | Condition key | Possible value(s) | Access level |
| ----------------- | ---------- | ---------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| GetExport         | simpledbv2 | [sdb:GetExport](#list_simpledb-action-GetExport "#list_simpledb-action-GetExport")                         |               |                   | Read         |
| ListExports       | simpledbv2 | [sdb:ListExports](#list_simpledb-action-ListExports "#list_simpledb-action-ListExports")                   |               |                   | List         |
| StartDomainExport | simpledbv2 | [sdb:StartDomainExport](#list_simpledb-action-StartDomainExport "#list_simpledb-action-StartDomainExport") |               |                   | Write        |

## Actions defined by Amazon SimpleDB

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                  | Description                                                                                                                                                                     | Resource types (\*required)                                                 | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------- | ------------ |
| [BatchDeleteAttributes](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_BatchDeleteAttributes.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_BatchDeleteAttributes.md") | Grants permission to perform multiple DeleteAttributes operations in a single call, which reduces round trips and latencies                                                     | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Write        |
| [BatchPutAttributes](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_BatchPutAttributes.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_BatchPutAttributes.md")          | Grants permission to perform multiple PutAttribute operations in a single call, which reduces round trips and latencies                                                         | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Write        |
| [CreateDomain](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_CreateDomain.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_CreateDomain.md")                            | Grants permission to create a new domain                                                                                                                                        | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Write        |
| [DeleteAttributes](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DeleteAttributes.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DeleteAttributes.md")                | Grants permission to delete one or more attributes associated with the item                                                                                                     | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Write        |
| [DeleteDomain](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DeleteDomain.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DeleteDomain.md")                            | Grants permission to delete a domain                                                                                                                                            | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Write        |
| [DomainMetadata](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DomainMetadata.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DomainMetadata.md")                      | Grants permission to return information about the domain, including when the domain was created, the number of items and attributes, and the size of attribute names and values | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Read         |
| [GetAttributes](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetAttributes.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetAttributes.md")                         | Grants permission to return all of the attributes associated with the item                                                                                                      | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Read         |
| [GetExport](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetExport.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetExport.md")                                     | Grants permission to return information for an existing domain export arn                                                                                                       | [export\*](#list_simpledb-resource-export "#list_simpledb-resource-export") |                | Read         |
| [ListDomains](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListDomains.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListDomains.md")                               | Grants permission to list all domains                                                                                                                                           |                                                                             |                | List         |
| [ListExports](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListExports.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListExports.md")                               | Grants permission to list all exports that were created. The results are paginated and can be filtered by domain name                                                           | [domain](#list_simpledb-resource-domain "#list_simpledb-resource-domain")   |                | List         |
| [PutAttributes](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_PutAttributes.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_PutAttributes.md")                         | Grants permission to create or replace attributes in an item                                                                                                                    | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Write        |
| [Select](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_Select.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_Select.md")                                              | Grants permission to execute a query against the items in a domain                                                                                                              | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Read         |
| [StartDomainExport](../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_StartDomainExport.md "../../../AmazonSimpleDB/latest/DeveloperGuide/SDB_API_StartDomainExport.md")             | Grants permission to initiates the export of a SimpleDB domain to an S3 bucket                                                                                                  | [domain\*](#list_simpledb-resource-domain "#list_simpledb-resource-domain") |                | Write        |

## Resource types defined by Amazon SimpleDB

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                    | ARN                                                                                 | Condition keys |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------- |
| [domain](../../../AmazonSimpleDB/latest/DeveloperGuide/DataModel.md "../../../AmazonSimpleDB/latest/DeveloperGuide/DataModel.md") | arn:${Partition}:sdb:${Region}:${Account}:domain/${DomainName}                      |                |
| [export](../../../AmazonSimpleDB/latest/DeveloperGuide/DataModel.md "../../../AmazonSimpleDB/latest/DeveloperGuide/DataModel.md") | arn:${Partition}:sdb:${Region}:${Account}:domain/${DomainName}/export/${ExportUUID} |                |

## Condition keys for Amazon SimpleDB

Amazon SimpleDB has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
