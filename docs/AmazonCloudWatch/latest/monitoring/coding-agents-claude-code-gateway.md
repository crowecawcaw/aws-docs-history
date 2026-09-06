

# Set up Claude Code with the Claude apps gateway
<a name="coding-agents-claude-code-gateway"></a>

The Claude apps gateway is a self-hosted service that sits between your developers' Claude Code clients and the model provider. Developers sign in with your corporate identity provider (IdP) instead of holding API keys or cloud credentials. The gateway holds the upstream credential, enforces model access and managed settings by IdP group, and relays usage telemetry to your observability stack—including Amazon CloudWatch.

The gateway is included in the `claude` binary. The same executable that runs Claude Code runs the gateway when you pass the `gateway` subcommand with a configuration file.

## Key capabilities
<a name="coding-agents-claude-code-gateway-capabilities"></a>

The Claude apps gateway provides centralized control across several dimensions.
+ **Credentials** — The upstream API key lives only in your infrastructure. Developers authenticate through SSO with short-lived tokens.
+ **Access control** — IdP groups map to model allowlists and managed settings policies.
+ **Settings delivery** — The gateway delivers managed settings to signed-in clients.
+ **Telemetry** — Routes OTLP metrics (token counts, model, user identity, latency) to your collector. You can fan out to multiple destinations including CloudWatch, Datadog, Splunk, and ClickHouse.
+ **Upstream routing** — Clients speak the Anthropic Messages API. The gateway translates for each upstream with failover. Supported upstreams include Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry, and the Anthropic API.

## Prerequisites
<a name="coding-agents-claude-code-gateway-prereqs"></a>

Before you deploy the gateway, confirm that the following requirements are met.


| Requirement | Details | 
| --- | --- | 
| Claude Code version | v2.1.195 or later | 
| Identity provider | OpenID Connect (OIDC) provider such as Okta, Microsoft Entra ID, Google Workspace, Keycloak, or Dex | 
| Database | PostgreSQL 14 or later | 
| Model upstream | Amazon Bedrock credentials, Claude Platform on AWS, Google Cloud, Microsoft Foundry, or Anthropic API key | 
| TLS | HTTPS certificate or TLS-terminating ingress | 
| Network | Private-network address (RFC 1918, link-local, CGNAT, IPv6 ULA, or loopback) | 
| Runtime | Linux for production (macOS for local development only) | 

## Deploy the gateway
<a name="coding-agents-claude-code-gateway-quickstart"></a>

The following procedure summarizes the quickstart steps. For detailed instructions, see the [Claude apps gateway documentation](https://code.claude.com/docs/en/claude-apps-gateway).

**To deploy the Claude apps gateway**

1. Register an OAuth client in your IdP. Set the redirect URI to `https://{{claude-gateway.your-domain}}/oauth/callback`.

1. Provision a PostgreSQL database (any PostgreSQL 14 or later instance). The gateway runs schema migrations at boot.

1. Write a `gateway.yaml` configuration file. The following example shows a minimal configuration that uses Amazon Bedrock as the upstream.

   ```
   listen:
     host: 0.0.0.0
     port: 8080
     public_url: https://{{claude-gateway.internal.example.com}}
   
   oidc:
     issuer: https://{{login.example.com}}
     client_id: {{0oa1example2}}
     client_secret: ${OIDC_CLIENT_SECRET}
     allowed_email_domains: [{{example.com}}]
     userinfo_fallback: true
   
   session:
     jwt_secret: ${GATEWAY_JWT_SECRET}
     ttl_hours: 1
   
   store:
     postgres_url: ${GATEWAY_POSTGRES_URL}
   
   upstreams:
     - provider: bedrock
       region: {{us-east-1}}
       auth: {}
   
   auto_include_builtin_models: true
   ```

1. Run the gateway. You can use Docker Compose or run the binary directly.

   ```
   claude gateway --config gateway.yaml
   ```

1. Verify the authentication surface. Fetch the discovery document, request device authorization, and test browser sign-in at your gateway URL.

1. Sign in a developer to confirm end-to-end connectivity.

## Connect developers to the gateway
<a name="coding-agents-claude-code-gateway-connect"></a>

To point developer machines to your gateway, distribute the following managed settings keys through mobile device management (MDM) or your configuration management tool.

```
{
  "forceLoginMethod": "gateway",
  "forceLoginGatewayUrl": "https://{{claude-gateway.internal.example.com}}"
}
```

After you distribute the settings, each developer completes the following steps.

**To sign in through the gateway**

1. Run the `/login` command in Claude Code.

1. Press Enter on the Cloud gateway screen.

1. Complete browser sign-in with your corporate IdP.

After sign-in, Claude Code routes inference through the gateway and the gateway exports telemetry to the configured destinations.

## Route telemetry to Amazon CloudWatch
<a name="coding-agents-claude-code-gateway-telemetry"></a>

The gateway supports OTLP/HTTP fan-out to multiple collectors, with identity-stamped exports. Configure telemetry destinations in the `gateway.yaml` file. Each destination can receive metrics, logs, or traces.

When you configure CloudWatch as a telemetry destination, the gateway stamps each export with the developer's identity from the IdP. Metrics arrive with user, team, and organizational attributes, so the same Coding Agent Insights dashboards populate.

For the complete telemetry configuration options, see the [configuration reference](https://code.claude.com/docs/en/claude-apps-gateway-config).

## Availability and limitations
<a name="coding-agents-claude-code-gateway-limitations"></a>

The following table summarizes what the gateway supports and current limitations.


| Item | Status | 
| --- | --- | 
| Supported upstreams | Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry, Anthropic API | 
| Supported IdPs | Okta, Microsoft Entra ID, Google Workspace, Keycloak, Dex, and other OIDC-compliant providers | 
| Telemetry protocol | OTLP/HTTP with fan-out to multiple destinations | 
| Runtime | Linux for production deployments. macOS is supported for local development only. | 
| Minimum Claude Code version | v2.1.195 | 

## Next steps
<a name="coding-agents-claude-code-gateway-next"></a>

Use the following resources for detailed deployment instructions, configuration options, and operational guidance.
+ [Claude apps gateway documentation](https://code.claude.com/docs/en/claude-apps-gateway) — Complete setup guide including Docker Compose templates and IdP registration walkthroughs.
+ [Configuration reference](https://code.claude.com/docs/en/claude-apps-gateway-config) — Full reference for all `gateway.yaml` options including telemetry destinations, upstream routing, and access policies.
+ [Deployment guide](https://code.claude.com/docs/en/claude-apps-gateway-deploy) — Production deployment patterns, scaling, and operational best practices.

After the gateway is sending metrics to CloudWatch, view the dashboards as described in [View the dashboards](coding-agents-insights.md#coding-agents-insights-view).