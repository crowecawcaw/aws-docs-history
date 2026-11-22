

# IAM Permissions

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

## Registry actions
<a name="registry-iam-actions"></a>

This section describes the IAM actions for AWS Agent Registry and the AWS managed policies that grant full or read-only access.

To create, manage, or use registries, attach an identity-based policy to your AWS Identity and Access Management (IAM) identity that allows it to perform [AWS Agent Registry-related actions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonagentregistry.html). For comprehensive permissions, you can use the [AgentRegistryFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AgentRegistryFullAccess.html) managed policy. For details about the full access policy, see [AWS managed policy: AgentRegistryFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AgentRegistryFullAccess). For read-only access, you can use the [AgentRegistryReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AgentRegistryReadOnlyAccess.html) managed policy. For details about the read-only policy, see [AWS managed policy: AgentRegistryReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AgentRegistryReadOnlyAccess).

For greater security and control, you can create your own custom policy by reducing the permissions in the full access policy.

**Note**  
In the `bedrock-agentcore` namespace, the actions listed below are covered by the `BedrockAgentCoreFullAccess` managed policy. In the `agent-registry` namespace, they are covered by the new `AgentRegistryFullAccess` managed policy. Each table below shows both namespaces during the migration window. For the complete migration mapping, see [Comprehensive registry migration guide](registry-faq.md).

## Registry control plane actions
<a name="registry-iam-control-plane"></a>

**Example**  


| Action | Description | Access level | 
| --- | --- | --- | 
|  `agent-registry:CreateRegistry`  | Grants permission to create a registry | Write | 
|  `agent-registry:GetRegistry`  | Grants permission to get a registry | Read | 
|  `agent-registry:UpdateRegistry`  | Grants permission to update a registry | Write | 
|  `agent-registry:DeleteRegistry`  | Grants permission to delete a registry | Write | 
|  `agent-registry:ListRegistries`  | Grants permission to list registries | List | 


| Action | Description | Access level | 
| --- | --- | --- | 
|  `bedrock-agentcore:CreateRegistry`  | Grants permission to create a registry | Write | 
|  `bedrock-agentcore:GetRegistry`  | Grants permission to get a registry | Read | 
|  `bedrock-agentcore:UpdateRegistry`  | Grants permission to update a registry | Write | 
|  `bedrock-agentcore:DeleteRegistry`  | Grants permission to delete a registry | Write | 
|  `bedrock-agentcore:ListRegistries`  | Grants permission to list registries | List | 

## Registry record control plane actions
<a name="registry-iam-record-control-plane"></a>

**Example**  


