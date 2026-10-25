

# Actions, resources, and condition keys for AWS Continuum
<a name="list_continuum"></a>

AWS Continuum (service prefix: `continuum`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/continuum/latest/userguide/what-is-continuum.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/continuum/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/continuum/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/continuum/continuum.json) for this service.

**Topics**
+ [Actions defined by AWS Continuum](#list_continuum-actions-as-permissions)
+ [Resource types defined by AWS Continuum](#list_continuum-resources-for-iam-policies)
+ [Condition keys for AWS Continuum](#list_continuum-policy-keys)

## Actions defined by AWS Continuum
<a name="list_continuum-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateCollector](https://docs.aws.amazon.com/continuum/latest/APIReference/API_AssociateCollector.html)  **
  - **Description:** Grants permission to associate a collector with an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:** [continuum:CollectorArn](#list_continuum-continuum_CollectorArn)
  - **Access level:** Write

- **   [CreateCodeFinding](https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateCodeFinding.html)  **
  - **Description:** Grants permission to create a code finding in an environment
  - **Resource types (\*required):** [code-findings\*](#list_continuum-resource-code-findings) / **Condition keys:**  
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateCodeScan](https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateCodeScan.html)  **
  - **Description:** Grants permission to start a code scan of an environment
  - **Resource types (\*required):** [code-scans\*](#list_continuum-resource-code-scans) / **Condition keys:**  
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateCollector](https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateCollector.html)  **
  - **Description:** Grants permission to create a collector
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments) / **Condition keys:** [continuum:RepositoryName](#list_continuum-continuum_RepositoryName)
  - **Resource types (\*required):** [integrations](#list_continuum-resource-integrations) / **Condition keys:** [continuum:RepositoryName](#list_continuum-continuum_RepositoryName)
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateIntegration.html)  **
  - **Description:** Grants permission to create an integration with an external source provider
  - **Resource types (\*required):** [integrations\*](#list_continuum-resource-integrations)
  - **Condition keys:** [continuum:S3BucketName](#list_continuum-continuum_S3BucketName)
  - **Access level:** Write

- **   [DeleteCollector](https://docs.aws.amazon.com/continuum/latest/APIReference/API_DeleteCollector.html)  **
  - **Description:** Grants permission to delete a collector
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/continuum/latest/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/continuum/latest/APIReference/API_DeleteIntegration.html)  **
  - **Description:** Grants permission to delete an integration
  - **Resource types (\*required):** [integrations\*](#list_continuum-resource-integrations)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateCollector](https://docs.aws.amazon.com/continuum/latest/APIReference/API_DisassociateCollector.html)  **
  - **Description:** Grants permission to disassociate a collector from an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:** [continuum:CollectorArn](#list_continuum-continuum_CollectorArn)
  - **Access level:** Write

- **   [GetCodeFinding](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCodeFinding.html)  **
  - **Description:** Grants permission to get a code finding
  - **Resource types (\*required):** [code-findings\*](#list_continuum-resource-code-findings)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCodeIssue](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCodeIssue.html)  **
  - **Description:** Grants permission to get a code issue
  - **Resource types (\*required):** [code-issues\*](#list_continuum-resource-code-issues)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCodeIssueArtifact](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCodeIssueArtifact.html)  **
  - **Description:** Grants permission to get an artifact of a code issue
  - **Resource types (\*required):** [code-issues\*](#list_continuum-resource-code-issues)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCodeScan](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCodeScan.html)  **
  - **Description:** Grants permission to get a code scan
  - **Resource types (\*required):** [code-scans\*](#list_continuum-resource-code-scans)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCollector](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCollector.html)  **
  - **Description:** Grants permission to get a collector
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCollectorDataAccessAuthorization](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCollectorDataAccessAuthorization.html)  **
  - **Description:** Grants permission to access the data of a collector from an environment
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:** [continuum:EnvironmentArn](#list_continuum-continuum_EnvironmentArn)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetEnvironment.html)  **
  - **Description:** Grants permission to get an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIntegration](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetIntegration.html)  **
  - **Description:** Grants permission to get an integration
  - **Resource types (\*required):** [integrations\*](#list_continuum-resource-integrations)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get the resource policy attached to a resource
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAssociatedCollectors](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListAssociatedCollectors.html)  **
  - **Description:** Grants permission to list the collectors associated with an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssociatedEnvironments](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListAssociatedEnvironments.html)  **
  - **Description:** Grants permission to list the environments associated with a collector
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeFindings](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListCodeFindings.html)  **
  - **Description:** Grants permission to list the code findings in an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeIssueArtifacts](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListCodeIssueArtifacts.html)  **
  - **Description:** Grants permission to list the artifacts of a code issue
  - **Resource types (\*required):** [code-issues\*](#list_continuum-resource-code-issues)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeIssues](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListCodeIssues.html)  **
  - **Description:** Grants permission to list the code issues in an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeScans](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListCodeScans.html)  **
  - **Description:** Grants permission to list the code scans of an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCollectors](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListCollectors.html)  **
  - **Description:** Grants permission to list collectors
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironments](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list environments
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIntegrations](https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListIntegrations.html)  **
  - **Description:** Grants permission to list integrations
  - **Resource types (\*required):** [integrations\*](#list_continuum-resource-integrations)
  - **Condition keys:**  
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/continuum/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to a resource
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartIntegrationAuthorization](https://docs.aws.amazon.com/continuum/latest/APIReference/API_StartIntegrationAuthorization.html)  **
  - **Description:** Grants permission to start an OAuth authorization for a new integration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCollector](https://docs.aws.amazon.com/continuum/latest/APIReference/API_UpdateCollector.html)  **
  - **Description:** Grants permission to update a collector
  - **Resource types (\*required):** [collectors\*](#list_continuum-resource-collectors)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/continuum/latest/APIReference/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update an environment
  - **Resource types (\*required):** [environments\*](#list_continuum-resource-environments) / **Condition keys:** [continuum:RepositoryName](#list_continuum-continuum_RepositoryName)
  - **Resource types (\*required):** [integrations](#list_continuum-resource-integrations) / **Condition keys:** [continuum:RepositoryName](#list_continuum-continuum_RepositoryName)
  - **Access level:** Write

- **   [UpdateIntegration](https://docs.aws.amazon.com/continuum/latest/APIReference/API_UpdateIntegration.html)  **
  - **Description:** Grants permission to update the IAM role of an Amazon S3 integration
  - **Resource types (\*required):** [integrations\*](#list_continuum-resource-integrations)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Continuum
<a name="list_continuum-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [code-findings](https://docs.aws.amazon.com/continuum/latest/APIReference/code-findings.html)  | arn:${Partition}:continuum:${Region}:${Account}:environments/${EnvironmentId}/code-findings/${FindingId} |   | 
|  [code-issues](https://docs.aws.amazon.com/continuum/latest/APIReference/code-issues.html)  | arn:${Partition}:continuum:${Region}:${Account}:environments/${EnvironmentId}/code-issues/${IssueId} |   | 
|  [code-scans](https://docs.aws.amazon.com/continuum/latest/APIReference/code-scans.html)  | arn:${Partition}:continuum:${Region}:${Account}:environments/${EnvironmentId}/code-scans/${ScanRunId} |   | 
|  [collectors](https://docs.aws.amazon.com/continuum/latest/APIReference/collectors.html)  | arn:${Partition}:continuum:${Region}:${Account}:collectors/${CollectorId} |   | 
|  [environments](https://docs.aws.amazon.com/continuum/latest/APIReference/environments.html)  | arn:${Partition}:continuum:${Region}:${Account}:environments/${EnvironmentId} |   | 
|  [integrations](https://docs.aws.amazon.com/continuum/latest/APIReference/integrations.html)  | arn:${Partition}:continuum:${Region}:${Account}:integrations/${IntegrationId} |   | 

## Condition keys for AWS Continuum
<a name="list_continuum-policy-keys"></a>

AWS Continuum defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [continuum:CollectorArn](https://docs.aws.amazon.com/continuum/latest/userguide/security-iam.html#condition-keys-CollectorArn)  | Filters access by the ARNs of the collectors in an AssociateCollector or DisassociateCollector request | ArrayOfARN | 
|   [continuum:EnvironmentArn](https://docs.aws.amazon.com/continuum/latest/userguide/security-iam.html#condition-keys-EnvironmentArn)  | Filters access by the ARN of the environment that requests access to the data of a collector | ARN | 
|   [continuum:RepositoryName](https://docs.aws.amazon.com/continuum/latest/userguide/security-iam.html#condition-keys-RepositoryName)  | Filters access by the repositories, as lowercase owner/repo values, that a CreateEnvironment or UpdateEnvironment request selects as sources | ArrayOfString | 
|   [continuum:S3BucketName](https://docs.aws.amazon.com/continuum/latest/userguide/security-iam.html#condition-keys-S3BucketName)  | Filters access by the name of the Amazon S3 bucket in a CreateIntegration request | String | 