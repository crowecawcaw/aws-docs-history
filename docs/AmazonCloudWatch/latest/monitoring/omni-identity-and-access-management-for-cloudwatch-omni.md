

# Identity and access management for CloudWatch Omni
<a name="omni-identity-and-access-management-for-cloudwatch-omni"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use CloudWatch Omni resources. IAM is an AWS service that you can use with no additional charge.

CloudWatch Omni uses the Amazon CloudWatch identity. Actions are in the `cloudwatch` namespace and requests are signed with the `cloudwatch` Signature Version 4 signing name. The endpoint prefix differs from the signing name: requests go to `cloudwatch-omni.{region}.api.aws` but sign as `cloudwatch`.

**Topics**
+ How CloudWatch Omni works with IAM
+ Domains and spaces
+ AWS managed policies
+ Service roles used for setup
+ Tag-based access control
+ Telemetry ingestion identity
+ Read-time access scope
+ Space-level access control
+ Troubleshooting identity and access

**How CloudWatch Omni works with IAM**


| IAM feature | CloudWatch Omni support | 
| --- | --- | 
| Resource-based policies | No | 
| Policy actions | Yes | 
| Policy resources | Yes | 
| Policy condition keys (service-specific) | Yes | 
| ACLs | No | 
| ABAC (tags in policies) | Partial | 
| Temporary credentials | Yes | 
| Forward access sessions | Yes | 
| Service roles | Yes | 
| Service-linked roles | Yes | 

To get a high-level view of how CloudWatch Omni and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Resource-based policies.** CloudWatch Omni does not support resource-based policies. Space membership and access grants control fine-grained access within a space instead. See [Control access to your space](omni-control-access-to-your-space.md) and [Access profiles](omni-access-profiles.md).

**Policy actions.** Administrators can use AWS JSON policies to specify who has access to what: which principal can perform actions on which resources, and under what conditions. To see the list of CloudWatch Omni actions, see the *Service Authorization Reference*.

**Policy resources.** CloudWatch Omni supports the following resource types in policies:

`access-grant`, `access-profile`, `alert`, `dataset`, `domain`, `integration`, `omni-dashboard`, `space`, and `view`.

Domains and access grants that are scoped to an organization use the `organization-domain` and `organization-access-grant` resource types.

**Policy condition keys.** CloudWatch Omni supports the tag-based condition keys `aws:RequestTag/*` and `aws:TagKeys` on the operations that create a taggable resource, and `aws:ResourceTag/*` on tagged resources. See the "Tag-based access control" section of this page.

**ACLs.** Access control lists control which principals have permissions to access a resource. CloudWatch Omni does not support ACLs.

**Attribute-based access control.** Attribute-based access control (ABAC) defines permissions based on attributes, which in AWS are tags. CloudWatch Omni supports applying tags when you create a resource, and supports the tag-based condition keys.

**Temporary credentials.** CloudWatch Omni works with temporary credentials, and requests are signed with Signature Version 4. You can sign in with IAM Identity Center or with IAM. In both cases, CloudWatch Omni issues credentials that are scoped to the space you are working in.

**Forward access sessions.** When you run a telemetry query, CloudWatch Omni uses forward access session credentials to read your telemetry on your behalf, so the read is authorized as you rather than as the service. See [Data encryption in CloudWatch Omni](omni-data-encryption-in-cloudwatch-omni.md) for how those credentials are protected.

**Service roles.** CloudWatch Omni uses IAM roles that it assumes to read your telemetry and to operate on your resources. It creates most of them for you, and accepts a role that you supply for an organization domain and for agent evaluations. See the "Service roles used for setup" section of this page.

**Service-linked roles.** CloudWatch Omni uses a service-linked role, `AWSServiceRoleForCloudWatch_Omni`, which carries the `AWSCloudWatchOmniServiceRolePolicy` managed policy. It assumes that role to create the setup roles it manages in your account, and to attach their policies.

**Domains and spaces**

A *domain* and a *space* are distinct resources. A domain is the identity and federation boundary, and single sign-on is configured for each domain. A space is the top-level container for observability data within a domain, with the resource type `space` and the ARN form `space/{spaceId}`.

**AWS managed policies**