| Action | Description | Access level | 
| --- | --- | --- | 
|  `agent-registry:CreateRegistryRecord`  | Grants permission to create a registry record | Write | 
|  `agent-registry:GetRegistryRecord`  | Grants permission to get a registry record | Read | 
|  `agent-registry:UpdateRegistryRecord`  | Grants permission to update a registry record | Write | 
|  `agent-registry:DeleteRegistryRecord`  | Grants permission to delete a registry record | Write | 
|  `agent-registry:ListRegistryRecords`  | Grants permission to list registry records | List | 
|  `agent-registry:SubmitRegistryRecordForApproval`  | Grants permission to submit a registry record for approval | Write | 
|  `agent-registry:UpdateRegistryRecordStatus`  | Grants permission to approve, reject, or deprecate a registry record | Write | 
|  `agent-registry:CompleteRegistryRecordTokenAuth`  | Grants permission to complete a user-delegated OAuth authorization that records in a registry are waiting on. The AWS Agent Registry console uses it to complete GitHub authorization for skill records; you don’t call it directly. Requires `bedrock-agentcore:CompleteResourceTokenAuth`. See [Permissions for a GitHub source](#registry-iam-skills-github). | Write | 


| Action | Description | Access level | 
| --- | --- | --- | 
|  `bedrock-agentcore:CreateRegistryRecord`  | Grants permission to create a registry record | Write | 
|  `bedrock-agentcore:GetRegistryRecord`  | Grants permission to get a registry record | Read | 
|  `bedrock-agentcore:UpdateRegistryRecord`  | Grants permission to update a registry record | Write | 
|  `bedrock-agentcore:DeleteRegistryRecord`  | Grants permission to delete a registry record | Write | 
|  `bedrock-agentcore:ListRegistryRecords`  | Grants permission to list registry records | List | 
|  `bedrock-agentcore:SubmitRegistryRecordForApproval`  | Grants permission to submit a registry record for approval | Write | 
|  `bedrock-agentcore:UpdateRegistryRecordStatus`  | Grants permission to approve, reject, or deprecate a registry record | Write | 

## Registry data plane actions
<a name="registry-iam-data-plane"></a>

**Example**  


| Action | Description | Access level | 
| --- | --- | --- | 
|  `agent-registry:SearchDiscoverableRegistryRecords`  | Grants permission to search approved registry records | Read | 
|  `agent-registry:ListDiscoverableRegistryRecords`  | Grants permission to list approved registry records | List | 
|  `agent-registry:GetDiscoverableRegistryRecord`  | Grants permission to retrieve an approved registry record. Also authorizes `BatchGetDiscoverableRegistryRecord`. | Read | 
|  `agent-registry:InvokeRegistryMcp`  | Grants permission to invoke the registry MCP endpoint | Read | 


| Action | Description | Access level | 
| --- | --- | --- | 
|  `bedrock-agentcore:SearchRegistryRecords`  | Grants permission to search registry records | Read | 
|  `bedrock-agentcore:InvokeRegistryMcp`  | Grants permission to invoke the registry MCP endpoint | Read | 

**Note**  
For invoking the registry MCP endpoint, you need both the search action and the `InvokeRegistryMcp` action. In the `agent-registry` namespace, the search action is `agent-registry:SearchDiscoverableRegistryRecords`; in the `bedrock-agentcore` namespace it is `bedrock-agentcore:SearchRegistryRecords`.

**Note**  
 `BatchGetDiscoverableRegistryRecord` does not have its own IAM action. Each requested record is authorized against `agent-registry:GetDiscoverableRegistryRecord`. Grant `GetDiscoverableRegistryRecord` to use `BatchGetDiscoverableRegistryRecord`.

### Record-level permissions and the discovery APIs
<a name="registry-iam-record-level-discovery"></a>

You can use an `Allow` or `Deny` statement to scope `agent-registry:GetDiscoverableRegistryRecord` to individual registry record ARNs. Only `BatchGetDiscoverableRegistryRecord` enforces that scope because it checks each requested record.

 AWS Agent Registry authorizes `SearchDiscoverableRegistryRecords` and `ListDiscoverableRegistryRecords` at the registry level only. These APIs don’t evaluate `GetDiscoverableRegistryRecord`. They ignore record-level `Allow` and `Deny` statements. A caller who can search or list a registry can discover every approved record in it. This includes records that you deny the caller through a `GetDiscoverableRegistryRecord` policy.

The same applies to the search and list tools on the registry’s MCP endpoint.

Search and list never return skill packages. Only `GetRegistryRecord`, `BatchGetDiscoverableRegistryRecord`, and the batch get tool on the registry’s MCP endpoint return a skill package download URL. `GetRegistryRecord` is authorized on the record, and the other two authorize each record against `GetDiscoverableRegistryRecord`. A record-level `Deny` therefore also keeps the denied caller from getting that record’s package.

## Permissions for skill packages and skill synchronization
<a name="registry-iam-skills"></a>

Uploading, synchronizing, and downloading skill packages don’t have IAM actions of their own. They use the record actions: `CreateRegistryRecord` and `UpdateRegistryRecord` to upload a package or to set or synchronize a skill source, and `GetRegistryRecord` and `GetDiscoverableRegistryRecord` to get a download URL. Depending on where the skill content comes from, the caller also needs permissions in other services. For an overview of skill packages, see [Publish skill packages](registry-skill-packages.md).

### Publisher permissions
<a name="registry-iam-skills-publisher"></a>

The following table lists what a publisher needs, by how the skill content is provided.


| Content source |  AWS Agent Registry actions | Other permissions | 
| --- | --- | --- | 
| Upload a package |  `agent-registry:CreateRegistryRecord` on the registry, or `agent-registry:UpdateRegistryRecord` on the record | For a registry encrypted with a customer managed key, the KMS permissions in [Permissions for registries encrypted with a customer managed key](#registry-iam-skills-kms). | 
| Synchronize from Amazon S3 |  `agent-registry:CreateRegistryRecord` on the registry, or `agent-registry:UpdateRegistryRecord` on the record |  `iam:PassRole` on the source’s IAM role, when the request includes a source with an IAM role. See [Pass the IAM role of an Amazon S3 source](#registry-iam-skills-s3). For a registry encrypted with a customer managed key, the KMS permissions in [Permissions for registries encrypted with a customer managed key](#registry-iam-skills-kms). | 
| Synchronize from GitHub |  `agent-registry:CreateRegistryRecord` on the registry, or `agent-registry:UpdateRegistryRecord` on the record. To complete the GitHub authorization in the console, also `agent-registry:CompleteRegistryRecordTokenAuth` on the registry. | AgentCore Identity and AWS Secrets Manager permissions. See [Permissions for a GitHub source](#registry-iam-skills-github). For a registry encrypted with a customer managed key, the KMS permissions in [Permissions for registries encrypted with a customer managed key](#registry-iam-skills-kms). | 

 `triggerSynchronization` and `forceAuthentication` are members of the `UpdateRegistryRecord` request and need no other AWS Agent Registry action.

#### Pass the IAM role of an Amazon S3 source
<a name="registry-iam-skills-s3"></a>

When a request includes an Amazon S3 source with the IAM role that AWS Agent Registry assumes to read it, the caller needs `iam:PassRole` on that role, even if the request sends the record’s stored role unchanged. AWS Agent Registry passes the role to the `agent-registry.amazonaws.com` service principal, for a record in the registry. On `CreateRegistryRecord`, the associated resource is `arn:aws:agent-registry:<region>:<account>:registry/<registryId>/record/*`; on `UpdateRegistryRecord`, it’s the record’s ARN. A condition that names a single record ARN therefore fails on `CreateRegistryRecord`, so use a record ARN pattern:

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowPassSkillSourceRole",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::111122223333:role/SkillSourceReadRole",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "agent-registry.amazonaws.com"
        },
        "StringLike": {
          "iam:AssociatedResourceARN": "arn:aws:agent-registry:us-east-1:111122223333:registry/*/record/*"
        }
      }
    }
  ]
}
```
+ The role must be in the caller’s account, even when the registry is shared with the caller’s account. Otherwise, the request fails with an `AccessDeniedException` and the message `Cross-account pass role is not allowed`.
+ An `UpdateRegistryRecord` request that only sets `triggerSynchronization` and keeps the stored role passes no role and needs no `iam:PassRole`.
+ A source with no credential provider (a public object) passes no role.

For the role’s trust policy and permissions, see [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md).

#### Permissions for a GitHub source
<a name="registry-iam-skills-github"></a>

A GitHub source reads the repository with the access that a GitHub user authorizes through an AgentCore Identity OAuth 2.0 credential provider. When a request sets or synchronizes a GitHub source, AWS Agent Registry calls AgentCore Identity with the caller’s credentials, through [Forward Access Sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) (FAS). The caller must be an IAM role or IAM user in the account that owns the registry, and needs the following permissions:
+  `bedrock-agentcore:GetWorkloadAccessTokenForUserId` on the registry’s workload identity, `registry-<registryId>`, and its workload identity directory.
+  `bedrock-agentcore:GetResourceOauth2Token` on the registry’s workload identity and its directory, the token vault, and the credential provider.
+  `secretsmanager:GetSecretValue` on the secret in which AgentCore Identity stores the credential provider’s client secret. AgentCore Identity reads it with the caller’s credentials.

To complete the GitHub authorization in the AWS Agent Registry console, the IAM role or user that started the authorization also needs the following permissions. The console completes the authorization with the credentials that you are signed in with, so sign in as the same IAM role or user.
+  `agent-registry:CompleteRegistryRecordTokenAuth` on the registry.
+  `bedrock-agentcore:CompleteResourceTokenAuth` on the registry’s workload identity and its directory, the token vault, and the credential provider.

If the record sets a `returnUrl`, your application completes the authorization instead, by calling the AgentCore Identity `CompleteResourceTokenAuth` operation. The IAM principal that your application uses must be in the account that owns the registry, and needs the following permissions:
+  `bedrock-agentcore:CompleteResourceTokenAuth` on the same resources.
+  `secretsmanager:GetSecretValue` on the secret in which AgentCore Identity stores the credential provider’s client secret. AgentCore Identity reads it with your application’s credentials when it completes the authorization.

For more information, see [Synchronize a skill from GitHub](registry-skill-sync-github.md).

The following example policy grants these permissions for one credential provider. Replace the Region, the account ID, and {{my-github-provider}} with your values.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowRegistryWorkloadAccessToken",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetWorkloadAccessTokenForUserId",
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:workload-identity-directory/default/workload-identity/registry-*"
      ]
    },
    {
      "Sid": "AllowGitHubTokenAndAuthorizationCompletion",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GetResourceOauth2Token",
        "bedrock-agentcore:CompleteResourceTokenAuth"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:workload-identity-directory/default/workload-identity/registry-*",
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:token-vault/default",
        "arn:aws:bedrock-agentcore:us-east-1:111122223333:token-vault/default/oauth2credentialprovider/my-github-provider"
      ]
    },
    {
      "Sid": "AllowGitHubProviderClientSecret",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:us-east-1:111122223333:secret:bedrock-agentcore-identity!default/oauth2/my-github-provider-*"
    },
    {
      "Sid": "AllowConsoleGitHubAuthorization",
      "Effect": "Allow",
      "Action": "agent-registry:CompleteRegistryRecordTokenAuth",
      "Resource": "arn:aws:agent-registry:us-east-1:111122223333:registry/*"
    }
  ]
}
```

