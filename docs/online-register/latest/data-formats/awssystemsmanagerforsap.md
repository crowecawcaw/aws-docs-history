

# Data retrieval APIs for AWS Systems Manager for SAP
<a name="awssystemsmanagerforsap"></a>

AWS Systems Manager for SAP provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="ssm-sap-GetApplication"></a>[GetApplication](https://docs.aws.amazon.com/systems-manager/index.html) | Access information about an application registered with SSM for SAP by providing the application ID or application ARN | Read | 
| <a name="ssm-sap-GetComponent"></a>[GetComponent](https://docs.aws.amazon.com/systems-manager/index.html) | Access information about a component registered with SSM for SAP by providing the application ID and component ID | Read | 
| <a name="ssm-sap-GetConfigurationCheckOperation"></a>[GetConfigurationCheckOperation](https://docs.aws.amazon.com/systems-manager/index.html) | Get the details of a configuration check operation by specifying the operation ID | Read | 
| <a name="ssm-sap-GetDatabase"></a>[GetDatabase](https://docs.aws.amazon.com/systems-manager/index.html) | Access information about a database registered with SSM for SAP by providing the application ID, component ID, and database ID | Read | 
| <a name="ssm-sap-GetOperation"></a>[GetOperation](https://docs.aws.amazon.com/systems-manager/index.html) | Access information about an operation by providing its operation ID | Read | 
| <a name="ssm-sap-ListApplications"></a>[ListApplications](https://docs.aws.amazon.com/systems-manager/index.html) | Retrieve a list of all applications registered with SSM for SAP under the customer AWS account | List | 
| <a name="ssm-sap-ListComponents"></a>[ListComponents](https://docs.aws.amazon.com/systems-manager/index.html) | Retrieve a list of all components in the account of customer, or a specific application | List | 
| <a name="ssm-sap-ListConfigurationCheckDefinitions"></a>[ListConfigurationCheckDefinitions](https://docs.aws.amazon.com/systems-manager/index.html) | List all configuration check types supported by AWS Systems Manager for SAP | List | 
| <a name="ssm-sap-ListConfigurationCheckOperations"></a>[ListConfigurationCheckOperations](https://docs.aws.amazon.com/systems-manager/index.html) | List past configuration check operations | List | 
| <a name="ssm-sap-ListDatabases"></a>[ListDatabases](https://docs.aws.amazon.com/systems-manager/index.html) | Retrieve a list of all databases in the account of customer, or a specific application | List | 
| <a name="ssm-sap-ListOperationEvents"></a>[ListOperationEvents](https://docs.aws.amazon.com/systems-manager/index.html) | Retrieve a list of all operation events in a specified operation | List | 
| <a name="ssm-sap-ListOperations"></a>[ListOperations](https://docs.aws.amazon.com/systems-manager/index.html) | Retrieve a list of all operations in the account of customer, additional filters can be applied | List | 
| <a name="ssm-sap-ListSubCheckResults"></a>[ListSubCheckResults](https://docs.aws.amazon.com/systems-manager/index.html) | List the sub-check results of a specified configuration check operation | List | 
| <a name="ssm-sap-ListSubCheckRuleResults"></a>[ListSubCheckRuleResults](https://docs.aws.amazon.com/systems-manager/index.html) | List the rules of a specified sub-check belonging to a configuration check operation | List | 
| <a name="ssm-sap-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/systems-manager/index.html) | List the tags on a specified resource ARN | Read | 