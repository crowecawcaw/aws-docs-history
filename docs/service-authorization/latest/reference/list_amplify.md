

# Actions, resources, and condition keys for AWS Amplify
<a name="list_amplify"></a>

AWS Amplify (service prefix: `amplify`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amplify/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amplify/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amplify/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/amplify/amplify.json) for this service.

**Topics**
+ [API operations defined by AWS Amplify](#list_amplify-operations)
+ [Actions defined by AWS Amplify](#list_amplify-actions-as-permissions)
+ [Resource types defined by AWS Amplify](#list_amplify-resources-for-iam-policies)
+ [Condition keys for AWS Amplify](#list_amplify-policy-keys)

## API operations defined by AWS Amplify
<a name="list_amplify-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_amplify-actions-as-permissions).




- **   CreateApp  **
  - **IAM action:**  [amplify:CreateApp](#list_amplify-action-CreateApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [amplify:TagResource](#list_amplify-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** amplify.amazonaws.com / **Access level:** Write

- **   CreateBackendEnvironment  **
  - **IAM action:**  [amplify:CreateBackendEnvironment](#list_amplify-action-CreateBackendEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBranch  **
  - **IAM action:**  [amplify:CreateBranch](#list_amplify-action-CreateBranch)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [amplify:TagResource](#list_amplify-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** amplify.amazonaws.com / **Access level:** Write

- **   CreateDeployment  **
  - **IAM action:**  [amplify:CreateDeployment](#list_amplify-action-CreateDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDomainAssociation  **
  - **IAM action:**  [amplify:CreateDomainAssociation](#list_amplify-action-CreateDomainAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** amplify.amazonaws.com / **Access level:** Write

- **   CreateWebhook  **
  - **IAM action:**  [amplify:CreateWebHook](#list_amplify-action-CreateWebHook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApp  **
  - **IAM action:**  [amplify:DeleteApp](#list_amplify-action-DeleteApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBackendEnvironment  **
  - **IAM action:**  [amplify:DeleteBackendEnvironment](#list_amplify-action-DeleteBackendEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBranch  **
  - **IAM action:**  [amplify:DeleteBranch](#list_amplify-action-DeleteBranch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainAssociation  **
  - **IAM action:**  [amplify:DeleteDomainAssociation](#list_amplify-action-DeleteDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJob  **
  - **IAM action:**  [amplify:DeleteJob](#list_amplify-action-DeleteJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebhook  **
  - **IAM action:**  [amplify:DeleteWebHook](#list_amplify-action-DeleteWebHook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateAccessLogs  **
  - **IAM action:**  [amplify:GenerateAccessLogs](#list_amplify-action-GenerateAccessLogs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApp  **
  - **IAM action:**  [amplify:GetApp](#list_amplify-action-GetApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArtifactUrl  **
  - **IAM action:**  [amplify:GetArtifactUrl](#list_amplify-action-GetArtifactUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBackendEnvironment  **
  - **IAM action:**  [amplify:GetBackendEnvironment](#list_amplify-action-GetBackendEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBranch  **
  - **IAM action:**  [amplify:GetBranch](#list_amplify-action-GetBranch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainAssociation  **
  - **IAM action:**  [amplify:GetDomainAssociation](#list_amplify-action-GetDomainAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJob  **
  - **IAM action:**  [amplify:GetJob](#list_amplify-action-GetJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWebhook  **
  - **IAM action:**  [amplify:GetWebHook](#list_amplify-action-GetWebHook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApps  **
  - **IAM action:**  [amplify:ListApps](#list_amplify-action-ListApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArtifacts  **
  - **IAM action:**  [amplify:ListArtifacts](#list_amplify-action-ListArtifacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBackendEnvironments  **
  - **IAM action:**  [amplify:ListBackendEnvironments](#list_amplify-action-ListBackendEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBranches  **
  - **IAM action:**  [amplify:ListBranches](#list_amplify-action-ListBranches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainAssociations  **
  - **IAM action:**  [amplify:ListDomainAssociations](#list_amplify-action-ListDomainAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **IAM action:**  [amplify:ListJobs](#list_amplify-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [amplify:ListTagsForResource](#list_amplify-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWebhooks  **
  - **IAM action:**  [amplify:ListWebHooks](#list_amplify-action-ListWebHooks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartDeployment  **
  - **IAM action:**  [amplify:StartDeployment](#list_amplify-action-StartDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartJob  **
  - **IAM action:**  [amplify:StartJob](#list_amplify-action-StartJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopJob  **
  - **IAM action:**  [amplify:StopJob](#list_amplify-action-StopJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [amplify:TagResource](#list_amplify-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [amplify:UntagResource](#list_amplify-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApp  **
  - **IAM action:**  [amplify:UpdateApp](#list_amplify-action-UpdateApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** amplify.amazonaws.com / **Access level:** Write

- **   UpdateBranch  **
  - **IAM action:**  [amplify:UpdateBranch](#list_amplify-action-UpdateBranch)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** amplify.amazonaws.com / **Access level:** Write

- **   UpdateDomainAssociation  **
  - **IAM action:**  [amplify:UpdateDomainAssociation](#list_amplify-action-UpdateDomainAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** amplify.amazonaws.com / **Access level:** Write

- **   UpdateWebhook  **
  - **IAM action:**  [amplify:UpdateWebHook](#list_amplify-action-UpdateWebHook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Amplify
<a name="list_amplify-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateWebACL](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to associate a WebACL to a Resource
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApp](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to create a new Amplify App
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplify-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBackendEnvironment](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to create a new backend environment for an Amplify App
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBranch](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to create a new Branch for an Amplify App
  - **Resource types (\*required):** [branches\*](#list_amplify-resource-branches)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplify-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeployment](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to create a deployment for manual deploy apps. (Apps are not connected to repository)
  - **Resource types (\*required):** [branches\*](#list_amplify-resource-branches)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDomainAssociation](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to create a new DomainAssociation on an App
  - **Resource types (\*required):** [domains\*](#list_amplify-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWebHook](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to create a new webhook on an App
  - **Resource types (\*required):** [branches\*](#list_amplify-resource-branches)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApp](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to delete an existing Amplify App by appId
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackendEnvironment](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to delete a branch for an Amplify App
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBranch](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to delete a branch for an Amplify App
  - **Resource types (\*required):** [branches\*](#list_amplify-resource-branches)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomainAssociation](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to delete a DomainAssociation
  - **Resource types (\*required):** [domains\*](#list_amplify-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJob](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to delete a job, for an Amplify branch, part of Amplify App
  - **Resource types (\*required):** [jobs\*](#list_amplify-resource-jobs)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteWebHook](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to delete a webhook by id
  - **Resource types (\*required):** [webhooks\*](#list_amplify-resource-webhooks)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWebACL](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to disassociate a WebACL from a Resource
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateAccessLogs](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to generate website access logs for a specific time range via a pre-signed URL
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApp](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to retrieve an existing Amplify App by appId
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetArtifactUrl](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to retrieve artifact info that corresponds to a artifactId
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBackendEnvironment](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to retrieve a backend environment for an Amplify App
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBranch](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to retrieve a branch for an Amplify App
  - **Resource types (\*required):** [branches\*](#list_amplify-resource-branches)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainAssociation](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to retrieve domain info that corresponds to an appId and domainName
  - **Resource types (\*required):** [domains\*](#list_amplify-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJob](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to get a job for a branch, part of an Amplify App
  - **Resource types (\*required):** [jobs\*](#list_amplify-resource-jobs)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWebACLForResource](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to retrieve the WebACL associated with a Resource
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWebHook](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to retrieve webhook info that corresponds to a webhookId
  - **Resource types (\*required):** [webhooks\*](#list_amplify-resource-webhooks)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApps](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list existing Amplify Apps
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListArtifacts](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list artifacts with an app, a branch, a job and an artifact type
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBackendEnvironments](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list backend environments for an Amplify App
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBranches](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list branches for an Amplify App
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomainAssociations](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list domains with an app
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list Jobs for a branch, part of an Amplify App
  - **Resource types (\*required):** [branches\*](#list_amplify-resource-branches)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListResourcesForWebACL](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list the Resources associated with a WebACL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list tags for an AWS Amplify Console resource
  - **Resource types (\*required):** [apps](#list_amplify-resource-apps) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [branches](#list_amplify-resource-branches) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains](#list_amplify-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [webhooks](#list_amplify-resource-webhooks) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWebHooks](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list webhooks on an App
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [StartDeployment](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to start a deployment for manual deploy apps. (Apps are not connected to repository)
  - **Resource types (\*required):** [branches\*](#list_amplify-resource-branches)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartJob](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to start a new job for a branch, part of an Amplify App
  - **Resource types (\*required):** [jobs\*](#list_amplify-resource-jobs)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopJob](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to stop a job that is in progress, for an Amplify branch, part of Amplify App
  - **Resource types (\*required):** [jobs\*](#list_amplify-resource-jobs)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to tag an AWS Amplify Console resource
  - **Resource types (\*required):** [apps](#list_amplify-resource-apps) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplify-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Resource types (\*required):** [branches](#list_amplify-resource-branches) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplify-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Resource types (\*required):** [domains](#list_amplify-resource-domains) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplify-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Resource types (\*required):** [webhooks](#list_amplify-resource-webhooks) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplify-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to remove a tag from an AWS Amplify Console resource
  - **Resource types (\*required):** [apps](#list_amplify-resource-apps) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Resource types (\*required):** [branches](#list_amplify-resource-branches) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Resource types (\*required):** [domains](#list_amplify-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Resource types (\*required):** [webhooks](#list_amplify-resource-webhooks) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplify-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApp](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to update an existing Amplify App
  - **Resource types (\*required):** [apps\*](#list_amplify-resource-apps)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBranch](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to update a branch for an Amplify App
  - **Resource types (\*required):** [branches\*](#list_amplify-resource-branches)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainAssociation](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to update a DomainAssociation on an App
  - **Resource types (\*required):** [domains\*](#list_amplify-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWebHook](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to update a webhook
  - **Resource types (\*required):** [webhooks\*](#list_amplify-resource-webhooks)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Amplify
<a name="list_amplify-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [apps](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplify:${Region}:${Account}:apps/${AppId} | [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_) | 
|  [branches](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplify:${Region}:${Account}:apps/${AppId}/branches/${BranchName} | [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_) | 
|  [domains](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplify:${Region}:${Account}:apps/${AppId}/domains/${DomainName} | [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_) | 
|  [jobs](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplify:${Region}:${Account}:apps/${AppId}/branches/${BranchName}/jobs/${JobId} |   | 
|  [webhooks](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplify:${Region}:${Account}:webhooks/${WebhookId} | [aws:ResourceTag/${TagKey}](#list_amplify-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Amplify
<a name="list_amplify-policy-keys"></a>

AWS Amplify defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag's key associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 