**Note**  
Scope `GetResourceOauth2Token` and `secretsmanager:GetSecretValue` to the credential providers that the caller uses for GitHub sources. A wildcard in the provider name grants access to every OAuth 2.0 credential provider in the account.

The [AgentRegistryFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AgentRegistryFullAccess.html) managed policy includes the permissions that GitHub sources need:
+  `bedrock-agentcore:GetWorkloadAccessTokenForUserId`, `bedrock-agentcore:GetResourceOauth2Token`, and `bedrock-agentcore:CompleteResourceTokenAuth`, including on `token-vault/default`, in the `AllowGetResourceOauth2TokenForOauthBasedSynchronization` statement.
+  `secretsmanager:GetSecretValue`.
+  `agent-registry:*`, which covers `agent-registry:CompleteRegistryRecordTokenAuth`.

If you write your own policy, grant the permissions in this section instead.

To create a credential provider for github.com, see [GitHub](identity-idp-github.md) in the AgentCore Identity documentation. For GHE.com or GitHub Enterprise Server, see [Add OAuth client using custom provider](identity-add-oauth-client-custom.md).

### Consumer permissions
<a name="registry-iam-skills-consumer"></a>

A consumer gets a skill package through a download URL that AWS Agent Registry returns with the record:
+  **Control plane** — `agent-registry:GetRegistryRecord` on the record. `GetRegistryRecord` returns the package of the record’s latest revision, including a revision in `DRAFT` status.
+  **Data plane** — `agent-registry:GetDiscoverableRegistryRecord` on each requested record, for `BatchGetDiscoverableRegistryRecord` and for the batch get tool on the registry’s MCP endpoint. These return the package of the record’s approved revision only. For the MCP endpoint, the caller also needs the actions in [Registry data plane actions](#registry-iam-data-plane).

Record-level `Allow` and `Deny` statements on these actions also apply to the package. For more information, see [Record-level permissions and the discovery APIs](#registry-iam-record-level-discovery).

The download URL is a presigned Amazon S3 URL that is valid for up to 5 minutes. Anyone who has the URL can download the package until it expires, without AWS credentials or permissions. Removing a caller’s permissions doesn’t revoke URLs that were already returned. For more information, see [Download a skill package](registry-skill-package-download.md).

### Permissions for registries encrypted with a customer managed key
<a name="registry-iam-skills-kms"></a>

If the registry is encrypted with a customer managed key, AWS Agent Registry also checks that the caller can use the key:
+  **Publishers** need `kms:GenerateDataKey` on the key to upload a package, or to synchronize a skill package from Amazon S3 or GitHub. AWS Agent Registry checks this permission with a `GenerateDataKey` dry-run request that uses the caller’s credentials and the registry’s encryption context. A synchronization of only a `SKILL.md` makes no such request. Publishers also need `kms:Decrypt`, as for any record.
+  **Consumers** that call with IAM credentials need `kms:Decrypt` on the key to receive a download URL.
+  **Downloaders** that use a download URL need no KMS permission.

For the key policy statements, see [Set customer managed key policy](registry-kms-key-policy.md). For information about how AWS Agent Registry encrypts skill packages, see [Data encryption](registry-data-encryption.md).

## Workload identity actions (required for registry lifecycle)
<a name="registry-iam-workload-identity"></a>

The following actions are required for registry-managed workload identity operations. These actions use the `bedrock-agentcore` namespace and are called by the service on your behalf during `CreateRegistry` and `DeleteRegistry` workflows.


| Action | Description | Access level | 
| --- | --- | --- | 
|  `bedrock-agentcore:CreateWorkloadIdentity`  | Grants permission to create a workload identity for a registry | Write | 
|  `bedrock-agentcore:GetWorkloadIdentity`  | Grants permission to retrieve workload identity details (used for idempotency on retry) | Read | 
|  `bedrock-agentcore:DeleteWorkloadIdentity`  | Grants permission to delete a workload identity when a registry is deleted | Write | 

**Note**  
The `GetWorkloadIdentity` permission is required to support idempotent retries of the `CreateRegistry` workflow. Without this permission, if a registry creation is retried (for example, after a transient failure), the workflow cannot verify the existing workload identity and will fail.

A skill record that synchronizes from GitHub also uses the registry’s workload identity. For the permissions that GitHub sources need, see [Permissions for a GitHub source](#registry-iam-skills-github).

## IAM service-linked role actions (required for registry lifecycle)
<a name="registry-iam-create-service-linked-role"></a>

The following action is required during registry lifecycle management. This action uses the `iam` namespace and is called by the service on your behalf during the `CreateRegistry` workflow.


| Action | Description | Access level | 
| --- | --- | --- | 
|  `iam:CreateServiceLinkedRole`  | Grants permission to create the service-linked role for AWS Agent Registry | Write | 

**Note**  
The `CreateServiceLinkedRole` permission is required during registry creation to enable service to publish CloudWatch metrics in your account after the registry is created. Without this permission, registry creation will fail.

## Registry resource types
<a name="registry-iam-resource-types"></a>

The following resource types are defined for AWS Agent Registry:

**Example**  


| Resource type | ARN format | 
| --- | --- | 
| Registry |  `arn:aws:agent-registry:{region}:{account}:registry/{registryId}`  | 
| Registry record |  `arn:aws:agent-registry:{region}:{account}:registry/{registryId}/record/{recordId}`  | 


| Resource type | ARN format | 
| --- | --- | 
| Registry |  `arn:aws:bedrock-agentcore:{region}:{account}:registry/{registryId}`  | 
| Registry record |  `arn:aws:bedrock-agentcore:{region}:{account}:registry/{registryId}/record/{recordId}`  | 