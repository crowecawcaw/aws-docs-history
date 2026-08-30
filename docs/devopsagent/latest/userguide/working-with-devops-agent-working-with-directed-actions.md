# Working with directed actions

AWS DevOps Agent can act on your connected services and AWS accounts when an operator explicitly asks it to. For example, an operator investigating an incident can ask the agent to describe the state of a resource. With the appropriate permissions and approvals, the operator can also ask the agent to remediate an issue directly.

The agent distinguishes two kinds of operations:

- **Read-only actions**: operations that only read information from your connected services and AWS accounts. These are available by default.
- **Directed actions**: operations that create, modify, or otherwise mutate resources. Directed actions are elevated: They are disabled by default and require explicit, layered opt-in plus per-action operator approval.
  The safety model for directed actions is defense in depth. The capability is disabled by default. You opt in through independent layers: enabling directed actions on the agent space, registering a per-account IAM role, and categorizing each tool. Every directed action requires operator approval at execution time. Every approval and resulting action is attributable to the approving operator in AWS CloudTrail.

For actions against AWS resources, the agent enforces its own guardrails on the AWS SDK operations it invokes, independent of the permissions you grant. For more information about these guardrails, see [Operations the agent will not perform](#operations-the-agent-will-not-perform "#operations-the-agent-will-not-perform").

## Example: executing a mitigation plan from an investigation

This example shows the end-to-end experience for a common scenario. An operator reviews the mitigation plan of an investigation, or an improvement recommendation. The operator asks the agent to carry it out without leaving the conversation.

A site reliability engineer (SRE) asks the agent in chat to look for any accounts that allow SSH access from `0.0.0.0/0`. The agent finds a security group with an open ingress rule. It recommends a mitigation: restrict the rule to the internal network range. The operator tells the agent to apply it.

1. **The agent proposes the change.** The agent inspects the security group (a read-only action). It proposes removing the `0.0.0.0/0` rule and adding a rule scoped to the internal network range. The proposal identifies the exact API operation, the target security group, a risk assessment, the expected blast radius, and rollback steps.
2. **The operator reviews and approves.** The operation mutates a resource, so it is a directed action. The approval request shows the operation and its parameters. The operator can adjust parameters, for example narrowing `10.0.0.0/8` to `10.1.0.0/16`, or reject the request. Nothing executes without explicit approval.
3. **The agent executes under scoped credentials.** The agent uses credentials from the registered elevated role. The credentials are scoped to the approved operation and resource, and valid for a bounded window. The approval cannot be reused for a different operation or resource.
4. **The action is fully auditable.** The call appears in AWS CloudTrail with a source identity that attributes it to the approving operator. CloudTrail records the approved and executed parameters.

The same flow applies when you inspect any investigation mitigation plan or improvement recommendation and ask the agent to execute a step. The agent turns the step into a specific proposed operation and requests approval before acting.

The same flow applies to third-party tools. An operator triaging alert noise asks the agent to raise the threshold on a Grafana alert rule. AWS DevOps Agent classifies this tool as mutating, and the team enabled it for elevated access on the integration. The agent presents an approval request showing the tool and parameters. After approval, the agent invokes the tool through the integration. AWS DevOps Agent attributes the action to the approving operator.

Before directed actions are enabled, or without a registered elevated role, the agent still investigates with read-only actions. It provides manual remediation steps instead of an executable change.

## Prerequisites

Before you can use directed actions, you need the following:

- An agent space in AWS DevOps Agent with at least one association to an AWS account or supported third-party integration.
- Permissions to update the agent space and its associations, for example through the AWS DevOps Agent console or API.
- Permissions in the target account to create an IAM role and define its trust and permission policies, for directed actions against AWS accounts.
- `iam:PassRole` permission on `arn:aws:iam::<account-id>:role/*` in your own account, with the condition key `iam:PassedToService` set to `aidevops.amazonaws.com`, to register the role on the association. A broader `iam:PassRole` grant also satisfies this requirement.
- Access to the agent space for the operators who will approve directed actions.

## Enabling directed actions on an agent space

Directed actions must be enabled on the agent space before any other elevated configuration takes effect. This is the primary control for directed actions. If it is disabled, elevated role registrations and elevated tool opt-ins have no effect. Attempts to register elevated configuration might be rejected.

### Enabling in the console

1. Open the AWS DevOps Agent console.
2. Choose your agent space.
3. Navigate to the agent space settings and enable directed actions.
4. Confirm the change.

### Enabling via the API

You enable directed actions through the agent space's `preferences`. This field is a typed map of preference keys to Boolean values. You set it on `CreateAgentSpace` and `UpdateAgentSpace`.

The following example enables directed actions with the AWS CLI.

```
aws devops-agent update-agent-space \
    --agent-space-id <your-agent-space-id> \
    --preferences elevatedActionsEnabled=true
```

The `preferences` field has the following behaviors:

- Supplying `preferences` on `UpdateAgentSpace` replaces the full set, so omitted preferences revert to their defaults.
- Omitting the `preferences` field leaves current values unchanged.
- Setting `elevatedActionsEnabled` is optional, because the preference defaults to `false`.
- Supplying an unknown preference key fails with `ValidationException`.
- Changing a preference takes effect immediately and is equivalent to the console toggle.
- Calling `GetAgentSpace` returns the current `preferences` map, which confirms the setting.

## Registering an elevated role for an AWS account

For each associated AWS account, you can optionally register an _elevated role_. The monitor account and any source accounts each support an elevated role registration. An elevated role is an IAM role in your account that AWS DevOps Agent assumes to perform directed actions on your behalf. You register the role by setting `agentElevatedRoleArn` on the association's AWS configuration.

When you register an elevated role, keep the following in mind:

- Registration is optional per account. If you do not register an elevated role for an account, only read-only actions are available for that account.
- We recommend a recognizable naming convention such as `DevOpsAgent-ElevatedAction-*` so elevated roles are easy to audit. The service does not require a specific name.
- The role's permission policy is customer-managed. Scope it to the actions you want the agent to be able to take. The role defines the _ceiling_ of what the agent can ever do in your account. It is not a standing grant. Every directed action additionally requires operator approval at execution time, and the agent's session is further scoped to the specific approved operation.

### Writing the trust policy

The elevated role must trust the AWS DevOps Agent service principal. Validation exercises the assume-role path. AWS DevOps Agent uses three STS actions when it assumes the role. The trust policy must allow all three: `sts:AssumeRole`, `sts:SetSourceIdentity`, and `sts:TagSession`. If you omit `sts:SetSourceIdentity` or `sts:TagSession`, directed actions fail at credential time even when the validation status is `valid`.

The following example shows a trust policy for an elevated role. Replace `111122223333` with your AWS account ID and `us-east-1` with the AWS Region of your agent space.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:SetSourceIdentity",
        "sts:TagSession"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:aidevops:us-east-1:111122223333:agentspace/*"
        }
      }
    }
  ]
}
```

The `aws:SourceAccount` and `aws:SourceArn` conditions protect against the confused deputy problem. They ensure that the role can only be assumed on behalf of your own agent spaces. The Region in the `aws:SourceArn` condition must match the Region of your agent space. If you operate agent spaces in multiple Regions, use a Region wildcard (`arn:aws:aidevops:*:111122223333:agentspace/*`) or the specific agent space ARN.

### Granting permissions to the elevated role

The elevated role's permission policy defines the ceiling of what AWS DevOps Agent can ever do in your account through directed actions. The agent never operates at this ceiling. Every directed action requires operator approval. The credentials issued for an approved action carry a session policy. The session policy scopes them down to the specific operation and resources that the operator approved. The agent composes the session policy only from a curated list of supported AWS IAM actions that AWS DevOps Agent maintains. An action outside that list can never be part of a session policy. To browse the list, open the **Configuration** page in the AWS DevOps Agent console. Choose **View Supported Actions** in the **Agent Actions** section. You have two options for the permission policy.

**Option 1: Attach the AWS managed policy.** AWS DevOps Agent provides the `AIDevOpsAgentActionsPolicy` managed policy. Its ARN is `arn:aws:iam::aws:policy/AIDevOpsAgentActionsPolicy`. For the policy document in code format, see the AWS Managed Policy Reference Guide.

The managed policy has the following characteristics:

- It grants broad permissions: all actions, on all resources. It excludes identity, credential, and organization management services. The excluded services are `account:*`, `cognito-identity:*`, `iam:*`, `identitystore:*`, `organizations:*`, `ram:*`, `rolesanywhere:*`, `sso:*`, and `sts:*`. As a result, the role cannot manage identities or obtain further access.
- It allows a small set of read-only actions back from those services: `account:GetAccountInformation`, `account:GetGovCloudAccountInformation`, `account:GetPrimaryEmail`, `account:ListRegions`, `iam:ListRoles`, `organizations:DescribeEffectivePolicy`, `organizations:DescribeOrganization`, and `sts:DecodeAuthorizationMessage`.
- It does include delete-class actions in the ceiling. The agent itself refuses delete-class operations regardless of the role's permissions. For more information about the operations the agent refuses, see [Operations the agent will not perform](#operations-the-agent-will-not-perform "#operations-the-agent-will-not-perform").
- The policy defines only the ceiling. Effective permissions for any single action are narrowed at execution time to the approved operation.

**Option 2: Write a customer-managed policy.** If you want a tighter ceiling than the managed policy provides, write your own policy. Scope it to exactly the actions and resources you want the agent to touch, and attach it to the role. Follow the principle of least privilege: start from the operations you expect operators to approve, and expand only as needed. Directed actions the role does not permit fail at execution time even when approved.

With either option, you can further restrict what the agent can do using service control policies (SCPs) and permissions boundaries. These controls apply to the elevated role like any other role in your account. For more information about scoping the agent's access, see [Limiting Agent Access in an AWS Account](aws-devops-agent-security-limiting-agent-access-in-an-aws-account.md "aws-devops-agent-security-limiting-agent-access-in-an-aws-account.md").

### Validation lifecycle

How trust-policy validation runs depends on the account type.

- **Monitor (primary) account.** Validation is synchronous. AWS DevOps Agent validates the role when you save it. The result is available by the time the page reloads or the API call returns. `agentElevatedRoleArnStatus` reflects `valid` or `invalid` immediately.
- **Source (secondary) accounts.** Validation is asynchronous. After you register an elevated role, the following happens:

  1.  The association immediately accepts the registration and reports `agentElevatedRoleArnStatus` as `pending-confirmation`.
  2.  AWS DevOps Agent validates the role by exercising the assume-role path.
  3.  The status transitions to `valid` if validation succeeds, or `invalid` if it fails.

The role is used for directed actions only after its status is `valid`.

For source accounts, poll the association with `GetAssociation` or `ListAssociations` and check the `agentElevatedRoleArnStatus` field. Validation typically completes within a few minutes.

## Operations the agent will not perform

Independent of the permissions you grant, the agent enforces its own guardrails on the AWS SDK operations it invokes as directed actions. These guardrails apply only to actions against AWS resources. Tool classification governs third-party tools instead. For more information about tool classification, see [Categorizing tools for third-party integrations](#categorizing-tools-for-third-party-integrations "#categorizing-tools-for-third-party-integrations"). These guardrails apply even when the elevated role's policy allows the operation. Operator approval does not override them.

- **Delete resources.** The agent refuses delete-class operations, for example deleting an instance, bucket, table, function, or stack. The operator deletes resources themselves with their own credentials.
- **Mutate permissions boundaries.** The agent refuses operations that set or remove IAM permissions boundaries: `iam:PutRolePermissionsBoundary`, `iam:DeleteRolePermissionsBoundary`, `iam:PutUserPermissionsBoundary`, and `iam:DeleteUserPermissionsBoundary`. Boundaries are a control your organization uses to constrain the agent, so the agent cannot change them.
- **Require `iam:PassRole`.** By default, the agent does not support operations that pass an IAM role to an AWS service. Examples include launching an instance with an instance profile or creating a Lambda function with an execution role. Starting a task with a task role is another example. Passing a role can indirectly extend what a service does on your behalf.

When directed to perform one of these operations, the agent declines and explains why. Where it can, it describes the manual steps instead.

These guardrails complement the controls you own: the elevated role's permission policy, SCPs, and permissions boundaries on the elevated role.

## Categorizing tools for third-party integrations

Third-party and MCP integrations expose tools in three categories that gate whether the agent can invoke the tool and what approval is required. AWS DevOps Agent assigns fixed classifications for native integrations. You assign them for customer-configured MCP servers.

| Classification | Meaning                                               | Behavior                                                                          |
| -------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| `READ_ONLY`    | The tool only reads information.                      | Available as a read-only action.                                                  |
| `MUTATIVE`     | The tool can create or modify resources.              | Requires directed actions to be enabled and per-action operator approval in chat. |
| `DESTRUCTIVE`  | The tool can delete or irreversibly change resources. | The agent never invokes tools in this classification.                             |

### Customer-configured MCP servers

For MCP server associations (including the SigV4 variant), you classify tools yourself through `toolDetails`, a per-tool list of entries. Each entry has a `name` and a `toolClassification`.

- Each `name` must exactly match an entry in the association's enabled tools list. A mismatch is rejected at registration time.
- Tools without a stored classification default to `READ_ONLY`. If you register or update an MCP server association programmatically, through an AWS SDK, the AWS CLI, or a direct API call, and you do not supply `toolDetails`, AWS DevOps Agent treats every tool on that association as `READ_ONLY`. The agent runs read-only tools without requesting approval. To require operator approval before a tool that creates or modifies resources runs, classify that tool explicitly as `MUTATIVE`. The console prompts you to classify each discovered tool. Programmatic callers must set `toolDetails` themselves.
- Tool names are 1–128 characters. You can classify up to 500 tools per association.

For more information about connecting and allowlisting MCP tools, see [Connecting MCP Servers](configuring-integrations-and-knowledge-connecting-mcp-servers.md "configuring-integrations-and-knowledge-connecting-mcp-servers.md").

### Native integrations (Datadog, Grafana)

For native integrations such as Datadog and Grafana, classifications are fixed by AWS DevOps Agent. You do not supply classifications. You cannot override these classifications. Instead, you opt specific mutating tools in through `enabledElevatedTools`, a list of tool entries.

- Only tools that AWS DevOps Agent classifies as `MUTATIVE` can be enabled.
- Tools classified as `DESTRUCTIVE` (for example, `grafana_delete_alert_rule`) can never be enabled.

## Approving directed actions

Directed actions are human-in-the-loop. When the agent determines that an operation it has been directed to perform mutates a resource, it does not execute the operation directly. Instead, the following happens:

1. The agent requests approval, presenting the specific tool, operation, and target resource to the operator.
2. The operator reviews the request and approves or rejects it.
3. If approved, the agent performs the operation. Each approval covers only the specific tool, operation, and resource requested. It remains valid for a bounded time window and cannot be reused for a different operation or resource.

AWS DevOps Agent surfaces operator approval requests only in chat. If the agent invokes a mutating tool outside chat, for example during an autonomous investigation, the call fails instead of presenting an approval request. AWS DevOps Agent never executes a mutating tool without approval.

Approvals and the resulting actions are attributable to the approving operator in AWS CloudTrail.

### The approval flow in the API

- `SendMessage` streams an approval request. The request identifies the tool, operation, and target resource, with interrupt identifiers for resuming. As a running example, suppose an operator works in an AI assistant such as Claude. The operator asks it to purge the dead-letter queue `arn:aws:sqs:us-east-1:111122223333:my-app-dlq`. Claude calls `SendMessage` on AWS DevOps Agent, and the response stream carries an approval request identifying the tool `use_aws`, the operation `sqs:PurgeQueue`, and the queue ARN, along with `toolUseId`, `interruptId`, and `approvalId` identifiers.
- The operator records the decision with `UpdateApprovalAction`. The operator approves with a finalized scope or rejects with an optional reason. Here Claude surfaces the request to the operator, then calls `UpdateApprovalAction` with `action: APPROVED` and a `finalPattern` of tool `use_aws`, with `argumentPins` pinning `operation` to `sqs:PurgeQueue` and `resource_arn` to the queue ARN.
- The finalized scope can narrow the request, but it can never widen it.
- The operator marks an approval single-use, or sets a reuse window of up to 4 hours. A queue purge is a one-time operation, so the operator marks this approval single-use (`singleUse: true`, no `ttlSeconds`).
- The client resumes the paused conversation by calling `SendMessage` again with the decision attached. In this example, Claude sets `userActionResponse` to `APPROVAL_ACTION` and supplies `approvalAction` with the `toolUseId`, `interruptId`, `approvalId`, and the `APPROVED` decision. AWS DevOps Agent then purges the queue.
- The approval lifecycle is `PENDING`, then `APPROVED` (redeemable) or `REJECTED` (terminal). An `APPROVED` approval becomes `REDEEMED` after it is consumed, and it can be `REVOKED` before use. Here the request is `PENDING` while the operator decides, `APPROVED` after the decision, and `REDEEMED` after the agent purges the queue.

Any agent consumer can drive this flow the same way, whether an AI assistant such as Claude, a Slack bot, or a custom operations client: Call `SendMessage`, surface the approval request to an operator, record the decision with `UpdateApprovalAction`, and resume the conversation with `SendMessage`.

## Monitoring and auditing

- **Role validation status** – Monitor `agentElevatedRoleArnStatus` on your AWS associations (through `GetAssociation` or `ListAssociations`) to confirm elevated roles remain in the `valid` state.
- **AWS CloudTrail** – Directed actions performed in your AWS accounts appear in CloudTrail. The assumed-role session carries a source identity that attributes the action to the approving operator. You can trace every directed action back to the human who approved it.

## Troubleshooting

**A registered role stays in `pending-confirmation`.** This applies to source (secondary) accounts, where validation is asynchronous. Validation normally completes within a few minutes. If the status does not transition, verify the role exists, and re-register the role ARN to trigger validation again.

**The role status is `invalid`.** The trust policy validation failed. Check that:

- The trust policy names the AWS DevOps Agent service principal.
- The trust policy allows all required STS actions (`sts:AssumeRole`, `sts:SetSourceIdentity`, and `sts:TagSession`), not just `sts:AssumeRole`.
- The `aws:SourceAccount` condition matches the account that owns the agent space.
- The Region in the `aws:SourceArn` condition matches the agent space's Region (or uses a Region wildcard).

Fix the trust policy and re-register the role.

**Directed actions fail even though the role status is `valid`.** The `valid` status reflects the validation check at registration time. If the trust policy was changed after validation, or if its `aws:SourceArn` condition is pinned to a different Region than the agent space, the live assume-role call can still fail. Review the trust policy against the checklist above.

**`ValidationException` when registering an elevated role.** Directed actions must be enabled on the agent space before you can register elevated configuration. Enable directed actions on the agent space first, then register the role.

**Tool name mismatch errors when supplying `toolDetails`.** Each name in `toolDetails` must exactly match a tool name in the association's enabled tools list, including case. Compare the two lists, correct any mismatches, and then retry.
