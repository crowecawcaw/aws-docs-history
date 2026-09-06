

# AWS Agent Registry and AWS Organizations
<a name="services-that-can-integrate-agent-registry"></a>

AWS Agent Registry is a fully managed discovery service. It provides a centralized catalog for organizing, curating, and discovering resources across your organization. With AWS Agent Registry, you can publish Model Context Protocol (MCP) servers, tools, agents, agent skills, and custom resources into a searchable registry. You can control access through an approval workflow. Both human users and AI agents can then discover the right tools and agents through hybrid search, catalog browsing, and a native MCP endpoint.

With AWS Agent Registry, you can automatically discover and catalog supported resources (currently Amazon Bedrock AgentCore Runtimes and Gateways) across member accounts, giving you a single organization-wide catalog with no per-account setup. The catalog stays in sync as resources and accounts change, and detection is fully managed with nothing to install in member accounts. For more information, see [Using AWS Agent Registry with AWS Organizations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-organizations.html) in the *Amazon Bedrock AgentCore Developer Guide*.

Use the following information to help you integrate AWS Agent Registry with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-agent-registry"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows AWS Agent Registry to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between AWS Agent Registry and Organizations, or if you remove the member account from the organization.

For more information, see [Using service-linked roles for AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-service-linked-role-agent-registry.html) in the *Amazon Bedrock AgentCore Developer Guide*.
+ `AWSServiceRoleForAgentRegistry` – Allows AWS Agent Registry to access AWS services and resources used or managed by AWS Agent Registry on your behalf.

## Service principals used by AWS Agent Registry
<a name="integrate-enable-svcprin-agent-registry"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by AWS Agent Registry grant access to the following service principals:
+ `agent-registry.amazonaws.com`

## Enabling trusted access with AWS Agent Registry
<a name="integrate-enable-ta-agent-registry"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

When you grant trusted access for AWS Agent Registry to your AWS Organization, the service gains permission to create AWS Config service-linked configuration recorders in member accounts. These recorders obtain information about active resources and notify AWS Agent Registry of create, update, and delete events. AWS Agent Registry then creates, updates, or deletes registry records according to these events using the credentials of the registry owner.

You can enable trusted access using either the AWS Agent Registry console or the AWS Organizations console.

**Important**  
We strongly recommend that whenever possible, you use the AWS Agent Registry console or tools to enable integration with Organizations. This lets AWS Agent Registry perform any configuration that it requires, such as creating resources needed by the service. Proceed with these steps only if you can’t enable integration using the tools provided by AWS Agent Registry. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration).   
If you enable trusted access by using the AWS Agent Registry console or tools then you don’t need to complete these steps.

To enable trusted access from the AWS Agent Registry console, see [Using AWS Agent Registry with AWS Organizations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-organizations.html) in the *Amazon Bedrock AgentCore Developer Guide*.

You can enable trusted access by using either the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To enable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Agent Registry** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for AWS Agent Registry** dialog box, type **enable** to confirm, and then choose **Enable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Agent Registry that they can now enable that service to work with AWS Organizations from the service console.

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the OrganizationsCLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Agent Registry as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \ 
      --service-principal agent-registry.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access
<a name="integrate-disable-ta-agent-registry"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

To disable trusted access from the AWS Agent Registry console, see [Using AWS Agent Registry with AWS Organizations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-organizations.html) in the *Amazon Bedrock AgentCore Developer Guide*. All delegated administrators must be removed before you can disable trusted access.

You can disable trusted access using either the AWS Agent Registry or the AWS Organizations tools.

**Important**  
We strongly recommend that whenever possible, you use the AWS Agent Registry console or tools to disable integration with Organizations. This lets AWS Agent Registry perform any clean up that it requires, such as deleting resources or access roles that are no longer needed by the service. Proceed with these steps only if you can’t disable integration using the tools provided by AWS Agent Registry.  
If you disable trusted access by using the AWS Agent Registry console or tools then you don’t need to complete these steps.

You can disable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Agent Registry as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal agent-registry.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for AWS Agent Registry
<a name="integrate-enable-da-agent-registry"></a>

A delegated administrator for AWS Agent Registry can create and manage registries with organization-wide auto-detection on behalf of the organization, without using the management account. For more information, see [Using AWS Agent Registry with AWS Organizations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-organizations.html) in the *Amazon Bedrock AgentCore Developer Guide*.

**Minimum permissions**  
Only an administrator in the Organizations management account can configure a delegated administrator for AWS Agent Registry.

------
#### [ AWS CLI, AWS API ]

You can register a delegated administrator account using the AWS CLI or one of the AWS SDKs:
+ AWS CLI: [register-delegated-administrator](https://docs.aws.amazon.com/cli/latest/reference/organizations/register-delegated-administrator.html)

  ```
  $ aws organizations register-delegated-administrator \
      --account-id {{ACCOUNT_ID}} \
      --service-principal agent-registry.amazonaws.com
  ```
+ AWS API: [RegisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html)

------

## Disabling a delegated administrator account for AWS Agent Registry
<a name="integrate-disable-da-agent-registry"></a>

Only an administrator in the Organizations management account can remove a delegated administrator account from the organization. You can remove a delegated administrator using the AWS Agent Registry console, or by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation. To remove a delegated administrator using the AWS Agent Registry console, see [Using AWS Agent Registry with AWS Organizations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-organizations.html) in the *Amazon Bedrock AgentCore Developer Guide*.

------
#### [ AWS CLI, AWS API ]

You can remove a delegated administrator account using the AWS CLI or one of the AWS SDKs:
+ AWS CLI: [deregister-delegated-administrator](https://docs.aws.amazon.com/cli/latest/reference/organizations/deregister-delegated-administrator.html)

  ```
  $ aws organizations deregister-delegated-administrator \
      --account-id {{ACCOUNT_ID}} \
      --service-principal agent-registry.amazonaws.com
  ```
+ AWS API: [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html)

------