The space operator role carries `CloudWatchOmniSpaceAccessPolicy` as its base policy, and can also carry two optional policies chosen during setup: `CloudWatchOmniModelInferencePolicy` (described below) and `CloudWatchOmniAWSIntegrationPolicy`, which lets CloudWatch Omni discover resources and their relationships for Context Graph. CloudWatch Omni provides further managed policies for other roles, including `CloudWatchOmniDomainAccessPolicy` for organization domain administration. For the complete set and each policy's contents, see [AWS managed policies for CloudWatch Omni](omni-aws-managed-policies-for-cloudwatch-omni.md).


| Managed policy | What it grants | When it is attached | 
| --- | --- | --- | 
| CloudWatchOmniSpaceAccessPolicy | The space experience — space and access-grant management, telemetry queries, the context graph, alerts, dashboards, access profiles, views, threads, and integrations — together with evaluation management. It also carries the supporting permissions those need in other services, including CloudWatch Logs, AWS KMS, and Secrets Manager. | Always. This is the base policy. | 
| CloudWatchOmniModelInferencePolicy | Model inference only: invoking foundation models and inference profiles in Amazon Bedrock, including streaming responses, and invoking models served through Amazon Bedrock Mantle. It grants nothing else. | Only for spaces that use the prompt playground or run evaluations with custom evaluators. A view-only space does not receive it. | 

Keeping inference in its own policy means that a space can set up and view its evaluation configuration without holding permission to invoke a model. Only running a model requires the second policy.

When the CloudWatch Omni service-linked role creates the space operator role, it applies `CloudWatchOmniSpaceAccessPolicy` as the role's permissions boundary, which caps the role's effective permissions to that same set.

For what each policy grants action by action, the permissions that read metadata across your whole account, and the permissions you must provide yourself, see [IAM policies to use CloudWatch Omni](omni-iam-policies-to-use-cloudwatch-omni.md).

**Service roles used for setup**

Setup uses several IAM roles, and CloudWatch Omni creates most of them for you. When you enable a capability, the service assumes its service-linked role and creates the role in your account with the matching AWS managed policy attached. Two roles are yours to create and pass in: the domain access role for an organization domain, and the evaluation execution role for online agent evaluations. You can also supply your own space operator role instead of letting CloudWatch Omni create one.


| Role | Purpose | Created by | Required | 
| --- | --- | --- | --- | 
| CloudWatchOmniOperatorRole | The space operator role, which is the primary setup and data-access role. It carries the CloudWatch Omni actions along with the Amazon Bedrock, AWS KMS, AWS Config, Secrets Manager, CloudWatch Logs, and iam:PassRole permissions that setup and evaluation require. One role per account, shared by every space in it. In the API it is the dataAccessRoleArn parameter. | CloudWatch Omni, or you | Required | 
| CloudWatchOmniDomainAccessRole | Domain access. You pass its ARN when you create a domain for your organization. | You | Required for an organization domain | 
| CloudWatchOmniIntegrationEnablementRole | Enabling telemetry integrations for your account. One role per member account. | CloudWatch Omni | Required for integrations | 
| CloudWatchOmniDatasetIntegrationExecutionRole | Dataset integration. Assumed by logs.amazonaws.com, and restricted to dataset integrations in your own account. | CloudWatch Omni | Required for dataset integration | 
| AgentCoreEvaluationRole | Execution role for online agent evaluations. You pass its ARN when you create or update a space. | You | Optional. You can opt out, or point to an existing role. | 

**Required** means the role must exist for that capability to work, not that you have to create it yourself.

The operator role trusts the CloudWatch Omni service principal `cloudwatch.amazonaws.com`. For the trust policies that setup uses, see [Cross-service confused deputy prevention](omni-cross-service-confused-deputy-prevention.md).

Several operations take a role ARN that you supply, including your own operator role, the domain access role, and the evaluation execution role. Your calling principal needs `iam:PassRole` for the role you pass.

**Tag-based access control**

CloudWatch Omni supports tags on 11 resource types: `space`, `domain`, `organization-domain`, `access-grant`, `organization-access-grant`, `access-profile`, `omni-dashboard`, `alert`, `view`, `integration`, and `dataset`. You cannot tag any other CloudWatch resource through CloudWatch Omni.

Eight of these accept tags at creation: `space`, `domain`, `organization-domain`, `access-grant`, `organization-access-grant`, `access-profile`, `omni-dashboard`, and `alert`. For these, you can use `aws:RequestTag/*` and `aws:TagKeys` in your policies to control what a principal is allowed to create.

The remaining three (`view`, `integration`, and `dataset`) are tagged after they exist, so the request-tag condition keys do not apply to them.

You can use `aws:ResourceTag/*` to control access to any tagged resource.

