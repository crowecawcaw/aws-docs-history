

# Actions, resources, and condition keys for Amazon SimpleDB
<a name="list_simpledb"></a>

Amazon SimpleDB (service prefix: `sdb`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sdb/sdb.json) for this service.

**Topics**
+ [API operations defined by Amazon SimpleDB](#list_simpledb-operations)
+ [Actions defined by Amazon SimpleDB](#list_simpledb-actions-as-permissions)
+ [Resource types defined by Amazon SimpleDB](#list_simpledb-resources-for-iam-policies)
+ [Condition keys for Amazon SimpleDB](#list_simpledb-policy-keys)

## API operations defined by Amazon SimpleDB
<a name="list_simpledb-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_simpledb-actions-as-permissions).




- **   GetExport  **
  - **SDK client:** simpledbv2
  - **IAM action:**  [sdb:GetExport](#list_simpledb-action-GetExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListExports  **
  - **SDK client:** simpledbv2
  - **IAM action:**  [sdb:ListExports](#list_simpledb-action-ListExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartDomainExport  **
  - **SDK client:** simpledbv2
  - **IAM action:**  [sdb:StartDomainExport](#list_simpledb-action-StartDomainExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon SimpleDB
<a name="list_simpledb-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchDeleteAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_BatchDeleteAttributes.html)  **
  - **Description:** Grants permission to perform multiple DeleteAttributes operations in a single call, which reduces round trips and latencies
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchPutAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_BatchPutAttributes.html)  **
  - **Description:** Grants permission to perform multiple PutAttribute operations in a single call, which reduces round trips and latencies
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_CreateDomain.html)  **
  - **Description:** Grants permission to create a new domain
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DeleteAttributes.html)  **
  - **Description:** Grants permission to delete one or more attributes associated with the item
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete a domain
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DomainMetadata](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DomainMetadata.html)  **
  - **Description:** Grants permission to return information about the domain, including when the domain was created, the number of items and attributes, and the size of attribute names and values
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetAttributes.html)  **
  - **Description:** Grants permission to return all of the attributes associated with the item
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetExport](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetExport.html)  **
  - **Description:** Grants permission to return information for an existing domain export arn
  - **Resource types (\*required):** [export\*](#list_simpledb-resource-export)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDomains](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListDomains.html)  **
  - **Description:** Grants permission to list all domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExports](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListExports.html)  **
  - **Description:** Grants permission to list all exports that were created. The results are paginated and can be filtered by domain name
  - **Resource types (\*required):** [domain](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** List

- **   [PutAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_PutAttributes.html)  **
  - **Description:** Grants permission to create or replace attributes in an item
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [Select](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_Select.html)  **
  - **Description:** Grants permission to execute a query against the items in a domain
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartDomainExport](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_StartDomainExport.html)  **
  - **Description:** Grants permission to initiates the export of a SimpleDB domain to an S3 bucket
  - **Resource types (\*required):** [domain\*](#list_simpledb-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon SimpleDB
<a name="list_simpledb-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [domain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/DataModel.html)  | arn:${Partition}:sdb:${Region}:${Account}:domain/${DomainName} |   | 
|  [export](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/DataModel.html)  | arn:${Partition}:sdb:${Region}:${Account}:domain/${DomainName}/export/${ExportUUID} |   | 

## Condition keys for Amazon SimpleDB
<a name="list_simpledb-policy-keys"></a>

Amazon SimpleDB has no service-specific condition keys that can be used in the `Condition` element of policy statements.