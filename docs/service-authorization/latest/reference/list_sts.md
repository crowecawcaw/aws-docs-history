

# Actions, resources, and condition keys for AWS Security Token Service
<a name="list_sts"></a>

AWS Security Token Service (service prefix: `sts`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/STS/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sts/sts.json) for this service.

**Topics**
+ [API operations defined by AWS Security Token Service](#list_sts-operations)
+ [Actions defined by AWS Security Token Service](#list_sts-actions-as-permissions)
+ [Permission-only actions for AWS Security Token Service](#list_sts-permission-only-actions)
+ [Resource types defined by AWS Security Token Service](#list_sts-resources-for-iam-policies)
+ [Condition keys for AWS Security Token Service](#list_sts-policy-keys)

## API operations defined by AWS Security Token Service
<a name="list_sts-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sts-actions-as-permissions).




- **   AssumeRole  **
  - **IAM action:**  [sts:AssumeRole](#list_sts-action-AssumeRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sts:SetContext](#list_sts-action-SetContext)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sts:SetSourceIdentity](#list_sts-action-SetSourceIdentity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sts:TagSession](#list_sts-action-TagSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AssumeRoot  **
  - **IAM action:**  [sts:AssumeRoot](#list_sts-action-AssumeRoot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DecodeAuthorizationMessage  **
  - **IAM action:**  [sts:DecodeAuthorizationMessage](#list_sts-action-DecodeAuthorizationMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessKeyInfo  **
  - **IAM action:**  [sts:GetAccessKeyInfo](#list_sts-action-GetAccessKeyInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCallerIdentity  **
  - **IAM action:**  [sts:GetCallerIdentity](#list_sts-action-GetCallerIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDelegatedAccessToken  **
  - **IAM action:**  [sts:GetDelegatedAccessToken](#list_sts-action-GetDelegatedAccessToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetFederationToken  **
  - **IAM action:**  [sts:GetFederationToken](#list_sts-action-GetFederationToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sts:TagSession](#list_sts-action-TagSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   GetSessionToken  **
  - **IAM action:**  [sts:GetSessionToken](#list_sts-action-GetSessionToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWebIdentityToken  **
  - **IAM action:**  [sts:GetWebIdentityToken](#list_sts-action-GetWebIdentityToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sts:TagGetWebIdentityToken](#list_sts-action-TagGetWebIdentityToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write



## Actions defined by AWS Security Token Service
<a name="list_sts-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)  **
  - **Description:** Grants permission to obtain a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to
  - **Resource types (\*required):** [role\*](#list_sts-resource-role)
  - **Condition keys:** [accounts.google.com:aud](#list_sts-accounts.google.com_aud)<br />[accounts.google.com:sub](#list_sts-accounts.google.com_sub)<br />[aws:RequestTag/${TagKey}](#list_sts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sts-aws_TagKeys)<br />[cognito-identity.amazonaws.com:amr](#list_sts-cognito-identity.amazonaws.com_amr)<br />[cognito-identity.amazonaws.com:aud](#list_sts-cognito-identity.amazonaws.com_aud)<br />[cognito-identity.amazonaws.com:sub](#list_sts-cognito-identity.amazonaws.com_sub)<br />[graph.facebook.com:app\_id](#list_sts-graph.facebook.com_app_id)<br />[graph.facebook.com:id](#list_sts-graph.facebook.com_id)<br />[iam:ResourceTag/${TagKey}](#list_sts-iam_ResourceTag___TagKey_)<br />[saml:namequalifier](#list_sts-saml_namequalifier)<br />[saml:sub](#list_sts-saml_sub)<br />[saml:sub\_type](#list_sts-saml_sub_type)<br />[sts:ExternalId](#list_sts-sts_ExternalId)<br />[sts:RoleSessionName](#list_sts-sts_RoleSessionName)<br />[sts:SourceIdentity](#list_sts-sts_SourceIdentity)<br />[sts:TransitiveTagKeys](#list_sts-sts_TransitiveTagKeys)<br />[www.amazon.com:app\_id](#list_sts-www.amazon.com_app_id)<br />[www.amazon.com:user\_id](#list_sts-www.amazon.com_user_id)
  - **Access level:** Write

- **   [AssumeRoleWithSAML](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)  **
  - **Description:** Grants permission to obtain a set of temporary security credentials for users who have been authenticated via a SAML authentication response
  - **Resource types (\*required):** [role\*](#list_sts-resource-role)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sts-aws_TagKeys)<br />[iam:ResourceTag/${TagKey}](#list_sts-iam_ResourceTag___TagKey_)<br />[saml:aud](#list_sts-saml_aud)<br />[saml:cn](#list_sts-saml_cn)<br />[saml:commonName](#list_sts-saml_commonName)<br />[saml:doc](#list_sts-saml_doc)<br />[saml:eduorghomepageuri](#list_sts-saml_eduorghomepageuri)<br />[saml:eduorgidentityauthnpolicyuri](#list_sts-saml_eduorgidentityauthnpolicyuri)<br />[saml:eduorglegalname](#list_sts-saml_eduorglegalname)<br />[saml:eduorgsuperioruri](#list_sts-saml_eduorgsuperioruri)<br />[saml:eduorgwhitepagesuri](#list_sts-saml_eduorgwhitepagesuri)<br />[saml:edupersonaffiliation](#list_sts-saml_edupersonaffiliation)<br />[saml:edupersonassurance](#list_sts-saml_edupersonassurance)<br />[saml:edupersonentitlement](#list_sts-saml_edupersonentitlement)<br />[saml:edupersonnickname](#list_sts-saml_edupersonnickname)<br />[saml:edupersonorgdn](#list_sts-saml_edupersonorgdn)<br />[saml:edupersonorgunitdn](#list_sts-saml_edupersonorgunitdn)<br />[saml:edupersonprimaryaffiliation](#list_sts-saml_edupersonprimaryaffiliation)<br />[saml:edupersonprimaryorgunitdn](#list_sts-saml_edupersonprimaryorgunitdn)<br />[saml:edupersonprincipalname](#list_sts-saml_edupersonprincipalname)<br />[saml:edupersonscopedaffiliation](#list_sts-saml_edupersonscopedaffiliation)<br />[saml:edupersontargetedid](#list_sts-saml_edupersontargetedid)<br />[saml:givenName](#list_sts-saml_givenName)<br />[saml:iss](#list_sts-saml_iss)<br />[saml:mail](#list_sts-saml_mail)<br />[saml:name](#list_sts-saml_name)<br />[saml:namequalifier](#list_sts-saml_namequalifier)<br />[saml:organizationStatus](#list_sts-saml_organizationStatus)<br />[saml:primaryGroupSID](#list_sts-saml_primaryGroupSID)<br />[saml:sub](#list_sts-saml_sub)<br />[saml:sub\_type](#list_sts-saml_sub_type)<br />[saml:surname](#list_sts-saml_surname)<br />[saml:uid](#list_sts-saml_uid)<br />[saml:x500UniqueIdentifier](#list_sts-saml_x500UniqueIdentifier)<br />[sts:RoleSessionName](#list_sts-sts_RoleSessionName)<br />[sts:SourceIdentity](#list_sts-sts_SourceIdentity)<br />[sts:TransitiveTagKeys](#list_sts-sts_TransitiveTagKeys)
  - **Access level:** Write

- **   [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)  **
  - **Description:** Grants permission to obtain a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider
  - **Resource types (\*required):** [role\*](#list_sts-resource-role)
  - **Condition keys:** [accounts.google.com:aud](#list_sts-accounts.google.com_aud)<br />[accounts.google.com:google/organization\_number](#list_sts-accounts.google.com_google_organization_number)<br />[accounts.google.com:oaud](#list_sts-accounts.google.com_oaud)<br />[accounts.google.com:sub](#list_sts-accounts.google.com_sub)<br />[agent.${Domain}.buildkite.dev:build\_branch](#list_sts-agent.__Domain_.buildkite.dev_build_branch)<br />[agent.${Domain}.buildkite.dev:cluster\_id](#list_sts-agent.__Domain_.buildkite.dev_cluster_id)<br />[agent.${Domain}.buildkite.dev:cluster\_name](#list_sts-agent.__Domain_.buildkite.dev_cluster_name)<br />[agent.${Domain}.buildkite.dev:organization\_id](#list_sts-agent.__Domain_.buildkite.dev_organization_id)<br />[agent.${Domain}.buildkite.dev:organization\_slug](#list_sts-agent.__Domain_.buildkite.dev_organization_slug)<br />[agent.${Domain}.buildkite.dev:pipeline\_id](#list_sts-agent.__Domain_.buildkite.dev_pipeline_id)<br />[agent.${Domain}.buildkite.dev:pipeline\_slug](#list_sts-agent.__Domain_.buildkite.dev_pipeline_slug)<br />[agent.${Domain}.buildkite.site:build\_branch](#list_sts-agent.__Domain_.buildkite.site_build_branch)<br />[agent.${Domain}.buildkite.site:cluster\_id](#list_sts-agent.__Domain_.buildkite.site_cluster_id)<br />[agent.${Domain}.buildkite.site:cluster\_name](#list_sts-agent.__Domain_.buildkite.site_cluster_name)<br />[agent.${Domain}.buildkite.site:organization\_id](#list_sts-agent.__Domain_.buildkite.site_organization_id)<br />[agent.${Domain}.buildkite.site:organization\_slug](#list_sts-agent.__Domain_.buildkite.site_organization_slug)<br />[agent.${Domain}.buildkite.site:pipeline\_id](#list_sts-agent.__Domain_.buildkite.site_pipeline_id)<br />[agent.${Domain}.buildkite.site:pipeline\_slug](#list_sts-agent.__Domain_.buildkite.site_pipeline_slug)<br />[agent.buildkite.com:build\_branch](#list_sts-agent.buildkite.com_build_branch)<br />[agent.buildkite.com:cluster\_id](#list_sts-agent.buildkite.com_cluster_id)<br />[agent.buildkite.com:cluster\_name](#list_sts-agent.buildkite.com_cluster_name)<br />[agent.buildkite.com:organization\_id](#list_sts-agent.buildkite.com_organization_id)<br />[agent.buildkite.com:organization\_slug](#list_sts-agent.buildkite.com_organization_slug)<br />[agent.buildkite.com:pipeline\_id](#list_sts-agent.buildkite.com_pipeline_id)<br />[agent.buildkite.com:pipeline\_slug](#list_sts-agent.buildkite.com_pipeline_slug)<br />[aws:RequestTag/${TagKey}](#list_sts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sts-aws_TagKeys)<br />[cognito-identity.amazonaws.com:amr](#list_sts-cognito-identity.amazonaws.com_amr)<br />[cognito-identity.amazonaws.com:aud](#list_sts-cognito-identity.amazonaws.com_aud)<br />[cognito-identity.amazonaws.com:sub](#list_sts-cognito-identity.amazonaws.com_sub)<br />[github.com/enterprises/${EnterpriseName}:actor](#list_sts-github.com_enterprises___EnterpriseName__actor)<br />[github.com/enterprises/${EnterpriseName}:actor\_id](#list_sts-github.com_enterprises___EnterpriseName__actor_id)<br />[github.com/enterprises/${EnterpriseName}:enterprise\_id](#list_sts-github.com_enterprises___EnterpriseName__enterprise_id)<br />[github.com/enterprises/${EnterpriseName}:environment](#list_sts-github.com_enterprises___EnterpriseName__environment)<br />[github.com/enterprises/${EnterpriseName}:job\_workflow\_ref](#list_sts-github.com_enterprises___EnterpriseName__job_workflow_ref)<br />[github.com/enterprises/${EnterpriseName}:ref](#list_sts-github.com_enterprises___EnterpriseName__ref)<br />[github.com/enterprises/${EnterpriseName}:repository](#list_sts-github.com_enterprises___EnterpriseName__repository)<br />[github.com/enterprises/${EnterpriseName}:repository\_id](#list_sts-github.com_enterprises___EnterpriseName__repository_id)<br />[github.com/enterprises/${EnterpriseName}:repository\_owner\_id](#list_sts-github.com_enterprises___EnterpriseName__repository_owner_id)<br />[github.com/enterprises/${EnterpriseName}:workflow](#list_sts-github.com_enterprises___EnterpriseName__workflow)<br />[gitlab.com:namespace\_id](#list_sts-gitlab.com_namespace_id)<br />[gitlab.com:pipeline\_source](#list_sts-gitlab.com_pipeline_source)<br />[gitlab.com:project\_id](#list_sts-gitlab.com_project_id)<br />[gitlab.com:ref\_protected](#list_sts-gitlab.com_ref_protected)<br />[gitlab.com:runner\_environment](#list_sts-gitlab.com_runner_environment)<br />[gitlab.com:user\_access\_level](#list_sts-gitlab.com_user_access_level)<br />[gitlab.com:user\_email](#list_sts-gitlab.com_user_email)<br />[gitlab.com:user\_id](#list_sts-gitlab.com_user_id)<br />[gitlab.com:user\_login](#list_sts-gitlab.com_user_login)<br />[graph.facebook.com:app\_id](#list_sts-graph.facebook.com_app_id)<br />[graph.facebook.com:id](#list_sts-graph.facebook.com_id)<br />[iam:ResourceTag/${TagKey}](#list_sts-iam_ResourceTag___TagKey_)<br />[idcs-${OciUniqueIdentifier}.identity.oraclecloud.com:rpst\_id](#list_sts-idcs-__OciUniqueIdentifier_.identity.oraclecloud.com_rpst_id)<br />[oidc.circleci.com/org/${OrgId}:oidc.circleci.com/project-id](#list_sts-oidc.circleci.com_org___OrgId__oidc.circleci.com_project-id)<br />[sts:RoleAuthorizedByIdp](#list_sts-sts_RoleAuthorizedByIdp)<br />[sts:RoleSessionName](#list_sts-sts_RoleSessionName)<br />[sts:SourceIdentity](#list_sts-sts_SourceIdentity)<br />[sts:TransitiveTagKeys](#list_sts-sts_TransitiveTagKeys)<br />[token.actions.${Domain}.ghe.com:actor](#list_sts-token.actions.__Domain_.ghe.com_actor)<br />[token.actions.${Domain}.ghe.com:actor\_id](#list_sts-token.actions.__Domain_.ghe.com_actor_id)<br />[token.actions.${Domain}.ghe.com:enterprise\_id](#list_sts-token.actions.__Domain_.ghe.com_enterprise_id)<br />[token.actions.${Domain}.ghe.com:environment](#list_sts-token.actions.__Domain_.ghe.com_environment)<br />[token.actions.${Domain}.ghe.com:job\_workflow\_ref](#list_sts-token.actions.__Domain_.ghe.com_job_workflow_ref)<br />[token.actions.${Domain}.ghe.com:ref](#list_sts-token.actions.__Domain_.ghe.com_ref)<br />[token.actions.${Domain}.ghe.com:repository](#list_sts-token.actions.__Domain_.ghe.com_repository)<br />[token.actions.${Domain}.ghe.com:repository\_id](#list_sts-token.actions.__Domain_.ghe.com_repository_id)<br />[token.actions.${Domain}.ghe.com:repository\_owner\_id](#list_sts-token.actions.__Domain_.ghe.com_repository_owner_id)<br />[token.actions.${Domain}.ghe.com:workflow](#list_sts-token.actions.__Domain_.ghe.com_workflow)<br />[token.actions.githubusercontent.com/${SubPath}:actor](#list_sts-token.actions.githubusercontent.com___SubPath__actor)<br />[token.actions.githubusercontent.com/${SubPath}:actor\_id](#list_sts-token.actions.githubusercontent.com___SubPath__actor_id)<br />[token.actions.githubusercontent.com/${SubPath}:enterprise\_id](#list_sts-token.actions.githubusercontent.com___SubPath__enterprise_id)<br />[token.actions.githubusercontent.com/${SubPath}:environment](#list_sts-token.actions.githubusercontent.com___SubPath__environment)<br />[token.actions.githubusercontent.com/${SubPath}:job\_workflow\_ref](#list_sts-token.actions.githubusercontent.com___SubPath__job_workflow_ref)<br />[token.actions.githubusercontent.com/${SubPath}:ref](#list_sts-token.actions.githubusercontent.com___SubPath__ref)<br />[token.actions.githubusercontent.com/${SubPath}:repository](#list_sts-token.actions.githubusercontent.com___SubPath__repository)<br />[token.actions.githubusercontent.com/${SubPath}:repository\_id](#list_sts-token.actions.githubusercontent.com___SubPath__repository_id)<br />[token.actions.githubusercontent.com/${SubPath}:repository\_owner\_id](#list_sts-token.actions.githubusercontent.com___SubPath__repository_owner_id)<br />[token.actions.githubusercontent.com/${SubPath}:workflow](#list_sts-token.actions.githubusercontent.com___SubPath__workflow)<br />[token.actions.githubusercontent.com:actor](#list_sts-token.actions.githubusercontent.com_actor)<br />[token.actions.githubusercontent.com:actor\_id](#list_sts-token.actions.githubusercontent.com_actor_id)<br />[token.actions.githubusercontent.com:enterprise\_id](#list_sts-token.actions.githubusercontent.com_enterprise_id)<br />[token.actions.githubusercontent.com:environment](#list_sts-token.actions.githubusercontent.com_environment)<br />[token.actions.githubusercontent.com:job\_workflow\_ref](#list_sts-token.actions.githubusercontent.com_job_workflow_ref)<br />[token.actions.githubusercontent.com:ref](#list_sts-token.actions.githubusercontent.com_ref)<br />[token.actions.githubusercontent.com:repository](#list_sts-token.actions.githubusercontent.com_repository)<br />[token.actions.githubusercontent.com:repository\_id](#list_sts-token.actions.githubusercontent.com_repository_id)<br />[token.actions.githubusercontent.com:repository\_owner\_id](#list_sts-token.actions.githubusercontent.com_repository_owner_id)<br />[token.actions.githubusercontent.com:workflow](#list_sts-token.actions.githubusercontent.com_workflow)<br />[www.amazon.com:app\_id](#list_sts-www.amazon.com_app_id)<br />[www.amazon.com:user\_id](#list_sts-www.amazon.com_user_id)
  - **Access level:** Write

- **   [AssumeRoot](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html)  **
  - **Description:** Grants permission to obtain a set of temporary security credentials that you can use to perform privileged tasks in member accounts in your organization
  - **Resource types (\*required):** [root-user\*](#list_sts-resource-root-user)
  - **Condition keys:** [sts:TaskPolicyArn](#list_sts-sts_TaskPolicyArn)
  - **Access level:** Write

- **   [DecodeAuthorizationMessage](https://docs.aws.amazon.com/STS/latest/APIReference/API_DecodeAuthorizationMessage.html)  **
  - **Description:** Grants permission to decode additional information about the authorization status of a request from an encoded message returned in response to an AWS request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAccessKeyInfo](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetAccessKeyInfo.html)  **
  - **Description:** Grants permission to obtain details about the access key id passed as a parameter to the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html)  **
  - **Description:** Grants permission to obtain details about the IAM identity whose credentials are used to call the API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDelegatedAccessToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetDelegatedAccessToken.html)  **
  - **Description:** Returns temporary security credentials for accessing an AWS account after temporary delegation request approval. This API requires the tradeInToken provided upon request delegation approval and is intended to be used only by Amazon or AWS Partners
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html)  **
  - **Description:** Grants permission to obtain a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a federated user
  - **Resource types (\*required):** [federated-user](#list_sts-resource-federated-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sts-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_sts-aws_TagKeys)
  - **Access level:** Write

- **   [GetSessionToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html)  **
  - **Description:** Grants permission to obtain a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for an AWS account or IAM user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html)  **
  - **Description:** Grants permission to obtain a short-lived, publicly verifiable JSON Web Token (JWT) that represents the calling IAM principal's identity
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sts-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_sts-aws_TagKeys)<br />[sts:DurationSeconds](#list_sts-sts_DurationSeconds)<br />[sts:IdentityTokenAudience](#list_sts-sts_IdentityTokenAudience)<br />[sts:SigningAlgorithm](#list_sts-sts_SigningAlgorithm)
  - **Access level:** Write



## Permission-only actions for AWS Security Token Service
<a name="list_sts-permission-only-actions"></a>

The following actions are defined by AWS Security Token Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetServiceBearerToken](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_bearer.html)  **
  - **Description:** Grants permission to obtain a STS bearer token for an AWS root user, IAM role, or an IAM user
  - **Resource types (\*required):** 
  - **Condition keys:** [sts:AWSServiceName](#list_sts-sts_AWSServiceName)<br />[sts:DurationSeconds](#list_sts-sts_DurationSeconds)
  - **Access level:** Read

- **   [SetContext](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-sts)  **
  - **Description:** Grants permission to set context keys on a STS session
  - **Resource types (\*required):** [role](#list_sts-resource-role) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sts-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_sts-iam_ResourceTag___TagKey_)<br />[sts:RequestContext/${ContextKey}](#list_sts-sts_RequestContext___ContextKey_)<br />[sts:RequestContextProviders](#list_sts-sts_RequestContextProviders)
  - **Resource types (\*required):** [self-session](#list_sts-resource-self-session) / **Condition keys:** [sts:RequestContext/${ContextKey}](#list_sts-sts_RequestContext___ContextKey_)<br />[sts:RequestContextProviders](#list_sts-sts_RequestContextProviders)
  - **Access level:** Write

- **   [SetSourceIdentity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html#id_credentials_temp_control-access_monitor-perms)  **
  - **Description:** Grants permission to set a source identity on a STS session
  - **Resource types (\*required):** [role](#list_sts-resource-role)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sts-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_sts-iam_ResourceTag___TagKey_)<br />[sts:SourceIdentity](#list_sts-sts_SourceIdentity)
  - **Access level:** Write

- **   [TagGetWebIdentityToken](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_web_identity_token_tags.html)  **
  - **Description:** Grants permission to add tags to the JSON Web Token (JWT) generated by the GetWebIdentityToken API
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sts-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_sts-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagSession](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html)  **
  - **Description:** Grants permission to add tags to a STS session
  - **Resource types (\*required):** [role](#list_sts-resource-role)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sts-aws_TagKeys)<br />[iam:ResourceTag/${TagKey}](#list_sts-iam_ResourceTag___TagKey_)<br />[saml:aud](#list_sts-saml_aud)<br />[sts:TransitiveTagKeys](#list_sts-sts_TransitiveTagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Security Token Service
<a name="list_sts-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [context-provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns)  | arn:${Partition}:iam::aws:contextProvider/${ContextProviderName} |   | 
|  [federated-user](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns)  | arn:${Partition}:sts::${Account}:federated-user/${FederatedUserName} |   | 
|  [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)  | arn:${Partition}:iam::${Account}:role/${RoleNameWithPath} | [aws:ResourceTag/${TagKey}](#list_sts-aws_ResourceTag___TagKey_)<br />[iam:ResourceTag/${TagKey}](#list_sts-iam_ResourceTag___TagKey_) | 
|  [root-user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)  | arn:${Partition}:iam::${Account}:root |   | 
|  [self-session](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns)  | arn:${Partition}:sts::${Account}:self |   | 

## Condition keys for AWS Security Token Service
<a name="list_sts-policy-keys"></a>

AWS Security Token Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [accounts.google.com:aud](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_aud)  | Filters access by the Google application ID | String | 
|   [accounts.google.com:google/organization\_number](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Google Cloud or Google Workspace organization number | Numeric | 
|   [accounts.google.com:oaud](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_oaud)  | Filters access by the Google audience | String | 
|   [accounts.google.com:sub](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_sub)  | Filters access by the subject of the claim (the Google user ID) | String | 
|   [agent.${Domain}.buildkite.dev:build\_branch](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the git branch that triggered the Buildkite build | String | 
|   [agent.${Domain}.buildkite.dev:cluster\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite cluster ID | String | 
|   [agent.${Domain}.buildkite.dev:cluster\_name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite cluster name | String | 
|   [agent.${Domain}.buildkite.dev:organization\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite organization ID | String | 
|   [agent.${Domain}.buildkite.dev:organization\_slug](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite organization slug | String | 
|   [agent.${Domain}.buildkite.dev:pipeline\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite pipeline ID | String | 
|   [agent.${Domain}.buildkite.dev:pipeline\_slug](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite pipeline slug | String | 
|   [agent.${Domain}.buildkite.site:build\_branch](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the git branch that triggered the Buildkite build | String | 
|   [agent.${Domain}.buildkite.site:cluster\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite cluster ID | String | 
|   [agent.${Domain}.buildkite.site:cluster\_name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite cluster name | String | 
|   [agent.${Domain}.buildkite.site:organization\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite organization ID | String | 
|   [agent.${Domain}.buildkite.site:organization\_slug](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite organization slug | String | 
|   [agent.${Domain}.buildkite.site:pipeline\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite pipeline ID | String | 
|   [agent.${Domain}.buildkite.site:pipeline\_slug](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite pipeline slug | String | 
|   [agent.buildkite.com:build\_branch](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the git branch that triggered the Buildkite build | String | 
|   [agent.buildkite.com:cluster\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite cluster ID | String | 
|   [agent.buildkite.com:cluster\_name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite cluster name | String | 
|   [agent.buildkite.com:organization\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite organization ID | String | 
|   [agent.buildkite.com:organization\_slug](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite organization slug | String | 
|   [agent.buildkite.com:pipeline\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite pipeline ID | String | 
|   [agent.buildkite.com:pipeline\_slug](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the Buildkite pipeline slug | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [cognito-identity.amazonaws.com:amr](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_amr)  | Filters access by the login information for Amazon Cognito | String | 
|   [cognito-identity.amazonaws.com:aud](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_aud)  | Filters access by the Amazon Cognito identity pool ID | String | 
|   [cognito-identity.amazonaws.com:sub](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_sub)  | Filters access by the subject of the claim (the Amazon Cognito user ID) | String | 
|   [github.com/enterprises/${EnterpriseName}:actor](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the personal account that initiated the workflow run | String | 
|   [github.com/enterprises/${EnterpriseName}:actor\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the personal account that initiated the workflow run | String | 
|   [github.com/enterprises/${EnterpriseName}:enterprise\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the enterprise that contains the repository from where the workflow is running | String | 
|   [github.com/enterprises/${EnterpriseName}:environment](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the name of the environment used by the job | String | 
|   [github.com/enterprises/${EnterpriseName}:job\_workflow\_ref](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the reference path to the reusable workflow for jobs using a reusable workflow | String | 
|   [github.com/enterprises/${EnterpriseName}:ref](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the git ref (branch or tag) that triggered the workflow run | String | 
|   [github.com/enterprises/${EnterpriseName}:repository](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the repository from where the workflow is running | String | 
|   [github.com/enterprises/${EnterpriseName}:repository\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the repository from where the workflow is running | String | 
|   [github.com/enterprises/${EnterpriseName}:repository\_owner\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the repository owner from where the workflow is running | String | 
|   [github.com/enterprises/${EnterpriseName}:workflow](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the name of the workflow | String | 
|   [gitlab.com:namespace\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the GitLab namespace (group) ID of the project running the CI/CD job | String | 
|   [gitlab.com:pipeline\_source](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the source that triggered the GitLab pipeline | String | 
|   [gitlab.com:project\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the GitLab project ID running the CI/CD job | String | 
|   [gitlab.com:ref\_protected](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by whether the GitLab git ref that triggered the job is protected | String | 
|   [gitlab.com:runner\_environment](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the GitLab runner environment for the CI/CD job | String | 
|   [gitlab.com:user\_access\_level](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the GitLab user access level within the project | String | 
|   [gitlab.com:user\_email](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the GitLab user email executing the CI/CD job | String | 
|   [gitlab.com:user\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the GitLab user ID executing the CI/CD job | String | 
|   [gitlab.com:user\_login](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the GitLab username executing the CI/CD job | String | 
|   [graph.facebook.com:app\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_id)  | Filters access by the Facebook application ID | String | 
|   [graph.facebook.com:id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_id)  | Filters access by the Facebook user ID | String | 
|   [iam:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_ResourceTag)  | Filters access by the tags that are attached to the role that is being assumed | String | 
|   [idcs-${OciUniqueIdentifier}.identity.oraclecloud.com:rpst\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the OCI resource principal session token ID | String | 
|   [oidc.circleci.com/org/${OrgId}:oidc.circleci.com/project-id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the CircleCI project ID | String | 
|   [saml:aud](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_aud)  | Filters access by the endpoint URL to which SAML assertions are presented | String | 
|   [saml:cn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_cn)  | Filters access by the eduOrg attribute | ArrayOfString | 
|   [saml:commonName](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_commonname)  | Filters access by the commonName attribute | String | 
|   [saml:doc](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_doc)  | Filters access by on the principal that was used to assume the role | String | 
|   [saml:eduorghomepageuri](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_eduorghomepageuri)  | Filters access by the eduOrg attribute | ArrayOfString | 
|   [saml:eduorgidentityauthnpolicyuri](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_aud)  | Filters access by the eduOrg attribute | ArrayOfString | 
|   [saml:eduorglegalname](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_eduorglegalname)  | Filters access by the eduOrg attribute | ArrayOfString | 
|   [saml:eduorgsuperioruri](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_eduorgsuperioruri)  | Filters access by the eduOrg attribute | ArrayOfString | 
|   [saml:eduorgwhitepagesuri](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_eduorgwhitepagesuri)  | Filters access by the eduOrg attribute | ArrayOfString | 
|   [saml:edupersonaffiliation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonaffiliation)  | Filters access by the eduPerson attribute | ArrayOfString | 
|   [saml:edupersonassurance](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonassurance)  | Filters access by the eduPerson attribute | ArrayOfString | 
|   [saml:edupersonentitlement](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonentitlement)  | Filters access by the eduPerson attribute | ArrayOfString | 
|   [saml:edupersonnickname](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonnickname)  | Filters access by the eduPerson attribute | ArrayOfString | 
|   [saml:edupersonorgdn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonorgdn)  | Filters access by the eduPerson attribute | String | 
|   [saml:edupersonorgunitdn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonorgunitdn)  | Filters access by the eduPerson attribute | ArrayOfString | 
|   [saml:edupersonprimaryaffiliation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonprimaryaffiliation)  | Filters access by the eduPerson attribute | String | 
|   [saml:edupersonprimaryorgunitdn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonprimaryorgunitdn)  | Filters access by the eduPerson attribute | String | 
|   [saml:edupersonprincipalname](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonprincipalname)  | Filters access by the eduPerson attribute | String | 
|   [saml:edupersonscopedaffiliation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersonscopedaffiliation)  | Filters access by the eduPerson attribute | ArrayOfString | 
|   [saml:edupersontargetedid](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_edupersontargetedid)  | Filters access by the eduPerson attribute | ArrayOfString | 
|   [saml:givenName](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_givenname)  | Filters access by the givenName attribute | String | 
|   [saml:iss](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_iss)  | Filters access by on the issuer, which is represented by a URN | String | 
|   [saml:mail](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_mail)  | Filters access by the mail attribute | String | 
|   [saml:name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_name)  | Filters access by the name attribute | String | 
|   [saml:namequalifier](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_namequalifier)  | Filters access by the hash value of the issuer, account ID, and friendly name | String | 
|   [saml:organizationStatus](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_organizationstatus)  | Filters access by the organizationStatus attribute | String | 
|   [saml:primaryGroupSID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_primarygroupsid)  | Filters access by the primaryGroupSID attribute | String | 
|   [saml:sub](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_sub)  | Filters access by the subject of the claim (the SAML user ID) | String | 
|   [saml:sub\_type](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_subtype)  | Filters access by the value persistent, transient, or the full Format URI | String | 
|   [saml:surname](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_surname)  | Filters access by the surname attribute | String | 
|   [saml:uid](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_uid)  | Filters access by the uid attribute | String | 
|   [saml:x500UniqueIdentifier](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_x500uniqueidentifier)  | Filters access by the uid attribute | String | 
|   [sts:AWSServiceName](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_awsservicename)  | Filters access by the service that is obtaining a bearer token | String | 
|   [sts:DurationSeconds](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_durationseconds)  | Filters access by the duration in seconds when getting a bearer token or a JSON Web Token (JWT) from the GetWebIdentityToken API | Numeric | 
|   [sts:ExternalId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_externalid)  | Filters access by the unique identifier required when you assume a role in another account | String | 
|   [sts:IdentityTokenAudience](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_identitytokenaudience)  | Filters access by the audience that is passed in the request | ArrayOfString | 
|   [sts:RequestContext/${ContextKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-sts)  | Filters access by the session context key-value pairs embedded in the signed context assertion retrieved from a trusted context provider | String | 
|   [sts:RequestContextProviders](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-sts)  | Filters access by the context provider ARNs | ArrayOfARN | 
|   [sts:RoleAuthorizedByIdp](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-sts)  | Filters access based on whether the identity provider authorized the role via the roles claim in the OIDC token | Bool | 
|   [sts:RoleSessionName](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_rolesessionname)  | Filters access by the role session name required when you assume a role | String | 
|   [sts:SigningAlgorithm](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_signingalgorithm)  | Filters access by the signing algorithm that is passed in the request | String | 
|   [sts:SourceIdentity](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_sourceidentity)  | Filters access by the source identity that is passed in the request | String | 
|   [sts:TaskPolicyArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-sts)  | Filters access by TaskPolicyARN | ARN | 
|   [sts:TransitiveTagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_TransitiveTagKeys)  | Filters access by the transitive tag keys that are passed in the request | ArrayOfString | 
|   [token.actions.${Domain}.ghe.com:actor](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the personal account that initiated the workflow run | String | 
|   [token.actions.${Domain}.ghe.com:actor\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the personal account that initiated the workflow run | String | 
|   [token.actions.${Domain}.ghe.com:enterprise\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the enterprise that contains the repository from where the workflow is running | String | 
|   [token.actions.${Domain}.ghe.com:environment](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the name of the environment used by the job | String | 
|   [token.actions.${Domain}.ghe.com:job\_workflow\_ref](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the reference path to the reusable workflow for jobs using a reusable workflow | String | 
|   [token.actions.${Domain}.ghe.com:ref](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the git ref (branch or tag) that triggered the workflow run | String | 
|   [token.actions.${Domain}.ghe.com:repository](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the repository from where the workflow is running | String | 
|   [token.actions.${Domain}.ghe.com:repository\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the repository from where the workflow is running | String | 
|   [token.actions.${Domain}.ghe.com:repository\_owner\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the repository owner from where the workflow is running | String | 
|   [token.actions.${Domain}.ghe.com:workflow](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the name of the workflow | String | 
|   [token.actions.githubusercontent.com/${SubPath}:actor](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the personal account that initiated the workflow run | String | 
|   [token.actions.githubusercontent.com/${SubPath}:actor\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the personal account that initiated the workflow run | String | 
|   [token.actions.githubusercontent.com/${SubPath}:enterprise\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the enterprise that contains the repository from where the workflow is running | String | 
|   [token.actions.githubusercontent.com/${SubPath}:environment](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the name of the environment used by the job | String | 
|   [token.actions.githubusercontent.com/${SubPath}:job\_workflow\_ref](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the reference path to the reusable workflow for jobs using a reusable workflow | String | 
|   [token.actions.githubusercontent.com/${SubPath}:ref](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the git ref (branch or tag) that triggered the workflow run | String | 
|   [token.actions.githubusercontent.com/${SubPath}:repository](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the repository from where the workflow is running | String | 
|   [token.actions.githubusercontent.com/${SubPath}:repository\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the repository from where the workflow is running | String | 
|   [token.actions.githubusercontent.com/${SubPath}:repository\_owner\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the repository owner from where the workflow is running | String | 
|   [token.actions.githubusercontent.com/${SubPath}:workflow](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the name of the workflow | String | 
|   [token.actions.githubusercontent.com:actor](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the personal account that initiated the workflow run | String | 
|   [token.actions.githubusercontent.com:actor\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the personal account that initiated the workflow run | String | 
|   [token.actions.githubusercontent.com:enterprise\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the enterprise that contains the repository from where the workflow is running | String | 
|   [token.actions.githubusercontent.com:environment](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the name of the environment used by the job | String | 
|   [token.actions.githubusercontent.com:job\_workflow\_ref](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the reference path to the reusable workflow for jobs using a reusable workflow | String | 
|   [token.actions.githubusercontent.com:ref](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the git ref (branch or tag) that triggered the workflow run | String | 
|   [token.actions.githubusercontent.com:repository](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the repository from where the workflow is running | String | 
|   [token.actions.githubusercontent.com:repository\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the repository from where the workflow is running | String | 
|   [token.actions.githubusercontent.com:repository\_owner\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the ID of the repository owner from where the workflow is running | String | 
|   [token.actions.githubusercontent.com:workflow](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif)  | Filters access by the name of the workflow | String | 
|   [www.amazon.com:app\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_id)  | Filters access by the Login with Amazon application ID | String | 
|   [www.amazon.com:user\_id](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_id)  | Filters access by the Login with Amazon user ID | String | 