**Telemetry ingestion identity**

CloudWatch Omni supports two ways to authenticate telemetry ingestion. Which ones are available depends on the signal.

1. **Signature Version 4 with an IAM role.** Sign OTLP ingestion requests with Signature Version 4 using temporary role credentials. This is the recommended approach, and it is the only approach available for all three signals.

1. **A bearer token.** For clients that cannot sign with Signature Version 4, you can use an IAM service-specific credential on a dedicated IAM user. This is available for **metrics and logs only.**

Traces have no bearer-token path. The X-Ray OTLP endpoint accepts Signature Version 4 only, so a client that sends traces must sign.

For metrics and logs, you create an API key from CloudWatch settings in the console. The console creates a dedicated IAM user with the `CloudWatchAPIKeyAccess` managed policy and issues the bearer token as a service-specific credential on that user. For the published setup steps, see [Bearer token authentication for OTLP metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLP-MetricsBearerTokenAuth.html) in the *Amazon CloudWatch User Guide* and [OTLP endpoints for CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_HTTP_Endpoints_OTLP.html) in the *Amazon CloudWatch Logs User Guide*.

You create and manage API keys and their credentials in the CloudWatch console using your own IAM permissions. CloudWatch Omni itself can list them but cannot create, rotate, or delete them.

For credential hygiene guidance, see [Security best practices for CloudWatch Omni](omni-security-best-practices-for-cloudwatch-omni.md).

**Read-time access scope**

A member's grant controls what their queries and views return. CloudWatch Omni applies the scope when it runs the query. To set it, see [Limit what members can see](omni-limit-what-members-can-see.md).

**The scope constrains the telemetry query path.** Other features can reach the same content, so grant their permissions with that in mind. See [Security best practices for CloudWatch Omni](omni-security-best-practices-for-cloudwatch-omni.md).

**Space-level access control**

IAM controls who can reach CloudWatch Omni and what the service may do in your account. Access to the contents of a space is a second, separate decision, evaluated inside the space. Both apply to every request.
+ **The member's permission level** decides whether a principal may ask for an operation. A grant carries one of four levels: Viewer, Editor, Space Admin, or Custom, where Custom allows exactly the actions it lists.
+ **The space operator role** decides whether the space may carry that operation out against your AWS resources. Raising a member to Space Admin adds no permission that this role does not already hold, so the role is the ceiling for everything in the space. One operator role serves every space in the account, so that ceiling is account-wide. You cannot separate two spaces from each other by giving them different operator roles.

For an audit, the properties that follow from that design:
+ **Grants only add.** A principal's effective access is the union of every grant it holds, directly and through groups. For the tiered levels the highest one wins, and a Custom grant adds the actions it names. There are no explicit denies, so you cannot subtract access from a principal by adding a grant. You remove the grant that provides the access. Action scopes narrow only the actions they name, so they do not turn a tiered level into an exact allowlist. See [Custom grant actions](omni-custom-grant-actions.md).
+ **Read scope is row-level and enforced at read time.** A grant can carry a data scope that filters telemetry rows on the query path, before results reach the member. It filters rows, not fields: a member who can see a record sees every field on it.
+ **A data scope on one grant does not narrow another.** A second grant without a scope restores the full view, including a grant inherited through a group.
+ **Space administration is reserved for people.** An access profile, which is the identity a resource such as an alert uses when no one is signed in, can hold Viewer, Editor, or Custom, never Space Admin, and can never exceed the space operator role.
+ **A space always retains at least one Space Admin.** The grant that provides the last Space Admin access cannot be deleted, and no principal can edit or delete its own grants.
+ **Some grants are created by the service.** Those are marked service managed and cannot be edited or deleted.

To review or change any of this, see [Control access to your space](omni-control-access-to-your-space.md) for the model, [Manage space members and permissions](omni-manage-space-members-and-permissions.md) for the members and grants surface, [Limit what members can see](omni-limit-what-members-can-see.md) for data scopes, and [Access profiles](omni-access-profiles.md) for resource identities.

**Troubleshooting identity and access**

A `403` response with `AccessDeniedException` indicates that the calling principal is not authorized, or that the request signature did not validate. Confirm which identity the request is using with `aws sts get-caller-identity`, and confirm that the identity holds an active access grant in the space. A sign-in problem, such as an expired one-time code, returns a `400` rather than a `403`.

For signing telemetry ingestion requests from an OpenTelemetry exporter, see [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).