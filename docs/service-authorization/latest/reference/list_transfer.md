

# Actions, resources, and condition keys for AWS Transfer Family
<a name="list_transfer"></a>

AWS Transfer Family (service prefix: `transfer`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/transfer/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/transfer/latest/userguide/api_reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/transfer/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/transfer/transfer.json) for this service.

**Topics**
+ [API operations defined by AWS Transfer Family](#list_transfer-operations)
+ [Actions defined by AWS Transfer Family](#list_transfer-actions-as-permissions)
+ [Resource types defined by AWS Transfer Family](#list_transfer-resources-for-iam-policies)
+ [Condition keys for AWS Transfer Family](#list_transfer-policy-keys)

## API operations defined by AWS Transfer Family
<a name="list_transfer-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_transfer-actions-as-permissions).




- **   CreateAccess  **
  - **IAM action:**  [transfer:CreateAccess](#list_transfer-action-CreateAccess)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   CreateAgreement  **
  - **IAM action:**  [transfer:CreateAgreement](#list_transfer-action-CreateAgreement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   CreateConnector  **
  - **IAM action:**  [transfer:CreateConnector](#list_transfer-action-CreateConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   CreateProfile  **
  - **IAM action:**  [transfer:CreateProfile](#list_transfer-action-CreateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServer  **
  - **IAM action:**  [transfer:CreateServer](#list_transfer-action-CreateServer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   CreateUser  **
  - **IAM action:**  [transfer:CreateUser](#list_transfer-action-CreateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   CreateWebApp  **
  - **IAM action:**  [transfer:CreateWebApp](#list_transfer-action-CreateWebApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   CreateWorkflow  **
  - **IAM action:**  [transfer:CreateWorkflow](#list_transfer-action-CreateWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccess  **
  - **IAM action:**  [transfer:DeleteAccess](#list_transfer-action-DeleteAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgreement  **
  - **IAM action:**  [transfer:DeleteAgreement](#list_transfer-action-DeleteAgreement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCertificate  **
  - **IAM action:**  [transfer:DeleteCertificate](#list_transfer-action-DeleteCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnector  **
  - **IAM action:**  [transfer:DeleteConnector](#list_transfer-action-DeleteConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHostKey  **
  - **IAM action:**  [transfer:DeleteHostKey](#list_transfer-action-DeleteHostKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfile  **
  - **IAM action:**  [transfer:DeleteProfile](#list_transfer-action-DeleteProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServer  **
  - **IAM action:**  [transfer:DeleteServer](#list_transfer-action-DeleteServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSshPublicKey  **
  - **IAM action:**  [transfer:DeleteSshPublicKey](#list_transfer-action-DeleteSshPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [transfer:DeleteUser](#list_transfer-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebApp  **
  - **IAM action:**  [transfer:DeleteWebApp](#list_transfer-action-DeleteWebApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebAppCustomization  **
  - **IAM action:**  [transfer:DeleteWebAppCustomization](#list_transfer-action-DeleteWebAppCustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflow  **
  - **IAM action:**  [transfer:DeleteWorkflow](#list_transfer-action-DeleteWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccess  **
  - **IAM action:**  [transfer:DescribeAccess](#list_transfer-action-DescribeAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAgreement  **
  - **IAM action:**  [transfer:DescribeAgreement](#list_transfer-action-DescribeAgreement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCertificate  **
  - **IAM action:**  [transfer:DescribeCertificate](#list_transfer-action-DescribeCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnector  **
  - **IAM action:**  [transfer:DescribeConnector](#list_transfer-action-DescribeConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExecution  **
  - **IAM action:**  [transfer:DescribeExecution](#list_transfer-action-DescribeExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHostKey  **
  - **IAM action:**  [transfer:DescribeHostKey](#list_transfer-action-DescribeHostKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProfile  **
  - **IAM action:**  [transfer:DescribeProfile](#list_transfer-action-DescribeProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSecurityPolicy  **
  - **IAM action:**  [transfer:DescribeSecurityPolicy](#list_transfer-action-DescribeSecurityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServer  **
  - **IAM action:**  [transfer:DescribeServer](#list_transfer-action-DescribeServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUser  **
  - **IAM action:**  [transfer:DescribeUser](#list_transfer-action-DescribeUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWebApp  **
  - **IAM action:**  [transfer:DescribeWebApp](#list_transfer-action-DescribeWebApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWebAppCustomization  **
  - **IAM action:**  [transfer:DescribeWebAppCustomization](#list_transfer-action-DescribeWebAppCustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkflow  **
  - **IAM action:**  [transfer:DescribeWorkflow](#list_transfer-action-DescribeWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportCertificate  **
  - **IAM action:**  [transfer:ImportCertificate](#list_transfer-action-ImportCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ImportHostKey  **
  - **IAM action:**  [transfer:ImportHostKey](#list_transfer-action-ImportHostKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ImportSshPublicKey  **
  - **IAM action:**  [transfer:ImportSshPublicKey](#list_transfer-action-ImportSshPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAccesses  **
  - **IAM action:**  [transfer:ListAccesses](#list_transfer-action-ListAccesses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgreements  **
  - **IAM action:**  [transfer:ListAgreements](#list_transfer-action-ListAgreements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCertificates  **
  - **IAM action:**  [transfer:ListCertificates](#list_transfer-action-ListCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConnectors  **
  - **IAM action:**  [transfer:ListConnectors](#list_transfer-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListExecutions  **
  - **IAM action:**  [transfer:ListExecutions](#list_transfer-action-ListExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFileTransferResults  **
  - **IAM action:**  [transfer:ListFileTransferResults](#list_transfer-action-ListFileTransferResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListHostKeys  **
  - **IAM action:**  [transfer:ListHostKeys](#list_transfer-action-ListHostKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListProfiles  **
  - **IAM action:**  [transfer:ListProfiles](#list_transfer-action-ListProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSecurityPolicies  **
  - **IAM action:**  [transfer:ListSecurityPolicies](#list_transfer-action-ListSecurityPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServers  **
  - **IAM action:**  [transfer:ListServers](#list_transfer-action-ListServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [transfer:ListTagsForResource](#list_transfer-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListUsers  **
  - **IAM action:**  [transfer:ListUsers](#list_transfer-action-ListUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWebApps  **
  - **IAM action:**  [transfer:ListWebApps](#list_transfer-action-ListWebApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflows  **
  - **IAM action:**  [transfer:ListWorkflows](#list_transfer-action-ListWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SendWorkflowStepState  **
  - **IAM action:**  [transfer:SendWorkflowStepState](#list_transfer-action-SendWorkflowStepState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDirectoryListing  **
  - **IAM action:**  [transfer:StartDirectoryListing](#list_transfer-action-StartDirectoryListing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFileTransfer  **
  - **IAM action:**  [transfer:StartFileTransfer](#list_transfer-action-StartFileTransfer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRemoteDelete  **
  - **IAM action:**  [transfer:StartRemoteDelete](#list_transfer-action-StartRemoteDelete) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRemoteMove  **
  - **IAM action:**  [transfer:StartRemoteMove](#list_transfer-action-StartRemoteMove) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartServer  **
  - **IAM action:**  [transfer:StartServer](#list_transfer-action-StartServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopServer  **
  - **IAM action:**  [transfer:StopServer](#list_transfer-action-StopServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [transfer:TagResource](#list_transfer-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestConnection  **
  - **IAM action:**  [transfer:TestConnection](#list_transfer-action-TestConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestIdentityProvider  **
  - **IAM action:**  [transfer:TestIdentityProvider](#list_transfer-action-TestIdentityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UntagResource  **
  - **IAM action:**  [transfer:UntagResource](#list_transfer-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccess  **
  - **IAM action:**  [transfer:UpdateAccess](#list_transfer-action-UpdateAccess)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   UpdateAgreement  **
  - **IAM action:**  [transfer:UpdateAgreement](#list_transfer-action-UpdateAgreement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   UpdateCertificate  **
  - **IAM action:**  [transfer:UpdateCertificate](#list_transfer-action-UpdateCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnector  **
  - **IAM action:**  [transfer:UpdateConnector](#list_transfer-action-UpdateConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   UpdateHostKey  **
  - **IAM action:**  [transfer:UpdateHostKey](#list_transfer-action-UpdateHostKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProfile  **
  - **IAM action:**  [transfer:UpdateProfile](#list_transfer-action-UpdateProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServer  **
  - **IAM action:**  [transfer:UpdateServer](#list_transfer-action-UpdateServer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   UpdateUser  **
  - **IAM action:**  [transfer:UpdateUser](#list_transfer-action-UpdateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   UpdateWebApp  **
  - **IAM action:**  [transfer:UpdateWebApp](#list_transfer-action-UpdateWebApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transfer.amazonaws.com / **Access level:** Write

- **   UpdateWebAppCustomization  **
  - **IAM action:**  [transfer:UpdateWebAppCustomization](#list_transfer-action-UpdateWebAppCustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Transfer Family
<a name="list_transfer-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAccess](https://docs.aws.amazon.com/transfer/latest/userguide/API_CreateAccess.html)  **
  - **Description:** Grants permission to add an access associated with a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgreement](https://docs.aws.amazon.com/transfer/latest/userguide/API_CreateAgreement.html)  **
  - **Description:** Grants permission to add an agreement associated with a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnector](https://docs.aws.amazon.com/transfer/latest/userguide/API_CreateConnector.html)  **
  - **Description:** Grants permission to create a connector
  - **Resource types (\*required):** [profile](#list_transfer-resource-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)<br />[transfer:RequestConnectorProtocol](#list_transfer-transfer_RequestConnectorProtocol)<br />[transfer:RequestSecurityPolicyName](#list_transfer-transfer_RequestSecurityPolicyName)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/transfer/latest/userguide/API_CreateProfile.html)  **
  - **Description:** Grants permission to create a profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_CreateServer.html)  **
  - **Description:** Grants permission to create a server
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)<br />[transfer:RequestSecurityPolicyName](#list_transfer-transfer_RequestSecurityPolicyName)<br />[transfer:RequestServerDomain](#list_transfer-transfer_RequestServerDomain)<br />[transfer:RequestServerEndpointType](#list_transfer-transfer_RequestServerEndpointType)<br />[transfer:RequestServerProtocols](#list_transfer-transfer_RequestServerProtocols)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/transfer/latest/userguide/API_CreateUser.html)  **
  - **Description:** Grants permission to add a user associated with a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWebApp](https://docs.aws.amazon.com/transfer/latest/userguide/API_CreateWebApp.html)  **
  - **Description:** Grants permission to create a webapp
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkflow](https://docs.aws.amazon.com/transfer/latest/userguide/API_CreateWorkflow.html)  **
  - **Description:** Grants permission to create a workflow
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccess](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteAccess.html)  **
  - **Description:** Grants permission to delete access
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgreement](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteAgreement.html)  **
  - **Description:** Grants permission to delete agreement
  - **Resource types (\*required):** [agreement\*](#list_transfer-resource-agreement)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCertificate](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteCertificate.html)  **
  - **Description:** Grants permission to delete certificate
  - **Resource types (\*required):** [certificate\*](#list_transfer-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteConnector.html)  **
  - **Description:** Grants permission to delete connector
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHostKey](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteHostKey.html)  **
  - **Description:** Grants permission to delete a host key associated with a server
  - **Resource types (\*required):** [host-key\*](#list_transfer-resource-host-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteProfile.html)  **
  - **Description:** Grants permission to delete profile
  - **Resource types (\*required):** [profile\*](#list_transfer-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteServer.html)  **
  - **Description:** Grants permission to delete a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSshPublicKey](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteSshPublicKey.html)  **
  - **Description:** Grants permission to delete an SSH public key from a user
  - **Resource types (\*required):** [user\*](#list_transfer-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete a user associated with a server
  - **Resource types (\*required):** [user\*](#list_transfer-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWebApp](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteWebApp.html)  **
  - **Description:** Grants permission to delete webapp
  - **Resource types (\*required):** [webapp\*](#list_transfer-resource-webapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWebAppCustomization](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteWebAppCustomization.html)  **
  - **Description:** Grants permission to delete webapp customization
  - **Resource types (\*required):** [webapp\*](#list_transfer-resource-webapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkflow](https://docs.aws.amazon.com/transfer/latest/userguide/API_DeleteWorkflow.html)  **
  - **Description:** Grants permission to delete a workflow
  - **Resource types (\*required):** [workflow\*](#list_transfer-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccess](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeAccess.html)  **
  - **Description:** Grants permission to describe an access assigned to a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAgreement](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeAgreement.html)  **
  - **Description:** Grants permission to describe an agreement assigned to a server
  - **Resource types (\*required):** [agreement\*](#list_transfer-resource-agreement)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCertificate](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeCertificate.html)  **
  - **Description:** Grants permission to describe a certificate
  - **Resource types (\*required):** [certificate\*](#list_transfer-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConnector](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeConnector.html)  **
  - **Description:** Grants permission to describe a connector
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExecution](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeExecution.html)  **
  - **Description:** Grants permission to describe an execution associated with a workflow
  - **Resource types (\*required):** [workflow\*](#list_transfer-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHostKey](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeHostKey.html)  **
  - **Description:** Grants permission to describe a host key associated with a server
  - **Resource types (\*required):** [host-key\*](#list_transfer-resource-host-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProfile](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeProfile.html)  **
  - **Description:** Grants permission to describe a profile
  - **Resource types (\*required):** [profile\*](#list_transfer-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSecurityPolicy](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeSecurityPolicy.html)  **
  - **Description:** Grants permission to describe a security policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeServer.html)  **
  - **Description:** Grants permission to describe a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUser](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeUser.html)  **
  - **Description:** Grants permission to describe a user associated with a server
  - **Resource types (\*required):** [user\*](#list_transfer-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWebApp](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeWebApp.html)  **
  - **Description:** Grants permission to describe a webapp
  - **Resource types (\*required):** [webapp\*](#list_transfer-resource-webapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWebAppCustomization](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeWebAppCustomization.html)  **
  - **Description:** Grants permission to describe a webapp customization
  - **Resource types (\*required):** [webapp\*](#list_transfer-resource-webapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkflow](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeWorkflow.html)  **
  - **Description:** Grants permission to describe a workflow
  - **Resource types (\*required):** [workflow\*](#list_transfer-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportCertificate](https://docs.aws.amazon.com/transfer/latest/userguide/API_ImportCertificate.html)  **
  - **Description:** Grants permission to add a certificate
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Write

- **   [ImportHostKey](https://docs.aws.amazon.com/transfer/latest/userguide/API_ImportHostKey.html)  **
  - **Description:** Grants permission to add a host key to a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Write

- **   [ImportSshPublicKey](https://docs.aws.amazon.com/transfer/latest/userguide/API_ImportSshPublicKey.html)  **
  - **Description:** Grants permission to add an SSH public key to a user
  - **Resource types (\*required):** [user\*](#list_transfer-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAccesses](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListAccesses.html)  **
  - **Description:** Grants permission to list accesses
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAgreements](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListAgreements.html)  **
  - **Description:** Grants permission to list agreements
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCertificates](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListCertificates.html)  **
  - **Description:** Grants permission to list certificates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConnectors](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListConnectors.html)  **
  - **Description:** Grants permission to list connectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExecutions](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListExecutions.html)  **
  - **Description:** Grants permission to list executions associated with a workflow
  - **Resource types (\*required):** [workflow\*](#list_transfer-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFileTransferResults](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListFileTransferResults.html)  **
  - **Description:** Grants permission to list file transfer statuses for connectors
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListHostKeys](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListHostKeys.html)  **
  - **Description:** Grants permission to list host keys associated with a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListProfiles](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListProfiles.html)  **
  - **Description:** Grants permission to list profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSecurityPolicies](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListSecurityPolicies.html)  **
  - **Description:** Grants permission to list security policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServers](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListServers.html)  **
  - **Description:** Grants permission to list servers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an AWS Transfer Family resource
  - **Resource types (\*required):** [agreement](#list_transfer-resource-agreement) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [certificate](#list_transfer-resource-certificate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connector](#list_transfer-resource-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [host-key](#list_transfer-resource-host-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [profile](#list_transfer-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [server](#list_transfer-resource-server) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user](#list_transfer-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workflow](#list_transfer-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUsers](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListUsers.html)  **
  - **Description:** Grants permission to list users associated with a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWebApps](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListWebApps.html)  **
  - **Description:** Grants permission to list webapps
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkflows](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListWorkflows.html)  **
  - **Description:** Grants permission to list workflows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SendWorkflowStepState](https://docs.aws.amazon.com/transfer/latest/userguide/API_SendWorkflowStepState.html)  **
  - **Description:** Grants permission to send a callback for asynchronous custom steps
  - **Resource types (\*required):** [workflow\*](#list_transfer-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDirectoryListing](https://docs.aws.amazon.com/transfer/latest/userguide/API_StartDirectoryListing.html)  **
  - **Description:** Grants permission to initiate a list operation on a remote server using a connector
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFileTransfer](https://docs.aws.amazon.com/transfer/latest/userguide/API_StartFileTransfer.html)  **
  - **Description:** Grants permission to initiate a connector file transfer
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRemoteDelete](https://docs.aws.amazon.com/transfer/latest/userguide/API_StartRemoteDelete.html)  **
  - **Description:** Grants permission to initiate a connector delete operation on remote server
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRemoteMove](https://docs.aws.amazon.com/transfer/latest/userguide/API_StartRemoteMove.html)  **
  - **Description:** Grants permission to initiate a connector move operation on remote server
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_StartServer.html)  **
  - **Description:** Grants permission to start a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_StopServer.html)  **
  - **Description:** Grants permission to stop a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/transfer/latest/userguide/API_TagResource.html)  **
  - **Description:** Grants permission to tag an AWS Transfer Family resource
  - **Resource types (\*required):** [agreement](#list_transfer-resource-agreement) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [certificate](#list_transfer-resource-certificate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [connector](#list_transfer-resource-connector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [host-key](#list_transfer-resource-host-key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_transfer-resource-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [server](#list_transfer-resource-server) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_transfer-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [webapp](#list_transfer-resource-webapp) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_transfer-resource-workflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transfer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestConnection](https://docs.aws.amazon.com/transfer/latest/userguide/API_TestConnection.html)  **
  - **Description:** Grants permission to test a connector's connection to remote server
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TestIdentityProvider](https://docs.aws.amazon.com/transfer/latest/userguide/API_TestIdentityProvider.html)  **
  - **Description:** Grants permission to test a server's custom identity provider
  - **Resource types (\*required):** [user\*](#list_transfer-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [UntagResource](https://docs.aws.amazon.com/transfer/latest/userguide/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an AWS Transfer Family resource
  - **Resource types (\*required):** [agreement](#list_transfer-resource-agreement) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [certificate](#list_transfer-resource-certificate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [connector](#list_transfer-resource-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [host-key](#list_transfer-resource-host-key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_transfer-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [server](#list_transfer-resource-server) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_transfer-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [webapp](#list_transfer-resource-webapp) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_transfer-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transfer-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccess](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateAccess.html)  **
  - **Description:** Grants permission to update access
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAgreement](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateAgreement.html)  **
  - **Description:** Grants permission to update an agreement
  - **Resource types (\*required):** [agreement\*](#list_transfer-resource-agreement)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCertificate](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateCertificate.html)  **
  - **Description:** Grants permission to update a certificate
  - **Resource types (\*required):** [certificate\*](#list_transfer-resource-certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConnector](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateConnector.html)  **
  - **Description:** Grants permission to update a connector
  - **Resource types (\*required):** [connector\*](#list_transfer-resource-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[transfer:RequestSecurityPolicyName](#list_transfer-transfer_RequestSecurityPolicyName)
  - **Resource types (\*required):** [profile](#list_transfer-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[transfer:RequestSecurityPolicyName](#list_transfer-transfer_RequestSecurityPolicyName)
  - **Access level:** Write

- **   [UpdateHostKey](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateHostKey.html)  **
  - **Description:** Grants permission to update a host key
  - **Resource types (\*required):** [host-key\*](#list_transfer-resource-host-key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProfile](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateProfile.html)  **
  - **Description:** Grants permission to update a profile
  - **Resource types (\*required):** [profile\*](#list_transfer-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateServer.html)  **
  - **Description:** Grants permission to update the configuration of a server
  - **Resource types (\*required):** [server\*](#list_transfer-resource-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)<br />[transfer:RequestSecurityPolicyName](#list_transfer-transfer_RequestSecurityPolicyName)<br />[transfer:RequestServerEndpointType](#list_transfer-transfer_RequestServerEndpointType)<br />[transfer:RequestServerProtocols](#list_transfer-transfer_RequestServerProtocols)
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateUser.html)  **
  - **Description:** Grants permission to update the configuration of a user
  - **Resource types (\*required):** [user\*](#list_transfer-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWebApp](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateWebApp.html)  **
  - **Description:** Grants permission to update the configuration of a webapp
  - **Resource types (\*required):** [webapp\*](#list_transfer-resource-webapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWebAppCustomization](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateWebAppCustomization.html)  **
  - **Description:** Grants permission to update the configuration of a webapp cutomization
  - **Resource types (\*required):** [webapp\*](#list_transfer-resource-webapp)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Transfer Family
<a name="list_transfer-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [agreement](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html)  | arn:${Partition}:transfer:${Region}:${Account}:agreement/${ServerId}/${AgreementId} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 
|  [certificate](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html)  | arn:${Partition}:transfer:${Region}:${Account}:certificate/${CertificateId} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 
|  [connector](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html)  | arn:${Partition}:transfer:${Region}:${Account}:connector/${ConnectorId} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 
|  [host-key](https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html)  | arn:${Partition}:transfer:${Region}:${Account}:host-key/${ServerId}/${HostKeyId} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 
|  [profile](https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html)  | arn:${Partition}:transfer:${Region}:${Account}:profile/${ProfileId} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 
|  [server](https://docs.aws.amazon.com/transfer/latest/userguide/configuring-servers.html)  | arn:${Partition}:transfer:${Region}:${Account}:server/${ServerId} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 
|  [user](https://docs.aws.amazon.com/transfer/latest/userguide/create-user.html)  | arn:${Partition}:transfer:${Region}:${Account}:user/${ServerId}/${UserName} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 
|  [webapp](https://docs.aws.amazon.com/transfer/latest/userguide/web-app.html)  | arn:${Partition}:transfer:${Region}:${Account}:webapp/${WebAppId} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 
|  [workflow](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-workflows.html)  | arn:${Partition}:transfer:${Region}:${Account}:workflow/${WorkflowId} | [aws:ResourceTag/${TagKey}](#list_transfer-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Transfer Family
<a name="list_transfer-policy-keys"></a>

AWS Transfer Family defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [transfer:RequestConnectorProtocol](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-condition-keys.html)  | Filters access by the connector protocol that is passed in the request | String | 
|   [transfer:RequestSecurityPolicyName](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-condition-keys.html)  | Filters access by the security policy name that is passed in the request | String | 
|   [transfer:RequestServerDomain](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-condition-keys.html)  | Filters access by the storage domain that is passed in the request | String | 
|   [transfer:RequestServerEndpointType](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-condition-keys.html)  | Filters access by the endpoint type that is passed in the request | String | 
|   [transfer:RequestServerProtocols](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-condition-keys.html)  | Filters access by the server protocols that are passed in the request | ArrayOfString | 