

# Actions, resources, and condition keys for AWS Serverless Application Repository
<a name="list_serverlessrepo"></a>

AWS Serverless Application Repository (service prefix: `serverlessrepo`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/what-is-serverlessrepo.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/resources.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/serverlessrepo/serverlessrepo.json) for this service.

**Topics**
+ [API operations defined by AWS Serverless Application Repository](#list_serverlessrepo-operations)
+ [Actions defined by AWS Serverless Application Repository](#list_serverlessrepo-actions-as-permissions)
+ [Resource types defined by AWS Serverless Application Repository](#list_serverlessrepo-resources-for-iam-policies)
+ [Condition keys for AWS Serverless Application Repository](#list_serverlessrepo-policy-keys)

## API operations defined by AWS Serverless Application Repository
<a name="list_serverlessrepo-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_serverlessrepo-actions-as-permissions).




- **   CreateApplication  **
  - **IAM action:**  [serverlessrepo:CreateApplication](#list_serverlessrepo-action-CreateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplicationVersion  **
  - **IAM action:**  [serverlessrepo:CreateApplicationVersion](#list_serverlessrepo-action-CreateApplicationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCloudFormationChangeSet  **
  - **IAM action:**  [serverlessrepo:CreateCloudFormationChangeSet](#list_serverlessrepo-action-CreateCloudFormationChangeSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCloudFormationTemplate  **
  - **IAM action:**  [serverlessrepo:CreateCloudFormationTemplate](#list_serverlessrepo-action-CreateCloudFormationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [serverlessrepo:DeleteApplication](#list_serverlessrepo-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [serverlessrepo:GetApplication](#list_serverlessrepo-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplicationPolicy  **
  - **IAM action:**  [serverlessrepo:GetApplicationPolicy](#list_serverlessrepo-action-GetApplicationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudFormationTemplate  **
  - **IAM action:**  [serverlessrepo:GetCloudFormationTemplate](#list_serverlessrepo-action-GetCloudFormationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplicationDependencies  **
  - **IAM action:**  [serverlessrepo:ListApplicationDependencies](#list_serverlessrepo-action-ListApplicationDependencies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplicationVersions  **
  - **IAM action:**  [serverlessrepo:ListApplicationVersions](#list_serverlessrepo-action-ListApplicationVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplications  **
  - **IAM action:**  [serverlessrepo:ListApplications](#list_serverlessrepo-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutApplicationPolicy  **
  - **IAM action:**  [serverlessrepo:PutApplicationPolicy](#list_serverlessrepo-action-PutApplicationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UnshareApplication  **
  - **IAM action:**  [serverlessrepo:UnshareApplication](#list_serverlessrepo-action-UnshareApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApplication  **
  - **IAM action:**  [serverlessrepo:UpdateApplication](#list_serverlessrepo-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Serverless Application Repository
<a name="list_serverlessrepo-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateApplication](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications.html)  **
  - **Description:** Grants permission to create an application, optionally including an AWS SAM file to create the first application version in the same call
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateApplicationVersion](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-versions-semanticversion.html)  **
  - **Description:** Grants permission to create an application version
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCloudFormationChangeSet](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-changesets.html)  **
  - **Description:** Grants permission to create an AWS CloudFormation ChangeSet for the given application
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:** [serverlessrepo:applicationType](#list_serverlessrepo-serverlessrepo_applicationType)
  - **Access level:** Write

- **   [CreateCloudFormationTemplate](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-templates.html)  **
  - **Description:** Grants permission to create an AWS CloudFormation template
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:** [serverlessrepo:applicationType](#list_serverlessrepo-serverlessrepo_applicationType)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid.html)  **
  - **Description:** Grants permission to delete the specified application
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid.html)  **
  - **Description:** Grants permission to get the specified application
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:** [serverlessrepo:applicationType](#list_serverlessrepo-serverlessrepo_applicationType)
  - **Access level:** Read

- **   [GetApplicationPolicy](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-policy.html)  **
  - **Description:** Grants permission to get the policy for the specified application
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCloudFormationTemplate](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-templates-templateid.html)  **
  - **Description:** Grants permission to get the specified AWS CloudFormation template
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListApplicationDependencies](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-dependencies.html)  **
  - **Description:** Grants permission to retrieve the list of applications nested in the containing application
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:** [serverlessrepo:applicationType](#list_serverlessrepo-serverlessrepo_applicationType)
  - **Access level:** List

- **   [ListApplicationVersions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-versions.html)  **
  - **Description:** Grants permission to list versions for the specified application owned by the requester
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:** [serverlessrepo:applicationType](#list_serverlessrepo-serverlessrepo_applicationType)
  - **Access level:** List

- **   [ListApplications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications.html)  **
  - **Description:** Grants permission to list applications owned by the requester
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutApplicationPolicy](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid-policy.html)  **
  - **Description:** Grants permission to put the policy for the specified application
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SearchApplications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid.html)  **
  - **Description:** Grants permission to get all applications authorized for this user
  - **Resource types (\*required):** 
  - **Condition keys:** [serverlessrepo:applicationType](#list_serverlessrepo-serverlessrepo_applicationType)
  - **Access level:** Read

- **   [UnshareApplication](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid.html)  **
  - **Description:** Grants permission to unshare the specified application
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplication](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications-applicationid.html)  **
  - **Description:** Grants permission to update meta-data of the application
  - **Resource types (\*required):** [applications\*](#list_serverlessrepo-resource-applications)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Serverless Application Repository
<a name="list_serverlessrepo-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [applications](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/applications.html)  | arn:${Partition}:serverlessrepo:${Region}:${Account}:applications/${ResourceId} |   | 

## Condition keys for AWS Serverless Application Repository
<a name="list_serverlessrepo-policy-keys"></a>

AWS Serverless Application Repository defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [serverlessrepo:applicationType](https://docs.aws.amazon.com/IAM/latest/UserGuide/applications.html)  | Filters access by application type | String | 