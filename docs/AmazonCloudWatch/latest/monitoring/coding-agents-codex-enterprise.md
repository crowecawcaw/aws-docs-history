

# Set up OpenAI Codex for an enterprise rollout
<a name="coding-agents-codex-enterprise"></a>

Use this path when you operate Codex across a fleet of developers and want consistent, automatically attributed telemetry without distributing long-term credentials. Developers authenticate through your corporate identity provider (IdP), so identity and organizational attributes are derived from your directory rather than entered by hand. Metrics still arrive in Amazon CloudWatch with identity and organizational data carried as OTel *resource* attributes, so the same Coding Agent Insights dashboards populate.

This path supports corporate single sign-on (SSO) providers including Okta, Microsoft Entra ID (Azure AD), Auth0, and AWS IAM Identity Center.

## How it works
<a name="coding-agents-codex-enterprise-how"></a>

In an enterprise rollout, a developer's identity flows from your IdP into the telemetry that reaches CloudWatch. A typical deployment includes the following components:
+ **Identity federation** — Developers sign in through your IdP (Okta, Microsoft Entra ID, Auth0, or AWS IAM Identity Center). The IdP provides the developer's email, and organizational attributes such as department, team, and cost center.
+ **Centralized Amazon Bedrock access** — Federated developers assume a role that grants access to Amazon Bedrock for inference, so you don't distribute static model credentials.
+ **Local collector** — A per-developer OpenTelemetry collector receives metrics from Codex on `localhost`, stamps the identity and organizational resource attributes, signs requests with AWS Signature Version 4 (SigV4), and forwards them to the CloudWatch native OTLP endpoint. Because the collector signs with the developer's federated credentials, no bearer token is distributed.

## Roll out to your fleet
<a name="coding-agents-codex-enterprise-rollout"></a>

The typical end-to-end rollout follows these stages.

**To roll out Codex telemetry across your organization**

1. **Configure identity federation.** Connect your IdP to AWS IAM Identity Center (or configure OIDC federation directly), and map the directory attributes you want to attribute usage by—such as department, team, and cost center—so they are available to the rollout.

1. **Centralize Amazon Bedrock access.** Grant federated developers a role that permits the Amazon Bedrock model invocations Codex needs, scoped to the AWS Regions and models you allow.

1. **Deploy the infrastructure.** Deploy the provided AWS CloudFormation templates to create the roles, policies, and supporting resources for the fleet.

1. **Generate and distribute developer configuration.** Use the provided setup scripts to generate each developer's collector configuration. The scripts derive `user.email` and `user.id` from the federated session and populate organizational resource attributes (department, team, cost center, organization, and similar) from your IdP. They then write the rendered collector configuration and the Codex `[otel]` block that points at the local collector.

1. **Developers run Codex.** Each developer signs in through SSO, starts the local collector, and runs Codex. Metrics flow from Codex to the local collector to CloudWatch, attributed to the developer and their organization automatically.

**Note**  
On this path, identity and organizational attributes are emitted as OTel *resource* attributes, the same shape the bearer token path produces. As a result, the same Coding Agent Insights dashboards populate without additional configuration.

## Complete guidance
<a name="coding-agents-codex-enterprise-more"></a>

For the complete, continually updated guidance—including the CloudFormation templates, identity-federation setup, and fleet setup scripts—see the [guidance for Codex on Amazon Bedrock](https://github.com/openai-on-aws/guidance-codex) on GitHub. After the fleet is sending metrics, view the dashboards as described in [View the dashboards](coding-agents-insights.md#coding-agents-insights-view).