# Integrating Nova Act with Bedrock AgentCore

Amazon Bedrock AgentCore offers purpose-built infrastructure to deploy and operate production AI agents at scale. AgentCore is comprised of several modules that can be used a la carte depending on your requirements. In this guide we show an example of using each integration with Nova Act.

## AgentCore Runtime (ACR)

When you deploy a Nova Act workflow to ACR, ACR provisions an endpoint which you use to invoke the Nova Act workflow. Deploying Nova Act workflows on ACR has the added benefit of simple integrations with other AgentCore services. ACR is serverless and does not require you to maintain any infrastructure. For a step-by-step guide of deploying a Nova Act workflow to ACR, refer to [this article](https://builder.aws.com/content/32HpPjNanKLl7OZTpn48xhV0mSX/run-your-nova-act-workflow-on-amazon-bedrock-agentcore "https://builder.aws.com/content/32HpPjNanKLl7OZTpn48xhV0mSX/run-your-nova-act-workflow-on-amazon-bedrock-agentcore").

## AgentCore Identity (ACI)

ACI allows developers to provide identities for their agents, which can be used to obtain necessary access to resources and to isolate activity to specific agents. Using ACI with Nova Act enables you to securely grant permission to your workflow to access resources when needed to complete an action. A common use case for this is accessing log credentials to login to a web application. ACI also supports injecting user context from the caller which allows your Nova Act workflow to run using a user’s context.

In this example, we use a custom OAuth provider to generate access tokens for a user, and then have Nova Act use this access token to take action on behalf of the user.

First, we create a credential provider using the AWS CLI. Refer to the [Bedrock AgentCore documentation](../../../cli/latest/reference/bedrock-agentcore-control/create-oa-oauth2-credential-provider.md "../../../cli/latest/reference/bedrock-agentcore-control/create-oa-oauth2-credential-provider.md") for more details on how to create these. Below is a partial sample for a `CustomOauth2` provider:

```
aws bedrock-agentcore-control create-oauth2-credential-provider \
  --region us-east-1 \
  --name "custom-oauth-provider" \
  --credential-provider-vendor "CustomOauth2" \
  --oauth2-provider-config-input '{
  "customOauth2ProviderConfig": {
    "oauthDiscovery": {
       ...
    },
    "clientId": "string",
    "clientSecret": "string"
  }
  }'
```

AgentCore Runtime automatically handles all identity management. When your agent is deployed, the runtime provides the agent identity and user context from the caller, then injects credentials via the decorator `@requires_access_token`.

```
from bedrock_agentcore.identity.auth import requires_access_token
from nova_act_sdk import NovaAct

@requires_access_token(
    provider_name="custom-oauth-provider",
)
def automate_customer_outreach(*, access_token: str):
    with NovaAct() as browser:
        # Token automatically injected by AgentCore Runtime
        result = browser.act(f"""
        Use OAuth token {access_token} to:
        1. Log into the site
        2. Search for software engineers in Seattle
        3. Send personalized connection requests
        """)
        return result
```

## AgentCore Browser Tool (ACBT)

ACBT provides serverless infrastructure for running a browser in the cloud. ACBT supports features such as live streaming the browser session from the AgentCore AWS Console, as well as the ability for someone to take over the browser for a period of time. Common examples of this include solving a CAPTCHA, or entering sensitive data, before returning control back to the Nova Act workflow. For an example of running Nova Act with ACBT, refer to [this article](https://builder.aws.com/content/32HpPjNanKLl7OZTpn48xhV0mSX/run-your-nova-act-workflow-on-amazon-bedrock-agentcore "https://builder.aws.com/content/32HpPjNanKLl7OZTpn48xhV0mSX/run-your-nova-act-workflow-on-amazon-bedrock-agentcore").

## AgentCore Observability (ACO)

ACO allows developers to instrument and emit OpenTelemetry Data from a Nova Act workflow. You can instrument the Nova Act SDK with OTEL for compatibility with the Observability dashboard.

To do this, follow these steps:

- Install the open telemetry library: `pip install aws-opentelemetry-distro`
- Import the library in the Nova Act code: `from opentelemetry import baggage, context`
- Obtain your session ID from your active Nova Act workflow, and pass this into your OTEL session context.

Here is an example of instrumenting a Nova Act workflow and writing the telemetry data to CloudWatch logs:

```
import uuid
import os
import boto3
import logging
import argparse
from opentelemetry import baggage, context
from nova_act import NovaAct

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_agentcore_observability(agent_id):
    """Setup AgentCore observability environment and create log groups"""
    agent_name = "nova-act-browser"
    log_group = "/aws/bedrock-agentcore/runtimes/nova-act-poc"

    # Create CloudWatch log group and stream
    logs_client = boto3.client('logs')
    try:
        logs_client.create_log_group(logGroupName=log_group)
        logger.info(f"Created log group: {log_group}")
    except logs_client.exceptions.ResourceAlreadyExistsException:
        logger.info(f"Log group already exists: {log_group}")

    # Create log stream
    log_stream = "runtime-logs"
    try:
        logs_client.create_log_stream(logGroupName=log_group, logStreamName=log_stream)
        logger.info(f"Created log stream: {log_stream}")
    except logs_client.exceptions.ResourceAlreadyExistsException:
        logger.info(f"Log stream already exists: {log_stream}")

    # Write AgentCore environment variables to .env file
    # Note that you can export these via the command line when running the script
    env_vars = {
        "AGENT_OBSERVABILITY_ENABLED": "true",
        "OTEL_PYTHON_DISTRO": "aws_distro",
        "OTEL_PYTHON_CONFIGURATOR": "aws_configurator",
        "OTEL_RESOURCE_ATTRIBUTES": f"service.name={agent_name},aws.log.group.names={log_group}",
        "OTEL_EXPORTER_OTLP_LOGS_HEADERS": f"x-aws-log-group={log_group},x-aws-log-stream=runtime-logs,x-aws-metric-namespace=bedrock-agentcore",
        "OTEL_EXPORTER_OTLP_LOGS_PROTOCOL": "http/protobuf",
        "OTEL_LOGS_EXPORTER": "otlp",
        "OTEL_TRACES_EXPORTER": "otlp"
    }

    with open('.env', 'w') as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")
    logger.info("Created .env file with AgentCore observability settings")

def set_session_context(session_id):
    """Set the session ID in OpenTelemetry baggage for trace correlation"""
    ctx = baggage.set_baggage("session.id", session_id)
    token = context.attach(ctx)
    logging.info(f"Session ID '{session_id}' attached to telemetry context")
    return token

def main():
    # Generate agent ID and session ID
    agent_id = str(uuid.uuid4())[:8]

    setup_agentcore_observability(agent_id)

    # Execute Nova Act - ADOT auto-instrumentation handles the rest
    client = NovaAct(starting_page="https://nova.amazon.com/act")
    client.start()

    # Set session context for trace correlation
    session_id = client.get_session_id()
    context_token = set_session_context(session_id)

    try:
        result = client.act("Click Learn More")
        logger.info(f"Agent ID: {agent_id}")
        logger.info(f"Session ID: {session_id}")
        logger.info(f"Success: {result}")
    finally:
        client.stop()
        # Detach context when done
        context.detach(context_token)
        logger.info(f"Session context for '{session_id}' detached")

if __name__ == "__main__":
    main()
```

## AgentCore Gateway (ACG)

ACG provides an easy and secure way for developers to build, deploy, discover, and connect to tools at scale. Nova Act integrates with ACG in two ways.

- Nova Act workflows can connect to an existing Gateway for agentic tool use.
- Nova Act workflows themselves can be exposed on the Gateway as a tool for other agents to use. Refer to the [ACG developer guide](../../../bedrock-agentcore/latest/devguide/gateway-quick-start.md "../../../bedrock-agentcore/latest/devguide/gateway-quick-start.md") for help on getting started.
