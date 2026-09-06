

# Actions, resources, and condition keys for AWS Systems Manager for SAP
<a name="list_ssm-sap"></a>

AWS Systems Manager for SAP (service prefix: `ssm-sap`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/systems-manager/index.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/systems-manager/index.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/systems-manager/index.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ssm-sap/ssm-sap.json) for this service.

**Topics**
+ [API operations defined by AWS Systems Manager for SAP](#list_ssm-sap-operations)
+ [Actions defined by AWS Systems Manager for SAP](#list_ssm-sap-actions-as-permissions)
+ [Resource types defined by AWS Systems Manager for SAP](#list_ssm-sap-resources-for-iam-policies)
+ [Condition keys for AWS Systems Manager for SAP](#list_ssm-sap-policy-keys)

## API operations defined by AWS Systems Manager for SAP
<a name="list_ssm-sap-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ssm-sap-actions-as-permissions).




- **   DeleteResourcePermission  **
  - **IAM action:**  [ssm-sap:DeleteResourcePermission](#list_ssm-sap-action-DeleteResourcePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeregisterApplication  **
  - **IAM action:**  [ssm-sap:DeregisterApplication](#list_ssm-sap-action-DeregisterApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [ssm-sap:GetApplication](#list_ssm-sap-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComponent  **
  - **IAM action:**  [ssm-sap:GetComponent](#list_ssm-sap-action-GetComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationCheckOperation  **
  - **IAM action:**  [ssm-sap:GetConfigurationCheckOperation](#list_ssm-sap-action-GetConfigurationCheckOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDatabase  **
  - **IAM action:**  [ssm-sap:GetDatabase](#list_ssm-sap-action-GetDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOperation  **
  - **IAM action:**  [ssm-sap:GetOperation](#list_ssm-sap-action-GetOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePermission  **
  - **IAM action:**  [ssm-sap:GetResourcePermission](#list_ssm-sap-action-GetResourcePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ListApplications  **
  - **IAM action:**  [ssm-sap:ListApplications](#list_ssm-sap-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComponents  **
  - **IAM action:**  [ssm-sap:ListComponents](#list_ssm-sap-action-ListComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationCheckDefinitions  **
  - **IAM action:**  [ssm-sap:ListConfigurationCheckDefinitions](#list_ssm-sap-action-ListConfigurationCheckDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationCheckOperations  **
  - **IAM action:**  [ssm-sap:ListConfigurationCheckOperations](#list_ssm-sap-action-ListConfigurationCheckOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatabases  **
  - **IAM action:**  [ssm-sap:ListDatabases](#list_ssm-sap-action-ListDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOperationEvents  **
  - **IAM action:**  [ssm-sap:ListOperationEvents](#list_ssm-sap-action-ListOperationEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOperations  **
  - **IAM action:**  [ssm-sap:ListOperations](#list_ssm-sap-action-ListOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubCheckResults  **
  - **IAM action:**  [ssm-sap:ListSubCheckResults](#list_ssm-sap-action-ListSubCheckResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubCheckRuleResults  **
  - **IAM action:**  [ssm-sap:ListSubCheckRuleResults](#list_ssm-sap-action-ListSubCheckRuleResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ssm-sap:ListTagsForResource](#list_ssm-sap-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePermission  **
  - **IAM action:**  [ssm-sap:PutResourcePermission](#list_ssm-sap-action-PutResourcePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RegisterApplication  **
  - **IAM action:**  [ssm-sap:RegisterApplication](#list_ssm-sap-action-RegisterApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ssm-sap:TagResource](#list_ssm-sap-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartApplication  **
  - **IAM action:**  [ssm-sap:StartApplication](#list_ssm-sap-action-StartApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartApplicationRefresh  **
  - **IAM action:**  [ssm-sap:StartApplicationRefresh](#list_ssm-sap-action-StartApplicationRefresh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartConfigurationChecks  **
  - **IAM action:**  [ssm-sap:StartConfigurationChecks](#list_ssm-sap-action-StartConfigurationChecks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopApplication  **
  - **IAM action:**  [ssm-sap:StopApplication](#list_ssm-sap-action-StopApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ssm-sap:TagResource](#list_ssm-sap-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ssm-sap:UntagResource](#list_ssm-sap-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplicationSettings  **
  - **IAM action:**  [ssm-sap:UpdateApplicationSettings](#list_ssm-sap-action-UpdateApplicationSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Systems Manager for SAP
<a name="list_ssm-sap-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BackupDatabase](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to perform backup operation on a specified database
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePermission](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to delete the SSM for SAP level resource permissions associated with a SSM for SAP database resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeregisterApplication](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to deregister an SAP application with SSM for SAP
  - **Resource types (\*required):** [application](#list_ssm-sap-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to access information about an application registered with SSM for SAP by providing the application ID or application ARN
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetComponent](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to access information about a component registered with SSM for SAP by providing the application ID and component ID
  - **Resource types (\*required):** [component](#list_ssm-sap-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfigurationCheckOperation](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to get the details of a configuration check operation by specifying the operation ID
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDatabase](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to access information about a database registered with SSM for SAP by providing the application ID, component ID, and database ID
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOperation](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to access information about an operation by providing its operation ID
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePermission](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to get the SSM for SAP level resource permissions associated with a SSM for SAP database resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ListApplications](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to retrieve a list of all applications registered with SSM for SAP under the customer AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComponents](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to retrieve a list of all components in the account of customer, or a specific application
  - **Resource types (\*required):** [application](#list_ssm-sap-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConfigurationCheckDefinitions](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to list all configuration check types supported by AWS Systems Manager for SAP
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurationCheckOperations](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to list past configuration check operations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatabases](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to retrieve a list of all databases in the account of customer, or a specific application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOperationEvents](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to retrieve a list of all operation events in a specified operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOperations](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to retrieve a list of all operations in the account of customer, additional filters can be applied
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubCheckResults](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to list the sub-check results of a specified configuration check operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubCheckRuleResults](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to list the rules of a specified sub-check belonging to a configuration check operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to list the tags on a specified resource ARN
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutResourcePermission](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to add the SSM for SAP level resource permissions associated with a SSM for SAP database resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RegisterApplication](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to registers an SAP application with SSM for SAP
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-sap-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-sap-aws_TagKeys)
  - **Access level:** Write

- **   [RestoreDatabase](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to restore a database from another database
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartApplication](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to start a registered SSM for SAP application
  - **Resource types (\*required):** [application](#list_ssm-sap-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartApplicationRefresh](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to start an on-demand discovery of a registered SSM for SAP application
  - **Resource types (\*required):** [application](#list_ssm-sap-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartConfigurationChecks](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to iniitiate configuration check operations against a specified application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopApplication](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to stop a registered SSM for SAP application
  - **Resource types (\*required):** [application](#list_ssm-sap-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to tag a specified resource ARN
  - **Resource types (\*required):** [application](#list_ssm-sap-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-sap-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-sap-aws_TagKeys)
  - **Resource types (\*required):** [component](#list_ssm-sap-resource-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-sap-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-sap-aws_TagKeys)
  - **Resource types (\*required):** [database](#list_ssm-sap-resource-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-sap-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-sap-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to remove tags from a specified resource ARN
  - **Resource types (\*required):** [application](#list_ssm-sap-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-sap-aws_TagKeys)
  - **Resource types (\*required):** [component](#list_ssm-sap-resource-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-sap-aws_TagKeys)
  - **Resource types (\*required):** [database](#list_ssm-sap-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-sap-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplicationSettings](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to update settings of a registered SSM for SAP application
  - **Resource types (\*required):** [application](#list_ssm-sap-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHANABackupSettings](https://docs.aws.amazon.com/systems-manager/index.html)  **
  - **Description:** Grants permission to update the HANA backup settings of a specified database
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Systems Manager for SAP
<a name="list_ssm-sap-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/systems-manager/index.html)  | arn:${Partition}:ssm-sap:${Region}:${Account}:${ApplicationType}/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_) | 
|  [component](https://docs.aws.amazon.com/systems-manager/index.html)  | arn:${Partition}:ssm-sap:${Region}:${Account}:${ApplicationType}/${ApplicationId}/COMPONENT/${ComponentId} | [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_) | 
|  [database](https://docs.aws.amazon.com/systems-manager/index.html)  | arn:${Partition}:ssm-sap:${Region}:${Account}:${ApplicationType}/${ApplicationId}/DB/${DatabaseId} | [aws:ResourceTag/${TagKey}](#list_ssm-sap-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Systems Manager for SAP
<a name="list_ssm-sap-policy-keys"></a>

AWS Systems Manager for SAP defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/systems-manager/index.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/systems-manager/index.html)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/systems-manager/index.html)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 